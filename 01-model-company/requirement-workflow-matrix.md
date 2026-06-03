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
| FIN-001 | Multi-entity GL | M | W9A (month-end close), W14 (IC transactions) | W10 (payroll GL posting), W30 (treasury) |
| FIN-002 | Automated IC Elimination | M | W9A.13, W14.8, W234 (IC profit elimination) | — |
| FIN-003 | Consolidated Financial Reporting | M | W9A.14, W35.8 | W26 (budget) |
| FIN-004 | AP with 3-Way Match | M | W7 (AP processing), W18.9 (DSD 3-way) | W20.11 (VMI settlement), W23.9 (consignment), W7D (AP vendor statement reconciliation), W100 (vendor statement reconciliation — finance), W244 (vendor invoice dispute & discrepancy resolution) |
| FIN-005 | AR for B2B | M | W8 (AR processing), W5B.4c (POS trade accounts), W229 (B2B credit limit exception), W108 (customer credit collection & escalation) | W58 (corporate accounts), W94 (customer deposit management), W101 (customer refund & credit processing) |
| FIN-006 | Philippine VAT (12%) | M | W5B (POS selling), W9A.16 (VAT return), W11/W19 (ecommerce VAT), W217 (SC/PWD VAT-exemption), W239 (customs duty recon) | W12 (returns — VAT reversal) |
| FIN-007 | Withholding Tax (Expanded) | M | W7.9a (EWT computation), W9A.16a (EWT remittance) | W7C (non-PO EWT on services) |
| FIN-008 | BIR Tax Return Generation | M | W9A.16 (VAT, income tax), W9A.16a (EWT), W9A.16c (LBT), W216 (BIR CAS audit), W217 (SC/PWD reporting) | W10.11 (statutory contribution files), W90 (monthly tax filing & statutory remittance) |
| FIN-009 | Multi-Bank Integration | S | W30.2 (bank statement import), W30.7 (cash sweeps) | W7.9 (payment file generation), W89 (bank reconciliation) |
| FIN-010 | Cash Management / Treasury | S | W30 (daily treasury), W5F (store cash reconciliation), W232 (LC lifecycle), W233 (liquidity forecasting), W174 (store-level CIT & armored car management) | W25 (petty cash), W89 (bank reconciliation), W99 (payment settlement reconciliation) |
| FIN-011 | Fixed Asset Management | M | W21.7–8 (asset creation & depreciation), W39 (disposal), W240 (DC equipment PM), W241 (HQ asset PM), W184 (fixed asset physical verification audit) | W16 (new store capex) |
| FIN-012 | Budgeting & Variance Analysis | S | W26 (annual budget), W35.9 (monthly variance), W85 (product costing & margin analysis review) | W21.3 (budget check) |
| FIN-013 | Landed Cost Calculation | M | W2B.12 (import landed cost), W239 (customs duty tax recon), W249 (port demurrage fee allocation) | W66.8 (inter-island freight allocation) |
| FIN-014 | Multi-Currency | M | W2B.12–13 (import FX), W9A.5a (FX revaluation), W232 (LC lifecycle) | W30.10 (USD accounts) |
| FIN-015 | Period-End Close Workflow | M | W9 (financial close & reporting — parent workflow), W9A (month-end close), W9B (year-end close) | — |
| FIN-016 | Capex Workflow | M | W21 (capex request & approval), W226 (store renovation capex) | W16 (new store capex) |
| FIN-017 | Petty Cash Management | M | W25 (petty cash lifecycle) | W47 (facility maintenance), W82 (small disposal costs) |
| FIN-018 | Consignment Settlement | S | W23 (consignment operations) | W7 (AP settlement) |
| FIN-019 | Vendor Rebate Management | S | W27 (rebate accrual & settlement) | W7.9b (credit memo) |
| FIN-020 | Duplicate Vendor Invoice Detection | M | W7 (duplicate detection engine, blocks and alerts) | W70 (credit note aging — duplicate overrides) |
| FIN-021 | FX Hedging / Forward Contract Management | S | W80 (forward contract lifecycle, settlement, MTM reporting) | W2B (import POs — exposure source), W9A.5a (month-end FX revaluation), W30 (treasury cash position) |
| FIN-022 | Bad Debt Write-Off & Recovery | M | W81 (bad debt provisioning, write-off with BIR documentation, recovery tracking) | W8.8a (AR collection escalation — feeds into write-off), W9A (month-end provision posting), W24 (credit block on written-off accounts) |
| FIN-023 | Insurance Policy Lifecycle Management | S | W59 (insurance policy lifecycle management — registry, premiums, claims, renewal) | W21 (capex — insurance for new assets) |
| FIN-024 | Employee Gratuity & Retirement Fund (RA 7641) | M | W175 (employee gratuity & retirement fund management per RA 7641) | W10 (payroll — retirement accrual posting), W43 (separation — retirement pay computation) |
| FIN-025 | Cash-in-Transit (CIT) & Armored Car Management | S | W174 (store-level CIT & armored car scheduling, custody transfer, reconciliation) | W30 (treasury — deposit confirmation), W5F (store EOD — cash handoff to CIT) |
| FIN-026 | Product Costing & Margin Analysis | S | W85 (product costing & margin analysis review — standard vs. actual, landed cost roll-up) | W9A (month-end cost variance posting), W35 (margin reporting) |
| FIN-027 | Customer Refund & Credit Processing | M | W101 (customer refund & credit processing — cash, card, store credit, BIR credit notes) | W12A (in-store returns — refund trigger), W99 (payment settlement reconciliation) |
| FIN-028 | Customer Credit Collection & Escalation | M | W108 (customer credit collection & escalation — call logging, promise-to-pay, aging escalation) | W8 (AR processing — collection feed), W81 (bad debt write-off — escalation outcome) |
| FIN-029 | Intercompany Dividend & Loan Management | S | W137 (intercompany dividend & loan management — declaration, interest, amortization) | W14 (IC settlement — net settlement), W9A (month-end — IC interest posting) |
| FIN-030 | Fixed Asset Physical Verification | S | W184 (fixed asset physical verification — tag scanning, missing flagging, reconciliation) | W39 (asset disposal — verification input), W21 (capex — new asset verification) |

