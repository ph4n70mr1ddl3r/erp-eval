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
| 7 | Approved PO transmitted to vendor (email, EDI, or vendor portal) | System / Buyer | Buyer | Automated |
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

### Staffing Implication
- **10–12 Buyers**: ~60 POs/day ÷ ~15 min review each = 15 hours/day. With 10 buyers that's 1.5 hours each for PO work, plus follow-ups. Reasonable with other duties.
- **1 Import Coordinator**: 20–30 active import POs at any time (45–90 day lead times). Each requires ~30 min/day tracking = 10–15 hours/week. One coordinator is sufficient.
- **2–3 Treasury Analysts** (in Finance): Handle LC opening, payment runs, and reconciliation alongside other AP duties.

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
| 6a | If damaged goods: Receiving Clerk creates damage report with photos; initiates one of: (a) Return to Vendor (RTV) via Buyer, (b) scrap with DC Supervisor authorization, or (c) insurance claim for insured shipments | Receiving Clerk | DC Supervisor | 10 min |
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

### System Touchpoints
- PO/TO lookup at receiving dock (W3.2)
- Barcode/RF scanning against PO (W3.4)
- Discrepancy flagging and Buyer notification (W3.6)
- Damage disposition workflow: RTV initiation, scrap authorization, insurance claim capture (W3.6a–c)
- Goods Receipt posting → inventory update (W3.7)
- Putaway direction (zone, bin, velocity-based) (W3.8)
- Cross-dock allocation to outbound orders (cross-dock variant)

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
| 5 | If loyalty member: Cashier scans loyalty card or asks for mobile number | Cashier | — | 15 sec |
| 6 | System calculates totals: applies promos, quantity breaks, loyalty discounts | System | — | Automated |
| 7 | Customer pays (cash, card, e-wallet, split tender) | Cashier | — | 30–60 sec |
| 8 | Receipt printed; inventory deducted in real-time | System / Cashier | — | 15 sec |
| 9 | Age-restricted items trigger cashier confirmation prompt | Cashier | Store Manager | 10 sec |

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
- Catch-weight / variable measure selling with weight/length capture and auto-price calculation (W5b.2)
- Custom SKU generation for paint mixing (W5b.3)
- Age-restricted product prompts (W5b.9)
- Z-report generation (W5c.2)
- Cash reconciliation / variance reporting (W5c.3–4)
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
| 3 | Physically count each SKU in assigned section; enter quantity into device | Stock Associate | Department Supervisor | 2–3 hours (700 SKUs ÷ ~10 sec each) |
| 4 | System compares physical count to system count; flags variances | System | — | Automated |
| 5 | For flagged items: Stock Associate recounts (blind recount) | Stock Associate | Department Supervisor | 15–30 min |
| 6 | If variance confirmed: Department Supervisor reviews and approves adjustment | Dept. Supervisor | Store Manager | 15 min |
| 7 | If adjustment > PHP 10,000 or > 5% of SKU value: Store Manager approval required | Store Manager | Store Manager | 5 min each |
| 8 | System posts inventory adjustment; audit trail recorded | System | — | Automated |
| 9 | Root cause analysis for recurring variances (theft, damage, receiving errors) | Dept. Supervisor | Store Manager | Weekly review |

**Cycle**: 35,000 SKUs ÷ 700/day = 50 working days per full cycle (~10 weeks ≈ quarterly)

### System Touchpoints
- Automated count assignment by zone/section (W6.1)
- RF device / handheld count entry (W6.3)
- Variance detection and blind recount workflow (W6.4–5)
- Inventory adjustment with tiered approval (W6.6–7)
- Immutable audit trail for all adjustments (W6.8)

