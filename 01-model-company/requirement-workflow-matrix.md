# Requirement-to-Workflow Cross-Reference Matrix

> Maps each ERP requirement from [erp-requirements.md](erp-requirements.md) to the operational
> workflows from the [workflows/](workflows/README.md) directory that exercise it.
> Ensures complete traceability: every requirement is validated by at least one workflow,
> and every workflow tests at least one requirement.

---

## How to Read This Matrix

- **Req ID**: Requirement identifier from erp-requirements.md
- **Priority**: Must Have (M), Should Have (S), Nice to Have (N)
- **Primary Workflows**: Workflows where this requirement is directly exercised and system touchpoints are listed
- **Supporting Workflows**: Workflows that indirectly involve this requirement

---

## R1. Financial Management (FIN)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| FIN-001 | Multi-entity GL | M | W9a (month-end close), W14 (IC transactions) | W10 (payroll GL posting), W30 (treasury) |
| FIN-002 | Automated IC Elimination | M | W9a.13, W14.8 | — |
| FIN-003 | Consolidated Financial Reporting | M | W9a.14, W35.8 | W26 (budget) |
| FIN-004 | AP with 3-Way Match | M | W7 (AP processing), W18.9 (DSD 3-way) | W20.11 (VMI settlement), W23.9 (consignment) |
| FIN-005 | AR for B2B | M | W8 (AR processing), W5b.4c (POS trade accounts) | W58 (corporate accounts), W94 (customer deposit management) |
| FIN-006 | Philippine VAT (12%) | M | W5b (POS selling), W9a.16 (VAT return), W11/W19 (ecommerce VAT) | W12 (returns — VAT reversal) |
| FIN-007 | Withholding Tax (Expanded) | M | W7.9a (EWT computation), W9a.16a (EWT remittance) | W7c (non-PO EWT on services) |
| FIN-008 | BIR Tax Return Generation | M | W9a.16 (VAT, income tax), W9a.16a (EWT), W9a.16c (LBT) | W10.11 (statutory contribution files), W90 (monthly tax filing & statutory remittance) |
| FIN-009 | Multi-Bank Integration | S | W30.2 (bank statement import), W30.7 (cash sweeps) | W7.9 (payment file generation), W89 (bank reconciliation) |
| FIN-010 | Cash Management / Treasury | S | W30 (daily treasury), W5f (store cash reconciliation) | W25 (petty cash), W89 (bank reconciliation), W99 (payment settlement reconciliation) |
| FIN-011 | Fixed Asset Management | M | W21.7–8 (asset creation & depreciation), W39 (disposal) | W16 (new store capex) |
| FIN-012 | Budgeting & Variance Analysis | S | W26 (annual budget), W35.9 (monthly variance) | W21.3 (budget check) |
| FIN-013 | Landed Cost Calculation | M | W2b.12 (import landed cost) | W66.8 (inter-island freight allocation) |
| FIN-014 | Multi-Currency | M | W2b.12–13 (import FX), W9a.5a (FX revaluation) | W30.10 (USD accounts) |
| FIN-015 | Period-End Close Workflow | M | W9a (month-end close), W9b (year-end close) | — |
| FIN-016 | Capex Workflow | M | W21 (capex request & approval) | W16 (new store capex) |
| FIN-017 | Petty Cash Management | M | W25 (petty cash lifecycle) | W47 (facility maintenance), W82 (small disposal costs) |
| FIN-018 | Consignment Settlement | S | W23 (consignment operations) | W7 (AP settlement) |
| FIN-019 | Vendor Rebate Management | S | W27 (rebate accrual & settlement) | W7.9b (credit memo) |
| FIN-020 | Duplicate Vendor Invoice Detection | M | W7 (duplicate detection engine, blocks and alerts) | W70 (credit note aging — duplicate overrides) |
| FIN-021 | FX Hedging / Forward Contract Management | S | W80 (forward contract lifecycle, settlement, MTM reporting) | W2b (import POs — exposure source), W9a.5a (month-end FX revaluation), W30 (treasury cash position) |
| FIN-022 | Bad Debt Write-Off & Recovery | M | W81 (bad debt provisioning, write-off with BIR documentation, recovery tracking) | W8.8a (AR collection escalation — feeds into write-off), W9a (month-end provision posting), W24 (credit block on written-off accounts) |

