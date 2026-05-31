# BuildRight Depot Corp. — Operational Workflows


> This document describes the end-to-end operational workflows of BuildRight Depot,
> defining who does what, when, and why. It serves three purposes:
>
> 1. **Validate headcount** — by mapping work volume to roles, we can verify staffing assumptions
> 2. **Inform ERP design** — each workflow reveals system touchpoints, automation opportunities, and integration needs
> 3. **Optimize organization** — by exposing handoffs, bottlenecks, and spans of control

---

## How to Read This Document

Each workflow follows this format:

| Field | Meaning |
|---|---|
| **Workflow ID** | Unique identifier (WF-XX) |
| **Name** | Process name |
| **Trigger** | What initiates the workflow |
| **Frequency** | How often it occurs |
| **Volume** | How many instances per occurrence |
| **Owner** | Role accountable for the outcome |
| **Participants** | All roles involved |
| **Steps** | Sequential activities with responsible role |
| **System Touchpoints** | Where ERP/system support is needed |
| **Time Estimate** | Estimated effort per occurrence |
| **Pain Points / Risks** | What can go wrong |

**RACI Key**: R = Responsible (does the work), A = Accountable (owns the outcome), C = Consulted, I = Informed

---


## Domain Files

Workflows are organized by functional domain for easier navigation and gap analysis:

- **[Merchandising & Pricing Workflows](./WF-merchandising.md)** (8 workflows) — Assortment planning, promotions, pricing, product lifecycle, PIM, and vendor rebate management.
- **[Procurement & Vendor Management Workflows](./WF-procurement.md)** (7 workflows) — Purchase orders, vendor onboarding, VMI, special orders, vendor performance, and contracts.
- **[Warehouse & Logistics Workflows](./WF-warehouse.md)** (4 workflows) — Receiving, putaway, kit assembly, fleet management, and inter-island logistics.
- **[Inventory Management Workflows](./WF-inventory.md)** (7 workflows) — Replenishment, cycle counting, transfers, consignment, physical inventory, backorders, and promo stock allocation.
- **[Store Operations Workflows](./WF-store-operations.md)** (16 workflows) — Daily store selling, POS, returns, loyalty, DSD receiving, gift cards, new store opening/closure, warranty, facility maintenance, performance review, and planogram compliance.
- **[Ecommerce Workflows](./WF-ecommerce.md)** (2 workflows) — BOPIS order fulfillment and home delivery fulfillment.
- **[Finance & Treasury Workflows](./WF-finance.md)** (16 workflows) — AP, AR, financial close, intercompany, capex, budget, treasury, insurance, credit/debit notes, management reporting, FX hedging, bad debt management, and product costing & margin analysis.
- **[HR & Payroll Workflows](./WF-hr.md)** (8 workflows) — Payroll, recruitment, shift scheduling, onboarding/offboarding, training, performance, expenses, and employee loans.
- **[Supply Chain Planning Workflows](./WF-supply-chain.md)** (2 workflows) — Demand forecasting and seasonal buy planning.
- **[Customer Experience Workflows](./WF-customer.md)** (6 workflows) — Complaint resolution, corporate/project accounts, price matching, satisfaction measurement, account reactivation, and feedback-to-action loop.
- **[IT Operations Workflows](./WF-it-operations.md)** (4 workflows) — Helpdesk, data privacy breach response, disaster recovery, and data migration/parallel-run testing.
- **[Compliance & Governance Workflows](./WF-compliance.md)** (7 workflows) — Loss prevention, business continuity, LGU permits, BIR audit, government procurement, grievance/whistleblower, and hazardous waste disposal.

- **[Marketing Campaign Workflows](./WF-marketing.md)** (1 workflow) — Campaign planning, creative production, multi-channel execution, budget tracking, and performance measurement.

- **[Workflow-to-System Touchpoint Map](./workflow-system-touchpoint-map.md)** — ERP module-to-workflow cross-reference

---

## Complete Workflow Index (W1–W87)

