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

## W1. Merchandise Planning & Assortment Review

| Field | Detail |
|---|---|
| **Trigger** | Seasonal calendar and quarterly business review |
| **Frequency** | Quarterly (4×/year) |
| **Volume** | ~8,750 SKUs reviewed per quarter (35,000 ÷ 4) |
| **Owner** | VP Merchandising |
| **Participants** | Category Managers, Buyers, Pricing Analysts, Merchandise Planners, Store Operations rep |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Pull category performance report (sales, margin, turns, sell-through) | Pricing Analyst | Category Manager | 2 hours |
| 2 | Identify underperformers (bottom 10% by revenue/sqm, negative margin, < 2 turns/year) | Category Manager | VP Merchandising | 3 hours |
| 3 | Review seasonal calendar and upcoming promotional events | Category Manager | VP Merchandising | 1 hour |
| 4 | Propose assortment changes: add new SKUs, discontinue slow movers, adjust depth/breadth | Buyer | Category Manager | 4 hours |
| 5 | Validate proposed changes against vendor contracts and minimum order quantities | Buyer | Category Manager | 2 hours |
| 6 | Present assortment plan to VP Merchandising for approval | Category Manager | VP Merchandising | 2 hours (meeting) |
| 7 | Update item master: create new SKUs, flag discontinued items, set discontinuation dates | Merchandise Planner | Category Manager | 3 hours |
| 8 | Communicate changes to stores via bulletin / system alert | Merchandise Planner | VP Merchandising | 1 hour |

**Total effort per quarter**: ~18 hours across team

### System Touchpoints
- Sales analytics by category/SKU (W1.1)
- Inventory turns and aging reports (W1.1)
- Item master create/modify with approval workflow (W1.7)
- Vendor contract and pricing reference (W1.5)
- Store communication / bulletin system (W1.8)
- Product content coordination: when new SKUs are created or item attributes change (W1.7), Merchandise Planner or Marketing coordinates product content (photos, specifications, dimensions, how-to guides) for publishing to the ecommerce platform via PIM integration or manual upload
- Sample / demo inventory management: system supports a 'Sample/Demo' inventory status for display items (tile gallery boards, appliance demo units, tool displays) tracked separately from saleable stock; samples excluded from available inventory and replenishment calculations but included in inventory valuation; quarterly review by Department Supervisor identifies samples for markdown sale, vendor return, or scrap; display refresh planned as part of W1 assortment review
- Slow-mover / dead stock operational review: monthly cross-functional review where Category Managers, Supply Planner, and Cost Accountant examine the slow-mover report (system-generated: items with > 90 days since last sale, < 2 turns/year, or current stock > 6 months forward demand); disposition decided per SKU — continue selling (monitor), markdown and clearance (W13.9a), RTV (W3.6a), bulk liquidation (W13.9b), donation, or scrap; results feed into quarterly assortment review (W1) for potential discontinuation; accounting consequences (NRV write-down) processed per W9a.16b
- Negative inventory resolution: system generates daily negative inventory alert listing all SKU-locations where on-hand < 0; at store level, Stock Associate investigates root cause (timing lag from offline POS transactions per W5d, receiving error, mispick, or cycle count needed); at DC level, Inventory Control clerk investigates (pending GR posting, allocation error, picking error); resolution action depends on cause — recount and adjust (W6), wait for pending transaction posting, or force adjustment with supervisor approval; system blocks negative-inventory locations from ecommerce ATP availability until resolved; monthly report of negative inventory frequency by location feeds into inventory accuracy improvement initiatives

### Staffing Implication
5 Category Managers each handling ~2 categories per quarterly cycle = manageable at ~18 hours/category. The 3 Pricing Analysts handle data pulls and analysis in parallel. 10–12 Buyers handle vendor validation. Current team of ~40 in Merchandising is adequate.

---

## W2. Procurement — Purchase Order Cycle

### W2a. Auto-Replenishment (Stocking Items)

| Field | Detail |
|---|---|
| **Trigger** | SKU hits reorder point (ROP) in system |
| **Frequency** | Daily review; POs generated daily |
| **Volume** | ~1,200 POs/month; ~18,000 PO lines/month |
| **Owner** | Buyer |
| **Participants** | System (auto-suggest), Buyer, Category Manager (approval if > PHP 50K) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System calculates ROP breaches based on: avg daily demand × lead time + safety stock | System | — | Automated |
| 2 | System generates suggested POs grouped by vendor, consolidated across DCs | System | — | Automated |
| 3 | Buyer reviews suggested PO list each morning: check quantities, adjust if needed | Buyer | Category Manager | 1–2 hours/day |
| 4 | Buyer confirms or modifies PO quantities, delivery dates, and DC destinations | Buyer | Category Manager | 1–2 hours/day |
| 5 | If PO total > PHP 50K: route to Category Manager for approval | Category Manager | Category Manager | 15 min/PO |
| 6 | If PO total > PHP 500K: route to VP Merchandising for approval | VP Merchandising | VP Merchandising | 15 min/PO |
| 7 | Approved PO transmitted to vendor (email, EDI, or vendor portal); vendors with portal access can view PO details, confirm delivery dates, and submit invoices through the portal | System / Buyer | Buyer | Automated |
| 8 | Buyer tracks open POs; follows up on overdue deliveries | Buyer | Buyer | 1 hour/day |

**Total buyer effort**: ~3–5 hours/day for daily PO review and follow-up

### W2b. Import Purchase Orders

| Field | Detail |
|---|---|
| **Trigger** | Seasonal buy plan or replenishment of import SKUs |
| **Frequency** | ~20–30 import POs/month |
| **Volume** | 50–70 TEUs/month |
| **Owner** | Buyer (with Import Coordinator) |
| **Participants** | Buyer, Import Coordinator, Finance (LC), Customs Broker, Warehouse (receiving) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Buyer creates import PO with estimated landed cost (FOB + freight + duty + insurance) | Buyer | Category Manager | 30 min/PO |
| 2 | Route for approval (> PHP 50K → Category Manager; > PHP 500K → VP Merchandising; > PHP 2M → CFO) | Category Manager / VP / CFO | As per tier | 15–30 min/PO |
| 3 | Finance opens Letter of Credit (LC) with bank or arranges TT payment | Treasury Analyst | CFO | 1–2 hours/PO |
| 4 | Buyer confirms order with vendor; vendor provides Proforma Invoice | Buyer | Buyer | 30 min/PO |
| 5 | Import Coordinator arranges freight booking (container) | Import Coordinator | Buyer | 1 hour/PO |
| 6 | Vendor ships; provides Bill of Lading (BL), Packing List, Commercial Invoice | Vendor | — | External |
| 7 | Import Coordinator receives shipping docs; engages customs broker | Import Coordinator | Import Coordinator | 1 hour/PO |
| 8 | Customs broker files import entry; pays duties/taxes | Customs Broker | Import Coordinator | 1–2 days |
| 9 | Import Coordinator tracks shipment status; updates ETA in system | Import Coordinator | Buyer | 15 min/day per PO |
| 10 | Goods arrive at port; customs clearance and release | Customs Broker | Import Coordinator | 1–3 days |
| 11 | Transport to DC; Receiving clerk processes Goods Receipt | Receiving Clerk (DC) | DC Manager | 2–4 hours/container |
| 12 | System calculates actual landed cost (duty, freight, insurance allocated per SKU) using GR exchange rate | System | Finance | Automated |
| 13 | Finance reconciles LC/TT payment with PO and Goods Receipt; system posts FX gain/loss if invoice rate differs from GR rate | Treasury Analyst | CFO | 30 min/PO |

**Total cycle time**: 45–90 days from PO to receipt

### System Touchpoints
- ROP/EOQ auto-calculation per SKU per location (W2a.1–2)
- PO creation with multi-tier approval workflow (W2a.5–6)
- Vendor PO transmission (W2a.7)
- Open PO tracking / overdue alerts (W2a.8)
- Import PO tracking with LC/BL/container fields (W2b.1–9)
- Landed cost calculation engine (W2b.12)
- 3-way match: PO → Goods Receipt → Vendor Invoice (W2b.13)
- FX rate capture at PO creation (budget rate), goods receipt (spot rate or BSR), and invoice (actual rate); automatic FX gain/loss posting (W2b.12–13)
- Month-end FX revaluation of open foreign-currency balances at BIR exchange rate with unrealized FX gain/loss posting and auto-reversal (W9a.5a)

### W2c. Blanket / Contract Purchase Orders

| Field | Detail |
|---|---|
| **Trigger** | Annual supply agreement negotiation cycle |
| **Frequency** | ~40–60 active contracts at any time; new contracts and renewals throughout the year |
| **Volume** | Primarily with top 50 vendors (by spend); typically covers 20–60% of purchasing volume for staple categories (cement, paint, lumber, electrical cable, plumbing fittings) |
| **Owner** | Buyer |
| **Participants** | Buyer, Category Manager, VP Merchandising, Finance (budget), Vendor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Buyer negotiates annual supply agreement with vendor: product range, pricing tiers, minimum/maximum commitment quantities, delivery schedule, payment terms, rebate structure | Buyer | Category Manager | 4–8 hours/vendor |
| 2 | Category Manager approves contract terms; VP Merchandising approves if total contract value > PHP 5M | Category Manager / VP | VP Merchandising | 30 min |
| 3 | Finance validates contract commitment against annual purchase budget | Controller | CFO | 30 min |
| 4 | Buyer creates Blanket PO in system: vendor, SKU lines with contract price, validity period (typically 1 year), min/max commitment quantities, agreed delivery schedule or release parameters | Buyer | Category Manager | 30–60 min |
| 5 | System enforces contract pricing on all release orders; alerts Buyer if release quantity would exceed maximum commitment | System | — | Automated |
| 6 | Buyer or system creates Release Order against Blanket PO (per agreed schedule or triggered by ROP): specifies exact quantity and delivery date for this release | Buyer / System | Buyer | 10 min |
| 7 | Release Order follows standard PO approval (W2a.5–6) if release value exceeds threshold; otherwise auto-approved within contract parameters | System | — | Automated |
| 8 | Vendor ships per release order; standard receiving (W3) and AP matching (W7) apply | Vendor | Buyer | Per W3/W7 |
| 9 | System tracks cumulative released quantity and value against contract commitment; Buyer monitors to ensure min-commit targets are met | System | Buyer | Automated |
| 10 | Monthly: Buyer reviews contract utilization report; identifies contracts below minimum commitment pace (risk of penalty or unfavorable renegotiation) | Buyer | Category Manager | 1 hour/month |
| 11 | Quarterly: Buyer and Category Manager evaluate contract performance vs. spot buying; decide renewal, renegotiation, or termination | Buyer + Category Manager | VP Merchandising | 2 hours/quarter |
| 12 | At contract expiry: system alerts Buyer 60 days before; if not renewed, system blocks further release orders | System | — | Automated |

**Contract coverage**: ~40–60 active blanket/contract POs at any time, representing ~45% of annual COGS (aligned with top-20 vendor concentration)

### System Touchpoints
- Blanket/contract PO creation with SKU lines, pricing tiers, validity dates, and commitment quantities (W2c.4)
- Contract pricing enforcement on release orders (W2c.5)
- Release order creation against blanket PO with quantity tracking (W2c.6–7)
- Cumulative commitment tracking: released vs. minimum vs. maximum (W2c.9)
- Contract utilization reporting (W2c.10)
- Contract expiry alerting with release order blocking (W2c.12)
- Integration with W27 (vendor rebates — rebates may be tied to contract commitment achievement)

### Staffing Implication
- **Buyers**: 40–60 contracts ÷ 10–12 buyers = ~4–5 contracts each. Monthly review adds ~1 hour/buyer/month. Quarterly evaluation adds ~2 hours/buyer/quarter. Absorbed within existing team.
- No incremental headcount beyond existing Buyer and Finance teams.

---

## W3. Warehouse Receiving & Putaway

| Field | Detail |
|---|---|
| **Trigger** | Vendor delivery truck arrives at DC (or container from port) |
| **Frequency** | ~6,000 goods receipts/month across all DCs; ~1,200/DC/month; ~40/day per DC |
| **Volume** | ~15 lines per receipt on average |
| **Owner** | DC Receiving Supervisor |
| **Participants** | Receiving Clerk, Quality Checker, Putaway Staff, DC Supervisor, Buyer (if discrepancy) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Truck arrives at DC gate; guard checks delivery schedule vs. appointment log | Guard | DC Supervisor | 5 min |
| 2 | Receiving Clerk pulls up expected PO or Transfer Order in system | Receiving Clerk | DC Supervisor | 2 min |
| 3 | Unload truck; stage in receiving area | Unloading Crew (3–4) | Receiving Clerk | 30–60 min |
| 4 | Scan/verify each item against PO: SKU, quantity, lot/batch (if applicable) | Receiving Clerk | DC Supervisor | 20–40 min |
| 5 | Quality check on sampled items (damage, correctness, expiry if applicable) | Quality Checker | DC Supervisor | 10–20 min |
| 6 | If discrepancy (shortage, damage, wrong item): flag in system; notify Buyer | Receiving Clerk | DC Supervisor | 5 min |
| 6a | If damaged goods: Receiving Clerk creates damage report with photos; initiates one of: (a) Return to Vendor (RTV) via Buyer, (b) scrap with DC Supervisor authorization, or (c) insurance claim for insured shipments. For insurance claims: Receiving Clerk documents damage with photos and notes on delivery receipt; Import Coordinator or DC Supervisor files claim with insurance provider within required notification window (typically 3–5 business days); system tracks claim status; upon settlement, Finance posts insurance recovery to income and reduces inventory loss | Receiving Clerk | DC Supervisor | 10 min |
| 6b | Buyer reviews RTV request; coordinates with vendor for credit note or replacement shipment | Buyer | Category Manager | 15 min/occurrence |
| 6c | If scrap authorized: DC Supervisor approves scrap disposition; system removes inventory and posts loss to damage/scrapping account | DC Supervisor | DC Manager | 5 min |
| 7 | Confirm Goods Receipt in system; inventory increases in real-time | Receiving Clerk | DC Supervisor | 5 min |
| 8 | System suggests putaway location based on zone, bin capacity, item velocity | System | — | Automated |
| 9 | Putaway staff moves goods to assigned bin; scan-confirm in system | Putaway Staff | DC Supervisor | 15–30 min |
| 10 | Update PO/TO status; trigger vendor invoice matching (AP) | System | — | Automated |

**Total time per receipt**: ~1.5–3 hours from gate to bin

### Cross-Dock Flow (Fast-Movers — ~30% of receipts)

For high-velocity items (A-class), steps 8–9 are skipped. Instead:
- After step 7, goods are moved directly to outbound staging area
- Allocated to pending store replenishment orders
- Loaded onto outbound trucks same day

### W3b. Yard & Outdoor Inventory Management

For lumber, building materials, and other bulky items stored in outdoor yard areas (present at all DCs and stores per the Lumber & Building Materials Yard zone):

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Goods received at yard gate (separate from indoor receiving); Receiving Clerk verifies against PO/TO using handheld | Receiving Clerk | DC Supervisor / Dept. Supervisor | 20–40 min |
| 2 | System records receipt into yard zone (zone-level tracking, not individual bin); inventory tracked by yard zone (e.g., Yard-A: Lumber, Yard-B: Cement/Blocks, Yard-C: Steel/Rebar) | System | — | Automated |
| 3 | For catch-weight items (lumber, rebar): associate measures and records actual length/piece count at receipt; system calculates quantity in board feet / linear meters / pieces | Receiving Clerk | Dept. Supervisor | 10–20 min |
| 4 | Goods staged in designated yard zone; organized by SKU type and length/size for easy retrieval | Yard Staff | DC Supervisor | 15–30 min |
| 5 | Physical counting: yard items counted by zone during cycle counts (W6) and annual physical inventory (W42); counted by piece/bundle rather than individual bin scan | Stock Associate | Dept. Supervisor | Per W6/W42 |
| 6 | Weather damage discovered during daily yard walkthrough: Stock Associate reports damage (warped lumber, water-damaged cement, rusted rebar); DC Supervisor/Dept. Supervisor approves disposition (markdown, scrap, RTV, insurance claim) per W3.6a process | Stock Associate | DC Supervisor / Dept. Supervisor | 10 min |
| 7 | Yard-to-sales-floor movement: when yard stock is needed indoors (e.g., small lumber pieces moved to indoor display), Stock Associate transfers items in system from yard zone to indoor location | Stock Associate | Dept. Supervisor | 10 min |

### System Touchpoints (Yard)
- Zone-level location master for yard areas (not bin-level) (W3b.2)
- Catch-weight/variable-length receipt and tracking in yard zones (W3b.3)
- Weather damage reporting and disposition (W3b.6)
- Yard-to-indoor inventory transfer (W3b.7)
- Yard inventory visible in real-time alongside indoor inventory (W3b.2)

### System Touchpoints
- PO/TO lookup at receiving dock (W3.2)
- Barcode/RF scanning against PO (W3.4)
- Discrepancy flagging and Buyer notification (W3.6)
- Damage disposition workflow: RTV initiation, scrap authorization, insurance claim capture (W3.6a–c)
- Goods Receipt posting → inventory update (W3.7)
- Putaway direction (zone, bin, velocity-based) (W3.8)
- Cross-dock allocation to outbound orders (cross-dock variant)
- DC forward-pick zone replenishment: system monitors forward-pick (fast-pick) location quantities in real-time; when quantity drops below minimum threshold, generates replenishment task (move from reserve/bulk storage to forward-pick); replenishment staff receives task on RF device, moves stock, scan-confirms at both locations; replenishment prioritized ahead of picking waves to avoid picker idle time (W3.8 post-putaway, integrated with W4 picking)
- Shelf-life / expiry date management: at Goods Receipt, Receiving Clerk captures manufacturing date and shelf-life duration for date-sensitive items (paint, adhesives, sealants, chemicals, cement, grout); system calculates and records expiry date per batch/lot; items with remaining shelf life below configurable threshold (e.g., < 30%) flagged for priority picking or markdown; expired items blocked from dispatch (W3.4)

### Staffing Implication
- Per DC: 3–4 Receiving Clerks (handling ~40 receipts/day in shifts, ~1.5–3 hrs each)
- Per DC: 4–6 Putaway Staff (handling putaway flow across zones)
- Per DC: 1–2 Quality Checkers
- Per DC: 1 Receiving Supervisor overseeing all inbound
- Total per DC: ~10–13 dedicated to receiving/putaway out of ~150 headcount. Reasonable.

---

## W4. Store Replenishment (DC → Store)

| Field | Detail |
|---|---|
| **Trigger** | System generates replenishment suggestion based on min/max or demand forecast |
| **Frequency** | 2–3 deliveries per store per week; ~5,000 store orders/month total |
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
- Replenishment calculation engine (min/max, forecast-based) (W4.1)
- Constrained allocation rules: when available supply is insufficient for all stores, system applies configurable allocation logic (e.g., equal distribution, rank by store revenue, prioritize A-stores) — Planner reviews and adjusts before confirming (W4.2)
- Store order creation and wave planning (W4.3)
- WMS pick/pack/ship with RF scanning (W4.4–6)
- In-transit inventory visibility (W4.8)
- Store receiving with discrepancy handling (W4.10–12)
- Real-time inventory update at both DC and store (W4.8, W4.12)
- FEFO (First Expired First Out) directed picking: for items with shelf-life tracking (paint, adhesives, chemicals, cement), WMS directs pickers to pick the earliest-expiring batch first; system sequences pick tasks by expiry date within the same SKU; ensures fresher stock remains in DC for later dispatch (W4.5)

### Staffing Implication
- **2–3 Supply Planners** (in HQ): ~167 orders/day to review. At 2–3 hours/day for review + 1 hour for wave management = 3–4 hours/day. 2–3 planners share this plus demand forecasting. Reasonable within the 30-person Supply Chain team.
- **Per DC**: 15–20 Pickers, 8–10 Packers, 4–6 Loading Crew (working in shifts to handle ~33 orders/day with ~50 lines each). Fits within ~150 DC headcount.

---

## W5. Daily Store Operations

### W5a. Store Opening

| Field | Detail |
|---|---|
| **Trigger** | Store operating hours begin (typically 8:00 AM) |
| **Frequency** | Daily per store |
| **Volume** | 200 stores × 365 days = 73,000 openings/year |
| **Owner** | Store Manager (or Assistant Manager) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Store Manager or Asst. Manager arrives; disarms alarm, unlocks | Store Manager | Store Manager | 5 min |
| 2 | Walk store floor: check for overnight issues (leaks, break-in signs, safety hazards) | Store Manager | Store Manager | 15 min |
| 3 | Boot up POS terminals; verify system connectivity | Cashier | Store Manager | 10 min |
| 4 | Count and load cash floats into each cash drawer (PHP 5,000/terminal × 5) | Cashier | Store Manager | 10 min |
| 5 | Log in to POS; confirm price file sync is current | Cashier | Store Manager | 5 min |
| 6 | Assign cashiers to terminals; brief on any promotions starting today | Store Manager | Store Manager | 10 min |
| 7 | Stock Associates begin replenishing shelves from backroom (ongoing) | Stock Associate | Department Supervisor | Continuous |

**Total opening time**: ~45 minutes before doors open

### W5b. In-Store Selling