## R2. Inventory Management (INV)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| INV-001 | Perpetual Inventory | M | W3.7 (GR posting), W5b.8 (POS deduction), W4.12 (transfer receipt) | W6 (cycle counts) |
| INV-002 | Real-Time Inventory Visibility | M | W4 (replenishment), W11.1 (BOPIS ATP), W19.1 (delivery ATP) | W22 (transfer availability check) |
| INV-003 | Weighted Average Cost (WAC) | M | W3.7 (receipt WAC recalc), W9a.6a (WAC verification) | W46.7 (kit costing) |
| INV-004 | ABC Classification | M | W31.8 (classification review), W42 (tiered count strategy) | W1 (assortment review) |
| INV-005 | Multi-Location Stock Transfer | M | W4 (DC→Store), W22 (store-to-store, inter-DC) | W45 (closure redistribution) |
| INV-006 | Cycle Counting | M | W6 (cycle counting) | W42 (annual physical inventory) |
| INV-007 | Physical Inventory (Wall-to-Wall) | M | W42 (annual physical inventory) | W6 (cycle counts feed C-item validation) |
| INV-008 | Lot & Serial Tracking | S | W5b.4b (POS batch capture), W29 (recall tracing) | W33 (warranty serial lookup) |
| INV-009 | Consignment Inventory | S | W23 (consignment operations) | — |
| INV-010 | Catch-Weight / Variable Measure | M | W5b.2 (POS catch-weight), W3b.3 (yard catch-weight), W22 (transfer catch-weight) | W18 (DSD catch-weight) |
| INV-011 | Inventory Aging Analysis | S | W1 (slow-mover review), W9a.16b (NRV review) | W13.9b (clearance disposition), W93 (markdown & clearance pricing for aging inventory) |
| INV-012 | Safety Stock & Reorder Point | M | W2a.1 (ROP calculation), W31.8 (parameter governance) | W56 (backorder — insufficient ROP) |
| INV-013 | Batch/LOT Tracking for Paint | S | W3.4 (shelf-life capture), W4.5 (FEFO picking) | W6 (near-expiry alerting) |
| INV-014 | In-Transit Inventory | M | W4.8 (DC→Store in-transit), W22.6 (transfer in-transit) | W66 (inter-island in-transit) |
| INV-015 | Inventory Valuation Reports | M | W9a.6 (inventory valuation), W42.17 (physical inventory summary) | W35.10 (store P&L) |
| INV-016 | Product Recall Tracking | S | W29 (product recall execution) | — |
| INV-017 | Consignment Inventory Tracking | M | W23 (consignment operations — non-valuated receipt, ownership transfer at sale) | W42 (vendor-owned inventory during physical count) |
| INV-018 | VMI Inventory Tracking | S | W20 (VMI operations) | W42 (vendor-owned inventory during physical count) |

## R3. Procurement & Purchasing (PUR)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| PUR-001 | Purchase Order Management | M | W2a (auto-replenishment), W2b (import PO), W2c (blanket PO) | W38 (special order PO), W60 (emergency PO) |
| PUR-002 | Automated Replenishment | M | W2a.1–2 (ROP/EOQ auto-generate), W31.6 (forecast release) | W57 (promo stock PO) |
| PUR-003 | Vendor Management | M | W36 (vendor onboarding), W44 (vendor scorecard) | W62 (non-PO contracts) |
| PUR-004 | Import Purchase Orders | M | W2b (import PO lifecycle) | W32 (seasonal import PO) |
| PUR-005 | 3-Way Matching | M | W7.2–3 (3-way match engine) | W18.9 (DSD 3-way) |
| PUR-006 | Blanket/Contract POs | S | W2c (blanket PO lifecycle) | — |
| PUR-007 | Vendor Portal | N | W2a.7 (vendor portal PO access), W36.9 (portal provisioning) | W20.1 (VMI data sharing) |
| PUR-008 | Vendor Performance Scorecard | S | W44 (vendor performance review) | W18b.5 (DSD no-show tracking) |
| PUR-009 | Multi-Entity Procurement | M | W2a (central buying), W14 (IC service fees) | — |
| PUR-010 | Approval Workflow | M | W2a.5–6 (PO approval tiers), W21.4 (capex approval), W24.5 (credit approval) | W7c.3 (non-PO approval) |
| PUR-011 | Goods Receipt Processing | M | W3 (DC receiving), W18 (store DSD receiving) | W20.6 (VMI receipt) |
| PUR-012 | Return to Vendor | M | W88 (RTV processing — full lifecycle) | W3.6a–b (DC receiving RTV), W23.10 (consignment return), W33.6 (warranty RTV) |
| PUR-013 | Direct Store Delivery | M | W18 (DSD receiving), W18b (DSD scheduling) | — |
| PUR-014 | Vendor Managed Inventory | S | W20 (VMI operations) | — |
| PUR-015 | Vendor Rebate Management | S | W27 (rebate accrual & settlement) | — |
| PUR-016 | Configurable AQL Sampling per SKU Category | S | W3 (AQL inspection standards per category at goods receipt) | W44 (vendor scorecard — quality reject rate) |