### Staffing Implication
- **3 Stock Associates per store**: Each spends 2–3 hours/day on cycle counting, remainder on replenishment and receiving. The 700 SKU/day target requires focused effort. With 3 associates rotating, workload is distributed. Current count of 3 is adequate but has no slack for absenteeism.

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
| 1 | AP Clerk receives and scans/logs vendor invoice | AP Clerk | AP Supervisor | 5 min/invoice |
| 2 | System attempts auto-match: PO → Goods Receipt → Invoice (3-way match) | System | — | Automated |
| 3 | If matched (quantities and price within tolerance): auto-approve for payment | System | AP Supervisor | Automated |
| 4 | If mismatch (price, quantity, or missing GR): route to AP Clerk for review | AP Clerk | AP Supervisor | 10 min/invoice |
| 5 | If price discrepancy: AP Clerk contacts Buyer for resolution | AP Clerk | Buyer | 15 min/invoice |
| 6 | If quantity discrepancy (partial receipt): verify GR status; wait for remaining delivery or adjust | AP Clerk | AP Supervisor | 10 min/invoice |
| 6a | Exception SLA: all unmatched invoices must be resolved within 5 business days; system tracks aging of exceptions | System | AP Supervisor | Automated |
| 6b | If exception unresolved after 5 days: system escalates to AP Supervisor; AP Supervisor coordinates with Buyer and vendor for resolution | AP Supervisor | Controller | 15 min/invoice |
| 7 | Approved invoices queued for payment per vendor terms (Net 30, Net 60) | System | — | Automated |
| 8 | AP Supervisor reviews AP aging weekly; prioritize payments by due date and vendor relationship | AP Supervisor | CFO | 2 hours/week |
| 9 | Twice-weekly payment run: system generates payment file (checks, bank transfers) | AP Clerk | AP Supervisor | 1 hour/run |
| 10 | Treasury reviews and approves payment batch; transmits to bank | Treasury Analyst | CFO | 30 min/run |
| 11 | System posts payment; updates vendor balance | System | — | Automated |

**Match rate target**: ≥ 80% auto-matched (no manual intervention)

### System Touchpoints
- Invoice scanning / OCR / digital capture (W7.1)
- 3-way match engine (PO → GR → Invoice) (W7.2)
- Auto-approval with tolerance thresholds (W7.3)
- Exception routing and workflow (W7.4–6)
- Exception aging tracker with SLA enforcement and auto-escalation at day 5 (W7.6a–b)
- AP aging report (W7.8)
- Payment file generation (bank formats) (W7.9–10)

### Staffing Implication
- **8–10 AP Clerks**: 217 invoices/day × 5 min (logging) = ~18 hours for basic processing. With ~20% requiring manual resolution at 25 min each = ~20 additional hours. Total ~38 hours/day. With 8 clerks that's ~5 hours each. Reasonable with payment runs and other duties.
- **1 AP Supervisor**: Oversight, aging review, escalations.
- **2 Treasury Analysts**: Payment approval, bank file transmission, LC management. Shared with AR and other treasury duties.

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
| 3 | AR: Post all AR invoices and payments received through month-end | AR Clerk | Controller | 1 hour |
| 4 | Accruals: Book accrual entries for expenses incurred but not yet invoiced (utilities, freight, rent) | Chief Accountant | Controller | 3 hours |
| 5 | Intercompany: Verify all IC transactions are posted; run IC matching | Chief Accountant | Controller | 2 hours |
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
- Accrual and journal entry workflow (W9a.4–8, 11)
- IC matching and elimination automation (W9a.5, 13)
- Inventory valuation engine (W9a.6)
- Bank reconciliation (W9a.9)
- Multi-entity financial statement generation (W9a.12–14)
- Period lock / close controls (W9a.17)
- BIR tax form generation (W9a.16)

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
| 6 | System processes refund (original tender method) or issues store credit | System / CSR | — | 2 min |
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
| 10 | Pricing Analyst generates post-promo analysis (lift, cannibalization, margin erosion) | Pricing Analyst | Category Manager | 2 hours/promo |

### System Touchpoints
- Promotional price setup with date-effective pricing (W13.2)
- Approval workflow for promotional prices (W13.3)
- Scheduled push of promo prices to POS (W13.5)
- Auto-application at POS without cashier intervention (W13.7)
- Real-time promo performance dashboard (W13.8)
- Automatic price reversion and clearance flagging (W13.9)
- Post-promo analysis reporting (W13.10)
- Digital coupon / online promo code management: creation of coupon codes with validity dates, usage limits, and channel restrictions (in-store, online, or both); redemption tracking across channels; synchronization with ecommerce platform (W13.2, W13.5)

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
| 7 | HR Assistant creates employee record in system (personal info, position, salary, entity, tax status) | HR Assistant | HR Head | 30 min |
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
| 2 | System creates loyalty account with tier status (Bronze default) | System | — | Automated |
| 3 | At each POS transaction, cashier scans loyalty card or enters mobile number | Cashier | — | 15 sec |
| 4 | System calculates points earned (1 point per PHP 100 spent) and updates balance | System | — | Automated |
| 5 | Customer checks points balance via app, receipt, or in-store kiosk | Customer | — | Self-service |
| 6 | At checkout, customer requests points redemption; cashier selects redemption option | Cashier | — | 30 sec |
| 7 | System validates sufficient points; converts to peso value; applies as discount | System | — | Automated |
| 8 | Monthly: Loyalty Manager reviews tier movement (upgrade/downgrade based on trailing 12-month spend) | System | Loyalty Manager | Automated + 1 hour review |
| 9 | Monthly: generate loyalty program report (enrollment, active rate, points liability, redemption rate) | System | Loyalty Manager | 30 min |
| 10 | Quarterly: Loyalty Manager plans double-points weekends and member-exclusive promos | Loyalty Manager | CMO | 2 hours/quarter |
| 11 | Annual: points expiry batch run (points unused after 24 months expire) | System | Loyalty Manager | Automated |