| Field | Detail |
|---|---|
| **Trigger** | Customer enters store |
| **Frequency** | Continuous during operating hours |
| **Volume** | ~14,000 transactions/store/month; ~467/day |
| **Owner** | Department Supervisors (floor), Lead Cashier (checkout) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer browses; Sales Associate provides assistance, product advice | Sales Associate | Department Supervisor | Varies |
| 2 | If item is catch-weight (lumber, wire): Associate measures/cuts; generates weight/length label | Sales Associate | Department Supervisor | 3–5 min |
| 3 | If paint mixing: Associate mixes paint per customer color choice; system creates custom SKU | Sales Associate | Department Supervisor | 5–10 min |
| 4 | Customer brings items to checkout; Cashier scans barcodes | Cashier | Store Manager | ~2 min/txn |
| 4a | If Cashier needs to override scanned price (customer price match, damaged-item discount, competitor price): system prompts for reason code; if override > 10% or > PHP 500: system requires manager swipe/card authorization; system logs override with cashier ID, authorizing manager ID, original price, override price, and reason code | Cashier / Store Manager | Store Manager | 1 min |
| 4b | For lot/batch-tracked items (per INV-008 and INV-013): when Cashier scans a lot-tracked SKU, system prompts for batch/lot number entry (scanned from item label or manually entered); system records batch number against transaction line for forward traceability; if item barcode includes batch-level data (GS1-128 or 2D barcode), system auto-extracts batch from scan | Cashier | Store Manager | 10 sec |
| 5 | If loyalty member: Cashier scans loyalty card or asks for mobile number | Cashier | — | 15 sec |
| 6 | System calculates totals: applies promos, quantity breaks, loyalty discounts | System | — | Automated |
| 7 | Customer pays (cash, card, e-wallet, split tender) | Cashier | — | 30–60 sec |
| 8 | Receipt printed; inventory deducted in real-time | System / Cashier | — | 15 sec |
| 9 | Age-restricted items trigger cashier confirmation prompt | Cashier | Store Manager | 10 sec |
| 10 | **Void transaction**: Cashier or Store Manager initiates void before transaction is finalized (pre-void) or after finalization (post-void); manager authorization (swipe/card) required for any void; system logs void with cashier ID, authorizing manager ID, original transaction number, void reason code, and timestamp; system reverses inventory deduction, payment, loyalty points earned/redeemed, and promo usage; voided transaction retained in full audit trail (not deleted) | Cashier / Store Manager | Store Manager | 1 min |

**Average transaction time**: ~3 minutes (checkout only); total customer visit ~20–30 min

### W5c. Store Closing & End-of-Day

| Field | Detail |
|---|---|
| **Trigger** | Store operating hours end (typically 7:00–9:00 PM) |
| **Frequency** | Daily per store |
| **Owner** | Store Manager (or Assistant Manager) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Announce closing; last customers checked out | Cashier | Store Manager | 15 min |
| 2 | Run Z-report on each POS terminal (sales summary by tender type) | Cashier | Store Manager | 5 min/terminal |
| 3 | Count physical cash in each drawer; compare to Z-report | Cashier | Store Manager | 10 min/terminal |
| 3a | System auto-imports or Cashier retrieves electronic payment settlement reports from card acquirer and e-wallet providers (GCash, Maya) for the day; compares Z-report totals per tender type (credit/debit card, e-wallet) against settlement reports | System / Cashier | Store Manager | Automated + 5 min review |
| 3b | If variance between Z-report electronic totals and settlement reports: Cashier flags discrepancy; Store Manager investigates (chargebacks, pending settlements, processing fees, failed transactions); system logs variance with tender type and amount | Cashier / Store Manager | Store Manager | 10 min if any |
| 4 | Investigate and document any cash variance > PHP 200 | Store Manager | Store Manager | 10 min if any |
| 5 | Prepare cash deposit (cash + checks); secure in safe | Cashier | Store Manager | 10 min |
| 6 | Log out of POS; shut down terminals | Cashier | Store Manager | 5 min |
| 7 | Store Manager reviews daily sales summary on dashboard | Store Manager | Store Manager | 10 min |
| 8 | Complete daily checklist (safety, cleanliness, equipment) | Maintenance/Utility | Store Manager | 15 min |
| 9 | Arm alarm; lock up | Store Manager | Store Manager | 5 min |

**Total closing time**: ~60 minutes

### System Touchpoints
- POS cash float management and tracking (W5a.4)
- POS terminals boot in offline-ready mode; product master and price file cached locally via nightly sync so selling can continue without network (W5a.3, W5a.5)
- Real-time price and promo sync (W5a.5)
- Barcode scanning, multi-tender, loyalty at POS (W5b.4–9)
- BIR-registered receipt format: receipts printed on BIR-authorized thermal paper with TIN, registered invoice number, and compliant layout (W5b.8)
- Customer-facing display (pole display or second screen) showing scanned items, running total, and payment amount during checkout (W5b.4–7)
- Price override with manager authorization threshold and audit trail (W5b.4a)
- Lot/batch capture at POS for lot-tracked items: system prompts for batch number, auto-extracts from GS1-128/2D barcode, records batch against transaction line for forward traceability (W5b.4b)
- Catch-weight / variable measure selling with weight/length capture and auto-price calculation (W5b.2)
- Custom SKU generation for paint mixing (W5b.3)
- Age-restricted product prompts (W5b.9)
- Void transaction with manager authorization: full audit trail (cashier, manager, reason, timestamp); automatic reversal of inventory, payment, loyalty points, and promo usage; voided transaction retained for loss prevention analysis (W5b.10)
- Z-report generation (W5c.2)
- Cash reconciliation / variance reporting (W5c.3–4)
- Electronic payment reconciliation: automated import of card acquirer and e-wallet settlement reports; comparison to Z-report by tender type; variance alerting (W5c.3a–b)
- Daily sales dashboard (W5c.7)

### Staffing Implication
- **6 Cashiers per store**: 5 terminals + 1 float. With 2 shifts (~10 hours total), each shift needs 3–4 cashiers. 6 covers shifts + days off with 1 relief. Tight but workable.
- **16 Sales Associates**: Across 4 departments (Lumber, Plumbing/Electrical, Tiles, Tools/Hardware) = 4 per dept. 2 shifts. Handles floor coverage + specialty tasks (paint mixing, lumber cutting). Reasonable.
- **3 Stock Associates**: Continuous replenishment + cycle counting. With ~700 SKUs to cycle count daily and ongoing shelf restocking, 3 is the minimum. Consider 4 during peak seasons.

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

### Staffing Implication
- **3 Stock Associates per store**: Each counts ~233 SKUs/day (~40 min), with remainder of time on replenishment, receiving, damage reporting, and BOPIS picking. Current count of 3 is adequate but has no slack for absenteeism.

---

## W7. Accounts Payable — Vendor Invoice Processing

| Field | Detail |
|---|---|
| **Trigger** | Vendor invoice received (email, mail, or vendor portal) |
| **Frequency** | ~6,500 invoices/month |
| **Volume** | ~217 invoices/day; peaks at month-end (+50%) |
| **Owner** | AP Supervisor |
| **Participants** | AP Clerk, Buyer (for discrepancies), Treasury (for payment), AP Supervisor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | AP Clerk receives and scans/logs vendor invoice (via email, mail, or vendor portal submission) | AP Clerk | AP Supervisor | 5 min/invoice |
| 2 | System attempts auto-match: PO → Goods Receipt → Invoice (3-way match) | System | — | Automated |
| 3 | If matched (quantities and price within tolerance): auto-approve for payment | System | AP Supervisor | Automated |
| 4 | If mismatch (price, quantity, or missing GR): route to AP Clerk for review | AP Clerk | AP Supervisor | 10 min/invoice |
| 5 | If price discrepancy: AP Clerk contacts Buyer for resolution | AP Clerk | Buyer | 15 min/invoice |
| 6 | If quantity discrepancy (partial receipt): verify GR status; wait for remaining delivery or adjust | AP Clerk | AP Supervisor | 10 min/invoice |
| 6a | Exception SLA: all unmatched invoices must be resolved within 5 business days; system tracks aging of exceptions | System | AP Supervisor | Automated |
| 6b | If exception unresolved after 5 days: system escalates to AP Supervisor; AP Supervisor coordinates with Buyer and vendor for resolution | AP Supervisor | Controller | 15 min/invoice |
| 7 | Approved invoices queued for payment per vendor terms (Net 30, Net 60) | System | — | Automated |
| 7a | System identifies invoices eligible for early payment discount (e.g., 2/10 Net 30); displays discount amount, discount deadline, and annualized return on taking discount; Treasury Analyst includes discount opportunities in weekly cash flow planning (W30 step 8); AP Supervisor prioritizes discounted invoices in payment run when Treasury authorizes | System / AP Supervisor | CFO | 15 min/review |
| 8 | AP Supervisor reviews AP aging weekly; prioritize payments by due date and vendor relationship | AP Supervisor | CFO | 2 hours/week |
| 9 | Twice-weekly payment run: system generates payment file (checks, bank transfers) | AP Clerk | AP Supervisor | 1 hour/run |
| 9a | System calculates Expanded Withholding Tax (EWT) per vendor invoice based on configured Alphanumeric Tax Code (ATC) in vendor master (e.g., WI010 for purchases of goods at 1%, WI020 for services at 2%, WC010 for rentals at 5%); net payment to vendor = invoice amount − EWT; system posts EWT to Withholding Tax Payable (liability); AP Clerk validates EWT computation before payment run | System / AP Clerk | AP Supervisor | Automated + 15 min validation/run |
| 9b | Vendor credit memo processing: AP Clerk receives vendor credit note (mail, email, portal); selects source — RTV reference (W3.6a), rebate settlement (W27.9), price protection (W40.11), or manual entry; system attempts auto-match to original PO/invoice/RTV; AP Clerk posts credit memo: system reduces vendor balance and posts to GL (Dr. Accounts Payable / Cr. COGS or appropriate expense); if vendor has open invoices, system applies credit memo against oldest open invoice; if net vendor credit balance results, AP Clerk decides to request refund, apply to next invoice, or offset | AP Clerk | AP Supervisor | 10 min/credit memo |
| 10 | Treasury reviews and approves payment batch; transmits to bank | Treasury Analyst | CFO | 30 min/run |
| 11 | System posts payment; updates vendor balance | System | — | Automated |

**Match rate target**: ≥ 80% auto-matched (no manual intervention)

### System Touchpoints
- Invoice scanning / OCR / digital capture from email, mail, or vendor portal (W7.1)
- 3-way match engine (PO → GR → Invoice) (W7.2)
- Auto-approval with tolerance thresholds (W7.3)
- Exception routing and workflow (W7.4–6)
- Exception aging tracker with SLA enforcement and auto-escalation at day 5 (W7.6a–b)
- Early payment discount detection: system identifies invoices eligible for discount, calculates annualized ROI, and highlights during payment run (W7.7a)
- AP aging report (W7.8)
- Payment file generation (bank formats) (W7.9–10)
- Expanded Withholding Tax (EWT): auto-computation per ATC in vendor master, net payment calculation (invoice − EWT), EWT Payable tracking, BIR 1601-E file generation (W7.9a)
- Vendor credit memo processing: credit note entry with source reference (RTV, rebate, price protection), auto-matching to original transactions, automatic application to open invoices, credit balance management (W7.9b)
- Non-PO / recurring expense invoice processing: 2-way match (invoice vs. contract or budget), store manager / department head approval routing, cost center allocation, utility and service bill capture (W7c.1–6)
- Shelf-life / expiry date management: capture manufacturing date and shelf-life at GR for date-sensitive items; system tracks expiry per batch; FEFO (First Expired First Out) pick direction in DC; alerting for near-expiry items; periodic expiry review feeds into slow-mover disposition (W3, W4, W6)

### Staffing Implication
- **8–10 AP Clerks**: 217 invoices/day × 5 min (logging) = ~18 hours for basic processing. With ~20% requiring manual resolution at 25 min each = ~20 additional hours. Total ~38 hours/day. With 8 clerks that's ~5 hours each. Reasonable with payment runs and other duties.
- **1 AP Supervisor**: Oversight, aging review, escalations.
- **2 Treasury Analysts**: Payment approval, bank file transmission, LC management. Shared with AR and other treasury duties.

### W7c. Non-PO / Recurring Expense Invoice Processing

| Field | Detail |
|---|---|
| **Trigger** | Utility bill, service invoice, rent, or other recurring expense received without a Purchase Order |
| **Frequency** | ~2,000–3,000 non-PO invoices/month across all locations (200 stores + 5 DCs + HQ) |
| **Volume** | ~10–15 recurring vendor invoices per store per month (electricity, water, internet, rent to Property Mgmt Inc., security, cleaning, waste disposal) |
| **Owner** | AP Supervisor |
| **Participants** | AP Clerk, Store Manager / Department Head (approval), AP Supervisor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | AP Clerk receives and logs non-PO invoice (utility bill, service invoice, lease payment); classifies as recurring or one-time | AP Clerk | AP Supervisor | 5 min/invoice |
| 2 | System attempts 2-way match: invoice amount vs. contract amount or budget allocation per cost center | System | — | Automated |
| 3 | If invoice within tolerance of contract/budget: route to cost center owner for approval (Store Manager for store expenses, Department Head for HQ expenses) | System | Cost center owner | 1 min/auto-approved |
| 4 | If invoice exceeds budget or no contract on file: route to cost center owner for review with explanation of variance | AP Clerk / Cost center owner | AP Supervisor | 5 min/invoice |
| 5 | Approved non-PO invoices queued for payment in standard payment run (W7.9–11); EWT computed per ATC for service invoices (W7.9a) | System | AP Supervisor | Automated |
| 6 | Monthly: AP Supervisor reviews non-PO expense summary by cost center; flags locations with unusual expense patterns for management review | AP Supervisor | Controller | 1 hour/month |

**Match rate target**: ≥ 70% auto-matched for recurring expenses (contract-based)

---

## W8. Accounts Receivable — Trade & Corporate Accounts

| Field | Detail |
|---|---|
| **Trigger** | Sales invoice generated for trade/corporate account at POS or by Sales Rep |
| **Frequency** | ~3,500 AR invoices/month |
| **Volume** | ~117 invoices/day; ~5,200 active AR accounts |
| **Owner** | AR Supervisor |
| **Participants** | AR Clerk, Sales Rep (trade accounts), AR Supervisor, Finance Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer purchase on trade/corporate account; invoice created at POS or by Sales Rep | Cashier / Sales Rep | Department Supervisor | Part of sale |
| 2 | System posts AR invoice; updates customer balance | System | — | Automated |
| 3 | System checks customer credit limit; blocks further sales if exceeded | System | AR Supervisor | Automated |
| 3a | Credit hold override: if sales rep or Store Manager requests sale despite credit block, system prompts for authorizer and reason; override requires AR Supervisor approval for up to 110% of credit limit, Finance Manager approval for up to 130%; override logged with customer ID, authorizer, overridden amount, reason, and 24-hour validity; system counts overridden amount against credit exposure for monitoring | Sales Rep / AR Supervisor / Finance Manager | Finance Manager | 5 min/override |
| 4 | AR Clerk sends monthly statement to each active account (1st of month) | AR Clerk | AR Supervisor | 4 hours/month (batch) |
| 5 | AR Clerk reviews aging report weekly; flags accounts > 30 days past due | AR Clerk | AR Supervisor | 1 hour/week |
| 6 | For 30-day overdue: AR Clerk contacts customer (phone/email) for follow-up | AR Clerk | AR Supervisor | 15 min/account |
| 7 | For 60-day overdue: escalate to Sales Rep for relationship-based collection | Sales Rep | AR Supervisor | 15 min/account |
| 8 | For 90-day overdue: escalate to Finance Manager; consider credit hold | Finance Manager | CFO | 30 min/account |
| 9 | Customer payment received; AR Clerk applies payment to open invoices | AR Clerk | AR Supervisor | 5 min/payment |
| 10 | Monthly reconciliation of AR sub-ledger to GL | AR Clerk | AR Supervisor | 2 hours/month |

### System Touchpoints
- AR invoice creation from POS/sales order (W8.1–2)
- Real-time credit limit check (W8.3)
- Credit hold override with tiered authorization, audit trail, and automatic expiry (W8.3a)
- Aging report generation (W8.5)
- Customer statement generation (W8.4)
- Payment application and matching (W8.9)
- AR sub-ledger to GL reconciliation (W8.10)

### Staffing Implication
- **3–4 AR Clerks**: 117 invoices/day is relatively low volume (retail is mostly cash/card). Main workload is collections on ~5,200 accounts. At any time, ~15% (780) may need follow-up. 3 clerks can manage with monthly statement runs and weekly aging reviews.
- **1 AR Supervisor**: Oversight and escalation handling.

---

## W9. Financial Close & Reporting

### W9a. Month-End Close

| Field | Detail |
|---|---|
| **Trigger** | Last calendar day of the month |
| **Frequency** | Monthly |
| **Volume** | 5 entities × 12 months = 60 entity-month closes/year |
| **Owner** | Chief Accountant / Controller |
| **Participants** | Chief Accountant, AP Supervisor, AR Supervisor, Treasury Analyst, Tax Accountant, Cost Accountant, CFO |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Verify all store day-end closings are posted; follow up on any outstanding | Chief Accountant | Controller | 2 hours |
| 2 | AP: Ensure all vendor invoices received before cut-off are entered and matched | AP Supervisor | Controller | 2 hours |
| 2a | GRNI reconciliation: system generates Goods Received Not Invoiced report showing all GRs without matching AP invoices; Finance verifies completeness; if system uses GR/IR clearing account, verify clearing account balance reconciles to open GRNI list; accrue provision for estimated costs where invoices are expected but not yet received | AP Supervisor / Chief Accountant | Controller | 1 hour |
| 3 | AR: Post all AR invoices and payments received through month-end | AR Clerk | Controller | 1 hour |
| 4 | Accruals: Book accrual entries for expenses incurred but not yet invoiced (utilities, freight, rent) | Chief Accountant | Controller | 3 hours |
| 5 | Intercompany: Verify all IC transactions are posted; run IC matching | Chief Accountant | Controller | 2 hours |
| 5a | FX Revaluation: System revalues all open foreign-currency AP and AR balances at month-end BIR exchange rate; posts unrealized FX gain/loss to P&L and FX revaluation reserve to BS; auto-reverses the revaluation entries at start of next period | System / Chief Accountant | Controller | Automated + 30 min review |
| 6 | Inventory: Run monthly inventory valuation (WAC); post any adjustments from cycle counts | Cost Accountant | Controller | 2 hours |
| 7 | Fixed Assets: Post monthly depreciation | Cost Accountant | Controller | 30 min |
| 8 | Prepayments: Amortize prepaid expenses (insurance, rent) | Chief Accountant | Controller | 30 min |
| 9 | Bank reconciliation: Match bank statements to GL cash accounts (all bank accounts, all entities) | Treasury Analyst | Controller | 3 hours |
| 10 | Run trial balance per entity; review for unusual balances | Chief Accountant | Controller | 1 hour |
| 11 | Post adjusting entries as needed | Chief Accountant | Controller | 1 hour |
| 12 | Generate preliminary financial statements per entity (BS, IS, CF) | System / Chief Accountant | Controller | 30 min |
| 13 | Run intercompany elimination entries for consolidation | Chief Accountant | CFO | 1 hour |
| 14 | Generate consolidated financial statements (5 entities) | System / Chief Accountant | CFO | 30 min |
| 15 | CFO reviews consolidated statements; queries variances | CFO | CFO | 1 hour |
| 16 | Tax Accountant prepares VAT return (BIR 2550M) and withholding tax returns (1601-E, 1601-C) | Tax Accountant | CFO | 3 hours |
| 16a | EWT remittance: Tax Accountant generates EWT remittance file (BIR 1601-E) from accumulated Withholding Tax Payable per vendor per ATC; reconciles to vendor remittance list; transmits to BIR via eFPS; system posts remittance (Dr. Withholding Tax Payable / Cr. Cash) | Tax Accountant | CFO | 1 hour |
| 16b | Inventory net realizable value (NRV) review: Cost Accountant runs inventory aging report (days since last sale); for slow-moving items (> 180 days), system compares WAC to estimated NRV (clearance price × sell-through probability); Cost Accountant proposes write-down per SKU where NRV < cost; Controller approves write-downs > PHP 50,000; system posts Dr. Inventory Write-Down Expense / Cr. Inventory Provision (contra-asset); if item later sells above written-down value, system reverses provision on sale | Cost Accountant / Controller | Controller | 2 hours |
| 17 | Final close: lock period in system | Controller | CFO | 15 min |

**Target**: Close within 5 working days of month-end

### W9b. Year-End Close

Additional steps on top of month-end close (December):

| # | Activity | Role (R) | Duration |
|---|---|---|---|
| 18 | 13th month pay accrual reconciliation | Payroll Accountant | 2 hours |
| 19 | Physical inventory (wall-to-wall) count and adjustment | Cost Accountant + all store staff | 1–2 days |
| 20 | Year-end tax provisions and adjustments | Tax Accountant | 4 hours |
| 21 | Annual income tax return preparation (BIR 1702RT) | Tax Accountant | 1 week |
| 22 | External audit preparation and coordination | Controller + CFO | Ongoing (Q1) |
| 23 | SEC annual report preparation | Controller | 1 week |

### System Touchpoints
- Store day-end posting monitoring (W9a.1)
- GRNI reconciliation report and clearing account balance verification (W9a.2a)
- Accrual and journal entry workflow (W9a.4–8, 11)
- IC matching and elimination automation (W9a.5, 13)
- Inventory valuation engine (W9a.6)
- Bank reconciliation (W9a.9)
- Multi-entity financial statement generation (W9a.12–14)
- Period lock / close controls (W9a.17)
- BIR tax form generation (W9a.16)
- EWT remittance file generation per BIR 1601-E with per-vendor per-ATC breakdown; eFPS transmission (W9a.16a)
- Inventory NRV review: aging by days-since-last-sale, NRV calculator, write-down journal entry with approval, provision reversal on subsequent sale (W9a.16b)

### Staffing Implication
- **Controller**: Owns the close process. 1 person sufficient with support.
- **1 Chief Accountant**: Handles most close entries. Stretched during close week (~30 hours of close work in 5 days).
- **1 Cost Accountant**: Inventory valuation + fixed assets.
- **1 Tax Accountant**: VAT + withholding monthly; income tax quarterly/annual.
- **Total Finance team (~35)**: During close week, 8–10 people are heavily involved. The rest of the month is lighter. Current headcount supports this.

---

## W10. Payroll Processing