## R2. Inventory Management (INV)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| INV-001 | Perpetual Inventory | M | W3.7 (GR posting), W5B.8 (POS deduction), W4.12 (transfer receipt), W219 (quarantine status adjustments), W109 (store-level inventory receiving & putaway) | W6 (cycle counts), W220 (SLOB actual write-offs), W91 (damaged & defective goods disposition), W92 (inventory adjustment & shrinkage authorization) |
| INV-002 | Real-Time Inventory Visibility | M | W4 (replenishment), W11.1 (BOPIS ATP), W19.1 (delivery ATP) | W22 (transfer availability check) |
| INV-003 | Weighted Average Cost (WAC) | M | W3.7 (receipt WAC recalc), W9A.6a (WAC verification) | W46.7 (kit costing) |
| INV-004 | ABC Classification | M | W31.8 (classification review), W42 (tiered count strategy) | W1 (assortment review) |
| INV-005 | Multi-Location Stock Transfer | M | W4 (DC→Store), W22 (store-to-store, inter-DC), W204 (regional expedited transfer), W214 (store-to-store expedited), W218 (inter-DC push), W22A (store-level outbound transfer fulfillment), W22B (store-to-DC return — excess/damaged) | W45 (closure redistribution), W4B (store-initiated replenishment request) |
| INV-006 | Cycle Counting | M | W6 (cycle counting), W248 (store variance LP investigation) | W42 (annual physical inventory) |
| INV-007 | Physical Inventory (Wall-to-Wall) | M | W42 (annual physical inventory), W248 (store variance LP investigation) | W6 (cycle counts feed C-item validation) |
| INV-008 | Lot & Serial Tracking | S | W5B.4b (POS batch capture), W29 (recall tracing) | W33 (warranty serial lookup) |
| INV-009 | Consignment Inventory | S | W23 (consignment operations) | — |
| INV-010 | Catch-Weight / Variable Measure | M | W5B.2 (POS catch-weight), W3B.3 (yard catch-weight), W22 (transfer catch-weight) | W18 (DSD catch-weight) |
| INV-011 | Inventory Aging Analysis | S | W1 (slow-mover review), W9A.16b (NRV review), W220 (SLOB provisioning & liquidation) | W13.9b (clearance disposition), W93 (markdown & clearance pricing for aging inventory) |
| INV-012 | Safety Stock & Reorder Point | M | W2A.1 (ROP calculation), W31.8 (parameter governance) | W56 (backorder — insufficient ROP) |
| INV-013 | Batch/LOT Tracking for Paint | S | W3.4 (shelf-life capture), W4.5 (FEFO picking) | W6 (near-expiry alerting) |
| INV-014 | In-Transit Inventory | M | W4.8 (DC→Store in-transit), W22.6 (transfer in-transit), W250 (supply chain control tower visibility) | W66 (inter-island in-transit) |
| INV-015 | Inventory Valuation Reports | M | W9A.6 (inventory valuation), W42.17 (physical inventory summary) | W35.10 (store P&L) |
| INV-016 | Product Recall Tracking | S | W29 (product recall execution) | — |
| INV-017 | Consignment Inventory Tracking | M | W23 (consignment operations — non-valuated receipt, ownership transfer at sale) | W42 (vendor-owned inventory during physical count) |
| INV-018 | VMI Inventory Tracking | S | W20 (VMI operations) | W42 (vendor-owned inventory during physical count) |
| INV-019 | Multi-Channel Inventory Allocation Governance | S | W105 (multi-channel inventory allocation & priority governance — reservation rules per channel) | W11 (BOPIS — channel reservation), W19 (home delivery — channel reservation) |
| INV-020 | Proactive Store Inventory Rebalancing | S | W154 (proactive store inventory rebalancing — system-suggested rebalancing) | W22 (transfers — execution vehicle), W4B (store-initiated request — demand signal) |

## R3. Procurement & Purchasing (PUR)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| PUR-001 | Purchase Order Management | M | W2 (procurement PO cycle — parent workflow), W2A (auto-replenishment), W2B (import PO), W2C (blanket PO), W246 (drop-ship back-to-back PO) | W38 (special order PO), W60 (emergency PO) |
| PUR-002 | Automated Replenishment | M | W2A.1–2 (ROP/EOQ auto-generate), W31.6 (forecast release) | W57 (promo stock PO) |
| PUR-003 | Vendor Management | M | W36 (vendor onboarding), W44 (vendor scorecard), W230 (legal contract review), W115 (supplier diversity & MSME development), W155 (vendor strategic collaboration & JBP), W62B (3PL/delivery partner onboarding & offboarding) | W62 (non-PO contracts), W160 (private label factory audit) |
| PUR-004 | Import Purchase Orders | M | W2B (import PO lifecycle), W232 (LC lifecycle), W239 (customs duty recon), W249 (port demurrage management), W250 (import shipment control tower tracking) | W32 (seasonal import PO) |
| PUR-005 | 3-Way Matching | M | W7.2–3 (3-way match engine) | W18.9 (DSD 3-way) |
| PUR-006 | Blanket/Contract POs | S | W2C (blanket PO lifecycle) | — |
| PUR-007 | Vendor Portal | N | W2A.7 (vendor portal PO access), W36.9 (portal provisioning) | W20.1 (VMI data sharing) |
| PUR-008 | Vendor Performance Scorecard | S | W44 (vendor performance review), W242 (3PL performance review), W245 (supplier compliance chargebacks), W161 (vendor price protection & market markdown claims) | W18B.5 (DSD no-show tracking), W110 (supplier quality CAPA — quality metrics) |
| PUR-009 | Multi-Entity Procurement | M | W2A (central buying), W14 (IC service fees) | — |
| PUR-010 | Approval Workflow | M | W2A.5–6 (PO approval tiers), W21.4 (capex approval), W24.5 (credit approval) | W7C.3 (non-PO approval) |
| PUR-011 | Goods Receipt Processing | M | W3 (DC receiving), W18 (store DSD receiving), W3C (DC inbound delivery scheduling) | W20.6 (VMI receipt) |
| PUR-012 | Return to Vendor | M | W88 (RTV processing — full lifecycle) | W3.6a–b (DC receiving RTV), W23.10 (consignment return), W33.6 (warranty RTV) |
| PUR-013 | Direct Store Delivery | M | W18 (DSD receiving), W18B (DSD scheduling) | — |
| PUR-014 | Vendor Managed Inventory | S | W20 (VMI operations) | — |
| PUR-015 | Vendor Rebate Management | S | W27 (rebate accrual & settlement) | — |
| PUR-016 | Configurable AQL Sampling per SKU Category | S | W3 (AQL inspection standards per category at goods receipt) | W44 (vendor scorecard — quality reject rate), W150 (product quality testing & certification) |
| PUR-017 | Supplier Quality & CAPA | S | W110 (supplier quality & CAPA — quality issue logging, corrective action tracking) | W3 (goods receipt — quality hold), W44 (vendor scorecard — quality metrics) |
| PUR-018 | Indirect / Non-Merchandise Procurement | M | W136 (indirect / non-merchandise procurement — supplies, services, IT, facilities) | W21 (capex — equipment procurement), W7C (non-PO recurring expenses) |
| PUR-019 | Vendor Invoice Dispute & Discrepancy Resolution | M | W244 (vendor invoice dispute & discrepancy resolution — case creation, hold payment, resolution) | W7 (AP — 3-way match variance flagging), W7D (AP vendor statement reconciliation) |
| PUR-020 | Vendor Price Protection & Market Markdown Claims | S | W161 (vendor price protection & market markdown claims — claim filing, credit memo) | W40 (price change — trigger for price protection), W27 (rebate — related vendor credits) |
| PUR-021 | Vendor Strategic Collaboration & JBP | S | W155 (vendor strategic collaboration & joint business planning — JBP documentation, scorecard) | W1 (assortment review — JBP input), W13 (promotions — co-investment tracking) |
| PUR-022 | Private Label Factory Audit & Social Compliance | S | W160 (private label factory audit & social compliance — audit scheduling, scoring, corrective action) | W36 (vendor onboarding — factory qualification), W44 (vendor scorecard — compliance score) |
| PUR-023 | Supplier Diversity & MSME Development Program | S | W115 (supplier diversity & MSME development — classification, spend reporting, development tracking) | W36 (vendor onboarding — MSME classification) |
| PUR-024 | Product Quality Testing & Certification | S | W150 (product quality testing & certification — test request, result recording, certificate tracking) | W3 (goods receipt — test trigger), W110 (supplier quality CAPA — failed test feed) |

