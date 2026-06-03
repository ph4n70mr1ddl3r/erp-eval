# Model Company — ERP Requirements Specification

> This document defines the detailed functional and non-functional requirements that any
> ERP system must meet to serve BuildRight Depot Corp. ERP-specific subfolders will reference
> this document and detail how their product addresses each requirement.

---

## R1. Financial Management

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| FIN-001 | Multi-entity General Ledger (5 entities) | Must Have | Shared COA with entity segment |
| FIN-002 | Automated Intercompany Elimination | Must Have | IC AP/AR, IC revenue/expense |
| FIN-003 | Consolidated Financial Reporting | Must Have | PFRS/IFRS compliant |
| FIN-004 | Accounts Payable with 3-Way Match | Must Have | PO → GR → Invoice |
| FIN-005 | Accounts Receivable for B2B | Must Have | Trade & corporate accounts |
| FIN-006 | Philippine VAT (12%) Processing | Must Have | Input/output VAT tracking |
| FIN-007 | Withholding Tax (Expanded) | Must Have | Auto-calculate EWT per vendor |
| FIN-008 | BIR Tax Return Generation | Must Have | 2550M, 2550Q, 1601-E, 1601-C, 1702 |
| FIN-009 | Multi-Bank Integration | Should Have | BDO, BPI, Metrobank formats |
| FIN-010 | Cash Management / Treasury | Should Have | Daily cash position, bank sweeps |
| FIN-011 | Fixed Asset Management | Must Have | Depreciation (PFRS), asset tracking |
| FIN-012 | Budgeting & Variance Analysis | Should Have | Annual budget, monthly variance |
| FIN-013 | Landed Cost Calculation | Must Have | Import duty, freight, insurance allocation |
| FIN-014 | Multi-Currency | Must Have | PHP base; USD for imports |
| FIN-015 | Period-End Close Workflow | Must Have | Month-end within 5 working days |
| FIN-016 | Capital Expenditure Workflow | Must Have | Capex request, tiered approval, budget check, asset capitalization |
| FIN-017 | Petty Cash Management | Must Have | Disbursement, replenishment, reconciliation per location (200 stores + 4 DCs) |
| FIN-018 | Consignment Settlement | Should Have | Sell-through reporting and vendor payment for consignment goods |
| FIN-019 | Vendor Rebate Management | Should Have | Rebate accrual, tracking, and settlement per vendor agreement |

## R2. Inventory Management

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| INV-001 | Perpetual Inventory (all locations) | Must Have | 200 stores + 4 DCs + HQ |
| INV-002 | Real-Time Inventory Visibility | Must Have | Across all locations |
| INV-003 | Weighted Average Cost (WAC) | Must Have | Philippine standard |
| INV-004 | ABC Classification | Must Have | Auto-classify by revenue contribution |
| INV-005 | Multi-Location Stock Transfer | Must Have | DC→Store, Store→Store, DC→DC |
| INV-006 | Cycle Counting | Must Have | Scheduled per section/category |
| INV-007 | Physical Inventory (Wall-to-Wall) | Must Have | Annual full count |
| INV-008 | Lot & Serial Tracking | Should Have | For select high-value items |
| INV-009 | Consignment Inventory | Should Have | Vendor-owned until sold |
| INV-010 | Catch-Weight / Variable Measure | Must Have | Lumber (board feet), wire (meters) — critical for big-box hardware retail |
| INV-011 | Inventory Aging Analysis | Should Have | Identify slow-moving/dead stock |
| INV-012 | Safety Stock & Reorder Point | Must Have | Per SKU, auto-calculated |
| INV-013 | Batch/LOT Tracking for Paint | Should Have | Paint mixing, batch traceability |
| INV-014 | In-Transit Inventory | Must Have | Visibility during DC→Store shipment |
| INV-015 | Inventory Valuation Reports | Must Have | By location, category, entity |
| INV-016 | Product Recall Tracking | Should Have | Lot/serial-based withdrawal, customer notification, and regulatory reporting |
| INV-017 | Consignment Inventory Tracking | Must Have | Non-valuated receipt, vendor ownership indicator, ownership transfer at sale, sell-through reporting |
| INV-018 | VMI Inventory Tracking | Should Have | Vendor-owned stock tracking with sell-through data sharing and settlement |

## R3. Procurement & Purchasing

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| PUR-001 | Purchase Order Management | Must Have | Create, approve, receive, close |
| PUR-002 | Automated Replenishment (MRP/ROP) | Must Have | Auto-generate POs based on ROP/EOQ |
| PUR-003 | Vendor Management | Must Have | 800–1,000 active vendors |
| PUR-004 | Import Purchase Orders | Must Have | LC tracking, customs, landed cost |
| PUR-005 | 3-Way Matching | Must Have | PO vs GR vs Invoice |
| PUR-006 | Blanket/Contract Purchase Orders | Should Have | Annual supply agreements |
| PUR-007 | Vendor Portal | Nice to Have | Vendors view POs, submit invoices |
| PUR-008 | Vendor Performance Scorecard | Should Have | On-time delivery, quality, fill rate |
| PUR-009 | Multi-Entity Procurement | Must Have | Central buying, entity-level receipt |
| PUR-010 | Approval Workflow | Must Have | Tiered by amount; PO > PHP 50K needs manager |
| PUR-011 | Goods Receipt Processing | Must Have | At DC and at store (DSD) |
| PUR-012 | Return to Vendor (RTV) | Must Have | Defective, overage, wrong items |
| PUR-013 | Direct Store Delivery (DSD) | Must Have | Store-level GR against PO; 3-way AP matching for DSD goods (~30% of inbound) |
| PUR-014 | Vendor Managed Inventory | Should Have | Sell-through data sharing, ASN receipt, auto-confirmation, and settlement |
| PUR-015 | Vendor Rebate Management | Should Have | Rebate accrual, tracking, and settlement per agreement |