| Field | Detail |
|---|---|
| **Trigger** | Semi-monthly payroll calendar (14th and 28th/30th) |
| **Frequency** | 10 payroll runs/month (5 entities × 2) |
| **Volume** | ~8,050 employees total |
| **Owner** | Payroll Manager |
| **Participants** | Payroll Officer, HR Assistant, Department Heads (OT/leave approval), Finance (bank file) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Payroll Officer pulls time & attendance data from biometric/RFID system | Payroll Officer | Payroll Manager | 30 min/run |
| 2 | HR Assistant verifies approved leaves, overtime, and schedule adjustments are posted | HR Assistant | Payroll Manager | 2 hours/run |
| 3 | Payroll Officer validates: basic salary + OT + night differential + holiday pay + allowances | Payroll Officer | Payroll Manager | 1 hour/run |
| 4 | System calculates deductions: SSS, PhilHealth, Pag-IBIG, withholding tax (TRAIN law), loans, advances | System | — | Automated |
| 5 | Payroll Officer reviews computed payroll for anomalies (negative net pay, unusually high OT) | Payroll Officer | Payroll Manager | 1 hour/run |
| 6 | Payroll Manager reviews and approves payroll register | Payroll Manager | CHRO | 30 min/run |
| 7 | System generates bank file for payroll crediting (BDO, BPI, etc.) | System | — | Automated |
| 8 | Finance/Treasury reviews bank file; transmits to bank | Treasury Analyst | CFO | 30 min/run |
| 9 | System posts payroll journal entries to GL (salary expense, payable, deductions) | System | — | Automated |
| 10 | Payslips generated; distributed via email or employee self-service portal | System | — | Automated |
| 11 | Monthly: generate SSS PRN, PhilHealth contribution, Pag-IBIG contribution files for remittance | Payroll Officer | Payroll Manager | 1 hour/month |
| 11a | Payroll Officer reconciles statutory contribution schedule (per-employee breakdown) to generated remittance file and bank payment confirmation; investigates and resolves discrepancies before remittance deadline; system flags employees with missing or incomplete statutory data | Payroll Officer | Payroll Manager | 30 min/month |
| 11b | Contractual / fixed-term workers: system tracks contract start/end dates and auto-alerts HR Assistant 30 days before expiry; payroll computes pro-rated 13th month pay and statutory benefits per contract duration; end-of-contract settlement computed similar to final pay (W10 step 12) but with different legal basis; if employee converts to regular status, HR Assistant updates employee type in system and payroll adjusts benefit computation accordingly | HR Assistant / Payroll Officer | Payroll Manager | 15 min/employee |
| 12 | Final pay computation (upon employee separation): system calculates pro-rated 13th month pay, converted unused leave credits, less outstanding loans/advances and clearance deductions | Payroll Officer | Payroll Manager | 30 min/employee |
| 13 | System posts final pay as separate payroll run or adjustment; generates final payslip | System | — | Automated |

**Total payroll processing time**: ~6 hours per run per entity. With 5 entities, can be parallelized across 2–3 payroll officers.

### System Touchpoints
- Time & attendance import from biometric system (W10.1)
- Leave and overtime approval workflow (W10.2)
- Philippine payroll computation engine (TRAIN law, SSS, PhilHealth, Pag-IBIG tables) (W10.3–4)
- Payroll anomaly detection (W10.5)
- Bank file generation in Philippine bank formats (W10.7)
- GL posting from payroll (W10.9)
- Payslip distribution (W10.10)
- Statutory contribution file generation with PRN (W10.11)
- Statutory remittance reconciliation: per-employee contribution schedule vs. remittance file vs. bank confirmation; discrepancy flagging (W10.11a)
- Contractual/fixed-term worker management: contract date tracking, pro-rated benefit computation, end-of-contract settlement, regularization conversion (W10.11b)

### Staffing Implication
- **2–3 Payroll Officers**: 5 entities × 2 runs = 10 runs/month. Each run takes ~6 hours. Total ~60 hours/month of payroll processing. 2 officers can handle this with time for reconciliation and inquiries.
- **1 Payroll Manager**: Approval, oversight, statutory compliance.
- **1–2 HR Assistants**: Leave and OT verification (data entry-heavy during payroll week).
- Fits within the ~15-person HR team.

---

## W11. Ecommerce — BOPIS Order Fulfillment

| Field | Detail |
|---|---|
| **Trigger** | Customer places BOPIS order on website/app |
| **Frequency** | ~25,700 BOPIS orders/month; ~857/day |
| **Volume** | Avg 3–4 items per order |
| **Owner** | Customer Service Rep (in-store) |
| **Participants** | System (order routing), Stock Associate (picker), Customer Service Rep (handoff), Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer places order on website/app; selects pickup store; pays online | Customer | — | — |
| 2 | System routes order to selected store; creates store pick list | System | — | Automated |
| 3 | Store receives notification (tablet/terminal alert + printed pick list) | System | — | Automated |
| 4 | Stock Associate picks items from sales floor or backroom; scans each item to confirm | Stock Associate | Dept. Supervisor | 5–15 min/order |
| 5 | If item not in stock at store: system offers substitution or cancels line; notifies customer | System / CSR | Store Manager | 3 min |
| 6 | Stock Associate stages picked items at Customer Service counter | Stock Associate | CSR | 2 min |
| 7 | System marks order as "Ready for Pickup"; sends SMS/email to customer | System | — | Automated |
| 8 | Customer arrives at Customer Service counter; presents ID and order number | Customer | — | — |
| 9 | Customer Service Rep verifies ID; scans order; releases items | CSR | Store Manager | 3 min |
| 10 | System marks order as "Completed"; inventory deducted | System | — | Automated |
| 11 | If not picked up within 5 days: auto-cancel; refund initiated; items returned to shelf | System | CSR | Automated (return: 5 min) |

**Pick SLA**: Ready within 4 hours of order placement

### System Touchpoints
- Real-time inventory availability per store on website (W11.1)
- Available-to-Promise (ATP) reservation at order placement: system deducts from available inventory (not physical) at the fulfillment location; ATP = on-hand − allocated to open orders − safety stock buffer; if ATP = 0, item shown as "unavailable" on website for that location (W11.1)
- ATP reservation held until pick confirmation (hard commitment) or order cancellation; BOPIS reservation auto-releases after 5-day hold period if not picked up (W11.11)
- Order routing to store with pick list generation (W11.2–3)
- In-store pick confirmation via scanning (W11.4)
- Out-of-stock substitution/cancellation handling (W11.5)
- Customer notification (SMS/email) (W11.7)
- Order handoff verification with ID check (W11.9)
- Auto-cancel and refund after hold period (W11.11)

### Staffing Implication
- **1 CSR per store**: 857 BOPIS orders/day ÷ 200 stores = ~4 BOPIS orders/store/day. At ~10 min per order (pick + handoff), that's ~40 min/day. The CSR also handles returns and special orders, so 1 per store is adequate. Current headcount (1 CSR/store) works.
- **Stock Associates absorb picking**: ~4 BOPIS picks/day is minimal additional load for 3 stock associates already doing replenishment and cycle counts.

---

## W12. Returns & Exchanges

### W12a. In-Store Returns

| Field | Detail |
|---|---|
| **Trigger** | Customer brings item to Customer Service counter for return/exchange |
| **Frequency** | ~2% of POS transactions = ~280 returns/day chain-wide; ~1.4 per store/day |
| **Volume** | ~56,000 returns/month chain-wide |
| **Owner** | Customer Service Rep |
| **Participants** | CSR, Store Manager (approval for high-value or no-receipt returns), Stock Associate (restock) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer presents item and receipt (or provides transaction details) at CSR counter | Customer | — | — |
| 2 | CSR looks up original transaction in system by receipt number or loyalty card | CSR | — | 2 min |
| 3 | CSR inspects item condition (resalable, damaged, defective) | CSR | — | 2 min |
| 4 | If return within policy and with receipt: CSR processes return in system | CSR | Store Manager | 3 min |
| 5 | If no receipt or outside standard policy: escalate to Store Manager for approval | Store Manager | Store Manager | 5 min |
| 6 | System processes refund (original tender method) or issues store credit; for split-tender transactions (e.g., customer paid PHP 1,000 cash + PHP 800 credit card): system refunds pro-rata to each original tender method in proportion to the amount paid via each method; if cash refund would exceed store cash availability threshold, system defaults to card or e-wallet refund for the excess portion; Store Manager can override with authorization | System / CSR | — | 2 min |
| 7 | Inventory returned to stock (if resalable) or flagged as damaged/defective | Stock Associate | Dept. Supervisor | 5 min |
| 8 | Defective items flagged for Return to Vendor (RTV) process | CSR | Dept. Supervisor | 2 min |

### W12b. Online-Initiated Returns

| Field | Detail |
|---|---|
| **Trigger** | Customer initiates return on website/app |
| **Frequency** | ~5% of ecommerce orders = ~2,250/month |
| **Owner** | Customer Service Rep (receiving store) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer submits return request on website with reason and photos | Customer | — | — |
| 2 | System sends return authorization with QR code; customer selects drop-off store | System | — | Automated |
| 3 | Customer brings item to store CSR counter | Customer | — | — |
| 4 | CSR scans QR code; verifies item condition matches return reason | CSR | Store Manager | 3 min |
| 5 | CSR accepts return; system processes refund to original payment method | CSR | — | 3 min |
| 6 | Inventory returned to stock or flagged as damaged | Stock Associate | Dept. Supervisor | 5 min |

### System Touchpoints
- Transaction lookup by receipt number / loyalty card (W12a.2)
- Return policy enforcement (time window, condition rules) (W12a.4)
- Manager override for policy exceptions (W12a.5)
- Refund processing to original tender (W12a.6)
- Inventory status change (saleable vs. damaged) (W12a.7)
- RTV tracking (W12a.8)
- Online return initiation with QR authorization (W12b.2)
- Split-tender refund processing: pro-rata refund to each original tender method; cash availability threshold enforcement with automatic redirect to card/e-wallet for excess (W12a.6)

### Staffing Implication
- Returns add ~15 min/day to CSR workload (1.4 in-store + ~0.5 online returns per store). Minimal impact on current headcount.

---

## W13. Promotions & Pricing Execution

| Field | Detail |
|---|---|
| **Trigger** | Promotional calendar (6 bi-monthly events + monthly hot deals) |
| **Frequency** | 6 major promos/year + 12 monthly hot deal cycles |
| **Volume** | ~200–500 SKUs per major promo; 10–20 SKUs per monthly hot deals |
| **Owner** | Pricing Analyst |
| **Participants** | Category Manager, Pricing Analyst, Marketing, Store Operations, IT |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Category Manager defines promo mechanics (percentage off, bundle price, buy-X-get-Y) | Category Manager | VP Merchandising | Per promo event |
| 2 | Pricing Analyst sets up promotional prices in system with effective dates | Pricing Analyst | Category Manager | 2–4 hours/promo |
| 3 | VP Merchandising approves promo pricing | VP Merchandising | VP Merchandising | 30 min review |
| 4 | Marketing creates promotional materials (shelf tags, POS materials, digital banners) | Marketing | CMO | 1–2 weeks lead time |
| 5 | System pushes promo prices to all POS terminals before promo start date | System | — | Automated (scheduled) |
| 6 | Store Operations coordinates shelf tag updates across stores | Regional Manager | COO | 1–2 days before promo |
| 7 | During promo: system auto-applies promotional pricing at POS (no cashier action) | System | — | Automated |
| 8 | Pricing Analyst monitors promo performance daily (sell-through, margin impact) | Pricing Analyst | Category Manager | 30 min/day during promo |
| 9 | After promo: system automatically reverts to regular price; flags unsold promo stock for clearance | System | — | Automated |
| 9a | **Clearance / Markdown Execution**: Pricing Analyst sets clearance price for flagged items (target: recover cost or minimize loss); system applies clearance flag and price at POS; POS displays clearance disclaimer ("Clearance — Final Sale — No Returns"); Department Supervisors move clearance items to designated clearance section or mark with red tags; clearance period typically 2–4 weeks | Pricing Analyst / Dept. Supervisor | Category Manager | 1–2 hours/promo |
| 9b | Post-clearance: unsold items dispositioned per policy — (a) bulk liquidation to discount buyers, (b) donation to partner organizations, (c) scrap/recycle; system removes remaining clearance inventory and posts final loss | Buyer / Dept. Supervisor | Category Manager | 1 hour |
| 10 | Pricing Analyst generates post-promo analysis (lift, cannibalization, margin erosion, clearance recovery rate) | Pricing Analyst | Category Manager | 2 hours/promo |

### System Touchpoints
- Promotional price setup with date-effective pricing (W13.2)
- Approval workflow for promotional prices (W13.3)
- Scheduled push of promo prices to POS (W13.5)
- Auto-application at POS without cashier intervention (W13.7)
- Real-time promo performance dashboard (W13.8)
- Automatic price reversion and clearance flagging (W13.9)
- Post-promo analysis reporting (W13.10)
- Clearance pricing with POS flag and disclaimer enforcement (W13.9a)
- Post-clearance inventory disposition tracking (W13.9b)
- Digital coupon / online promo code management: creation of coupon codes with validity dates, usage limits, and channel restrictions (in-store, online, or both); redemption tracking across channels; synchronization with ecommerce platform (W13.2, W13.5)
- Pricing conflict resolution rules: (1) If a regular price change (W40) occurs during an active promotion, the promo price is NOT automatically adjusted — promo overrides regular price for the promo period. (2) If a new promotion starts and the regular price has changed since the promo was set up, the system alerts the Pricing Analyst to recalculate the promo price from the new base. (3) If two promotions overlap for the same SKU, system applies the lower price (customer-friendly) and alerts Pricing Analyst to investigate. (4) Post-promotion: system reverts to the CURRENT regular price, not the price active when the promo was created

### Staffing Implication
- **3 Pricing Analysts**: 6 major promos + 12 monthly cycles = ~18 events/year. Each event requires ~6–8 hours of setup + 30 min/day monitoring during the promo period + 2 hours post-analysis. With staggered events, 3 analysts can handle this alongside regular price maintenance.

---

## W14. Intercompany Transactions & Settlement

| Field | Detail |
|---|---|
| **Trigger** | Ongoing business operations between the 5 legal entities |
| **Frequency** | Monthly processing and settlement |
| **Volume** | ~100–200 IC transactions/month |
| **Owner** | Chief Accountant |
| **Participants** | Chief Accountant, AP/AR Clerks, Treasury, CFO |

### Intercompany Flows

| Flow | From → To | Nature | Frequency |
|---|---|---|---|
| Store rent | Depot Inc. → Property Mgmt Inc. | Monthly lease payments | Monthly |
| DC warehousing fees | Depot Inc. → Logistics Inc. | Storage and distribution fees | Monthly |
| Ecommerce fulfillment | Digital Commerce Inc. → Depot Inc. (BOPIS) or Logistics Inc. (delivery) | Fulfillment fees per order | Monthly |
| Ecommerce payment collection | Digital Commerce Inc. → Depot Inc. | Remittance of in-store BOPIS revenue | Monthly |
| Management fees | All subsidiaries → Holdings Inc. | Corporate overhead allocation | Monthly |
| Intercompany loans | Holdings → subsidiaries as needed | Cash advances / funding | As needed |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System auto-generates IC invoices based on configured transfer pricing rules | System | Chief Accountant | Automated |
| 2 | Chief Accountant reviews IC invoice batch for accuracy | Chief Accountant | Controller | 1 hour/month |
| 3 | System posts IC AP in buying entity and IC AR in selling entity simultaneously | System | — | Automated |
| 4 | Monthly: run IC reconciliation report — verify balances match across all entity pairs | Chief Accountant | Controller | 2 hours/month |
| 5 | Resolve any IC mismatches (timing differences, missing entries) | Chief Accountant | Controller | 1 hour/month |
| 6 | Prepare net settlement schedule (offset IC balances; only net amounts paid) | Chief Accountant | CFO | 1 hour/month |
| 7 | CFO approves IC settlement; Treasury executes bank transfers | Treasury Analyst | CFO | 30 min/month |
| 8 | At month-end close: system runs IC elimination entries for consolidation | System | — | Automated |
| 9 | Verify consolidation eliminates all IC revenue, expense, AP, AR | Chief Accountant | CFO | 1 hour/month |

### System Touchpoints
- Automated IC invoice generation with transfer pricing rules (W14.1)
- Simultaneous IC AP/AR posting across entities (W14.3)
- IC reconciliation report across entity pairs (W14.4)
- IC elimination automation during consolidation (W14.8)
- Consolidated financial statement generation with IC lines eliminated (W14.9)
- Transfer pricing rule maintenance with annual review documentation per BIR RR 19-2020 (W14.1)

### Annual IC Transfer Pricing Review

| Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|
| CFO and Controller review all IC pricing schedules (store rent, DC fees, ecommerce fulfillment, management fees, IC loans, ecommerce payment collection) against market benchmarks and arm's-length principles | CFO + Controller | CEO | Annually (during budget cycle, W26) |
| Update transfer pricing rules in system for new fiscal year; prepare and store transfer pricing documentation per BIR RR 19-2020 requirements | Controller | CFO | Annually |
| CFO approves updated IC pricing; system updates IC invoice generation rules effective new fiscal year | CFO | CEO | Annually |

### Staffing Implication
- IC processing adds ~6–8 hours/month to the Chief Accountant's workload. No dedicated IC clerk needed — it's absorbed into the month-end close cycle within the current ~35-person Finance team.

---

## W15. Recruitment & Employee Onboarding

| Field | Detail |
|---|---|
| **Trigger** | Vacancy created (resignation, new position, new store opening) |
| **Frequency** | ~100–130 hires/month (1,200–1,600/year including turnover + growth) |
| **Volume** | Peaks during new store openings (35 hires per new store) |
| **Owner** | HR Recruitment Officer |
| **Participants** | Recruitment Officer, HR Assistant, Hiring Manager, HR Head |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Hiring Manager submits staffing request with role, department, justification | Hiring Manager | Dept. Head | 15 min |
| 2 | HR Recruitment Officer posts job on job boards, social media, walk-in postings | Recruitment Officer | HR Head | 30 min/role |
| 3 | Screen applications; shortlist candidates | Recruitment Officer | HR Head | 2–4 hours/role |
| 4 | Conduct interviews (1st: HR; 2nd: Hiring Manager) | Recruitment Officer + Hiring Manager | Dept. Head | 1 hour/candidate |
| 5 | Select candidate; extend offer | Recruitment Officer | HR Head | 30 min |
| 6 | New hire completes pre-employment requirements (SSS, PhilHealth, Pag-IBIG, TIN, medical, NBI clearance) | New Hire | Recruitment Officer | — |
| 7 | HR Assistant creates employee record in system (personal info, position, salary, entity, tax status); employee type classified as regular, probationary, fixed-term, or project-based with contract start/end dates for non-regular employees | HR Assistant | HR Head | 30 min |
| 8 | System generates employee ID; enrolls in payroll with correct statutory deductions | System | — | Automated |
| 9 | Assign biometric/RFID credentials for time & attendance | HR Assistant | — | 10 min |
| 10 | Onboarding: safety orientation, company policies, POS/system training | Dept. Supervisor + HR | Hiring Manager | 2–3 days |
| 11 | First payroll: system computes pro-rated salary for partial month | System | — | Automated |

### Staffing Implication
- **1–2 Recruitment Officers**: 100–130 hires/month. Each hire takes ~4–6 hours of HR time (screening + interview + paperwork). With 2 recruiters: ~60 hires each/month × 5 hours = 300 hours ÷ 160 working hours/month = ~2 recruiters at near-full capacity. 2 is appropriate.
- **2 HR Assistants**: Employee record creation, credentials, onboarding logistics. 130 hires × 1 hour admin each = 130 hours/month. 2 assistants can handle alongside other HR admin.

---

## W16. New Store Opening

| Field | Detail |
|---|---|
| **Trigger** | Board approval of new store location |
| **Frequency** | ~10–15 new stores/year |
| **Volume** | 1 store at a time; each takes 3–6 months from approval to opening |
| **Owner** | Store Operations Director |
| **Participants** | COO, Store Ops Director, Real Estate, IT, Merchandising, HR, Supply Chain, Marketing |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Real Estate secures lease; negotiates terms with landlord | Property Mgmt Inc. | COO | 1–2 months |
| 2 | Store fit-out: layout design, shelving, signage, POS cabling, paint | Store Ops + Contractor | COO | 2–3 months |
| 3 | IT installs connectivity (fiber/LTE), POS terminals, network equipment | IT Team | CIO | 1–2 weeks |
| 4 | IT configures store location in ERP system (location master, tax registration, GL segments) | IT Team | CIO | 2–3 days |
| 5 | Merchandising assigns SKU assortment to new store; sets initial order quantities | Category Manager | VP Merchandising | 1 week |
| 6 | Supply Chain plans initial fill: DC generates transfer orders for opening stock | Supply Planner | Supply Chain Manager | 1 week |
| 7 | DC picks, packs, and ships opening inventory to new store | DC Team | DC Manager | 1–2 weeks |
| 8 | HR recruits store staff (~35 people); assigns Store Manager first | Recruitment Officer | CHRO | 4–6 weeks |
| 9 | Store Manager + staff training (POS, processes, safety, product knowledge) | Store Ops + HR | Store Ops Director | 1–2 weeks |
| 9a | IT and Store Ops execute go-live readiness checklist: verify POS terminal connectivity and offline mode, test price file sync, confirm location master and GL segments, validate tax registration per LGU, perform test transaction and void, verify Z-report generation | IT Team + Store Ops Director | CIO | 1–2 days |
| 10 | Receiving and stocking: new team receives goods and merchandises store floor | New Store Staff | Store Manager | 3–5 days |
| 11 | Marketing executes grand opening campaign | Marketing | CMO | 2 weeks (lead) |
| 12 | Soft opening (friends & family, VIP); iron out issues | Store Manager | Store Ops Director | 1–2 days |
| 13 | Grand opening | All | COO | 1 day |

**Total lead time**: 3–6 months from lease signing to opening

### System Touchpoints
- New location creation in location master (W16.4)
- Tax registration per LGU (W16.4)
- SKU assortment assignment per store (W16.5)
- Initial stock transfer order generation (W16.6)
- Employee onboarding batch for ~35 staff (W16.8)
- POS terminal provisioning and store activation (W16.3–4)
- Go-live readiness checklist: automated validation of POS connectivity, price sync, location master, GL segments, tax registration, test transaction, Z-report (W16.9a)
- New store capex project tracking: each store opening tracked as a capex project in the system; all related POs, invoices, and expenses tagged to a project code; Cost Accountant tracks actual vs. budgeted cost per project (construction, fixtures, IT equipment, POS terminals, signage, pre-opening marketing, training, initial staffing); post-opening review (W16 step 13) includes cost variance analysis; project closed and total cost capitalized as fixed assets per W21.7

