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

- **[Merchandising & Pricing Workflows](./WF-merchandising.md)** (15 workflows) — Assortment planning, promotions, pricing, product lifecycle, PIM, vendor rebate management, markdown & clearance pricing, sample & demo inventory management, category performance review & P&L ownership, pricing hierarchy governance, private label development, and competitor intelligence.
- **[Procurement & Vendor Management Workflows](./WF-procurement.md)** (21 workflows) — Purchase orders, vendor onboarding, VMI, special orders, vendor performance, contracts, return to vendor processing, supplier quality CAPA, supplier diversity, and indirect procurement.
- **[Warehouse & Logistics Workflows](./WF-warehouse.md)** (10 workflows) — Receiving, putaway, kit assembly, fleet management, inter-island logistics, and DC outbound dispatch & load planning.
- **[Inventory Management Workflows](./WF-inventory.md)** (19 workflows) — Replenishment, cycle counting, transfers, consignment, physical inventory, backorders, promo stock allocation, damaged goods disposition, inventory adjustment authorization, multi-channel inventory allocation governance, and inter-store/inter-DC stock rebalancing.
- **[Store Operations Workflows](./WF-store-operations.md)** (38 workflows) — Daily store selling, POS, returns, loyalty, DSD receiving, gift cards, new store opening/closure, warranty, facility maintenance, performance review, planogram compliance, store renovation projects, store-level inventory receiving & putaway, and automated store cash management (Smart Safe).
- **[Ecommerce Workflows](./WF-ecommerce.md)** (9 workflows) — BOPIS order fulfillment, home delivery fulfillment, ship-from-store, ecommerce order exception & cancellation management, and home delivery reverse logistics (returns).
- **[Finance & Treasury Workflows](./WF-finance.md)** (32 workflows) — AP, AR, financial close, intercompany, capex, budget, treasury, insurance, credit/debit notes, management reporting, FX hedging, bad debt management, product costing & margin analysis, bank reconciliation, tax filing & statutory remittance, customer deposit management, payment settlement reconciliation, vendor statement reconciliation, customer refund & credit processing, customer credit collection, intercompany loans/dividends, and Senior Citizen/PWD VAT-exemption reporting.
- **[HR & Payroll Workflows](./WF-hr.md)** (11 workflows) — Payroll, recruitment, shift scheduling, onboarding/offboarding, training, performance, expenses, and employee loans.
- **[Supply Chain Planning Workflows](./WF-supply-chain.md)** (8 workflows) — Demand forecasting, seasonal buy planning, S&OP cycle, and international logistics/import operations.
- **[Customer Experience Workflows](./WF-customer.md)** (9 workflows) — Complaint resolution, corporate/project accounts, price matching, satisfaction measurement, account reactivation, feedback-to-action loop, trade sales pipeline & territory management, and trade counter / pro desk operations.
- **[IT Operations Workflows](./WF-it-operations.md)** (8 workflows) — Helpdesk, data privacy breach response, disaster recovery, data migration/parallel-run testing, business intelligence, IT asset management, and software change management.
- **[Compliance & Governance Workflows](./WF-compliance.md)** (17 workflows) — Loss prevention, business continuity, LGU permits, BIR audit, government procurement, grievance/whistleblower, hazardous waste disposal, external audit coordination, sustainability & environmental compliance reporting, and BIR CAS compliance audit.
- **[Marketing Campaign Workflows](./WF-marketing.md)** (11 workflows) — Campaign planning, creative production, multi-channel execution, budget tracking, performance measurement, loyalty program financial governance, crisis communication, CSR program execution, social media & influencer management, PR & corporate communications, and bank partnership management.
- **[Real Estate & Lease Management Workflows](./WF-property.md)** (4 workflows) — Site selection, lease administration, rent processing, and property tax management.
- **[Internal Audit & Risk Management Workflows](./WF-audit.md)** (5 workflows) — Audit planning, execution, enterprise risk management, and fraud investigation.
- **[Corporate Governance, Legal & Strategy Workflows](./WF-governance.md)** (8 workflows) — Board operations, legal case management, IP management, strategic planning, project management, and legal contract review.
- **[Installation & Value-Added Services](./WF-services.md)** (8 workflows) — Home installation, tool rental, DIY workshops, design consultancy, paint mixing, lumber cutting, 3D rendering, and contractor quality audit.
- **[Engineering & Construction Workflows](./WF-engineering-construction.md)** (5 workflows) — Site development, new store construction, renovations, and commissioning.
- **[Treasury & Corporate Finance Workflows](./WF-treasury.md)** (4 workflows) — LC management, cash flow forecasting, intercompany elimination, and transfer pricing.
- **[Hazardous Materials (Hazmat) & Compliance](./WF-hazmat.md)** (4 workflows) — Hazmat storage, safety handling, spill response, and customs reconciliation.
- **[Facility & Asset Maintenance (HQ & DC)](./WF-non-store-maintenance.md)** (4 workflows) — DC/HQ maintenance, 3PL performance, and POA/Board resolutions.
- **[Health, Safety & Environment Workflows](./WF-health-safety.md)** (3 workflows) — Occupational health & safety (OHS) incident management and workplace safety inspection & audit.
- **[Wholesale & Reseller Operations Workflows](./WF-wholesale.md)** (2 workflows) — Wholesale reseller onboarding and bulk fulfillment/cross-docking.
- **[Project-Based B2B & Trade Sales Workflows](./WF-project-sales.md)** (7 workflows) — Quotations, bid management, contract pricing, staged deliveries, and project-specific logistics.
- **[ESG & Sustainability Reporting Workflows](./WF-esg.md)** (4 workflows) — Carbon footprint, waste management, circular economy, and social impact.
- **[Fleet Operations & Driver Management](./WF-logistics-fleet.md)** (4 workflows) — Route optimization, driver performance, and fuel management.
- **[Innovation & Digital Transformation](./WF-innovation.md)** (5 workflows) — AI/ML, RPA, predictive maintenance, and computer vision.