## R4. Warehouse Management (WMS)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| WMS-001 | RF/Barcode Directed Operations | M | W3 (receiving), W4 (pick/pack/ship), W6 (cycle count) | W42 (physical inventory) |
| WMS-002 | Cross-Dock Capability | S | W3 (cross-dock flow for fast-movers), W221 (cross-docking fast-moving bulky items) | — |
| WMS-003 | Wave/Zone Picking | S | W4.3–5 (wave planning & picking) | — |
| WMS-004 | Receiving & Putaway | M | W3 (DC receiving & putaway) | W18 (DSD — no putaway) |
| WMS-005 | Shipping & Dispatch | M | W4.6–7 (pack & load), W19.6–8 (ecommerce shipping), W106 (DC outbound dispatch & load planning) | — |
| WMS-006 | Yard Management | S | W3B (yard & outdoor inventory), W222 (DC container yard & chassis management) | W188 (fleet spare parts & preventive maintenance — yard equipment) |
| WMS-007 | Label Printing | M | W63 (shelf label distribution) | W46.6 (kit barcode labels) |
| WMS-008 | WMS Integration with ERP | M | W4 (replenishment), W3 (receiving), W19 (ecommerce fulfillment) | W22 (transfers) |

## R5. POS & Retail (POS)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| POS-001 | 600 POS Terminals | M | W5B (in-store selling), W5 (daily store operations — parent workflow), W16 (new store POS setup) | W45 (store closure decommission) |
| POS-002 | Offline Mode | M | W5G (offline POS recovery & reconciliation) | W49 (typhoon — degraded mode) |
| POS-003 | Barcode Scanning | M | W5B.4 (barcode scanning at checkout) | W3.4 (receiving scan), W6.3 (cycle count scan) |
| POS-004 | Multi-Tender | M | W5B.7 (multi-tender payment), W12A.6 (split-tender refund) | — |
| POS-005 | Loyalty Integration | M | W5B.5 (loyalty scan), W17 (loyalty program operations) | — |
| POS-006 | Price Override (w/ Auth) | M | W5B.4a (price override with manager authorization) | W61 (competitor price match) |
| POS-007 | Returns & Exchanges | M | W12A (in-store returns), W12B (online returns), W12C (cross-store returns), W215 (home delivery returns) | — |
| POS-008 | Cash Drawer Management | M | W5A.4 (cash float), W5F.2–5 (Z-report & cash count), W212 (Smart Safe deposit) | W89 (bank reconciliation), W99 (payment settlement reconciliation) |
| POS-009 | End-of-Day Reconciliation | M | W5F (store closing & EOD), W212.5 (Smart Safe reconciliation) | W30.4 (deposit auto-matching), W89 (bank reconciliation), W99 (payment settlement reconciliation), W5D (in-store customer delivery scheduling — delivery EOD reconciliation), W5E (store opening delay procedure — delayed start EOD impact) |
| POS-010 | Quantity Break Pricing | M | W5B.6 (auto quantity breaks), W40.15–19 (quantity break setup) | — |
| POS-011 | Customer Display | S | W5B.4–7 (customer-facing display during checkout) | — |
| POS-012 | Receipt Printing | M | W5B.8 (BIR-registered receipt) | — |
| POS-013 | Real-Time Inventory Deduction | M | W5B.8 (inventory deduction at sale), W5G.5 (offline reconciliation) | — |
| POS-014 | Promotional Pricing Auto-Apply | M | W13.7 (auto-apply at POS), W5B.6 (system calculates promos) | — |
| POS-014a | Senior Citizen & PWD Discount Compliance | M | W170 (senior citizen & PWD discount compliance — PH legal, auto-detect and apply 20% discount, VAT-exemption for SC) | W217 (SC/PWD VAT-exemption reporting), W5B (POS — discount application) |
| POS-015 | Gift Card / Store Credit | S | W28 (gift card & store credit lifecycle) | W12A.6 (store credit from returns) |
| POS-016 | Catch-Weight / Variable Measure at POS | M | W5B.2 (catch-weight selling) | W3B.3 (catch-weight receiving), W22 (catch-weight transfer) |
| POS-017 | Paint Mixing / Custom SKU at POS | M | W5B.3 (paint mixing) | — |
| POS-018 | Age-Restricted Product Prompts | S | W5B.9 (age-restricted prompts) | — |
| POS-019 | Warranty Claim Registration | S | W33 (warranty claim processing) | — |
| POS-020 | Layaway / Installment Sales | S | W75 (layaway agreement lifecycle — exercises POS-004, POS-015, FIN-005) | — |
| POS-021 | Multi-DC Order Splitting | S | W19 (multi-DC order splitting logic) | — |
| POS-022 | Employee Discount at POS | S | W205 (employee purchase program), W5B.12 (staff discount logic) | W17 (employee purchases excluded from loyalty points) |
| POS-023 | Store-Level Customer Delivery Scheduling | S | W5D (in-store customer delivery scheduling — date/time slot, fee, dispatch) | W19 (home delivery — delivery partner handoff), W52 (fleet — own delivery) |