## R4. Warehouse Management (WMS)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| WMS-001 | RF/Barcode Directed Operations | M | W3 (receiving), W4 (pick/pack/ship), W6 (cycle count) | W42 (physical inventory) |
| WMS-002 | Cross-Dock Capability | S | W3 (cross-dock flow for fast-movers) | — |
| WMS-003 | Wave/Zone Picking | S | W4.3–5 (wave planning & picking) | — |
| WMS-004 | Receiving & Putaway | M | W3 (DC receiving & putaway) | W18 (DSD — no putaway) |
| WMS-005 | Shipping & Dispatch | M | W4.6–7 (pack & load), W19.6–8 (ecommerce shipping) | — |
| WMS-006 | Yard Management | S | W3b (yard & outdoor inventory) | — |
| WMS-007 | Label Printing | M | W63 (shelf label distribution) | W46.6 (kit barcode labels) |
| WMS-008 | WMS Integration with ERP | M | W4 (replenishment), W3 (receiving), W19 (ecommerce fulfillment) | W22 (transfers) |

## R5. POS & Retail (POS)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| POS-001 | 1,000 POS Terminals | M | W5b (in-store selling), W16 (new store POS setup) | W45 (store closure decommission) |
| POS-002 | Offline Mode | M | W5g (offline POS recovery & reconciliation) | W49 (typhoon — degraded mode) |
| POS-003 | Barcode Scanning | M | W5b.4 (barcode scanning at checkout) | W3.4 (receiving scan), W6.3 (cycle count scan) |
| POS-004 | Multi-Tender | M | W5b.7 (multi-tender payment), W12a.6 (split-tender refund) | — |
| POS-005 | Loyalty Integration | M | W5b.5 (loyalty scan), W17 (loyalty program operations) | — |
| POS-006 | Price Override (w/ Auth) | M | W5b.4a (price override with manager authorization) | W61 (competitor price match) |
| POS-007 | Returns & Exchanges | M | W12a (in-store returns), W12b (online returns), W12c (cross-store returns) — loyalty points reversal on all return types | — |
| POS-008 | Cash Drawer Management | M | W5a.4 (cash float), W5f.2–5 (Z-report & cash count) | W89 (bank reconciliation), W99 (payment settlement reconciliation) |
| POS-009 | End-of-Day Reconciliation | M | W5f (store closing & EOD) | W30.4 (deposit auto-matching), W89 (bank reconciliation), W99 (payment settlement reconciliation) |
| POS-010 | Quantity Break Pricing | M | W5b.6 (auto quantity breaks), W40.15–19 (quantity break setup) | — |
| POS-011 | Customer Display | S | W5b.4–7 (customer-facing display during checkout) | — |
| POS-012 | Receipt Printing | M | W5b.8 (BIR-registered receipt) | — |
| POS-013 | Real-Time Inventory Deduction | M | W5b.8 (inventory deduction at sale), W5g.5 (offline reconciliation) | — |
| POS-014 | Promotional Pricing Auto-Apply | M | W13.7 (auto-apply at POS), W5b.6 (system calculates promos) | — |
| POS-015 | Gift Card / Store Credit | S | W28 (gift card & store credit lifecycle) | W12a.6 (store credit from returns) |
| POS-016 | Catch-Weight / Variable Measure at POS | M | W5b.2 (catch-weight selling) | W3b.3 (catch-weight receiving), W22 (catch-weight transfer) |
| POS-017 | Paint Mixing / Custom SKU at POS | M | W5b.3 (paint mixing) | — |
| POS-018 | Age-Restricted Product Prompts | S | W5b.9 (age-restricted prompts) | — |
| POS-019 | Warranty Claim Registration | S | W33 (warranty claim processing) | — |
| POS-020 | Layaway / Installment Sales | S | W75 (layaway agreement lifecycle — exercises POS-004, POS-015, FIN-005) | — |
| POS-021 | Multi-DC Order Splitting | S | W19 (multi-DC order splitting logic) | — |
| POS-022 | Employee Discount at POS | S | W5b.12 (employee purchase with discount, limits, logging) | W17 (employee purchases excluded from loyalty points) |

