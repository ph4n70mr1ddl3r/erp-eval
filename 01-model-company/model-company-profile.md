# BuildRight Depot Corp. — Model Company Profile

> A theoretical hardware/DIY/home improvement big-box retail chain used as the reference
> model for ERP system design and architecture across different ERP platforms.

---

## 1. Company Overview

| Attribute | Detail |
|---|---|
| **Legal Name** | BuildRight Depot Corporation |
| **Trade Name** | BuildRight Depot |
| **Industry** | Retail — Hardware / DIY / Home Improvement (Big Box Format) |
| **Country** | Republic of the Philippines |
| **Corporate HQ** | Davao City, Philippines |
| **Year Founded** | Theoretical (assumed 15+ years in operation) |
| **Ownership** | Privately held, Filipino-owned family corporation |
| **Corporate Structure** | 5 legal entities under a holding company |
| **Store Format** | Big-box warehouse-style retail (8,000–15,000 sqm selling area) |
| **Tagline** | "Your Home Building Partner" |

---

## 2. Corporate Structure & Legal Entities

The company operates through **5 legal entities** organized as follows:

| Entity | Purpose | Registration |
|---|---|---|
| **BuildRight Holdings, Inc.** | Parent / holding company | SEC-registered, Davao City |
| **BuildRight Depot, Inc.** | Primary retail operations (stores & POS) | SEC-registered, Davao City |
| **BuildRight Logistics, Inc.** | Distribution, warehousing, and inbound freight | SEC-registered, Davao City |
| **BuildRight Digital Commerce, Inc.** | Ecommerce platform, BOPIS, digital channels | SEC-registered, Davao City |
| **BuildRight Property Management, Inc.** | Real estate leasing (store sites, DCs, offices) | SEC-registered, Davao City |

### Intercompany Relationships
- BuildRight Depot, Inc. leases store/distribution center sites from BuildRight Property Management, Inc.
- BuildRight Depot, Inc. pays warehousing/distribution fees to BuildRight Logistics, Inc.
- BuildRight Digital Commerce, Inc. fulfills orders through BuildRight Depot stores (for BOPIS) and BuildRight Logistics DCs (for delivery).
- All intercompany transactions must be settled at arm's-length transfer pricing.
- Consolidated financial reporting required for the group.

---

## 3. Physical Footprint

### 3.1 Retail Stores

| Parameter | Value |
|---|---|
| **Total Stores** | 200 |
| **Store Format** | Big-box warehouse (selling area: 8,000–15,000 sqm each) |
| **Total Selling Area** | ~1.6M – 3.0M sqm aggregate |
| **Store Staff** | ~30 employees per store |
| **Total Store-Level Headcount** | ~6,000 |

#### Store Location Distribution (Philippines)

| Region | No. of Stores | Notes |
|---|---|---|
| Mindanao | 60 | HQ region; highest density in Davao City (8 stores) |
| Visayas | 40 | Cebu, Iloilo, Bacolod hubs |
| Luzon (outside Metro Manila) | 50 | CALABARZON, Central Luzon, Bicol |
| Metro Manila | 30 | NCR concentration |
| North/Central Luzon | 20 | Expanding region |
| **Total** | **200** | |

#### Per-Store Layout Zones
- **Main Sales Floor**: Shelved merchandise, power aisles
- **Lumber & Building Materials Yard**: Outdoor/covered area
- **Tile & Flooring Gallery**: Display area
- **Appliance Section**: Appliances and fixtures
- **Tool & Hardware Wall**: Fasteners, hand tools, power tools
- **Paint Mixing Station**: Custom tinting
- **Checkout Area**: 3 POS terminals
- **Receiving/Backroom**: Inbound goods staging
- **Customer Service Counter**: Returns, special orders, BOPIS pickup

### 3.2 Distribution Centers (DCs)

| DC | Location | Size (sqm) | Role |
|---|---|---|---|
| **DC1 — Mindanao Hub** | Davao City (near HQ) | 25,000 | Primary DC; serves Mindanao stores |
| **DC2 — Visayas Hub** | Cebu (Mandaue) | 20,000 | Serves Visayas stores |
| **DC3 — South Luzon Hub** | Calamba, Laguna | 25,000 | Serves South Luzon & Metro Manila |
| **DC4 — North Luzon Hub** | Clark, Pampanga | 15,000 | Serves North/Central Luzon |

