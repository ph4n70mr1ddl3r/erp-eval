# Microsoft Dynamics 365 Evaluation — BuildRight Depot Corp.

> This folder contains the Microsoft Dynamics 365-specific evaluation for the BuildRight Depot model company.

## Status: Not Started

## Contents (to be created)

| Document | Purpose |
|---|---|
| `d365-fit-gap.md` | Requirement-by-requirement fit/gap analysis against [ERP Requirements](../01-model-company/erp-requirements.md) |
| `d365-architecture.md` | Proposed D365 solution architecture (Commerce, Supply Chain, Finance) |
| `d365-cost-estimate.md` | Licensing, implementation, and 5-year TCO estimate |
| `d365-localization.md` | Philippine localization assessment (BIR, statutory, VAT) |
| `d365-scorecard.md` | Scored evaluation per the [Scoring Methodology](../07-methodology/scoring-methodology.md) |

## Products in Scope

| Product | Role |
|---|---|
| Dynamics 365 Finance | GL, AP, AR, consolidation, tax |
| Dynamics 365 Supply Chain Management | Inventory, procurement, WMS, planning |
| Dynamics 365 Commerce | POS, ecommerce, BOPIS, channel management |
| Dynamics 365 Human Resources | HR & payroll (evaluate Philippine payroll) |
| Power Platform | Custom extensions, workflows, BI dashboards |
| Azure | Cloud infrastructure, integration (API Management, Service Bus) |

## Key Evaluation Questions

1. How does D365 Commerce handle 1,000 POS terminals with offline capability?
2. How mature is the Philippine regulatory localization (BIR forms, VAT, withholding tax)?
3. Can D365 SCM handle catch-weight / variable measure items natively?
4. How does the 5-entity intercompany setup work in D365 Finance?
5. What is the Azure region latency for Philippines-based stores?

---

*Date created: 2026-05-30*