## R6. Ecommerce Integration (ECOM)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| ECOM-001 | Real-Time Inventory Sync | M | W11 (BOPIS ATP), W19 (delivery ATP) | W50 (catalog sync) |
| ECOM-002 | Real-Time Price Sync | M | W13.5 (promo price push), W40.7 (price sync) | — |
| ECOM-003 | BOPIS Order Flow | M | W11 (BOPIS fulfillment) | — |
| ECOM-004 | Home Delivery Order Flow | M | W19 (home delivery fulfillment) | — |
| ECOM-005 | Order Status Tracking | M | W19.9 (tracking link), W41.E (ecommerce issue resolution) | — |
| ECOM-006 | Payment Gateway Integration | M | W19 (payment reconciliation), W11.1 (BOPIS payment) | — |
| ECOM-007 | Return Initiation (Online) | M | W12b (online returns), W19.12a (home delivery reverse logistics) | — |
| ECOM-008 | Customer Data Sync | M | W17 (loyalty data), W41 (complaint data) | W24 (customer master) |
| ECOM-009 | Product Catalog Sync | M | W50 (PIM / product content management) | — |
| ECOM-010 | Promo/Coupon Integration | S | W13 (digital coupon management) | — |
| ECOM-011 | Home Delivery Fulfillment | M | W19 (full home delivery lifecycle including failed delivery) | — |
| ECOM-012 | Delivery Partner Integration | M | W19.7 (3PL API integration), W66 (inter-island logistics) | — |

## R7. Supply Chain Planning (SCP)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| SCP-001 | Demand Forecasting | S | W31 (demand forecasting cycle) | W32 (seasonal planning) |
| SCP-002 | Replenishment Planning | M | W4.1 (auto replenishment), W57 (promo stock allocation) | — |
| SCP-003 | Reorder Point Calculation | M | W2a.1 (ROP breach), W31.8 (parameter governance) | — |
| SCP-004 | Safety Stock Optimization | S | W31.8 (safety stock review) | — |
| SCP-005 | Seasonal Planning | S | W32 (seasonal buy planning) | W13 (promo calendar) |
| SCP-006 | Allocation Management | S | W4.2 (constrained allocation), W57 (promo allocation) | — |
| SCP-007 | Purchase Recommendation | M | W2a.1–2 (auto-suggest POs), W31.6 (forecast-driven POs) | W56 (backorder triggers PO) |

## R8. HR & Payroll (HR)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| HR-001 | Multi-Entity Payroll | M | W10 (payroll processing — 5 entities × 2 runs) | W43.15 (cross-entity transfer) |
| HR-002 | Philippine Statutory Deductions | M | W10.4 (SSS, PhilHealth, Pag-IBIG) | — |
| HR-003 | BIR Withholding Tax (Compensation) | M | W10.4 (TRAIN law tables) | W43.10 (final pay computation) |
| HR-004 | 13th Month Pay Computation | M | W10 (13th month auto-calc), W43.10 (pro-rated final pay) | W9b.18 (year-end accrual) |
| HR-005 | Time & Attendance Integration | S | W10.1 (biometric import), W34 (shift scheduling) | — |
| HR-006 | Shift Scheduling | S | W34 (store shift scheduling) | — |
| HR-007 | Leave Management | M | W10.2 (leave verification), W34.1d (leave in scheduling) | — |
| HR-008 | Employee Self-Service | N | W10.10 (payslip distribution), W17.5 (loyalty balance inquiry) | — |
| HR-009 | Recruitment & Onboarding | N | W15 (recruitment & onboarding) | W16 (new store hiring) |
| HR-010 | Overtime Calculation | M | W10.3 (OT calculation per Labor Code) | W34.8 (scheduled vs. actual hours) |
| HR-011 | Holiday Pay Calculation | M | W10.3 (holiday pay rates) | — |
| HR-012 | Bank File Generation | M | W10.7 (bank file for payroll crediting) | — |