### Staffing Implication
- New store openings (10–15/year) are the primary growth driver of hiring volume.
- Store Ops Director + 2–3 Regional Managers oversee openings on a rolling basis.
- IT deploys a team of 2–3 for each store setup (~1 week per store).
- Opening 10–15 stores over 12 months = ~1 new store every 3–5 weeks. Manageable with current team structure if staggered.

---

## W17. Customer Loyalty Program Operations

| Field | Detail |
|---|---|
| **Trigger** | Customer transaction (earn) or redemption request (redeem) |
| **Frequency** | Continuous at POS; monthly batch processing |
| **Volume** | ~2.8M POS transactions/month (earn); ~50,000 redemptions/month |
| **Owner** | Marketing — Loyalty Manager |
| **Participants** | Cashier (POS), Loyalty Manager, Customer Service, Marketing |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer signs up for loyalty program (in-store, online, or via app) | Customer / CSR | Loyalty Manager | 3 min (in-store) |
| 2 | System creates loyalty account with tier status (Bronze default); captures data privacy consent flag with purpose, date, and consent version per RA 10173 (Data Privacy Act) | System | — | Automated |
| 3 | At each POS transaction, cashier scans loyalty card or enters mobile number | Cashier | — | 15 sec |
| 4 | System calculates points earned (1 point per PHP 100 spent) and updates balance; per PFRS 15, system allocates transaction revenue between product revenue and loyalty deferred revenue based on relative standalone selling price of points (Dr. Cash or Accounts Receivable / Cr. Revenue for product portion, Cr. Deferred Revenue — Loyalty Points for points portion) | System | — | Automated |
| 5 | Customer checks points balance via app, receipt, or in-store kiosk | Customer | — | Self-service |
| 6 | At checkout, customer requests points redemption; cashier selects redemption option | Cashier | — | 30 sec |
| 7 | System validates sufficient points; converts to peso value; applies as discount; system recognizes deferred revenue proportionally for redeemed points (Dr. Deferred Revenue — Loyalty Points / Cr. Revenue) | System | — | Automated |
| 8 | Monthly: Loyalty Manager reviews tier movement (upgrade/downgrade based on trailing 12-month spend) | System | Loyalty Manager | Automated + 1 hour review |
| 9 | Monthly: generate loyalty program report (enrollment, active rate, points liability, redemption rate) | System | Loyalty Manager | 30 min |
| 10 | Quarterly: Loyalty Manager plans double-points weekends and member-exclusive promos | Loyalty Manager | CMO | 2 hours/quarter |
| 11 | Annual: points expiry batch run (points unused after 24 months expire); system recognizes breakage revenue from expired points (Dr. Deferred Revenue — Loyalty Points / Cr. Revenue) | System | Loyalty Manager | Automated |
| 11a | Monthly: Cost Accountant estimates total loyalty liability (outstanding points × redemption value × expected redemption rate based on trailing 12-month actual redemption data); reconciles to deferred revenue balance on balance sheet; adjusts deferred revenue if estimate differs from recorded balance | Cost Accountant | Controller | 30 min/month |

### System Touchpoints
- Loyalty enrollment (in-store, online, app) (W17.1–2)
- Points earning at POS with real-time update (W17.3–4)
- Points balance inquiry (app, receipt, kiosk) (W17.5)
- Points redemption at POS as payment method (W17.6–7)
- Tier auto-calculation based on trailing spend (W17.8)
- Loyalty analytics dashboard (W17.9)
- Scheduled points expiry with breakage revenue recognition (W17.11)
- Loyalty deferred revenue: allocation at POS earning (PFRS 15), proportional recognition at redemption, breakage recognition at expiry, monthly liability estimation and reconciliation (W17.4, W17.7, W17.11, W17.11a)
- Manual points adjustment: Loyalty Manager (or authorized CSR) initiates adjustment with reason code and supporting documentation (system error, complaint resolution per W41, retroactive earning for missing transaction, dispute resolution); approval required for adjustments above threshold (> 500 points: Loyalty Manager; > 5,000 points: Marketing Head); system logs adjustment with initiator ID, approver ID, reason, and original transaction reference; monthly audit of all adjustments by Loyalty Manager (W17)
- Customer data deduplication: system performs fuzzy-match deduplication at enrollment (blocks creation if > 85% match on name + phone or name + email); Loyalty Manager reviews weekly deduplication queue of potential duplicates; merges approved records with points consolidation; monthly data quality dashboard showing duplicate rate, incomplete records, and invalid contact info (W17.1–2)

### Staffing Implication
- **1 Loyalty Manager** (within Marketing): Day-to-day program management is largely automated. Monthly reviews and quarterly promo planning = ~5 hours/month. One person within the 20-person Marketing team handles this alongside other duties.

---

## W18. Direct Store Delivery (DSD) Receiving

| Field | Detail |
|---|---|
| **Trigger** | Vendor delivers goods directly to store (bypassing DC) |
| **Frequency** | ~2–3 DSD deliveries per store per week; ~500–600 DSD receipts/month chain-wide |
| **Volume** | ~30% of total inbound goods by value/weight (cement, lumber, sand, gravel are bulky/high-value); ~500–600 DSD receipts/month (~8–10% of total receipt count); ~5–10 lines per receipt |
| **Owner** | Receiving Clerk (Store) |
| **Participants** | Receiving Clerk, Department Supervisor, Vendor Driver, AP Clerk |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Vendor arrives at store receiving dock; presents Delivery Receipt (DR) and PO reference | Vendor Driver | Receiving Clerk | 5 min |
| 2 | Receiving Clerk retrieves PO in system on handheld/tablet | Receiving Clerk | Dept. Supervisor | 2 min |
| 3 | Unload goods; Receiving Clerk scans/verifies each item against PO: SKU, quantity, condition | Receiving Clerk | Dept. Supervisor | 20–45 min |
| 4 | Quality check on sampled items (damage, completeness) | Dept. Supervisor | Dept. Supervisor | 5–10 min |
| 5 | If discrepancy: flag in system; note on DR; notify Buyer | Receiving Clerk | Dept. Supervisor | 5 min if any |
| 6 | Confirm Goods Receipt in system; store inventory increases in real-time | Receiving Clerk | Dept. Supervisor | 5 min |
| 7 | Vendor DR signed and returned; copy retained for AP matching | Receiving Clerk | — | 2 min |
| 8 | Stock Associate moves goods directly to sales floor (no backroom staging for DSD) | Stock Associate | Dept. Supervisor | 15–30 min |
| 9 | AP receives vendor invoice; 3-way match: PO → Store GR → Invoice | AP Clerk | AP Supervisor | Automated / 10 min |

**Total time per DSD delivery**: ~1–2 hours from truck arrival to shelf

### DSD vs. DC-Receiving Differences
- No putaway step — goods go directly to sales floor
- No WMS involved — processed through store-level receiving in POS/ERP
- Smaller average receipt size (~5–10 lines vs. ~15 for DC)
- Vendor driver typically waits for GR confirmation and signed DR
- Common DSD categories: cement, lumber, sand, gravel, large appliances

### System Touchpoints
- PO lookup on store handheld/tablet (W18.2)
- Barcode/RF scanning against PO at store level (W18.3)
- Store-level Goods Receipt posting → inventory update (W18.6)
- DR capture and linking to PO for AP matching (W18.7, W18.9)
- 3-way match including store-level GR (W18.9)
- Real-time inventory visibility for DSD items (W18.6)
- DSD GRNI follow-up: for DSD-related GRNI exceptions at month-end (W9a.2a), AP Clerk contacts the store Receiving Clerk who processed the original GR (W18.3) to confirm received quantities and resolve discrepancies with the vendor
- Shelf-life / expiry capture at DSD receiving: for date-sensitive DSD items (cement, paint, adhesives), Receiving Clerk captures manufacturing date and shelf-life at goods receipt; system records expiry date per batch; near-expiry items flagged for priority sale or markdown (W18)

### Staffing Implication
- **2 Receiving Clerks per store** (already in staffing model): DSD adds 2–3 additional receiving events per week (~3–6 hours). Combined with DC replenishment receiving (2–3 trucks/week) and BOPIS, the 2 clerks in alternating shifts can handle the load. No additional headcount needed.

---

## W19. Ecommerce — Home Delivery Fulfillment

| Field | Detail |
|---|---|
| **Trigger** | Customer places delivery order on website/app (non-BOPIS) |
| **Frequency** | ~17,200 delivery orders/month; ~573/day |
| **Volume** | Avg 3–4 items per order |
| **Owner** | DC Dispatch Supervisor |
| **Participants** | System (order routing), DC Picker, DC Packer, Delivery Partner driver, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer places delivery order on website/app; selects delivery address; pays online | Customer | — | — |
| 2 | System routes order to nearest DC (or store if DC out of stock); creates pick list | System | — | Automated |
| 3 | DC receives pick task; assigns to picker by zone | WMS / DC Supervisor | DC Supervisor | 2 min |
| 4 | Picker picks items; scans each for confirmation | Picker | DC Supervisor | 5–15 min/order |
| 5 | If item unavailable: system offers substitution or cancels line; notifies customer | System / CSR | — | 3 min |
| 6 | Packer packs items for shipping; generates shipping label and packing slip | Packer | DC Supervisor | 5 min/order |
| 7 | System creates delivery order with selected partner (Lalamove, Transportify, own fleet) | System | DC Dispatch | Automated |
| 8 | Delivery partner picks up package; system updates order status to "Shipped" | Delivery Partner | DC Dispatch | 5 min |
| 9 | System sends tracking link to customer via SMS/email | System | — | Automated |
| 10 | Delivery partner delivers to customer; obtains proof of delivery (photo, signature) | Delivery Partner | — | Varies by distance |
| 11 | System marks order as "Delivered"; inventory formally deducted | System | — | Automated |
| 12 | If delivery fails (customer unavailable): reschedule or return to DC; restock | Delivery Partner / DC | DC Supervisor | 15 min |

**Delivery SLA**: 2–5 business days from order placement

### System Touchpoints
- Real-time inventory availability per DC on website (W19.1)
- Available-to-Promise (ATP) reservation at order placement: system deducts from available inventory at the fulfillment DC; ATP = on-hand − allocated to open orders − safety stock buffer; if ATP = 0, item shown as "unavailable" for that delivery zone (W19.1)
- ATP reservation held until pick confirmation (hard commitment) or order cancellation; released if delivery fails and order is cancelled (W19.12)
- Order routing to nearest fulfillment location (W19.2)
- WMS pick task generation and assignment (W19.3–4)
- Out-of-stock substitution/cancellation (W19.5)
- Shipping label and packing slip generation (W19.6)
- Delivery partner API integration for order creation and tracking (W19.7, W19.8, W19.10)
- Customer notification (SMS/email) with tracking link (W19.9)
- Proof of delivery capture (W19.10)
- Failed delivery / return-to-origin handling (W19.12)
- Ecommerce payment reconciliation: system imports daily settlement reports from each payment gateway (PayMongo, Dragonpay, GCash, Maya); matches settlement line items to individual ecommerce orders; reconciles gross payments, gateway fees (per-transaction and percentage), chargebacks, and refunds; posts gateway fees to payment processing expense (Dr. Payment Processing Expense / Cr. Cash); flags unreconciled settlements for investigation; Treasury verifies bank deposits match expected settlement amounts; reconciliation performed daily by Treasury Analyst as part of W30 daily cycle (W19)
- 3PL / delivery partner management: carrier master record with rate cards per zone/weight/tier and SLA terms; automated carrier selection by delivery zone, package weight, and cost; carrier performance dashboard tracking on-time delivery %, damage rate, cost per delivery, and customer complaint rate per carrier; monthly carrier invoice reconciliation (carrier fees matched to completed delivery orders); quarterly carrier performance review similar to W44 vendor scorecard; rate renegotiation triggered by SLA breach or market benchmarking (W19.7, W19.8, W19.10)

### Staffing Implication
- **Per DC**: Home delivery adds ~115 orders/day ÷ 5 DCs = ~23 orders/DC/day. At ~15 min pick+pack per order, that's ~6 hours/day of additional DC labor. Absorbed by existing picking/packing staff within the ~150 DC headcount.
- **No incremental headcount**: Home delivery fulfillment uses the same DC pick/pack team as store replenishment (W4), just with different packing and labeling requirements.

---

## W20. Vendor Managed Inventory (VMI)

| Field | Detail |
|---|---|
| **Trigger** | VMI vendor reviews sell-through data or system sends replenishment signal |
| **Frequency** | Varies by vendor (typically weekly or bi-weekly) |
| **Volume** | ~300 SKUs from 12 key vendors |
| **Owner** | Buyer (oversight) |
| **Participants** | VMI Vendor, Buyer, Receiving Clerk (DC or Store), AP Clerk |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System shares sell-through data and current stock levels with VMI vendor (EDI or portal) | System | Buyer | Automated |
| 2 | VMI vendor analyzes data and determines replenishment quantities | VMI Vendor | VMI Vendor | External |
| 3 | VMI vendor creates shipment; provides Advance Shipping Notice (ASN) to system | VMI Vendor | Buyer | External |
| 4 | Buyer reviews and confirms ASN; or system auto-confirms if within agreed parameters | Buyer / System | Buyer | 10 min/batch |
| 5 | Vendor ships goods to DC or store per agreement | VMI Vendor | — | External |
| 6 | Receiving Clerk processes Goods Receipt against ASN (standard receiving process) | Receiving Clerk | Dept. Supervisor / DC Supervisor | Per W3 or W18 |
| 7 | Goods recorded as vendor-owned inventory in system (non-valuated until sold) | System | — | Automated |
| 7a | At month-end close (W9): system accrues VMI liability for all VMI goods sold but not yet settled with vendor; Cost Accountant includes VMI accrual in monthly close entries | System / Cost Accountant | Controller | Automated + 15 min/month |
| 8 | At POS: system records sell-through event per VMI SKU; ownership transfers at point of sale | System | — | Automated |
| 9 | Monthly: system generates VMI sell-through report per vendor showing units sold × agreed price | System | Buyer | Automated |
| 10 | Buyer reviews sell-through report; confirms settlement | Buyer | Category Manager | 1 hour/month/vendor |
| 11 | System generates AP invoice from sell-through data; vendor payment processed | System / AP Clerk | AP Supervisor | Automated + 30 min |

**Settlement cycle**: Monthly per VMI vendor

### System Touchpoints
- Sell-through data export to vendor (EDI/portal/API) (W20.1)
- ASN receipt and processing from vendor (W20.3)
- Non-valuated (vendor-owned) inventory tracking (W20.7)
- Sell-through event capture at POS (W20.8)
- VMI settlement report generation (W20.9)
- Auto-generation of AP from sell-through (W20.11)

### Staffing Implication
- **Buyer time**: 12 VMI vendors × 1 hour/month review = 12 hours/month. Spread across 10–12 buyers, this is ~1 hour each per month. Minimal impact.
- **AP**: VMI settlement adds 12 additional AP invoices/month. Negligible incremental load.

---

## W21. Capital Expenditure (Capex) Request & Approval

| Field | Detail |
|---|---|
| **Trigger** | Need identified for asset acquisition (equipment, vehicles, fixtures, IT hardware, store build-out) |
| **Frequency** | ~50–80 capex requests/year |
| **Volume** | Peaks during new store openings (W16) and annual budget cycle |
| **Owner** | Requesting Department Head |
| **Participants** | Requestor, Department Head, Finance (Capex Analyst), CFO, CEO/Board |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Requestor submits capex request: item description, justification, quotations (min. 3), expected useful life, budget code | Requestor | Dept. Head | 30 min |
| 2 | Department Head reviews and approves or returns for revision | Dept. Head | Dept. Head | 15 min |
| 3 | Finance (Capex Analyst) validates against approved annual budget; checks ROI calculation | Capex Analyst | CFO | 30 min |
| 4 | Route for approval per tiered matrix (see below) | System | As per tier | 15–30 min |
| 5 | Approved capex → Purchase Order created (standard PO workflow W2) or direct purchase | Buyer / Requestor | Dept. Head | Per W2 |
| 6 | Goods/asset received; Goods Receipt posted | Receiving Clerk / IT | Dept. Head | Per W3 |
| 7 | Finance capitalizes asset in Fixed Asset module: asset tag, location, depreciation schedule, useful life | Cost Accountant | Controller | 15 min/asset |
| 8 | System begins monthly depreciation per schedule | System | — | Automated |
| 9 | Post-implementation review: actual vs. budgeted cost; in-service date | Capex Analyst | CFO | Quarterly |

### Approval Matrix

| Amount | Approval Required |
|---|---|
| ≤ PHP 100,000 | Finance Manager |
| PHP 100,001 – 500,000 | CFO |
| PHP 500,001 – 5,000,000 | CEO |
| > PHP 5,000,000 | Board of Directors |

### System Touchpoints
- Capex request form with quotation attachments (W21.1)
- Tiered approval workflow (W21.4)
- Budget availability check against annual capex budget (W21.3)
- PO creation from approved capex (W21.5)
- Fixed Asset creation and capitalization (W21.7)
- Depreciation schedule auto-generation (W21.8)
- Capex vs. budget reporting (W21.9)

### Staffing Implication
- **1 Capex Analyst** (within Finance): 50–80 requests/year. Each requires ~30 min validation. ~40 hours/year = ~1 day/month. Absorbed by existing Finance team (~35). May be the Cost Accountant or a dedicated analyst role during peak store-opening periods.

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

**Transfer lead time**: Inter-DC: 3–7 days; Store-to-Store: 1–3 days (same city) or 3–5 days (inter-region)

### System Touchpoints
- Transfer Order creation with source/destination (W22.2)
- Real-time availability check at source (W22.3)
- Approval workflow (W22.4)
- In-transit inventory tracking (W22.6)
- Receiving against Transfer Order (W22.7)
- Inventory update at both locations (W22.8)
- Discrepancy handling (W22.9)

### Staffing Implication
- Inter-DC transfers are part of Supply Planner's existing duties (within the 30-person Supply Chain team).
- Store-to-store transfers are managed by Store Managers with Regional Manager approval — absorbed into existing roles.

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

### Staffing Implication
- Consignment management adds ~15–25 hours/month to Buyer workload (review + settlement). Spread across 10–12 buyers handling their respective vendor portfolios, this is ~2 hours/buyer/month. Absorbed within existing headcount.

---

## W24. Trade & Corporate Credit Application

| Field | Detail |
|---|---|
| **Trigger** | Customer applies for trade or corporate credit account |
| **Frequency** | ~100–150 new credit applications/month |
| **Volume** | ~5,200 active trade accounts; ~200 corporate accounts |
| **Owner** | AR Supervisor |
| **Participants** | Sales Rep, AR Clerk, AR Supervisor, Finance Manager, Credit Committee |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer submits credit application (in-store, via Sales Rep, or online form) | Customer / Sales Rep | AR Clerk | 15 min |
| 2 | AR Clerk verifies application completeness: business registration, financial statements, trade references | AR Clerk | AR Supervisor | 30 min |
| 3 | AR Clerk runs credit check (bank references, trade references, external credit bureau if available) | AR Clerk | AR Supervisor | 30 min |
| 4 | AR Clerk prepares credit assessment with recommended limit and terms | AR Clerk | AR Supervisor | 15 min |
| 5 | Approval per tier (see matrix below) | Approver | Approver | 10–30 min |
| 6 | System creates customer account with approved credit limit, payment terms, and entity assignment | AR Clerk | AR Supervisor | 15 min |
| 7 | Customer notified of approval; account activated | AR Clerk | — | 10 min |
| 8 | Annual credit review: AR Clerk reviews all accounts for limit adjustment (increase, decrease, or suspension) | AR Clerk | AR Supervisor | 5 min/account |

### Credit Approval Matrix

| Credit Limit | Approver |
|---|---|
| ≤ PHP 200,000 | AR Supervisor |
| PHP 200,001 – 1,000,000 | Finance Manager |
| > PHP 1,000,000 | Credit Committee (CFO + Finance Manager + AR Supervisor) |

### System Touchpoints
- Credit application form (online or in-store) (W24.1)
- Customer master creation with credit limit and payment terms (W24.6)
- Credit limit enforcement at POS/sales order (W24.6 → W8.3)
- Annual credit review scheduling and workflow (W24.8)

### Staffing Implication
- **AR Clerks** (3–4): 100–150 applications/month × ~90 min each = 150–225 hours/month. Spread across 3–4 clerks = ~50 hours/clerk/month. Absorbed within existing AR team workload, primarily in the first half of the month when collection activity is lighter.

---

## W25. Petty Cash Management

| Field | Detail |
|---|---|
| **Trigger** | Small expense incurred at store or DC that cannot go through standard PO/AP process |
| **Frequency** | ~10–15 petty cash disbursements per store per month; ~2,000–3,000/month chain-wide |
| **Volume** | PHP 20,000 float per store; PHP 50,000 float per DC |
| **Owner** | Store Manager / DC Supervisor |
| **Participants** | Employee (requestor), Store Manager, Petty Cash Custodian, AP Clerk |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Employee requests petty cash for small expense (supplies, minor repairs, transport, miscellaneous) | Employee | Store Manager | 5 min |
| 2 | Store Manager approves request (verifies business purpose) | Store Manager | Store Manager | 5 min |
| 3 | Petty Cash Custodian disburses cash; employee signs petty cash voucher | Custodian | Store Manager | 5 min |
| 4 | Employee provides receipt and any change back to Custodian | Employee | — | 5 min |
| 5 | Custodian records transaction in petty cash log (physical or system) | Custodian | Store Manager | 5 min |
| 6 | When fund runs low (~70% disbursed): Custodian prepares replenishment request with all vouchers | Custodian | Store Manager | 30 min |
| 7 | Store Manager reviews vouchers; approves replenishment | Store Manager | Store Manager | 15 min |
| 8 | AP Clerk processes replenishment; creates petty cash voucher in system; posts expense to GL | AP Clerk | AP Supervisor | 15 min |
| 9 | Treasury / bank transfers replenishment amount to store custodian | Treasury Analyst | CFO | 10 min |
| 10 | Monthly: Custodian reconciles petty cash (cash on hand + outstanding vouchers = fund amount) | Custodian | Store Manager | 15 min |