## R4. Warehouse Management

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| WMS-001 | RF/Barcode Directed Operations | Must Have | Putaway, pick, pack, ship |
| WMS-002 | Cross-Dock Capability | Should Have | Fast movers bypass storage |
| WMS-003 | Wave/Zone Picking | Should Have | For store replenishment orders |
| WMS-004 | Receiving & Putaway | Must Have | Against PO or transfer order |
| WMS-005 | Shipping & Dispatch | Must Have | Store delivery planning |
| WMS-006 | Yard Management (Lumber) | Should Have | Outdoor inventory for lumber/building materials |
| WMS-007 | Label Printing | Must Have | Barcodes, bin labels, shipping labels |
| WMS-008 | WMS Integration with ERP | Must Have | Real-time inventory sync |

## R5. Point-of-Sale (POS) & Retail

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| POS-001 | 600 POS Terminals | Must Have | 3 per store × 200 stores |
| POS-002 | Offline Mode | Must Have | Must sell during network outage |
| POS-003 | Barcode Scanning | Must Have | 1D + 2D barcode support |
| POS-004 | Multi-Tender | Must Have | Cash, card, e-wallet, split |
| POS-005 | Loyalty Integration | Must Have | Points earn/redeem at POS |
| POS-006 | Price Override (w/ Auth) | Must Have | Manager approval for manual price |
| POS-007 | Returns & Exchanges | Must Have | With/without receipt; store credit |
| POS-008 | Cash Drawer Management | Must Have | Float, cash count, deposit |
| POS-009 | End-of-Day Reconciliation | Must Have | Z-report, cash vs system variance |
| POS-010 | Quantity Break Pricing | Must Have | Auto-tiered pricing at POS |
| POS-011 | Customer Display | Should Have | Pole display or customer-facing screen |
| POS-012 | Receipt Printing | Must Have | Thermal; BIR-registered format |
| POS-013 | Real-Time Inventory Deduction | Must Have | Immediate sync to central inventory |
| POS-014 | Promotional Pricing Auto-Apply | Must Have | No cashier intervention needed; system auto-applies promotional price based on date, SKU, and quantity rules |
| POS-014a | Senior Citizen & PWD Discount Compliance (PH Legal) | Must Have | Auto-detect SC/PWD from ID scan, apply 20% discount on eligible items per RA 9994/RA 10754, VAT-exemption for senior citizens per RA 9994, mandatory logs for audit trail, BIR-compliant reporting |
| POS-015 | Gift Card / Store Credit | Should Have | Issuance, reload, redemption, balance inquiry, expiry, and breakage accounting |
| POS-016 | Catch-Weight / Variable Measure at POS | Must Have | Weight-based (kg) and cut-to-length (m, board ft) selling — critical for lumber, wire, bulk nails |
| POS-017 | Paint Mixing / Custom SKU at POS | Must Have | Generate custom SKU for tinted paint; link to base paint + colorant inventory |
| POS-018 | Age-Restricted Product Prompts | Should Have | Mandatory prompt for solvents, cutting tools, etc.; requires cashier confirmation |
| POS-019 | Warranty Claim Registration | Should Have | Record warranty claims at POS; link to vendor return or repair tracking |

## R6. Ecommerce Integration

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| ECOM-001 | Real-Time Inventory Sync | Must Have | Per-store availability on website |
| ECOM-002 | Real-Time Price Sync | Must Have | Including promotions |
| ECOM-003 | BOPIS Order Flow | Must Have | Order → Store pick → Customer pickup |
| ECOM-004 | Home Delivery Order Flow | Must Have | Order → DC pick → Ship to customer |
| ECOM-005 | Order Status Tracking | Must Have | Customer-facing tracking |
| ECOM-006 | Payment Gateway Integration | Must Have | PayMongo, Dragonpay, GCash |
| ECOM-007 | Return Initiation (Online) | Must Have | Process completed in-store |
| ECOM-008 | Customer Data Sync | Must Have | Ecommerce ↔ ERP ↔ Loyalty |
| ECOM-009 | Product Catalog Sync | Must Have | Item master, images, specs |
| ECOM-010 | Promo/Coupon Integration | Should Have | Online promotions synced |
| ECOM-011 | Home Delivery Fulfillment | Must Have | DC pick, carrier dispatch, real-time tracking, proof of delivery, failed delivery handling |
| ECOM-012 | Delivery Partner Integration | Must Have | API integration with 3PL carriers (Lalamove, Transportify, own fleet) for order dispatch and status |

