# SAP ERP Evaluation — BuildRight Depot Corp.

> This folder contains the SAP-specific evaluation for the BuildRight Depot model company.

## Status: Not Started

## Contents (to be created)

| Document | Purpose |
|---|---|
| `sap-fit-gap.md` | Requirement-by-requirement fit/gap analysis against [ERP Requirements](../01-model-company/erp-requirements.md) |
| `sap-architecture.md` | Proposed SAP solution architecture (S/4HANA Cloud, BTP, POS integration) |
| `sap-cost-estimate.md` | Licensing, implementation, and 5-year TCO estimate |
| `sap-localization.md` | Philippine localization assessment (BIR, statutory, VAT) |
| `sap-scorecard.md` | Scored evaluation per the [Scoring Methodology](../07-methodology/scoring-methodology.md) |

## Products in Scope

| Product | Role |
|---|---|
| SAP S/4HANA Cloud (public or private) | Core ERP |
| SAP BTP (Business Technology Platform) | Integration, extensions |
| SAP Customer Checkout | POS (evaluate vs. third-party) |
| SAP Integrated Business Planning (IBP) | Supply chain planning |
| SAP SuccessFactors | HR & payroll (evaluate Philippine payroll capability) |
| SAP Commerce Cloud | Ecommerce (evaluate vs. third-party) |

## Key Evaluation Questions

1. Can S/4HANA Cloud handle 2.8M POS transactions/month across 1,000 terminals?
2. How mature is the Philippine localization (BIR forms, VAT, statutory deductions)?
3. What is the offline POS strategy (SAP Customer Checkout offline mode)?
4. How does the 5-entity intercompany consolidation work in S/4HANA Cloud?
5. What is the total cost for 1,000 POS users + 8,050 total users?

---

## Scorecard Template

> To be completed during evaluation. See [Scoring Methodology](../07-methodology/scoring-methodology.md) for full details.

### Dimension Scores

| Dimension | Score (1–5) | Weight | Weighted Score | Notes |
|---|---|---|---|---|
| Functional Fit | — | 40% | — | See sap-fit-gap.md |
| TCO (5-year) | — | 20% | — | See sap-cost-estimate.md |
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
