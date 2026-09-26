"""
upload_raw_data.py

Uploads the raw Olist e-commerce CSVs into the `raw/ecommerce` path of the
ADLS Gen2 storage account for the Azure E-Commerce Analytics Pipeline project.

Prerequisites:
    pip install azure-identity azure-storage-blob

    - Azure CLI installed and logged in (`az login`), OR any credential
      supported by DefaultAzureCredential (env vars, managed identity, etc.)
    - Your account has the "Storage Blob Data Contributor" role on the
      storage account
    - Dataset downloaded from:
      https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Usage:
    python upload_raw_data.py --account stecommercedlspl --source ./ecommerce-data

    python upload_raw_data.py --account stecommercedlspl --source ./ecommerce-data \
        --container raw --dest-path ecommerce
"""

import argparse
import sys
from pathlib import Path

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError, ResourceNotFoundError, HttpResponseError


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Upload raw Olist e-commerce CSVs to Azure Data Lake Storage Gen2."
    )
    parser.add_argument(
        "--account",
        required=True,
        help="Storage account name, e.g. stecommercedlspl",
    )
    parser.add_argument(
        "--source",
        default="./ecommerce-data",
        help="Local folder containing the Olist CSV files (default: ./ecommerce-data)",
    )
    parser.add_argument(
        "--container",
        default="raw",
        help="Target container name (default: raw)",
    )
    parser.add_argument(
        "--dest-path",
        default="ecommerce",
        help="Destination folder path inside the container (default: ecommerce)",
    )
    parser.add_argument(
        "--pattern",
        default="*.csv",
        help="Glob pattern for files to upload (default: *.csv)",
    )
    return parser.parse_args()


def get_container_client(account_name: str, container_name: str):
    account_url = f"https://{account_name}.blob.core.windows.net"
    credential = DefaultAzureCredential()
    blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

    container_client = blob_service_client.get_container_client(container_name)
    try:
        container_client.get_container_properties()
        print(f"✅ Container '{container_name}' found.")
    except ResourceNotFoundError:
        print(f"ℹ️  Container '{container_name}' not found — creating it.")
        try:
            container_client.create_container()
        except ResourceExistsError:
            pass  # race condition safeguard

    return container_client


def upload_files(container_client, source_dir: Path, dest_path: str, pattern: str) -> None:
    files = sorted(source_dir.glob(pattern))

    if not files:
        print(f"❌ No files matching '{pattern}' found in '{source_dir}'.")
        sys.exit(1)

    print(f"⬆️  Uploading {len(files)} file(s) from '{source_dir}' to "
          f"'{container_client.container_name}/{dest_path}'...\n")

    for file_path in files:
        blob_name = f"{dest_path}/{file_path.name}" if dest_path else file_path.name
        print(f"   {file_path.name} -> {blob_name}")

        with open(file_path, "rb") as data:
            try:
                container_client.upload_blob(
                    name=blob_name,
                    data=data,
                    overwrite=True,
                )
            except HttpResponseError as e:
                print(f"   ❌ Failed to upload {file_path.name}: {e.message}")
                continue

    print("\n✅ Upload complete.")


def main() -> None:
    args = parse_args()

    source_dir = Path(args.source)
    if not source_dir.is_dir():
        print(f"❌ Local data folder '{source_dir}' does not exist.")
        print("   Download the Olist dataset from Kaggle and place the CSVs there first.")
        sys.exit(1)

    print(f"🔎 Connecting to storage account '{args.account}'...")
    container_client = get_container_client(args.account, args.container)

    upload_files(container_client, source_dir, args.dest_path, args.pattern)

    print(
        f"\nVerify with:\n"
        f"  az storage blob list --account-name {args.account} "
        f"--container-name {args.container} --prefix {args.dest_path} "
        f"--auth-mode login --output table"
    )


if __name__ == "__main__":
    main()
