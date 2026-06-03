# Inventory Management Workflows

> Replenishment, cycle counting, transfers, consignment, physical inventory, backorders, promo stock allocation, damaged & defective goods disposition, inventory adjustment & shrinkage authorization, multi-channel inventory allocation governance, inter-store/inter-DC stock rebalancing, quarantine & recertification, and SLOB provisioning & liquidation.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W4. Store Replenishment (DC → Store)](#store-replenishment-dc-→-store)
- [W4B. Store-Initiated Replenishment Request](#store-initiated-replenishment-request)
- [W6. Cycle Counting & Inventory Accuracy](#cycle-counting-inventory-accuracy)
- [W22. Stock Transfers (Store-to-Store & Inter-DC)](#stock-transfers-store-to-store-inter-dc)
- [W22A. Store-Level Outbound Transfer Fulfillment](#store-level-outbound-transfer-fulfillment)
- [W22B. Store-to-DC Return (Excess / Damaged Inventory)](#store-to-dc-return-excess--damaged-inventory)
- [W23. Consignment Inventory Operations](#consignment-inventory-operations)
- [W42. Annual Physical Inventory Execution](#annual-physical-inventory-execution)
- [W56. Customer Backorder Management](#customer-backorder-management)
- [W57. Promotional Stock Allocation & Pre-Positioning](#promotional-stock-allocation-pre-positioning)
- [W91. Damaged & Defective Goods Disposition](#damaged-defective-goods-disposition)
- [W92. Inventory Adjustment & Shrinkage Authorization](#inventory-adjustment-shrinkage-authorization)
- [W105. Multi-Channel Inventory Allocation & Priority Governance](#multi-channel-inventory-allocation--priority-governance)
- [W154. Proactive Store Inventory Rebalancing (Stock Push)](#proactive-store-inventory-rebalancing-stock-push)
- [W204. Regional Stock Rebalancing & Inter-Store Expedited Transfers](#regional-stock-rebalancing--inter-store-expedited-transfers)
- [W214. Store-to-Store Expedited Transfers (Customer-Initiated)](#store-to-store-expedited-transfers-customer-initiated)
- [W218. Inter-DC Stock Rebalancing (Stock Push)](#inter-dc-stock-rebalancing-stock-push)
- [W219. Store Inventory Quarantine & Recertification](#store-inventory-quarantine--recertification)
- [W220. Slow-Moving & Obsolete Inventory (SLOB) Provisioning & Liquidation](#slow-moving--obsolete-inventory-slob-provisioning--liquidation)

---

## W4. Store Replenishment (DC → Store)

| Field | Detail |
|---|---|
| **Trigger** | System generates replenishment suggestion based on min/max or demand forecast |
| **Frequency** | 2–3 physical deliveries per store per week; ~5,000 replenishment orders/month total (each delivery truck carries 2–3 orders consolidated for that store) |
| **Volume** | ~167 orders/day across all DCs (~33 per DC/day); avg ~50 lines per order |
| **Owner** | Supply Planner |
| **Participants** | Supply Planner, DC Pick/Pack/Ship team, Truck Driver, Store Receiving Clerk, Store Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System calculates replenishment needs per store: current stock vs. min/max or forecast | System | — | Automated (nightly) |
| 2 | Supply Planner reviews suggested orders each morning; adjusts for promotions, seasonality, store-specific factors | Supply Planner | Supply Planning Manager | 2–3 hours/day |
| 3 | Planner confirms orders; system groups into waves by DC and delivery route | Supply Planner | Supply Planning Manager | 1 hour/day |
| 4 | DC receives pick wave; WMS assigns pick tasks to staff by zone | WMS / DC Supervisor | DC Supervisor | 5 min (assignment) |
| 5 | Pickers pick items from bins per RF gun direction; scan-confirm each item | Picker | DC Supervisor | 2–4 hours/wave |
| 6 | Packers pack into store-labeled totes/cases; scan-confirm shipment | Packer | DC Supervisor | 1–2 hours/wave |
| 7 | Load truck per route sequence (multi-drop) | Loading Crew | DC Supervisor | 30–60 min |
| 8 | System creates Transfer Order; in-transit inventory created | System | — | Automated |
| 9 | Truck departs DC; ETA communicated to store | Driver | DC Dispatch | — |
| 10 | Store Receiving Clerk unloads truck; scans each item/case against Transfer Order | Receiving Clerk (Store) | Store Manager | 30–60 min |
| 11 | Discrepancies (shortage, damage) flagged in system; DC notified | Receiving Clerk (Store) | Store Manager | 5 min if any |
| 12 | Store confirms receipt; in-transit inventory becomes store inventory | Receiving Clerk (Store) | Store Manager | 5 min |
| 13 | Replenishment moved to sales floor or backroom stock | Stock Associate | Department Supervisor | 30–60 min |

**Total cycle time**: 1–3 days from order creation to store shelf

### System Touchpoints
- Dual-sourced item management: for SKUs that are replenished through both DC delivery (W4) and DSD (W18) — typically cement, lumber, and bulky building materials — system maintains a primary/secondary supply channel indicator per SKU per store; ATP calculation aggregates on-hand + incoming DC replenishment + incoming DSD orders; when auto-replenishment (W4.1) generates a transfer order for a dual-sourced SKU, system checks if a DSD delivery is already scheduled within the replenishment lead time and adjusts the transfer order quantity accordingly to avoid overstocking; Store Manager can override the default supply channel per SKU via handheld; monthly: Supply Planner reviews dual-sourced SKU inventory levels to identify overstocking or conflicting deliveries (W4, W18)
- Replenishment calculation engine (min/max, forecast-based) (W4.1)
- Constrained allocation rules: when available supply is insufficient for all stores, system applies configurable allocation logic (e.g., equal distribution, rank by store revenue, prioritize A-stores) — Planner reviews and adjusts before confirming (W4.2)
- Store order creation and wave planning (W4.3)
- WMS pick/pack/ship with RF scanning (W4.4–6)
- In-transit inventory visibility (W4.8)
- Store receiving with discrepancy handling (W4.10–12)
- Real-time inventory update at both DC and store (W4.8, W4.12)
- FEFO (First Expired First Out) directed picking: for items with shelf-life tracking (paint, adhesives, chemicals, cement), WMS directs pickers to pick the earliest-expiring batch first; system sequences pick tasks by expiry date within the same SKU; ensures fresher stock remains in DC for later dispatch (W4.5)
- Inventory ownership clarification: goods moving from DC to store in W4 are Depot Inc. inventory at both locations; DC facilities are operated by Logistics Inc. (which charges monthly warehousing/distribution fees per W14), but Depot Inc. owns the merchandise throughout; W4 transfer orders are intra-entity inventory movements (no per-TO IC invoice); IC invoicing applies only to inter-entity goods transfers (W22) or service fees (W14)
- New store demand ramp-up (first 90 days): for newly opened stores (W16), auto-replenishment parameters (ROP, safety stock, min/max) derived from comparable store averages may not reflect actual local demand patterns during the ramp-up period; during the first 90 days post-opening, Supply Planner overrides auto-replenishment with manual review — (a) system flags all replenishment orders for new stores with "Ramp-Up" status requiring Planner confirmation (no auto-release), (b) Planner reviews suggested orders daily against early sell-through data and adjusts quantities based on actual demand velocity observed in the first weeks, (c) Store Manager provides daily feedback on fast-moving and slow-moving items via the W4B store-initiated replenishment request channel, (d) after 90 days, Demand Planner analyzes accumulated sales data to calculate store-specific ROP/safety stock parameters per W31.8; system transitions the store from "Ramp-Up" to standard auto-replenishment; parameters reviewed again at 180 days; this manual override period prevents both overstocking (tying up working capital in a new store) and stockouts (damaging customer first impressions)
- Constrained allocation rule governance: when available supply is insufficient for all stores, system applies configurable allocation logic; Supply Planning Manager defines allocation method per SKU or category (equal distribution, rank by store revenue, prioritize A-stores, proportional to historical demand); allocation rules reviewed and approved by VP Supply Chain; rule changes logged with old method, new method, reason, approver, and effective date; monthly: Supply Planning Manager reviews allocation fairness dashboard showing per-store fill rate and allocation share; fairness disputes escalated by Store Managers through W4B channel feed into allocation rule review; quarterly: allocation methodology reviewed as part of W31.8 parameter governance cycle (W4.2)

### W4B. Store-Initiated Replenishment Request

| Field | Detail |
|---|---|
| **Trigger** | Store Manager or Department Supervisor identifies local demand that exceeds current replenishment plan (e.g., nearby construction project, local event, weather-driven spike) |
| **Frequency** | ~100–200 store-initiated requests/month chain-wide; ~0.5–1 per store per month |
| **Volume** | Typically 5–20 SKUs per request |
| **Owner** | Supply Planner |
| **Participants** | Store Manager / Dept. Supervisor, Supply Planner, Buyer (if new PO needed) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Store Manager or Dept. Supervisor identifies items needing additional stock beyond automated replenishment; opens replenishment request in system (handheld or terminal) — selects SKUs, enters requested quantity, urgency (routine / expedited / emergency), and business justification (e.g., "new subdivision project starting 2 km away") | Store Manager / Dept. Supervisor | Store Manager | 10 min |
| 2 | System checks: (a) current on-hand at store, (b) current on-hand at serving DC, (c) open POs and incoming replenishment orders, (d) ATP at DC after existing commitments; presents Supply Planner with a dashboard showing the request alongside existing supply position | System | — | Automated |
| 3 | Supply Planner reviews request each morning alongside standard replenishment review (W4 step 2); evaluates: (a) is the demand legitimate and near-term, (b) does DC have available stock to fulfill without depriving other stores, (c) if expedited — can it ride on the next wave, or does it need a separate shipment | Supply Planner | Supply Planning Manager | 5–10 min/request |
| 4 | **If approved — DC has stock**: Supply Planner adds requested quantities to the next replenishment order for that store (W4 step 2); system creates a pick task in the next wave; request status updated to "Approved — Scheduled" | Supply Planner | Supply Planning Manager | 2 min |
| 5 | **If approved — DC has insufficient stock**: Supply Planner requests Buyer to expedite a PO (W2A) or arrange an inter-DC transfer (W22); request status updated to "Approved — Pending Supply"; Supply Planner tracks until supply arrives | Supply Planner / Buyer | Supply Planning Manager | 10 min |
| 6 | **If denied**: Supply Planner rejects request with reason (insufficient DC stock, lower priority than other stores, demand not validated); system notifies Store Manager; Store Manager may escalate to Regional Manager if disagreement | Supply Planner | Supply Planning Manager | 2 min |
| 7 | Fulfillment follows standard W4 pick/pack/ship process; request closed when goods received at store | Per W4 | — | Per W4 |
| 8 | Weekly: Supply Planning Manager reviews store-initiated request report — approval rate, top requesting stores, frequently requested items; flags items with high ad-hoc request frequency for ROP/safety stock adjustment per W31.8 | Supply Planning Manager | VP Supply Chain | 30 min/week |

### System Touchpoints
- Store-initiated replenishment request form in POS/terminal/handheld with SKU selection, quantity, urgency, and justification fields (W4B.1)
- Supply Planner dashboard showing request alongside current supply position (on-hand, ATP, open POs, pending replenishment) (W4B.2)
- Request status lifecycle: Submitted → Under Review → Approved (Scheduled / Pending Supply) / Denied → Fulfilled / Closed (W4B.3–7)
- Weekly request analytics: approval rate, requesting stores, frequently requested items feeding into ROP parameter review (W31.8) (W4B.8)
- Integration with W4 (replenishment order creation), W2A (expedited PO), W22 (inter-DC transfer), W31 (forecast and ROP adjustment)

### Staffing Implication
- **Supply Planner**: ~100–200 requests/month ÷ 20 working days = ~5–10/day. At ~10 min each for review = ~1 hour/day incremental. Absorbed within existing 2–3 planner team.
- **Store Managers**: ~0.5–1 requests/month × 10 min = negligible.

### Staffing Implication (W4 overall)
- **2–3 Supply Planners** (in HQ): ~167 orders/day to review. At 2–3 hours/day for review + 1 hour for wave management = 3–4 hours/day. 2–3 planners share this plus demand forecasting. Reasonable within the 30-person Supply Chain team.
- **Per DC**: 15–20 Pickers, 8–10 Packers, 4–6 Loading Crew (working in shifts to handle ~33 orders/day with ~50 lines each). Fits within ~150 DC headcount.

---



---

## W6. Cycle Counting & Inventory Accuracy

| Field | Detail |
|---|---|
| **Trigger** | Daily schedule (rolling through all sections) |
| **Frequency** | Daily per store; each SKU counted at least once per quarter |
| **Volume** | ~700 SKUs/day per store; 200 stores × 700 = 140,000 SKU counts/day chain-wide |
| **Owner** | Department Supervisor |
| **Participants** | Stock Associate (counter), Department Supervisor (reviewer), Store Manager (approver for adjustments) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates daily count assignment by section/aisle | System | — | Automated (nightly) |
| 2 | Stock Associate retrieves count sheet on handheld/RF device | Stock Associate | Department Supervisor | — |
| 3 | Physically count each SKU in assigned section; enter quantity into device (3 Stock Associates each count ~233 SKUs/day, taking ~40 min each at ~10 sec/SKU) | Stock Associate | Department Supervisor | ~40 min per associate |
| 4 | System compares physical count to system count; flags variances | System | — | Automated |
| 5 | For flagged items: Stock Associate recounts (blind recount) | Stock Associate | Department Supervisor | 15–30 min |
| 6 | If variance confirmed: Department Supervisor reviews and approves adjustment | Dept. Supervisor | Store Manager | 15 min |
| 7 | If adjustment > PHP 10,000 or > 5% of SKU value: Store Manager approval required | Store Manager | Store Manager | 5 min each |
| 8 | System posts inventory adjustment; audit trail recorded | System | — | Automated |
| 8a | **In-store damage discovered during operations**: Stock Associate identifies damaged item on sales floor (customer drop, water damage, forklift damage, yard weather damage); creates damage report in system with photo and cause code; Department Supervisor reviews and approves disposition: (a) markdown and sell at reduced price, (b) scrap with supervisor authorization, (c) Return to Vendor per W3.6a process; system posts inventory adjustment and loss to damage/scrapping account | Stock Associate / Dept. Supervisor | Store Manager | 10 min |
| 9 | Root cause analysis for recurring variances (theft, damage, receiving errors) | Dept. Supervisor | Store Manager | Weekly review |

**Cycle**: 35,000 SKUs ÷ 700/day = 50 working days per full cycle (~10 weeks ≈ quarterly)

### System Touchpoints
- Automated count assignment by zone/section (W6.1)
- RF device / handheld count entry (W6.3)
- Variance detection and blind recount workflow (W6.4–5)
- Inventory adjustment with tiered approval (W6.6–7)
- Immutable audit trail for all adjustments (W6.8)
- In-store damage discovery reporting with photo, cause code, and disposition workflow (W6.8a)
- Near-expiry alerting: during cycle counts, system flags items approaching expiry (configurable threshold per category, e.g., 90 days for paint, 60 days for cement); Department Supervisor reviews flagged items and initiates disposition per W13.9a (markdown), W3.6a (RTV), or W13.9b (scrap/liquidation) (W6)
- Negative inventory resolution: system generates daily negative inventory alert listing all SKU-locations where on-hand < 0; at store level, Stock Associate investigates root cause (timing lag from offline POS transactions per W5G, receiving error, mispick, or cycle count needed); at DC level, Inventory Control clerk investigates (pending GR posting, allocation error, picking error); resolution action depends on cause — recount and adjust (W6), wait for pending transaction posting, or force adjustment with supervisor approval; system blocks negative-inventory locations from ecommerce ATP availability until resolved; monthly report of negative inventory frequency by location feeds into inventory accuracy improvement initiatives

### Staffing Implication
- **3 Stock Associates per store**: Each counts ~233 SKUs/day (~40 min), with remainder of time on replenishment, receiving, damage reporting, and BOPIS picking. Current count of 3 is adequate but has no slack for absenteeism.

---



---

## W22. Stock Transfers (Store-to-Store & Inter-DC)

| Field | Detail |
|---|---|
| **Trigger** | Stock imbalance between locations; emergency need; inter-DC rebalancing |
| **Frequency** | ~30–40 inter-DC transfers/month; ~50–80 store-to-store transfers/month |
| **Volume** | Variable (typically 5–20 lines per transfer) |
| **Owner** | Supply Planner (inter-DC); Store Manager (store-to-store) |
| **Participants** | Supply Planner, Store Manager, Receiving Clerk, Stock Associate, DC Picker |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Requestor identifies transfer need (stock-out risk, excess inventory, rebalancing) | Supply Planner / Store Manager | Supply Planning Mgr / Regional Mgr | 10 min |
| 2 | Requestor creates Transfer Order in system: source location, destination, items, quantities | Requestor | — | 10 min |
| 3 | System checks availability at source location; confirms or flags shortage | System | — | Automated |
| 4 | Approval: inter-DC → Supply Planning Manager; store-to-store → Regional Manager | Approver | Approver | 10 min |
| 5 | Source location picks items (DC: WMS pick; Store: Stock Associate picks from shelf) | Picker / Stock Associate | DC Supervisor / Store Manager | 15–60 min |
| 6 | Items packed and shipped; system creates in-transit inventory | Shipper / Driver | DC Supervisor / Store Manager | 15–30 min |
| 7 | Destination location receives items; scans against Transfer Order | Receiving Clerk | DC Supervisor / Store Manager | 15–30 min |
| 8 | System updates: source inventory decreases, in-transit clears, destination inventory increases | System | — | Automated |
| 9 | If discrepancy at destination: flag in system; source location notified for investigation | Receiving Clerk | DC Supervisor / Store Manager | 5 min if any |
9a | Transfer discrepancy resolution: (a) if source picking error confirmed → source location absorbs loss (system posts inventory adjustment at source, Dr. Inventory Loss / Cr. Inventory at source location); (b) if carrier damage → DC Supervisor or Store Manager files carrier damage claim with photos and delivery receipt notation per W3.6a insurance claim process; (c) if unexplained shortage after investigation → destination writes off with approval per tier (Store Manager ≤ PHP 10,000, DC Manager ≤ PHP 50,000, Controller > PHP 50,000); system posts adjustment at destination (Dr. Inventory Loss / Cr. Inventory) | Receiving Clerk / DC Supervisor / Store Manager | Controller | 15–30 min

### W22A. Store-Level Outbound Transfer Fulfillment

When a store is the source location for a store-to-store transfer (W22 step 5), the picking, packing, and dispatch process differs from DC operations (no WMS). The following details the store-level outbound process:

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Store Manager or Dept. Supervisor receives transfer pick list on handheld/terminal from approved Transfer Order | Stock Associate | Dept. Supervisor | 2 min |
| 2 | Stock Associate picks items from sales floor or backroom per pick list; scan-confirms each item using handheld barcode scanner; system validates scanned SKU and quantity against Transfer Order | Stock Associate | Dept. Supervisor | 15–45 min |
| 3 | If item not found or short: Stock Associate enters actual quantity picked; system updates Transfer Order with partial quantity and notifies destination store | Stock Associate | Dept. Supervisor | 2 min |
| 4 | Stock Associate packs items in available shipping cartons or bags; labels each package with destination store name, Transfer Order number, and item count | Stock Associate | Dept. Supervisor | 10–20 min |
| 5 | **Dispatch options**: (a) **DC truck backhaul** (preferred): items ride on the next DC delivery truck returning from this store — Stock Associate stages packed items at receiving dock for driver pickup; (b) **Own fleet or 3PL**: if urgent or no DC truck scheduled within 2 days, Fleet Manager or DC Dispatch arranges separate pickup; (c) **Inter-store courier**: for same-city transfers, Store Manager may arrange direct courier delivery | Stock Associate / Driver | Store Manager | 5–10 min staging |
| 6 | Driver or carrier confirms pickup by scanning transfer shipment barcode on handheld; system updates Transfer Order status to "Shipped" and creates in-transit inventory | Driver / Carrier | Store Manager | 5 min |
| 7 | System deducts picked items from source store inventory at shipment confirmation | System | — | Automated | |

**Transfer lead time**: Inter-DC: 3–7 days; Store-to-Store: 1–3 days (same city) or 3–5 days (inter-region)

### System Touchpoints
- Transfer Order creation with source/destination (W22.2)
- Real-time availability check at source (W22.3)
- Approval workflow (W22.4)
- In-transit inventory tracking (W22.6)
- Receiving against Transfer Order (W22.7)
- Inventory update at both locations (W22.8)
- Discrepancy handling with financial resolution: source error, carrier damage, or unexplained loss disposition (W22.9a)
- Intercompany model — see W14 for full dual IC framework (service-based vs. goods-based); standard DC→Store replenishment (W4) is NOT an inter-entity transfer — Depot Inc. owns goods at both locations; Logistics Inc. provides warehousing services billed monthly per W14, not per-transfer
- Customer-initiated inter-store transfer: when a customer at Store A requests an item out of stock, Sales Associate checks real-time inventory at nearby stores via handheld or terminal; if available, Associate creates customer transfer request (item, quantity, source store, destination store, customer contact); Store Manager at destination approves; source Store Manager or system auto-confirms if within same region; system creates Transfer Order per W22; source store picks and ships; destination store receives and notifies customer via SMS/app; sale booked at destination store when customer purchases; transport cost absorbed by company as customer service (no charge to customer); real-time cross-store inventory lookup available to Sales Associates via handheld/terminal and to customers via website/app store selector
- Catch-weight / variable-measure items during transfers: for catch-weight items (lumber, wire, bulk nails), source location measures and records actual length/weight/piece count on Transfer Order; destination location re-measures upon receipt; if quantity differs from TO, variance handled per W22.9a with measurement tolerance applied (e.g., ±2% for lumber, ±1% for wire by length); within tolerance: system accepts destination measurement and posts variance as inventory adjustment at source; outside tolerance: source location investigates (measurement error, transit damage); system supports dual-entry measurement capture for catch-weight items on both outbound and inbound transfer processing

### W22B. Store-to-DC Return (Excess / Damaged Inventory)

| Field | Detail |
|---|---|
| **Trigger** | Store identifies excess inventory beyond replenishment needs, damaged items requiring DC inspection/disposition, or items recalled/discontinued requiring central processing |
| **Frequency** | ~100–200 store-to-DC returns/month chain-wide; ~0.5–1 per store per month |
| **Volume** | Typically 5–15 lines per return shipment |
| **Owner** | Store Manager (initiation); DC Supervisor (receiving) |
| **Participants** | Store Manager, Stock Associate, Supply Planner, DC Receiving Clerk, DC Supervisor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Store Manager or Dept. Supervisor identifies items for return to DC: (a) excess stock — on-hand significantly above max and unlikely to sell before expiry/obsolescence, (b) damaged items — store-damaged goods requiring central disposition (W6.8a), (c) discontinued/recalled items — per W29 or W68 (product discontinuation), (d) vendor-RTV consolidation — items staged for vendor return that are more efficiently processed through DC | Store Manager / Dept. Supervisor | Store Manager | 15 min |
| 2 | Store Manager creates Store-to-DC Return Order in system: select items, quantities, return reason code (excess / damaged / discontinued / RTV consolidation); system validates that items originated from DC (not DSD-only items that should be returned directly to vendor) | Store Manager | — | 10 min |
| 3 | Supply Planner reviews return request: for excess items, confirms DC has demand or storage capacity to absorb returned stock; for damaged items, auto-approved; system routes for approval | Supply Planner | Supply Planning Manager | 5 min/return |
| 4 | Stock Associate picks and packs items for return shipment; scan-confirms each item against Return Order; stages at store receiving area for DC truck pickup | Stock Associate | Dept. Supervisor | 30–60 min |
| 5 | Items shipped on next available DC delivery truck (reverse logistics — truck returns to DC with return shipment); system creates in-transit inventory | Driver / Stock Associate | DC Supervisor | Per W4 schedule |
| 6 | DC Receiving Clerk receives returned items; scans against Return Order; inspects condition | DC Receiving Clerk | DC Supervisor | 15–30 min |
| 7 | **Disposition by return reason**: (a) excess — system returns items to DC saleable inventory at current WAC; (b) damaged — DC Supervisor inspects and decides disposition per W6.8a (markdown, scrap, RTV); (c) discontinued — system routes to clearance/liquidation holding area per W13.9a or W68; (d) RTV consolidation — Buyer coordinates with vendor per W3.6b | DC Receiving Clerk / DC Supervisor / Buyer | DC Manager | 15–30 min |
| 8 | System updates: store inventory decreases, in-transit clears, DC inventory increases (for resalable items) or posts to appropriate disposition account (for damaged/scrap/RTV) | System | — | Automated |
| 9 | Monthly: Supply Planner reviews store-to-DC return report: frequency by store, reason, and category; flags stores with high return frequency for root cause analysis (ordering discipline, receiving quality, demand planning accuracy) | Supply Planner | Supply Planning Manager | 30 min/month |

### System Touchpoints (Store-to-DC Return)
- Store-to-DC Return Order creation with reason codes (excess, damaged, discontinued, RTV consolidation) (W22B.2)
- Supply Planner approval workflow with DC capacity/demand check (W22B.3)
- In-transit inventory tracking for reverse movement (W22B.5)
- Disposition routing based on return reason code with integration to W6.8a (damage), W13.9a (clearance), W3.6b (RTV) (W22B.7)
- Store-to-DC return analytics: frequency, reason, category, store (W22B.9)
- Integration with W4 (reverse logistics on delivery truck), W6 (damage reporting), W13 (clearance), W22 (standard transfers), W29 (recall), W68 (discontinuation)

### Staffing Implication
- **Store Manager**: ~0.5–1 return initiations/month × 25 min = ~15 min/month. Absorbed.
- **Supply Planner**: 5 min review per return × ~200/month = ~17 hours/month across all stores. Absorbed by existing planner team.
- **DC Receiving**: adds ~15–30 min per return shipment to existing receiving workload. With ~100–200/month ÷ 5 DCs = ~20–40/DC/month. Manageable.

### Staffing Implication (W22 overall)
- Inter-DC transfers are part of Supply Planner's existing duties (within the 30-person Supply Chain team).
- Store-to-store transfers are managed by Store Managers with Regional Manager approval — absorbed into existing roles.

---



---

## W23. Consignment Inventory Operations

| Field | Detail |
|---|---|
| **Trigger** | Consignment goods received at store/DC; or consignment goods sold |
| **Frequency** | ~15–25 consignment vendors; settlement monthly |
| **Volume** | ~500–1,000 consignment SKUs (primarily appliances, select tiles, fixtures) |
| **Owner** | Buyer (consignment agreements) |
| **Participants** | Buyer, Receiving Clerk, Cashier, AP Clerk, Consignment Vendor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Buyer establishes consignment agreement: vendor, SKUs, consignment price, settlement terms | Buyer | Category Manager | Per vendor setup |
| 2 | System flags consignment items in item master with vendor ownership indicator | Merchandise Planner | Buyer | 5 min/SKU |
| 3 | Vendor delivers consignment goods; Receiving Clerk processes GR (standard receiving) | Receiving Clerk | Dept. Supervisor | Per W3/W18 |
| 4 | System records consignment receipt as non-valuated inventory (vendor-owned) | System | — | Automated |
| 5 | Consignment items displayed and sold on sales floor; POS scans barcode normally | Cashier | — | Part of sale |
| 6 | At sale: system records sell-through event; ownership transfers from vendor to company to customer; system posts GL entries: Dr. Cost of Goods Sold / Cr. Consignment Vendor Payable (at consignment cost); simultaneously Dr. Cash or Accounts Receivable / Cr. Revenue (at selling price) | System | — | Automated |
| 6a | At month-end close (W9): system accrues consignment liability for all consignment goods sold but not yet settled with vendor; Finance reconciles consignment payable sub-ledger to GL | System / Cost Accountant | Controller | Automated + 30 min/month |
| 7 | Monthly: system generates consignment sell-through report per vendor (units sold × consignment price) | System | Buyer | Automated |
| 8 | Buyer reviews and confirms settlement report | Buyer | Category Manager | 1 hour/vendor/month |
| 9 | AP Clerk processes consignment vendor payment based on confirmed sell-through; system generates AP invoice from sell-through data: Dr. Consignment Vendor Payable / Cr. Cash (settles the accrued liability from step 6) | AP Clerk | AP Supervisor | Per W7 |
| 10 | Quarterly: Buyer reviews consignment SKU performance; identifies slow movers for return to vendor; coordinates physical pickup with vendor (vendor arranges collection or Buyer schedules transport); Receiving Clerk processes return shipment in system (reduces non-valuated consignment inventory; no GL posting since goods remain vendor-owned throughout); vendor confirms received quantities and issues updated consignment stock list; system updates consignment on-hand quantities | Buyer / Receiving Clerk | Category Manager | 2 hours/quarter |

### System Touchpoints
- Consignment item flagging in item master (W23.2)
- Non-valuated inventory receipt and tracking (W23.4)
- Ownership transfer at point of sale with automatic GL posting (Dr. COGS / Cr. Consignment Payable) (W23.6)
- Period-end accrual for sold-but-unsettled consignment goods (W23.6a)
- Consignment payable sub-ledger reconciliation to GL (W23.6a)
- Consignment sell-through report generation (W23.7)
- AP settlement from sell-through data with GL posting (Dr. Consignment Payable / Cr. Cash) (W23.9)
- Consignment return logistics: return shipment processing with non-valuated inventory reduction (no GL impact); vendor confirmation and updated stock list; on-hand quantity adjustment (W23.10)
- Quarterly consignment vendor statement reconciliation: Cost Accountant generates consignment reconciliation report per vendor — compares BuildRight's recorded consignment sell-through (units sold × consignment cost) to vendor's statement; reconciles on-hand quantities (system record vs. vendor record of goods shipped minus goods sold); investigates discrepancies (unrecorded sell-through, unreported returns, missing receipts, timing gaps); reconciling items documented and resolved within 15 business days; unreconciled differences > PHP 50,000 escalated to Controller; results feed into vendor scorecard (W44) (W23)

### Staffing Implication
- Consignment management adds ~15–25 hours/month to Buyer workload (review + settlement). Spread across 10–12 buyers handling their respective vendor portfolios, this is ~2 hours/buyer/month. Absorbed within existing headcount.

---



---

## W42. Annual Physical Inventory Execution

| Field | Detail |
|---|---|
| **Trigger** | Year-end close calendar (typically December 31 or last business day of fiscal year) |
| **Frequency** | Annual; each store and DC counted once per year |
| **Volume** | 35,000 SKUs × 205 locations (200 stores + 5 DCs); executed in coordinated 3–5 day window per region |
| **Owner** | Cost Accountant (overall); Store Manager (per store); DC Manager (per DC) |
| **Participants** | Cost Accountant, Store Managers, DC Managers, all store staff, inventory count teams, IT, Internal Audit |

### Pre-Count Planning (2–3 weeks before count)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Cost Accountant issues physical inventory instructions: count dates, methodology, team assignments, system freeze schedule | Cost Accountant | Controller | 4 hours |
| 2 | IT configures count sheets in system: generate zone-based count sheets per location with expected system quantities (hidden for blind count) | IT Team | Cost Accountant | 1 day |
| 3 | Store Managers organize count teams: assign zones (8 zones per store), designate team leaders, schedule shifts for 2-day count | Store Manager | Store Ops Director | 2 hours/store |
| 4 | Store Managers ensure all receiving and shipments are posted before count; process pending transactions; stage goods in correct locations | Store Manager | Store Ops Director | 4 hours/store |
| 5 | Internal Audit prepares to observe counts at selected locations (sample: 20–30 stores + all DCs) | Internal Audit | CFO | 1 week |

### Count Execution (Day 1 — full count; Days 2–3 — recounts and adjustments; Days 4–5 — residual clean-up if needed)

> **Feasibility note**: Counting 35,000 SKUs per store with 30 staff in 2 days is infeasible for a full wall-to-wall count. BuildRight addresses this with a **tiered counting strategy**: (a) **A/B items** (~10,500 SKUs, 95% of inventory value) receive full physical count during the annual window; (b) **C items** (~24,500 SKUs) are validated by extrapolating from rolling cycle counts (W6) conducted throughout the year — the annual process confirms that cycle count accuracy for C-items meets the ≥ 97% threshold, rather than recounting every C-item. This reduces the per-store counting burden to ~10,500 SKUs ÷ 30 staff ÷ 2 days = ~175 SKUs/person/day, achievable at ~3 min/SKU including travel between locations. DCs, with higher item density and forklift-access racking, allocate 3–5 days for a full count of all SKUs.
>
> **C-item extrapolation methodology**: C-item inventory accuracy is validated using a statistical sampling approach — (a) throughout the year, W6 cycle counts cover all C-item SKUs at least once per quarter (per the quarterly cycle in W6); (b) each C-item's cycle count accuracy (physical vs. system quantity) is recorded per count event; (c) at year-end, Cost Accountant computes the aggregate C-item accuracy rate = (total C-item SKU-locations where physical matched system within tolerance) ÷ (total C-item SKU-locations counted during the year); (d) if aggregate accuracy ≥ 97%, C-items are considered validated and no additional count is required at year-end; (e) if aggregate accuracy < 97%, Cost Accountant identifies the worst-performing C-item categories (by variance rate) and adds them to the annual count scope; (f) sample size for interim confidence: to achieve 95% confidence that the true accuracy rate is within ±1% of the observed rate, a minimum of ~500 C-item SKU-locations must be cycle-counted per quarter per store (approximately 2% of C-item SKU-locations, achievable within W6 daily count volume of ~700 SKUs/day); (g) this methodology is reviewed and approved by Internal Audit annually as part of the W42 physical inventory observation; (h) **below-threshold contingency**: if aggregate C-item accuracy falls below 97%, Cost Accountant quantifies the gap and identifies worst-performing C-item categories by variance rate; additional items added to the annual count scope in priority order (highest-variance categories counted first); if additional scope threatens the 2-day count window, Cost Accountant escalates to Controller with a proposed extended count schedule (up to 5 days with staggered zone freezing per W42 system freeze mitigation); Controller approves or denies extension; if extension denied, Cost Accountant counts the highest-risk C-items within the standard window and accepts a qualified inventory opinion for the remaining C-items — Controller discloses the qualification in the year-end close package (W9B); Internal Audit documents the below-threshold outcome and includes it in the W42 observation report.

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 6 | System freezes inventory transactions at count locations (no sales, receiving, or transfers during count window) | System / IT | Cost Accountant | Automated |
| 7 | Count teams physically count every SKU in assigned zone: two-person teams (one counts, one records on RF device/count sheet) | Count Teams | Team Leader | 6–10 hours/location |
| 8 | Team leaders submit zone counts; system compares to system quantities (blind count — system quantity only revealed after team submits) | Team Leader | Store Manager | Per zone |
| 9 | System generates variance report per zone: items where physical count differs from system count | System | — | Automated |
| 10 | For items with variance: recount team (different from original) performs blind recount | Recount Team | Store Manager | 2–4 hours/location |
| 11 | If recount confirms variance: Team Leader investigates and documents root cause (theft, damage, receiving error, data entry error) | Team Leader | Store Manager | 15 min/item |
| 12 | Store Manager reviews and approves adjustments per tier: (a) adjustment ≤ PHP 10,000: Store Manager, (b) adjustment PHP 10,001–100,000: Regional Manager, (c) adjustment > PHP 100,000: Controller | Approver | Approver | 5–15 min/adjustment |
| 13 | Internal Audit observes counts at sampled locations; validates methodology compliance and count accuracy | Internal Audit | CFO | Full count day |
| 14 | System posts approved inventory adjustments; updates inventory valuation; posts to GL (gain/loss on inventory) | System | — | Automated |

### Post-Count (1 week after)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 15 | System unfreezes inventory transactions; normal operations resume | IT Team | Cost Accountant | Automated |
| 16 | Cost Accountant reconciles total inventory valuation post-adjustment to GL inventory accounts | Cost Accountant | Controller | 4 hours |
| 17 | Cost Accountant generates physical inventory summary report: total adjustments by location, by category, by variance type (gain/loss), shrinkage as % of sales | Cost Accountant | Controller | 2 hours |
| 18 | Controller and CFO review physical inventory results; identify high-shrinkage locations for loss prevention action (W37) | Controller | CFO | 2 hours |
| 19 | Internal Audit issues observation report with recommendations for count process improvement | Internal Audit | CFO | 1 week |

### System Touchpoints
- System inventory transaction freeze per location (W42.6, W42.15); auto-replenishment orders for frozen stores are automatically queued by the system and released upon unfreeze — no replenishment orders are lost during the count window; queued orders visible on Supply Planner dashboard with "Pending — Store Count Freeze" status
- Zone-based count sheet generation with blind count mode (W42.2, W42.7–8)
- RF device / handheld count entry (W42.7)
- Variance detection after count submission (W42.9)
- Recount tracking (W42.10)
- Adjustment approval workflow with tiered authorization (W42.12)
- Bulk inventory adjustment posting and GL impact (W42.14)
- Vendor-owned inventory (consignment/VMI) during physical count: count teams count consignment (W23) and VMI (W20) items using separate count sheets flagged as "Vendor-Owned — Non-Valuated"; system records vendor-owned counts separately from BuildRight-owned (valuated) inventory; after count, system reconciles physical count of vendor-owned items to vendor's expected quantities per W23/W20 records; discrepancies investigated — if physical < system, potential unrecorded sell-through requiring W20/W23 settlement adjustment; if physical > system, potential unrecorded receipt requiring investigation; vendor-owned count results shared with respective vendors for reconciliation; Internal Audit (W42 step 13) verifies that all counted items are correctly classified as owned (valuated) or vendor-owned (non-valuated) for audit evidence (W42.7–8)
- Physical inventory summary reporting (W42.17)
- System freeze mitigation: to minimize operational disruption during the counting window, system supports **staggered zone freezing** as an alternative to full-location freeze — (a) stores may remain open during count using zone-by-zone freeze: zone being counted is frozen for transactions (no sales, receiving, or transfers for items in that zone); remaining zones continue normal operations; as each zone's count is submitted, system unfreezes that zone; full count completed over 2 days with rotating zone freezes; (b) for DCs: system supports module-by-module freeze (e.g., count inbound module while outbound module continues shipping); critical outbound shipments for same-day delivery commitments are prioritized before the freeze window; (c) if full-location freeze is required (smaller stores or DCs with high inventory interdependency): system freeze window is minimized to non-business hours where possible (overnight freeze with count starting at close of business; completed before next day opening); IT monitors system performance during zone freeze/unfreeze cycles to ensure no transaction loss; Store Manager communicates freeze zones to staff in real-time via handheld notifications (W42)
- Continuous counting alternative for high-volume stores: for the top 20 stores by revenue (where even a 2-day partial disruption is significant), the annual wall-to-wall count may be replaced by a **perpetual inventory validation** program — system generates weekly count tasks covering 1/52 of all SKUs per week (completing a full cycle in 1 year, overlapping with W6 cycle counts); Cost Accountant validates perpetual counts quarterly and Internal Audit observes the process semi-annually; this alternative requires Controller approval and is only available for stores with demonstrated ≥ 98% cycle count accuracy over the prior 12 months (W42)

### Staffing Implication
- **All store staff (30/store)**: Mobilized for 2-day count. Stores may close early or operate with skeleton crew during count.
- **DC staff (~150/DC)**: Full DC count requires 1–2 days. Operations paused during count.
- **Cost Accountant**: 20–30 hours for planning, execution support, and reconciliation. Heaviest workload of the year for this role.
- **Internal Audit (3–5 auditors)**: Travel to sampled locations. Absorbed within annual audit plan.
- **IT**: 1 day for count sheet configuration + system freeze/unfreeze support.

---



---

## W56. Customer Backorder Management

| Field | Detail |
|---|---|
| **Trigger** | Customer requests an item that is out of stock at the store and/or DC level |
| **Frequency** | ~2,000–3,000 backorder requests/month (primarily B2B trade accounts) |
| **Volume** | Concentrated in fast-moving commodity categories (cement, lumber, paint, plumbing fittings, electrical wire) during peak construction season |
| **Owner** | Sales Associate (intake); Supply Planner (fulfillment) |
| **Participants** | Sales Associate, Supply Planner, Buyer, Store Manager, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer requests out-of-stock item at store or via Sales Rep; Sales Associate checks real-time inventory across all locations (stores + DCs) via handheld | Sales Associate | Dept. Supervisor | 3 min |
| 2 | If available at another store: offer customer-initiated inter-store transfer per W22 (customer-initiated transfer) | Sales Associate | Store Manager | 5 min |
| 3 | If unavailable chain-wide or customer prefers to wait: Sales Associate creates backorder in system — item, quantity, customer details (loyalty account or trade account), preferred store for pickup, delivery preference, maximum wait time (customer-stated) | Sales Associate | Dept. Supervisor | 5 min |
| 4 | System links backorder to next expected replenishment: (a) if PO already in progress (W2) with expected GR date — system shows estimated availability date, (b) if no PO exists — system flags to Supply Planner for PO creation (W2A), (c) if import item — shows import PO ETA (W2B) | System | — | Automated |
| 5 | System reserves backorder quantity against incoming PO or replenishment order (allocates to backorder before general store replenishment); backorder takes priority over routine replenishment allocation | System | — | Automated |
| 6 | Sales Associate communicates estimated availability date to customer; for trade/corporate accounts, Sales Rep manages the communication | Sales Associate / Sales Rep | — | 2 min |
| 7 | When goods are received at DC and backorder allocation is fulfilled: system routes allocated quantity to the customer's preferred store in the next replenishment wave (W4); or if customer prefers delivery, system creates home delivery order (W19) | System | Supply Planner | Automated |
| 8 | System sends customer notification (SMS/email/app): "Your item is on the way to [Store Name], expected availability [date]" | System | — | Automated |
| 9 | Item arrives at store; Stock Associate stages for customer pickup (similar to BOPIS W11); system sends "Ready for pickup" notification | Stock Associate / System | Store Manager | 5 min + automated |
| 10 | Customer picks up item; sale processed at POS (standard transaction or trade account per W5B.4c); backorder closed in system | Cashier / Customer | — | 5 min |
| 11 | If customer cancels backorder before fulfillment: Sales Associate cancels in system; allocation released back to general inventory | Sales Associate | Dept. Supervisor | 2 min |
| 12 | If backorder exceeds customer-stated maximum wait time: system auto-notifies customer with options to (a) extend wait, (b) accept substitute item, or (c) cancel; if no response in 7 days, system auto-cancels and releases allocation | System | — | Automated |
| 13 | Weekly: Supply Planner reviews open backorder aging report: items with no incoming PO (step 4b — no supply planned), long-wait backorders (> 14 days), and backorders at risk of cancellation; escalates to Buyer for expedited procurement | Supply Planner | Supply Planning Manager | 1 hour/week |

### System Touchpoints
- Real-time inventory visibility across all locations with cross-store lookup (W56.1)
- Backorder creation linked to customer account (loyalty or trade) with estimated availability (W56.3–4)
- Allocation reservation against incoming PO/replenishment with backorder priority (W56.5)
- Automated customer notification at each status change: created, allocated, in transit, ready for pickup (W56.8–9)
- Backorder aging report with escalation triggers (W56.13)
- Backorder price protection: if a promotional price (W13) or regular price reduction (W40) becomes effective between backorder creation and fulfillment, system automatically applies the lower price to the backorder at fulfillment (customer-friendly policy); system logs the price adjustment with original backorder price, new lower price, and price source (promo or price change); if price increases, the original backorder price is honored (locked at creation); this rule applies to both trade account and retail backorders
- Auto-cancellation after maximum wait time with customer notification (W56.12)
- Integration with W2 (PO creation trigger), W4 (replenishment allocation), W13 (promotional pricing — backorder price protection), W19 (home delivery option), W22 (inter-store transfer alternative), W38 (special order for non-stock items — backorder is for stock items, special order is for non-stock items), W68 (product discontinuation — system auto-cancels open backorders for discontinued SKUs and notifies customers)

### Staffing Implication
- **Sales Associates**: ~2,000–3,000 backorders/month ÷ 200 stores = ~10–15/store/month × ~10 min each = ~2 hours/store/month. Absorbed.
- **Supply Planner**: 1 hour/week for backorder review. Absorbed within existing planning duties.

---



---

## W57. Promotional Stock Allocation & Pre-Positioning

| Field | Detail |
|---|---|
| **Trigger** | Promotional event confirmed (W13 step 3 — VP Merchandising approves promo pricing) |
| **Frequency** | 6 major bi-monthly promos/year + 12 monthly hot deal cycles |
| **Volume** | 200–500 SKUs per major promo; stock pre-positioned to 200 stores over 1–2 weeks before event |
| **Owner** | Supply Planner |
| **Participants** | Supply Planner, Category Manager, DC Supervisor, Store Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | After promo approval (W13 step 3), Category Manager provides Supply Planner with promo SKU list, expected demand lift (historical lift % × baseline forecast), and maximum shelf capacity per store | Category Manager | VP Merchandising | 2 hours/promo |
| 2 | Supply Planner calculates promotional stock requirement per SKU per store: (base weekly demand × promo lift factor × promo duration weeks) + safety buffer (10–20%) − current store inventory − already-in-transit inventory | Supply Planner | Supply Planning Manager | 2–4 hours/promo |
| 3 | Supply Planner checks DC inventory for promo items; identifies shortfalls; requests Buyer to expedite POs for items with insufficient DC stock to cover promotional allocation (may use air freight for imports if lead time is critical) | Supply Planner / Buyer | Category Manager | 1 hour/promo |
| 4 | System generates promotional replenishment orders per store with "Promo" priority flag; these orders are prioritized ahead of routine replenishment in the pick wave (W4 step 3) | System | Supply Planner | Automated |
| 5 | DC picks and ships promotional stock to stores in waves over 1–2 weeks before promo start date; stores in each region scheduled to receive promo stock 3–5 days before event | DC Team | DC Supervisor | Per W4 |
| 6 | Store Receiving Clerk receives promo stock; Stock Associate stages in backroom or designated promo display area (not commingled with regular shelf stock to preserve promo allocation integrity) | Receiving Clerk / Stock Associate | Store Manager | Per W4 |
| 7 | System tracks promotional stock allocation vs. actual receipt per store; flags stores that have not received their full allocation 2 days before promo start | System | Supply Planner | Automated |
| 8 | During promo: system reports promo stock sell-through daily per store; Supply Planner monitors for stores selling faster than expected and arranges emergency replenishment from DC or transfers from slower-selling stores (W22) | Supply Planner | Supply Planning Manager | 30 min/day during promo |
| 9 | After promo: remaining promo stock disposition per W13.9a (clearance) or return to regular shelf inventory if sell-through ≥ 90% | Pricing Analyst / Stock Associate | Category Manager | Per W13 |

### System Touchpoints
- Promotional demand lift calculation tool integrated with forecast engine (W31) and historical promo performance data (W57.2)
- Promotional replenishment order generation with priority flag and promo allocation tracking (W57.4)
- Promotional stock allocation dashboard: planned vs. shipped vs. received per store (W57.7)
- Promotional sell-through dashboard: real-time sales velocity during promo period with store-level drill-down (W57.8)
- Integration with W2 (expedited POs), W4 (replenishment waves), W13 (promo pricing and clearance), W22 (emergency inter-store transfers), W31 (demand forecast)

### Staffing Implication
- **Supply Planner**: adds ~4–6 hours per major promo event for allocation planning + 30 min/day monitoring during the promo. With 6 major events/year, this is ~30–40 hours/year of incremental planning work, concentrated in the 2 weeks before each event. Absorbed within existing Supply Chain team.
- **DC Team**: promotional pre-positioning adds temporary surge to pick/pack/ship volume in the 1–2 weeks before each event. Managed with shift scheduling adjustments (W34).

---



## W91. Damaged & Defective Goods Disposition

| Field | Detail |
|---|---|
| **Trigger** | Damaged or defective goods identified during receiving (W3, W18), cycle counting (W6), daily operations (W5), or customer return (W12) |
| **Frequency** | ~500–800 damaged/defective units/month across all locations |
| **Volume** | ~15–25 per store per month; ~50–100 per DC per month |
| **Owner** | Store Manager (store-level); DC Supervisor (DC-level) |
| **Participants** | Store Manager, DC Supervisor, Stock Associate, Receiving Clerk, Buyer, Category Manager, Controller |

### Background

Damaged and defective goods are an inevitable part of retail operations — items damaged in transit (DC→Store or vendor→DC), in-store handling damage, customer-caused damage on display items, vendor manufacturing defects, and age-related deterioration (paint expiry, adhesive hardening). While W88 (Return to Vendor) handles the vendor-liability path and W92 (Inventory Adjustment) handles the accounting authorization, this workflow governs the physical identification, documentation, and disposition decision-making for damaged/defective goods regardless of liability. It fills the gap between discovering damaged inventory and the final resolution.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Identification and documentation**: (a) Store Associate, Stock Associate, or Receiving Clerk discovers damaged/defective item; (b) scans item barcode and selects damage type: (i) transit damage (DC→Store or vendor→DC/Store), (ii) in-store handling damage (dropped, shelving collapse, water damage), (iii) customer-caused damage (opened package, broken seal on display), (iv) vendor manufacturing defect (functional failure, missing parts, cosmetic defect out of box), (v) age/expiry deterioration (expired paint, hardened adhesive, rusted hardware), (vi) environmental damage (flood, typhoon — W49); (c) takes photo of damage; (d) system creates damage report with timestamp, location, item, quantity, damage type, and photo evidence | Stock Associate / Receiving Clerk | Dept. Supervisor / DC Supervisor | 5 min/item |
| 2 | **Quarantine and physical segregation**: System moves damaged items to "Damaged/Defective" inventory status (unavailable for sale, unavailable for replenishment calculation); physical items moved to designated damaged goods area in store backroom or DC quarantine zone | Stock Associate / Receiving Clerk | Store Manager / DC Supervisor | 5 min/item |
| 3 | **Liability assessment**: (a) **Vendor liability** — damage type is vendor defect, transit damage from vendor, or wrong item received: route to W88 (Return to Vendor) for vendor credit or replacement; (b) **Carrier liability** — damage type is transit damage from DC to store or 3PL delivery to customer: route to carrier claim (W19.12b for ecommerce, W66 for inter-island, W52 for fleet); (c) **BuildRight liability** — in-store handling damage, customer-caused damage, environmental damage: no external recovery possible; proceed to disposition decision; (d) **Undetermined** — route to Buyer for vendor negotiation or DC Supervisor for carrier investigation | Dept. Supervisor / DC Supervisor | Store Manager / DC Supervisor | 5 min/item |
| 4 | **Disposition decision** (BuildRight-liability items only — vendor/carrier items follow W88 or carrier claim): (a) **Markdown and sell at discount** — item is cosmetically damaged but functionally usable (e.g., dented can of paint, scratched tile, box-damaged appliance); system routes to W93 (Markdown & Clearance) for discounted sale; (b) **Donate** — item is functional but not saleable at any price (e.g., display model replaced by newer version); coordinate with CSR for community donation program; requires Controller approval; (c) **Scrap/dispose** — item is non-functional, hazardous (paint/chemical per W82), or broken beyond any use; system routes to disposal with proper documentation; (d) **Return to regular stock** — item was incorrectly flagged (e.g., packaging scuff but product perfect); system reverses damage status | Dept. Supervisor / Store Manager / DC Supervisor | Store Manager / DC Supervisor | 5 min/item |
| 5 | **DC-level consolidation**: DC Supervisor consolidates damaged/defective items from DC operations and items returned from stores (via W22B store-to-DC return); sorts by vendor for potential consolidated RTV shipment per W88; disposes of scrap items in bulk per W82 (hazardous materials) or general waste protocols | DC Supervisor | Supply Chain Manager | 1 hour/week |
| 6 | **Financial impact recording**: System calculates damage/defective value at WAC per item; records in damage/defective register: total value by damage type, by location, by category; feeds into shrinkage report per W37 (loss prevention) and W92 (inventory adjustment) | System | Controller | Automated |
| 7 | **Monthly damage analysis**: Category Manager and Controller review monthly damage/defective report: (a) damage rate by category (target: < 0.5% of inventory value), (b) damage rate by location (flag stores > 1% rate), (c) damage rate by damage type (trend analysis), (d) top 20 items by damage frequency (possible packaging improvement or vendor quality issue), (e) vendor defect rate feeds into W44 vendor scorecard; (f) transit damage rate by carrier feeds into W52/W62B carrier performance | Category Manager / Controller | VP Merchandising / CFO | 1 hour/month |

### System Touchpoints
- Damage report creation with barcode scan, damage type classification, and photo evidence (W91.1)
- Inventory status change to "Damaged/Defective" (blocked from sale and allocation) (W91.2)
- Liability assessment routing: W88 (vendor), carrier claim, or BuildRight (W91.3)
- Disposition decision workflow: markdown (W93), donate, scrap/dispose, or reinstate (W91.4)
- Damage/defective register with value tracking by type, location, category (W91.6)
- Monthly damage analysis dashboard with rate tracking and trend analysis (W91.7)
- Integration with W3 (DC receiving — transit damage from vendor), W4 (DC→Store transit damage), W6 (cycle count — discovered damage), W12 (customer returns — damaged items), W18 (DSD — transit damage), W22 (transfers — in-transit damage), W37 (loss prevention — damage as shrinkage component), W44 (vendor scorecard — vendor defect rate), W52/W62B (carrier performance — transit damage rate), W66 (inter-island — transit damage), W82 (hazardous waste disposal), W88 (RTV — vendor liability path), W92 (inventory adjustment — accounting authorization), W93 (markdown — sellable damaged goods)

### Staffing Implication
- **Store Associates / Stock Associates**: ~15–25 damaged items/store/month × 10 min each = ~2.5–4 hours/store/month. Absorbed.
- **DC Supervisor**: 1 hour/week for consolidation. Absorbed.
- **Category Manager / Controller**: 1 hour/month for damage review. Absorbed.
- **No incremental headcount.**

---



## W92. Inventory Adjustment & Shrinkage Authorization

| Field | Detail |
|---|---|
| **Trigger** | Cycle count discrepancy identified (W6); annual physical inventory variance (W42); confirmed theft or loss (W37); damaged goods write-off (W91); RTV write-off (W88); or system correction needed (negative inventory, data entry error) |
| **Frequency** | ~1,500–2,500 adjustments/month across all locations (mostly from cycle counts) |
| **Volume** | ~8–12 adjustments per store per month; ~30–50 per DC per month |
| **Owner** | Controller |
| **Participants** | Stock Associate, Store Manager, DC Supervisor, Cost Accountant, Controller, Internal Audit |

### Background

W6 (Cycle Counting) identifies discrepancies between system and physical inventory, and W42 (Annual Physical Inventory) produces wall-to-wall variances. However, the resolution — investigating the root cause, authorizing the adjustment, and posting the accounting entry — requires a separate control workflow. Inventory adjustments directly impact the GL (inventory asset and COGS/shrinkage expense), so they require proper authorization tiers, documentation, and segregation of duties. This workflow also covers adjustments from confirmed theft (W37), damage write-offs (W91), and system corrections.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Adjustment request creation**: System automatically creates adjustment request when: (a) cycle count (W6) reveals variance exceeding threshold (±1 unit for A-items, ±3 for B-items, ±5 for C-items), (b) physical inventory (W42) variance confirmed, (c) confirmed theft reported (W37), (d) damaged goods disposition completed (W91 — markdown, scrap, or donate), (e) RTV unresolved > 90 days (W88.9 — auto-write-off), (f) negative inventory detected (system shows on-hand < 0). Alternatively, Stock Associate or DC Supervisor manually creates adjustment request with reason code and supporting documentation | System / Stock Associate / DC Supervisor | Store Manager / DC Supervisor | 5 min/request |
| 2 | **Root cause classification**: Initiator or Supervisor classifies the adjustment reason: (a) shrinkage/theft (unexplained loss), (b) receiving/putaway error (item received but put in wrong location), (c) POS scanning error (wrong item scanned at checkout), (d) damage/spoilage (per W91), (e) vendor short-shipment (received less than PO — per W3), (f) data entry error (incorrect quantity or SKU entered), (g) negative inventory correction (overselling or system timing), (h) RTV write-off (per W88), (i) intercompany/transfer discrepancy (per W22), (j) other (with explanation) | Dept. Supervisor / DC Supervisor | Store Manager / DC Supervisor | 5 min/request |
| 3 | **Investigation** (for material adjustments): (a) A-items with variance > PHP 10,000: Dept. Supervisor investigates — review POS transactions for scanning errors, review receiving logs, check transfer records, review CCTV if theft suspected; (b) confirmed theft: escalate to Loss Prevention per W37; (c) receiving/putaway error: check if item is in adjacent bin location (common in big-box with 35,000 SKUs); (d) document findings in adjustment request | Dept. Supervisor / DC Supervisor | Store Manager / DC Supervisor | 15 min/investigation |
| 4 | **Authorization** (tiered approval): (a) **Level 1 — Store Manager / DC Supervisor**: adjustments ≤ PHP 5,000 per SKU per count event; max 20 adjustments/month per location without escalation; (b) **Level 2 — Cost Accountant**: adjustments > PHP 5,000 and ≤ PHP 50,000; validates GL impact and cost center allocation; (c) **Level 3 — Controller**: adjustments > PHP 50,000; reviews root cause documentation and investigation quality; approves or requests additional investigation; (d) **Level 4 — CFO**: adjustments > PHP 500,000 (typically annual physical inventory major variances); requires Internal Audit observation per CTL-38 in Internal Controls Matrix | Per tier above | Per tier above | 5–15 min/approval |
| 5 | **System posting**: Upon authorization, system posts inventory adjustment: (a) Dr. COGS-Shrinkage / Cr. Inventory (at WAC) — for losses, theft, damage write-offs; (b) Dr. Inventory / Cr. COGS-Shrinkage — for gains (found items, receiving errors corrected); (c) Dr. Vendor Claim Receivable / Cr. Inventory — for vendor short-shipment (pending vendor credit per W88); (d) Dr. Carrier Claim Receivable / Cr. Inventory — for carrier damage (pending carrier claim); (e) adjustment posted with authorization trail, reason code, supporting evidence reference, and GL impact | System | Cost Accountant | Automated |
| 6 | **Negative inventory resolution**: Special handling for negative inventory (system shows < 0 on-hand): (a) system auto-creates adjustment request flagged as high priority; (b) immediate investigation by Dept. Supervisor — most common causes: (i) POS sold item not yet received (timing), (ii) POS sold wrong SKU (scanning error), (iii) cycle count in progress but not posted; (c) resolution within 24 hours; if unresolved, system blocks further sales of that SKU at that location until resolved (prevents cascading negative inventory) | System / Dept. Supervisor | Store Manager | 15 min/case |
| 7 | **Monthly shrinkage reporting**: Cost Accountant prepares monthly shrinkage report: (a) total adjustments by reason code, by location, by category; (b) shrinkage as % of sales (target: < 1.5% per company profile); (c) shrinkage trend by store — identify stores exceeding target; (d) adjustment authorization compliance — verify all adjustments properly approved per tier; (e) top 20 SKUs by shrinkage value; submits to Controller for management reporting per W35 | Cost Accountant | Controller | 2 hours/month |
| 8 | **Quarterly Internal Audit review**: Internal Audit samples adjustments quarterly: (a) verify authorization compliance (right approval tier used), (b) verify documentation completeness (reason code, investigation, evidence), (c) verify segregation of duties (requestor ≠ authorizer for Level 2+), (d) test negative inventory resolution timeliness; findings reported to CFO and Audit Committee | Internal Audit | CFO | 4 hours/quarter |

### System Touchpoints
- Auto-adjustment request creation from cycle count variances, physical inventory variances, negative inventory detection (W92.1)
- Reason code classification with mandatory documentation per code type (W92.2)
- Tiered approval workflow with amount-based routing and authorization trail (W92.4)
- GL posting with WAC recalculation and proper debit/credit routing (W92.5)
- Negative inventory alerting with auto-block on further sales (W92.6)
- Monthly shrinkage report: by reason, location, category, SKU (W92.7)
- Adjustment authorization compliance dashboard for Internal Audit (W92.8)
- Integration with W3 (DC receiving — short-shipment adjustments), W4 (replenishment — in-transit variances), W6 (cycle counting — primary source of adjustments), W12 (returns — cross-store adjustments), W22 (transfers — discrepancy adjustments), W37 (loss prevention — confirmed theft write-offs), W42 (annual physical inventory — major adjustments), W44 (vendor scorecard — vendor short-shipment rate), W88 (RTV — unresolved write-offs), W91 (damaged goods — disposition-driven adjustments)

### Staffing Implication
- **Cost Accountant**: adds ~2 hours/month for shrinkage reporting and Level 2 approvals. Absorbed.
- **Controller**: adds ~1 hour/month for Level 3 approvals and shrinkage review. Absorbed.
- **Internal Audit**: adds ~4 hours/quarter for adjustment testing. Absorbed.
- **No incremental headcount.**

---



## W105. Multi-Channel Inventory Allocation & Priority Governance

| Field | Detail |
|---|---|
| **Trigger** | Quarterly allocation governance review; or ad-hoc triggered by sustained stockout pattern, new channel launch, or allocation conflict escalation |
| **Frequency** | Quarterly governance review; continuous allocation monitoring |
| **Volume** | 35,000 active SKUs allocated across: 200 stores (W4), ecommerce BOPIS from stores (W11), ecommerce home delivery from DCs (W19), B2B trade/corporate orders (W58), promotional pre-positioning (W57), backorder fulfillment (W56) |
| **Owner** | Supply Planning Manager |
| **Participants** | Supply Planning Manager, VP Supply Chain, Category Manager, Ecommerce Manager, Sales Manager, DC Supervisor |

### Background

Multiple workflows reference inventory allocation: W4 (store replenishment with constrained allocation), W11 (BOPIS ATP reservation), W19 (home delivery ATP), W57 (promotional pre-positioning), and W56 (backorder priority). However, there is no unified governance framework defining allocation priorities when multiple demand channels compete for the same limited inventory. During constrained supply periods (vendor delays, seasonal peaks, promotional surges), the absence of clear priority rules leads to ad-hoc decisions, channel conflict, and customer dissatisfaction. This workflow establishes the allocation governance framework.

### Allocation Priority Hierarchy (Constrained Supply)

| Priority | Demand Channel | Rationale | Override Authority |
|---|---|---|---|
| 1 | **Existing customer backorders** (W56) | Customer already committed and waiting; highest service obligation | Supply Planning Manager |
| 2 | **Promotional pre-positioning** (W57) | Committed marketing spend; stockout during promo damages brand | VP Supply Chain + VP Merchandising |
| 3 | **Ecommerce BOPIS** (W11) | Customer already paid; fulfillment SLA of 4 hours | Supply Planning Manager |
| 4 | **Ecommerce home delivery** (W19) | Customer already paid; fulfillment SLA of 2–5 days | Supply Planning Manager |
| 5 | **B2B trade/corporate project orders** (W58) | Contractual obligation; high-value accounts | VP Supply Chain + Sales Manager |
| 6 | **Store replenishment — A-items** (W4) | Top 20% of SKUs generating 80% of revenue; highest retail impact | Supply Planning Manager |
| 7 | **Store replenishment — B-items** (W4) | Mid-tier items; moderate revenue impact | Supply Planning Manager |
| 8 | **Store replenishment — C-items** (W4) | Bottom 50% of SKUs; lowest revenue impact; highest tolerance for stockout | System auto-allocated from residual |

**Safety stock buffers**: each channel's ATP calculation deducts a configurable safety stock buffer that is NOT available for allocation to any channel — this buffer protects against demand variability and prevents complete stockout at any location.

- **DC safety stock**: configurable per SKU per DC (set during W31.8 parameter governance); deducted from DC ATP before any allocation
- **Store safety stock**: configurable per SKU per store; deducted from store ATP for BOPIS availability
- **BOPIS buffer**: stores reserve a configurable buffer (default: 2 units per A-item SKU) so that walk-in customers are not completely displaced by BOPIS orders

### Steps

### Quarterly Allocation Governance Review

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Allocation performance report**: System generates quarterly allocation performance report: (a) fill rate by demand channel (target: A-items ≥ 97%, B-items ≥ 93%, C-items ≥ 85%), (b) allocation conflicts — instances where demand exceeded supply and priority rules were applied, with channel impact, (c) safety stock breaches — instances where actual inventory fell below safety stock buffer (indicates systemic under-supply), (d) channel stockout frequency — how often did each channel experience out-of-stock due to allocation exhaustion?, (e) override log — all instances where default priority was overridden, with approver and justification | System | — | Automated |
| 2 | Supply Planning Manager reviews allocation performance with cross-functional stakeholders: (a) **Ecommerce Manager**: BOPIS and home delivery fill rate, customer impact of stockouts, allocation adequacy for peak events, (b) **Sales Manager**: B2B trade/corporate fill rate, impact on account relationships and revenue, (c) **Category Manager**: category-level fill rate, vendor supply reliability issues, (d) **DC Supervisor**: operational impact of allocation-driven picking priorities (promotional vs. routine orders), capacity conflicts | Supply Planning Manager | VP Supply Chain | 2 hours/quarter |
| 3 | **Allocation rule review**: Supply Planning Manager and VP Supply Chain review and adjust allocation rules: (a) are priority rankings still appropriate given channel revenue contribution and growth trajectory?, (b) are safety stock buffers adequate or excessive? (benchmark: buffer usage rate — how often is buffer consumed?), (c) should any channels be added or removed from the hierarchy? (e.g., new ship-from-store channel per W19B), (d) are ABC classification thresholds (W31.8) correctly driving allocation priority — do A-items get sufficient allocation vs. B/C-items? | Supply Planning Manager / VP Supply Chain | VP Supply Chain | 1 hour/quarter |
| 4 | **Conflict resolution from past quarter**: Review all allocation overrides from the past quarter — were they justified? Were the right approvers involved? Should any override patterns trigger a permanent rule change? (e.g., if B2B orders were frequently prioritized over ecommerce, consider adjusting the default hierarchy) | Supply Planning Manager | VP Supply Chain | 1 hour/quarter |
| 5 | Supply Planning Manager updates allocation configuration in system based on review: priority weights, safety stock parameters, ATP buffer rules; documents changes with effective date, rationale, and VP Supply Chain approval; system logs all configuration changes with audit trail | Supply Planning Manager | VP Supply Chain | 30 min/quarter |

### Continuous Allocation Monitoring

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 6 | System monitors allocation conflicts in real-time: when demand from a higher-priority channel exhausts available allocation for a lower-priority channel, system alerts Supply Planner with: SKU, location, channels affected, quantities short, and suggested action (expedite PO per W2, arrange inter-DC transfer per W22, or accept stockout) | System | — | Automated |
| 7 | Supply Planner reviews daily allocation conflict dashboard; resolves conflicts by: (a) expediting POs with vendors for critical shortfalls, (b) rebalancing safety stock buffers (temporary reduction for low-demand locations), (c) arranging emergency inter-DC transfers per W22, (d) recommending substitution to affected channel (alternative SKU with available inventory) | Supply Planner | Supply Planning Manager | 30 min/day |
| 8 | **Allocation override**: When a business decision requires deviating from the default priority (e.g., prioritizing a large corporate project order over routine store replenishment), requestor (Category Manager, Sales Manager, or Ecommerce Manager) submits allocation override request in system with: SKU, quantity, source location, requested priority channel, business justification, and revenue impact; VP Supply Chain approves overrides affecting > 5% of a location's inventory; system logs override with full audit trail | Requestor / VP Supply Chain | VP Supply Chain | 15 min/override |

### System Touchpoints
- Configurable allocation priority engine with channel-specific weights and safety stock buffers (W105 allocation hierarchy)
- ATP calculation per channel per SKU per location incorporating priority rules, safety stock, and existing commitments (W105 ATP logic)
- Quarterly allocation performance report with fill rate, conflicts, safety stock breaches, and override log (W105.1)
- Daily allocation conflict dashboard with real-time alerts and suggested actions (W105.6)
- Allocation override request workflow with VP Supply Chain approval and audit trail (W105.8)
- Integration with W4 (store replenishment), W11 (BOPIS), W19 (home delivery), W22 (inter-DC transfers), W31 (demand planning parameters), W56 (backorder priority), W57 (promo allocation), W58 (B2B orders)

### Staffing Implication
- **Supply Planning Manager**: adds ~4 hours/quarter for governance review + 30 min/day for conflict monitoring = ~28 hours/quarter. Absorbed within existing role.
- **Supply Planner**: 30 min/day for conflict resolution = ~10 hours/month. Absorbed within existing planning duties.
- **VP Supply Chain**: ~2 hours/quarter for governance review + ~30 min/quarter for override approvals. Absorbed.
- **No incremental headcount.**

---

---

## W154. Proactive Store Inventory Rebalancing (Stock Push)

| Field | Detail |
|---|---|
| **Trigger** | High inventory variance between stores; slow-mover identification (W1); or localized demand spike |
| **Frequency** | Monthly |
| **Volume** | ~500–1,000 SKUs rebalanced per cycle |
| **Owner** | Supply Planning Manager |
| **Participants** | Supply Planner, Store Managers, Logistics |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Analysis**: Identify SKUs with "Overstock" at Store A and "Understock/High Velocity" at Store B | Supply Planner | Supply Planning Mgr | 4 hours |
| 2 | **Validation**: Store Managers confirm physical stock availability and condition for transfer | Store Manager | — | 30 min/store |
| 3 | **Push Order**: System generates "Push" Stock Transfers (W22); overrides standard ROP to clear excess | Supply Planner | Supply Planning Mgr | 1 hour |
| 4 | **Logistics**: Consolidate transfers into weekly DC-to-Store backhaul or store-to-store courier | Logistics | — | Varies |
| 5 | **Impact Review**: Measure sales lift at receiving store and holding cost reduction at sending store | Supply Planner | CFO | 2 hours |

---

## W204. Regional Stock Rebalancing & Inter-Store Expedited Transfers

| Field | Detail |
|---|---|
| **Trigger** | Critical stock-out at Store A; excess stock of same SKU at Store B (within same region/cluster) |
| **Frequency** | Weekly |
| **Volume** | ~50–100 transfers per week |
| **Owner** | Regional Store Operations Manager |
| **Participants** | Store Managers, Supply Planner, Local Courier (3PL) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Opportunity Identification**: Store A Manager identifies "Sold Out" status for high-demand SKU; checks "Regional Inventory" in real-time system (W5) | Store Manager | — | 5 min |
| 2 | **Transfer Request**: Store A Manager initiates an "Expedited Transfer Request" from Store B (nearest location with > 2 weeks cover) | Store Manager | — | 2 min |
| 3 | **Approval**: Regional Manager or Supply Planner approves based on regional inventory health and cost of transfer vs. margin | Regional Manager | — | 1 hour |
| 4 | **Pick & Stage**: Store B Staff picks and stages items in backroom; system records "In-Transit" status (W22) | Stock Associate | Store Manager | 15 min |
| 5 | **Expedited Dispatch**: Local 3PL (Lalamove/Transportify) picks up from Store B; delivers to Store A within 4-8 hours | Logistics | — | 4-8 hours |
| 6 | **Receipt**: Store A Receiving Clerk processes Goods Receipt; inventory available for sale immediately | Receiving Clerk | Store Manager | 10 min |

---

## W214. Store-to-Store Expedited Transfers (Customer-Initiated)

| Field | Detail |
|---|---|
| **Trigger** | Customer requests an out-of-stock item at Store A that is in stock at Store B |
| **Frequency** | Daily |
| **Volume** | ~20–30 customer-initiated transfers per day |
| **Owner** | Store Manager (Store A) |
| **Participants** | Sales Associate, Store Manager B, 3PL Courier, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Inquiry**: Customer requests an out-of-stock item at Store A. Sales Associate checks real-time inventory in ERP and finds stock available at nearby Store B. | Sales Associate | — | 5 min |
| 2 | **Order & Payment**: Sales Associate offers to have the item transferred from Store B via expedited courier. Customer agrees and pays for the item (plus optional transfer fee) at Store A; system generates a "Customer-Initiated Transfer Order" with status "Awaiting Pickup". | Sales Associate | Store Manager A | 10 min |
| 3 | **Notification**: System automatically routes a high-priority pick task to Store B's terminal/handheld. | System | — | Automated |
| 4 | **Pick & Pack**: Store B Stock Associate picks the item, places it in secure packaging, and prints an transfer label with Store A's order number and Customer details. | Stock Associate B | Store Manager B | 15 min |
| 5 | **Dispatch**: Store B books a local 3PL courier (Lalamove/Grab/Transportify) via ERP integration to transport the item to Store A. | Store Manager B | — | 10 min |
| 6 | **Transit & Arrival**: 3PL Courier transports item to Store A. Store A Receiving Clerk receives it in the system; ERP automatically triggers an SMS/email to the Customer ("Your order is ready for pickup!"). | Courier / Store A Clerk | Store Manager A | 1–3 hours |
| 7 | **Customer Collection**: Customer arrives at Store A Pro Desk; Sales Associate scan-confirms collection and closes the transfer order. | Sales Associate | — | 5 min |

---

## W218. Inter-DC Stock Rebalancing (Stock Push)

| Field | Detail |
|---|---|
| **Trigger** | Supply planning identifies "Overstock" in one DC and "Stock-out Risk" in another |
| **Frequency** | Monthly; or as needed for peak seasons |
| **Volume** | Bulk pallet transfers |
| **Owner** | Supply Planning Manager |
| **Participants** | Supply Planner, DC Managers, Logistics (3PL Carrier) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Imbalance Detection**: Supply Planner reviews "DC-to-DC Inventory Health" report; identifies SKUs where current DC stock > 6 months cover vs. < 2 weeks at another DC | Supply Planner | — | 2 hours |
| 2 | **Transfer Proposal**: System suggests "Rebalancing Transfer" (Push) to move bulk stock to the understocked DC | System / Planner | Supply Planning Mgr | 1 hour |
| 3 | **Fulfillment Booking**: Logistics books heavy-duty transport (tractor head / 10-wheeler) for the bulk move | Logistics | — | 1 hour |
| 4 | **Loading**: Source DC picks from bulk storage; system verifies quantities via WMS (W3) | DC Picker | DC Supervisor | 2 hours |
| 5 | **Transit**: Bulk shipment moves between DCs; system tracks "In-Transit" at WAC | Driver | — | 1–3 days |
| 6 | **Receipt**: Destination DC processes bulk GR; inventory available for sale immediately | Receiving Clerk | DC Manager | 2 hours |
| 7 | **Efficiency Audit**: Review total freight cost vs. margin preserved by avoiding stock-outs | Supply Planning Mgr | — | Quarterly |

### System Touchpoints
- DC-level inventory health and cover analysis dashboard
- Bulk transfer order generation (Push mode)
- WMS bulk zone picking and receiving
- In-transit inventory value tracking between DCs

---

## W219. Store Inventory Quarantine & Recertification

| Field | Detail |
|---|---|
| **Trigger** | Customer return (W12), cycle count discrepancy, or receive inspection identifies suspected, damaged, or expired stock |
| **Frequency** | Daily across all stores |
| **Volume** | ~20–50 items/store/month |
| **Owner** | Store Quality Inspector |
| **Participants** | Store Quality Inspector, Stock Associate, Store Manager, Category Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Quarantine Creation**: CSR or Stock Associate flags stock as "Damaged" or "Suspect"; system moves inventory from "Saleable" status to "Quarantined" status (Dr. Quarantined Inventory / Cr. Saleable Inventory) and moves to quarantine location | CSR / Stock Associate | Store Manager | 5 min |
| 2 | **Physical Segregation**: Stock Associate prints "Quarantine Label" from system; attaches to item and physically moves to the secure store quarantine cage | Stock Associate | Dept. Supervisor | 10 min |
| 3 | **Inspection & Evaluation**: Store Quality Inspector performs physical inspection; uploads photo evidence to system; classifies defect (e.g., cosmetic package damage, internal mechanical fault, paint tint mismatch) | Quality Inspector | Store Manager | 15 min |
| 4 | **Disposition Determination**: Inspector enters recommended disposition: (a) *Refurbish & Recertify* (repackage, clean, test); (b) *B-Grade Downgrade* (cosmetic damage, sell on discount); (c) *Scrap / Write-off*; (d) *Return to Vendor (RTV)* | Quality Inspector | Store Manager | 10 min |
| 5 | **Action Execution**: <br>• (a) *Refurbish*: Stock Associate performs repacking; system updates status to "Saleable" (Dr. Saleable Inventory / Cr. Quarantined Inventory);<br>• (b) *B-Grade*: System moves SKU to "B-Grade/Clearance" status and auto-applies standard clearance markdown (W93);<br>• (c) *Scrap*: Store Manager approves; system posts inventory adjustment (Dr. Scrap Expense / Cr. Quarantined Inventory) and schedules disposal (W82);<br>• (d) *RTV*: System generates Return to Vendor request (W88) | Stock Associate / System | Store Manager | 15 min |
| 6 | **Discrepancy Reporting**: Quality Inspector generates monthly quarantine velocity and defect report to highlight recurring SKU failures to Category Managers | Quality Inspector | Store Manager | 1 hour/month |

### System Touchpoints
- Segregated quarantine inventory status (non-ATP)
- Photographic upload and defect category logging in system
- Automated financial posting for status transitions and write-offs
- Integration with W93 (markdowns), W88 (RTV), and W82 (hazmat/scrap)

---

## W220. Slow-Moving & Obsolete Inventory (SLOB) Provisioning & Liquidation

| Field | Detail |
|---|---|
| **Trigger** | Monthly inventory aging cycle or system alert on aging thresholds |
| **Frequency** | Monthly |
| **Volume** | Reviewing ~500–1,000 slow-moving SKUs chain-wide |
| **Owner** | Inventory Control Manager |
| **Participants** | Inventory Control Manager, Category Manager, CFO, VP Merchandising, Store Managers |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Aging Detection**: System generates monthly aging report showing SKUs with > 180 days since last sale or inventory age exceeding category-specific thresholds (e.g., lumber shelf life, paint expiry) | System | Inventory Control Mgr | Automated |
| 2 | **Obsolescence Provisioning**: Finance automatically calculates SLOB provision using standardized logic (e.g., 50% provision for 180–270 days age, 100% provision for > 270 days); system posts journal (Dr. Inventory Obsolescence Expense / Cr. SLOB Inventory Allowance) | System / Financial Analyst | CFO | 2 hours |
| 3 | **Liquidation Campaign Proposal**: Inventory Control Manager routes the aging SKU list to the respective Category Manager with recommended liquidation strategies: (a) in-store clearance markdown (W93); (b) bulk wholesaler buy-out (W146); (c) stock transfer to high-velocity stores (W204); (d) vendor buy-back | Inventory Control Mgr | Category Manager | 2 days |
| 4 | **Strategy Approval**: Category Manager selects liquidation route; CFO/VP Merchandising approves any margin impact exceeding PHP 100K | Category Manager | CFO | 1 day |
| 5 | **Campaign Execution**: <br>• For in-store clearance: system applies pricing markdown;<br>• For redistribution: system auto-generates transfer orders (W204);<br>• For wholesaler: system creates Wholesale Sales Order (W146) | System / Category Manager | — | 1 hour |
| 6 | **Allowance Release**: Upon actual sale of liquidated items or approved physical scrap write-off: system releases the provision allowance (Dr. SLOB Inventory Allowance / Cr. Inventory Asset) to realize the final inventory value | System | Financial Analyst | Automated |

### System Touchpoints
- Automated Inventory Aging Engine (180, 270, 360+ days)
- Financial provisioning logic matrix
- Automated GL posting for obsolescence reserves and allowance release
- Integration with W93 (markdowns), W204 (transfers), and W146 (wholesale sales)



