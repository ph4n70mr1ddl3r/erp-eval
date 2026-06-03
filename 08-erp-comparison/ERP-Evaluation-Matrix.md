# ERP Evaluation Matrix — BuildRight Depot Corp.

> Side-by-side capability assessment of **SAP S/4HANA Cloud**, **Microsoft Dynamics 365**, and **Oracle Fusion Cloud Applications** against all BuildRight Depot requirements.

---

## Legend

| Symbol | Fit Score | Meaning |
|---|---|---|
| ✅ | 4 — Native Fit | Available out-of-the-box, no customization needed |
| ⚙️ | 3 — Configured Fit | Achievable through admin configuration (no code) |
| 🔧 | 2 — Custom/3rd-Party | Requires custom development or third-party add-on |
| ⚠️ | 1 — Partial | Only partially addressed; significant workaround needed |
| ❌ | 0 — Not Available | Not available and no viable workaround |

---

## Executive Summary

| Dimension | SAP S/4HANA Cloud | Microsoft Dynamics 365 | Oracle Fusion Cloud |
|---|---|---|---|
| **Products in Scope** | S/4HANA Cloud, BTP, Customer Checkout, IBP, SuccessFactors, Commerce Cloud | D365 Finance, SCM, Commerce, HR, Power Platform, Azure | Fusion Cloud ERP, SCM, HCM, CX, Warehouse Management, NetSuite Retail (POS) |
| **Must Have Requirements (≈110)** | ~85 ✅/⚙️ · ~18 🔧 · ~5 ⚠️ · ~2 ❌ | ~80 ✅/⚙️ · ~20 🔧 · ~7 ⚠️ · ~3 ❌ | ~75 ✅/⚙️ · ~22 🔧 · ~9 ⚠️ · ~4 ❌ |
| **Philippine Localization** | ⚠️ Growing — BIR forms need ISV/partner | ⚠️ Limited — needs ISV payroll & tax add-on | ⚠️ Limited — needs partner localization |
| **Retail POS Maturity** | 🔧 SAP Customer Checkout is immature for big-box | ✅ D365 Commerce POS is retail-native with offline | ❌ No native POS; must integrate third-party |
| **Multi-Entity Consolidation** | ✅ Best-in-class | ✅ Strong | ✅ Strong |
| **Scalability (2.8M txns/mo)** | ✅ HANA in-memory, proven at scale | ✅ Azure cloud, Commerce Scale Unit for POS | ✅ OCI cloud, but POS aggregation needed |
| **Implementation Complexity** | High — large ecosystem, long timeline | Medium — modular, but 5-app suite to integrate | High — multiple Oracle Cloud modules to orchestrate |
| **5-Year TCO Estimate** | High ($$$) | Medium-High ($$) | Medium-High ($$) |

---

## R1. Financial Management (FIN)

| Req ID | Requirement | Priority | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|---|
| FIN-001 | Multi-entity GL (5 entities) | Must | ✅ Leading/Segment COA; multiple company codes | ✅ Multiple legal entities with shared COA | ✅ Multi-ledger, multi-entity with shared segments |
| FIN-002 | Automated IC Elimination | Must | ✅ Central Finance / group close with auto IC elimination | ✅ Intercompany accounting with auto elimination | ✅ Intercompany elimination rules in consolidation |
| FIN-003 | Consolidated Financial Reporting | Must | ✅ SAP Group Reporting / BCS for PFRS/IFRS | ✅ Financial consolidation in D365 Finance | ✅ Oracle Enterprise Performance Management (EPM) |
| FIN-004 | AP with 3-Way Match | Must | ✅ Native 3-way match (PO-GR-Invoice) | ✅ Native 3-way match in Procurement | ✅ 3-way match in Fusion Payables |
| FIN-005 | AR for B2B | Must | ✅ Full AR with trade/corporate accounts | ✅ AR module with credit management | ✅ Fusion Receivables with credit management |
| FIN-006 | Philippine VAT (12%) | Must | ⚙️ Tax engine supports VAT; PH config needed | ⚙️ Tax engine configurable; PH rates set up | ⚙️ Tax engine supports VAT; PH configuration |
| FIN-007 | Withholding Tax (Expanded) | Must | ⚙️ Extended WHT configurable per vendor | ⚙️ Configurable withholding tax per vendor | ⚙️ Withholding tax setup per supplier |
| FIN-008 | BIR Tax Return Generation | Must | 🔧 ISV/partner add-on needed for 2550M, 1601-E etc. | 🔧 ISV partner needed for BIR-specific forms | 🔧 Partner localization for BIR forms |
| FIN-009 | Multi-Bank Integration | Should | ✅ SAP Multi-Bank Connectivity; BDO/BPI formats | ✅ Advanced bank account management; formats configurable | ✅ Oracle Banking formats; PH bank format config |
| FIN-010 | Cash Management / Treasury | Should | ✅ SAP Treasury & Risk Management | ✅ Cash management in D365 Finance | ✅ Oracle Cash Management & Treasury |
| FIN-011 | Fixed Asset Management | Must | ✅ Full FA module with PFRS depreciation | ✅ Fixed assets with configurable depreciation | ✅ Oracle Assets with depreciation methods |
| FIN-012 | Budgeting & Variance Analysis | Should | ✅ Budget control & variance reports | ✅ Budget control with variance reporting | ✅ Budgetary control & variance analysis |
| FIN-013 | Landed Cost Calculation | Must | ✅ Landed cost in MM; duty/freight/insurance allocation | ⚙️ Landed cost module in D365 SCM; configuration needed | ⚙️ Landed cost in Fusion Cost Accounting; config needed |
| FIN-014 | Multi-Currency | Must | ✅ Full multi-currency with exchange rate management | ✅ Multi-currency with exchange rate types | ✅ Multi-currency with daily rates |
| FIN-015 | Period-End Close Workflow | Must | ✅ Financial Close in SAP; task management | ✅ Period close workspace with checklist | ✅ Financial close management in EPM |
| FIN-016 | Capex Workflow | Must | ✅ Investment management with tiered approval | ⚙️ Capex via Power Automate approval workflow | ⚙️ Capex via approval workflow in Fusion |
| FIN-017 | Petty Cash Management | Must | ⚙️ Configure petty cash as subledger/cash journal | ⚙️ Petty cash via cash accounts & journals | ⚙️ Configure petty cash accounts & journals |
| FIN-018 | Consignment Settlement | Should | ✅ SAP Consignment processing with settlement | 🔧 D365 consignment via vendor consignment inventory | 🔧 Consignment via custom process in Fusion |
| FIN-019 | Vendor Rebate Management | Should | ✅ SAP Settlement Management for rebates | ⚙️ Rebate management via D365 Trade Allowances | ⚙️ Oracle Trade Management for rebates |
| FIN-020 | Duplicate Vendor Invoice Detection | Must | ✅ Auto duplicate check on invoice number/amount | ✅ Duplicate invoice detection in AP | ✅ Duplicate invoice validation in Payables |
| FIN-021 | FX Hedging / Forward Contracts | Should | ✅ SAP Treasury hedging module | 🔧 Requires third-party or custom Power App | ✅ Oracle Treasury includes FX hedging |
| FIN-022 | Bad Debt Write-Off & Recovery | Must | ✅ AR write-off with approval; recovery posting | ⚙️ Bad debt write-off via AR write-off function | ⚙️ Bad debt write-off via AR adjustments |
| FIN-023 | Insurance Policy Lifecycle | Should | 🔧 Custom development or BTP extension | 🔧 Power App for insurance registry | 🔧 Custom object / extension in Fusion |
| FIN-024 | Employee Gratuity / Retirement (RA 7641) | Must | 🔧 PH-specific; custom payroll rules needed | 🔧 ISV payroll or custom calculation | 🔧 PH-specific; custom HCM calculation |
| FIN-025 | Cash-in-Transit / Armored Car | Should | 🔧 Custom process / BTP extension | 🔧 Power App for CIT management | 🔧 Custom extension |
| FIN-026 | Product Costing & Margin Analysis | Should | ✅ CO-PA profitability analysis; margin by SKU/store | ⚙️ Cost accounting module; margin analysis | ⚙️ Oracle Cost Management & profitability |
| FIN-027 | Customer Refund & Credit Processing | Must | ✅ Credit memo processing with approval | ✅ Credit notes with approval workflow | ✅ Credit memos with approval |
| FIN-028 | Customer Credit Collection & Escalation | Must | ✅ Collection management with aging escalation | ✅ Collections in AR with aging & letters | ✅ Oracle Collections with aging escalation |
| FIN-029 | IC Dividend & Loan Management | Should | ✅ IC loan management in Treasury | ⚙️ IC loan setup via manual journal/process | ⚙️ IC loan via custom process |
| FIN-030 | Fixed Asset Physical Verification | Should | 🔧 Asset tracking via RF gun / SAP EAM integration | 🔧 Power App for asset physical count | 🔧 Custom extension for asset verification |
| FIN-031 | BIR eFPS Filing & e-Payment | Must | 🔧 ISV/partner add-on for eFPS integration | 🔧 ISV partner for eFPS submission | 🔧 Partner localization for eFPS |
| FIN-032 | E-Wallet Settlement Reconciliation | Must | 🔧 Custom integration with GCash/Maya settlement files | 🔧 Custom Power Automate / integration | 🔧 Custom integration for settlement files |

