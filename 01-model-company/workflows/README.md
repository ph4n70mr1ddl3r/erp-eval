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

- **[Merchandising & Pricing Workflows](./WF-merchandising.md)** (12 workflows) — Assortment planning, promotions, pricing, product lifecycle, PIM, vendor rebate management, markdown & clearance pricing, sample & demo inventory management, category performance review & P&L ownership, and pricing hierarchy governance & compliance audit.
- **[Procurement & Vendor Management Workflows](./WF-procurement.md)** (10 workflows) — Purchase orders, vendor onboarding, VMI, special orders, vendor performance, contracts, return to vendor processing, supplier quality CAPA, and supplier diversity & MSME development.
- **[Warehouse & Logistics Workflows](./WF-warehouse.md)** (5 workflows) — Receiving, putaway, kit assembly, fleet management, inter-island logistics, and DC outbound dispatch & load planning.
- **[Inventory Management Workflows](./WF-inventory.md)** (10 workflows) — Replenishment, cycle counting, transfers, consignment, physical inventory, backorders, promo stock allocation, damaged goods disposition, inventory adjustment authorization, and multi-channel inventory allocation governance.
- **[Store Operations Workflows](./WF-store-operations.md)** (19 workflows) — Daily store selling, POS, returns, loyalty, DSD receiving, gift cards, new store opening/closure, warranty, facility maintenance, performance review, planogram compliance, store renovation projects, store-level inventory receiving & putaway, and store energy & utility consumption management.
- **[Ecommerce Workflows](./WF-ecommerce.md)** (3 workflows) — BOPIS order fulfillment, home delivery fulfillment, and ecommerce order exception & cancellation management.
- **[Finance & Treasury Workflows](./WF-finance.md)** (23 workflows) — AP, AR, financial close, intercompany, capex, budget, treasury, insurance, credit/debit notes, management reporting, FX hedging, bad debt management, product costing & margin analysis, bank reconciliation, tax filing & statutory remittance, customer deposit management, payment settlement reconciliation, vendor statement reconciliation, customer refund & credit processing, and customer credit collection & escalation.
- **[HR & Payroll Workflows](./WF-hr.md)** (8 workflows) — Payroll, recruitment, shift scheduling, onboarding/offboarding, training, performance, expenses, and employee loans.
- **[Supply Chain Planning Workflows](./WF-supply-chain.md)** (2 workflows) — Demand forecasting and seasonal buy planning.
- **[Customer Experience Workflows](./WF-customer.md)** (8 workflows) — Complaint resolution, corporate/project accounts, price matching, satisfaction measurement, account reactivation, feedback-to-action loop, trade sales pipeline & territory management, and trade counter / pro desk operations.
- **[IT Operations Workflows](./WF-it-operations.md)** (5 workflows) — Helpdesk, data privacy breach response, disaster recovery, data migration/parallel-run testing, and business intelligence & data governance.
- **[Compliance & Governance Workflows](./WF-compliance.md)** (9 workflows) — Loss prevention, business continuity, LGU permits, BIR audit, government procurement, grievance/whistleblower, hazardous waste disposal, external audit coordination, and sustainability & environmental compliance reporting.

- **[Marketing Campaign Workflows](./WF-marketing.md)** (2 workflows) — Campaign planning, creative production, multi-channel execution, budget tracking, performance measurement, and loyalty program financial governance & periodic review.

- **[Workflow-to-System Touchpoint Map](./workflow-system-touchpoint-map.md)** — ERP module-to-workflow cross-reference

---

## Complete Workflow Index (W1–W99)

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
| W88 | Return to Vendor (RTV) Processing | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W89 | Bank Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W90 | Monthly Tax Filing & Statutory Remittance | [Finance & Treasury Workflows](WF-finance.md) |
| W91 | Damaged & Defective Goods Disposition | [Inventory Management Workflows](WF-inventory.md) |
| W92 | Inventory Adjustment & Shrinkage Authorization | [Inventory Management Workflows](WF-inventory.md) |
| W93 | Markdown & Clearance Pricing Execution | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W94 | Customer Deposit & Advance Payment Management | [Finance & Treasury Workflows](WF-finance.md) |
| W95 | External Audit Coordination & Support | [Compliance & Governance Workflows](WF-compliance.md) |
| W96 | Store Renovation & Remodel Project | [Store Operations Workflows](WF-store-operations.md) |
| W97 | Sample & Demo Inventory Management | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W98 | Ecommerce Order Exception & Cancellation Management | [Ecommerce Workflows](WF-ecommerce.md) |
| W99 | Payment Settlement Reconciliation (Card / E-Wallet / Online) | [Finance & Treasury Workflows](WF-finance.md) |
| W100 | Vendor Statement Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W101 | Customer Refund & Credit Processing | [Finance & Treasury Workflows](WF-finance.md) |
| W102 | Category Performance Review & P&L Ownership | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W103 | Trade Sales Pipeline & Territory Management | [Customer Experience Workflows](WF-customer.md) |
| W104 | Loyalty Program Financial Governance & Periodic Review | [Marketing Campaign Workflows](WF-marketing.md) |
| W105 | Multi-Channel Inventory Allocation & Priority Governance | [Inventory Management Workflows](WF-inventory.md) |
| W106 | DC Outbound Dispatch & Load Planning | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W107 | Pricing Hierarchy Governance & Compliance Audit | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W108 | Customer Credit Collection & Escalation | [Finance & Treasury Workflows](WF-finance.md) |
| W109 | Store-Level Inventory Receiving & Putaway | [Store Operations Workflows](WF-store-operations.md) |
| W110 | Supplier Quality & CAPA (Corrective and Preventive Action) | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W111 | Store Energy & Utility Consumption Management | [Store Operations Workflows](WF-store-operations.md) |
| W112 | Trade Counter / Pro Desk Operations | [Customer Experience Workflows](WF-customer.md) |
| W113 | Business Intelligence & Data Governance | [IT Operations Workflows](WF-it-operations.md) |
| W114 | Sustainability & Environmental Compliance Reporting | [Compliance & Governance Workflows](WF-compliance.md) |
| W115 | Supplier Diversity & MSME Development Program | [Procurement & Vendor Management Workflows](WF-procurement.md) |

---

*Total: 116 workflows across 13 domains. Split from original monolithic file*
