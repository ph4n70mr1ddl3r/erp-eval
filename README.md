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
│   ├── workflows/                      276 workflows organized by functional domain
│   │   ├── README.md                         Workflow index & format guide
│   │   ├── WF-merchandising.md               W1, W13, W27, W40, W50, W63, W64, W68, W93, W97, W102, W107
│   │   ├── WF-procurement.md                 W2, W20, W36, W38, W44, W60, W62, W88, W110, W115
│   │   ├── WF-warehouse.md                   W3, W46, W52, W66, W106
│   │   ├── WF-inventory.md                   W4, W6, W22, W23, W42, W56, W57, W91, W92, W105
│   │   ├── WF-store-operations.md            W5, W12, W16, W17, W18, W28, W29, W33, W45, W47, W67, W69, W71, W75, W86, W96, W109, W111
│   │   ├── WF-ecommerce.md                   W11, W19, W98
│   │   ├── WF-finance.md                     W7, W8, W9, W14, W21, W24, W25, W26, W30, W35, W39, W59, W70, W80, W81, W85, W89, W90, W94, W99, W100, W101, W108
│   │   ├── WF-hr.md                          W10, W15, W34, W43, W51, W72, W74, W76
│   │   ├── WF-supply-chain.md                W31, W32
│   │   ├── WF-customer.md                    W41, W58, W61, W65, W84, W87, W103, W112
│   │   ├── WF-it-operations.md               W48, W53, W55, W73, W113
│   │   ├── WF-compliance.md                  W37, W49, W54, W77, W78, W79, W82, W95, W114
│   │   ├── WF-marketing.md                   W83, W104
│   │   └── workflow-system-touchpoint-map.md  ERP module-to-workflow cross-reference
│   ├── executive-summary.md            1-page C-suite overview
│   ├── assumptions-and-design-decisions.md  Consolidated assumptions & rationale
│   ├── requirement-workflow-matrix.md  Cross-reference: requirements ↔ workflows
│   ├── internal-controls-matrix.md     43 internal controls by objective
│   ├── mobile-app-strategy.md          Customer & employee mobile app strategy
│   └── data-migration-mapping.md       Data migration field mapping templates
├── 02-wilcon-benchmark/         ← Real-world Wilcon Depot research & comparison
├── 03-sap/                      ← SAP S/4HANA evaluation (placeholder)
├── 04-oracle-netsuite/          ← Oracle NetSuite evaluation (placeholder)
├── 04-oracle-fusion/            ← Oracle Fusion Cloud evaluation (placeholder)
├── 05-microsoft-d365/           ← Microsoft Dynamics 365 evaluation (placeholder)
├── 06-odoo/                     ← Odoo evaluation (placeholder)
├── 07-methodology/              ← Scoring methodology, implementation roadmap, technical guidelines
├── 08-erp-comparison/           ← Side-by-side ERP comparison matrix
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
| Monthly POS Transactions per Store | 14,000 |
| Avg Lines per Transaction | 4 |
| Staff per Store | ~28 |
| Active SKUs | 35,000 |
| Monthly Trade Purchase Orders | ~1,200 merchandise; ~1,400–1,600 total |
| Legal Entities | 5 |
| Total Headcount | ~6,510 (200 stores × 28 + ~600 DC + ~310 HQ) |
| Ecommerce | Yes (with BOPIS) |
| Country | Philippines |

## Inspiration

This model company is heavily inspired by **Wilcon Depot** (PSE: WLCON), the Philippines' largest home improvement and construction supply retail chain. See `02-wilcon-benchmark/` for detailed real-world research.
