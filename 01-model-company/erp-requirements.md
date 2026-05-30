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

## R2. Inventory Management

| Req ID | Requirement | Priority | Notes |
|---|---|---|---|
| INV-001 | Perpetual Inventory (all locations) | Must Have | 200 stores + 5 DCs + HQ |
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
| POS-001 | 1,000 POS Terminals | Must Have | 5 per store × 200 stores |
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
| POS-014 | Promotional Pricing Auto-Apply | Must Have | No cashier intervention needed |
| POS-015 | Gift Card / Store Credit | Should Have | Issuance and redemption |
| POS-016 | Catch-Weight / Variable Measure at POS | Must Have | Weight-based (kg) and cut-to-length (m, board ft) selling — critical for lumber, wire, bulk nails |
| POS-017 | Paint Mixing / Custom SKU at POS | Must Have | Generate custom SKU for tinted paint; link to base paint + colorant inventory |
| POS-018 | Age-Restricted Product Prompts | Should Have | Mandatory prompt for solvents, cutting tools, etc.; requires cashier confirmation |

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
| NFR-005 | Concurrent Users | 1,000–1,500 |
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

---

*Document Version: 1.3 | Date: 2026-05-30 | Removed NFR-016 (technical detail); reworded NFR-011/012 to be business-level; removed deployment model prescriptions*