#### DC Operations
- Cross-dock capable for fast-moving items
- Full warehouse management (pick/pack/ship) for slower movers
- Vendor managed inventory (VMI) for select suppliers
- Each DC serves ~50 stores on average
- Replenishment cycles: 2–3x per week per store
- DC headcount: ~80–120 per DC (~400 total)
- Special handling areas: lumber, tiles, paint/chemicals

### 3.3 Corporate Headquarters

| Parameter | Value |
|---|---|
| **Location** | Davao City, Philippines |
| **Office Size** | ~3,000 sqm |
| **HQ Headcount** | ~250–300 |

#### HQ Departments
- **Executive Office**: CEO, CFO, COO, CIO, CMO
- **Merchandising & Buying**: Category managers, buyers, pricing analysts (~40)
- **Finance & Accounting**: GL, AP, AR, treasury, tax (~35)
- **Supply Chain & Logistics**: Planning, DC ops, fleet, procurement (~30)
- **Information Technology**: Infrastructure, applications, data, security (~25)
- **Human Resources**: Recruitment, compensation, training, payroll (~15)
- **Marketing**: Brand, promotions, ecommerce, digital (~20)
- **Store Operations**: Regional managers, operations standards (~20)
- **Legal & Compliance**: Corporate secretary, regulatory (~5)
- **Internal Audit**: (~5)
- **Customer Service / Call Center**: (~30)

---

## 4. Total Headcount

| Category | Count |
|---|---|
| Store Personnel | 6,000 (200 stores × 30) |
| Distribution Center Personnel | ~400 (4 DCs × ~100) |
| Corporate HQ Personnel | ~300 |
| **Total Company Headcount** | **~6,700** |

---

## 5. Point-of-Sale (POS) Operations

### Per-Store POS Details

| Parameter | Value |
|---|---|
| **POS Terminals per Store** | 3 |
| **Total POS Terminals (all stores)** | 600 |
| **Monthly Transactions per Store** | 10,000 |
| **Total Monthly Transactions (all stores)** | 2,000,000 |
| **Total Annual Transactions** | 24,000,000 |
| **Avg Lines per Transaction** | 4 |
| **Total Monthly Line Items** | 8,000,000 |
| **Total Annual Line Items** | 96,000,000 |

### Transaction Types at POS
- **Cash Sale** (~40%)
- **Credit/Debit Card** (~35%)
- **E-Wallet (GCash, Maya)** (~15%)
- **Corporate / Charge Account** (~5%)
- **BOPIS Pickup** (~3%)
- **Returns/Exchanges** (~2% return rate)

### POS Functional Requirements
- Offline capability (must continue selling during network outage)
- Barcode scanning (1D + 2D)
- Customer-facing display
- Receipt printing (thermal)
- Cash drawer management
- Age-restricted product prompts (solvents, cutting tools)
- Price override with manager authorization
- Loyalty points earning/redemption
- Multi-tender support (split payment across cash + card + e-wallet)
- Real-time inventory sync to central system
- Support for weight-based items (sold by kg: nails, screws in bulk)
- Support for cut-to-length items (lumber, pipes, wire)
- Support for paint mixing (custom SKU generation)

---

## 6. Product & Merchandise

### 6.1 SKU Portfolio

| Parameter | Value |
|---|---|
| **Active SKUs (at any time)** | 20,000 |
| **Total SKU Master (including seasonal/discontinued)** | ~35,000 |
| **SKU growth rate** | ~5–8% annually |

### 6.2 Product Categories & Approximate SKU Distribution