### System Touchpoints
- Loyalty enrollment (in-store, online, app) (W17.1–2)
- Points earning at POS with real-time update (W17.3–4)
- Points balance inquiry (app, receipt, kiosk) (W17.5)
- Points redemption at POS as payment method (W17.6–7)
- Tier auto-calculation based on trailing spend (W17.8)
- Loyalty analytics dashboard (W17.9)
- Scheduled points expiry (W17.11)

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
- Order routing to nearest fulfillment location (W19.2)
- WMS pick task generation and assignment (W19.3–4)
- Out-of-stock substitution/cancellation (W19.5)
- Shipping label and packing slip generation (W19.6)
- Delivery partner API integration for order creation and tracking (W19.7, W19.8, W19.10)
- Customer notification (SMS/email) with tracking link (W19.9)
- Proof of delivery capture (W19.10)
- Failed delivery / return-to-origin handling (W19.12)

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
| 6 | At sale: system records sell-through event; ownership transfers from vendor to company to customer | System | — | Automated |
| 7 | Monthly: system generates consignment sell-through report per vendor (units sold × consignment price) | System | Buyer | Automated |
| 8 | Buyer reviews and confirms settlement report | Buyer | Category Manager | 1 hour/vendor/month |
| 9 | AP Clerk processes consignment vendor payment based on confirmed sell-through | AP Clerk | AP Supervisor | Per W7 |
| 10 | Quarterly: Buyer reviews consignment SKU performance; returns slow movers to vendor | Buyer | Category Manager | 2 hours/quarter |

### System Touchpoints
- Consignment item flagging in item master (W23.2)
- Non-valuated inventory receipt and tracking (W23.4)
- Ownership transfer at point of sale (W23.6)
- Consignment sell-through report generation (W23.7)
- AP settlement from sell-through data (W23.9)

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

## Workflow-to-Headcount Summary

### HQ Departments

| Department | Roles | Count | Key Workflows | Validation |
|---|---|---|---|---|
| **Merchandising & Buying** | VP, Category Managers, Buyers, Pricing Analysts, Merch Planners | ~40 | W1, W2, W13, W20, W23, W27, W29 | ✅ Adequate for daily PO review + quarterly assortment cycles + VMI/consignment oversight + rebate management |
| **Finance & Accounting** | Controller, Chief Accountant, AP/AR Clerks, Treasury, Tax | ~35 | W7, W8, W9, W14, W21, W24, W25, W26, W27, W28, W30 | ✅ Stretched during close week; capex/credit/petty cash absorbed; treasury daily cycle manageable with 2–3 analysts |
| **Supply Chain & Logistics** | Supply Planners, Import Coordinator, DC Ops managers | ~30 | W3, W4, W19, W22 | ✅ 2–3 planners handle replenishment + transfers; home delivery picked by DC staff |
| **HR & Payroll** | HR Head, Recruitment, Payroll, HR Assistants | ~15 | W10, W15 | ✅ 2–3 payroll officers + 2 recruiters handle the volume |
| **Marketing** | Brand, Promo, Loyalty, Ecommerce, Digital | ~20 | W13, W17 | ✅ Loyalty is largely automated; promo work is cyclical |
| **Store Operations** | Director, Regional Managers, Ops Standards | ~20 | W5, W16, W29, W5d | ✅ 4 Regional Managers × 50 stores each; oversee new openings; offline recovery is Store Mgr responsibility |
| **IT** | Infrastructure, Apps, Data, Security | ~25 | W16 (store setups) | ✅ 2–3 per store setup + BAU support |
| **Other** | Legal, Internal Audit, Customer Service, Executive | ~50 | — | ✅ Support functions |

