# Azure Data Projects Portfolio

A collection of 5 end-to-end Azure data projects, all built around the same e-commerce dataset (Olist Brazilian E-Commerce), covering the full data lifecycle: **ingest → process → model → predict → govern**.

Each project lives in its own folder below with a full README, architecture diagram, code, and dashboard/demo assets.

---

## 📁 Projects

| # | Project | What it demonstrates | Key tech |
|---|---|---|---|
| 1 | [**Batch Analytics Pipeline**](./azure-ecommerce-analytics-pipeline) | ETL orchestration, medallion architecture, EDA, BI dashboarding | ADF, Synapse Serverless SQL, Power BI |
| 2 | [**Real-Time Streaming Pipeline**](./azure-ecommerce-streaming-pipeline) | Event-driven architecture, stream processing, live dashboards | Event Hubs, Stream Analytics, Power BI |
| 3 | [**Dimensional Data Warehouse**](./azure-ecommerce-dimensional-warehouse) | Relational modeling, star schema design, SQL, indexing | Azure SQL Database, T-SQL, Power BI |
| 4 | [**Demand Forecasting**](./azure-ecommerce-demand-forecasting) | Machine learning, AutoML, time-series analysis | Azure Machine Learning, AutoML, ARIMAX |
| 5 | [**Data Quality & Governance**](./azure-ecommerce-data-governance) | Data cataloging, classification, automated validation | Microsoft Purview, Great Expectations |

---

## 🧭 The Story

Rather than five unrelated exercises, these projects are designed to read as one coherent body of work — each one tackles a different stage of a real data platform, using the same underlying dataset so the outputs of one naturally inform the next:

```
                     ┌─────────────────────────────┐
                     │   Olist E-Commerce Dataset   │
                     └──────────────┬──────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
 1. Batch Pipeline           2. Streaming Pipeline        (shared raw data)
 (ADF + Synapse)             (Event Hubs + ASA)                  │
        │                           │                           │
        └─────────────┬─────────────┘                           │
                       │                                        │
              3. Dimensional Warehouse                          │
                 (Azure SQL Database)                            │
                       │                                        │
              4. Demand Forecasting                              │
                 (Azure ML AutoML)                                │
                       │                                        │
              5. Data Quality & Governance  ◄─────────────────────┘
                 (Purview + Great Expectations)
```

- **Projects 1 & 2** show two different processing paradigms — batch vs. real-time — on the same domain.
- **Project 3** takes the same data and asks a different question: is it modeled the way a BI team would actually want it, with proper relationships and indexing?
- **Project 4** moves from descriptive to predictive — from "what happened" to "what's next."
- **Project 5** sits on top of all of it, asking whether any of this data can be trusted and governed at scale.

---

## 🛠️ Full Tech Stack Across All Projects

| Category | Services / Tools Used |
|---|---|
| **Storage** | Azure Data Lake Storage Gen2 |
| **Orchestration** | Azure Data Factory |
| **Querying / Warehousing** | Azure Synapse Analytics (Serverless SQL), Azure SQL Database |
| **Streaming** | Azure Event Hubs, Azure Stream Analytics |
| **Machine Learning** | Azure Machine Learning, AutoML |
| **Governance** | Microsoft Purview, Great Expectations |
| **Visualization** | Power BI (batch, dimensional, and live streaming reports) |
| **Languages** | Python (pandas, SQLAlchemy, azure-eventhub), T-SQL, Bash |

---

## 🔗 Live Repos

- [azure-ecommerce-analytics-pipeline](https://github.com/shijithpulikkal/azure-ecommerce-analytics-pipeline)
- [azure-ecommerce-streaming-pipeline](https://github.com/shijithpulikkal/azure-ecommerce-streaming-pipeline)
- [azure-ecommerce-dimensional-warehouse](https://github.com/shijithpulikkal/azure-ecommerce-dimensional-warehouse)
- [azure-ecommerce-demand-forecasting](https://github.com/shijithpulikkal/azure-ecommerce-demand-forecasting)
- [azure-ecommerce-data-governance](https://github.com/shijithpulikkal/azure-ecommerce-data-governance)

---

## 📊 Highlighted Results

- **Demand Forecasting:** AutoML-selected ARIMAX model achieved **R² of 0.96** and **MAPE of 18.9%** predicting daily revenue 30 days ahead.
- **Data Quality:** 5/5 automated Great Expectations checks passed against **112,650 rows** of curated sales data.
- **Governance:** Microsoft Purview automatically classified sensitive/location columns across the data lake — and caught a real classifier mislabel in the process (a Brazilian zip code column tagged as "U.S. Zip Codes"), a useful reminder that automated classification still needs human review.

---

## 📂 Repo Structure

```
Azure Projects/
├── README.md                                  ← you are here
├── azure-ecommerce-analytics-pipeline/
├── azure-ecommerce-streaming-pipeline/
├── azure-ecommerce-dimensional-warehouse/
├── azure-ecommerce-demand-forecasting/
└── azure-ecommerce-data-governance/
```

Each subfolder is self-contained with its own README, architecture diagram, scripts/notebooks, SQL, and dashboard assets — open any one directly for full details on that project.

---

## 👤 About

Built by [Shijith Pulikkal](https://github.com/shijithpulikkal) as a hands-on portfolio covering the Azure data platform end to end. Feedback and suggestions welcome — feel free to open an issue or reach out.