| ID | Workflow Name | Domain File |
|---|---|---|
| W1 | Merchandise Planning & Assortment Review | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W2 | Procurement — Purchase Order Cycle | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W3 | Warehouse Receiving & Putaway | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W4 | Store Replenishment (DC → Store) | [Inventory Management Workflows](WF-inventory.md) |
| W5 | Daily Store Operations | [Store Operations Workflows](WF-store-operations.md) |
| W5g | Offline POS Recovery & Reconciliation | [Store Operations Workflows](WF-store-operations.md) |
| W6 | Cycle Counting & Inventory Accuracy | [Inventory Management Workflows](WF-inventory.md) |
| W7 | Accounts Payable — Vendor Invoice Processing | [Finance & Treasury Workflows](WF-finance.md) |
| W8 | Accounts Receivable — Trade & Corporate Accounts | [Finance & Treasury Workflows](WF-finance.md) |
| W9 | Financial Close & Reporting | [Finance & Treasury Workflows](WF-finance.md) |
| W10 | Payroll Processing | [HR & Payroll Workflows](WF-hr.md) |
| W11 | Ecommerce — BOPIS Order Fulfillment | [Ecommerce Workflows](WF-ecommerce.md) |
| W12 | Returns & Exchanges | [Store Operations Workflows](WF-store-operations.md) |
| W13 | Promotions & Pricing Execution | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W14 | Intercompany Transactions & Settlement | [Finance & Treasury Workflows](WF-finance.md) |
| W15 | Recruitment & Employee Onboarding | [HR & Payroll Workflows](WF-hr.md) |
| W16 | New Store Opening | [Store Operations Workflows](WF-store-operations.md) |
| W17 | Customer Loyalty Program Operations | [Store Operations Workflows](WF-store-operations.md) |
| W18 | Direct Store Delivery (DSD) Receiving | [Store Operations Workflows](WF-store-operations.md) |
| W19 | Ecommerce — Home Delivery Fulfillment | [Ecommerce Workflows](WF-ecommerce.md) |
| W20 | Vendor Managed Inventory (VMI) | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W21 | Capital Expenditure (Capex) Request & Approval | [Finance & Treasury Workflows](WF-finance.md) |
| W22 | Stock Transfers (Store-to-Store & Inter-DC) | [Inventory Management Workflows](WF-inventory.md) |
| W23 | Consignment Inventory Operations | [Inventory Management Workflows](WF-inventory.md) |
| W24 | Trade & Corporate Credit Application | [Finance & Treasury Workflows](WF-finance.md) |
| W25 | Petty Cash Management | [Finance & Treasury Workflows](WF-finance.md) |
| W26 | Annual Budget Preparation & Monthly Variance Review | [Finance & Treasury Workflows](WF-finance.md) |
| W27 | Vendor Rebate Accrual & Settlement | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W28 | Gift Card & Store Credit Lifecycle | [Store Operations Workflows](WF-store-operations.md) |
| W29 | Product Recall Execution | [Store Operations Workflows](WF-store-operations.md) |
| W30 | Daily Treasury & Cash Position Management | [Finance & Treasury Workflows](WF-finance.md) |
| W31 | Demand Forecasting Cycle | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W32 | Seasonal Buy Planning | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W33 | Warranty Claim Processing | [Store Operations Workflows](WF-store-operations.md) |
| W34 | Store Shift Scheduling | [HR & Payroll Workflows](WF-hr.md) |
| W35 | Management Reporting Rhythm | [Finance & Treasury Workflows](WF-finance.md) |
| W36 | Vendor Onboarding | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W37 | Loss Prevention & Exception Reporting | [Compliance & Governance Workflows](WF-compliance.md) |
| W38 | Special Order / Non-Stock Item Fulfillment | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W39 | Fixed Asset Disposal & Retirement | [Finance & Treasury Workflows](WF-finance.md) |
| W40 | Regular Price Change Execution | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W41 | Customer Complaint Resolution | [Customer Experience Workflows](WF-customer.md) |
| W42 | Annual Physical Inventory Execution | [Inventory Management Workflows](WF-inventory.md) |
| W43 | Employee Separation & Offboarding | [HR & Payroll Workflows](WF-hr.md) |
| W44 | Vendor Performance Review | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W45 | Store Closure / Relocation | [Store Operations Workflows](WF-store-operations.md) |
| W46 | Kit / Bundle Assembly & Disassembly | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W47 | Store Facility Maintenance & Work Orders | [Store Operations Workflows](WF-store-operations.md) |
| W48 | IT Operations & Helpdesk Support | [IT Operations Workflows](WF-it-operations.md) |
| W49 | Natural Disaster / Typhoon Business Continuity | [Compliance & Governance Workflows](WF-compliance.md) |
| W50 | Product Information Management (PIM) | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W51 | Employee Training & Skills Development | [HR & Payroll Workflows](WF-hr.md) |
| W52 | Fleet Management | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W53 | Data Privacy Breach Response | [IT Operations Workflows](WF-it-operations.md) |
| W54 | LGU Business Permit Renewal per Location | [Compliance & Governance Workflows](WF-compliance.md) |
| W55 | IT Disaster Recovery & System Failover | [IT Operations Workflows](WF-it-operations.md) |
| W56 | Customer Backorder Management | [Inventory Management Workflows](WF-inventory.md) |
| W57 | Promotional Stock Allocation & Pre-Positioning | [Inventory Management Workflows](WF-inventory.md) |
| W58 | Corporate / Project Account Management | [Customer Experience Workflows](WF-customer.md) |
| W59 | Insurance Policy Lifecycle Management | [Finance & Treasury Workflows](WF-finance.md) |
| W60 | Emergency Procurement | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W61 | Competitor Price Match Process | [Customer Experience Workflows](WF-customer.md) |
| W62 | Vendor Contract Lifecycle (Non-PO Contracts) | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W63 | Shelf Label & Price Tag Distribution | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W64 | New Product Pilot / Store Test | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W65 | Customer Satisfaction Measurement | [Customer Experience Workflows](WF-customer.md) |
| W66 | Inter-Island Logistics & Freight Management | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W67 | Monthly Store Performance Review | [Store Operations Workflows](WF-store-operations.md) |
| W68 | Product Lifecycle & Discontinuation | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W69 | Price Compliance Audit | [Store Operations Workflows](WF-store-operations.md) |
| W70 | Credit Note & Debit Note Aging Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W71 | Store Physical Security & Access Control | [Store Operations Workflows](WF-store-operations.md) |
| W72 | Employee Performance Management | [HR & Payroll Workflows](WF-hr.md) |
| W73 | Data Migration Validation & Parallel-Run Testing | [IT Operations Workflows](WF-it-operations.md) |
| W74 | Employee Expense Reimbursement | [HR & Payroll Workflows](WF-hr.md) |
| W75 | Layaway / Installment Sales | [Store Operations Workflows](WF-store-operations.md) |
| W76 | Employee Loans & Advances | [HR & Payroll Workflows](WF-hr.md) |
| W77 | BIR Tax Audit Response | [Compliance & Governance Workflows](WF-compliance.md) |
| W78 | Government / Institutional Procurement Participation | [Compliance & Governance Workflows](WF-compliance.md) |
| W79 | Employee Grievance & Whistleblower Process | [Compliance & Governance Workflows](WF-compliance.md) |
| W80 | FX Hedging & Forward Contract Management | [Finance & Treasury Workflows](WF-finance.md) |
| W81 | Bad Debt Provisioning, Write-Off & Recovery | [Finance & Treasury Workflows](WF-finance.md) |
| W82 | Hazardous Waste Disposal Tracking & DENR Compliance | [Compliance & Governance Workflows](WF-compliance.md) |
| W83 | Marketing Campaign Planning, Execution & Performance Measurement | [Marketing Campaign Workflows](WF-marketing.md) |
| W84 | Customer Account Reactivation | [Customer Experience Workflows](WF-customer.md) |
| W85 | Product Costing & Margin Analysis Review | [Finance & Treasury Workflows](WF-finance.md) |
| W86 | Planogram Compliance & Store Layout Verification | [Store Operations Workflows](WF-store-operations.md) |
| W87 | Customer Feedback-to-Action Loop | [Customer Experience Workflows](WF-customer.md) |

---

*Total: 87 workflows across 13 domains. Split from original monolithic file*
