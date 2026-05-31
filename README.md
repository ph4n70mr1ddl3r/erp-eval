# ERP Plans — Model Company & System Architecture

## Purpose

This repository contains ERP implementation plans for a theoretical retail company (the **"Model Company"**). The model company's complete business profile, requirements, and specifications live here at the root level. Each subfolder contains the design and architecture for a specific ERP product to handle this model company.

## Folder Structure

```
erpplans/
├── README.md                    ← You are here
├── 01-model-company/            ← Complete model company profile, requirements & workflows
│   ├── model-company-profile.md       Company profile, operations, financials
│   ├── erp-requirements.md            ~200 requirements across 14 categories
│   ├── data-volumes-and-integrations.md  Transaction volumes, integration map
│   ├── operational-workflows.md        79 detailed workflows (W1–W79)
│   ├── executive-summary.md            1-page C-suite overview
│   ├── assumptions-and-design-decisions.md  Consolidated assumptions & rationale
│   ├── requirement-workflow-matrix.md  Cross-reference: requirements ↔ workflows
│   ├── internal-controls-matrix.md     43 internal controls by objective
│   ├── mobile-app-strategy.md          Customer & employee mobile app strategy
│   └── data-migration-mapping.md       Data migration field mapping templates
├── 02-wilcon-benchmark/         ← Real-world Wilcon Depot research & comparison
├── 03-sap/                      ← SAP S/4HANA evaluation (placeholder)
├── 04-oracle-netsuite/          ← Oracle NetSuite evaluation (placeholder)
├── 05-microsoft-d365/           ← Microsoft Dynamics 365 evaluation (placeholder)
├── 06-odoo/                     ← Odoo evaluation (placeholder)
├── 07-methodology/              ← Scoring methodology, implementation roadmap, technical guidelines
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
| Monthly Trade Purchase Orders | ~1,200 merchandise; ~1,400–1,600 total |
| Legal Entities | 5 |
| Total Headcount | ~8,060 (200 stores × 35 + ~750 DC + ~310 HQ) |
| Ecommerce | Yes (with BOPIS) |
| Country | Philippines |

## Inspiration

This model company is heavily inspired by **Wilcon Depot** (PSE: WLCON), the Philippines' largest home improvement and construction supply retail chain. See `02-wilcon-benchmark/` for detailed real-world research.