## R9. CRM & Loyalty (CRM)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| CRM-001 | Loyalty Points Engine | M | W17 (loyalty program operations) | W5b.5 (POS points earning) |
| CRM-002 | Customer Master (B2C) | M | W17.1–2 (enrollment & dedup), W50 (ecommerce customer sync) | — |
| CRM-003 | Trade Account Management | M | W8 (AR processing, dormant account management), W5b.4c (trade pricing at POS) | W24 (credit application) |
| CRM-004 | Corporate Account Management | M | W58 (corporate/project accounts), W24 (credit application), W162 (Project Quotation), W163 (Contract Pricing), W164 (Staged Delivery), W165 (Milestone Billing), W166 (Tendering) | — |
| CRM-005 | Tiered Loyalty | S | W17.8 (tier movement) | — |
| CRM-006 | Customer Purchase History | S | W12a.2 (transaction lookup), W17 (loyalty history) | W29 (recall customer tracing) |
| CRM-007 | Marketing Campaign Integration | N | W13 (promotions), W65 (CSAT/NPS surveys) | — |
| CRM-008 | Credit Application Workflow | M | W24 (credit application & approval) | W8.3 (credit limit enforcement) |

## R10. Analytics & Reporting (RPT)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| RPT-001 | Executive Dashboard | M | W35.2 (daily flash), W35.4 (weekly sales) | — |
| RPT-002 | Store P&L | M | W35.10 (store P&L with occupancy allocation) | W26 (budget variance) |
| RPT-003 | Sales Analytics | M | W35.4 (week-on-week sales), W13.8 (promo performance) | W31.7 (forecast vs. actual) |
| RPT-004 | Inventory Reports | M | W6 (cycle count variance), W9a.6 (inventory valuation) | W42.17 (physical inventory summary) |
| RPT-005 | Purchase Analysis | S | W44 (vendor scorecard), W27 (rebate analytics) | — |
| RPT-006 | BIR-Compliant Tax Reports | M | W9a.16 (VAT returns), W9a.16a (EWT remittance) | — |
| RPT-007 | Consolidated Financial Statements | M | W9a.14 (consolidated statements) | — |
| RPT-008 | Ad-Hoc Reporting | S | W35.18–19 (ad-hoc reports & BI analyses) | — |
| RPT-009 | Mobile Dashboard | N | W35.2 (CFO mobile dashboard) | — |
| RPT-010 | Scheduled Report Distribution | S | W35 (full reporting rhythm — daily/weekly/monthly) | — |

## R11. Intercompany & Transfer Pricing (IC)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| IC-001 | IC AP/AR Automation | M | W14 (IC transactions & settlement) | — |
| IC-002 | Arm's-Length Transfer Pricing | M | W14 (transfer pricing rules), W14 annual review | — |
| IC-003 | IC Elimination on Consolidation | M | W9a.13 (IC elimination) | — |
| IC-004 | IC Settlement | M | W14.6–7 (net settlement) | — |
| IC-005 | IC Reconciliation | M | W14.4–5 (IC reconciliation) | — |

## R12. Document Management (DOC)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| DOC-001 | Electronic Document Storage | M | W7.1 (invoice capture), W21.1 (capex attachments), W33.3 (warranty photos) | W50 (digital assets) |
| DOC-002 | BIR-Compliant Invoice Format | M | W5b.8 (BIR-registered receipt), W7 (vendor invoices) | — |
| DOC-003 | Delivery Receipt Tracking | M | W18.7 (DR capture), W3 (DC receiving DR) | — |
| DOC-004 | Import Document Management | M | W2b (BL, LC, customs docs), W36 (vendor permits) | — |
| DOC-005 | Document Retention Policy | M | W35 quarterly review, W42 (7-year archive) | W53 (breach register 5-year retention), W81 (bad debt write-off 7-year retention) |
| DOC-006 | Approval Workflow with Attachments | S | W21 (capex with quotes), W62 (contracts with attachments) | — |
| DOC-007 | Hazardous Waste Disposal Tracking | S | W82 (DENR-compliant manifest tracking, per-location generator registration, quarterly reporting), W167 (Recycling / Circular Economy) | W52 (fleet — used oil/battery disposal), W68 (discontinued chemical waste) |