## R6. Ecommerce Integration (ECOM)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| ECOM-001 | Real-Time Inventory Sync | M | W11 (BOPIS ATP), W19 (delivery ATP) | W50 (catalog sync) |
| ECOM-002 | Real-Time Price Sync | M | W13.5 (promo price push), W40.7 (price sync) | — |
| ECOM-003 | BOPIS Order Flow | M | W11 (BOPIS fulfillment) | — |
| ECOM-004 | Home Delivery Order Flow | M | W19 (home delivery fulfillment) | — |
| ECOM-005 | Order Status Tracking | M | W19.9 (tracking link), W41.E (ecommerce issue resolution) | — |
| ECOM-006 | Payment Gateway Integration | M | W19 (payment reconciliation), W11.1 (BOPIS payment) | — |
| ECOM-007 | Return Initiation (Online) | M | W12B (online returns), W19.12a (home delivery reverse logistics), W215 (home delivery returns) | — |
| ECOM-008 | Customer Data Sync | M | W17 (loyalty data), W41 (complaint data) | W24 (customer master) |
| ECOM-009 | Product Catalog Sync | M | W50 (PIM / product content management) | — |
| ECOM-010 | Promo/Coupon Integration | S | W13 (digital coupon management) | — |
| ECOM-011 | Home Delivery Fulfillment | M | W19 (full home delivery lifecycle including failed delivery) | — |
| ECOM-012 | Delivery Partner Integration | M | W19.7 (3PL API integration), W66 (inter-island logistics), W242 (3PL performance review), W62B (3PL/delivery partner onboarding & offboarding) | — |
| ECOM-013 | Marketplace Integration (Lazada/Shopee) | S | W180 (e-commerce marketplace integration — listing sync, order pull, inventory reservation, commission reconciliation) | W50 (PIM — product content feed), W13 (promotions — marketplace pricing) |
| ECOM-014 | Ship-from-Store Fulfillment | S | W19B (ship from store — order routing, store pick & pack, carrier handoff) | W4 (replenishment — store stock for fulfillment), W11 (BOPIS — store pick infrastructure) |
| ECOM-015 | Omni-channel Customer Ticketing & Support | S | W258 (omni-channel customer ticketing & support management — unified tickets, routing, SLA, escalation) | W41 (complaint resolution — ticket source), W17 (loyalty — customer 360) |
| ECOM-016 | Ecommerce Order Exception & Cancellation Management | S | W98 (ecommerce order exception & cancellation management — payment failure, fraud hold, auto-refund) | W19 (home delivery — order lifecycle), W12B (online returns — cancellation trigger) |

## R7. Supply Chain Planning (SCP)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| SCP-001 | Demand Forecasting | S | W31 (demand forecasting cycle) | W32 (seasonal planning) |
| SCP-002 | Replenishment Planning | M | W4.1 (auto replenishment), W57 (promo stock allocation) | — |
| SCP-003 | Reorder Point Calculation | M | W2A.1 (ROP breach), W31.8 (parameter governance) | — |
| SCP-004 | Safety Stock Optimization | S | W31.8 (safety stock review) | — |
| SCP-005 | Seasonal Planning | S | W32 (seasonal buy planning), W191 (global supply chain — incoterm & marine insurance tracking) | W13 (promo calendar) |
| SCP-006 | Allocation Management | S | W4.2 (constrained allocation), W57 (promo allocation) | — |
| SCP-007 | Purchase Recommendation | M | W2A.1–2 (auto-suggest POs), W31.6 (forecast-driven POs) | W56 (backorder triggers PO), W133 (S&OP cycle — consensus demand input), W183 (supply chain network optimization review) |

## R8. HR & Payroll (HR)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| HR-001 | Multi-Entity Payroll | M | W10 (payroll processing — 5 entities × 2 runs) | W43.15 (cross-entity transfer) |
| HR-002 | Philippine Statutory Deductions | M | W10.4 (SSS, PhilHealth, Pag-IBIG) | — |
| HR-003 | BIR Withholding Tax (Compensation) | M | W10.4 (TRAIN law tables) | W43.10 (final pay computation) |
| HR-004 | 13th Month Pay Computation | M | W10 (13th month auto-calc), W43.10 (pro-rated final pay) | W9B.18 (year-end accrual) |
| HR-005 | Time & Attendance Integration | S | W10.1 (biometric import), W34 (shift scheduling) | — |
| HR-006 | Shift Scheduling | S | W34 (store shift scheduling) | — |
| HR-007 | Leave Management | M | W10.2 (leave verification), W34.1d (leave in scheduling) | — |
| HR-008 | Employee Self-Service | N | W10.10 (payslip distribution), W17.5 (loyalty balance inquiry) | — |
| HR-009 | Recruitment & Onboarding | N | W15 (recruitment & onboarding) | W16 (new store hiring) |
| HR-010 | Overtime Calculation | M | W10.3 (OT calculation per Labor Code), W228 (sales commission calculation) | W34.8 (scheduled vs. actual hours), W74 (employee expense reimbursement — OT meal allowance) |
| HR-011 | Holiday Pay Calculation | M | W10.3 (holiday pay rates) | — |
| HR-012 | Bank File Generation | M | W10.7 (bank file for payroll crediting) | — |
| HR-013 | Employee Loan & Advance Management | M | W76 (employee loans & advances) | W10 (payroll processing), W43 (separation — loan balance settlement) |
| HR-014 | Employee Grievance & Whistleblower Case Management | S | W79 (employee grievance & whistleblower process) | W53 (data privacy breach response) |
| HR-015 | Philippine Statutory Benefits & Claims Management | M | W251 (Philippine statutory benefits & claims administration) | W10 (payroll processing statutory deductions) |
| HR-016 | Employee Expense Reimbursement | M | W74 (employee expense reimbursement — receipt attachment, approval, reimbursement via payroll) | W10 (payroll — reimbursement payment), W25 (petty cash — small expense alternative) |
| HR-017 | Employee PPE & Uniform Lifecycle | S | W172 (employee PPE & uniform lifecycle — issuance, replacement, cost allocation) | W15 (onboarding — initial PPE/uniform issuance), W47 (facility maintenance — PPE for maintenance staff) |

## R9. CRM & Loyalty (CRM)


| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| CRM-001 | Loyalty Points Engine | M | W17 (loyalty program operations) | W5B.5 (POS points earning) |
| CRM-002 | Customer Master (B2C) | M | W17.1–2 (enrollment & dedup), W50 (ecommerce customer sync) | — |
| CRM-003 | Trade Account Management | M | W8 (AR processing, dormant account management), W5B.4c (trade pricing at POS) | W24 (credit application) |
| CRM-004 | Corporate Account Management | M | W58 (corporate/project accounts), W24 (credit application), W162 (Project Quotation), W163 (Contract Pricing), W164 (Staged Delivery), W165 (Milestone Billing), W166 (Tendering) | — |
| CRM-005 | Tiered Loyalty | S | W17.8 (tier movement) | — |
| CRM-006 | Customer Purchase History | S | W12A.2 (transaction lookup), W17 (loyalty history), W156 (customer data platform — unified profile across channels) | W29 (recall customer tracing) |
| CRM-007 | Marketing Campaign Integration | N | W13 (promotions), W65 (CSAT/NPS surveys) | — |
| CRM-008 | Credit Application Workflow | M | W24 (credit application & approval) | W8.3 (credit limit enforcement) |
| CRM-009 | Government Procurement Compliance (PHILGEPS) | S | W78 (government procurement participation) | W166 (corporate/institutional tendering), W230 (contract review) |
| CRM-010 | Customer Account Reactivation | S | W84 (customer account reactivation — dormant account identification, outreach, reactivation offers) | W8 (AR — dormant account management), W17 (loyalty — reactivation points) |
| CRM-011 | Customer Feedback-to-Action Loop | S | W87 (customer feedback-to-action loop — NPS tracking, feedback categorization, action assignment) | W65 (CSAT/NPS surveys — feedback source), W41 (complaint resolution — feedback from complaints) |
| CRM-012 | Trade Sales Pipeline & Territory Management | S | W103 (trade sales pipeline & territory management — pipeline stages, territory assignment, forecasting) | W58 (corporate accounts — pipeline source), W162 (project quotation — quote from pipeline) |
| CRM-013 | Trade Counter / Pro Desk Operations | S | W112 (trade counter / pro desk operations — order taking, quick quote, express checkout for trade customers) | W5B (POS — trade pricing at checkout), W138 (home installation — pro referral) |
| CRM-014 | Customer Data Platform & Hyper-Personalization | S | W156 (customer data platform — unified profile, identity resolution, consent management, segmentation) | W17 (loyalty — customer data source), W50 (ecommerce — behavioral data) |

## R10. Analytics & Reporting (RPT)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| RPT-001 | Executive Dashboard | M | W35.2 (daily flash), W35.4 (weekly sales), W231 (QBR reporting) | — |
| RPT-002 | Store P&L | M | W35.10 (store P&L with occupancy allocation) | W26 (budget variance) |
| RPT-003 | Sales Analytics | M | W35.4 (week-on-week sales), W13.8 (promo performance) | W31.7 (forecast vs. actual) |
| RPT-004 | Inventory Reports | M | W6 (cycle count variance), W9A.6 (inventory valuation), W102 (category performance review & P&L ownership) | W42.17 (physical inventory summary), W97 (sample & demo inventory reporting) |
| RPT-005 | Purchase Analysis | S | W44 (vendor scorecard), W27 (rebate analytics), W130 (competitor price intelligence gathering) | — |
| RPT-006 | BIR-Compliant Tax Reports | M | W9A.16 (VAT returns), W9A.16a (EWT remittance), W216 (BIR CAS audit), W235 (transfer pricing compliance) | — |
| RPT-007 | Consolidated Financial Statements | M | W9A.14 (consolidated statements) | — |
| RPT-008 | Ad-Hoc Reporting | S | W35.18–19 (ad-hoc reports & BI analyses), W113 (business intelligence & data governance — self-service analytics) | — |
| RPT-009 | Mobile Dashboard | N | W35.2 (CFO mobile dashboard) | — |
| RPT-010 | Scheduled Report Distribution | S | W35 (full reporting rhythm — daily/weekly/monthly), W231 (QBR reporting), W67 (monthly store performance review) | — |
| RPT-011 | Category Performance Review & P&L Ownership | S | W102 (category performance review & P&L ownership — category P&L, buyer scorecard, assortment vs. plan) | W1 (assortment review — category input), W35 (management reporting — category reports) |
| RPT-012 | Pricing Hierarchy Governance & Compliance Audit | S | W107 (pricing hierarchy governance & compliance audit — rule validation, override audit, price gap analysis) | W40 (price change — hierarchy execution), W69 (price compliance audit — store-level check) |

## R11. Intercompany & Transfer Pricing (IC)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| IC-001 | IC AP/AR Automation | M | W14 (IC transactions & settlement) | — |
| IC-002 | Arm's-Length Transfer Pricing | M | W14 (transfer pricing rules), W14 annual review, W235 (transfer pricing compliance) | — |
| IC-003 | IC Elimination on Consolidation | M | W9A.13 (IC elimination), W234 (IC profit elimination) | — |
| IC-004 | IC Settlement | M | W14.6–7 (net settlement) | — |
| IC-005 | IC Reconciliation | M | W14.4–5 (IC reconciliation) | — |

## R12. Document Management (DOC)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| DOC-001 | Electronic Document Storage | M | W7.1 (invoice capture), W21.1 (capex attachments), W33.3 (warranty photos) | W50 (digital assets) |
| DOC-002 | BIR-Compliant Invoice Format | M | W5B.8 (BIR-registered receipt), W7 (vendor invoices) | — |
| DOC-003 | Delivery Receipt Tracking | M | W18.7 (DR capture), W3 (DC receiving DR) | — |
| DOC-004 | Import Document Management | M | W2B (BL, LC, customs docs), W36 (vendor permits) | — |
| DOC-005 | Document Retention Policy | M | W35 quarterly review, W42 (7-year archive), W256 (enterprise document retention & archiving policy) | W53 (breach register 5-year retention), W81 (bad debt write-off 7-year retention) |
| DOC-006 | Approval Workflow with Attachments | S | W21 (capex with quotes), W62 (contracts with attachments), W243 (POA board approval lifecycle) | — |
| DOC-007 | Hazardous Waste Disposal Tracking | S | W82 (DENR-compliant manifest tracking, per-location generator registration, quarterly reporting), W167 (Recycling / Circular Economy), W236 (hazmat storage DC), W237 (hazmat handling store), W238 (hazmat spill incident) | W52 (fleet — used oil/battery disposal), W68 (discontinued chemical waste) |
| DOC-008 | Enterprise Document Retention & Archiving Policy | M | W255 (electronic document storage & retrieval ERP-wide), W256 (enterprise document retention & archiving policy — configurable periods, legal hold, secure destruction) | W35 (reporting — retention review), W42 (physical inventory — archive) |