## R7. Supply Chain Planning

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| SCP-001 | Demand Forecasting | Should Have | Historical sales-based forecasting |
| SCP-002 | Replenishment Planning (DC→Store) | Must Have | Auto-generate transfer orders |
| SCP-003 | Reorder Point Calculation | Must Have | Per SKU per location |
| SCP-004 | Safety Stock Optimization | Should Have | Dynamic based on demand variability |
| SCP-005 | Seasonal Planning | Should Have | Forward buy for peak seasons |
| SCP-006 | Allocation Management | Should Have | Constrained supply allocation to stores |
| SCP-007 | Purchase Recommendation | Must Have | Suggested POs based on stock levels |

## R8. HR & Payroll

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| HR-001 | Multi-Entity Payroll | Must Have | 5 entities, semi-monthly runs |
| HR-002 | Philippine Statutory Deductions | Must Have | SSS, PhilHealth, Pag-IBIG |
| HR-003 | BIR Withholding Tax (Compensation) | Must Have | TRAIN law tax tables |
| HR-004 | 13th Month Pay Computation | Must Have | Auto-calculate and schedule |
| HR-005 | Time & Attendance Integration | Should Have | Biometric/RFID feed |
| HR-006 | Shift Scheduling | Should Have | For store-level staff |
| HR-007 | Leave Management | Must Have | VL, SL, maternity, paternity, etc. |
| HR-008 | Employee Self-Service | Nice to Have | Payslips, leave requests |
| HR-009 | Recruitment & Onboarding | Nice to Have | Job posting, applicant tracking |
| HR-010 | Overtime Calculation | Must Have | Philippine Labor Code premiums |
| HR-011 | Holiday Pay Calculation | Must Have | Regular + Special holiday rates |
| HR-012 | Bank File Generation | Must Have | For payroll crediting |

## R9. Customer Relationship & Loyalty

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| CRM-001 | Loyalty Points Engine | Must Have | Earn, redeem, expire |
| CRM-002 | Customer Master (B2C) | Must Have | 600,000 members |
| CRM-003 | Trade Account Management (B2B) | Must Have | 5,000 accounts with credit limits |
| CRM-004 | Corporate Account Management | Must Have | 200 accounts with negotiated pricing |
| CRM-005 | Tiered Loyalty | Should Have | Bronze, Silver, Gold, Platinum |
| CRM-006 | Customer Purchase History | Should Have | For personalization and service |
| CRM-007 | Marketing Campaign Integration | Nice to Have | Promo targeting by segment |
| CRM-008 | Credit Application Workflow | Must Have | Trade/corporate credit application, credit assessment, tiered approval, annual review |

## R10. Analytics & Reporting

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| RPT-001 | Executive Dashboard | Must Have | Revenue, margin, inventory, cash |
| RPT-002 | Store P&L | Must Have | Per-store profitability |
| RPT-003 | Sales Analytics | Must Have | By store, category, SKU, time period |
| RPT-004 | Inventory Reports | Must Have | Stock status, aging, turns |
| RPT-005 | Purchase Analysis | Should Have | Spend by vendor, category |
| RPT-006 | BIR-Compliant Tax Reports | Must Have | For monthly/quarterly filing |
| RPT-007 | Consolidated Financial Statements | Must Have | BS, IS, CF, Equity Changes |
| RPT-008 | Ad-Hoc Reporting | Should Have | Self-service report builder |
| RPT-009 | Mobile Dashboard | Nice to Have | For executives on the go |
| RPT-010 | Scheduled Report Distribution | Should Have | Auto-email weekly/monthly reports |

## R11. Intercompany & Transfer Pricing

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| IC-001 | Intercompany AP/AR Automation | Must Have | Auto-generate IC invoices for leasing, distribution fees, ecommerce fulfillment |
| IC-002 | Arm's-Length Transfer Pricing | Must Have | Configurable IC pricing rules per service/goods flow |
| IC-003 | IC Elimination on Consolidation | Must Have | Automatic elimination of IC revenue, expense, receivable, payable during consolidation |
| IC-004 | IC Settlement | Must Have | Net settlement between entities; bank transfer generation |
| IC-005 | IC Reconciliation | Must Have | Monthly reconciliation of IC balances across entities |

## R12. Document Management

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| DOC-001 | Electronic Document Storage | Must Have | Attach invoices, receipts, delivery receipts, LCs, customs docs to transactions |
| DOC-002 | BIR-Compliant Invoice Format | Must Have | Registered sales invoices, official receipts per BIR requirements |
| DOC-003 | Delivery Receipt Tracking | Must Have | DR linked to PO/transfer order and goods receipt |
| DOC-004 | Import Document Management | Must Have | Store and track BL, customs declaration, LC, packing lists per import PO |
| DOC-005 | Document Retention Policy | Must Have | 7-year retention per BIR; configurable per document type |
| DOC-006 | Approval Workflow with Attachments | Should Have | Route documents (capex requests, vendor contracts) with file attachments for approval |

