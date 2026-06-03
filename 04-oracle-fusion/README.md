# Oracle Fusion Cloud Evaluation — BuildRight Depot Corp.

> This folder contains the Oracle Fusion Cloud-specific evaluation for the BuildRight Depot model company.

## Status: Not Started

## Contents (to be created)

| Document | Purpose |
|---|---|
| `fusion-fit-gap.md` | Requirement-by-requirement fit/gap analysis against [ERP Requirements](../01-model-company/erp-requirements.md) |
| `fusion-architecture.md` | Proposed Fusion Cloud solution architecture (ERP, SCM, HCM, CX, WMS) |
| `fusion-cost-estimate.md` | Licensing, implementation, and 5-year TCO estimate |
| `fusion-localization.md` | Philippine localization assessment (BIR, statutory, VAT) |
| `fusion-scorecard.md` | Scoreed evaluation per the [Scoring Methodology](../07-methodology/scoring-methodology.md) |

## Products in Scope

| Product | Role |
|---|---|
| Oracle Fusion Cloud ERP | Core financials (GL, AP, AR, FA, consolidation) |
| Oracle Fusion Cloud SCM | Inventory, procurement, order management, logistics |
| Oracle Fusion Cloud HCM | HR, payroll, talent, time & labor |
| Oracle Fusion Cloud CX | CRM, sales, loyalty, service, marketing |
| Oracle Fusion Cloud EPM | Planning, budgeting, consolidation, reporting |
| Oracle Warehouse Management Cloud | Warehouse operations (LogFire) |
| Oracle Commerce Cloud | Ecommerce (evaluate vs. third-party) |
| Oracle Integration Cloud | Middleware and integration |
| Third-party POS | POS (Oracle Retail Xstore or third-party) |

## Key Evaluation Questions

1. How does Oracle Fusion handle 600 POS terminals without a native POS solution?
2. What is the offline POS strategy — can Oracle Retail Xstore integrate with Fusion Cloud SCM?
3. How mature is the Philippine localization for BIR forms, VAT, and statutory deductions?
4. Can Oracle WMS Cloud handle catch-weight items (lumber, wire)?
5. What is the integration overhead between Fusion Cloud ERP, SCM, HCM, and CX modules?

---

## Scorecard Template

> To be completed during evaluation. See [Scoring Methodology](../07-methodology/scoring-methodology.md) for full details.

### Dimension Scores

| Dimension | Score (1–5) | Weight | Weighted Score | Notes |
|---|---|---|---|---|
| Functional Fit | — | 40% | — | See fusion-fit-gap.md |
| TCO (5-year) | — | 20% | — | See fusion-cost-estimate.md |
| Implementation Risk | — | 15% | — | |
| Scalability & Performance | — | 15% | — | |
| Local Support Ecosystem | — | 10% | — | |
| **Overall** | | **100%** | **—** | |

### Fit-Gap Summary (by Requirement Category)

| Category | Must Have Count | Met (4-3) | Partial (2-1) | Gap (0) | Notes |
|---|---|---|---|---|---|
| FIN (Financial Management) | 22 | — | — | — | |
| INV (Inventory Management) | 12 | — | — | — | |
| PUR (Procurement) | 12 | — | — | — | |
| WMS (Warehouse Management) | 5 | — | — | — | |
| POS (Point of Sale) | 17 | — | — | — | **Major gap: no native POS** |
| ECOM (Ecommerce Integration) | 9 | — | — | — | |
| SCP (Supply Chain Planning) | 3 | — | — | — | |
| HR (HR & Payroll) | 11 | — | — | — | |
| CRM (CRM & Loyalty) | 5 | — | — | — | |
| RPT (Analytics & Reporting) | 5 | — | — | — | |
| IC (Intercompany) | 5 | — | — | — | |
| DOC (Document Management) | 5 | — | — | — | |
| MDM (Master Data Management) | 5 | — | — | — | |
| NFR (Non-Functional Requirements) | 14 | — | — | — | |
| **Total** | **~130 Must Have** | — | — | — | |

### Disqualifiers / Red Flags
- **No native POS** — must integrate Oracle Retail Xstore or third-party POS for 600 terminals
- **Offline POS capability** — dependent on third-party POS solution
- **Philippine localization** — BIR tax forms, statutory deductions require partner add-ons

### Top Strengths
1. Strong enterprise financials and consolidation (EPM)
2. Comprehensive HCM suite with Oracle HCM Cloud
3. Scalable OCI cloud infrastructure

### Top Gaps / Risks
1. No native retail POS — major gap for 200-store retail
2. Fragmented cloud modules require extensive integration (ERP ↔ SCM ↔ CX ↔ WMS Cloud)
3. Philippine localization ecosystem smaller than SAP/D365

### Recommendation
**Conditional** — Strong ERP foundation but requires Oracle Retail Xstore (or equivalent) for POS. Only viable if Oracle can demonstrate a proven retail POS + Fusion Cloud integration at scale.

---

*Date created: 2026-06-03*