**FIN Summary**: All three systems are strong in core financials. SAP has the edge in consolidation and treasury. **BIR tax forms and eFPS filing are gaps for all three** — each requires a Philippines-local ISV or partner add-on.

---

## R2. Inventory Management (INV)

| Req ID | Requirement | Priority | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|---|
| INV-001 | Perpetual Inventory (all locations) | Must | ✅ Real-time perpetual across all storage locations | ✅ Perpetual across all warehouses/sites | ✅ Perpetual across all subinventories |
| INV-002 | Real-Time Inventory Visibility | Must | ✅ HANA real-time across 200 stores + 4 DCs | ✅ Real-time inventory across sites | ✅ Real-time inventory visibility |
| INV-003 | Weighted Average Cost (WAC) | Must | ✅ Supports WAC valuation method | ✅ Supports WAC (weighted average) | ✅ Supports WAC valuation |
| INV-004 | ABC Classification | Must | ✅ ABC analysis in material management | ⚙️ ABC classification via inventory policies | ✅ ABC classification in inventory |
| INV-005 | Multi-Location Stock Transfer | Must | ✅ Stock transfer orders across plants/storage locations | ✅ Transfer orders across warehouses/sites | ✅ Inter-org transfers across subinventories |
| INV-006 | Cycle Counting | Must | ✅ Cycle counting with variances | ✅ Cycle counting in warehouse management | ✅ Cycle counting in Oracle Inventory |
| INV-007 | Physical Inventory (Wall-to-Wall) | Must | ✅ Full physical inventory process | ✅ Full physical inventory process | ✅ Full physical inventory process |
| INV-008 | Lot & Serial Tracking | Should | ✅ Batch/lot and serial number management | ✅ Batch and serial tracking in inventory | ✅ Lot and serial tracking |
| INV-009 | Consignment Inventory | Should | ✅ Vendor consignment stock (non-valuated) | ✅ Vendor consignment inventory | 🔧 Consignment via custom process |
| INV-010 | Catch-Weight / Variable Measure | Must | ⚠️ Catch-weight management via EWM or variant config | ⚠️ Product variants with catch-weight; needs config | ⚠️ Variable measure via UOM conversion; limited |
| INV-011 | Inventory Aging Analysis | Should | ✅ Inventory aging reports standard | ⚙️ Aging via inventory reports / Power BI | ⚙️ Aging reports via OTBI/BI Publisher |
| INV-012 | Safety Stock & Reorder Point | Must | ✅ Safety stock & ROP per SKU in MRP | ✅ Safety stock & min/max in inventory | ✅ Safety stock & reorder planning |
| INV-013 | Batch/Lot for Paint | Should | ✅ Batch management with shelf life | ✅ Batch tracking with attributes | ✅ Lot tracking with attributes |
| INV-014 | In-Transit Inventory | Must | ✅ In-transit stock visibility | ✅ In-transit inventory with transfer orders | ✅ In-transit inventory visibility |
| INV-015 | Inventory Valuation Reports | Must | ✅ Valuation by location, category, entity | ✅ Valuation reports per site/category | ✅ Valuation reports by subinventory |
| INV-016 | Product Recall Tracking | Should | ⚙️ Recall via batch/lot tracing workflow | 🔧 Recall process via custom workflow | 🔧 Custom recall tracking process |
| INV-017 | Consignment Tracking (non-valuated) | Must | ✅ Vendor consignment with ownership transfer at sale | ⚙️ Consignment with ownership transfer config | 🔧 Consignment tracking via custom extension |
| INV-018 | VMI Inventory Tracking | Should | ✅ VMI processing in SAP MM/SD | ⚙️ VMI via vendor collaboration features | ⚙️ VMI via supplier collaboration |
| INV-019 | Multi-Channel Inventory Allocation | Should | ✅ ATP checks across channels in S/4HANA + CAR | ⚙️ Channel inventory allocation via D365 Commerce | ⚙️ Inventory allocation rules in Fusion |
| INV-020 | Proactive Store Inventory Rebalancing | Should | ⚙️ Rebalancing suggestions via IBP/forecasting | 🔧 Custom replenishment suggestion logic | 🔧 Custom rebalancing logic |

**INV Summary**: All three handle core inventory well. **Catch-weight (INV-010) is a challenge for all** — critical for lumber/wire. SAP EWM has the most mature catch-weight handling. Consignment and VMI are best in SAP, adequate in D365, and need customization in Oracle Fusion.

---

## R3. Procurement & Purchasing (PUR)