| Category | % of Active SKUs | ~SKU Count | Examples |
|---|---|---|---|
| **Lumber & Building Materials** | 15% | 3,000 | Plywood, cement, rebar, hollow blocks, lumber |
| **Tiles & Flooring** | 10% | 2,000 | Ceramic tiles, vinyl, granite, adhesives, grout |
| **Plumbing** | 12% | 2,400 | Pipes, fittings, faucets, toilets, water tanks |
| **Electrical** | 10% | 2,000 | Wires, switches, breakers, conduit, panels |
| **Paint & Finishes** | 8% | 1,600 | Interior/exterior paint, stains, varnishes, thinners |
| **Hand Tools** | 10% | 2,000 | Hammers, saws, screwdrivers, wrenches, pliers |
| **Power Tools** | 5% | 1,000 | Drills, grinders, saws, sanders, compressors |
| **Hardware & Fasteners** | 15% | 3,000 | Nails, screws, bolts, hinges, locks, padlocks |
| **Home Appliances** | 5% | 1,000 | Fans, aircons, water heaters, kitchen appliances |
| **Home Décor & Furniture** | 5% | 1,000 | Lighting fixtures, shelving, storage, blinds |
| **Garden & Outdoor** | 3% | 600 | Plants, pots, hoses, sprinklers, outdoor furniture |
| **Safety & PPE** | 2% | 400 | Hard hats, gloves, masks, goggles, harnesses |
| **Seasonal / Promo Items** | — | ~500 | Christmas lights, flood control items, etc. |

### 6.3 Inventory Valuation
- **Method**: Weighted Average Cost (WAC) — standard in Philippine retail
- **Physical Inventory**: Full wall-to-wall count annually; cycle counting weekly
- **Inventory Accuracy Target**: ≥ 97%

### 6.4 Item Types in ERP
| Item Type | Description | Examples |
|---|---|---|
| **Standard Stock** | Regular replenishment items | Cement, nails, paint, tools |
| **Seasonal Stock** | Seasonal procurement | Christmas décor, flood control items |
| **Consignment** | Owned by supplier until sold | Major appliances, select tiles |
| **Non-Stock / Special Order** | Ordered on demand for customer | Custom fixtures, bulk special orders |
| **Kit / Bundle** | Pre-packaged combo | Tool set, bathroom combo kit |
| **Service Item** | Labor/service charges | Paint mixing, pipe cutting, delivery fee |
| **Catch-Weight** | Sold by variable weight/length | Lumber (per board foot), wire (per meter), nails in bulk |

### 6.5 Supplier / Vendor Profile

| Parameter | Value |
|---|---|
| **Active Vendors** | ~800–1,000 |
| **Local (Philippine) Vendors** | ~600 (60%) |
| **International / Import Vendors** | ~400 (40%) — China, Taiwan, Indonesia, Malaysia, Japan, Europe |
| **Top 20 Vendors** | Account for ~45% of COGS |
| **Vendor-Managed Inventory (VMI)** | ~200 SKUs from 10 key vendors |
| **Monthly Trade Purchase Orders** | 1,000 |
| **Annual Purchase Orders** | 12,000 |

### 6.6 Purchasing Parameters
| Parameter | Value |
|---|---|
| **Lead Time (Local)** | 7–21 days |
| **Lead Time (Import)** | 45–90 days |
| **Reorder Point (ROP)** | Calculated per SKU based on avg daily demand × lead time + safety stock |
| **Safety Stock Policy** | 1–2 weeks of demand for A-items; 2–4 weeks for B-items; minimal for C-items |
| **ABC Classification** | A: top 20% SKUs = 80% revenue; B: next 30% = 15% revenue; C: bottom 50% = 5% revenue |
| **Purchase Order Average Lines** | ~15 lines per PO |
| **Monthly PO Lines** | ~15,000 |

---

## 7. Supply Chain & Logistics

### 7.1 Inbound Logistics (Vendor → DC)
- ~70% of goods flow through DCs first (stocking items)
- ~30% delivered direct-to-store (DSD) for bulky/fresh items (cement, lumber)
- Import containers: ~40–60 TEUs/month across all import vendors
- Customs brokerage managed in-house for imports
- Payment terms: typically 30–60 days for local; LC/TT for imports

### 7.2 Outbound Logistics (DC → Store)
- **Replenishment Frequency**: 2–3 deliveries per store per week
- **Fleet**: Mix of owned (20%) and third-party (80%) trucks
- **Vehicle Types**: 10-wheeler wing vans, 6-wheeler trucks, multi-drop routing
- **Delivery Lead Time**: 1–3 days from DC order to store receipt
- **Store Replenishment Orders**: ~3,000–4,000 per month (across all stores)