### System Touchpoints
- Petty cash voucher recording (W25.5)
- Replenishment request and approval workflow (W25.6–7)
- GL posting for petty cash expenses (W25.8)
- Petty cash reconciliation reporting (W25.10)

### Staffing Implication
- **Petty Cash Custodian**: Typically the Assistant Store Manager or a designated cashier. Not a separate role.
- **AP impact**: ~2,000–3,000 replenishment requests/year. Most stores replenish once or twice monthly. Absorbed by existing AP clerks.

---

## W26. Annual Budget Preparation & Monthly Variance Review

| Field | Detail |
|---|---|
| **Trigger** | Annual budget calendar (typically Q4 for following year) |
| **Frequency** | Annual budget cycle; monthly variance review |
| **Volume** | 5 entities × 200+ cost centers; ~500–800 GL accounts per entity |
| **Owner** | Controller |
| **Participants** | Controller, CFO, Department Heads, Category Managers (merchandising budget), Store Ops Director (store-level budget), HR (payroll budget), IT (capex budget) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | CFO issues budget circular with guidelines, assumptions (revenue growth, inflation, headcount plan, new store openings) | CFO | CEO | 1 week |
| 2 | Department Heads prepare department-level budget: opex, headcount, capex requests | Dept. Heads | VP / C-Suite | 2–3 weeks |
| 3 | Category Managers prepare merchandise purchase budget by category (COGS, margin targets, inventory levels) | Category Manager | VP Merchandising | 1–2 weeks |
| 4 | Store Ops Director prepares store-level P&L budgets (revenue per store, labor, utilities, shrinkage) | Store Ops Director | COO | 1–2 weeks |
| 5 | HR prepares payroll budget (salary adjustments, new hires, statutory increases) | HR Head | CHRO | 1 week |
| 6 | Controller consolidates all department budgets into draft company budget per entity | Controller | CFO | 1 week |
| 7 | CFO and CEO review consolidated draft; negotiate adjustments with Department Heads | CFO / CEO | CEO | 1–2 weeks |
| 8 | Board approves annual budget | Board | CEO | 1 meeting |
| 9 | System loads approved budget per entity, per cost center, per GL account (monthly phasing) | Controller / System | CFO | 2–3 days |
| 10 | Monthly: Controller generates budget vs. actual report per entity and consolidated | Controller | CFO | 2 hours/month |
| 11 | Department Heads review their variances; provide explanations for material deviations (> 10%) | Dept. Heads | VP / C-Suite | 1 hour/month each |
| 12 | CFO reviews consolidated variance report; identifies risks and corrective actions | CFO | CEO | 1 hour/month |
| 13 | Quarterly: if material changes warranted, Controller prepares budget revision for CFO/Board approval | Controller | CFO | 4 hours/quarter |

**Total annual budget cycle**: ~8–10 weeks (Q4)
**Monthly variance review**: ~1 day total effort across Finance and Department Heads

### System Touchpoints
- Budget entry by department, cost center, GL account with monthly phasing (W26.2–5)
- Consolidation of department budgets into entity and group budgets (W26.6)
- Budget loading and lock-down after Board approval (W26.9)
- Budget vs. actual reporting with variance % and drill-down (W26.10–11)
- Budget revision workflow with approval (W26.13)
- Budget availability check during PO and capex creation (links to W2, W21)

### Staffing Implication
- **Controller**: Owns the budget process. ~30 hours during annual cycle + ~4 hours/month for variance review.
- **Department Heads**: ~3–5 hours each during annual cycle + ~1 hour/month variance review. Absorbed into existing management duties.
- No additional headcount needed.

---

## W27. Vendor Rebate Accrual & Settlement

| Field | Detail |
|---|---|
| **Trigger** | Vendor rebate agreement established; or monthly settlement date |
| **Frequency** | Agreements established annually; settlements monthly or quarterly per contract terms |
| **Volume** | ~40–60 active rebate agreements (top 20 vendors = 45% of COGS; ~2–3 agreements per vendor) |
| **Owner** | Buyer (agreement); Finance — Cost Accountant (accrual and settlement) |
| **Participants** | Buyer, Category Manager, Cost Accountant, AP Clerk, Vendor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Buyer negotiates rebate agreement with vendor: terms (volume-based, growth-based, promotional), qualifying SKUs, rebate rate, settlement frequency, measurement period | Buyer | Category Manager | Per negotiation |
| 2 | System records rebate agreement: vendor, SKUs, rebate type, rate/tier, effective dates, settlement schedule | Buyer | Category Manager | 15 min/agreement |
| 3 | At each qualifying purchase (PO receipt): system accrues rebate amount based on agreement terms | System | — | Automated |
| 4 | At each qualifying sale (POS): system accrues rebate for sell-through-based agreements | System | — | Automated |
| 5 | Monthly: Cost Accountant reviews accrued rebates report; validates accruals against agreement terms | Cost Accountant | Controller | 2 hours/month |
| 6 | At settlement date (monthly/quarterly): system generates rebate settlement report per vendor showing accrued rebate, qualifying volume, and amount due | System | Cost Accountant | Automated |
| 7 | Buyer reviews settlement report; confirms quantities and amounts with vendor | Buyer | Category Manager | 30 min/vendor |
| 8 | If vendor disputes: Buyer negotiates resolution; adjusts settlement amount with Category Manager approval | Buyer | Category Manager | 1 hour/occurrence |
| 9 | Cost Accountant posts rebate settlement: AP credit memo created; vendor balance reduced | Cost Accountant | Controller | 15 min/vendor |
| 10 | AP processes net payment to vendor (or offset against next invoice per agreement) | AP Clerk | AP Supervisor | Per W7 |
| 11 | Quarterly: Buyer reviews rebate program effectiveness; recommends renewal, renegotiation, or termination | Buyer | VP Merchandising | 2 hours/quarter |

### System Touchpoints
- Rebate agreement creation with configurable terms (volume tiers, growth targets, promo-based) (W27.2)
- Automatic rebate accrual at purchase or sale (W27.3–4)
- Accrued rebates report by vendor (W27.5)
- Settlement report generation with qualifying volume and amount (W27.6)
- AP credit memo creation from rebate settlement (W27.9)
- Rebate program analytics: ROI, margin impact, vendor comparison (W27.11)

### Staffing Implication
- **Cost Accountant**: Adds ~4–6 hours/month for rebate accrual review and settlement. Absorbed within existing Finance team.
- **Buyers**: 40–60 agreements ÷ 10–12 buyers = ~4–5 agreements each. Settlement review = ~2 hours/buyer/settlement cycle. Absorbed.

---

## W28. Gift Card & Store Credit Lifecycle

| Field | Detail |
|---|---|
| **Trigger** | Customer purchases or receives a gift card; or customer issued store credit as refund |
| **Frequency** | Continuous at POS and online |
| **Volume** | ~8,000–12,000 active gift cards/month; ~500–800 store credits issued/month (from returns without receipt) |
| **Owner** | Customer Service Rep (in-store); Marketing (gift card program) |
| **Participants** | Cashier, CSR, Customer, Marketing, Finance (breakage accounting) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer purchases gift card at POS: Cashier selects "Sell Gift Card"; scans/activates new card; loads amount | Cashier | Store Manager | 2 min |
| 2 | System activates gift card number; records liability (unredeemed balance) on balance sheet | System | — | Automated |
| 3 | Customer (or recipient) presents gift card at checkout; Cashier scans barcode or enters card number | Cashier | — | 15 sec |
| 4 | System validates card is active and has sufficient balance; applies as payment method | System | — | Automated |
| 5 | If partial redemption: remaining balance stays on card; receipt shows new balance | System | — | Automated |
| 6 | If customer requests balance inquiry: Cashier scans card; system displays balance on receipt or customer display | Cashier | — | 10 sec |
| 7 | Customer can reload existing gift card at POS or online | Cashier / Customer (online) | — | 1 min |
| 8 | Store credit issued (W12 returns with no receipt or outside policy): system generates store credit voucher with unique barcode and amount | CSR | Store Manager | 3 min |
| 9 | Store credit redeemed at POS: Cashier scans voucher barcode; applies as payment; system marks voucher as fully/partially used | Cashier | — | 30 sec |
| 10 | Gift card expiry after 24 months of inactivity: system flags expired cards; Finance recognizes breakage income | System | Controller | Automated (monthly batch) |
| 11 | Monthly: Finance reviews gift card liability report (total outstanding, aging, breakage recognized) | Cost Accountant | Controller | 30 min/month |

### System Touchpoints
- Gift card sale and activation at POS with barcode scanning (W28.1)
- Gift card liability tracking on balance sheet (W28.2)
- Gift card redemption as payment method at POS and online (W28.3–5)
- Balance inquiry via POS, receipt, or customer-facing display (W28.6)
- Gift card reload capability (W28.7)
- Store credit voucher generation from returns (W28.8)
- Store credit redemption via barcode scanning (W28.9)
- Scheduled expiry processing with breakage accounting (W28.10)
- Gift card liability aging report (W28.11)

### Staffing Implication
- No incremental headcount. Gift card transactions add ~2 min to occasional POS transactions. Store credit adds to existing CSR return workflow (W12).
- **Cost Accountant**: Adds ~30 min/month for liability and breakage review.

---

## W29. Product Recall Execution

| Field | Detail |
|---|---|
| **Trigger** | DTI/BPS recall notice, vendor recall notification, or internal quality discovery |
| **Frequency** | Rare (2–5 events/year expected) |
| **Volume** | Varies widely — from a single lot to multiple SKUs across all locations |
| **Owner** | VP Merchandising (product side); Store Ops Director (execution) |
| **Participants** | VP Merchandising, Buyer, Store Ops Director, Store Managers, Customer Service, Marketing, Legal, IT |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Recall trigger received: DTI/BPS directive, vendor notification, or internal quality report | Buyer / Legal | VP Merchandising | — |
| 2 | VP Merchandising activates recall protocol: identifies affected SKUs, lot numbers, batch numbers, date ranges | VP Merchandising | COO | 1 hour |
| 3 | System generates affected inventory report: locations holding the identified lots/batches, quantities on hand, quantities sold (with customer data if traceable via loyalty or B2B account) | System | VP Merchandising | Automated |
| 4 | Buyer contacts vendor for recall instructions (return, destroy, credit terms) | Buyer | VP Merchandising | 2 hours |
| 5 | IT immediately blocks affected items at POS: system flags items as "recall — do not sell"; cashiers see alert when scanning | IT | CIO | 30 min |
| 6 | Ecommerce: system removes affected items from website; cancels pending orders containing recalled items; initiates refunds | System / Ecom Team | CMO | 1 hour |
| 7 | Store Ops instructs all stores to pull affected items from shelves immediately; quarantine in backroom | Store Ops Director | COO | 2 hours |
| 8 | Marketing issues public recall notice (press release, social media, website banner, in-store signage) | Marketing | CMO | 4–8 hours |
| 9 | Customer Service handles inbound inquiries; processes returns/exchanges for recalled items (no receipt required) | CSR / Call Center | Store Ops Director | Ongoing |
| 10 | System tracks all recalled items returned by customers; matches against sold quantities to gauge recall coverage | System | VP Merchandising | Automated |
| 11 | Store Managers report quarantine completion; system records inventory hold per location | Store Manager | Store Ops Director | 1 day |
| 12 | Per vendor instructions: initiate RTV or on-site destruction with documentation | Buyer / DC Supervisor | VP Merchandising | 1–2 weeks |
| 13 | Legal prepares regulatory report (DTI/BPS) documenting recall scope, actions taken, and customer notifications | Legal | CEO | 1 week |
| 14 | Post-recall: VP Merchandising and Legal conduct after-action review; update quality procedures | VP Merchandising + Legal | COO | 2 hours |

### System Touchpoints
- Lot/batch/serial number traceability: forward (sold-to) and backward (received-from) tracing (W29.3)
- POS blocking flag for recalled items with cashier alert (W29.5)
- Ecommerce automatic removal and refund processing (W29.6)
- Recall-specific returns processing without receipt requirement (W29.9)
- Recall tracking dashboard: quantities pulled, returned by customers, pending per location (W29.10–11)
- RTV or destruction documentation (W29.12)

### Staffing Implication
- No dedicated headcount for recalls (2–5 events/year). When a recall occurs, it is managed by existing roles as a cross-functional effort led by VP Merchandising.
- Call center (30 people) absorbs inbound customer inquiries during active recalls.

---

## W5d. Offline POS Recovery & Reconciliation

| Field | Detail |
|---|---|
| **Trigger** | POS terminal or store network connectivity is restored after an outage |
| **Frequency** | Occasional (estimated 2–4 significant outages per store per year) |
| **Volume** | Variable — depends on outage duration; worst case 8+ hours of transactions (~390 transactions at ~467/day ÷ 10 hours) |
| **Owner** | Store Manager |
| **Participants** | Cashier, Store Manager, IT Helpdesk |

### Background

POS terminals must continue selling during network outages (NFR-011: ≥ 8 hours offline). Terminals cache the local product master and price file (refreshed nightly) so that barcode scanning, price lookup, promotions, and payment processing work offline. Transactions are stored locally and queued for upload when connectivity returns.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Connectivity is restored; POS terminal automatically begins uploading queued offline transactions to ERP | System | — | Automated (2–5 min for a full shift of transactions) |
| 2 | System compares uploaded transaction data against central inventory: identifies any inventory conflicts (item sold offline that was also sold online or allocated to BOPIS) | System | — | Automated |
| 3 | If inventory conflict detected (negative stock): system alerts Store Manager and IT Helpdesk; flags affected transactions for review | System | Store Manager | Automated |
| 4 | Store Manager reviews conflicts: (a) if physical stock exists (count was ahead of system), confirm and accept; (b) if truly oversold, contact affected customer for substitution or refund | Store Manager | Store Ops Director | 15–30 min |
| 5 | System reconciles: posts all offline sales to GL, updates inventory to final state, syncs loyalty points earned/redemed during outage | System | — | Automated |
| 6 | System verifies cash drawer totals (offline Z-report) match uploaded transaction totals; flags any variance | System | Store Manager | Automated |
| 7 | Store Manager confirms reconciliation is complete; acknowledges any variances in system | Store Manager | — | 10 min |
| 8 | If offline period exceeded 8 hours (stale price risk): system flags transactions where promo or price changes occurred during outage for manager review | System | Store Manager | Automated |
| 9 | IT Helpdesk reviews root cause of outage; updates incident log | IT Helpdesk | CIO | 15 min |

### System Touchpoints
- Local product/price cache on each POS terminal with nightly refresh (W5a.3, W5a.5)
- Offline transaction queuing and encrypted local storage (W5d.1)
- Automated upload and inventory conflict detection on reconnection (W5d.2–3)
- Offline-to-online GL and inventory reconciliation (W5d.5–6)
- Loyalty points reconciliation for transactions processed offline (W5d.5)
- Stale price detection for extended outages (W5d.8)

### Staffing Implication
- No incremental headcount. Outage recovery is a Store Manager responsibility with IT support.
- Estimated 2–4 recoveries per store per year × 30 min each = ~1–2 hours/year per store.

---

## W30. Daily Treasury & Cash Position Management

| Field | Detail |
|---|---|
| **Trigger** | Daily treasury operations cycle |
| **Frequency** | Daily |
| **Volume** | 200 stores + 5 DCs + HQ cash positions; ~210 bank accounts across 4 banks (BDO, BPI, Metrobank, Chinabank) × 5 entities |
| **Owner** | Treasury Analyst |
| **Participants** | Treasury Analyst, Store Managers (cash deposits), CFO, Banks |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Store Managers prepare daily cash deposit from POS takings per W5c; armored car or bank branch deposit | Store Manager | COO | 30 min/day per store |
| 2 | System imports daily bank statements from all bank accounts (BDO, BPI, Metrobank, Chinabank) via BPI BizLink, BDO Corporate, or equivalent bank APIs | System | Treasury Analyst | Automated (daily) |
| 3 | Treasury Analyst reviews daily cash position report: bank balances per entity, pending inflows (store deposits), pending outflows (AP payment runs, payroll) | Treasury Analyst | CFO | 30 min/day |
| 4 | System auto-matches store cash deposits to expected amounts from Z-reports; flags shortages or delayed deposits | System | Treasury Analyst | Automated |
| 5 | Treasury Analyst identifies surplus or deficit per entity; recommends inter-entity cash transfers or short-term placements | Treasury Analyst | CFO | 15 min/day |
| 6 | If inter-entity transfer needed: Treasury Analyst initiates transfer with CFO approval; system posts IC loan entry | Treasury Analyst | CFO | 15 min/transfer |
| 7 | Twice weekly: Treasury executes cash sweep from store collection accounts to main operating accounts per entity | Treasury Analyst | CFO | 30 min/run |
| 8 | Weekly: Treasury prepares cash flow forecast (2-week rolling) based on AP aging, AR collection schedule, payroll dates, and capex commitments | Treasury Analyst | CFO | 2 hours/week |
| 9 | Monthly: Treasury reconciles all bank accounts per entity; posts bank charges, interest income, FX gains/losses | Treasury Analyst | Controller | 1 day/month |
| 10 | Import payments: Treasury manages USD accounts; executes FX conversions for import vendor payments based on LC/TT schedule | Treasury Analyst | CFO | As needed |

### System Touchpoints
- Multi-bank statement import (BDO, BPI, Metrobank, Chinabank) via file formats or API (W30.2)
- Daily cash position dashboard per entity and consolidated (W30.3)
- Store cash deposit auto-matching to Z-report amounts (W30.4)
- Cash sweep scheduling and execution (W30.7)
- Rolling cash flow forecast (W30.8)
- Bank reconciliation per entity (W30.9; also linked to W9a step 9)
- Multi-currency (PHP/USD) account management with FX conversion tracking (W30.10)

### Staffing Implication
- **2–3 Treasury Analysts**: Daily cash position (30 min) + sweep execution (30 min × 2/week) + weekly forecast (2 hours) + monthly bank reconciliation (1 day) + import payments + inter-entity transfers. This is a full-time role for 2 analysts with a 3rd covering during peaks (month-end, import payment seasons).
- **Store Managers**: Daily cash deposit preparation adds ~30 min to closing routine — absorbed into W5c.

---

## W31. Demand Forecasting Cycle

| Field | Detail |
|---|---|
| **Trigger** | Weekly forecast recalculation schedule (Sunday batch) |
| **Frequency** | Weekly recalculation; monthly review; quarterly adjustment |
| **Volume** | 35,000 active SKUs × 5 DCs × 200 stores = up to 7.2M SKU-location forecasts; typically forecasted at DC level (175,000 SKU-DC combinations) and disaggregated to stores |
| **Owner** | Demand Planner |
| **Participants** | Demand Planner, Supply Planner, Category Manager, Pricing Analyst |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System runs automated forecast engine: statistical algorithms (exponential smoothing, seasonal decomposition) applied to 2+ years of historical sales data per SKU per DC | System | — | Automated (Sunday batch, 1–3 hours) |
| 2 | System adjusts raw statistical forecast for known events: promotional calendar (W13), seasonal calendar, new store openings (W16), planned store closures, one-time events (typhoons, pandemic) | System | — | Automated |
| 3 | Demand Planner reviews forecast exception report: SKUs with forecast error > 30%, SKUs with insufficient history, new SKUs with no history, SKUs with sudden demand spikes or drops | Demand Planner | Supply Planning Manager | 2–3 hours/week |
| 4 | Demand Planner adjusts flagged forecasts manually: overrides algorithm, inputs qualitative intelligence (vendor intel, market trends, competitive activity) | Demand Planner | Supply Planning Manager | 1–2 hours/week |
| 5 | Demand Planner reviews forecast accuracy metrics (MAPE, bias) by category; identifies systematic over/under-forecasting patterns | Demand Planner | Supply Planning Manager | 1 hour/week |
| 6 | Adjusted forecast released to replenishment engine (W4.1, W2a.1); system uses forecast instead of simple min/max for forecasted SKUs | System | — | Automated |
| 7 | Monthly: Demand Planner presents forecast vs. actual report to Category Managers; discusses upcoming demand shifts | Demand Planner | VP Merchandising | 1 hour/category/month |
| 8 | Quarterly: Demand Planner recalibrates forecast model parameters (alpha, beta, gamma for exponential smoothing); updates seasonal indices based on latest year of data; reviews and updates safety stock parameters per SKU-location based on forecast error and demand variability changes (feeds into W2a.1 ROP/safety stock calculation) | Demand Planner | Supply Planning Manager | 4–6 hours/quarter |

**Total Demand Planner effort**: ~8–12 hours/week + 4–6 hours/quarter for model recalibration

### System Touchpoints
- Statistical forecast engine with multiple algorithms (W31.1)
- Automated event adjustment from promotional and seasonal calendars (W31.2)
- Forecast exception reporting with error thresholds (W31.3)
- Manual forecast override with audit trail (W31.4)
- Forecast accuracy dashboards (MAPE, bias, weighted MAPE) (W31.5)
- Forecast release to replenishment/MRP engine (W31.6)
- Forecast vs. actual variance reporting by category (W31.7)
- Model parameter maintenance and seasonal index recalculation (W31.8)
- Safety stock parameter review and update linked to ROP calculation in W2a (W31.8)
- Multi-echelon DC replenishment sourcing: when a DC's inventory for a SKU drops below ROP, system evaluates available stock at other DCs, inter-DC transfer cost and lead time, vs. vendor PO cost and lead time; recommends optimal source; if transfer recommended, auto-generates Transfer Order per W22; if PO recommended, auto-generates suggested PO per W2a; Supply Planner reviews sourcing recommendations as part of daily replenishment review (W31.6, W4.2)