| Req ID | Requirement | Priority | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|---|
| PUR-001 | Purchase Order Management | Must | ✅ Full PO lifecycle | ✅ Full PO lifecycle | ✅ Full PO lifecycle |
| PUR-002 | Automated Replenishment (MRP/ROP) | Must | ✅ MRP/ROP auto-generate POs | ✅ MRP with auto-firming to POs | ✅ MRP/Min-Max auto-generate POs |
| PUR-003 | Vendor Management (800–1,000) | Must | ✅ Vendor master for thousands of suppliers | ✅ Vendor management at scale | ✅ Supplier management at scale |
| PUR-004 | Import Purchase Orders (LC, customs) | Must | ✅ Import processing with LC tracking | ⚙️ Import PO with landed cost; LC via config | ⚙️ Import POs; LC tracking via Treasury |
| PUR-005 | 3-Way Matching | Must | ✅ Native 3-way match | ✅ Native 3-way match | ✅ Native 3-way match |
| PUR-006 | Blanket/Contract POs | Should | ✅ Scheduling agreements / contracts | ✅ Purchase agreements / blanket POs | ✅ Blanket purchase agreements |
| PUR-007 | Vendor Portal | Nice | ✅ SAP Ariba Supplier Portal | ⚙️ Vendor collaboration portal in D365 | ✅ Oracle Supplier Portal |
| PUR-008 | Vendor Performance Scorecard | Should | ✅ Vendor evaluation in MM | ⚙️ Vendor rating via custom metrics/Power BI | ⚙️ Supplier performance via OTBI/BI reports |
| PUR-009 | Multi-Entity Procurement | Must | ✅ Central purchasing with entity-level receipt | ✅ Central procurement across legal entities | ✅ Shared procurement across business units |
| PUR-010 | Approval Workflow | Must | ✅ Flexible approval workflows per amount | ✅ Workflow engine with tiered approvals | ✅ Approval workflows with AMX rules |
| PUR-011 | Goods Receipt Processing | Must | ✅ GR against PO at plant/storage location | ✅ Product receipt against PO at site | ✅ Receipt against PO at subinventory |
| PUR-012 | Return to Vendor (RTV) | Must | ✅ Return purchase order process | ✅ Return order process | ✅ Return to supplier process |
| PUR-013 | Direct Store Delivery (DSD) | Must | ⚙️ DSD via separate plant per store; config needed | ⚙️ DSD receipt at store location; config needed | ⚙️ DSD receipt at store subinventory; config |
| PUR-014 | Vendor Managed Inventory | Should | ✅ VMI in SAP MM with auto-replenishment | ⚙️ VMI via vendor collaboration features | ⚙️ VMI via supplier collaboration in Fusion |
| PUR-015 | Vendor Rebate Management | Should | ✅ Settlement Management for rebates | ⚙️ Rebate management in Trade Allowances | ⚙️ Oracle Trade Management |
| PUR-016 | AQL Sampling per SKU Category | Should | ⚙️ Quality inspection with sampling plans | 🔧 Quality management via custom inspection | ⚙️ Quality inspection with sampling in Fusion |
| PUR-017 | Supplier Quality & CAPA | Should | ✅ QM module with CAPA workflows | 🔧 Quality management via custom Power App | ⚙️ Quality management in Fusion SCM |
| PUR-018 | Indirect / Non-Merchandise Procurement | Must | ✅ Separate PO types / account categories | ✅ Procurement categories for indirect spend | ✅ Procurement categories for indirect spend |
| PUR-019 | Vendor Invoice Dispute | Must | ✅ Block invoice; dispute resolution in AP | ✅ Invoice hold with dispute notes/workflow | ✅ Invoice hold with dispute resolution |
| PUR-020 | Vendor Price Protection Claims | Should | ⚙️ Price protection via Settlement Management | 🔧 Custom workflow for price protection | 🔧 Custom process for price protection |
| PUR-021 | Vendor Strategic Collaboration & JBP | Should | 🔧 SAP Ariba for JBP collaboration | 🔧 Supplier collaboration portal / Power BI | 🔧 Custom supplier collaboration workspace |
| PUR-022 | PL Factory Audit & Social Compliance | Should | 🔧 Ariba Supplier Risk / custom audit mgmt | 🔧 Power App for factory audit tracking | 🔧 Custom supplier audit management |
| PUR-023 | Supplier Diversity / MSME Program | Should | 🔧 Custom reporting on vendor classifications | 🔧 Power BI + custom vendor attributes | 🔧 Custom supplier diversity tracking |
| PUR-024 | Product Quality Testing & Certification | Should | ⚙️ QM module with test plans & certificates | 🔧 Quality management via custom extension | ⚙️ Quality management with test results |

**PUR Summary**: Core procurement is strong across all three. SAP leads with Ariba for supplier collaboration and QM for quality. D365 and Oracle require more customization for quality management and supplier collaboration.

---

## R4. Warehouse Management (WMS)

| Req ID | Requirement | Priority | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|---|
| WMS-001 | RF/Barcode Directed Operations | Must | ✅ SAP EWM with RF-directed putaway/pick | ✅ D365 Warehouse Mgmt with mobile device directed | ✅ Oracle WMS Cloud with RF/barcode |
| WMS-002 | Cross-Dock Capability | Should | ✅ Cross-dock in EWM | ✅ Cross-docking in warehouse management | ✅ Cross-dock in WMS Cloud |
| WMS-003 | Wave/Zone Picking | Should | ✅ Wave management in EWM | ✅ Wave/zone picking in D365 WMS | ✅ Wave planning in WMS Cloud |
| WMS-004 | Receiving & Putaway | Must | ✅ RF-directed receiving & putaway in EWM | ✅ Receiving & directed putaway | ✅ Receiving & putaway in WMS Cloud |
| WMS-005 | Shipping & Dispatch | Must | ✅ Outbound delivery & shipping in EWM | ✅ Shipping & load management | ✅ Shipping & dispatch in WMS Cloud |
| WMS-006 | Yard Management (Lumber) | Should | ✅ EWM Yard Management for outdoor stock | 🔧 Custom yard management via Power App | 🔧 Yard management via custom extension |
| WMS-007 | Label Printing | Must | ✅ Label printing / Adobe forms | ✅ Label printing / SSRS reports | ✅ Label printing in WMS Cloud |
| WMS-008 | WMS-ERP Integration | Must | ✅ EWM embedded in S/4HANA (same system) | ✅ WMS native in D365 SCM | ⚠️ WMS Cloud is separate; integration via API |

**WMS Summary**: SAP EWM is the most comprehensive WMS (yard management, advanced RF). D365 WMS is native and strong for standard operations. Oracle WMS Cloud (LogFire) is capable but is a separate cloud service requiring API integration.

---

## R5. Point-of-Sale (POS) & Retail (POS)