## R13. Master Data Management (MDM)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| MDM-001 | Centralized Item Master | M | W1.7 (SKU creation), W46.1 (kit BOM), W64 (pilot SKU), W252 (centralized item master creation & governance) | W50 (PIM content), W181 (store-level price tag printing & verification — item data accuracy) |
| MDM-002 | Item Attribute Management | M | W50.4 (category-specific attributes), W1 (assortment) | — |
| MDM-003 | Customer Data Quality | M | W17 (deduplication at enrollment), W24 (credit data validation), W253 (customer master data governance & deduplication) | — |
| MDM-004 | Vendor Onboarding Workflow | S | W36 (vendor onboarding lifecycle), W252 (item master governance — vendor-SKU linkage) | — |
| MDM-005 | Pricing Master Governance | M | W40 (price change with approval), W13 (promo pricing with approval) | W61 (price match analytics) |
| MDM-006 | Location Master | M | W16.4 (new store creation), W54 (LGU permit data), W45 (closure deactivation), W254 (location master lifecycle & hierarchy management) | — |
| MDM-007 | Hierarchical Category Structure | M | W1 (category management), W50 (category navigation) | — |
| MDM-008 | Vendor Master Data Governance | M | W252 (item master governance — vendor-SKU linkage), W36 (vendor onboarding — creation with approval), W253 (deduplication — vendor dedup logic) | W44 (vendor scorecard — vendor data quality feed) |

## R14. Non-Functional Requirements (NFR)

| Req ID | Requirement | Target | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| NFR-001 | POS Uptime | 99.9% | W5G (offline recovery), W55 (DR failover), W5E (store opening delay procedure — system-down protocol) | W48 (helpdesk P1 SLA) |
| NFR-002 | Back-Office Uptime | 99.5% | W55 (IT disaster recovery) | W48 (incident management) |
| NFR-003 | POS Transaction Speed | < 3 sec | W5B (POS selling) | — |
| NFR-004 | Report Generation | < 30 sec | W35 (management reporting), W113 (BI & data governance — query performance) | — |
| NFR-005 | Concurrent Users | 600–1,100 | W5B (600 POS terminals), W35 (HQ reporting) | — |
| NFR-006 | Data Retention | 7 years | W42 (physical inventory archive), W35 quarterly retention review | Data Volumes §1.2 |
| NFR-007 | Security | RBAC, audit trails | W37 (POS audit), W48 (change management), W186 (SOP governance), W230 (contract review), W236 (hazmat storage DC), W237 (hazmat handling store), W238 (hazmat spill incident), W243 (POA lifecycle), W152 (employee IT provisioning & access lifecycle management), W132 (software development & change management), W131 (IT asset lifecycle management) | W53 (breach response) |
| NFR-008 | Scalability | 300+ stores | W16 (new store opening process), W45 (store closure), W223 (store design), W224 (contractor selection), W225 (construction supervision), W226 (store renovation capex), W227 (handover) | — |
| NFR-009 | Localization | Full PH | W9A (BIR compliance), W10 (payroll statutory), W54 (LGU permits), W216 (BIR CAS audit), W217 (SC/PWD VAT-exemption), W54A (BIR CAS registration per location) | — |
| NFR-010 | Data Privacy | RA 10173 | W53 (breach response), W41 (DSAR handling), W17.2 (consent management) | — |
| NFR-011 | Offline POS | ≥ 8 hours | W5G (offline POS recovery & reconciliation) | W49 (typhoon degraded mode) |
| NFR-012 | Integration Capability | All touchpoints | W3–W7 (core integrations), W19 (3PL), W30 (banking), W257 (enterprise API & systems integration lifecycle management) | Data Volumes §3 |
| NFR-013 | Disaster Recovery | RPO ≤ 1h, RTO ≤ 4h | W55 (IT DR & failover) | W49 (physical disaster BC) |
| NFR-014 | Data Migration | Legacy → ERP | Implementation Roadmap §3 (data migration plan), W73 (data migration validation & parallel-run testing) | — |
| NFR-015 | Batch Processing Windows | Off-peak | Data Volumes §5 (batch windows), W9A (month-end) | — |
| NFR-016 | Data Privacy Breach Response | RA 10173 | W53 (full breach response lifecycle) | W41 (DSAR) |
| NFR-017 | LGU Business Permit Tracking | Per location | W54 (LGU permit renewal per location) | W16 (new store initial permit) |
| NFR-018 | ESG & Sustainability Reporting | S | W192 (GHG tracking), W193 (Waste diversion) | W194 (CSR), W195 (Ethical audit) |
| NFR-019 | Advanced Fleet Optimization | S | W196 (Route optimization), W199 (Telematics), W249 (port container turn-around) | W197 (Driver performance), W198 (Fuel) |
| NFR-020 | AI & Innovation Framework | N | W200 (AI Personalization), W201 (RPA), W208 (AI Inventory Optimization) | W202 (Predictive maint), W203 (Computer vision) |
| NFR-021 | Smart Store Operations | S | W206 (Mobile POS), W212 (Smart Safe), W211 (3D Rendering), W214 (expedited transfer), W240 (DC facilities), W241 (HQ facilities), W247 (smart locker), W173 (store-level solar energy monitoring) | W205 (Employee purchase), W207 (CCTV audit) |
| NFR-023 | Enterprise API & Integration Lifecycle Management | S | W257 (enterprise API & systems integration lifecycle — gateway, versioning, monitoring, health dashboard) | W19 (3PL integration — API consumer), W11 (BOPIS — API consumer), W30 (banking — API consumer) |
| NFR-024 | IT Asset Lifecycle Management | S | W131 (IT asset lifecycle management — hardware/software registry, procurement, deployment, retirement, license compliance) | W21 (capex — IT asset procurement), W48 (helpdesk — asset support) |
| NFR-025 | Employee IT Provisioning & Access Lifecycle | M | W152 (employee IT provisioning & access lifecycle — account creation on hire, role-based access, revocation on separation) | W15 (onboarding — provisioning trigger), W43 (separation — revocation trigger) |
| NFR-026 | Business Intelligence & Data Governance | S | W113 (business intelligence & data governance — BI platform, governed semantic layer, data quality monitoring) | W35 (management reporting — BI consumer), W31 (demand forecasting — data consumer) |
| NFR-027 | Omni-channel Customer Data Platform | S | W156 (customer data platform — unified profile, identity resolution, consent management) | W17 (loyalty — data source), W41 (complaint — data source), W258 (ticketing — data source) |
| NFR-022 | Local & Partner Governance | S | W209 (Barangay relationship), W213 (Contractor audit), W215 (home delivery returns), W216 (BIR CAS audit), W242 (3PL performance review) | W157 (E-waste), W210 (Dark store) |
| NFR-022a | BIR CAS Registration per Location | M | W54A (BIR Computerized Accounting System CAS registration per location, compliance documentation, renewal tracking) | W54 (LGU permits — related regulatory process), W16 (new store — initial CAS registration) |