### Staffing Implication
- **1–2 Demand Planners** (within the 30-person Supply Chain team): This is a specialized analytical role. With 35,000 SKUs across 5 DCs, weekly review of forecast exceptions + monthly category reviews + quarterly recalibration requires a dedicated person. A 2nd demand planner provides coverage and can focus on new-item forecasting (no history) and promotional lift modeling.
- **Category Managers**: 1 hour/month each for forecast review meetings = ~10 hours/month total. Absorbed into existing duties.

---

## W32. Seasonal Buy Planning

| Field | Detail |
|---|---|
| **Trigger** | Seasonal calendar milestones (6 months before each season peak) |
| **Frequency** | 4 major seasonal planning cycles/year: Christmas (plan in Jun), Summer/March (plan in Oct), Back-to-School (plan in Nov), Rainy Season/ typhoon prep (plan in Jan) |
| **Volume** | ~3,000–5,000 seasonal SKUs per major event; ~20–30 import POs per season |
| **Owner** | Category Manager |
| **Participants** | Category Manager, Buyer, Demand Planner, Import Coordinator, VP Merchandising, Finance (budget) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Demand Planner generates seasonal forecast: prior-year sales by SKU for the season period, adjusted for current trend and planned promotions | Demand Planner | Category Manager | 4 hours/season |
| 2 | Category Manager reviews seasonal forecast; identifies SKUs to carry forward, new items to add, items to drop | Category Manager | VP Merchandising | 2 hours/season |
| 3 | Buyer solicits vendor quotations for seasonal items; negotiates volume discounts, early-order incentives, and return/excess-stock terms | Buyer | Category Manager | 1 week/season |
| 4 | Category Manager creates seasonal buy plan: SKU-level quantities, vendor allocation, delivery schedule (phased receipts vs. single drop) | Category Manager | VP Merchandising | 4 hours/season |
| 5 | Finance validates seasonal buy plan against working capital budget and inventory plan (max inventory days target) | Controller | CFO | 2 hours/season |
| 6 | VP Merchandising approves seasonal buy plan | VP Merchandising | VP Merchandising | 1 hour/season |
| 7 | Buyer creates import POs (W2b) or domestic POs (W2a) per the seasonal buy plan; times orders to arrive 6–8 weeks before season start | Buyer | Category Manager | Per W2 |
| 8 | System tracks seasonal PO commitments vs. seasonal buy plan budget; alerts if over-committed | System | — | Automated |
| 9 | As season approaches: Pricing Analyst sets up seasonal pricing and promotions (W13) | Pricing Analyst | Category Manager | Per W13 |
| 10 | Mid-season: Category Manager and Buyer review sell-through vs. plan; trigger re-orders for hot items or accelerate markdowns for slow movers | Category Manager | VP Merchandising | 1 hour/week during season |
| 11 | Post-season: Buyer and Category Manager conduct post-mortem: actual vs. plan sales, margin, leftover inventory disposition (clearance, return to vendor, carry forward to next year) | Buyer + Category Manager | VP Merchandising | 2 hours/season |

**Total cycle time**: 6 months from planning start to season peak

### System Touchpoints
- Seasonal forecast generation from historical data with event adjustment (W32.1)
- Seasonal buy plan entry with SKU, quantity, vendor, delivery phasing (W32.4)
- Budget/working capital check against seasonal plan (W32.5)
- PO commitment tracking against seasonal buy plan budget (W32.8)
- Seasonal sell-through dashboard: actual vs. plan by SKU (W32.10)
- Post-season analysis and leftover inventory disposition tracking (W32.11)
- Integration with W1 (assortment review), W2 (PO creation), W13 (promotions)

### Staffing Implication
- **Category Managers**: Seasonal planning is an extension of their existing W1 duties. Each seasonal cycle adds ~8–10 hours of work per category, spread over several weeks. With 5 Category Managers and 4 seasonal cycles, each handles ~1 major seasonal plan at a time. Absorbed within existing ~40-person Merchandising team.
- **Buyers**: Import PO creation follows standard W2b. Seasonal volume adds ~20–30 import POs per season, concentrated in a few weeks. Manageable within existing team.
- **Demand Planner**: Adds ~4 hours per seasonal cycle for forecast generation. With 4 cycles/year = 16 hours/year. Minimal impact.

---

## W33. Warranty Claim Processing

| Field | Detail |
|---|---|
| **Trigger** | Customer brings defective product to store within warranty period, or submits claim online |
| **Frequency** | ~800–1,200 warranty claims/month chain-wide; ~4–6 per store per month |
| **Volume** | Primarily power tools, appliances, plumbing fixtures, electrical equipment |
| **Owner** | Customer Service Rep (in-store) |
| **Participants** | CSR, Department Supervisor, Buyer, Vendor, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer brings defective item to CSR counter with proof of purchase (receipt, loyalty lookup, or bank statement) | Customer | — | — |
| 2 | CSR looks up original transaction; verifies item is within warranty period (system displays warranty terms per SKU) | CSR | Dept. Supervisor | 3 min |
| 3 | CSR inspects item and documents defect: photographs, written description, defect category (manufacturing defect, premature wear, DOA) | CSR | Dept. Supervisor | 5 min |
| 4 | System creates warranty claim record: linked to original transaction, SKU, serial/lot number (if tracked), customer contact, defect description, photos | CSR | Dept. Supervisor | 5 min |
| 5 | CSR determines resolution path based on warranty policy and defect type: (a) direct replacement from store stock, (b) send to vendor for repair, or (c) refund if item cannot be repaired/replaced | CSR | Dept. Supervisor | 2 min |
| 6 | **If direct replacement**: CSR processes replacement in system; new item issued to customer; defective unit removed from inventory; system creates RTV record linked to warranty claim | CSR | Store Manager | 5 min |
| 7 | **If vendor repair**: CSR labels item with warranty claim number; stages in backroom for vendor pickup or shipment to vendor service center; system creates RTV shipment record | CSR | Dept. Supervisor | 5 min |
| 8 | **If refund**: CSR processes refund per W12 return workflow; warranty claim closed with refund as resolution | CSR | Store Manager | Per W12 |
| 9 | Buyer is notified of warranty claim for vendor-owned items; Buyer tracks vendor response SLA (repair: 15 business days; replacement: 10 business days) | Buyer | Category Manager | Automated notification + 5 min/claim |
| 10 | If vendor repair/replacement exceeds SLA: Buyer escalates to Category Manager; Category Manager may authorize store to issue replacement from stock pending vendor resolution | Category Manager | VP Merchandising | 10 min/escalation |
| 11 | Repaired/replaced item received from vendor: CSR notifies customer for pickup; system links incoming item to original warranty claim | CSR | Dept. Supervisor | 5 min |
| 12 | Customer receives repaired/replaced item; warranty claim closed in system | CSR | — | 3 min |
| 13 | Monthly: system generates warranty claim report by vendor, SKU, defect type; Buyer reviews with top vendors during vendor performance review (W44) | System / Buyer | Category Manager | 1 hour/month |

### System Touchpoints
- Transaction lookup with warranty terms display per SKU (W33.2)
- Warranty claim record creation with photo attachment and defect categorization (W33.4)
- Serial/lot number linkage to warranty claim (W33.4)
- Replacement issuance with RTV creation (W33.6)
- Vendor repair tracking with RTV shipment record (W33.7)
- Vendor response SLA tracking and auto-notification (W33.9)
- Warranty claim lifecycle status tracking (open → in repair → resolved → closed) (W33.4–12)
- Warranty analytics dashboard by vendor, SKU, defect type (W33.13)

### Staffing Implication
- **CSR**: ~4–6 warranty claims/store/month × ~15 min each = ~1–1.5 hours/store/month. Absorbed within existing CSR role.
- **Buyer**: Warranty claims that need vendor follow-up add ~5 min/claim. With ~800–1,200 claims/month, not all require buyer intervention (many are direct replacements). Estimated ~200–300 needing buyer action = ~20–25 hours/month across 10–12 buyers = ~2 hours/buyer/month. Absorbed.
- No incremental headcount needed.

---

## W34. Store Shift Scheduling

| Field | Detail |
|---|---|
| **Trigger** | Weekly schedule creation cycle |
| **Frequency** | Weekly per store; published 1 week in advance |
| **Volume** | 35 staff × 200 stores = 7,000 weekly shift assignments; 2–3 shifts per day (opening: 7 AM–2 PM, mid: 10 AM–6 PM, closing: 2 PM–10 PM) |
| **Owner** | Store Manager |
| **Participants** | Store Manager, Assistant Store Manager, Department Supervisors, HR Assistant |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates draft schedule based on: (a) store operating hours, (b) staffing model per shift (min cashiers, floor associates, receiving), (c) historical sales volume by day and hour, (d) approved leave requests, (e) labor budget (max hours per employee per week) | System | — | Automated |
| 2 | Store Manager reviews draft schedule; adjusts for: expected delivery days (DSD receiving), upcoming promotions, special events, employee skill mix per shift | Store Manager | Store Ops Director | 1 hour/week |
| 3 | Department Supervisors review shift assignments for their departments; flag conflicts or coverage gaps | Dept. Supervisor | Store Manager | 30 min/week |
| 4 | Store Manager finalizes and publishes schedule in system; employees receive notification (mobile app, SMS, or bulletin board) | Store Manager | — | 15 min |
| 5 | Employee views schedule; submits swap requests to Store Manager if needed | Employee | — | Self-service |
| 6 | Store Manager approves or denies shift swap requests; updates schedule | Store Manager | — | 15 min/week |
| 7 | During the week: if unplanned absence (sick leave, emergency): Store Manager activates contingency (call in off-duty employee, redistribute floor staff, cover cashier shift personally) | Store Manager | — | Ad hoc |
| 8 | System tracks actual hours worked (biometric/RFID clock-in/out) vs. scheduled hours; flags overtime and undertime | System | — | Automated |
| 9 | Weekly: Store Manager reviews schedule adherence report; adjusts next week's plan based on actuals | Store Manager | Regional Manager | 15 min/week |
| 10 | Monthly: Regional Manager reviews overtime hours per store vs. labor budget; flags stores consistently exceeding targets | Regional Manager | Store Ops Director | 2 hours/month (across 50 stores) |

### System Touchpoints
- Automated schedule generation based on rules engine (W34.1)
- Leave request integration (W34.1d)
- Shift swap request and approval workflow (W34.5–6)
- Schedule publishing with employee notification (W34.4)
- Time & attendance integration: actual vs. scheduled hours comparison (W34.8)
- Overtime alerting (W34.8)
- Schedule adherence and labor budget reporting (W34.9–10)
- Integration with payroll (W10) for hour calculation

### Staffing Implication
- **Store Manager**: ~2 hours/week on scheduling. Absorbed into existing duties.
- **Department Supervisors**: ~30 min/week reviewing their section schedules. Absorbed.
- **Regional Managers**: ~2 hours/month reviewing overtime reports across their 50 stores. Absorbed.
- No incremental headcount. The system's automated draft generation significantly reduces manual scheduling effort.

---

## W35. Management Reporting Rhythm

| Field | Detail |
|---|---|
| **Trigger** | Reporting calendar (daily, weekly, monthly, quarterly cadences) |
| **Frequency** | Daily flash, weekly review, monthly close reporting, quarterly board pack |
| **Volume** | ~50 standard reports on recurring schedules; ~20 ad-hoc requests/month |
| **Owner** | Controller |
| **Participants** | Controller, CFO, CEO, Department Heads, BI Analyst |

### Steps

### Daily

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 1 | System generates daily flash report (auto-distributed by 7:00 AM): total chain revenue, transactions, avg ticket, same-store sales vs. prior year, top/bottom 10 stores | System | Controller | Daily (automated) |
| 2 | CFO reviews daily flash on mobile dashboard | CFO | — | 5 min/day |
| 3 | System generates daily inventory exception report: negative stock alerts, stockouts at store level, critical DC shortages | System | Supply Planning Manager | Daily (automated) |

### Weekly

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 4 | Week-on-week sales report by store, category, and channel (POS vs. ecommerce); auto-distributed every Monday | System | Controller | Weekly (automated) |
| 5 | Supply chain KPI report: fill rate, on-time delivery (DC→store), PO overdue rate, forecast accuracy | Demand Planner | Supply Planning Manager | Weekly |
| 6 | AP aging summary: total payables, overdue invoices, payment run schedule | AP Supervisor | Controller | Weekly |
| 7 | Treasury: weekly cash flow forecast (W30 step 8) | Treasury Analyst | CFO | Weekly |

### Monthly

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 8 | Financial statements per entity and consolidated (from W9 close process) | Chief Accountant | Controller | Monthly (by day 5) |
| 9 | Budget vs. actual variance report per entity, per department (from W26) | Controller | CFO | Monthly (by day 7) |
| 10 | Store P&L: revenue, COGS, gross margin, labor cost, occupancy, shrinkage, EBITDA per store | System | Store Ops Director | Monthly (by day 7) |
| 11 | Merchandising performance: category sales, margin, inventory turns, sell-through, vendor rebate realization | Pricing Analyst | VP Merchandising | Monthly (by day 7) |
| 12 | AR aging and collections performance: DSO, overdue %, write-offs | AR Supervisor | CFO | Monthly |
| 13 | HR metrics: turnover rate, time-to-fill, absenteeism, overtime hours, headcount vs. plan | HR Head | CHRO | Monthly |
| 14 | Management committee meeting: CFO presents consolidated results; Department Heads present functional KPIs | CFO / Dept. Heads | CEO | Monthly (by day 10) |

### Quarterly

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 15 | Board pack preparation: consolidated financials, management discussion & analysis, KPI scorecard, risk register update | Controller + CFO | CEO | Quarterly |
| 16 | Vendor performance scorecard review (W44) | Buyer | VP Merchandising | Quarterly |
| 17 | Budget revision (if material changes warranted) (W26 step 13) | Controller | CFO | Quarterly |
| 18 | **Document retention compliance review**: Controller verifies that all document types (invoices, receipts, delivery receipts, import docs, capex records) meet 7-year BIR retention requirements; confirms expired documents are archived and accessible; flags any gaps in document attachment compliance | Controller | CFO | Quarterly |

### Ad-Hoc

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 18 | Department Heads request ad-hoc reports from BI Analyst or self-service via report builder | Dept. Heads / BI Analyst | — | As needed (~20/month) |
| 19 | BI Analyst creates custom analyses: product affinity, customer segmentation, promotional lift analysis, geographic trends | BI Analyst | Requestor | As needed |

### System Touchpoints
- Scheduled report auto-generation and distribution (email, portal, mobile) (W35.1, 4, 8–13)
- Executive dashboard with real-time KPIs (W35.2)
- Store P&L module (W35.10)
- Self-service report builder / ad-hoc query tool (W35.18)
- Mobile dashboard for executives (W35.2)
- Integration with all ERP modules (financials, inventory, POS, procurement, HR, ecommerce) for data aggregation

### Staffing Implication
- **1 BI Analyst** (within IT or Finance): Handles ~20 ad-hoc requests/month + maintains standard report templates + supports self-service tool adoption. This may be a new role or absorbed by a data-savvy Finance team member.
- **Controller**: Monthly reporting adds ~8 hours/month (review + variance analysis + board pack quarterly). Absorbed into existing duties.
- Most standard reports are auto-generated; the human effort is in review, interpretation, and action.

---

## W36. Vendor Onboarding

| Field | Detail |
|---|---|
| **Trigger** | New vendor identified by Buyer or Category Manager (new product sourcing, alternative supplier, new brand) |
| **Frequency** | ~50–100 new vendors/year (replacing churned vendors + new categories) |
| **Volume** | Peaks during seasonal planning (W32) and new store openings (W16) |
| **Owner** | Buyer |
| **Participants** | Buyer, Category Manager, AP Clerk, Finance (credit assessment), IT (portal setup) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Buyer identifies need for new vendor; collects basic information: company name, contact person, product categories offered, business registration | Buyer | Category Manager | 30 min |
| 2 | Buyer sends vendor application form to prospective vendor; vendor provides: DTI/SEC registration, BIR TIN, business permit, tax compliance certificate, bank certificate, product catalog with SRP | Buyer | Category Manager | External (vendor-dependent) |
| 3 | AP Clerk or Finance validates vendor documents: confirms TIN is valid, business permit is current, bank details verified | AP Clerk | AP Supervisor | 30 min |
| 4 | Buyer evaluates vendor capability: product quality (sample review), pricing competitiveness (vs. current vendors), delivery lead time, minimum order quantities, payment terms offered | Buyer | Category Manager | 2–4 hours |
| 5 | Category Manager approves vendor for onboarding (or rejects with reason) | Category Manager | VP Merchandising | 15 min |
| 6 | Buyer creates vendor master record in system: name, TIN, address, contact details, payment terms, bank account, currency, lead time, assigned category, entity(ies) | Buyer | Category Manager | 15 min |
| 7 | System assigns vendor number; configures: approval tier for PO amounts, default PO delivery location(s), matching tolerance for invoice price variance | System | — | Automated |
| 8 | Merchandise Planner maps vendor's product catalog to item master: creates new SKUs or links to existing SKUs; sets vendor-specific cost, lead time, minimum order quantity, order multiple | Merchandise Planner | Buyer | 1–2 hours/vendor (varies by catalog size) |
| 9 | IT configures vendor portal access (if vendor uses portal): credentials, PO visibility, invoice submission capability | IT Team | Buyer | 15 min |
| 10 | Buyer places trial PO (small initial order) to validate vendor reliability, product quality at scale, and delivery performance | Buyer | Category Manager | Per W2 |
| 11 | After 3 trial orders: Buyer completes vendor scorecard baseline (delivery on-time %, quality reject rate, invoice accuracy) for future performance tracking (W44) | Buyer | Category Manager | 30 min |

**Total onboarding cycle**: 2–4 weeks from identification to first PO

### System Touchpoints
- Vendor master creation with document attachments (W36.6)
- TIN validation and business permit tracking with expiry alerts (W36.3, W36.6)
- Vendor-specific configuration: payment terms, tolerance thresholds, approval tiers (W36.7)
- Item-vendor mapping with cost, lead time, MOQ (W36.8)
- Vendor portal provisioning (W36.9)
- Vendor document tracking with expiry alerts: system tracks business permit, tax compliance certificate, and other regulatory document expiry dates; alerts Buyer and AP Clerk 30 days before expiry; vendor blocked from new POs if documents expired
- Integration with vendor performance scorecard (W36.11 → W44)

### Staffing Implication
- **Buyer**: 50–100 new vendors/year × ~4–6 hours of buyer time each = 200–600 hours/year = ~1–3 hours/week. Absorbed across 10–12 buyers.
- **AP Clerk**: 30 min per vendor for document validation = ~25–50 hours/year. Negligible.
- **Merchandise Planner**: Item-vendor mapping is the most labor-intensive step at 1–2 hours per vendor. With 50–100 vendors = ~100 hours/year. Absorbed within existing team.

---

## W37. Loss Prevention & Exception Reporting

| Field | Detail |
|---|---|
| **Trigger** | Daily exception report generation; or real-time alert triggered by POS exception |
| **Frequency** | Daily review; real-time alerts for high-severity exceptions |
| **Volume** | ~500–1,000 exception events/day chain-wide across all 200 stores |
| **Owner** | Loss Prevention Officer (LPO) |
| **Participants** | LPO, Store Manager, Regional Manager, Internal Audit, Cashier, Department Supervisor |

### Background

Shrinkage target: < 1.5% of sales (~PHP 75M/month at risk). Exception-based reporting identifies suspicious transaction patterns at POS and receiving dock that may indicate theft, fraud, or process errors.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System automatically monitors POS transactions in real-time and generates exception alerts for: (a) excessive voids/cancels per cashier, (b) high-value refunds without manager override, (c) manual price overrides, (d) sweet-hearting (repeated transactions with loyalty card of same employee or family), (e) excessive no-sale drawer opens, (f) post-void patterns, (g) high ratio of discount transactions | System | — | Real-time |
| 2 | System generates daily exception summary report per store: top exception categories, top cashiers by exception count, transaction drill-down capability | System | — | Automated (daily) |
| 3 | LPO reviews daily exception report; prioritizes investigation of high-risk patterns (e.g., one cashier with 5× average void rate) | LPO | Internal Audit | 1–2 hours/day |
| 4 | For flagged exceptions: LPO pulls transaction details, CCTV timestamps (cross-reference with security footage), and employee history | LPO | Internal Audit | 30 min/case |
| 5 | If investigation confirms irregularity: LPO documents findings; escalates to Regional Manager and Internal Audit for disciplinary action | LPO | Internal Audit | 1 hour/case |
| 6 | For receiving dock exceptions: system monitors GR short shipments, frequent damage claims from same vendor, and receiving patterns outside scheduled appointments | System | DC Manager | Automated |
| 7 | Monthly: LPO generates shrinkage report per store (inventory adjustment value ÷ sales); flags stores exceeding 1.5% threshold | LPO | Internal Audit | 2 hours/month |
| 8 | Monthly: LPO and Regional Manager review top shrinkage stores; develop action plans (additional training, CCTV repositioning, staffing adjustments) | LPO + Regional Manager | Internal Audit | 1 hour/month per high-shrinkage store |
| 9 | Quarterly: Internal Audit includes POS exception trends in audit findings; recommends system configuration changes (e.g., tighten void approval rules) | Internal Audit | CFO | Quarterly report |
| 10 | System tracks all investigation cases: status (open/investigating/closed), resolution, recovery amount, disciplinary action taken | System | — | Automated |

### System Touchpoints
- Real-time POS exception monitoring with configurable thresholds per exception type (W37.1)
- Daily exception summary report with drill-down to transaction level (W37.2)
- Transaction detail with CCTV timestamp cross-reference capability (W37.4)
- Receiving dock exception monitoring (W37.6)
- Shrinkage report per store with threshold alerting (W37.7)
- Investigation case management with status tracking (W37.10)
- Exception threshold configuration and tuning (W37.9)
- Integration with CCTV system (timestamp correlation, not video storage)