| Req ID | Requirement | Priority | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|---|
| POS-001 | 600 POS Terminals | Must | 🔧 SAP Customer Checkout limited; may need third-party | ✅ D365 Commerce POS scales to 1,000+ terminals | ❌ No native POS; third-party POS required |
| POS-002 | Offline Mode | Must | ⚠️ SAP CCO has offline mode but limited | ✅ Commerce Scale Unit (CSU) enables full offline | ❌ Third-party POS must provide offline |
| POS-003 | Barcode Scanning | Must | ✅ SAP CCO supports 1D/2D scanning | ✅ Native barcode scanning | 🔧 Third-party POS dependent |
| POS-004 | Multi-Tender | Must | ✅ Multi-tender support in SAP CCO | ✅ Native multi-tender with split payment | 🔧 Third-party POS dependent |
| POS-005 | Loyalty Integration | Must | ⚙️ Integration with SAP Loyalty or custom | ✅ Native loyalty in D365 Commerce | 🔧 Custom integration with loyalty engine |
| POS-006 | Price Override (w/ Auth) | Must | ✅ Price override with manager auth | ✅ Price override with permission | 🔧 Third-party POS dependent |
| POS-007 | Returns & Exchanges | Must | ✅ Returns processing in SAP CCO | ✅ Native returns & exchanges | 🔧 Third-party POS dependent |
| POS-008 | Cash Drawer Management | Must | ✅ Cash drawer in SAP CCO | ✅ Native cash drawer management | 🔧 Third-party POS dependent |
| POS-009 | End-of-Day Reconciliation | Must | ✅ Z-report in SAP CCO | ✅ Native shift/close reporting | 🔧 Third-party POS dependent |
| POS-010 | Quantity Break Pricing | Must | ⚙️ Configurable in SAP pricing | ✅ Native quantity breaks in D365 Commerce | 🔧 Third-party POS / custom pricing |
| POS-011 | Customer Display | Should | ✅ Customer display in SAP CCO | ✅ Native customer display support | 🔧 Third-party POS dependent |
| POS-012 | Receipt Printing | Must | ✅ Receipt printing; BIR format needs customization | ✅ Receipt printing; BIR format needs customization | 🔧 Third-party POS dependent |
| POS-013 | Real-Time Inventory Deduction | Must | ✅ Real-time sync to S/4HANA inventory | ✅ Real-time via Commerce Scale Unit | 🔧 Third-party POS integration latency |
| POS-014 | Promotional Pricing Auto-Apply | Must | ✅ Promotion engine in SAP CAR/CRM | ✅ Native retail discounts/auto-apply | 🔧 Third-party POS + custom promo engine |
| POS-014a | Senior/PWD Discount (PH Legal) | Must | 🔧 PH-specific; custom discount rules | 🔧 Custom discount rules for SC/PWD | 🔧 Custom PH discount logic |
| POS-015 | Gift Card / Store Credit | Should | ⚙️ Gift card via SAP or third-party | ✅ Native gift card in D365 Commerce | 🔧 Custom gift card module |
| POS-016 | Catch-Weight at POS | Must | 🔧 Custom catch-weight handling at POS | ⚙️ Variable weight items in D365 Commerce | 🔧 Custom catch-weight in third-party POS |
| POS-017 | Paint Mixing / Custom SKU | Must | 🔧 Custom SKU generation at POS | 🔧 Product configurator or custom POS extension | 🔧 Custom SKU generation at POS |
| POS-018 | Age-Restricted Prompts | Should | ⚙️ Configure age-check prompts | ✅ Age-restriction prompts in D365 Commerce | 🔧 Third-party POS dependent |
| POS-019 | Warranty Claim Registration | Should | 🔧 Custom warranty process | 🔧 Custom via Power App at POS | 🔧 Custom warranty process |
| POS-020 | Layaway / Installment Sales | Should | 🔧 Custom layaway process | 🔧 Custom via POS extension | 🔧 Custom layaway process |
| POS-021 | Multi-DC Order Splitting (Ecom) | Should | ⚙️ Split delivery in SAP Commerce | ⚙️ Order splitting via D365 Commerce | ⚙️ Split fulfillment in Order Management |
| POS-022 | Employee Discount at POS | Should | ⚙️ Employee pricing condition in SAP | ⚙️ Employee discount group in D365 | 🔧 Custom employee discount logic |
| POS-023 | Store-Level Delivery Scheduling | Should | 🔧 Custom delivery scheduling | ⚙️ Delivery scheduling in D365 Commerce | 🔧 Custom delivery scheduling |
| POS-028 | POS Hardware Maintenance | Should | 🔧 ITSM via SAP Solution Manager | 🔧 ITSM via Power App / ServiceNow | 🔧 ITSM via custom extension |

**POS Summary**: **D365 Commerce is the clear POS leader** — native retail POS with offline CSU, multi-tender, loyalty, and gift cards. SAP Customer Checkout is adequate but immature for 600-terminal big-box retail. **Oracle Fusion has no native POS** — a major gap requiring a third-party POS (e.g., LS Retail, Oracle Retail Xstore) with integration overhead.

---

## R6. Ecommerce Integration (ECOM)

| Req ID | Requirement | Priority | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|---|
| ECOM-001 | Real-Time Inventory Sync | Must | ✅ SAP Commerce Cloud with OData to S/4 | ✅ D365 Commerce native real-time inventory | ⚙️ Oracle Commerce integration via API |
| ECOM-002 | Real-Time Price Sync | Must | ✅ Price sync via CPI/integration | ✅ Native price sync in D365 Commerce | ⚙️ Price sync via integration layer |
| ECOM-003 | BOPIS Order Flow | Must | ✅ BOPIS in SAP Commerce Cloud | ✅ Native BOPIS in D365 Commerce | ⚙️ BOPIS via Oracle Commerce / custom |
| ECOM-004 | Home Delivery Order Flow | Must | ✅ Home delivery in SAP Commerce | ✅ Home delivery in D365 Commerce | ⚙️ Delivery via Oracle Order Management |
| ECOM-005 | Order Status Tracking | Must | ✅ Order tracking in Commerce Cloud | ✅ Native order tracking | ✅ Order tracking in Order Management |
| ECOM-006 | Payment Gateway (PayMongo etc.) | Must | 🔧 Custom payment adapter for PH gateways | 🔧 Custom payment connector for PH gateways | 🔧 Custom payment integration for PH gateways |
| ECOM-007 | Return Initiation (Online) | Must | ✅ Returns in SAP Commerce | ✅ Native returns initiation | ⚙️ Returns via Oracle Commerce |
| ECOM-008 | Customer Data Sync | Must | ✅ Customer integration via CIF/CPI | ✅ Native customer sync in D365 | ⚙️ Customer sync via integration |
| ECOM-009 | Product Catalog Sync | Must | ✅ Catalog sync via SAP CPI | ✅ Native catalog sync | ⚙️ Catalog sync via integration |
| ECOM-010 | Promo/Coupon Integration | Should | ✅ Promotion sync with SAP Promotions | ✅ Native promotion sync | ⚙️ Promo sync via integration |
| ECOM-011 | Home Delivery Fulfillment | Must | ✅ Fulfillment with carrier integration | ✅ Fulfillment with carrier integration | ⚙️ Fulfillment via Order Management |
| ECOM-012 | Delivery Partner Integration | Must | 🔧 API integration with Lalamove/Transportify | 🔧 Custom carrier connector | 🔧 API integration with PH carriers |
| ECOM-013 | Marketplace (Lazada/Shopee) | Should | 🔧 Custom marketplace integration | 🔧 Custom marketplace integration | 🔧 Custom marketplace integration |
| ECOM-014 | Ship-from-Store | Should | ⚙️ Ship-from-store via SAP CAR | ⚙️ Ship-from-store in D365 Commerce | 🔧 Custom ship-from-store process |
| ECOM-015 | Omni-channel Ticketing & Support | Should | ⚙️ SAP Service Cloud integration | ⚙️ D365 Customer Service integration | ⚙️ Oracle Service Center integration |
| ECOM-016 | Order Exception & Cancellation | Should | ⚙️ Exception handling in Order Management | ⚙️ Exception handling in D365 Commerce | ⚙️ Exception handling in Order Mgmt |