## R13. Master Data Management

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| MDM-001 | Centralized Item Master | Must Have | Single source of truth for 55K SKUs; controlled creation/modification workflow |
| MDM-002 | Item Attribute Management | Must Have | Rich attributes per category (e.g., tile: material, size, finish; lumber: species, dimensions) |
| MDM-003 | Customer Data Quality | Must Have | Deduplication, validation rules for 600K+ customer records |
| MDM-004 | Vendor Onboarding Workflow | Should Have | Structured vendor creation with approval, tax info (TIN), banking details |
| MDM-005 | Pricing Master Governance | Must Have | Controlled price list creation/modification with approval workflow |
| MDM-006 | Location Master | Must Have | Stores, DCs, HQ as distinct locations with address, tax registration, operating params |
| MDM-007 | Hierarchical Category Structure | Must Have | Multi-level product category tree for reporting and merchandising |

## R14. Non-Functional Requirements

| Req ID | Requirement | Target |
|---|---|---|
| NFR-001 | POS Uptime | 99.9% |
| NFR-002 | Back-Office Uptime | 99.5% |
| NFR-003 | POS Transaction Speed | < 3 seconds |
| NFR-004 | Report Generation | < 30 seconds (standard) |
| NFR-005 | Concurrent Users | 600–1,100 |
| NFR-006 | Data Retention | 7 years (BIR) |
| NFR-007 | Security | Role-based access, audit trails, encryption |
| NFR-008 | Scalability | Support growth to 300+ stores |
| NFR-009 | Localization | Full Philippine localization (language, tax, regulatory) |
| NFR-010 | Data Privacy | RA 10173 (Data Privacy Act) compliance |
| NFR-011 | Offline POS Capability | POS terminals must continue selling during network outages (≥ 8 hours offline); auto-sync upon reconnection |
| NFR-012 | Integration Capability | Must support standard integration methods with all external systems listed in [Integration Touchpoints](model-company-profile.md#143-integration-touchpoints) |
| NFR-013 | Disaster Recovery | RPO ≤ 1 hour; RTO ≤ 4 hours for core; POS must operate offline 8+ hours with automatic sync reconciliation upon reconnection |
| NFR-014 | Data Migration | Tools/process for migrating from legacy accounting, POS, payroll, and inventory data |
| NFR-015 | Batch Processing Windows | Month-end close, payroll runs, and bulk report generation must complete within defined off-peak windows (see [Data Volumes §5](data-volumes-and-integrations.md#5-batch-processing-windows)) |
| NFR-016 | Data Privacy Breach Response | Must Have | Automated breach register, NPC notification workflow, forensic audit trail, data subject notification capability per RA 10173 |
| NFR-017 | LGU Business Permit Tracking per Location | Must Have | Per-location permit calendar, renewal alerting, permit document storage, and permit status dashboard for 200+ LGU jurisdictions |
| NFR-018 | ESG & Sustainability Reporting | Should Have | System-level capability to track carbon footprint, waste redirection, social impact, and ethical vendor audit metrics (see GOV-008 for operational governance workflows) |
| NFR-019 | Advanced Fleet Optimization | Should Have | GPS/telematics tracking, fuel management, routing optimization, and port demurrage fee avoidance |
| NFR-020 | AI & Innovation Framework | Nice to Have | AI personalization, RPA automation, predictive maintenance, and computer vision for stock audits |
| NFR-021 | Smart Store Operations | Should Have | Mobile POS queue busting, Smart Safe cash reconciliation, 3D custom design rendering, and Smart Locker integration |
| NFR-022 | Local & Partner Governance | Should Have | Barangay community relations, 3PL/install partner audits, ecommerce returns logistics, and BIR CAS compliance |
| NFR-022a | BIR CAS Registration per Location | Must Have | BIR Computerized Accounting System (CAS) registration per location/store, permit renewal tracking, CAS compliance documentation management, registration status dashboard |
| FIN-020 | Duplicate Vendor Invoice Detection | Must Have | System auto-detects duplicate vendor invoices by invoice number, vendor+amount+date, or PO reference+invoice number; blocks duplicates and alerts AP Clerk with matching reference |
| FIN-021 | FX Hedging / Forward Contract Management | Should Have | Record and track USD forward contracts (notional amount, forward rate, maturity, counterparty bank); FX exposure reporting; no speculative positions — hedging for committed import payables only |
| FIN-022 | Bad Debt Write-Off & Recovery | Must Have | Bad debt write-off with tiered approval; BIR-compliant documentation (demand letter, collection report, court filing); write-off recovery posting; separate tracking from regular AR collections |
| POS-020 | Layaway / Installment Sales | Should Have | Layaway agreement creation with deposit collection, installment schedule, inventory reservation (excluded from ATP), cancellation with fee, forfeiture with income recognition, and completion with revenue/COGS recognition |
| POS-021 | Multi-DC Order Splitting (Ecommerce) | Should Have | For ecommerce orders where no single DC has ATP for all items, system splits order into sub-orders per fulfillment DC with separate tracking per sub-order while presenting unified customer experience |
| POS-022 | Employee Discount at POS | Should Have | Configurable employee discount rate applied at POS via employee ID badge; monthly purchase limit per employee; per-SKU quantity limit; discount does not stack with promotional pricing (lower of employee discount or promo price applies); excluded from catch-weight and clearance items; employee purchases logged with employee ID and running monthly total |
| HR-013 | Employee Loan & Advance Management | Must Have | Loan/advance request with eligibility validation, tiered approval, automatic payroll deduction with minimum wage protection, loan portfolio reporting, and final pay settlement at separation |
| HR-014 | Employee Grievance & Whistleblower Case Management | Should Have | Grievance submission (identified and anonymous), case management with severity classification, investigation tracking, retaliation protection flagging, and resolution documentation |
| CRM-009 | Government Procurement Compliance (PHILGEPS) | Should Have | PHILGEPS registration tracking, government bid/quotation management, government-specific billing and collection procedures, separate government receivable aging |
| CRM-010 | Customer Account Reactivation | Should Have | Dormant account identification (no transaction > 6 months), automated reactivation outreach campaigns, win-back offers, reactivation success tracking |
| CRM-011 | Customer Feedback-to-Action Loop | Should Have | Systematic feedback collection (NPS, CSAT), feedback categorization and routing, action item assignment to responsible teams,闭环 tracking of feedback-driven improvements |
| CRM-012 | Trade Sales Pipeline & Territory Management | Should Have | Trade sales pipeline stages (lead → qualify → quote → negotiate → close), territory assignment and management, pipeline forecasting, sales rep performance tracking |
| CRM-013 | Trade Counter / Pro Desk Operations | Should Have | Dedicated trade counter workflow for professional customers, quick quote generation, express checkout for trade accounts, order history lookup, product availability inquiry |
| CRM-014 | Customer Data Platform & Hyper-Personalization | Should Have | Unified customer profile across POS, ecommerce, loyalty, CRM, support; identity resolution and deduplication; consent management per RA 10173; segment creation for marketing |
| DOC-007 | Hazardous Waste Disposal Tracking | Should Have | DENR-compliant hazardous waste manifest tracking, per-location waste generator registration renewal, transporter accreditation tracking, quarterly disposal reporting per location |
| PUR-016 | Configurable AQL Sampling per SKU Category | Should Have | Configurable Acceptable Quality Level parameters per SKU category at goods receipt; AQL sampling plan selection; inspection checklist per category; quality hold process with aging tracking |
| HR-015 | Philippine Statutory Benefits & Claims Management | Must Have | Managed advances, online agency portal certification, and automated semi-monthly payroll deductions for SSS, PhilHealth, and Pag-IBIG |
| HR-016 | Employee Expense Reimbursement | Must Have | Expense report submission with receipt attachment, tiered approval by amount, mileage calculation, per-diem rates, reimbursement via payroll or separate bank transfer |
| HR-017 | Employee PPE & Uniform Lifecycle | Should Have | PPE/uniform issuance tracking per employee, replacement schedule, size/quantity management, cost allocation to department/location |
| FIN-023 | Insurance Policy Lifecycle Management | Should Have | Policy registry (property, liability, vehicle, cargo, business interruption), premium tracking, renewal alerting, claims filing, and coverage allocation to entities/locations |
| FIN-024 | Employee Gratuity & Retirement Fund (RA 7641) | Must Have | Auto-calculate retirement gratuity per RA 7641, retirement fund accrual, separation pay vs. retirement pay distinction, half-month pay per year of service formula |
| FIN-025 | Cash-in-Transit (CIT) & Armored Car Management | Should Have | CIT service scheduling, cash pickup/delivery tracking, custody transfer confirmation, armored car vendor SLA monitoring, reconciliation with bank deposits |
| FIN-026 | Product Costing & Margin Analysis | Should Have | Standard cost vs. actual cost variance analysis, margin analysis by category/SKU/store/channel, landed cost roll-up into item cost, what-if costing scenarios |
| FIN-027 | Customer Refund & Credit Processing | Must Have | Refund request workflow (cash, card, store credit), credit memo generation, refund approval tiers, refund aging tracking, BIR-compliant credit note issuance |
| FIN-028 | Customer Credit Collection & Escalation | Must Have | Collection call logging, promise-to-pay tracking, automated aging-based escalation, collection letter generation, write-off recommendation trigger |
| FIN-029 | Intercompany Dividend & Loan Management | Should Have | IC dividend declaration and distribution workflow, IC loan setup with interest calculation, loan amortization scheduling, IC loan balance reconciliation |
| FIN-030 | Fixed Asset Physical Verification | Should Have | Periodic fixed asset physical count, asset tag scanning, missing/damaged asset flagging, reconciliation with fixed asset register, discrepancy resolution workflow |
| POS-023 | Store-Level Customer Delivery Scheduling | Should Have | Delivery order creation at POS for bulky items, delivery date/time slot selection, delivery fee calculation by distance/zone, driver/dispatch assignment, proof-of-delivery capture |
| ECOM-013 | Marketplace Integration (Lazada/Shopee) | Should Have | Product listing sync, order pull from marketplace, inventory reservation across channels, marketplace-specific pricing, fulfillment status push, commission/fee reconciliation |
| ECOM-014 | Ship-from-Store Fulfillment | Should Have | Order routing to nearest store with ATP, store pick & pack workflow, carrier handoff, customer notification, inventory deduction at ship-from-store location |
| ECOM-015 | Omni-channel Customer Ticketing & Support | Should Have | Unified ticket creation from email, chat, phone, social, in-store; ticket routing & SLA management; customer 360 view; escalation workflow; satisfaction survey post-resolution |
| ECOM-016 | Ecommerce Order Exception & Cancellation Management | Should Have | Order exception handling (payment failure, inventory unavailability, fraud hold), cancellation workflow with auto-refund, partial cancellation, restock trigger on cancellation |
| INV-019 | Multi-Channel Inventory Allocation Governance | Should Have | Configurable inventory reservation rules per channel (POS, BOPIS, home delivery, marketplace), allocation priority hierarchy, safety stock buffers per channel, reallocation triggers when channel demand shifts |
| INV-020 | Proactive Store Inventory Rebalancing | Should Have | System-suggested rebalancing based on demand patterns, store-to-DC return for excess, store-to-store transfer for localized demand, rebalancing approval workflow |
| PUR-017 | Supplier Quality & CAPA | Should Have | Quality issue logging at goods receipt, CAPA case creation, root cause analysis documentation, supplier corrective action tracking, quality hold process, quality metrics in vendor scorecard |
| PUR-018 | Indirect / Non-Merchandise Procurement | Must Have | Non-merchandise PO categories (supplies, services, IT, facilities), budget validation at PO creation, receipt confirmation by requester, separate GL account mapping |
| PUR-019 | Vendor Invoice Dispute & Discrepancy Resolution | Must Have | Dispute case creation (quantity, price, quality), 3-way match variance auto-flagging, dispute communication log, hold payment during dispute, resolution with debit memo or revised invoice |
| PUR-020 | Vendor Price Protection & Market Markdown Claims | Should Have | Price protection claim filing when vendor reduces wholesale price, markdown claim for unsold inventory at vendor-requested promo, claim documentation and approval, credit memo from vendor |
| PUR-021 | Vendor Strategic Collaboration & Joint Business Planning | Should Have | Annual JBP meeting documentation, joint growth targets, shared promotional calendar, JBP scorecard tracking, co-investment tracking (endcaps, flyers, digital) |
| PUR-022 | Private Label Factory Audit & Social Compliance | Should Have | Factory audit scheduling, social compliance checklist (labor, safety, environment), audit scoring, corrective action tracking, audit certificate management, approved factory list per supplier |
| PUR-023 | Supplier Diversity & MSME Development Program | Should Have | MSME vendor classification tracking, diversity spend reporting, MSME onboarding assistance, development program milestones, preferential payment terms for qualified MSMEs |
| PUR-024 | Product Quality Testing & Certification | Should Have | Quality test request at goods receipt, test result recording, certificate of compliance tracking, failed test disposition (return, destroy, discount), periodic quality audit per supplier |
| DOC-008 | Enterprise Document Retention & Archiving Policy | Must Have | Configurable retention periods per document type (BIR 7-year, HR 5-year, etc.), automated archive after retention trigger, legal hold capability, secure destruction with audit trail, retrieval from archive |
| MDM-008 | Vendor Master Data Governance | Must Have | Centralized vendor creation with approval workflow, TIN/banking validation, vendor classification (local/import/service/MSME), duplicate vendor detection, vendor master change audit trail |
| NFR-023 | Enterprise API & Integration Lifecycle Management | Should Have | API gateway for all external integrations (POS, ecommerce, banks, 3PL, government), API versioning, rate limiting, monitoring & alerting, integration health dashboard, API key management |
| NFR-024 | IT Asset Lifecycle Management | Should Have | IT hardware and software asset registry, procurement request integration, deployment tracking, maintenance scheduling, retirement/disposal workflow, license compliance tracking |
| NFR-025 | Employee IT Provisioning & Access Lifecycle | Must Have | Automated user account creation on hire, role-based access provisioning, access modification on transfer, full revocation on separation, access review audit trail |
| NFR-026 | Business Intelligence & Data Governance | Should Have | Centralized BI platform, data warehouse/lake integration, governed semantic layer, report certification process, data quality monitoring, self-service analytics with controlled publishing |
| NFR-027 | Omni-channel Customer Data Platform | Should Have | Unified customer profile across POS, ecommerce, loyalty, CRM, support tickets; identity resolution and deduplication; consent management per RA 10173; segment creation for marketing |
| RPT-011 | Category Performance Review & P&L Ownership | Should Have | Category-level P&L with gross margin, shrinkage, markdown, and promotional cost allocation; buyer/category manager scorecard; assortment performance vs. plan |
| RPT-012 | Pricing Hierarchy Governance & Compliance Audit | Should Have | Pricing rule validation across hierarchy (national → regional → store), promotional pricing compliance check, price override audit report, trade vs. retail price gap analysis |

---

## R15. Installation & Value-Added Services

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| SRV-001 | Installation & Value-Added Services Management | Should Have | Service order creation (installation, cutting, mixing), scheduling & resource allocation, service completion confirmation, service revenue recognition, service partner quality audit, service cost tracking |
| SRV-002 | DIY Workshop & In-Store Event Management | Should Have | Event scheduling, attendee registration, material cost tracking, event attendance reporting, post-event CSAT survey, event ROI analysis |

---

## R16. Wholesale & Reseller Operations

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| WSL-001 | Wholesale & Reseller Operations | Should Have | Wholesale customer onboarding with credit check, bulk order fulfillment with cross-dock option, wholesale-specific pricing tiers, pallet-level picking & shipping, wholesale invoice & settlement |
| WSL-002 | Trade Sales Pipeline & Territory Management | Should Have | Trade sales pipeline stages (lead → qualify → quote → negotiate → close), territory assignment, pipeline forecasting, sales rep performance tracking, trade counter / pro desk operations |

---

## R17. Corporate Governance, Legal & Strategy

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| GOV-001 | Corporate Governance & Legal Management | Should Have | Corporate secretarial management (board resolutions, SEC filings), legal case & litigation tracking, IP portfolio management, strategic planning & OKR tracking, enterprise project management lifecycle, SOP governance, legal contract review & approval |
| GOV-002 | Internal Audit & Risk Management | Should Have | Annual audit planning & risk assessment, operational audit execution (store/DC/HQ), enterprise risk management review, fraud investigation protocol, anti-bribery & corruption monitoring, external audit coordination |
| GOV-003 | Real Estate & Lease Management | Should Have | Site selection feasibility analysis, lease administration & renewal tracking, rent & CAM payment processing, real property tax (amillaramento) management per location |
| GOV-004 | Health, Safety & Environment Management | Should Have | OHS incident reporting & investigation, workplace safety inspection & audit scheduling, contractor safety orientation tracking, incident corrective action tracking, regulatory compliance reporting |
| GOV-005 | Engineering & Construction Management | Should Have | New store design & engineering standards management, construction bidding & contractor selection, construction supervision & quality control, store renovation/retrofitting project management, commissioning & operational handover |
| GOV-006 | Facility & Asset Maintenance (Non-Store) | Should Have | DC facility & warehouse equipment preventive maintenance, HQ office & executive asset maintenance, 3PL & logistics partner performance review, POA & board resolution lifecycle management |
| GOV-007 | Fleet Operations & Driver Management | Should Have | Route planning & dispatch optimization, driver performance & safety scoring, fuel management & consumption monitoring, fleet telematics & real-time tracking, fleet spare parts & preventive maintenance |
| GOV-008 | Sustainability & Environmental Compliance | Should Have | GHG emissions tracking per location, waste management & diversion reporting, social impact & community development tracking, sustainable sourcing & ethical vendor audit management, circular economy program management |
| GOV-009 | Innovation & Digital Transformation | Should Have | AI-driven personalization & recommendation engine, RPA lifecycle management, predictive maintenance for industrial assets, computer vision for inventory & planogram audit, retail analytics & AI-driven inventory optimization |
| GOV-010 | Marketing Campaign Management | Should Have | End-to-end campaign planning, execution & measurement; loyalty program financial governance; crisis communication & brand reputation management; social media & influencer management; PR & corporate communications; bank & credit card partnership management; retail media network operations; referral program & brand ambassador management; in-house creative production management; CSR impact measurement & reporting |
| GOV-011 | Business Continuity & Disaster Preparedness | Should Have | Business continuity drill scheduling & execution, DR testing & results documentation, BC plan maintenance, BIA (business impact analysis) updates, BC awareness training tracking |
| GOV-012 | Product Liability & Consumer Safety | Should Have | Consumer safety incident logging, regulatory notification workflow (FDA/DTI), product liability case management, recall coordination with vendors, corrective action tracking, incident trend analysis |
| GOV-013 | Anti-Bribery & Corruption Monitoring | Should Have | ABC risk assessment per vendor/transaction, gift & hospitality register, conflict of interest declaration, third-party due diligence, ABC training compliance tracking, whistleblower integration |
| GOV-014 | Competitor Intelligence & Market Monitoring | Should Have | Competitor price intelligence gathering workflow, market trend analysis, competitor store visit reporting, competitive benchmarking dashboards, intelligence dissemination to merchandising |
| GOV-015 | Private Label Development & Management | Should Have | Private label product development lifecycle, supplier qualification for PL, PL quality testing & certification, PL margin analysis, PL packaging & branding management, PL lifecycle & discontinuation |
| GOV-016 | Employee Training & Development | Should Have | Training needs assessment, training program creation & scheduling, attendance tracking, skills certification management, training effectiveness measurement, compliance training tracking (safety, hazmat, LP) |
| GOV-017 | Employee Performance & Career Development | Should Have | Performance review cycle management (goal setting, mid-year, year-end), competency framework, succession planning, internal mobility/job posting, management trainee program tracking, 360-degree feedback |
| GOV-018 | Store Performance Management | Should Have | Monthly store performance review with KPIs, store manager scorecard, store ranking/ benchmarking, improvement action plan tracking, store visit audit findings, planogram compliance verification |
| GOV-019 | Price Compliance & Energy Management (Store) | Should Have | Price tag/shelf label printing & verification audit, price compliance scoring per store, store energy & utility consumption monitoring, solar panel performance tracking (where installed), energy cost benchmarking |
| GOV-020 | Store-Level Security & Loss Prevention | Should Have | Store physical security & access control management, security camera (CCTV) audit & LP integration, store physical security & yard patrol routine, vending & concessionaire management, gift/home registry lifecycle |
| GOV-021 | Store-Level Reverse Logistics | Should Have | Store-to-DC reverse logistics consolidation, store renovation & remodel project management, store-level inventory receiving & putaway workflow standardization |
| GOV-022 | DC Inbound & Outbound Operations | Should Have | DC inbound delivery scheduling, DC outbound dispatch & load planning, cross-docking operations for fast-moving bulky items, fleet spare parts & preventive maintenance management |
| GOV-023 | Customer Experience Management | Should Have | Customer account reactivation workflow, customer feedback-to-action loop with NPS tracking, trade counter / pro desk operations standardization, omni-channel customer ticketing & support management |
| GOV-024 | Employee Financial Benefits Management | Should Have | Employee gratuity & retirement fund management per RA 7641, employee gratuity accrual & provision tracking, retirement eligibility monitoring, separation pay computation integration |
| GOV-025 | Sales Commission Management | Should Have | Sales commission calculation for trade & project sales, commission plan configuration (flat rate, tiered, quota-based), commission accrual & GL posting, commission payment via payroll, dispute resolution workflow |
| GOV-026 | Supply Chain Network Optimization | Should Have | Supply chain network optimization review, S&OP cycle management, international logistics & import operations, global supply chain incoterm & marine insurance tracking, inter-island logistics coordination |
| GOV-027 | 3PL & Delivery Partner Management | Should Have | 3PL/delivery partner onboarding & offboarding, 3PL SLA monitoring & performance review, delivery partner contract management, partner invoice verification & settlement |
| GOV-028 | Sample & Demo Inventory Management | Should Have | Sample/demo inventory tracking separate from saleable stock, sample issuance to stores, demo display lifecycle management, sample disposition (return, donate, destroy), sample inventory valuation exclusion |
| GOV-029 | Markdown & Clearance Pricing Management | Should Have | Markdown trigger rules (aging, season-end, discontinuation), clearance pricing approval workflow, markdown budget tracking, clearance performance reporting, markdown cost allocation to margin analysis |

---

## R18. Additional Cross-Functional Requirements

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| CRM-015 | Call Center Daily Operations & Queue Management | Should Have | Omnichannel queue management (phone, chat, email, social), IVR self-service, skill-based routing, callback queue, real-time agent monitoring, SLA tracking (80% calls < 60 sec), per-agent CSAT measurement |
| FIN-031 | BIR eFPS Filing & Electronic Payment Submission | Must Have | Automated tax return generation per BIR form specifications (2550M/Q, 1601-E, 1601-C, 1702Q/RT, 1604-C/E), eFPS submission integration, PRN generation, AAB payment integration, filing calendar with deadline alerts, multi-entity filing management |
| FIN-032 | E-Wallet & Digital Payment Settlement Reconciliation | Must Have | Settlement file import from GCash, Maya, GrabPay, ShopeePay; auto-matching settlement to POS/ecommerce transactions; MDR fee verification against contracted rates; per-store e-wallet reconciliation; chargeback dispute management; settlement aging tracking |
| MER-001 | Store Promotional Setup & Visual Merchandising Execution | Should Have | Promotional setup brief distribution (HQ to store), planogram compliance tracking with photo upload, promotional stock pick list generation, signage and shelf tag auto-generation, display teardown workflow, post-promotion sell-through summary |
| CRM-016 | Loyalty Member Enrollment & Onboarding Journey | Should Have | Multi-channel enrollment (in-store, online, call center, event), real-time deduplication during enrollment, RA 10173 consent management with granular opt-in, digital loyalty card generation, automated welcome communication sequence, enrollment-to-first-purchase conversion tracking |
| MER-002 | Seasonal Merchandise Transition & Display Rotation | Should Have | Seasonal assortment planning with store clustering, seasonal markdown trigger engine, seasonal setup brief with planogram distribution, display build and teardown workflow, in-season sell-through monitoring, post-season review and carry-forward analysis |
| NFR-028 | POS Terminal Hardware Maintenance & Peripheral Management | Should Have | POS hardware incident ticketing with priority matrix, remote diagnostics and remediation, spare peripheral inventory tracking per store, quarterly preventive maintenance scheduling, peripheral vendor warranty and RMA tracking, hardware failure analytics (MTBF, MTTR) |

---

*Document Version: 4.2 | Date: 2026-06-02 | 261 requirements across 18 categories (R1–R18). Removed duplicate GOV-030 (identical to GOV-008); clarified NFR-018 vs GOV-008 scope; renamed R18 section title*