### Per-Store Staffing (35 people)

| Role | Count | Key Workflows | Workload Validation |
|---|---|---|---|
| Store Manager | 1 | W5 (open/close), W6 (approvals), W12 (returns), W16 (opening) | Manageable; delegates floor ops to supervisors |
| Asst. Store Manager | 1 | W5 (open/close backup), W6, W12 | Shares management load; covers days off |
| Dept. Supervisors | 4 | W5b (floor selling), W6 (cycle count review), W12 (restock) | 4 depts × 1 supervisor; handles floor + counts |
| Sales Associates | 16 | W5b (selling, paint mixing, lumber cutting), W11 (BOPIS pick) | 4/dept × 2 shifts = adequate for floor coverage |
| Cashiers | 6 | W5b (checkout), W17 (loyalty scan), W28 (gift card sell/reload) | 5 terminals + 1 float; 2 shifts of 3; tight on coverage |
| Receiving Clerks | 2 | W4 (store receiving from DC), W18 (DSD receiving), W22 (transfer receiving) | 2–3 DC trucks/week + 2–3 DSD/week + transfers; 2 clerks in shifts handle it |
| Stock Associates | 3 | W4 (shelf stocking), W6 (cycle counting), W11 (BOPIS pick), W18 (DSD shelving), W22 (transfer pick/receive) | 700 SKUs/day counting + stocking + DSD + transfers; adequate but minimal slack |
| Customer Service Rep | 1 | W11 (BOPIS handoff), W12 (returns), W24 (credit application assistance), W28 (store credit), W29 (recall returns) | ~4 BOPIS + ~2 returns + ~0.5 gift cards/day = light; also handles special orders |
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

## Workflow-to-System Touchpoint Map

Summary of which ERP modules support which workflows:

| ERP Module | Workflows Supported |
|---|---|
| **POS / Retail** | W5 (store selling, offline recovery), W12 (returns), W17 (loyalty at POS), W18 (DSD receiving), W23 (consignment sale), W28 (gift card/store credit), W29 (recall blocking) |
| **Inventory Management** | W3 (GR posting), W4 (replenishment), W6 (cycle counting), W11 (BOPIS pick), W18 (DSD GR), W20 (VMI stock), W22 (transfers), W23 (consignment tracking), W29 (recall quarantine) |
| **Procurement** | W2 (PO cycle), W3 (receiving vs. PO), W18 (DSD PO/GR), W20 (VMI ASN), W21 (capex PO) |
| **Warehouse Management** | W3 (putaway, cross-dock), W4 (pick/pack/ship), W19 (home delivery pick/pack), W22 (transfer pick) |
| **Financials (GL/AP/AR)** | W7 (AP), W8 (AR), W9 (close), W14 (intercompany), W21 (capex & FA), W24 (credit approval), W25 (petty cash), W26 (budget), W27 (rebates), W28 (gift card liability), W30 (treasury & cash management) |
| **Supply Chain Planning** | W2a (auto-replenishment), W4 (replenishment calculation), W22 (transfer planning), W27 (rebate accrual triggers) |
| **HR & Payroll** | W10 (payroll), W15 (onboarding) |
| **Ecommerce** | W11 (BOPIS order flow), W12b (online returns), W19 (home delivery fulfillment) |
| **CRM / Loyalty** | W17 (loyalty program), W24 (credit application) |
| **Pricing / Merchandising** | W13 (promotions), W27 (vendor rebates) |
| **Master Data** | W1 (SKU lifecycle), W16 (new store/location creation), W20 (VMI item setup), W23 (consignment item setup) |
| **Reporting / Analytics** | W1 (assortment analysis), W9 (financial statements), W13 (promo analysis), W19 (delivery performance), W21 (capex vs. budget), W26 (budget variance), W27 (rebate ROI), W28 (gift card liability), W29 (recall tracking), W30 (cash flow forecast) |

---

*Document Version: 3.0 | Date: 2026-05-30 | Added W26–W30 (budget, rebates, gift cards, product recall, offline POS recovery, treasury); fixed W2b FX handling, W3 damage disposition, W4 allocation, W5a offline cache, W5b BIR receipt/customer display, W7 exception SLA, W10 final pay, W13 digital coupons, W16 go-live checklist, W18 volume clarification; updated summary tables*