## R15. Installation & Value-Added Services (SRV)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| SRV-001 | Installation & Value-Added Services Management | S | W138 (home installation services management), W139 (tool & equipment rental operations), W148 (home design & consultancy services), W168 (custom paint mixing & tinting), W169 (lumber & board cutting services), W211 (in-store 3D kitchen/bathroom design rendering), W213 (installation service partner quality audit) | W5B (POS — service item selling), W33 (warranty — installation defect claims) |
| SRV-002 | DIY Workshop & In-Store Event Management | S | W147 (DIY workshop & in-store event management — scheduling, registration, material tracking, ROI) | W83 (marketing campaign — event promotion), W17 (loyalty — event attendance points) |

## R16. Wholesale & Reseller Operations (WSL)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| WSL-001 | Wholesale & Reseller Operations | S | W145 (wholesale reseller onboarding & credit management), W146 (bulk fulfillment & cross-docking for wholesale) | W24 (credit application — wholesale credit check), W8 (AR — wholesale invoicing) |
| WSL-002 | Trade Sales Pipeline & Territory Management | S | W103 (trade sales pipeline & territory management — pipeline stages, territory assignment, forecasting) | W58 (corporate/project accounts — pipeline source), W162 (project quotation — quote from pipeline) |

## R17. Corporate Governance, Legal & Strategy (GOV)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| GOV-001 | Corporate Governance & Legal Management | S | W124 (corporate secretarial & entity management), W125 (legal case & litigation management), W126 (IP portfolio management), W127 (annual strategic planning & OKRs), W128 (enterprise project management lifecycle), W186 (internal SOP & policy governance lifecycle), W230 (legal contract review & approval), W231 (management performance reporting QBR) | W14 (IC transactions — corporate secretarial support) |
| GOV-002 | Internal Audit & Risk Management | S | W120 (internal audit planning & risk assessment), W121 (operational audit execution store/DC/HQ), W122 (enterprise risk management review), W123 (fraud investigation protocol), W159 (anti-bribery & corruption monitoring & audit), W95 (external audit coordination & support) | W37 (loss prevention — audit findings feed), W77 (BIR tax audit response — external audit) |
| GOV-003 | Real Estate & Lease Management | S | W116 (site selection & feasibility analysis), W117 (lease administration & renewal), W118 (rent & CAM payment processing), W119 (real property tax amillaramento management) | W16 (new store opening — site selection output), W45 (store closure — lease termination) |
| GOV-004 | Health, Safety & Environment Management | S | W140 (OHS incident management), W141 (workplace safety inspection & audit), W187 (contractor & third-party on-site safety orientation) | W82 (hazardous waste disposal — HSE coordination), W236–238 (hazmat — safety interface) |
| GOV-005 | Engineering & Construction Management | S | W223 (new store design & engineering standards), W224 (construction bidding & contractor selection), W225 (store construction management & supervision), W226 (store renovation & retrofitting CAPEX), W227 (commissioning & operational handover) | W16 (new store opening — construction handoff), W21 (capex — construction budget) |
| GOV-006 | Facility & Asset Maintenance (Non-Store) | S | W240 (DC facility & warehouse equipment maintenance), W241 (HQ office facility & executive asset maintenance), W242 (3PL & logistics partner performance review), W243 (POA & board resolution lifecycle) | W21 (capex — facility improvement), W39 (asset disposal — decommissioned equipment) |
| GOV-007 | Fleet Operations & Driver Management | S | W196 (route planning & dispatch optimization), W197 (driver performance & safety management), W198 (fuel management & consumption monitoring), W199 (fleet telematics & real-time tracking), W188 (fleet spare parts & preventive maintenance) | W52 (fleet management — fleet admin), W4 (replenishment — fleet scheduling) |
| GOV-008 | Sustainability & Environmental Compliance | S | W192 (GHG emissions tracking), W193 (waste management & circular economy), W194 (social impact & community development CSR), W195 (sustainable sourcing & ethical vendor audit), W167 (store & DC recycling program — circular economy), W114 (sustainability & environmental compliance reporting — aggregate ESG reporting) | W82 (hazardous waste — environmental compliance), W157 (e-waste — circular economy) |
| GOV-009 | Innovation & Digital Transformation | S | W200 (AI-driven personalization & recommendation engine), W201 (RPA lifecycle), W202 (predictive maintenance for industrial assets), W203 (computer vision for inventory & planogram audit), W208 (retail analytics & AI-driven inventory optimization) | W113 (BI & data governance — AI data pipeline), W19 (ecommerce — personalization output) |
| GOV-010 | Marketing Campaign Management | S | W83 (campaign planning, execution & performance measurement), W104 (loyalty program financial governance), W134 (crisis communication & brand reputation), W135 (CSR program execution), W142 (social media & influencer management), W143 (PR & corporate communications), W149 (bank & credit card partnership management), W151 (CSR impact measurement & reporting), W153 (retail media network operations), W189 (referral program & brand ambassador management), W190 (in-house design & creative production management) | W13 (promotions — campaign execution), W17 (loyalty — campaign targeting) |
| GOV-011 | Business Continuity & Disaster Preparedness | S | W158 (business continuity drill & disaster recovery testing) | W49 (natural disaster/typhoon BC — operational response), W55 (IT DR — technical response) |
| GOV-012 | Product Liability & Consumer Safety | S | W185 (product liability & consumer safety incident management — incident logging, regulatory notification, case management) | W29 (product recall — safety trigger), W82 (hazardous waste — disposal of unsafe products) |
| GOV-013 | Anti-Bribery & Corruption Monitoring | S | W159 (anti-bribery & corruption monitoring & audit — risk assessment, gift register, due diligence) | W79 (grievance & whistleblower — ABC reporting channel), W230 (contract review — ABC due diligence) |
| GOV-014 | Competitor Intelligence & Market Monitoring | S | W130 (competitor price intelligence gathering — price checks, market trend analysis, benchmarking) | W1 (assortment review — competitive positioning), W40 (price changes — market response) |
| GOV-015 | Private Label Development & Management | S | W129 (private label / in-house brand development — development lifecycle, supplier qualification, quality testing) | W1 (assortment — PL assortment decisions), W160 (factory audit — PL factory compliance) |
| GOV-016 | Employee Training & Development | S | W51 (employee training & skills development — needs assessment, program scheduling, attendance, certification) | W15 (onboarding — initial training), W140 (OHS — safety training) |
| GOV-017 | Employee Performance & Career Development | S | W72 (employee performance management — goal setting, reviews, competency framework), W178 (employee succession & internal mobility), W179 (management trainee cadetship program) | W10 (payroll — performance bonus processing), W34 (scheduling — performance-linked shifts) |
| GOV-018 | Store Performance Management | S | W67 (monthly store performance review — KPIs, manager scorecard, ranking), W96 (store renovation & remodel project), W86 (planogram compliance & store layout verification) | W35 (management reporting — store metrics), W67 (store review — performance data) |
| GOV-019 | Price Compliance & Energy Management (Store) | S | W69 (price compliance audit), W111 (store energy & utility consumption management), W173 (store-level solar energy monitoring), W181 (store-level price tag printing & verification) | W40 (price changes — compliance source), W35 (reporting — energy cost reporting) |
| GOV-020 | Store-Level Security & Loss Prevention | S | W71 (store physical security & access control), W171 (store physical security & yard patrol routine), W182 (gift/home registry lifecycle), W177 (vending & concessionaire management) | W37 (loss prevention — security data feed), W5A (store opening — security check) |
| GOV-021 | Store-Level Reverse Logistics | S | W176 (store-to-DC reverse logistics consolidation), W109 (store-level inventory receiving & putaway) | W22B (store-to-DC return — damaged/excess), W91 (damaged goods — return feed) |
| GOV-022 | DC Inbound & Outbound Operations | S | W3C (DC inbound delivery scheduling), W106 (DC outbound dispatch & load planning), W221 (cross-docking operations for fast-moving bulky items), W222 (DC container yard & chassis management), W188 (fleet spare parts & PM) | W3 (DC receiving — inbound execution), W4 (store replenishment — outbound execution) |
| GOV-023 | Customer Experience Management | S | W84 (customer account reactivation), W87 (customer feedback-to-action loop), W112 (trade counter / pro desk operations), W258 (omni-channel customer ticketing & support management) | W41 (complaint resolution — feedback source), W156 (CDP — unified customer view) |
| GOV-024 | Employee Financial Benefits Management | S | W175 (employee gratuity & retirement fund management RA 7641) | W10 (payroll — gratuity accrual posting), W43 (separation — retirement eligibility check) |
| GOV-025 | Sales Commission Management | S | W228 (sales commission calculation for trade & project sales — plan configuration, accrual, GL posting) | W10 (payroll — commission payment), W162 (project quotation — commission basis) |
| GOV-026 | Supply Chain Network Optimization | S | W133 (S&OP cycle), W144 (international logistics & import operations), W183 (supply chain network optimization review), W191 (global supply chain incoterm & marine insurance tracking) | W31 (demand forecasting — S&OP input), W250 (control tower — visibility) |
| GOV-027 | 3PL & Delivery Partner Management | S | W62B (3PL/delivery partner onboarding & offboarding), W242 (3PL & logistics partner performance review) | W19 (home delivery — 3PL execution), W66 (inter-island logistics — 3PL partner) |
| GOV-028 | Sample & Demo Inventory Management | S | W97 (sample & demo inventory management — separate tracking, issuance, disposition) | W1 (assortment — sample allocation), W46 (kit assembly — sample kit) |
| GOV-029 | Markdown & Clearance Pricing Management | S | W93 (markdown & clearance pricing execution — trigger rules, approval, budget tracking, performance) | W13 (promotions — clearance promo), W220 (SLOB — markdown trigger) |

