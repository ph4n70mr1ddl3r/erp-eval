# ERP Plans — Model Company & System Architecture

## Purpose

This repository contains ERP implementation plans for a theoretical retail company (the **"Model Company"**). The model company's complete business profile, requirements, and specifications live here at the root level. Each subfolder contains the design and architecture for a specific ERP product to handle this model company.

## Folder Structure

```
erpplans/
├── README.md                    ← You are here
├── 01-model-company/            ← Complete model company profile & requirements
├── 02-wilcon-benchmark/         ← Real-world Wilcon Depot research & comparison
└── (erp subfolders to follow)   ← e.g., sap/, oracle-netsuite/, odoo/, microsoft-d365/, etc.
```

## The Model Company at a Glance

| Parameter | Value |
|---|---|
| Company Name | **BuildRight Depot Corp.** (theoretical) |
| Format | Hardware / DIY / Home Improvement Big Box |
| Stores | 200 |
| Distribution Centers | 4 |
| Corporate HQ | Davao City, Philippines |
| POS Machines per Store | 3 |
| Monthly POS Transactions per Store | 10,000 |
| Avg Lines per Transaction | 4 |
| Staff per Store | ~30 |
| Active SKUs | 20,000 |
| Monthly Trade Purchase Orders | 1,000 |
| Legal Entities | 5 |
| Ecommerce | Yes (with BOPIS) |
| Country | Philippines |

## Inspiration

This model company is heavily inspired by **Wilcon Depot** (PSE: WLCON), the Philippines' largest home improvement and construction supply retail chain. See `02-wilcon-benchmark/` for detailed real-world research.
