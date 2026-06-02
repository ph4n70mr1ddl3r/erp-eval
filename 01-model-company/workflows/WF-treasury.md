# Treasury & Corporate Finance Workflows

> Letter of Credit (LC) management, bank guarantees, cash flow forecasting, intercompany profit elimination, and transfer pricing.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W232. Letter of Credit (LC) & Bank Guarantee Lifecycle](#letter-of-credit-lc--bank-guarantee-lifecycle)
- [W233. Cash Flow Forecasting & Liquidity Management](#cash-flow-forecasting--liquidity-management)
- [W234. Intercompany Profit Elimination & Consolidation](#intercompany-profit-elimination--consolidation)
- [W235. Transfer Pricing Compliance & Documentation](#transfer-pricing-compliance--documentation)

---

## W232. Letter of Credit (LC) & Bank Guarantee Lifecycle

| Field | Detail |
|---|---|
| **Trigger** | Approved Import PO (W2B) requiring LC; or contract requirement for Bank Guarantee |
| **Frequency** | 10–20 LCs/month (imports); 5–10 Bank Guarantees/year |
| **Volume** | High-value import shipments (Machinery, bulk construction materials) |
| **Owner** | Treasury Manager |
| **Participants** | Import Coordinator, Buyer, Bank, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Application**: Import Coordinator requests LC issuance based on Pro-forma Invoice and PO | Import Coord | Treasury Mgr | 1 day |
| 2 | **Bank Submission**: Treasury submits LC application to partner bank via electronic portal | Treasury Mgr | CFO | 1 day |
| 3 | **LC Issuance**: Bank issues LC; notifies Vendor's bank (Advising Bank) | Bank | — | 2–3 days |
| 4 | **Document Negotiation**: Vendor ships goods; submits shipping documents (Bill of Lading, Invoice, Packing List) to bank | Vendor | — | 1 week |
| 5 | **Discrepancy Check**: Treasury and Bank review documents for discrepancies vs. LC terms | Treasury Mgr | — | 2 days |
| 6 | **Payment/Acceptance**: Treasury authorizes payment or acceptance of draft; Bank releases documents to BuildRight for customs clearance (W233) | Treasury Mgr | CFO | 1 day |
| 7 | **Closure**: LC closed in system once goods received (W3) and payment settled | Treasury Mgr | — | 1 day |

---

## W233. Cash Flow Forecasting & Liquidity Management

| Field | Detail |
|---|---|
| **Trigger** | Weekly treasury cycle |
| **Frequency** | Weekly (Daily monitoring) |
| **Volume** | Covers 5 entities and ~50 bank accounts |
| **Owner** | Treasury Analyst |
| **Participants** | CFO, Controller, AP/AR Managers |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Data Aggregation**: Pull expected receipts (AR) and planned payments (AP, Payroll, Tax) from ERP | System | Treasury Analyst | 1 hour |
| 2 | **Non-ERP Inputs**: Add manual forecasts for CAPEX, loan repayments, and dividends | Treasury Analyst | Treasury Mgr | 2 hours |
| 3 | **Analysis**: Identify liquidity gaps or excess cash across entities | Treasury Analyst | Treasury Mgr | 2 hours |
| 4 | **Cash Positioning**: Execute intercompany transfers (sweeping) to optimize interest or cover deficits | Treasury Mgr | CFO | 1 day |
| 5 | **Reporting**: Weekly Cash Position Report to Executive Team | Treasury Mgr | CFO | 1 hour |

---

## W234. Intercompany Profit Elimination & Consolidation

| Field | Detail |
|---|---|
| **Trigger** | Month-end close (W9) |
| **Frequency** | Monthly |
| **Volume** | Sales between Logistics Inc., Property Inc., and Depot Inc. |
| **Owner** | Consolidation Manager |
| **Participants** | Entity Controllers, CFO |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Reconciliation**: Match intercompany sales/purchases and AR/AP balances between entities | Entity Accountant | Consolidation Mgr | 1 day |
| 2 | **Profit Identification**: Identify "Unrealized Profit" in ending inventory for goods sold between entities (e.g., Depot Inc. holding stock bought from Logistics Inc.) | Consolidation Mgr | Controller | 1 day |
| 3 | **Elimination Entries**: Post elimination journals in the Consolidation Ledger (Dr. Revenue / Cr. COGS; Dr. COGS / Cr. Inventory) | Consolidation Mgr | CFO | 4 hours |
| 4 | **Validation**: Verify Consolidated Trial Balance reflects zero intercompany balances | Consolidation Mgr | — | 2 hours |

---

## W235. Transfer Pricing Compliance & Documentation

| Field | Detail |
|---|---|
| **Trigger** | Annual tax cycle; or major change in intercompany service agreements |
| **Frequency** | Annual (Documentation); Quarterly (Review) |
| **Volume** | 5 related entities in the Philippines |
| **Owner** | Tax Manager |
| **Participants** | External Tax Advisor, CFO, Controller |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Benchmarking**: Conduct annual comparability study for intercompany markups (Logistics services, Rent) | Tax Manager | CFO | 2 weeks |
| 2 | **Local File Prep**: Prepare "Transfer Pricing Documentation" (TPD) per BIR RR No. 19-2020 | Tax Manager | External Advisor | 1 month |
| 3 | **Quarterly Monitoring**: Review actual intercompany margins against the Arm's Length Range | Tax Manager | Controller | 1 day |
| 4 | **Adjustments**: If margins are outside range, trigger true-up/true-down entries | Tax Manager | CFO | 1 day |
| 5 | **Reporting**: File BIR Form 1709 (RPT Form) with the Annual Income Tax Return | Tax Manager | CFO | Per schedule |

### System Touchpoints
- Treasury Management Module (LC tracking, Bank limits)
- Cash Flow Forecasting tool (direct/indirect methods)
- Consolidation Engine with automated elimination rules
- Intercompany matching workbench
- Integration with W2B (Import PO), W7 (Payments), W8 (Receipts), W14 (Logistics Billing)