### Staffing Implication
- **2–3 Loss Prevention Officers** (reporting to Internal Audit or a dedicated LP function): Daily review (1–2 hours) + case investigation (5–10 active cases at any time) + monthly shrinkage reporting + quarterly reviews. This is a specialized role that may not exist in the current org chart. Recommend adding 2 LPOs to cover 200 stores (each covering ~70 stores, rotating through physical store visits).
- **Store Managers**: Review their store's exception report daily (~15 min). Absorbed into opening routine.
- **Internal Audit**: Incorporates LP findings into quarterly audit cycle. No incremental headcount.

---

## W38. Special Order / Non-Stock Item Fulfillment

| Field | Detail |
|---|---|
| **Trigger** | Customer requests an item not carried in regular store assortment |
| **Frequency** | ~500–1,000 special orders/month chain-wide; ~2–5 per store per month |
| **Volume** | Primarily professional trade customers (contractors, builders) and project-specific items; avg order value ~PHP 5,000–15,000 |
| **Owner** | Customer Service Rep (order intake); Buyer (fulfillment) |
| **Participants** | CSR, Sales Rep (trade accounts), Buyer, Receiving Clerk, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer requests non-stock item at store (CSR counter) or via Sales Rep; provides product description, specification, quantity needed, and desired delivery date | Customer | — | — |
| 2 | CSR or Sales Rep searches item in system: (a) checks if item exists in item master as non-stock/Special Order type, (b) if not found, creates a non-stock item request with description, specs, and estimated price | CSR / Sales Rep | Dept. Supervisor | 5–10 min |
| 3 | System routes non-stock item creation request to Merchandise Planner for item master setup (category assignment, unit of measure, tax classification) | System | Merchandise Planner | Automated routing |
| 3a | Merchandise Planner creates non-stock SKU in item master with type = "Special Order / Non-Stock"; flags as non-stocking (no ROP, no safety stock, no replenishment) | Merchandise Planner | Category Manager | 10 min |
| 4 | Buyer identifies vendor, obtains quotation (price, lead time, minimum quantity); enters quote in system linked to the non-stock SKU | Buyer | Category Manager | 30–60 min |
| 5 | CSR or Sales Rep communicates quote to customer: price, estimated delivery date, payment terms (typically 50% deposit, 50% on delivery) | CSR / Sales Rep | — | 10 min |
| 6 | Customer confirms order and pays deposit; system records deposit as liability (Cr. Customer Deposits Payable / Dr. Cash); not recognized as revenue until delivery | Customer / Cashier | — | 5 min |
| 7 | System creates Sales Order linked to non-stock SKU with customer deposit recorded; reservation created against incoming PO | System | — | Automated |
| 8 | Buyer creates Special Order PO (links PO to Sales Order); routes for approval per standard tiered matrix (W2) | Buyer | Category Manager | Per W2 |
| 9 | Buyer tracks PO; follows up with vendor on delivery schedule | Buyer | Buyer | Per W2 |
| 10 | Goods received at store or DC (per W3 or W18); system matches GR to both PO and linked Sales Order | Receiving Clerk | Dept. Supervisor | Per W3/W18 |
| 11 | System alerts CSR that special order has arrived; CSR contacts customer for pickup or arranges delivery | System / CSR | Store Manager | Automated + 5 min |
| 12 | Customer picks up item (or receives delivery); pays remaining balance; system recognizes revenue (Dr. Customer Deposits / Cr. Revenue) and COGS (Dr. COGS / Cr. Inventory) at delivery; Sales Order closed | Cashier / CSR | — | 5 min |
| 13 | If customer cancels before PO is placed: CSR cancels Sales Order; deposit refunded; no PO created | CSR | Store Manager | 5 min |
| 14 | If customer cancels after PO is placed but before shipment: Buyer negotiates with vendor (restocking fee, return); Finance processes partial refund less any costs | Buyer + Finance | Category Manager | 30 min |
| 15 | Unclaimed deposit management: system tracks age of customer deposits linked to completed special orders (goods received but not picked up); after 30 days with no customer response post-delivery notification, system sends reminder notification (SMS/email); after 90 days with no response, system flags deposit for review; Store Manager or Finance approves recognition of abandoned deposit as other income (Dr. Customer Deposits Payable / Cr. Other Income); goods dispositioned per standard clearance (W13.9a), RTV (W3.6a), or return to shelf | System / Store Manager / Finance | Controller | Automated + 5 min/review |

**Total cycle time**: 7–30 days from order to delivery (depends on vendor lead time and whether domestic or import)

### System Touchpoints
- Non-stock item type in item master with no auto-replenishment (W38.3a)
- Item creation request workflow (W38.3)
- Sales Order creation with customer deposit and PO linkage (W38.7–8)
- PO-to-Sales-Order reservation and matching (W38.8, W38.10)
- Customer deposit liability tracking (Cr. Customer Deposits Payable) with revenue recognition trigger at delivery (W38.6, W38.12)
- Customer notification upon receipt (W38.11)
- Sales Order lifecycle: open → PO linked → goods received → customer notified → closed (W38.7–12)
- Cancellation handling with deposit refund workflow (W38.13–14)
- Unclaimed deposit aging: system tracks deposit age from goods-receipt date; automated reminder at 30 days; escalation flag at 90 days; abandonment recognition with approval workflow; goods disposition tracking (W38.15)

### Staffing Implication
- **CSR**: ~2–5 special orders/store/month × ~20 min each (intake + communication + handoff) = ~1–1.5 hours/store/month. Absorbed.
- **Buyer**: 500–1,000 special orders/month ÷ 10–12 buyers = ~50–80/buyer/month × ~30 min each = ~30 hours/buyer/month. This is significant. Special orders should be handled by a dedicated 1–2 Buyers who specialize in trade/special orders, with remaining buyers focused on replenishment.
- **Merchandise Planner**: 500–1,000 non-stock SKU creations/year = ~2–4 hours/week. Absorbed within existing team.

---

## W39. Fixed Asset Disposal & Retirement

| Field | Detail |
|---|---|
| **Trigger** | Asset reaches end of useful life, becomes uneconomic to maintain, or is replaced by new asset |
| **Frequency** | ~50–100 asset disposals/year; peaks during store renovations and IT refresh cycles |
| **Volume** | ~8,050 fixed assets across all entities (POS terminals, forklifts, vehicles, fixtures, IT servers, office equipment) |
| **Owner** | Cost Accountant |
| **Participants** | Cost Accountant, Requestor (dept), CFO, IT (for IT assets), Procurement (if resale), Legal (if land/building) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Requestor identifies asset for disposal: reason (end of life, beyond repair, obsolete, replacement, store closure) | Requestor (Dept. Head) | Dept. Head | 15 min |
| 2 | Cost Accountant reviews asset record: original cost, accumulated depreciation, net book value (NBV), remaining useful life, any outstanding encumbrances | Cost Accountant | Controller | 15 min/asset |
| 3 | If NBV is material (> PHP 50,000): Requestor obtains disposal valuation or market quotation for resale | Requestor | Dept. Head | 1–2 hours |
| 4 | Disposal request routed for approval per tier: (a) NBV ≤ PHP 50,000: Controller, (b) NBV PHP 50,001–500,000: CFO, (c) NBV > PHP 500,000: CEO, (d) Land/building: Board | Approver | Approver | 15–30 min |
| 5 | Cost Accountant determines disposal method: (a) trade-in (against new asset purchase), (b) public sale/auction, (c) scrap/recycle, (d) donation, (e) write-off (no residual value) | Cost Accountant | Controller | 15 min/asset |
| 6 | If sale: Procurement or Admin conducts sale; system records proceeds | Procurement / Admin | Controller | Varies |
| 7 | If IT asset: IT ensures data wipe and compliance with Data Privacy Act (RA 10173) before physical disposal | IT Team | CIO | 30 min/asset |
| 8 | Physical disposal or handover executed; asset tag removed; documented with photos | Requestor / Admin | Dept. Head | 30 min/asset |
| 9 | Cost Accountant posts disposal entry in system: (a) remove asset at original cost from fixed asset register, (b) remove accumulated depreciation, (c) recognize gain/loss on disposal = proceeds − NBV (or NBV if scrapped), (d) post to GL disposal P&L account | Cost Accountant | Controller | 15 min/asset |
| 10 | System updates fixed asset register; asset status changed to "Disposed" with disposal date; asset no longer depreciated | System | — | Automated |
| 11 | Quarterly: Cost Accountant reviews disposed assets report; reconciles disposal gain/loss to GL | Cost Accountant | Controller | 30 min/quarter |

### System Touchpoints
- Fixed asset disposal workflow with approval tiers (W39.4)
- Asset record with NBV calculation at any point (W39.2)
- Disposal entry auto-generation: cost removal, depreciation reversal, gain/loss calculation (W39.9)
- Asset status lifecycle: Active → Pending Disposal → Disposed (W39.10)
- Disposal gain/loss reporting (W39.11)
- Integration with W21 (Capex → Asset creation) for full asset lifecycle tracking

### Staffing Implication
- **Cost Accountant**: 50–100 disposals/year × ~30 min each = ~25–50 hours/year = ~2–4 hours/month. Absorbed within existing Finance team.
- No incremental headcount needed.

---

## W40. Regular Price Change Execution

| Field | Detail |
|---|---|
| **Trigger** | Vendor cost increase notification, competitive price adjustment, periodic SRP review, or regulatory price change |
| **Frequency** | ~200–500 SRP changes/month across 35,000 active SKUs; peaks when major vendors announce price increases (typically quarterly) |
| **Volume** | ~10–25 price changes/day; concentrated in categories with commodity-linked pricing (lumber, cement, metals, paint) |
| **Owner** | Pricing Analyst |
| **Participants** | Pricing Analyst, Category Manager, Buyer, IT (price sync) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Buyer receives vendor price increase notice (letter, email, or portal notification); enters new cost and effective date in system | Buyer | Category Manager | 10 min/vendor notice |
| 2 | System calculates margin impact: current SRP × current cost vs. current SRP × new cost; shows margin erosion per SKU and total category impact | System | — | Automated |
| 3 | Pricing Analyst reviews margin impact report; decides action per SKU: (a) absorb cost increase (reduce margin), (b) pass through to SRP, (c) increase SRP partially, (d) negotiate with vendor, (e) switch to alternative vendor, (f) discontinue item | Pricing Analyst | Category Manager | 2–4 hours/vendor notice |
| 4 | Pricing Analyst enters new SRP per SKU with effective date in system; system shows new margin % for validation | Pricing Analyst | Category Manager | 5 min/SKU |
| 5 | Category Manager reviews and approves price changes; VP Merchandising approves if aggregate margin impact > PHP 500K/month | Category Manager / VP | VP Merchandising | 30 min – 1 hour/batch |
| 6 | System schedules price update: new SRP takes effect at configured date/time (typically start of business day) | System | — | Automated |
| 7 | System pushes updated price file to all POS terminals per nightly sync (or immediately if real-time sync configured); updates ecommerce catalog | System | — | Automated |
| 8 | Store Operations receives price change bulletin; Department Supervisors update shelf tags before store opening on effective date | Dept. Supervisor | Store Manager | 30–60 min per price change batch |
| 9 | System maintains full price history per SKU: date range, old SRP, new SRP, reason code, approver — for audit and BIR compliance | System | — | Automated |
| 10 | Monthly: Pricing Analyst generates price change summary report: # of changes, average increase/decrease, margin impact, top categories affected | Pricing Analyst | Category Manager | 1 hour/month |

### System Touchpoints
- Vendor cost change entry with effective date (W40.1)
- Margin impact calculator: current vs. new cost at current SRP (W40.2)
- SRP entry with effective date and margin display (W40.4)
- Approval workflow for price changes with aggregate impact thresholds (W40.5)
- Scheduled price activation (W40.6)
- Price file sync to POS and ecommerce (W40.7)
- Full price history with audit trail (W40.9)
- Price change analytics (W40.10)
- Integration with W13 (promotional pricing — regular and promo prices coexist with date ranges)
- Price protection / retroactive cost adjustment: vendor announces retroactive cost reduction; system calculates credit due based on quantities purchased between effective date and now; generates vendor credit memo (W7.9b); revalues on-hand inventory to new cost if retroactive scope applies; posts difference as reduction in COGS (W40.11)

### Staffing Implication
- **3 Pricing Analysts**: 200–500 changes/month × 5 min/SKU (entry) + 2–4 hours per vendor notice (analysis) = ~60–80 hours/month. With 3 analysts that's ~20–25 hours each. This is a core part of their role alongside promotional pricing (W13). Current team of 3 is adequate.
- **Department Supervisors (stores)**: Shelf tag updates are the most labor-intensive step. With 10–25 price changes/day chain-wide, most stores see only a few changes per week. Shelf tag updates take ~30–60 min per batch. Absorbed into daily opening routine.

---

### Price Protection / Retroactive Cost Adjustment

| Field | Detail |
|---|---|
| **Trigger** | Vendor announces retroactive price reduction (price protection) |
| **Frequency** | Occasional — typically quarterly when commodity-linked vendors adjust prices |
| **Volume** | ~10–20 price protection events/year; concentrated in lumber, cement, steel, paint categories |
| **Owner** | Buyer |
| **Participants** | Buyer, Category Manager, AP Clerk, Cost Accountant, Pricing Analyst |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 11 | Buyer receives vendor price protection notice: new lower cost with effective date (possibly retroactive); enters in system: vendor, SKU(s), old cost, new cost, effective date, scope (future only vs. retroactive) | Buyer | Category Manager | 15 min/event |
| 12 | If retroactive: system calculates credit due based on quantities purchased between effective date and now; generates vendor credit memo per W7.9b | System | Cost Accountant | Automated |
| 13 | If on-hand inventory exists at old cost: system revalues on-hand inventory to new cost; posts difference (Dr. Accounts Payable / Cr. COGS or Inventory) | System / Cost Accountant | Controller | Automated + 15 min review |
| 14 | Buyer communicates new cost to Pricing Analyst for SRP review per standard W40 process | Buyer | Category Manager | Per W40 |

---

## W41. Customer Complaint Resolution

| Field | Detail |
|---|---|
| **Trigger** | Customer submits complaint in-store, by phone (call center), by email/chat, or on website/app |
| **Frequency** | ~2,000–3,000 complaints/month chain-wide; ~10–15 per store per month |
| **Volume** | Categories: product quality (30%), delivery issues (20%), staff behavior (15%), pricing/charging errors (15%), out-of-stock (10%), others (10%) |
| **Owner** | Customer Service Rep (Tier 1) / Customer Service Manager (Tier 2) |
| **Participants** | CSR, CS Manager, Department Supervisor, Store Manager, Buyer, Call Center Agent, Logistics |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer submits complaint via any channel: in-store (CSR counter), phone (call center), email/chat, or website/app form | Customer | — | — |
| 2 | System creates complaint ticket: unique ticket number, channel, customer info (loyalty lookup or guest), category, description, priority (auto-assessed by category) | CSR / Call Center Agent | CS Manager | 5 min |
| 3 | **Tier 1 Resolution** (CSR or Call Center Agent): attempt immediate resolution — (a) product issue: offer exchange (W12), warranty claim (W33), or store credit; (b) pricing error: verify and issue refund; (c) delivery issue: check status, arrange redelivery | CSR / Call Center Agent | CS Manager | 5–15 min |
| 4 | If resolved at Tier 1: CSR closes ticket with resolution code and customer satisfaction rating (if provided) | CSR / Call Center Agent | — | 2 min |
| 5 | If unresolved at Tier 1: ticket escalated to Tier 2 (CS Manager or Store Manager); system reassigns ticket and starts SLA timer | System | CS Manager | Automated |
| 6 | **Tier 2 Resolution** (CS Manager / Store Manager): investigates root cause; coordinates with relevant department (Buyer for product issues, Logistics for delivery, HR for staff complaints) | CS Manager / Store Manager | Store Ops Director | 30–60 min |
| 7 | CS Manager proposes resolution to customer: refund, exchange, discount voucher, written apology, corrective action commitment | CS Manager | Store Ops Director | 15 min |
| 8 | If customer accepts: ticket closed with resolution; system triggers any financial actions (refund, voucher issuance) | CS Manager | — | 5 min |
| 9 | If customer rejects or complaint involves legal/regulatory risk: escalate to Store Ops Director or Legal; system logs escalation | CS Manager | Store Ops Director | 15 min |
| 10 | SLA enforcement: Tier 1 must respond within 4 hours; Tier 2 must resolve within 48 hours; if exceeded, system escalates to Store Ops Director | System | — | Automated |
| 11 | Monthly: CS Manager generates complaint analytics report: volume by category, by store, resolution rate, SLA compliance, top recurring issues | CS Manager | Store Ops Director | 2 hours/month |
| 12 | Monthly: Store Ops Director reviews complaint trends with Department Heads; assigns corrective actions for recurring root causes | Store Ops Director | COO | 1 hour/month |
| 13 | Quarterly: top complaint root causes feed into operational improvement initiatives (training, process changes, vendor quality requirements) | Store Ops Director | COO | Quarterly review |

### System Touchpoints
- Multi-channel complaint ticket creation (in-store, phone, email, chat, web) (W41.1–2)
- Ticket categorization with auto-priority assignment (W41.2)
- Tiered escalation workflow with SLA timers (W41.5, W41.10)
- Resolution code tracking and financial action triggers (refund, voucher) (W41.4, W41.8)
- Customer satisfaction capture at resolution (W41.4)
- Data Subject Access Request (DSAR) handling per RA 10173: system logs DSAR requests (access, correction, deletion, consent withdrawal) with 72-hour acknowledgment and 30-day resolution tracking; supports data anonymization for deactivated accounts after retention period; customer consent preferences viewable and editable via self-service portal (W41.2, W17.2)
- Complaint analytics dashboard: volume, category, store, resolution rate, SLA compliance (W41.11)
- Root cause analysis reporting (W41.12–13)

### Staffing Implication
- **CSRs (stores)**: 10–15 complaints/store/month × ~10 min each = ~2–3 hours/store/month. Absorbed within existing CSR role.
- **Call Center (30 people)**: Handles phone, email, chat, and web complaints. ~1,000–1,500 complaints/month via call center ÷ 30 agents = ~50 complaints/agent/month ÷ 20 working days = ~2.5/day. Each takes ~10–15 min. Manageable; call center also handles inbound inquiries, order tracking, and general support.
- **CS Manager (HQ or regional)**: 1 CS Manager oversees complaint analytics and Tier 2 escalations. May be a regional role (4 Regional CS Managers) or 1 centralized with store managers handling Tier 2 locally.

---

## W42. Annual Physical Inventory Execution

| Field | Detail |
|---|---|
| **Trigger** | Year-end close calendar (typically December 31 or last business day of fiscal year) |
| **Frequency** | Annual; each store and DC counted once per year |
| **Volume** | 35,000 SKUs × 205 locations (200 stores + 5 DCs); executed in coordinated 2-day window |
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

### Count Execution (Day 1 — full count; Day 2 — recounts and adjustments)

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
- System inventory transaction freeze per location (W42.6, W42.15)
- Zone-based count sheet generation with blind count mode (W42.2, W42.7–8)
- RF device / handheld count entry (W42.7)
- Variance detection after count submission (W42.9)
- Recount tracking (W42.10)
- Adjustment approval workflow with tiered authorization (W42.12)
- Bulk inventory adjustment posting and GL impact (W42.14)
- Physical inventory summary reporting (W42.17)

### Staffing Implication
- **All store staff (35/store)**: Mobilized for 2-day count. Stores may close early or operate with skeleton crew during count.
- **DC staff (~150/DC)**: Full DC count requires 1–2 days. Operations paused during count.
- **Cost Accountant**: 20–30 hours for planning, execution support, and reconciliation. Heaviest workload of the year for this role.
- **Internal Audit (3–5 auditors)**: Travel to sampled locations. Absorbed within annual audit plan.
- **IT**: 1 day for count sheet configuration + system freeze/unfreeze support.

---

## W43. Employee Separation & Offboarding

| Field | Detail |
|---|---|
| **Trigger** | Employee submits resignation, or management initiates termination, or employee retires |
| **Frequency** | ~100–130 separations/month (1,200–1,600/year at 15–20% annual turnover) |
| **Volume** | Peaks in January (post-13th month pay resignations) and during store opening months (transfer to new store vs. separation) |
| **Owner** | HR Assistant |
| **Participants** | HR Assistant, HR Head, Department Head, Payroll Officer, IT, Employee |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Employee submits resignation letter (or management issues termination notice) | Employee / Dept. Head | Dept. Head | — |
| 2 | HR Assistant creates separation record in system: resignation date, last working day (30-day notice per Labor Code or garden leave), separation type (resignation, termination, retirement, end of contract) | HR Assistant | HR Head | 10 min |
| 3 | Department Head conducts exit interview; documents feedback (work conditions, compensation, management, reason for leaving) | Dept. Head | HR Head | 30 min |
| 4 | HR Assistant initiates clearance process: system generates clearance form routed to all relevant departments | System | HR Assistant | Automated |
| 5 | **IT clearance**: IT confirms return of laptop/tablet/phone (if issued); deactivates system accounts (ERP, POS, email, VPN); revokes access badges | IT Team | CIO | 15 min/employee |
| 6 | **Department clearance**: Dept. Head confirms return of company property (uniforms, tools, keys); approves final leave usage | Dept. Head | Dept. Head | 10 min/employee |
| 7 | **Finance clearance**: AP Clerk confirms no outstanding cash advances or loans; AR confirms no corporate account exposure | AP / AR Clerk | AP/AR Supervisor | 10 min/employee |
| 8 | **Store Operations clearance** (if store employee): Store Manager confirms no pending inventory accountability issues, cash drawer reconciled | Store Manager | Store Ops Director | 10 min/employee |
| 9 | HR Assistant collects all signed clearances; marks clearance as complete in system | HR Assistant | HR Head | 10 min/employee |
| 10 | Payroll Officer computes final pay per W10 step 12: pro-rated salary, pro-rated 13th month pay, converted unused leave credits (VL to cash per company policy), less outstanding loans/advances and clearance deductions | Payroll Officer | Payroll Manager | Per W10 |
| 11 | System generates final pay as separate payroll run or adjustment; final payslip issued (W10 step 13) | System | — | Automated |
| 12 | System updates employee status to "Separated"; deactivates payroll processing; retains record for regulatory retention (7 years) | System | — | Automated |
| 13 | System generates COE (Certificate of Employment) on request: dates of employment, position, compensation range (optional) | System / HR Assistant | HR Head | 5 min/request |
| 14 | HR Head includes separation data in monthly turnover report: rate by department, store, and separation type; exit interview themes | HR Head | CHRO | 1 hour/month |