### 7.3 Store Receiving
- Each store receives 2–3 trucks per week
- Backroom inventory kept minimal (sell-from-shelf model)
- Goods Receipt processed on handheld/tablet at receiving dock
- Discrepancies flagged and resolved within 24 hours

### 7.4 Inter-DC Transfers
- Occasional rebalancing transfers between DCs (~20–30/month)
- Transfer orders initiated by supply planning team
- In-transit inventory visibility required

---

## 8. Ecommerce & Digital

### 8.1 Ecommerce Platform

| Parameter | Value |
|---|---|
| **Channel** | Web (responsive) + Mobile App (iOS & Android) |
| **URL** | buildright.com.ph (theoretical) |
| **Catalog** | Full 20,000 SKU catalog online |
| **Product Content** | Photos, specifications, dimensions, how-to guides |
| **Search & Navigation** | Category browse, keyword search, filter by specs |
| **Customer Accounts** | Optional registration; guest checkout available |
| **Payment Methods** | CC, GCash, Maya, bank transfer, COD |
| **Fulfillment Options** | BOPIS (store pickup), Home Delivery (from DC) |

### 8.2 BOPIS (Buy Online, Pick Up In Store)

| Parameter | Value |
|---|---|
| **Availability** | All 200 stores |
| **Process** | Customer places order online → store receives pick list → staff picks & stages → customer arrives with ID → release at customer service counter |
| **Pick SLA** | Ready within 4 hours of order placement |
| **Hold Period** | 5 days; auto-cancel and refund after |
| **% of Total Sales** | Target 3–5% within Year 1 |

### 8.3 Home Delivery

| Parameter | Value |
|---|---|
| **Fulfillment** | Shipped from nearest DC or store |
| **Coverage** | Metro areas initially; nationwide within 2 years |
| **Delivery Fee** | Based on weight/distance; free above PHP 5,000 |
| **Delivery Partners** | Third-party logistics (Lalamove, Transportify, own fleet for bulk) |
| **Lead Time** | 2–5 business days |

### 8.4 Ecommerce Integration Requirements
- Real-time inventory availability per store (aggregated)
- Real-time price sync (including ongoing promotions)
- Order push to store (BOPIS) or DC (delivery) for fulfillment
- Fulfillment status push back to ecommerce (tracking)
- Customer data sync to loyalty/CRM
- Returns initiated online; processed in-store
- Payment gateway integration (PayMongo, Dragonpay)

### 8.5 Projected Ecommerce Volume
| Parameter | Monthly Estimate |
|---|---|
| Orders (BOPIS) | ~3,000 |
| Orders (Delivery) | ~2,000 |
| Total Ecommerce Orders | ~5,000 |
| Average Order Value | PHP 3,500 |
| Ecommerce GMV | ~PHP 17.5M/month |

---

## 9. Customers & Sales

### 9.1 Customer Segments

| Segment | % of Revenue | Description |
|---|---|---|
| **Walk-in Retail (B2C)** | 55% | Individual homeowners, DIYers, small contractors |
| **Professional / Trade (B2B)** | 30% | Contractors, builders, interior designers, architects |
| **Corporate / Institutional (B2B)** | 10% | Developers, government projects, large enterprises |
| **Ecommerce** | 5% | Online B2C & B2B |

### 9.2 Customer Data
| Parameter | Value |
|---|---|
| **Registered Loyalty Members** | ~500,000 |
| **Trade Account Customers** | ~5,000 |
| **Corporate Account Customers** | ~200 |
| **Loyalty Program** | Points-based (1 point per PHP 100 spent); tiers: Bronze, Silver, Gold, Platinum |

### 9.3 Pricing Structure

| Price Type | Description |
|---|---|
| **Retail Price (SRP)** | Standard shelf price for walk-in customers |
| **Trade Price** | 5–15% discount for registered trade accounts |
| **Corporate / Project Price** | Negotiated contract pricing for large accounts |
| **Promotional Price** | Temporary markdowns (bi-monthly sale events) |
| **Bundle Price** | Discounted combo pricing for kits |
| **Quantity Break Price** | Tiered pricing per unit at POS (e.g., buy 10+ get 5% off) |

