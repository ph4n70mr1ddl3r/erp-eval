# Oracle NetSuite Evaluation — BuildRight Depot Corp.

> This folder contains the Oracle NetSuite-specific evaluation for the BuildRight Depot model company.

## Status: Not Started

## Contents (to be created)

| Document | Purpose |
|---|---|
| `netsuite-fit-gap.md` | Requirement-by-requirement fit/gap analysis against [ERP Requirements](../01-model-company/erp-requirements.md) |
| `netsuite-architecture.md` | Proposed NetSuite solution architecture (SuiteCommerce, POS integration, WMS) |
| `netsuite-cost-estimate.md` | Licensing, implementation, and 5-year TCO estimate |
| `netsuite-localization.md` | Philippine localization assessment (BIR, statutory, VAT) |
| `netsuite-scorecard.md` | Scored evaluation per the [Scoring Methodology](../07-methodology/scoring-methodology.md) |

## Products in Scope

| Product | Role |
|---|---|
| Oracle NetSuite ERP | Core ERP |
| NetSuite SuiteCommerce | Ecommerce |
| NetSuite WMS | Warehouse management |
| NetSuite SRP | Supply chain planning (evaluate capability) |
| Oracle HCM NetSuite | HR & payroll (evaluate Philippine payroll) |
| Third-party POS | POS integration (NetSuite does not have native POS) |

## Key Evaluation Questions

1. Can NetSuite handle 2.8M POS transactions/month, or does it require a middleware/aggregation layer?
2. How does offline POS work when NetSuite is cloud-only?
3. How mature is the Philippine SuiteTax / localization module?
4. Can SuiteCommerce handle BOPIS with real-time per-store inventory?
5. What are the concurrent user licensing implications for 600 POS terminals?

---

## Scorecard Template

> To be completed during evaluation. See [Scoring Methodology](../07-methodology/scoring-methodology.md) for full details.

### Dimension Scores

| Dimension | Score (1–5) | Weight | Weighted Score | Notes |
|---|---|---|---|---|
| Functional Fit | — | 40% | — | See netsuite-fit-gap.md |
| TCO (5-year) | — | 20% | — | See netsuite-cost-estimate.md |
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