**ECOM Summary**: D365 Commerce has the tightest native ecommerce-POS-inventory integration. SAP Commerce Cloud is feature-rich but requires CPI integration middleware. Oracle Fusion needs significant integration work between Commerce, Order Management, and Inventory.

---

## R7. Supply Chain Planning (SCP)

| Req ID | Requirement | Priority | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|---|
| SCP-001 | Demand Forecasting | Should | ✅ SAP IBP demand forecasting | ⚙️ Demand forecasting in D365 Planning Optimization | ✅ Oracle Demand Management |
| SCP-002 | Replenishment Planning (DC→Store) | Must | ✅ IBP for retail replenishment | ✅ Planning Optimization for replenishment | ⚙️ Oracle Supply Planning for replenishment |
| SCP-003 | Reorder Point Calculation | Must | ✅ ROP per SKU per location | ✅ Min/max and safety stock calculations | ✅ Reorder planning per item/location |
| SCP-004 | Safety Stock Optimization | Should | ✅ Dynamic safety stock in IBP | ⚙️ Safety stock calculations in Planning | ⚙️ Safety stock optimization in Planning |
| SCP-005 | Seasonal Planning | Should | ✅ Seasonal planning in IBP | ⚙️ Seasonal via forecast adjustments | ⚙️ Seasonal planning in Supply Planning |
| SCP-006 | Allocation Management | Should | ✅ Allocation in SAP GATP/ARun | ⚙️ Allocation in D365 via reservation | ⚙️ Allocation in Oracle Supply Chain |
| SCP-007 | Purchase Recommendation | Must | ✅ MRP/PP/DS suggested POs | ✅ Planning Optimization suggested POs | ✅ MRP suggested POs |

**SCP Summary**: SAP IBP is the strongest supply chain planning solution. D365 Planning Optimization is improving rapidly but less mature for complex retail. Oracle Fusion has solid planning but requires multiple cloud modules.

---

## R8. HR & Payroll (HR)

| Req ID | Requirement | Priority | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|---|
| HR-001 | Multi-Entity Payroll (5 entities) | Must | ✅ SuccessFactors Payroll multi-entity | ⚠️ D365 HR limited for payroll; needs ISV | ✅ Oracle HCM Payroll multi-entity |
| HR-002 | PH Statutory Deductions (SSS etc.) | Must | ⚠️ SuccessFactors PH localization growing | 🔧 ISV partner for PH statutory (e.g., Itsubmit) | ⚠️ Oracle HCM PH payroll localization |
| HR-003 | BIR Withholding Tax (Compensation) | Must | ⚠️ PH tax tables via localization partner | 🔧 ISV partner for BIR compensation tax | ⚠️ PH tax tables via localization |
| HR-004 | 13th Month Pay | Must | ⚙️ Configure 13th month in payroll | ⚙️ Configure in payroll / ISV | ⚙️ Configure 13th month in payroll |
| HR-005 | Time & Attendance Integration | Should | ✅ SuccessFactors Time Tracking with biometric | ⚙️ T&A integration via D365 or third-party | ✅ Oracle Time & Labor with biometric |
| HR-006 | Shift Scheduling | Should | ✅ SF Employee Central scheduling | ⚙️ Shift scheduling via D365 or third-party | ✅ Oracle Workforce Scheduling |
| HR-007 | Leave Management | Must | ✅ SuccessFactors Leave Management | ⚙️ Leave management in D365 HR | ✅ Oracle Absence Management |
| HR-008 | Employee Self-Service | Nice | ✅ SuccessFactors ESS | ✅ D365 Employee self-service | ✅ Oracle HCM ESS |
| HR-009 | Recruitment & Onboarding | Nice | ✅ SuccessFactors Recruiting & Onboarding | ⚙️ D365 Talent or LinkedIn integration | ✅ Oracle Recruiting & Onboarding |
| HR-010 | Overtime Calculation | Must | ⚙️ Configure PH overtime rules | ⚙️ Configure overtime in payroll/ISV | ⚙️ Configure PH overtime rules |
| HR-011 | Holiday Pay Calculation | Must | ⚙️ Configure PH holiday rates | ⚙️ Configure holiday pay rules | ⚙️ Configure PH holiday pay rates |
| HR-012 | Bank File Generation | Must | ✅ Payroll bank file generation | ⚙️ Bank file via payroll / ISV | ✅ Payroll bank file generation |
| HR-013 | Employee Loan & Advance | Must | ⚙️ Configure loan deduction in payroll | 🔧 Custom loan management in D365 | ⚙️ Configure loan deductions in payroll |
| HR-014 | Grievance & Whistleblower | Should | 🔧 Custom case management | 🔧 Power App for grievance tracking | 🔧 Custom case management |
| HR-015 | PH Statutory Benefits & Claims | Must | ⚙️ Configure statutory benefits in payroll | 🔧 ISV partner for PH statutory claims | ⚙️ Configure statutory benefits in payroll |
| HR-016 | Employee Expense Reimbursement | Must | ✅ SuccessFactors / Concur integration | ✅ D365 Expense Management | ✅ Oracle Expenses Management |
| HR-017 | PPE & Uniform Lifecycle | Should | 🔧 Custom asset tracking | 🔧 Power App for PPE tracking | 🔧 Custom tracking extension |

**HR Summary**: All three require localization for Philippine payroll (SSS, PhilHealth, Pag-IBIG, BIR tax). SAP SuccessFactors and Oracle HCM are more complete HR suites. D365 HR is weaker on payroll — relies on ISV partners. **None have turnkey PH payroll** — all need a localization partner.

---

## R9. Customer Relationship & Loyalty (CRM)

| Req ID | Requirement | Priority | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|---|
| CRM-001 | Loyalty Points Engine | Must | ✅ SAP Loyalty Management | ✅ Native loyalty in D365 Commerce | 🔧 Oracle Loyalty (separate cloud) or custom |
| CRM-002 | Customer Master (B2C, 600K) | Must | ✅ SAP Customer Data Cloud | ✅ Customer master in D365 | ✅ Oracle Customer Data Management |
| CRM-003 | Trade Account Management (B2B) | Must | ✅ SAP SD with trade accounts | ✅ Customer accounts with credit limits | ✅ Oracle Receivables with trade accounts |
| CRM-004 | Corporate Account Mgmt | Must | ✅ Corporate accounts in SAP SD | ✅ Corporate accounts with negotiated pricing | ✅ Corporate accounts in Fusion |
| CRM-005 | Tiered Loyalty | Should | ✅ Tiered loyalty in SAP Loyalty | ✅ Tiered loyalty in D365 Commerce | ⚙️ Tiered loyalty via Oracle Loyalty Cloud |
| CRM-006 | Customer Purchase History | Should | ✅ SAP Customer Activity Repository (CAR) | ✅ Purchase history in D365 Commerce | ⚙️ Customer analytics in Oracle CX |
| CRM-007 | Marketing Campaign Integration | Nice | ✅ SAP Marketing Cloud integration | ✅ D365 Marketing / Customer Insights | ✅ Oracle CX Marketing integration |
| CRM-008 | Credit Application Workflow | Must | ✅ Credit management in SAP FI | ✅ Credit management in D365 | ✅ Oracle Credit Management |
| CRM-009 | PHILGEPS Compliance | Should | 🔧 Custom government bid management | 🔧 Custom Power App for gov't bids | 🔧 Custom government procurement module |
| CRM-010 | Customer Account Reactivation | Should | 🔧 Custom via SAP Marketing/Campaign | 🔧 Custom via D365 Marketing/Power BI | 🔧 Custom reactivation campaigns |
| CRM-011 | Customer Feedback-to-Action | Should | ⚙️ SAP Service Cloud feedback workflow | ⚙️ D365 Customer Service + Voice of Customer | ⚙️ Oracle Service Center feedback |
| CRM-012 | Trade Sales Pipeline & Territory | Should | ✅ SAP Sales Cloud with pipeline | ✅ D365 Sales pipeline management | ✅ Oracle Sales Cloud pipeline |
| CRM-013 | Trade Counter / Pro Desk | Should | 🔧 Custom trade counter workflow | 🔧 Custom POS extension for trade | 🔧 Custom trade counter process |
| CRM-014 | Customer Data Platform | Should | ✅ SAP Customer Data Platform | ✅ D365 Customer Insights (CDP) | ✅ Oracle CX Unity (CDP) |
| CRM-015 | Call Center Queue Management | Should | ✅ SAP Service Cloud omnichannel | ✅ D365 Customer Service omnichannel | ✅ Oracle Service Center omnichannel |
| CRM-016 | Loyalty Enrollment Journey | Should | ⚙️ SAP Loyalty + Marketing Cloud | ⚙️ D365 Commerce + Marketing orchestration | ⚙️ Oracle Loyalty + Marketing orchestration |

