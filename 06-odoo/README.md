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

1. Can Odoo handle 2.8M POS transactions/month across 600 terminals at acceptable performance?
2. How robust is Odoo's offline POS mode for extended outages?
3. Does Odoo have a certified Philippine payroll/BIR localization, or does it require custom development?
4. How does multi-entity (5 companies) consolidation work in Odoo?
5. What is the scaling strategy (multi-server, database sharding) for this volume?
6. Can Odoo handle 600,000+ customer records and 55,000 SKUs performantly?

---

## Scorecard Template

> To be completed during evaluation. See [Scoring Methodology](../07-methodology/scoring-methodology.md) for full details.

### Dimension Scores

| Dimension | Score (1–5) | Weight | Weighted Score | Notes |
|---|---|---|---|---|
| Functional Fit | — | 40% | — | See odoo-fit-gap.md |
| TCO (5-year) | — | 20% | — | See odoo-cost-estimate.md |
| Implementation Risk | — | 15% | — | |
| Scalability & Performance | — | 15% | — | |
| Local Support Ecosystem | — | 10% | — | |
| **Overall** | | **100%** | **—** | |

### Fit-Gap Summary (by Requirement Category)

| Category | Must Have Count | Met (4-3) | Partial (2-1) | Gap (0) | Notes |
|---|---|---|---|---|---|
| FIN (Financial Management) | 15 | — | — | — | |
| INV (Inventory Management) | 12 | — | — | — | |
| PUR (Procurement) | 10 | — | — | — | |
| WMS (Warehouse Management) | 5 | — | — | — | |
| POS (Point of Sale) | 13 | — | — | — | |
| ECOM (Ecommerce Integration) | 9 | — | — | — | |
| SCP (Supply Chain Planning) | 3 | — | — | — | |
| HR (HR & Payroll) | 8 | — | — | — | |
| CRM (CRM & Loyalty) | 5 | — | — | — | |
| RPT (Analytics & Reporting) | 5 | — | — | — | |
| IC (Intercompany) | 5 | — | — | — | |
| DOC (Document Management) | 4 | — | — | — | |
| MDM (Master Data Management) | 5 | — | — | — | |
| NFR (Non-Functional Requirements) | 11 | — | — | — | |
| **Total** | **~110 Must Have** | — | — | — | |

### Disqualifiers / Red Flags
- [List any Must Have requirements scored 0 or 1]

### Top Strengths
1.
2.
3.

### Top Gaps / Risks
1.
2.
3.

### Recommendation
[Proceed / Conditional / Eliminate] — with rationale

---

*Date created: 2026-05-30*