**Total cycle time**: 30 days (notice period) + 5 business days after last day for final pay release

### System Touchpoints
- Separation record creation with type classification (W43.2)
- Automated clearance form generation and routing (W43.4)
- Clearance status tracking per department (W43.5–9)
- System account deactivation trigger (W43.5)
- Final pay computation with pro-ration and deductions (W43.10–11)
- Employee status lifecycle: Active → On Notice → Separated (W43.12)
- Certificate of Employment generation (W43.13)
- Turnover analytics (W43.14)
- Integration with W10 (payroll) and W15 (onboarding — reverse process)

### Staffing Implication
- **HR Assistants (2)**: 100–130 separations/month × ~45 min admin each (clearance coordination + documentation) = ~90 hours/month. With 2 assistants that's ~45 hours each. Manageable alongside other HR admin duties.
- **IT**: 100–130 deactivations/month × 15 min each = ~30 hours/month. Absorbed by IT helpdesk.
- **Department Heads / Store Managers**: ~20 min per separating employee for clearance. With ~100/month spread across 200 stores, most managers handle < 1 separation/month. Negligible impact.

---

## W44. Vendor Performance Review

| Field | Detail |
|---|---|
| **Trigger** | Quarterly review calendar; or ad-hoc triggered by persistent quality/delivery issues |
| **Frequency** | Quarterly for top 50 vendors (by spend); annually for remaining active vendors |
| **Volume** | ~800–1,000 active vendors; top 50 = 45% of COGS |
| **Owner** | Buyer |
| **Participants** | Buyer, Category Manager, VP Merchandising, Receiving Supervisor (quality input), AP Supervisor (invoice accuracy input) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System auto-generates vendor scorecard per vendor for the review period with the following metrics: | System | — | Automated |
| | • **On-time delivery %**: PO lines delivered on or before promised date ÷ total PO lines | | | |
| | • **Fill rate %**: PO lines delivered at full ordered quantity ÷ total PO lines | | | |
| | • **Quality reject rate %**: GR lines rejected for quality ÷ total GR lines | | | |
| | • **Invoice accuracy %**: Invoices matching PO within tolerance on first submission ÷ total invoices | | | |
| | • **Lead time variance**: avg actual lead time vs. agreed lead time (days) | | | |
| | • **Return rate %**: RTV lines ÷ total receipt lines | | | |
| 2 | Buyer reviews scorecard; adds qualitative notes: vendor responsiveness, market reputation, new product pipeline, relationship quality | Buyer | Category Manager | 15–30 min/vendor |
| 3 | Buyer assigns overall rating: A (Preferred), B (Acceptable), C (Watch), D (Probation), F (Exit) | Buyer | Category Manager | 5 min/vendor |
| 4 | For C-rated vendors: Buyer drafts improvement plan with specific targets and timeline; communicates to vendor | Buyer | Category Manager | 30 min/vendor |
| 5 | For D/F-rated vendors: Buyer escalates to Category Manager for decision: (a) put on probation with 90-day improvement deadline, (b) initiate vendor exit process (transition to alternative vendor, settle outstanding obligations) | Buyer | VP Merchandising | 1 hour/vendor |
| 6 | Quarterly: Category Manager and VP Merchandising review top 50 vendor scorecards in portfolio review meeting; discuss strategic vendor relationships, negotiate improved terms for A-rated vendors | Category Manager | VP Merchandising | 2 hours/quarter |
| 7 | Annually: VP Merchandising and CFO review total vendor portfolio performance; approve vendor list for next year; authorize new vendor onboarding (W36) and vendor exits | VP Merchandising + CFO | CEO | 4 hours/year |
| 8 | System maintains vendor scorecard history for trend analysis; supports vendor selection decisions in W2 and W36 | System | — | Automated |

### System Touchpoints
- Automated vendor scorecard generation from operational data (W44.1)
- Multi-metric scoring: on-time delivery, fill rate, quality, invoice accuracy, lead time, return rate (W44.1)
- Vendor rating system with configurable thresholds (W44.3)
- Improvement plan tracking (W44.4)
- Vendor lifecycle status: Active → Probation → Exit (W44.5)
- Scorecard history and trend analysis (W44.8)
- Integration with W2 (PO performance), W3 (receiving quality), W7 (invoice matching), W36 (vendor onboarding)

### Staffing Implication
- **Buyers**: Top 50 vendors reviewed quarterly × 30 min = 25 hours/quarter. Remaining ~750 vendors reviewed annually × 15 min = ~190 hours/year. Total ~290 hours/year ÷ 10 buyers = ~29 hours/buyer/year. Absorbed within existing buyer duties.
- **Category Managers**: 2 hours/quarter for portfolio review + 1 hour/quarter for escalations = ~12 hours/year. Absorbed.
- **VP Merchandising**: 2 hours/quarter for top vendor review + 4 hours/year for annual portfolio review = ~12 hours/year. Absorbed.

---

## W45. Store Closure / Relocation

| Field | Detail |
|---|---|
| **Trigger** | Persistent underperformance, lease expiry non-renewal, market exit, or relocation to better site |
| **Frequency** | Occasional (estimated 2–5 closures/relocations per year as network matures to 300+ stores) |
| **Volume** | 1 store at a time; each takes 2–3 months from decision to final close-out |
| **Owner** | Store Operations Director |
| **Participants** | COO, Store Ops Director, Real Estate (Property Mgmt Inc.), IT, Finance, HR, Supply Chain, Marketing |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Store performance review triggers closure decision: sustained negative EBITDA, declining foot traffic, lease renewal at unfavorable terms, or strategic market exit | Store Ops Director / CFO | CEO | Decision meeting |
| 2 | CEO and Board approve closure/relocation; Store Ops Director appointed as closure lead | CEO / Board | CEO | Board meeting |
| 3 | Property Mgmt Inc. negotiates lease termination with landlord; settles any penalties or early termination fees | Property Mgmt Inc. | CFO | 2–4 weeks |
| 4 | Supply Planner creates mass inventory redistribution plan: system generates transfer orders from closing store to nearest stores and serving DC; prioritizes by item velocity and destination need | Supply Planner | Supply Planning Manager | 1 week |
| 5 | DC and receiving stores process inbound transfers per standard receiving (W22, W3); closing store picks and ships inventory in waves over 1–2 weeks | Closing Store Staff | DC Supervisor / Store Manager | 1–2 weeks |
| 6 | HR initiates employee action: (a) redeploy high-performers to nearby stores (transfer, not separation), (b) offer voluntary separation to others, (c) process separations per W43 for staff not redeployed; peak: up to 35 separations per store | HR Assistant / HR Head | CHRO | 2–4 weeks |
| 7 | Marketing executes customer communication plan: notify loyalty members of closure, redirect to nearest store, offer relocation promotion (e.g., extra loyalty points at new nearest store), update store locator on website/app | Marketing | CMO | 2 weeks |
| 8 | Customer Service handles inbound inquiries from trade/corporate accounts; reassigns accounts to nearest store's Sales Rep or Regional Manager | CS Manager / Sales Rep | Store Ops Director | 1 week |
| 9 | AR Clerk reviews and collects any outstanding trade/corporate account balances specific to closing store location | AR Clerk | AR Supervisor | 2 weeks |
| 10 | IT decommissions store infrastructure: POS terminals, network equipment, RF devices (reverse of W16.3); deactivates store location in ERP system; removes from price file and replenishment routing | IT Team | CIO | 1 week |
| 11 | Cost Accountant disposes store fixtures and fixed assets per W39 (disposal/retirement); capitalizes any leasehold improvement write-offs | Cost Accountant | Controller | Per W39 |
| 12 | System deactivates store location master: location status set to "Closed"; no further transactions posted; location excluded from reports and dashboards | IT / Controller | CFO | Automated + 15 min |
| 13 | Controller runs final store P&L and balance sheet reconciliation: all inventory cleared, all AP/AR settled, all assets disposed; final profit/loss on closure recognized | Controller | CFO | 1 day |
| 14 | Post-closure: system retains closed store data for 7-year retention period (BIR); historical data accessible for reporting but location excluded from active operations | System | — | Automated |

**Total closure cycle**: 2–3 months from decision to final close-out

### System Touchpoints
- Mass transfer order generation from closing store to multiple destinations (W45.4)
- Store location deactivation: status change, transaction blocking, removal from active reporting (W45.12)
- Employee redeployment (transfer between locations in same entity) vs. separation processing per W43 (W45.6)
- Fixed asset disposal trigger for store-specific assets per W39 (W45.11)
- Customer account reassignment to new default store (W45.7)
- Trade/AR account collection and reassignment (W45.8–9)
- Final store financial close-out with closure P&L recognition (W45.13)
- Closed location data retention with restricted access (W45.14)

### Staffing Implication
- **Store Ops Director**: Leads closure process. ~20 hours per closure spread over 2–3 months.
- **Supply Planner**: Mass redistribution planning adds ~1 week per closure. Absorbed within existing team.
- **HR**: Up to 35 separations + redeployments per closure. Absorbed within existing HR team with advance planning.
- **IT**: 1 week per store decommission. 2–3 IT staff per closure. With 2–5 closures/year, this is ~5–15 staff-weeks. Absorbed within existing IT team.
- **Finance**: Final P&L close-out adds ~1 day per closure. Absorbed.

---

## Workflow-to-Headcount Summary

### HQ Departments

| Department | Roles | Count | Key Workflows | Validation |
|---|---|---|---|---|
| **Merchandising & Buying** | VP, Category Managers, Buyers, Pricing Analysts, Merch Planners | ~40 | W1, W2, W13, W20, W23, W27, W29, W32, W36, W40, W44 | ✅ Adequate for daily PO review + quarterly assortment cycles + VMI/consignment oversight + rebate management + seasonal planning + vendor onboarding + price maintenance |
| **Finance & Accounting** | Controller, Chief Accountant, AP/AR Clerks, Treasury, Tax | ~35 | W7, W8, W9, W14, W21, W24, W25, W26, W27, W28, W30, W39, W42 | ✅ Stretched during close week; capex/credit/petty cash absorbed; treasury daily cycle manageable with 2–3 analysts; asset disposal and annual physical inventory absorbed |
| **Supply Chain & Logistics** | Supply Planners, Demand Planners, Import Coordinator, DC Ops managers | ~30 | W3, W4, W19, W22, W31 | ✅ 2–3 planners handle replenishment + transfers; home delivery picked by DC staff; 1–2 dedicated demand planners handle forecasting |
| **HR & Payroll** | HR Head, Recruitment, Payroll, HR Assistants | ~15 | W10, W15 | ✅ 2–3 payroll officers + 2 recruiters handle the volume |
| **Marketing** | Brand, Promo, Loyalty, Ecommerce, Digital | ~20 | W13, W17 | ✅ Loyalty is largely automated; promo work is cyclical |
| **Store Operations** | Director, Regional Managers, CS Manager, Ops Standards | ~22 | W5, W16, W29, W5d, W34, W37, W41 | ✅ 4 Regional Managers × 50 stores each; oversee new openings; offline recovery is Store Mgr responsibility; shift scheduling and complaint handling absorbed; 2–3 LPOs recommended for loss prevention |
| **IT** | Infrastructure, Apps, Data, Security, BI Analyst | ~26 | W16 (store setups), W35 (reporting) | ✅ 2–3 per store setup + BAU support; 1 BI Analyst supports management reporting |
| **Other** | Legal, Internal Audit, Customer Service (call center), Executive | ~50 | W41 (complaints), W42 (audit observation) | ✅ Support functions; call center handles multi-channel complaint intake |

### Per-Store Staffing (35 people)

| Role | Count | Key Workflows | Workload Validation |
|---|---|---|---|
| Store Manager | 1 | W5 (open/close), W6 (approvals), W12 (returns), W16 (opening) | Manageable; delegates floor ops to supervisors |
| Asst. Store Manager | 1 | W5 (open/close backup), W6, W12 | Shares management load; covers days off |
| Dept. Supervisors | 4 | W5b (floor selling), W6 (cycle count review), W12 (restock) | 4 depts × 1 supervisor; handles floor + counts |
| Sales Associates | 16 | W5b (selling, paint mixing, lumber cutting), W11 (BOPIS pick) | 4/dept × 2 shifts = adequate for floor coverage |
| Cashiers | 6 | W5b (checkout), W17 (loyalty scan), W28 (gift card sell/reload) | 5 terminals + 1 float; 2 shifts of 3; tight on coverage |
| Receiving Clerks | 2 | W4 (store receiving from DC), W18 (DSD receiving), W22 (transfer receiving) | 2–3 DC trucks/week + 2–3 DSD/week + transfers; 2 clerks in shifts handle it |
| Stock Associates | 3 | W4 (shelf stocking), W6 (cycle counting), W11 (BOPIS pick), W18 (DSD shelving), W22 (transfer pick/receive), W34 (shift adherence), W42 (annual count) | 700 SKUs/day counting + stocking + DSD + transfers; adequate but minimal slack |
| Customer Service Rep | 1 | W11 (BOPIS handoff), W12 (returns), W24 (credit application assistance), W28 (store credit), W29 (recall returns), W33 (warranty claims), W38 (special order intake), W41 (complaints) | ~4 BOPIS + ~2 returns + ~0.5 gift cards + ~2 warranty claims + ~0.5 special orders + ~10 complaints/day = moderate; also handles special orders |
| Maintenance | 1 | W5c (closing checklist), general upkeep | Standard for big-box format |
| **Total** | **35** | | **Validated — headcount is lean but supportable** |

### Per-DC Staffing (~150 people)

| Function | Count | Key Workflows | Workload Validation |
|---|---|---|---|
| DC Manager + Supervisors | 5 | W3, W4 (oversight) | 1 manager + 4 shift/area supervisors |
| Receiving | 10–13 | W3 (receiving & putaway), W20 (VMI receipt) | ~40 receipts/day × 1.5–3 hrs; 3–4 clerks + 4–6 putaway + 1–2 QC |
| Picking & Packing | 25–30 | W4 (pick/pack/ship), W19 (home delivery pick/pack) | ~33 store orders + ~23 home delivery orders/day; 15–20 pickers + 8–10 packers |
| Loading & Dispatch | 6–8 | W4 (loading) | Multi-drop truck loading; 4–6 crew + dispatch |
| Inventory Control | 2–3 | W6 (DC cycle counts) | DC-level accuracy monitoring |
| Admin & Support | 5–8 | Admin, safety, maintenance | Office, security, equipment maintenance |
| Special Handling (lumber, tiles, paint) | 8–10 | W3, W4 (special areas) | Dedicated teams for heavy/hazardous goods |
| **Total** | **~150** | | **Validated** |

---

## W46. Kit / Bundle Assembly & Disassembly

| Field | Detail |
|---|---|
| **Trigger** | Kit demand (auto-assembly) or planned batch assembly schedule |
| **Frequency** | ~200–400 kit assemblies/month across DCs; primarily tool sets, bathroom combo kits, paint starter kits |
| **Volume** | ~50–100 active kit SKUs |
| **Owner** | DC Supervisor |
| **Participants** | Merchandise Planner (BOM setup), DC Assembly Staff, DC Supervisor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Merchandise Planner defines kit Bill of Materials (BOM) in item master: kit SKU + component SKUs with quantities per unit; kit item type = 'Kit / Bundle' | Merchandise Planner | Category Manager | 15 min/kit |
| 2 | Assembly triggered by: (a) demand-driven — system auto-generates assembly order when kit is ordered (ecommerce) or picked (store replenishment) but insufficient kit stock exists, or (b) planned batch — DC Supervisor schedules weekly assembly of popular kits based on forecast | System / DC Supervisor | DC Supervisor | 5 min |
| 3 | System creates assembly order: lists required component quantities; checks component availability at DC; reserves components against assembly order | System | — | Automated |
| 4 | If component shortage: DC Supervisor alerts Buyer for expedited replenishment or suggests substitution (with Merchandise Planner approval) | DC Supervisor | Supply Planning Manager | 10 min |
| 5 | Assembly Staff picks components from DC bins per assembly order; scan-confirms each component | Assembly Staff | DC Supervisor | 10–30 min/kit |
| 6 | Assembly Staff assembles kit (physical packaging, labeling, shrink-wrap); applies kit barcode label | Assembly Staff | DC Supervisor | 5–15 min/kit |
| 7 | System consumes component inventory (decreases) and creates kit inventory (increases); kit cost = sum of component WAC at time of assembly | System | — | Automated |
| 8 | Kit received into finished goods storage location in DC; available for picking and shipping | Assembly Staff | DC Supervisor | 5 min |
| 9 | Kit disassembly (if components needed individually): DC Supervisor initiates disassembly order; system reverses process — consumes kit inventory, restores component inventory at original component WAC; disassembly labor posted to overhead | DC Supervisor | DC Manager | 10 min |

### System Touchpoints
- Kit BOM definition in item master with component quantities (W46.1)
- Assembly order auto-generation triggered by demand or planned schedule (W46.2–3)
- Component availability check and reservation against assembly order (W46.3)
- Component consumption and kit creation with automatic costing (W46.5–7)
- Kit disassembly with component restoration (W46.9)
- Kit inventory tracked separately from components; kit excluded from ROP/replenishment (assembled on demand)

### Staffing Implication
- **DC Assembly Staff**: ~200–400 assemblies/month × 20 min average = ~70–130 hours/month. With 5 DCs, that's ~15–25 hours/DC/month. Absorbed by existing DC staff (within ~150/DC) as a scheduled weekly activity.
- **Merchandise Planner**: ~50–100 active kits × initial setup + occasional BOM updates = ~4–6 hours/month. Absorbed.

---

## Workflow-to-System Touchpoint Map

Summary of which ERP modules support which workflows:

| ERP Module | Workflows Supported |
|---|---|
| **POS / Retail** | W5 (store selling, offline recovery, void transactions), W12 (returns, split-tender refunds), W17 (loyalty at POS), W18 (DSD receiving), W23 (consignment sale), W28 (gift card/store credit), W29 (recall blocking), W33 (warranty claims), W38 (special order deposit) |
| **Inventory Management** | W3 (GR posting, shelf-life/expiry tracking), W4 (replenishment, FEFO picking), W6 (cycle counting, near-expiry alerting), W11 (BOPIS pick), W18 (DSD GR, shelf-life capture), W20 (VMI stock), W22 (transfers), W23 (consignment tracking, consignment returns), W29 (recall quarantine), W37 (shrinkage tracking), W42 (annual physical inventory), W46 (kit assembly/disassembly), negative inventory resolution |
| **Procurement** | W2 (PO cycle), W3 (receiving vs. PO), W18 (DSD PO/GR), W20 (VMI ASN), W21 (capex PO), W36 (vendor onboarding), W38 (special order PO) |
| **Warehouse Management** | W3 (putaway, cross-dock, forward-pick replenishment), W4 (pick/pack/ship), W19 (home delivery pick/pack), W22 (transfer pick), W42 (DC count), W46 (kit assembly) |
| **Financials (GL/AP/AR)** | W7 (AP, EWT, vendor credit memos, non-PO recurring expenses), W8 (AR, credit hold override), W9 (close, NRV review), W14 (intercompany), W21 (capex & FA), W24 (credit approval), W25 (petty cash), W26 (budget), W27 (rebates), W28 (gift card liability), W30 (treasury & cash management, ecommerce payment reconciliation), W39 (asset disposal), W42 (inventory adjustments) |
| **Supply Chain Planning** | W2a (auto-replenishment), W4 (replenishment calculation), W22 (transfer planning), W27 (rebate accrual triggers), W31 (demand forecasting, multi-echelon DC replenishment sourcing), W32 (seasonal buy planning) |
| **HR & Payroll** | W10 (payroll), W15 (onboarding), W34 (shift scheduling), W43 (separation & offboarding) |
| **Ecommerce** | W11 (BOPIS order flow), W12b (online returns), W19 (home delivery fulfillment, payment reconciliation, 3PL management) |
| **CRM / Loyalty** | W17 (loyalty program, manual points adjustment, customer deduplication), W24 (credit application), W41 (complaint management) |
| **Pricing / Merchandising** | W13 (promotions, pricing conflict rules), W27 (vendor rebates), W40 (regular price changes, price protection) |
| **Master Data** | W1 (SKU lifecycle, sample/demo inventory, slow-mover review), W16 (new store/location creation, capex project tracking), W20 (VMI item setup), W23 (consignment item setup), W36 (vendor onboarding), W38 (non-stock item creation, unclaimed deposit aging), W46 (kit BOM) |
| **Reporting / Analytics** | W1 (assortment analysis), W9 (financial statements), W13 (promo analysis), W19 (delivery performance), W21 (capex vs. budget), W26 (budget variance), W27 (rebate ROI), W28 (gift card liability), W29 (recall tracking), W30 (cash flow forecast), W31 (forecast accuracy), W35 (management reporting rhythm), W37 (shrinkage/exception reports), W40 (price change analytics), W41 (complaint analytics), W42 (physical inventory summary), W44 (vendor scorecards) |
| **Loss Prevention** | W37 (POS exception monitoring, shrinkage tracking) |
| **Store Lifecycle** | W16 (new store opening), W45 (store closure / relocation) |

---

*Document Version: 8.0 | Date: 2026-05-30 | Wave 5 gap analysis: added W7c (Non-PO AP), W5b.10 (void transactions), W38.15 (unclaimed deposits); expanded W1 (slow-mover review, negative inventory), W3 (shelf-life/expiry tracking), W4 (FEFO picking), W5c (split-tender refunds via W12), W6 (near-expiry alerting), W12 (split-tender refunds), W16 (capex project tracking), W17 (manual points adjustment, customer dedup), W18 (shelf-life capture), W19 (ecommerce payment reconciliation, 3PL management), W23 (consignment return logistics), W31 (multi-echelon DC sourcing); fixed revenue math in model-company-profile §9.4 (PHP 5.19B total)*