### 9.4 Estimated Revenue

| Parameter | Estimate |
|---|---|
| **Average Transaction Value (ATV)** | PHP 1,800 |
| **Monthly Transactions** | 2,000,000 |
| **Monthly Gross Revenue** | ~PHP 3.6 Billion |
| **Annual Gross Revenue** | ~PHP 43.2 Billion |
| **Average Gross Margin** | ~28–32% |
| **Annual COGS** | ~PHP 29–31 Billion |
| **EBITDA Margin** | ~10–12% |

> Note: Revenue figures are theoretical projections for a 200-store chain of this format.

---

## 10. Financial Operations

### 10.1 Accounting Requirements
- **Chart of Accounts**: Multi-entity shared COA with entity-specific segments
- **Accounting Standard**: PFRS (Philippine Financial Reporting Standards) / IFRS
- **Functional Currency**: PHP (Philippine Peso)
- **Tax**: VAT (12%), Withholding Tax, Percentage Tax, Local Business Tax
- **Fiscal Year**: January 1 – December 31
- **Consolidation**: Full consolidation of 5 entities with intercompany elimination

### 10.2 Accounts Payable

| Parameter | Value |
|---|---|
| **Monthly Vendor Invoices** | ~5,000–6,000 |
| **Payment Terms (Typical)** | Net 30, Net 60 |
| **Payment Methods** | Check, bank transfer, LC (imports) |
| **3-Way Match** | Required for all PO-based purchases (PO → GR → Invoice) |
| **Aging Monitoring** | Weekly AP aging review |

### 10.3 Accounts Receivable

| Parameter | Value |
|---|---|
| **AR Focus** | Trade & Corporate accounts only (retail is cash/card at POS) |
| **Active AR Accounts** | ~5,200 |
| **Credit Terms** | Net 30 for trade; Net 60–90 for corporate projects |
| **Credit Limit Policy** | Per-account limit with periodic review |
| **Collection** | Monthly statement; 30/60/90 aging follow-up |
| **Monthly AR Invoice Count** | ~3,000 |

### 10.4 Cash & Treasury
- **Bank Accounts**: BDO, BPI, Metrobank, Chinabank — multi-entity
- **Petty Cash**: Per store (PHP 20,000 float) and per DC (PHP 50,000 float)
- **Cash Management**: Daily cash deposit from stores; central treasury sweeps
- **Foreign Currency**: USD accounts for import payments
- **Capex Approval**: Tiered approval matrix (store manager up to board level)

### 10.5 Tax Compliance (Philippines)

| Tax Type | Frequency | Notes |
|---|---|---|
| **VAT (12%)** | Monthly + Quarterly | Input/output VAT; monthly VAT return (BIR Form 2550M) |
| **Withholding Tax (Expanded)** | Monthly | 1–10% on various vendor payments (BIR 1601-E) |
| **Withholding Tax (Compensation)** | Monthly | Employee withholding (BIR 1601-C) |
| **Percentage Tax** | Monthly | For entities below VAT threshold (if applicable) |
| **Income Tax (Corporate)** | Quarterly + Annual | BIR 1702Q / 1702RT |
| **Local Business Tax** | Annual / Quarterly | Paid to LGU where each store/DC operates |
| **Documentary Stamp Tax** | Per transaction | On loans, leases, certain documents |
| **PEZA/BOI Incentives** | If applicable | Possible tax holidays for specific operations |

---

## 11. Human Resources & Payroll

### 11.1 Organizational Structure

```
BuildRight Holdings, Inc.
├── CEO / President
│   ├── CFO — Finance, Accounting, Treasury
│   ├── COO — Store Operations, Supply Chain, DCs
│   ├── CIO — IT, Digital, Data
│   ├── CMO — Marketing, Ecommerce, Loyalty
│   ├── CHRO — HR, Org Development
│   └── VP Legal & Compliance
```

### 11.2 Payroll Parameters (Philippines)

