# Odoo Evaluation — BuildRight Depot Corp.

> This folder contains the Odoo-specific evaluation for the BuildRight Depot model company.

## Status: Not Started

## Contents (to be created)

| Document | Purpose |
|---|---|
| `odoo-fit-gap.md` | Requirement-by-requirement fit/gap analysis against [ERP Requirements](../01-model-company/erp-requirements.md) |
| `odoo-architecture.md` | Proposed Odoo solution architecture (modules, POS, hosting) |
| `odoo-cost-estimate.md` | Licensing, implementation, and 5-year TCO estimate |
| `odoo-localization.md` | Philippine localization assessment (BIR, statutory, VAT) |
| `odoo-scorecard.md` | Scored evaluation per the [Scoring Methodology](../07-methodology/scoring-methodology.md) |

## Products in Scope

| Product | Role |
|---|---|
| Odoo Enterprise (all relevant modules) | Core ERP |
| Odoo Point of Sale | POS (built-in; evaluate offline capability) |
| Odoo Website / eCommerce | Ecommerce |
| Odoo Inventory / Warehouse | Inventory & WMS |
| Odoo Purchase | Procurement |
| Odoo Accounting | Finance (evaluate Philippine localization) |
| Odoo HR / Payroll | HR & payroll (evaluate Philippine statutory compliance) |

## Key Evaluation Questions

1. Can Odoo handle 2.8M POS transactions/month across 1,000 terminals at acceptable performance?
2. How robust is Odoo's offline POS mode for extended outages?
3. Does Odoo have a certified Philippine payroll/BIR localization, or does it require custom development?
4. How does multi-entity (5 companies) consolidation work in Odoo?
5. What is the scaling strategy (multi-server, database sharding) for this volume?
6. Can Odoo handle 600,000+ customer records and 55,000 SKUs performantly?

---

*Date created: 2026-05-30*
