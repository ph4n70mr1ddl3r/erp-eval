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
5. What are the concurrent user licensing implications for 1,000 POS terminals?

---

*Date created: 2026-05-30*