| Parameter | Value |
|---|---|
| **Payroll Frequency** | Semi-monthly (15th and 30th) |
| **Total Employees** | ~6,700 |
| **Payroll Entities** | 5 (one per legal entity) |
| **Statutory Benefits** | SSS, PhilHealth, Pag-IBIG (HDMF) |
| **13th Month Pay** | Mandatory (1/12 of annual basic salary, paid by Dec 24) |
| **Overtime** | Per Philippine Labor Code (125%–200% premium) |
| **Night Differential** | 10% premium for 10 PM–6 AM work |
| **Holiday Pay** | Regular holiday (200%), Special non-working (130%) |
| **Minimum Wage** | Varies by region; follow DOLE-mandated rates |
| **Tax Table** | TRAIN law graduated tax table (BIR) |

### 11.3 Time & Attendance
- **System**: Biometric (fingerprint) + RFID badge per store/DC
- **Scheduling**: Shift-based for stores (2–3 shifts per day); flexible for HQ
- **Overtime Approval**: Manager pre-approval required
- **Leave Types**: VL, SL, Maternity (105 days expanded), Paternity (7 days), Solo Parent (7 days), Bereavement, etc.

### 11.4 Recruitment & Onboarding
- ~1,000–1,500 hires per year (including turnover replacement)
- Turnover rate: ~15–20% annually (retail industry standard)
- Onboarding includes POS training, safety orientation, product knowledge

---

## 12. Store Operations

### 12.1 Store Staffing Model (30 per store)

| Role | Count | Notes |
|---|---|---|
| Store Manager | 1 | Overall P&L responsibility |
| Assistant Store Manager | 1 | Operations and compliance |
| Department Supervisors | 4 | Lumber, Plumbing/Electrical, Tiles, Tools/Hardware |
| Sales Associates | 14 | Floor coverage, customer assistance |
| Cashiers | 4 | Covers 3 POS + 1 float/relief |
| Receiving Clerk | 2 | Inbound goods processing |
| Stockroom / Stock Associate | 2 | Replenishment, inventory counts |
| Customer Service Rep | 1 | Returns, BOPIS pickup, special orders |
| Maintenance / Utility | 1 | Store upkeep |

### 12.2 Store-Level Processes
- **Opening Procedures**: Cash float, system login, store walkthrough
- **Daily Operations**: Replenishment from backroom, price checks, customer service
- **Receiving**: Match PO → Delivery Receipt → Goods Receipt in system
- **Cycle Counting**: Daily count of assigned sections (~500 SKUs/day rolling)
- **Price Management**: Price changes applied centrally; RF guns for shelf label updates
- **Promotions**: Managed centrally by merchandising; auto-applied at POS
- **Returns**: Processed at customer service counter; restock or return-to-vendor
- **End-of-Day**: Z-report, cash count reconciliation, deposit preparation, system close
- **Loss Prevention**: CCTV, EAS tags on select high-value items, exception reporting

### 12.3 Store KPIs

| KPI | Target |
|---|---|
| Sales per Store per Month | PHP 18M |
| Sales per Sqm per Year | PHP 100,000 |
| Gross Margin % | 28–32% |
| Inventory Turns | 8–10x per year |
| Shrinkage / Loss | < 1.5% of sales |
| Customer Satisfaction Score | ≥ 85% |
| On-time Replenishment | ≥ 95% |

---

## 13. Merchandising & Category Management

### 13.1 Buying Team Structure
- **VP for Merchandising**
  - 5 Category Managers (each overseeing 2–3 product categories)
  - 10–12 Buyers
  - 3 Pricing Analysts
  - 2 Merchandise Planners

### 13.2 Seasonal Calendar (Philippines)

| Period | Event | Merchandise Focus |
|---|---|---|
| Jan–Feb | Post-holiday renovation | Paint, tiles, tools |
| Mar–Apr | Summer / dry season | Garden, outdoor, aircon, water tanks |
| May | School build-out | Paint, electrical, plumbing for schools |
| Jun–Aug | Rainy season prep | Waterproofing, flood control items, tarps |
| Sep–Oct | Ber-months home improvement | Holiday décor, home furniture, lighting |
| Nov–Dec | Christmas peak | Christmas lights, gift items, appliances |