**CRM Summary**: D365 has the tightest integration between CRM, loyalty, and POS. SAP has strong but separate cloud products (Loyalty, Marketing, Sales Clouds). Oracle CX is comprehensive but fragmented across many cloud modules.

---

## R10. Analytics & Reporting (RPT)

| Req ID | Requirement | Priority | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|---|
| RPT-001 | Executive Dashboard | Must | ✅ SAP Analytics Cloud (SAC) | ✅ Power BI dashboards | ✅ Oracle BI / OTBI dashboards |
| RPT-002 | Store P&L | Must | ✅ CO-PA profitability by store | ✅ Power BI with financial data | ⚙️ P&L by cost center / segment |
| RPT-003 | Sales Analytics | Must | ✅ SAP CAR sales analytics | ✅ Power BI + D365 sales data | ⚙️ Oracle Sales Analytics |
| RPT-004 | Inventory Reports | Must | ✅ Standard inventory reports | ✅ Power BI + D365 inventory reports | ✅ Standard inventory reports |
| RPT-005 | Purchase Analysis | Should | ✅ MM reporting + SAC | ✅ Power BI procurement analytics | ⚙️ Oracle Procurement analytics |
| RPT-006 | BIR-Compliant Tax Reports | Must | 🔧 ISV/partner for BIR-specific formats | 🔧 ISV/partner for BIR-specific formats | 🔧 Partner localization for BIR reports |
| RPT-007 | Consolidated Financial Statements | Must | ✅ SAP Group Reporting | ✅ Financial reporting in D365 Finance | ✅ Oracle Financial Reporting Studio |
| RPT-008 | Ad-Hoc Reporting | Should | ✅ SAC ad-hoc analysis | ✅ Power BI self-service | ✅ Oracle BI ad-hoc analysis |
| RPT-009 | Mobile Dashboard | Nice | ✅ SAC mobile | ✅ Power BI mobile app | ✅ Oracle BI mobile |
| RPT-010 | Scheduled Report Distribution | Should | ✅ SAC scheduling & distribution | ✅ Power BI scheduled refresh + email | ✅ Oracle BI scheduling |
| RPT-011 | Category Performance Review | Should | ✅ CO-PA by category + CAR | ⚙️ Power BI category dashboards | ⚙️ Oracle BI category analytics |
| RPT-012 | Pricing Hierarchy Audit | Should | ⚙️ Pricing condition analysis reports | ⚙️ Pricing reports in D365 Commerce | 🔧 Custom pricing audit reports |

**RPT Summary**: All three have strong analytics. **Power BI (D365) is the most user-friendly self-service BI tool**. SAP Analytics Cloud and HANA are powerful but complex. Oracle BI is enterprise-grade but less intuitive.

---

## R11. Intercompany & Transfer Pricing (IC)

| Req ID | Requirement | Priority | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|---|
| IC-001 | IC AP/AR Automation | Must | ✅ Auto IC invoice generation (IDoc/SD-MM) | ✅ Intercompany AP/AR automation | ✅ Intercompany invoicing in Fusion |
| IC-002 | Arm's-Length Transfer Pricing | Must | ✅ IC pricing conditions configurable | ✅ IC pricing rules in trade agreements | ✅ IC transfer pricing rules |
| IC-003 | IC Elimination on Consolidation | Must | ✅ Auto elimination in Group Reporting | ✅ Auto elimination in consolidation | ✅ Auto elimination in consolidation |
| IC-004 | IC Settlement | Must | ✅ IC net settlement via payment run | ✅ IC settlement via centralized payments | ✅ IC settlement via payment process |
| IC-005 | IC Reconciliation | Must | ✅ IC reconciliation in Group Reporting | ✅ IC matching and reconciliation | ✅ IC reconciliation in consolidation |

**IC Summary**: All three handle intercompany well — this is core ERP functionality. SAP Group Reporting is the most mature for complex multi-entity consolidation.

---

## R12. Document Management (DOC)

| Req ID | Requirement | Priority | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|---|
| DOC-001 | Electronic Document Storage | Must | ✅ SAP Document Management / ArchiveLink | ✅ SharePoint / D365 document attachments | ✅ Oracle WebCenter / document attachments |
| DOC-002 | BIR-Compliant Invoice Format | Must | 🔧 Custom BIR invoice format in SAP | 🔧 Custom BIR invoice format in D365 | 🔧 Custom BIR invoice format in Fusion |
| DOC-003 | Delivery Receipt Tracking | Must | ✅ DR linked to PO/transfer in SD | ✅ Delivery notes linked to orders | ✅ Delivery tracking linked to orders |
| DOC-004 | Import Document Management | Must | ✅ Attach BL, customs, LC to import PO | ✅ Attach documents to PO in SharePoint | ✅ Attach import documents to PO |
| DOC-005 | Document Retention Policy | Must | ⚙️ Retention via SAP ILM / ArchiveLink | ⚙️ Retention via SharePoint policies | ⚙️ Retention via Oracle records management |
| DOC-006 | Approval with Attachments | Should | ✅ Workflow with document attachments | ✅ Power Automate with file attachments | ✅ Approval workflow with attachments |
| DOC-007 | Hazardous Waste Disposal Tracking | Should | 🔧 Custom hazmat tracking in SAP EHS | 🔧 Power App for hazmat tracking | 🔧 Custom hazmat tracking extension |
| DOC-008 | Enterprise Retention & Archiving | Must | ✅ SAP ILM for retention management | ⚙️ SharePoint compliance features | ⚙️ Oracle records management |

**DOC Summary**: All three support document management. SAP ILM is the most comprehensive for retention. D365 leverages SharePoint natively. **BIR-compliant invoice formatting is a gap for all three** — requires custom forms.