- **[Workflow-to-System Touchpoint Map](./workflow-system-touchpoint-map.md)** — ERP module-to-workflow cross-reference

---

## Complete Workflow Index (W1–W250)

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
| W19b | Ship from Store (Store-Fulfilled Home Delivery) | [Ecommerce Workflows](WF-ecommerce.md) |
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
| W116 | Site Selection & Feasibility Analysis | [Real Estate & Lease Management Workflows](WF-property.md) |
| W117 | Lease Administration & Renewal | [Real Estate & Lease Management Workflows](WF-property.md) |
| W118 | Rent & CAM Payment Processing | [Real Estate & Lease Management Workflows](WF-property.md) |
| W119 | Real Property Tax (Amillaramento) Management | [Real Estate & Lease Management Workflows](WF-property.md) |
| W120 | Internal Audit Planning & Risk Assessment | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W121 | Operational Audit Execution (Store/DC/HQ) | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W122 | Enterprise Risk Management (ERM) Review | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W123 | Fraud Investigation | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W124 | Corporate Secretarial & Entity Management | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W125 | Legal Case & Litigation Management | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W126 | Intellectual Property (IP) Portfolio Management | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W127 | Annual Strategic Planning & OKRs | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W128 | Enterprise Project Management (EPM) Lifecycle | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W129 | Private Label / In-house Brand Development | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W130 | Competitor Price Intelligence Gathering | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W131 | IT Asset Lifecycle Management | [IT Operations Workflows](WF-it-operations.md) |
| W132 | Software Development & Change Management | [IT Operations Workflows](WF-it-operations.md) |
| W133 | Sales & Operations Planning (S&OP) Cycle | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W134 | Crisis Communication & Brand Reputation Management | [Marketing Campaign Workflows](WF-marketing.md) |
| W135 | CSR Program Execution | [Marketing Campaign Workflows](WF-marketing.md) |
| W136 | Indirect / Non-Merchandise Procurement | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W137 | Intercompany Dividend & Loan Management | [Finance & Treasury Workflows](WF-finance.md) |
| W138 | Home Installation Services Management | [Installation & Value-Added Services](WF-services.md) |
| W139 | Tool & Equipment Rental Operations | [Installation & Value-Added Services](WF-services.md) |
| W140 | OHS Incident Management | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W141 | Workplace Safety Inspection & Audit | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W142 | Social Media & Influencer Management | [Marketing Campaign Workflows](WF-marketing.md) |
| W143 | Public Relations & Corporate Communications | [Marketing Campaign Workflows](WF-marketing.md) |
| W144 | International Logistics & Import Operations | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W145 | Wholesale Reseller Onboarding & Credit | [Wholesale & Reseller Operations Workflows](WF-wholesale.md) |
| W146 | Bulk Fulfillment & Cross-Docking | [Wholesale & Reseller Operations Workflows](WF-wholesale.md) |
| W147 | DIY Workshop & In-Store Event Management | [Installation & Value-Added Services](WF-services.md) |
| W148 | Home Design & Consultancy Services | [Installation & Value-Added Services](WF-services.md) |
| W149 | Bank & Credit Card Partnership Management | [Marketing Campaign Workflows](WF-marketing.md) |
| W150 | Product Quality Testing & Certification | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W151 | Corporate Social Responsibility (CSR) Impact Measurement & Reporting | [Marketing Campaign Workflows](WF-marketing.md) |
| W152 | Employee IT Provisioning & Access Lifecycle Management | [IT Operations Workflows](WF-it-operations.md) |
| W153 | Retail Media Network (RMN) Operations | [Marketing Campaign Workflows](WF-marketing.md) |
| W154 | Proactive Store Inventory Rebalancing (Stock Push) | [Inventory Management Workflows](WF-inventory.md) |
| W155 | Vendor Strategic Collaboration & Joint Business Planning (JBP) | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W156 | Customer Data Platform (CDP) & Hyper-Personalization | [Customer Experience Workflows](WF-customer.md) |
| W157 | E-waste Collection & Circular Economy Operations | [Compliance & Governance Workflows](WF-compliance.md) |
| W158 | Business Continuity Drill & Disaster Recovery Testing | [Compliance & Governance Workflows](WF-compliance.md) |
| W159 | Anti-Bribery & Corruption (ABC) Monitoring & Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W160 | Private Label Factory Audit & Social Compliance | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W161 | Vendor Price Protection & Market Markdown Claims | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W162 | Project Quotation & Bid Management | [Project Sales Workflows](WF-project-sales.md) |
| W163 | Contract Pricing & Project Price Books | [Project Sales Workflows](WF-project-sales.md) |
| W164 | Staged Project Delivery & Call-Off Orders | [Project Sales Workflows](WF-project-sales.md) |
| W165 | Project Retention & Milestone Billing | [Project Sales Workflows](WF-project-sales.md) |
| W166 | Corporate / Institutional Tendering | [Project Sales Workflows](WF-project-sales.md) |
| W167 | Store & DC Recycling Program (Circular Economy) | [Compliance & Governance Workflows](WF-compliance.md) |
| W168 | Custom Paint Mixing & Tinting Operations | [Installation & Value-Added Services](WF-services.md) |
| W169 | Lumber & Board Cutting Services | [Installation & Value-Added Services](WF-services.md) |
| W170 | Senior Citizen & PWD Discount Compliance (PH Legal) | [Store Operations Workflows](WF-store-operations.md) |
| W171 | Store Physical Security & Yard Patrol Routine | [Store Operations Workflows](WF-store-operations.md) |
| W172 | Employee PPE & Uniform Lifecycle | [HR & Payroll Workflows](WF-hr.md) |
| W173 | Store-Level Solar Energy Monitoring | [Store Operations Workflows](WF-store-operations.md) |
| W174 | Store-Level Cash-in-Transit (CIT) & Armored Car Management | [Finance & Treasury Workflows](WF-finance.md) |
| W175 | Employee Gratuity & Retirement Fund Management (RA 7641) | [Finance & Treasury Workflows](WF-finance.md) |
| W176 | Store-to-DC Reverse Logistics (Consolidation) | [Store Operations Workflows](WF-store-operations.md) |
| W177 | Vending & Concessionaire Management | [Store Operations Workflows](WF-store-operations.md) |
| W178 | Employee Succession & Internal Mobility | [HR & Payroll Workflows](WF-hr.md) |
| W179 | Management Trainee (Cadetship) Program | [HR & Payroll Workflows](WF-hr.md) |
| W180 | E-commerce Marketplace Integration (Lazada/Shopee) | [Ecommerce Workflows](WF-ecommerce.md) |
| W181 | Store-Level Price Tag Printing & Verification | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W182 | Gift / Home Registry Lifecycle | [Store Operations Workflows](WF-store-operations.md) |
| W183 | Supply Chain Network Optimization Review | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W184 | Fixed Asset Physical Verification (Audit) | [Finance & Treasury Workflows](WF-finance.md) |
| W185 | Product Liability & Consumer Safety Incident Management | [Compliance & Governance Workflows](WF-compliance.md) |
| W186 | Internal SOP & Policy Governance Lifecycle | [Corporate Governance & Strategy Workflows](WF-governance.md) |
| W187 | Contractor & Third-Party On-site Safety Orientation | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W188 | Fleet Spare Parts & Preventive Maintenance (PM) Management | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W189 | Referral Program & Brand Ambassador Management | [Marketing Campaign Workflows](WF-marketing.md) |
| W190 | In-house Design & Creative Production Management | [Marketing Campaign Workflows](WF-marketing.md) |
| W191 | Global Supply Chain — Incoterm & Marine Insurance Tracking | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W192 | Greenhouse Gas (GHG) Emissions Tracking | [ESG & Sustainability Reporting](WF-esg.md) |
| W193 | Waste Management & Circular Economy | [ESG & Sustainability Reporting](WF-esg.md) |
| W194 | Social Impact & Community Development (CSR) | [ESG & Sustainability Reporting](WF-esg.md) |
| W195 | Sustainable Sourcing & Ethical Vendor Audit | [ESG & Sustainability Reporting](WF-esg.md) |
| W196 | Route Planning & Dispatch Optimization | [Fleet Operations & Driver Management](WF-logistics-fleet.md) |
| W197 | Driver Performance & Safety Management | [Fleet Operations & Driver Management](WF-logistics-fleet.md) |
| W198 | Fuel Management & Consumption Monitoring | [Fleet Operations & Driver Management](WF-logistics-fleet.md) |
| W199 | Fleet Telematics & Real-Time Tracking | [Fleet Operations & Driver Management](WF-logistics-fleet.md) |
| W200 | AI-Driven Personalization & Recommendation Engine | [Innovation & Digital Transformation](WF-innovation.md) |
| W201 | Robotic Process Automation (RPA) Lifecycle | [Innovation & Digital Transformation](WF-innovation.md) |
| W202 | Predictive Maintenance for Industrial Assets | [Innovation & Digital Transformation](WF-innovation.md) |
| W203 | Computer Vision for Inventory & Planogram Audit | [Innovation & Digital Transformation](WF-innovation.md) |
| W204 | Regional Stock Rebalancing & Inter-Store Expedited Transfers | [Inventory Management Workflows](WF-inventory.md) |
| W205 | Employee Purchase Program & Internal Staff Sales | [Store Operations Workflows](WF-store-operations.md) |
| W206 | Mobile POS (mPOS) & Queue-Busting Operations | [Store Operations Workflows](WF-store-operations.md) |
| W207 | Store-Level Security Camera (CCTV) Audit & LP Integration | [Compliance & Governance Workflows](WF-compliance.md) |
| W208 | Retail Analytics & AI-Driven Inventory Optimization | [Innovation & Digital Transformation](WF-innovation.md) |
| W209 | Barangay & Local Community Relationship Management | [Compliance & Governance Workflows](WF-compliance.md) |
| W210 | E-commerce Fulfillment Hub (Dark Store) Operations | [Ecommerce Workflows](WF-ecommerce.md) |
| W211 | In-Store 3D Kitchen/Bathroom Design Rendering | [Installation & Value-Added Services](WF-services.md) |
| W212 | Automated Store Cash Management & Smart Safe Integration | [Store Operations Workflows](WF-store-operations.md) |
| W213 | Installation Service Partner Quality Audit | [Installation & Value-Added Services](WF-services.md) |
| W214 | Store-to-Store Expedited Transfers (Customer-Initiated) | [Inventory Management Workflows](WF-inventory.md) |
| W215 | Customer Home Delivery Reverse Logistics (Returns) | [Ecommerce Workflows](WF-ecommerce.md) |
| W216 | BIR CAS (Computerized Accounting System) Compliance Audit | [Compliance & Governance Workflows](WF-compliance.md) |
| W217 | Senior Citizen & PWD VAT-Exemption Audit & Reporting | [Finance & Treasury Workflows](WF-finance.md) |
| W218 | Inter-DC Stock Rebalancing (Stock Push) | [Inventory Management Workflows](WF-inventory.md) |
| W219 | Store Inventory Quarantine & Recertification | [Inventory Management Workflows](WF-inventory.md) |
| W220 | Slow-Moving & Obsolete Inventory (SLOB) Provisioning & Liquidation | [Inventory Management Workflows](WF-inventory.md) |
| W221 | Cross-Docking Operations for Fast-Moving Bulky Items | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W222 | DC Container Yard & Chassis Management | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W223 | New Store Design & Engineering Standards | [Engineering & Construction Workflows](WF-engineering-construction.md) |
| W224 | Construction Bidding & Contractor Selection | [Engineering & Construction Workflows](WF-engineering-construction.md) |
| W225 | Store Construction Management & Supervision | [Engineering & Construction Workflows](WF-engineering-construction.md) |
| W226 | Store Renovation & Retrofitting (CAPEX) | [Engineering & Construction Workflows](WF-engineering-construction.md) |
| W227 | Commissioning & Operational Handover | [Engineering & Construction Workflows](WF-engineering-construction.md) |
| W228 | Sales Commission Calculation (Trade & Project Sales) | [Project-Based B2B & Trade Sales Workflows](WF-project-sales.md) |
| W229 | B2B Customer Credit Limit Exception & Escalation | [Project-Based B2B & Trade Sales Workflows](WF-project-sales.md) |
| W230 | Legal Contract Review & Approval | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W231 | Management Performance Reporting (QBR) | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W232 | Letter of Credit (LC) & Bank Guarantee Lifecycle | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W233 | Cash Flow Forecasting & Liquidity Management | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W234 | Intercompany Profit Elimination & Consolidation | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W235 | Transfer Pricing Compliance & Documentation | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W236 | Hazmat Storage & Segregation Compliance (DC) | [Hazardous Materials (Hazmat) & Compliance](WF-hazmat.md) |
| W237 | Hazmat Handling & Safety Training (Store) | [Hazardous Materials (Hazmat) & Compliance](WF-hazmat.md) |
| W238 | Hazmat Spill Response & Incident Management | [Hazardous Materials (Hazmat) & Compliance](WF-hazmat.md) |
| W239 | Customs Duty & Tax Reconciliation (BOC) | [Hazardous Materials (Hazmat) & Compliance](WF-hazmat.md) |
| W240 | DC Facility & Warehouse Equipment Maintenance | [Facility & Asset Maintenance (HQ & DC)](WF-non-store-maintenance.md) |
| W241 | HQ Office Facility & Executive Asset Maintenance | [Facility & Asset Maintenance (HQ & DC)](WF-non-store-maintenance.md) |
| W242 | 3PL & Logistics Partner Performance Review | [Facility & Asset Maintenance (HQ & DC)](WF-non-store-maintenance.md) |
| W243 | Power of Attorney (POA) & Board Resolution Lifecycle | [Facility & Asset Maintenance (HQ & DC)](WF-non-store-maintenance.md) |
| W244 | Vendor Invoice Dispute & Discrepancy Resolution | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W245 | Vendor Performance Chargebacks & Penalties Management | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W246 | Drop-Ship Vendor (DSV) Order Fulfillment | [Ecommerce Workflows](WF-ecommerce.md) |
| W247 | BOPIS Smart Locker & Queue Management | [Ecommerce Workflows](WF-ecommerce.md) |
| W248 | Store Inventory Variance & LP Investigation | [Store Operations Workflows](WF-store-operations.md) |
| W249 | Import Port Demurrage & Detention Management | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W250 | Supply Chain Control Tower & Real-Time Shipment Visibility | [Supply Chain Planning Workflows](WF-supply-chain.md) |

---

*Total: 274 workflows across 23 domains. Expanded to include Treasury, Hazmat, Facilities Maintenance, Engineering & Construction, Legal, Sales Commission, Dispute Resolution, Smart Locker Fulfillment, LP Investigation, and Port Demurrage Management, alongside ESG, fleet optimization, digital innovation, and advanced regulatory compliance.*