## R18. New Workflows — Additional Requirements

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| CRM-015 | Call Center Daily Operations & Queue Management | S | W259 (call center daily operations — IVR, queue routing, agent monitoring, SLA tracking) | W258 (ticketing — escalation destination), W156 (CDP — customer 360 in agent console), W34 (scheduling — agent shift scheduling), W65 (CSAT/NPS — post-interaction survey) |
| FIN-031 | BIR eFPS Filing & Electronic Payment Submission | M | W260 (BIR eFPS filing — return generation, eFPS submission, PRN, AAB payment) | W9A (month-end close — tax provision posting), W90 (monthly tax filing — high-level process), W216 (BIR CAS audit — filing archive), W239 (customs duty — import tax data source), W217 (SC/PWD reporting — VAT-exemption data source) |
| FIN-032 | E-Wallet & Digital Payment Settlement Reconciliation | M | W261 (e-wallet settlement reconciliation — GCash, Maya, GrabPay, ShopeePay matching, MDR verification, chargeback management) | W99 (payment settlement reconciliation — card settlement), W89 (bank reconciliation — settlement bank posting), W30 (treasury — cash position impact), W5F (store EOD — e-wallet Z-report), W149 (bank partnership — promo MDR terms) |
| MER-001 | Store Promotional Setup & Visual Merchandising Execution | S | W262 (store promotional setup — planogram distribution, stock pulling, display construction, signage placement, compliance photo tracking) | W13 (promotions — pricing source), W93 (markdown — clearance disposition), W181 (price tag printing — signage), W190 (creative production — display assets) |
| CRM-016 | Loyalty Member Enrollment & Onboarding Journey | S | W263 (loyalty enrollment — multi-channel capture, dedup, consent, digital card, welcome sequence, conversion tracking) | W17 (loyalty operations — account creation), W253 (customer dedup — enrollment dedup engine), W156 (CDP — unified profile), W259 (call center — enrollment via phone) |
| MER-002 | Seasonal Merchandise Transition & Display Rotation | S | W264 (seasonal transition — planning, markdown trigger, setup brief, display build/teardown, in-season monitoring, post-season review) | W32 (seasonal buy planning — seasonal PO), W31 (demand forecasting — seasonal forecast), W13 (promotions — seasonal pricing), W93 (markdown — seasonal clearance), W1 (assortment review — seasonal assortment) |
| NFR-028 | POS Terminal Hardware Maintenance & Peripheral Management | S | W265 (POS hardware maintenance — incident ticketing, remote diagnosis, spare swap, PM scheduling, warranty/RMA tracking) | W48 (helpdesk — incident ticketing), W131 (IT asset lifecycle — hardware register), W39 (asset disposal — decommissioned peripherals), W5G (offline POS — UPS battery PM) |

---

## Coverage Validation

- **Total requirements**: 261 across 18 categories (R1–R18)
- **Requirements with primary workflow mapping**: All ✅
- **Total workflows referenced**: 290 (all workflows in the README index)

---

*Date: 2026-06-02 (v23 — removed duplicate GOV-030 (identical to GOV-008); corrected coverage count from 237+ to 261; corrected category count from 31 to 18; all 290 workflows retain full requirement traceability)*