---

## R13. Master Data Management (MDM)

| Req ID | Requirement | Priority | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|---|
| MDM-001 | Centralized Item Master (55K SKUs) | Must | ✅ Material Master with governance | ✅ Product master with shared products | ✅ Item master with governance |
| MDM-002 | Item Attribute Management | Must | ✅ Classification system with rich attributes | ⚙️ Product attributes and attributes in D365 | ⚙️ Item descriptors and attribute groups |
| MDM-003 | Customer Data Quality | Must | ✅ SAP MDG for customer dedup/validation | ⚙️ Customer dedup rules in D365 | ⚙️ Customer data quality in Fusion |
| MDM-004 | Vendor Onboarding Workflow | Should | ✅ SAP MDG for supplier governance | ⚙️ Vendor approval workflow in D365 | ⚙️ Supplier onboarding workflow |
| MDM-005 | Pricing Master Governance | Must | ✅ Pricing condition with approval workflow | ⚙️ Trade agreements with approval | ⚙️ Price lists with approval workflow |
| MDM-006 | Location Master | Must | ✅ Plant/storage location master | ✅ Site/warehouse master | ✅ Organization/subinventory master |
| MDM-007 | Hierarchical Category Structure | Must | ✅ Material hierarchy (multi-level) | ✅ Product category hierarchy | ✅ Item category hierarchy |
| MDM-008 | Vendor Master Data Governance | Must | ✅ SAP MDG for vendor master governance | ⚙️ Vendor approval workflow + audit trail | ⚙️ Supplier master governance in Fusion |

**MDM Summary**: SAP MDG (Master Data Governance) is the gold standard for master data management with approval workflows, audit trails, and deduplication. D365 and Oracle have adequate but less mature governance capabilities.

---

## R14. Non-Functional Requirements (NFR)

| Req ID | Requirement | Priority | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|---|
| NFR-001 | POS Uptime (99.9%) | Must | ⚠️ Depends on SAP CCO architecture | ✅ CSU offline ensures POS availability | ❌ Third-party POS must ensure uptime |
| NFR-002 | Back-Office Uptime (99.5%) | Must | ✅ SAP SLA > 99.5% | ✅ Azure SLA > 99.9% | ✅ OCI SLA > 99.9% |
| NFR-003 | POS Transaction Speed (< 3s) | Must | ✅ SAP CCO transaction speed acceptable | ✅ D365 Commerce POS optimized for speed | 🔧 Third-party POS dependent |
| NFR-004 | Report Generation (< 30s) | Must | ✅ HANA in-memory analytics | ✅ Power BI with DirectQuery | ✅ Oracle BI with OTBI |
| NFR-005 | Concurrent Users (600–1,100) | Must | ✅ S/4HANA handles thousands of users | ✅ Azure auto-scales for users | ✅ OCI auto-scales for users |
| NFR-006 | Data Retention (7 years) | Must | ✅ SAP ILM for 7-year retention | ⚙️ Azure + D365 retention policies | ⚙️ Oracle data retention policies |
| NFR-007 | Security (RBAC, audit, encryption) | Must | ✅ SAP security framework | ✅ Azure security + D365 RBAC | ✅ Oracle security framework |
| NFR-008 | Scalability (300+ stores) | Must | ✅ S/4HANA proven at enterprise scale | ✅ Azure cloud scales dynamically | ✅ OCI scales for enterprise |
| NFR-009 | PH Localization | Must | ⚠️ Growing PH localization; gaps in BIR | ⚠️ Limited PH localization; ISV needed | ⚠️ Limited PH localization; partner needed |
| NFR-010 | Data Privacy (RA 10173) | Must | ⚙️ SAP can be configured for PH DPA | ⚙️ Azure complies; D365 configured for DPA | ⚙️ Oracle configured for PH DPA |
| NFR-011 | Offline POS (≥ 8 hours) | Must | ⚠️ SAP CCO offline mode has limitations | ✅ CSU full offline for extended periods | ❌ Third-party POS must provide this |
| NFR-012 | Integration Capability | Must | ✅ SAP BTP Integration Suite | ✅ Azure API Management + Logic Apps | ✅ Oracle Integration Cloud |
| NFR-013 | Disaster Recovery | Must | ✅ SAP DR on cloud | ✅ Azure Site Recovery | ✅ OCI disaster recovery |
| NFR-014 | Data Migration | Must | ✅ SAP Migration Cockpit / LSMW | ⚙️ D365 Data Management Framework | ⚙️ Oracle FBDI / data import tools |
| NFR-015 | Batch Processing Windows | Must | ✅ SAP background processing | ✅ Azure batch processing | ✅ Oracle scheduled processes |
| NFR-016 | Data Privacy Breach Response | Must | ⚙️ Configure breach response workflow | ⚙️ Configure breach response in D365 | ⚙️ Configure breach response in Fusion |
| NFR-017 | LGU Business Permit Tracking | Must | 🔧 Custom LGU permit tracking | 🔧 Power App for LGU permits | 🔧 Custom permit tracking extension |
| NFR-018 | ESG & Sustainability Reporting | Should | ⚙️ Sustainability analytics via SAP | 🔧 Power BI + custom ESG tracking | 🔧 Custom ESG reporting |
| NFR-019 | Fleet Optimization | Should | 🔧 SAP TM + custom telematics | 🔧 Azure Maps + custom fleet app | 🔧 Custom fleet optimization |
| NFR-020 | AI & Innovation Framework | Nice | ✅ SAP AI Core / Business AI | ✅ Azure AI / Copilot | ✅ Oracle AI / OCI AI Services |
| NFR-021 | Smart Store Operations | Should | 🔧 Custom IoT integration | 🔧 Azure IoT + Power Apps | 🔧 Custom smart store solutions |
| NFR-022 | Local & Partner Governance | Should | 🔧 Custom partner governance | 🔧 Power Apps for partner management | 🔧 Custom partner governance |
| NFR-022a | BIR CAS Registration per Location | Must | 🔧 Custom BIR CAS registration tracking | 🔧 Power App for BIR CAS tracking | 🔧 Custom BIR CAS registration |
| NFR-023 | Enterprise API Management | Should | ✅ SAP API Management on BTP | ✅ Azure API Management | ✅ Oracle API Gateway |
| NFR-024 | IT Asset Lifecycle | Should | ⚙️ SAP Asset Accounting for IT assets | 🔧 Custom IT asset tracking in D365 | 🔧 Custom IT asset tracking |
| NFR-025 | Employee IT Provisioning | Must | ⚙️ SuccessFactors onboarding → SAP auth | ⚙️ D365 HR → Azure AD provisioning | ⚙️ Oracle HCM → OCI IAM provisioning |
| NFR-026 | BI & Data Governance | Should | ✅ SAP Datasphere + SAC | ✅ Azure Synapse + Power BI | ✅ Oracle Autonomous DW + BI |
| NFR-027 | Omni-channel CDP | Should | ✅ SAP Customer Data Platform | ✅ D365 Customer Insights | ✅ Oracle CX Unity |
| NFR-028 | POS Hardware Maintenance | Should | ⚙️ SAP Solution Manager for ITSM | 🔧 Power App / ServiceNow integration | 🔧 Custom ITSM extension |

