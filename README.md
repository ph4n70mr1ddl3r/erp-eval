# ERP Plans — Model Company & System Architecture

## Purpose

This repository contains ERP implementation plans for a theoretical retail company (the **"Model Company"**). The model company's complete business profile, requirements, and specifications live here at the root level. Each subfolder contains the design and architecture for a specific ERP product to handle this model company.

## Folder Structure

```
erpplans/
├── README.md                    ← You are here
├── 01-model-company/            ← Complete model company profile & requirements
├── 02-wilcon-benchmark/         ← Real-world Wilcon Depot research & comparison
├── 03-sap/                      ← SAP S/4HANA evaluation (placeholder)
├── 04-oracle-netsuite/          ← Oracle NetSuite evaluation (placeholder)
├── 05-microsoft-d365/           ← Microsoft Dynamics 365 evaluation (placeholder)
├── 06-odoo/                     ← Odoo evaluation (placeholder)
└── 07-methodology/              ← Scoring methodology & implementation roadmap
```

## The Model Company at a Glance

| Parameter | Value |
|---|---|
| Company Name | **BuildRight Depot Corp.** (theoretical) |
| Format | Hardware / DIY / Home Improvement Big Box |
| Stores | 200 |
| Distribution Centers | 5 |
| Corporate HQ | Davao City, Philippines |
| POS Machines per Store | 5 |
| Monthly POS Transactions per Store | 14,000 |
| Avg Lines per Transaction | 4 |
| Staff per Store | ~35 |
| Active SKUs | 35,000 |
| Monthly Trade Purchase Orders | 1,200 |
| Legal Entities | 5 |
| Ecommerce | Yes (with BOPIS) |
| Country | Philippines |

## Inspiration

This model company is heavily inspired by **Wilcon Depot** (PSE: WLCON), the Philippines' largest home improvement and construction supply retail chain. See `02-wilcon-benchmark/` for detailed real-world research.