### 13.3 Promotional Strategy
- **Bi-monthly Sale Events**: 6 major catalog-based promotions per year
- **Monthly Hot Deals**: 10–20 items on deep discount to drive foot traffic
- **Bundle Offers**: Contractor packages (e.g., bathroom complete set)
- **Loyalty Exclusive**: Double points weekends, member-only pricing
- **Clearance**: Seasonal items marked down at end-of-season
- **Vendor-Funded Promos**: Co-op advertising, vendor rebates

---

## 14. IT Infrastructure & Systems

### 14.1 Current State (Pre-ERP)
> Note: This describes the legacy landscape that the new ERP will replace/consolidate.

| System | Function | Pain Point |
|---|---|---|
| Legacy on-premise accounting | GL, AP, AR | Siloed per entity; no consolidation |
| Standalone POS software | In-store sales | Not integrated with inventory |
| Spreadsheet-based purchasing | PO creation | Manual, error-prone |
| Manual inventory counts | Stock management | No real-time visibility |
| Separate payroll software | HR/Payroll | Not linked to accounting |
| Custom ecommerce site | Online sales | No inventory sync |
| Email-based approvals | Capex, PO approvals | No audit trail |

### 14.2 Target ERP Requirements

| Functional Area | Key Requirements |
|---|---|
| **Financials** | Multi-entity GL, AP, AR, FA, consolidation, BIR-compliant tax |
| **Inventory Management** | Real-time perpetual inventory across all locations |
| **Procurement** | Automated PO generation, 3-way match, vendor portal |
| **Warehouse Management** | RF-directed putaway/pick, cycle count, lot/serial tracking |
| **POS / Retail** | 600 terminals, offline capable, multi-tender, loyalty integration |
| **Ecommerce** | BOPIS + delivery, real-time inventory & price sync |
| **Supply Chain Planning** | Demand forecasting, ROP/EOQ, replenishment planning |
| **HR & Payroll** | Philippine statutory compliance (SSS, PhilHealth, Pag-IBIG, BIR) |
| **CRM / Loyalty** | Customer management, points engine, trade accounts |
| **Analytics & BI** | Dashboards, sales analytics, inventory reports, P&L by store |
| **Intercompany** | Automated IC elimination, transfer pricing, settlement |
| **Approvals / Workflow** | Configurable approval matrix for PO, capex, discounts |
| **Mobile** | Store manager app, receiving app, executive dashboard |

### 14.3 Integration Requirements

| Integration | Direction | Protocol |
|---|---|---|
| POS ↔ ERP | Bidirectional | API / real-time |
| Ecommerce ↔ ERP | Bidirectional | REST API |
| Payment Gateway ↔ ERP | Inbound | Webhook / API |
| Bank ↔ ERP (Banking) | Bidirectional | File-based (BPI, BDO formats) / API |
| BIR eFPS ↔ ERP | Outbound | File-based (tax returns) |
| SSS / PhilHealth / Pag-IBIG ↔ ERP | Outbound | File-based (PRN, contribution tables) |
| Delivery Partners ↔ ERP | Bidirectional | API |
| Loyalty Engine ↔ ERP/POS | Bidirectional | API |
| WMS (RF Guns) ↔ ERP | Bidirectional | API / middleware |
| Supplier Portal ↔ ERP | Bidirectional | Web portal / EDI |

---

## 15. Data Volumes & Performance Requirements

### 15.1 Transactional Volumes

| Metric | Monthly | Annual |
|---|---|---|
| POS Transactions | 2,000,000 | 24,000,000 |
| POS Line Items | 8,000,000 | 96,000,000 |
| Purchase Orders | 1,000 | 12,000 |
| Purchase Order Lines | 15,000 | 180,000 |
| Store Replenishment Orders | ~3,500 | ~42,000 |
| Goods Receipts (Inbound) | ~4,500 | ~54,000 |
| Ecommerce Orders | ~5,000 | ~60,000 |
| AR Invoices | ~3,000 | ~36,000 |
| AP Invoices | ~5,500 | ~66,000 |
| Journal Entries (Auto) | ~10,000 | ~120,000 |
| Payroll Runs | 10 (5 entities × 2) | 120 |