**NFR Summary**: All three meet cloud uptime, scalability, and security requirements. **D365 Commerce CSU offline capability is the only native solution for 8-hour POS offline** — a critical differentiator. SAP and Oracle rely on POS-specific solutions for offline. Philippine localization is a gap for all three.

---

## R15–R18. Cross-Functional Requirements (SRV, WSL, GOV, MER)

These requirements span installation services, wholesale, corporate governance, and merchandising. Most require customization across all three platforms.

| Category | Req IDs | SAP S/4HANA | MS D365 | Oracle Fusion | Notes |
|---|---|---|---|---|---|
| **R15. Installation & Services** | SRV-001, SRV-002 | 🔧 Custom service order + scheduling | 🔧 D365 Field Service / custom | 🔧 Oracle Field Service / custom | None have turnkey DIY workshop mgmt |
| **R16. Wholesale & Reseller** | WSL-001, WSL-002 | ✅ SAP SD wholesale pricing | ⚙️ D365 wholesale via trade agreements | ⚙️ Oracle Order Management wholesale | Core wholesale is supported; pro desk needs custom |
| **R17. Governance & Legal** | GOV-001 to GOV-029 | 🔧 Mostly custom / SAP GRC for some | 🔧 Mostly Power Apps / custom | 🔧 Mostly custom extensions | Corporate governance is niche; no ERP handles natively |
| **R18. Merchandising & Cross-Func** | MER-001, MER-002, CRM-015, CRM-016, FIN-031, FIN-032 | 🔧 Custom workflows | 🔧 Power Apps + Power Automate | 🔧 Custom workflows | Merchandising execution is retail-specific custom |

---

## Capability Heat Map Summary

| Category | Must Have Count | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|---|
| R1. Financial Management (FIN) | 22 | ✅✅✅✅✅ | ✅✅✅✅✅ | ✅✅✅✅✅ |
| R2. Inventory (INV) | 12 | ✅✅✅✅✅ | ✅✅✅✅ | ✅✅✅✅ |
| R3. Procurement (PUR) | 12 | ✅✅✅✅✅ | ✅✅✅✅ | ✅✅✅✅ |
| R4. Warehouse (WMS) | 5 | ✅✅✅✅✅ | ✅✅✅✅ | ✅✅✅✅ |
| R5. POS & Retail (POS) | 17 | ⚠️⚠️⚠️ | ✅✅✅✅✅ | ❌❌❌ |
| R6. Ecommerce (ECOM) | 9 | ✅✅✅✅ | ✅✅✅✅✅ | ✅✅✅ |
| R7. Supply Chain (SCP) | 3 | ✅✅✅✅✅ | ✅✅✅✅ | ✅✅✅✅ |
| R8. HR & Payroll (HR) | 11 | ✅✅✅✅ | ⚠️⚠️⚠️ | ✅✅✅✅ |
| R9. CRM & Loyalty (CRM) | 5 | ✅✅✅✅ | ✅✅✅✅✅ | ✅✅✅ |
| R10. Analytics (RPT) | 5 | ✅✅✅✅✅ | ✅✅✅✅✅ | ✅✅✅✅ |
| R11. Intercompany (IC) | 5 | ✅✅✅✅✅ | ✅✅✅✅✅ | ✅✅✅✅✅ |
| R12. Document Mgmt (DOC) | 5 | ✅✅✅✅ | ✅✅✅✅ | ✅✅✅✅ |
| R13. Master Data (MDM) | 5 | ✅✅✅✅✅ | ✅✅✅✅ | ✅✅✅✅ |
| R14. Non-Functional (NFR) | 14 | ✅✅✅✅ | ✅✅✅✅✅ | ✅✅✅✅ |
| R15–R18. Cross-Functional | 6 | ⚠️⚠️ | ⚠️⚠️ | ⚠️⚠️ |

> More ✅ = stronger coverage in that category. ⚠️ = gaps exist. ❌ = significant gap.

---

## Critical Disqualifier Assessment

| Disqualifier Check | SAP S/4HANA | MS D365 | Oracle Fusion |
|---|---|---|---|
| **600 POS terminals with offline** | ⚠️ Risk — SAP CCO not proven at this scale | ✅ Pass — D365 Commerce POS proven | ❌ Fail — No native POS |
| **BIR tax compliance (VAT, WHT, forms)** | ⚠️ Risk — Needs ISV add-on | ⚠️ Risk — Needs ISV add-on | ⚠️ Risk — Needs partner localization |
| **PH payroll (SSS, PhilHealth, Pag-IBIG)** | ⚠️ Risk — Needs localization partner | ⚠️ Risk — Needs ISV payroll partner | ⚠️ Risk — Needs localization partner |
| **2.8M POS transactions/month** | ✅ Pass — HANA handles volume | ✅ Pass — Azure + CSU handles volume | ⚠️ Risk — Depends on third-party POS |
| **5-entity consolidation** | ✅ Pass — Best-in-class | ✅ Pass — Strong | ✅ Pass — Strong |
| **Catch-weight / variable measure** | ⚠️ Risk — Needs EWM config | ⚠️ Risk — Needs product variant config | ⚠️ Risk — Limited native support |
| **Real-time inventory (200 stores + 4 DCs)** | ✅ Pass — Real-time in HANA | ✅ Pass — Real-time in D365 | ✅ Pass — Real-time in Fusion |

---

## Recommendation Matrix

| Criteria | SAP S/4HANA | Microsoft D365 | Oracle Fusion |
|---|---|---|---|
| **Best for** | Largest enterprises; complex supply chain; deep financials | Mid-to-large retail; unified commerce; fastest time-to-value | Enterprise-grade with Oracle ecosystem preference |
| **Biggest strength** | End-to-end breadth; IBP; consolidation; MDM | Native retail POS + Commerce; Power Platform; Azure | Strong HCM & ERP; OCI cloud; EPM for consolidation |
| **Biggest risk** | POS immaturity; highest TCO; longest implementation | PH payroll gaps; less mature supply chain planning | No native POS; fragmented cloud modules; integration complexity |
| **Philippine readiness** | ⚠️ Growing — partners available | ⚠️ Limited — ISV ecosystem emerging | ⚠️ Limited — partner ecosystem smaller |
| **Retail fitness** | ⚠️ Acceptable — POS is weak link | ✅ Strong — native retail suite | ❌ Weak — no native POS/retail |
| **Overall verdict** | **Conditional** — strong ERP but POS needs third-party | **Proceed** — best retail fit; address PH gaps | **Conditional** — strong ERP but POS & retail are major gaps |

---

## Next Steps

1. **Request vendor demos** using BuildRight-specific scenarios (offline POS, catch-weight selling, BOPIS fulfillment, BIR tax filing)
2. **Engage Philippines-local implementation partners** for each platform to assess localization readiness
3. **Validate third-party POS options** for SAP and Oracle (e.g., LS Retail, Oracle Retail Xstore)
4. **Request TCO proposals** with 5-year projections including POS terminals, users, and cloud infrastructure
5. **Score each system** using the [Scoring Methodology](../07-methodology/scoring-methodology.md) and complete scorecards

---

*Document Version: 1.0 | Date: 2026-06-03 | 261 requirements evaluated across 18 categories for 3 ERP systems*