## R13. Master Data Management (MDM)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| MDM-001 | Centralized Item Master | M | W1.7 (SKU creation), W46.1 (kit BOM), W64 (pilot SKU) | W50 (PIM content) |
| MDM-002 | Item Attribute Management | M | W50.4 (category-specific attributes), W1 (assortment) | — |
| MDM-003 | Customer Data Quality | M | W17 (deduplication at enrollment), W24 (credit data validation) | — |
| MDM-004 | Vendor Onboarding Workflow | S | W36 (vendor onboarding lifecycle) | — |
| MDM-005 | Pricing Master Governance | M | W40 (price change with approval), W13 (promo pricing with approval) | W61 (price match analytics) |
| MDM-006 | Location Master | M | W16.4 (new store creation), W54 (LGU permit data), W45 (closure deactivation) | — |
| MDM-007 | Hierarchical Category Structure | M | W1 (category management), W50 (category navigation) | — |

## R14. Non-Functional Requirements (NFR)

| Req ID | Requirement | Target | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| NFR-001 | POS Uptime | 99.9% | W5g (offline recovery), W55 (DR failover) | W48 (helpdesk P1 SLA) |
| NFR-002 | Back-Office Uptime | 99.5% | W55 (IT disaster recovery) | W48 (incident management) |
| NFR-003 | POS Transaction Speed | < 3 sec | W5b (POS selling) | — |
| NFR-004 | Report Generation | < 30 sec | W35 (management reporting) | — |
| NFR-005 | Concurrent Users | 1,000–1,500 | W5b (1,000 POS terminals), W35 (HQ reporting) | — |
| NFR-006 | Data Retention | 7 years | W42 (physical inventory archive), W35 quarterly retention review | Data Volumes §1.2 |
| NFR-007 | Security | RBAC, audit trails | W37 (POS audit), W48 (change management), W186 (SOP governance) | W53 (breach response) |
| NFR-008 | Scalability | 300+ stores | W16 (new store opening process), W45 (store closure) | — |
| NFR-009 | Localization | Full PH | W9a (BIR compliance), W10 (payroll statutory), W54 (LGU permits) | — |
| NFR-010 | Data Privacy | RA 10173 | W53 (breach response), W41 (DSAR handling), W17.2 (consent management) | — |
| NFR-011 | Offline POS | ≥ 8 hours | W5g (offline POS recovery & reconciliation) | W49 (typhoon degraded mode) |
| NFR-012 | Integration Capability | All touchpoints | W3–W7 (core integrations), W19 (3PL), W30 (banking) | Data Volumes §3 |
| NFR-013 | Disaster Recovery | RPO ≤ 1h, RTO ≤ 4h | W55 (IT DR & failover) | W49 (physical disaster BC) |
| NFR-014 | Data Migration | Legacy → ERP | Implementation Roadmap §3 (data migration plan) | — |
| NFR-015 | Batch Processing Windows | Off-peak | Data Volumes §5 (batch windows), W9a (month-end) | — |
| NFR-016 | Data Privacy Breach Response | RA 10173 | W53 (full breach response lifecycle) | W41 (DSAR) |
| NFR-017 | LGU Business Permit Tracking | Per location | W54 (LGU permit renewal per location) | W16 (new store initial permit) |
| NFR-018 | ESG & Sustainability Reporting | S | W192 (GHG tracking), W193 (Waste diversion) | W194 (CSR), W195 (Ethical audit) |
| NFR-019 | Advanced Fleet Optimization | S | W196 (Route optimization), W199 (Telematics) | W197 (Driver performance), W198 (Fuel) |
| NFR-020 | AI & Innovation Framework | N | W200 (AI Personalization), W201 (RPA) | W202 (Predictive maint), W203 (Computer vision) |

---

## Coverage Validation

- **Total requirements**: 105+ across 14 categories
- **Requirements with primary workflow mapping**: All ✅

---

*Date: 2026-05-31 (v15 — gap analysis: added W192–W203; total now 203 workflows)*