### 15.2 Master Data

| Master | Records |
|---|---|
| Items / SKUs | 35,000 (20,000 active) |
| Customers (B2C Loyalty) | 500,000 |
| Customers (B2B Trade) | 5,000 |
| Customers (B2B Corporate) | 200 |
| Vendors / Suppliers | 1,000 |
| Locations (Stores + DCs + HQ) | 206 |
| Employees | 6,700 |
| Chart of Accounts | ~500–800 per entity |
| GL Accounts (consolidated) | ~2,000–3,000 |

### 15.3 Performance Requirements

| Requirement | Target |
|---|---|
| POS transaction processing | < 3 seconds per transaction |
| Inventory visibility (all stores) | Real-time (< 30 sec delay) |
| Report generation (standard) | < 30 seconds |
| Month-end close | Within 5 working days |
| System uptime (POS) | 99.9% |
| System uptime (back office) | 99.5% |
| Concurrent users (peak) | ~800–1,000 |
| Data retention | 7 years (BIR requirement) |

---

## 16. Compliance & Regulatory (Philippines)

| Regulation | Impact on ERP |
|---|---|
| **BIR Revenue Regulations** | Registered POS, e-invoicing readiness, CAS (Computerized Accounting System) registration |
| **BIR Form Requirements** | 2550M/Q (VAT), 1601-E (EWT), 1601-C (CWT), 1702Q/RT (Income Tax), 1604-C/E (Annual) |
| **SEC Financial Reporting** | PFRS/IFRS compliant FS, consolidated reporting |
| **DOLE Labor Standards** | Payroll compliance, leave tracking, 13th month |
| **SSS / PhilHealth / Pag-IBIG** | Monthly contribution remittance, PRN generation |
| **Local Government Unit (LGU)** | Business permits per location, local business tax |
| **Consumer Act (RA 7394)** | Price tag display, return policy |
| **Data Privacy Act (RA 10173)** | NPC compliance, customer data handling, consent management |
| **Build-Operate-Transfer (BOT)** | If any government project sales |
| **Customs / Tariff** | Import duty calculations, customs brokerage integration |
| **Anti-Red Tape Authority (ARTA)** | Business permit renewal compliance |
|**Bangko Sentral ng Pilipinas (BSP)**| Foreign exchange, cross-border payments |

---

## 17. Critical Success Factors for ERP Implementation

1. **Multi-entity, multi-location readiness** out of the box
2. **Philippine localization**: BIR, SSS, PhilHealth, Pag-IBIG compliance
3. **High-volume POS**: 2M transactions/month across 600 terminals
4. **Real-time inventory visibility** across 200 stores + 4 DCs
5. **Ecommerce integration**: Seamless BOPIS + delivery fulfillment
6. **Scalability**: From 200 to potentially 300+ stores
7. **Offline POS resilience**: Stores must sell during outages
8. **Intercompany automation**: 5-entity consolidation
9. **Supply chain optimization**: Demand planning, auto-replenishment
10. **User adoption**: ~6,700 users across varying tech literacy levels

---

## 18. Glossary

| Term | Definition |
|---|---|
| **ATV** | Average Transaction Value |
| **BOPIS** | Buy Online, Pick Up In Store |
| **COA** | Chart of Accounts |
| **DC** | Distribution Center |
| **DSD** | Direct Store Delivery |
| **EOQ** | Economic Order Quantity |
| **GMV** | Gross Merchandise Value |
| **IC** | Intercompany |
| **LGU** | Local Government Unit |
| **POS** | Point of Sale |
| **ROP** | Reorder Point |
| **SKU** | Stock Keeping Unit |
| **SRP** | Suggested Retail Price |
| **TEU** | Twenty-foot Equivalent Unit (shipping container) |
| **VMI** | Vendor Managed Inventory |
| **WAC** | Weighted Average Cost |
| **WMS** | Warehouse Management System |

---

*Document Version: 1.0 | Date: 2026-05-29 | Status: Initial Draft*
