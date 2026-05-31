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
- Competitive intelligence monitoring: as part of the quarterly assortment review cycle, Category Managers review competitive landscape per category — (a) new competitor store openings or closures within BuildRight trade areas (sourced from Store Manager reports and publicly available data), (b) competitor promotional events and pricing actions (sourced from Sales Associate and Pricing Analyst field observations, competitor websites/flyers), (c) new competitor product introductions in overlapping categories; findings documented per category and inform SKU add/drop decisions (W1.4), pricing adjustments (W40), and promotional planning (W13); Store Managers report competitive activity in their monthly performance review (W67); competitive intelligence is not a separate system module but is embedded in the W1 quarterly cycle with data sourced from operational channels


### Staffing Implication
5 Category Managers each handling ~2 categories per quarterly cycle = manageable at ~18 hours/category. The 3 Pricing Analysts handle data pulls and analysis in parallel. 10–12 Buyers handle vendor validation. Current team of ~40 in Merchandising is adequate.

> **Buyer staffing note**: At 800–1,000 active vendors ÷ 10–12 buyers = ~67–100 vendors per buyer, which is above the industry average of 30–50. This lean buying model is viable because (a) ~70% of vendors are replenished via auto-generated POs (W2a), reducing daily buyer intervention; (b) top 20 vendors (45% of COGS) are on blanket contracts (W2c) requiring less transactional management; and (c) VMI vendors (12) are largely self-managing. However, during seasonal planning cycles (W32), the team may be stretched. Consider expanding to 15–17 buyers if vendor management quality suffers.

---

## W2. Procurement — Purchase Order Cycle

### W2a. Auto-Replenishment (Stocking Items)

| Field | Detail |
|---|---|
| **Trigger** | SKU hits reorder point (ROP) in system |
| **Frequency** | Daily review; POs generated daily |
| **Volume** | ~1,200 merchandise POs/month (auto-replenishment + ad-hoc); ~18,000 PO lines/month; excludes ~80–240 blanket/contract release orders/month (W2c), ~20–30 import POs/month (W2b), and ~30–50 non-merchandise POs/month (capex, IT, supplies); total all types: ~1,400–1,600 POs/month |

> **PO-to-GR ratio**: ~1,200 merchandise POs generate ~6,000 DC goods receipts/month (W3) — an average of ~5 GRs per PO. This ratio reflects partial shipments (vendors delivering across multiple drops), scheduled phased deliveries for large POs, and blanket PO releases each generating a separate GR. Import POs (W2b) typically generate 1 GR per container. DSD POs delivered to stores generate store-level GRs (W18) outside the DC receiving workflow.
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

### PO Lifecycle: Amendment, Cancellation & Close

| Activity | Trigger | Approval | System Action |
|---|---|---|---|
| **PO Amendment** | Buyer needs to change quantity, delivery date, price, or add/remove lines on an approved PO | Re-approval per tiered matrix (same thresholds as original PO: > PHP 50K → Category Manager, > PHP 500K → VP Merchandising, > PHP 2M → CFO for imports) if change exceeds materiality threshold (quantity change > 20%, price change > 5%, or any delivery date change); minor changes (within threshold) auto-approved with Buyer note | System transmits amendment to vendor (email, EDI, or portal); tracks amendment history with full audit trail (original values, amended values, reason code, approver ID, timestamp); for import POs (W2b), Finance notifies bank if LC amendment is required for value changes |
| **PO Cancellation** | Vendor cannot deliver, demand drops, item discontinued, or PO no longer needed | Buyer initiates with reason code; Category Manager approval required for cancellations > PHP 50K; VP Merchandising for > PHP 500K | System checks for existing GR against PO: if no GR, auto-cancels with vendor notification; if partial GR, Buyer confirms close of remaining quantity; system releases budget commitment; cancelled PO retained in audit trail |
| **PO Auto-Close** | PO fully received (GR quantity matches ordered quantity within tolerance) or PO open beyond configured age limit | Automated | System auto-closes fully received POs; system flags POs open > 90 days for Buyer review (dashboard alert); Buyer reviews aged POs weekly and decides: close remaining quantity, extend delivery date (amendment), or escalate to Category Manager |

### System Touchpoints (PO Lifecycle)
- PO amendment workflow with materiality thresholds triggering re-approval (W2a)
- Amendment history with full audit trail: original vs. amended values, reason, approver (W2a)
- Vendor notification on amendment (email/EDI/portal) (W2a)
- Import PO LC amendment trigger (cross-reference W2b) (W2a)
- PO cancellation with reason code and budget release (W2a)
- Partial-receipt PO close workflow (W2a)
- Auto-close rules: tolerance-based for fully received POs; aging threshold for open POs (W2a)

### W2b. Import Purchase Orders

| Field | Detail |
|---|---|
| **Trigger** | Seasonal buy plan or replenishment of import SKUs |
| **Frequency** | ~20–30 import POs/month |
| **Volume** | ~400–600 TEUs/month across all import vendors (per model-company-profile §7.1); ~15–25 TEUs per major import PO |
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

### Vendor Rebate Dispute Resolution

| Field | Detail |
|---|---|
| **Trigger** | Vendor disputes rebate settlement amount calculated by BuildRight's system (W27 step 6) |
| **Frequency** | Occasional — estimated 5–10 disputes/year |
| **Dispute SLA** | 15 business days from dispute raised to resolution |
| **Owner** | Buyer |
| **Participants** | Buyer, Category Manager, Cost Accountant, Finance Manager |

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|
| 1 | Vendor disputes settlement amount: Buyer receives vendor's written objection with vendor's calculation | Buyer | Category Manager | 15 min |
| 2 | Buyer and Cost Accountant jointly review: compare BuildRight's settlement data (qualifying volume, rebate rate applied) to vendor's claim; identify specific discrepancy (volume count difference, rate tier interpretation, timing gap, excluded transactions) | Buyer / Cost Accountant | Category Manager | 30–60 min |
| 3 | If BuildRight calculation confirmed correct: Buyer responds to vendor with supporting data; dispute closed; no settlement adjustment | Buyer | Category Manager | 15 min |
| 4 | If partial vendor claim valid: Buyer proposes adjusted settlement; Category Manager approves adjustment; Cost Accountant posts adjustment with Category Manager approval and documentation in system | Buyer / Category Manager / Cost Accountant | Finance Manager | 30 min |
| 5 | If dispute unresolved within 15 business days: Buyer escalates to Finance Manager for mediation; Finance Manager reviews both calculations and makes binding recommendation within 5 business days | Finance Manager | CFO | 30 min |
| 6 | Monthly: Cost Accountant tracks rebate dispute frequency and resolution time per vendor; feeds into vendor scorecard (W44); chronic disputing vendors flagged for contract renegotiation (W2c) | Cost Accountant | Controller | 15 min/month |

### System Touchpoints
- Blanket/contract PO creation with SKU lines, pricing tiers, validity dates, and commitment quantities (W2c.4)
- Contract pricing enforcement on release orders (W2c.5)
- Release order creation against blanket PO with quantity tracking (W2c.6–7)
- Cumulative commitment tracking: released vs. minimum vs. maximum (W2c.9)
- Contract utilization reporting (W2c.10)
- Contract expiry alerting with release order blocking (W2c.12)
- Integration with W27 (vendor rebates — rebates may be tied to contract commitment achievement; rebate dispute resolution per W27 dispute SLA of 15 business days)

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
| 5 | Quality check on sampled items (damage, correctness, expiry if applicable) per category-specific inspection checklist (see Quality Inspection Standards below) | Quality Checker | DC Supervisor | 10–20 min |
| 6 | If discrepancy (shortage, damage, wrong item): flag in system; notify Buyer | Receiving Clerk | DC Supervisor | 5 min |
| 6a | If damaged goods: Receiving Clerk creates damage report with photos; initiates one of: (a) Return to Vendor (RTV) via Buyer, (b) scrap with DC Supervisor authorization, or (c) insurance claim for insured shipments. For insurance claims: Receiving Clerk documents damage with photos and notes on delivery receipt; Import Coordinator or DC Supervisor files claim with insurance provider within required notification window (typically 3–5 business days); system tracks claim status; upon settlement, Finance posts insurance recovery to income and reduces inventory loss | Receiving Clerk | DC Supervisor | 10 min |
| 6b | Buyer reviews RTV request; coordinates with vendor for credit note or replacement shipment | Buyer | Category Manager | 15 min/occurrence |
| 6c | If scrap authorized: DC Supervisor approves scrap disposition; system removes inventory and posts loss to damage/scrapping account | DC Supervisor | DC Manager | 5 min |
| 7 | Confirm Goods Receipt in system; inventory increases in real-time | Receiving Clerk | DC Supervisor | 5 min |
| 8 | System suggests putaway location based on zone, bin capacity, item velocity | System | — | Automated |
| 9 | Putaway staff moves goods to assigned bin; scan-confirm in system | Putaway Staff | DC Supervisor | 15–30 min |
| 10 | Update PO/TO status; trigger vendor invoice matching (AP) | System | — | Automated |

**Total time per receipt**: ~1.5–3 hours from gate to bin

### Quality Inspection Standards (W3 Step 5 Detail)

Quality inspection at receiving uses configurable, category-specific checklists. The system presents the Quality Checker with the appropriate checklist per SKU category on the RF device. AQL (Acceptable Quality Level) sampling is applied per ANSI Z1.4 single sampling plan, normal inspection level II, with configurable AQL per category.

| Category | Inspection Criteria | Sampling Plan | AQL | Reject Action |
|---|---|---|---|---|
| **Tiles & ceramics** | Visual defects (chips, cracks, glaze inconsistencies on sampled pieces); color consistency vs. reference sample; dimensional check (±1mm tolerance on length/width); PEI rating confirmation per packaging | Per lot: ≤ 100 pcs → inspect 5; 101–500 → inspect 20; 501+ → inspect 32 | 2.5% | Reject entire lot if defect rate exceeds AQL; Buyer notifies vendor |
| **Lumber & wood** | Moisture content spot-check (if meter available); warping/bowing check (visual); species/treatment verification; grade stamp verification; length/piece count | Per bundle: inspect 5 pieces from each bundle | 4.0% (visual) | Reject non-conforming pieces; accept remainder; Buyer adjusts PO quantity |
| **Paint & chemicals** | Manufacturing date and shelf-life capture (mandatory per shelf-life management); container integrity (dents, leaks, tamper seal); color match for tinted items; safety data sheet availability check | Per delivery: inspect 10% of cartons, minimum 2 | 1.5% (critical: leaks/tamper) | Reject entire lot if critical defect found; quarantine for Buyer review |
| **Cement & masonry** | Bag integrity (no tears, moisture damage, hardened lumps); manufacturing date check (cement shelf-life typically 3 months); weight spot-check on sampled bags | Per pallet: inspect 5 bags from top, middle, bottom | 2.5% | Reject damaged bags; accept sound bags; Buyer adjusts PO quantity |
| **Plumbing & electrical** | Visual defect check (finish, threads, connectors); brand/model verification against PO; quantity count; packaging integrity | Per line item: inspect 10% of units, minimum 2 | 2.5% | Reject non-conforming units; Buyer coordinates with vendor |
| **Power tools & appliances** | External packaging check; serial number capture for high-value items (> PHP 10,000); physical damage check; accessory completeness vs. product spec | Per unit: 100% inspection for high-value; 10% for standard | 1.0% (high-value); 2.5% (standard) | Reject damaged units; serial-tracked items logged for warranty (W33) |
| **Hardware & fasteners** | Quantity count (weigh-count or piece count); rust/corrosion check; grade/size verification against PO | Per line: weigh-count verification | 4.0% | Reject if count variance > 5%; Buyer adjusts PO |

**Quality hold process**: if inspection fails, system places goods in "Quality Hold" status — inventory is physically segregated in QC hold area and not available for putaway, allocation, or sale; Quality Checker creates quality hold record with defect description, photos, and inspection checklist result; Buyer notified for vendor resolution (replace, credit, or scrap); if not resolved within 5 business days, DC Supervisor escalates to Category Manager.

**Monthly**: DC Supervisor generates quality metrics report per vendor: inspection pass rate, top defect categories, quality hold aging; feeds into vendor scorecard (W44 quality reject rate metric).

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

### W3c. DC Inbound Delivery Scheduling

| Field | Detail |
|---|---|
| **Trigger** | Purchase order confirmed with vendor or import shipment ETA confirmed |
| **Frequency** | Daily; ~40 receipts/day per DC |
| **Volume** | ~1,200 merchandise receipts/month + ~80–240 blanket releases + ~20–30 import containers + ~30–50 non-merchandise receipts per DC per month |
| **Owner** | DC Receiving Supervisor |
| **Participants** | Buyer, Import Coordinator, DC Receiving Supervisor, DC Dispatch, Vendor/Carrier |

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates inbound delivery forecast from open POs: PO number, vendor, expected delivery date (from PO promised date or import ETA), number of lines, estimated pallet/cube count, and dock door requirements (refrigerated none; hazardous materials for paint/chemicals; standard for general merchandise) | System | — | Automated (nightly) |
| 2 | DC Receiving Supervisor reviews next 3-day inbound forecast each morning; identifies days with high receiving volume (> 50 receipts) or overlapping large deliveries; adjusts dock door assignments and staff scheduling | DC Receiving Supervisor | DC Manager | 15 min/day |
| 3 | For domestic vendor deliveries: Buyer or system transmits delivery appointment to vendor with requested delivery date and time window (typically 8:00 AM – 4:00 PM, 2-hour windows); vendor confirms or proposes alternative; system logs appointment confirmation | Buyer / System | DC Receiving Supervisor | 5 min/PO |
| 4 | For import containers: Import Coordinator books delivery appointment with DC once container is released from port; provides container number, commodity, estimated weight, and special handling requirements; DC Receiving Supervisor confirms appointment and assigns dock door | Import Coordinator | DC Receiving Supervisor | 10 min/container |
| 5 | If vendor arrives without appointment: guard checks against open PO list; if valid PO exists, Receiving Supervisor accepts on a space-available basis (may result in extended wait time); if no valid PO, guard turns delivery away with Buyer notification | Guard / DC Receiving Supervisor | DC Manager | 5 min |
| 6 | System maintains dock door utilization dashboard per DC: shows scheduled appointments, completed receipts, and available capacity by time slot; Receiving Supervisor uses dashboard to optimize dock assignments and avoid congestion | System | — | Automated |
| 7 | Monthly: DC Receiving Supervisor reviews appointment compliance report — vendor on-time arrival %, no-show rate, unscheduled delivery rate; feeds into vendor scorecard (W44) and carrier performance review (W52) | DC Receiving Supervisor | DC Manager | 30 min/month |

### System Touchpoints (DC Scheduling)
- Inbound delivery forecast from open PO data with dock door requirements (W3c.1)
- Delivery appointment booking with vendor confirmation tracking (W3c.3–4)
- Dock door utilization dashboard with real-time capacity visibility (W3c.6)
- Appointment compliance reporting feeding vendor scorecard (W3c.7)
- Unscheduled delivery handling with PO validation at gate (W3c.5)
- Integration with W3 (DC receiving — appointments feed step 1 guard check), W2a (auto-replenishment POs generate appointments), W2b (import container appointments), W18b (DSD scheduling — store equivalent), W44 (vendor scorecard — appointment compliance), W52 (carrier performance)
- Barcode/RF scanning against PO (W3.4)
- Discrepancy flagging and Buyer notification (W3.6)
- Damage disposition workflow: RTV initiation, scrap authorization, insurance claim capture (W3.6a–c)
- Goods Receipt posting → inventory update; perpetual WAC recalculation at each receipt: new WAC = (prior inventory value + receipt value) ÷ (prior quantity + receipt quantity) (W3.7)
- Putaway direction (zone, bin, velocity-based) (W3.8)
- Cross-dock allocation to outbound orders (cross-dock variant)
- DC forward-pick zone replenishment: system monitors forward-pick (fast-pick) location quantities in real-time; when quantity drops below minimum threshold, generates replenishment task (move from reserve/bulk storage to forward-pick); replenishment staff receives task on RF device, moves stock, scan-confirms at both locations; replenishment prioritized ahead of picking waves to avoid picker idle time (W3.8 post-putaway, integrated with W4 picking)
- Shelf-life / expiry date management: at Goods Receipt, Receiving Clerk captures manufacturing date and shelf-life duration for date-sensitive items (paint, adhesives, sealants, chemicals, cement, grout); system calculates and records expiry date per batch/lot; items with remaining shelf life below configurable threshold (e.g., < 30%) flagged for priority picking or markdown; expired items blocked from dispatch (W3.4)
- Inventory ownership: all merchandise received into DCs is owned by BuildRight Depot Inc. even though DC facilities are operated by BuildRight Logistics Inc.; Logistics Inc. provides warehousing and distribution services billed monthly per W14; goods are Depot Inc. inventory throughout the DC→Store flow
- RTV physical logistics and tracking: Receiving Clerk stages RTV items in designated RTV holding area at DC; system creates RTV shipment record with lifecycle tracking (Initiated → Packed → Shipped → In Transit → Vendor Received → Credit Note Issued → Settled); DC dispatch arranges carrier pickup or vendor pickup per agreement with Buyer coordination; system tracks RTV aging by status; for store-initiated RTVs (W6.8a, W12a.8, W33.6), Stock Associate stages items in backroom and system creates RTV shipment record; Buyer coordinates with vendor for direct pickup from store or shipment to DC for consolidation; vendor credit note triggered upon vendor confirmation of receipt; if vendor disputes, Buyer negotiates resolution per W3.6b; system maintains RTV tracking dashboard with aging by status
- RTV vendor credit note SLA: system enforces configurable credit note SLA per vendor — default 15 business days from vendor receipt of returned goods to credit note issuance; if credit note not received within SLA, system escalates to Buyer with auto-notification; Buyer contacts vendor for resolution; if unresolved after 30 days, Buyer escalates to Category Manager for vendor scorecard impact (W44); credit note SLA compliance tracked as a metric in vendor scorecard (W44 invoice accuracy metric); monthly: AP Clerk generates RTV credit note aging report showing all open RTVs awaiting vendor credit note with days outstanding, feeding into W7d vendor statement reconciliation
- RTV freight cost allocation: freight cost for returning goods to vendor is borne by the party responsible for the return reason — (a) defective/wrong items (vendor fault): vendor bears freight cost; deducted from credit note amount negotiated by Buyer; (b) buyer-initiated returns (overstock, discontinuation): BuildRight bears freight cost; posted to inventory write-down or return-to-vendor expense; (c) carrier damage: freight cost claimed from carrier insurance per W3.6a; system captures RTV freight cost as a separate line on the RTV shipment record; AP Clerk reconciles freight cost allocation during credit note processing (W7.9b)
- DC RTV consolidation & vendor return shipment batching: with 200 stores returning defective/damaged/discontinued items to 5 DCs (W22b), DC Receiving Clerks accumulate RTV items in a designated RTV holding area organized by vendor; system maintains a DC-level RTV consolidation dashboard showing accumulated items per vendor, total value, and aging; weekly, Buyer reviews the consolidation dashboard and determines batch shipment timing per vendor — (a) for high-volume vendors (weekly returns): Buyer schedules weekly vendor pickup or carrier shipment when accumulated value exceeds a configurable threshold (e.g., PHP 20,000 per vendor), (b) for low-volume vendors: items held until accumulated value justifies shipment cost, or consolidated with next regular vendor delivery truck for backhaul; system generates RTV shipment manifest per vendor listing all items, source locations (store or DC), quantities, credit note expected per item, and total claim value; Buyer transmits manifest to vendor for advance confirmation; upon vendor pickup or shipment, system updates RTV lifecycle status per W3 RTV tracking; AP Clerk uses consolidated manifest for credit note reconciliation per W7.9b; monthly: Buyer reviews DC RTV aging dashboard for items in RTV holding > 30 days and escalates to Category Manager for alternative disposition if vendor is unresponsive

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
- New store demand ramp-up (first 90 days): for newly opened stores (W16), auto-replenishment parameters (ROP, safety stock, min/max) derived from comparable store averages may not reflect actual local demand patterns during the ramp-up period; during the first 90 days post-opening, Supply Planner overrides auto-replenishment with manual review — (a) system flags all replenishment orders for new stores with "Ramp-Up" status requiring Planner confirmation (no auto-release), (b) Planner reviews suggested orders daily against early sell-through data and adjusts quantities based on actual demand velocity observed in the first weeks, (c) Store Manager provides daily feedback on fast-moving and slow-moving items via the W4b store-initiated replenishment request channel, (d) after 90 days, Demand Planner analyzes accumulated sales data to calculate store-specific ROP/safety stock parameters per W31.8; system transitions the store from "Ramp-Up" to standard auto-replenishment; parameters reviewed again at 180 days; this manual override period prevents both overstocking (tying up working capital in a new store) and stockouts (damaging customer first impressions)
- Constrained allocation rule governance: when available supply is insufficient for all stores, system applies configurable allocation logic; Supply Planning Manager defines allocation method per SKU or category (equal distribution, rank by store revenue, prioritize A-stores, proportional to historical demand); allocation rules reviewed and approved by VP Supply Chain; rule changes logged with old method, new method, reason, approver, and effective date; monthly: Supply Planning Manager reviews allocation fairness dashboard showing per-store fill rate and allocation share; fairness disputes escalated by Store Managers through W4b channel feed into allocation rule review; quarterly: allocation methodology reviewed as part of W31.8 parameter governance cycle (W4.2)

### W4b. Store-Initiated Replenishment Request

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
| 5 | **If approved — DC has insufficient stock**: Supply Planner requests Buyer to expedite a PO (W2a) or arrange an inter-DC transfer (W22); request status updated to "Approved — Pending Supply"; Supply Planner tracks until supply arrives | Supply Planner / Buyer | Supply Planning Manager | 10 min |
| 6 | **If denied**: Supply Planner rejects request with reason (insufficient DC stock, lower priority than other stores, demand not validated); system notifies Store Manager; Store Manager may escalate to Regional Manager if disagreement | Supply Planner | Supply Planning Manager | 2 min |
| 7 | Fulfillment follows standard W4 pick/pack/ship process; request closed when goods received at store | Per W4 | — | Per W4 |
| 8 | Weekly: Supply Planning Manager reviews store-initiated request report — approval rate, top requesting stores, frequently requested items; flags items with high ad-hoc request frequency for ROP/safety stock adjustment per W31.8 | Supply Planning Manager | VP Supply Chain | 30 min/week |

### System Touchpoints
- Store-initiated replenishment request form in POS/terminal/handheld with SKU selection, quantity, urgency, and justification fields (W4b.1)
- Supply Planner dashboard showing request alongside current supply position (on-hand, ATP, open POs, pending replenishment) (W4b.2)
- Request status lifecycle: Submitted → Under Review → Approved (Scheduled / Pending Supply) / Denied → Fulfilled / Closed (W4b.3–7)
- Weekly request analytics: approval rate, requesting stores, frequently requested items feeding into ROP parameter review (W31.8) (W4b.8)
- Integration with W4 (replenishment order creation), W2a (expedited PO), W22 (inter-DC transfer), W31 (forecast and ROP adjustment)

### Staffing Implication
- **Supply Planner**: ~100–200 requests/month ÷ 20 working days = ~5–10/day. At ~10 min each for review = ~1 hour/day incremental. Absorbed within existing 2–3 planner team.
- **Store Managers**: ~0.5–1 requests/month × 10 min = negligible.

### Staffing Implication (W4 overall)
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
| 4c | For trade/corporate account customers: Cashier identifies customer via loyalty card, account card, or mobile number lookup; system loads customer's pricing tier (trade discount % or corporate contract price list) and applies account-specific pricing to scanned items; if promotional price is lower than account price, system applies the lower price and alerts cashier; for accounts with project-specific pricing, Cashier selects applicable price list; sale posts to customer's AR account (W8) instead of cash/card tender; credit limit checked in real-time per W8.3; for new trade customers not yet in system: Cashier provides W24 credit application form or directs customer to CSR counter for application intake; sale processed as cash/card transaction until account is approved and activated | Cashier | Store Manager | 30 sec |
| 5 | If loyalty member: Cashier scans loyalty card or asks for mobile number | Cashier | — | 15 sec |
| 6 | System calculates totals: applies promos, quantity breaks, loyalty discounts | System | — | Automated |
| 7 | Customer pays (cash, card, e-wallet, split tender) | Cashier | — | 30–60 sec |
| 8 | Receipt printed; inventory deducted in real-time | System / Cashier | — | 15 sec |
| 9 | Age-restricted items trigger cashier confirmation prompt | Cashier | Store Manager | 10 sec |
| 10 | **Void transaction**: Cashier or Store Manager initiates void before transaction is finalized (pre-void) or after finalization (post-void); manager authorization (swipe/card) required for any void; system logs void with cashier ID, authorizing manager ID, original transaction number, void reason code, and timestamp; system reverses inventory deduction, payment, loyalty points earned/redeemed, and promo usage; voided transaction retained in full audit trail (not deleted) | Cashier / Store Manager | Store Manager | 1 min |
| 11 | **Price dispute at POS**: customer claims the scanned price differs from the displayed shelf tag; Cashier visually verifies shelf tag; if discrepancy confirmed: (a) Cashier honors the shelf tag price (customer-friendly policy per DTI price tag accuracy requirements), (b) Cashier applies price override with reason code "Shelf Tag Discrepancy" — manager authorization required per standard W5b.4a override rules, (c) system logs dispute with original price, shelf tag price, cashier ID, authorizing manager ID, and item barcode; (d) system creates shelf tag discrepancy ticket auto-routed to Department Supervisor for immediate shelf tag correction (W63) and inclusion in next W69 price audit cycle; if the shelf tag price is higher than the scanned (system) price, Cashier informs customer that the lower system price applies — no override needed | Cashier / Store Manager | Store Manager | 2 min |
| 12 | **Employee purchase**: employee presents employee ID badge at checkout; Cashier selects "Employee Purchase" tender type in POS; system applies configured employee discount (default 10% off SRP, configurable by company policy) and enforces purchase limits (max PHP 20,000/month per employee, max 3 units per SKU per month); discount does not stack with promotional pricing — lower of employee discount or promo price applies; employee discount excluded from catch-weight and clearance items; system logs employee purchase with employee ID, discount applied, and monthly running total; monthly: Store Manager receives employee purchase summary report; purchases exceeding monthly limit require Store Manager override with justification; employee purchases are not eligible for loyalty points earning | Cashier / Employee | Store Manager | 1 min additional |

**Average transaction time**: ~3 minutes (checkout only); total customer visit ~20–30 min

### W5d. In-Store Customer Delivery Scheduling

| Field | Detail |
|---|---|
| **Trigger** | Walk-in customer purchases bulky items (lumber, cement, appliances, tiles, fixtures) at POS and requests home delivery |
| **Frequency** | ~5–10 delivery requests per store per week; ~4,000–8,000/year chain-wide |
| **Volume** | Avg 2–5 items per delivery; avg delivery value PHP 3,000–15,000 |
| **Owner** | Sales Associate (intake); DC Dispatch / Fleet Manager (carrier coordination) |
| **Participants** | Sales Associate, Cashier, Customer, DC Dispatch, 3PL carrier |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer selects bulky/heavy items in store; Sales Associate identifies items needing delivery and confirms customer wants home delivery instead of self-transport | Sales Associate | — | 2 min |
| 2 | Sales Associate opens delivery order in POS/terminal: scans items, confirms quantities, captures delivery address (street, barangay, city/municipality, province, landmark), customer name, mobile number, preferred delivery date (next available), and notes (gate code, floor level, elevator access) | Sales Associate | Dept. Supervisor | 5 min |
| 3 | System calculates delivery fee based on delivery zone (distance from store using configured rate cards per zone/weight/tier — same carrier rate cards as W19 home delivery); displays fee to Sales Associate and customer; delivery fee added to transaction total | System | — | Automated |
| 4 | Customer pays for merchandise + delivery fee at POS; system creates delivery order linked to POS transaction; delivery fee posted to Delivery Revenue (Cr.) / Cash (Dr.); merchandise revenue and COGS posted per standard W5b | Cashier / Customer | Store Manager | Part of checkout |
| 5 | System transmits delivery order to carrier pool: selects 3PL carrier per delivery zone (same W19 carrier selection logic — Lalamove, Transportify, or own fleet if available); creates carrier pickup request with store address as origin, customer address as destination, item description, estimated weight, and preferred delivery date/time | System | — | Automated |
| 6 | Carrier accepts pickup request; driver dispatched to store; system sends tracking link to customer via SMS with estimated delivery window | Carrier / System | DC Dispatch | Automated |
| 7 | Sales Associate or Stock Associate stages paid items at store dispatch area; hands items to carrier driver with delivery order printout; driver confirms pickup on carrier app | Sales Associate / Carrier | Store Manager | 5 min |
| 8 | Carrier delivers to customer address; obtains proof of delivery (photo, signature); system marks delivery order as "Delivered" | Carrier | — | Varies by distance |
| 9 | If delivery fails (customer unavailable): follows same failed delivery lifecycle as W19.12 — carrier attempts re-delivery or returns items to store; Sales Associate contacts customer to reschedule; if customer cancels, system refunds delivery fee and processes merchandise return per W12 | Carrier / Sales Associate | Store Manager | Per W19.12 |
| 10 | Weekly: Store Manager reviews in-store delivery report — delivery count, revenue, delivery fee collected, carrier performance (on-time %, damage rate); flags high delivery fee refund rates for carrier escalation per W62b | Store Manager | Regional Manager | 15 min/week |

### System Touchpoints (In-Store Delivery)
- In-store delivery order creation at POS/terminal with delivery address capture, zone-based delivery fee calculation, and carrier selection (W5d.2–3, W5d.5)
- Delivery fee as a separate line item on POS transaction with distinct GL posting (Dr. Cash / Cr. Delivery Revenue) (W5d.4)
- 3PL carrier integration: reuses W19 carrier selection logic, rate cards, and API integration for order creation and tracking (W5d.5–8)
- Customer notification with tracking link via SMS (W5d.6)
- Failed delivery handling aligned with W19.12 lifecycle (W5d.9)
- In-store delivery analytics: delivery count, revenue, fee collection, carrier performance per store (W5d.10)
- Integration with W5b (POS checkout — delivery order linked to sales transaction), W19 (home delivery — same carrier infrastructure), W62b (3PL partner management), W63 (shelf labels — catch-weight items display unit pricing)

### Staffing Implication
- **Sales Associates**: ~5–10 delivery orders/store/week × ~7 min each (address capture + staging) = ~35–70 min/week. Absorbed within existing Sales Associate duties.
- **No incremental headcount**. Uses existing 3PL carrier relationships (W62b) and store staging process.

### W5e. Store Opening Delay Procedure

| Field | Detail |
|---|---|
| **Trigger** | Issue discovered during W5a store opening sequence that prevents normal opening by scheduled store opening time |
| **Frequency** | Occasional — estimated 2–4 delayed openings per store per year |
| **Volume** | Variable — from 15-minute delay to full-day closure |
| **Owner** | Store Manager |
| **Participants** | Store Manager, IT Helpdesk (W48), Facilities Coordinator (W47), Regional Manager |

### Delay Scenarios & Responses

| Scenario | Response | Minimum Viable Opening |
|---|---|---|
| **Power outage** | Store Manager contacts Meralco/utility provider for ETA; if generator available, start generator and open with reduced lighting in non-essential areas; POS runs on UPS/battery backup during generator switchover | Open with generator power; 3 of 5 POS terminals sufficient |
| **POS system / network down** | Store Manager contacts IT Helpdesk (W48 P1); if estimated fix < 2 hours, delay opening until restored; if > 2 hours, open in manual mode (written receipts, manual price lookup from printed price list); reconcile per W5g offline recovery upon restoration | Open with manual receipts if < 2 hours; otherwise delay |
| **Alarm malfunction** | Guard performs exterior walkthrough (W71.1); if no signs of intrusion, Store Manager enters and inspects; contacts alarm monitoring company for emergency repair; opens if interior verified safe | Open if security verified; alarm repair scheduled per W47 |
| **Safety hazard found during walkthrough** (water leak, structural damage, gas smell) | Store Manager isolates affected area; contacts Facilities Coordinator for emergency repair per W47; if hazard is localized, open store with restricted access to affected zone; if hazard affects entire store (gas leak, major flooding), keep closed until resolved | Open partial if hazard isolated; full closure if building-wide |
| **Late staff arrival** (multiple no-shows due to transport, weather) | Store Manager calls in available off-duty staff; opens with minimum crew: 1 cashier, 1 floor associate, 1 stock associate, 1 manager; remaining terminals closed | Open with 1 terminal + 1 floor associate + manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Store Manager identifies delay issue during W5a opening sequence; assesses severity per delay scenario table above | Store Manager | — | 5 min |
| 2 | Store Manager contacts appropriate support: IT Helpdesk (W48) for system issues, Facilities Coordinator (W47) for physical issues, alarm company for security issues | Store Manager | — | 5 min |
| 3 | Store Manager decides: (a) delay opening by estimated fix time, or (b) open in minimum viable configuration per scenario table | Store Manager | Regional Manager | 5 min |
| 4 | If delaying: Store Manager posts "Opening at [time]" signage on store entrance; updates store status in system; Regional Manager notified | Store Manager | — | 5 min |
| 5 | If opening with reduced capacity: Store Manager assigns available staff to critical positions (minimum 1 cashier, 1 floor, 1 manager); remaining terminals shuttered; DSD receiving deferred | Store Manager | — | 10 min |
| 6 | Upon issue resolution: Store Manager transitions to full operations; communicates "now open" via store signage and system update; reconciles manual transactions (if any) per W5g upon system restoration | Store Manager | — | 10 min |
| 7 | Store Manager documents delay incident in system: root cause, duration of delay, impact on sales (estimated lost revenue), corrective action taken; includes in daily report to Regional Manager | Store Manager | Regional Manager | 10 min |

### System Touchpoints
- Store status management: Store Manager can set store status to "Delayed Opening" or "Partial Operations" in system; suppresses BOPIS order routing (W11) and ecommerce availability (W19) during delay; auto-restores when status set to "Open" (W5e.4, W5e.6)
- Manual receipt reconciliation: upon system restoration, manual transactions entered as batch per W5g offline recovery process (W5e.6)
- Delay incident logging with root cause categorization and lost revenue estimation (W5e.7)
- Integration with W5a (opening procedure), W5g (offline recovery), W47 (facility emergency repair), W48 (IT helpdesk P1), W49 (natural disaster — this is for non-disaster delays), W71 (security incidents)

### Staffing Implication
- No incremental headcount. Delay handling is a Store Manager responsibility. Estimated 2–4 delayed openings/store/year × ~30 min each = ~1–2 hours/year per store.

### W5f. Store Closing & End-of-Day

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
| 5a | Store Manager or Cashier seals cash in tamper-evident deposit bag per armored car provider's procedure; records bag number and amount in system; armored car guard collects per scheduled pickup (or Store Manager deposits at nearest bank branch if no armored car service); system records deposit confirmation number and expected deposit amount per Z-report total | Store Manager / Cashier | Store Manager | 10 min |
| 5b | If armored car pickup delayed or missed: Store Manager contacts armored car provider for emergency pickup; if unavailable by end of business, Store Manager or designated Cashier deposits at bank branch with witness; system logs exception | Store Manager | Store Manager | 15 min if exception |
| 6 | Log out of POS; shut down terminals | Cashier | Store Manager | 5 min |
| 7 | Store Manager reviews daily sales summary on dashboard | Store Manager | Store Manager | 10 min |
| 8 | Complete daily checklist (safety, cleanliness, equipment) | Maintenance/Utility | Store Manager | 15 min |
| 9 | Arm alarm; lock up | Store Manager | Store Manager | 5 min |

**Total closing time**: ~60 minutes

> **Note**: W5f was previously numbered W5c in the document structure. W5d (In-Store Customer Delivery Scheduling), W5e (Store Opening Delay Procedure), and W5f (Store Closing & End-of-Day) are now sequential sub-sections of W5.

### System Touchpoints
- POS cash float management and tracking (W5a.4)
- POS terminals boot in offline-ready mode; product master and price file cached locally via nightly sync so selling can continue without network (W5a.3, W5a.5)
- Real-time price and promo sync (W5a.5)
- Barcode scanning, multi-tender, loyalty at POS (W5b.4–9)
- BIR-registered receipt format: receipts printed on BIR-authorized thermal paper with TIN, registered invoice number, and compliant layout (W5b.8)
- Customer-facing display (pole display or second screen) showing scanned items, running total, and payment amount during checkout (W5b.4–7)
- Price override with manager authorization threshold and audit trail (W5b.4a)
- Lot/batch capture at POS for lot-tracked items: system prompts for batch number, auto-extracts from GS1-128/2D barcode, records batch against transaction line for forward traceability (W5b.4b)
- Trade / corporate account pricing at POS: Cashier identifies customer via card or mobile number; system loads customer's pricing tier (trade discount %, corporate contract price list, or project-specific pricing); applies account-specific pricing to scanned items; if promo price is lower than account price, system applies lower price; sale posted to customer AR account with real-time credit limit check (W5b.4c, cross-reference W8, W24)
- VAT-exempt / zero-rated sales at POS: when a VAT-exempt or zero-rated customer account is identified at POS (per VAT treatment classification in W24.6), system automatically applies zero output VAT to the transaction; receipt prints "VAT-EXEMPT" or "ZERO-RATED" designation per BIR requirements; transaction recorded in separate VAT register for exempt/zero-rated sales; system segregates VATable, exempt, and zero-rated sales in BIR Form 2550M reporting (W9a.16); VAT-exempt customers include government agencies with supporting BIR ruling, PEZA-registered entities, and other entities with documented VAT exemption (W5b.4c)
- VMI and consignment items at POS: system automatically identifies VMI and consignment items at scan via item master flags (no cashier intervention); standard items post Dr. COGS / Cr. Inventory; VMI items post Dr. COGS / Cr. VMI Vendor Payable (W20.8); consignment items post Dr. COGS / Cr. Consignment Vendor Payable (W23.6); cashier experience is identical regardless of item ownership type; different GL posting paths are transparent to the cashier
- Catch-weight / variable measure selling with weight/length capture and auto-price calculation (W5b.2)
- Custom SKU generation for paint mixing (W5b.3)
- Age-restricted product prompts (W5b.9)
- Void transaction with manager authorization: full audit trail (cashier, manager, reason, timestamp); automatic reversal of inventory, payment, loyalty points, and promo usage; voided transaction retained for loss prevention analysis (W5b.10); BIR-compliant void document: system prints or records a void receipt referencing the original transaction number with void indicator, reason code, and authorizing manager ID per CAS permit requirements (W54a.8); void receipt retained for 7-year BIR retention period alongside the original transaction record
- Void authorization roles and queuing: void authorization granted to Store Manager and Assistant Store Manager by default; Department Supervisors may be granted void authorization for their department's items up to a configurable threshold (e.g., ≤ PHP 5,000); if no authorized person is physically available at the time of void request, cashier can suspend the transaction and queue the void for next-available manager authorization; system enforces that all queued voids are authorized within the same business day; queued voids visible on Store Manager's terminal dashboard (W5b.10)
- Z-report generation (W5c.2)
- Cash reconciliation / variance reporting (W5c.3–4)
- Electronic payment reconciliation: automated import of card acquirer and e-wallet settlement reports; comparison to Z-report by tender type; variance alerting (W5c.3a–b)
- Cash-in-transit tracking: armored car pickup confirmation or bank deposit receipt capture per store; bag number and amount logging; deposit confirmation matching to Z-report totals; delayed pickup exception alerting (W5c.5a–b); deposit timing enforcement: system requires Store Manager to confirm deposit (armored car pickup or bank deposit) within 24 hours of store closing; unconfirmed deposits auto-escalate to Regional Manager on day 2; Regional Manager contacts Store Manager for explanation and resolution; system logs all deposit confirmation timestamps with variance from expected schedule
- Daily sales dashboard (W5c.7)

### Staffing Implication
- **6 Cashiers per store**: 5 terminals + 1 float. With 2 shifts (~10 hours total), each shift needs 3–4 cashiers. 6 covers shifts + days off with 1 relief. Tight but workable.
- **16 Sales Associates**: Across 4 departments (Lumber, Plumbing/Electrical, Tiles, Tools/Hardware) = 4 per dept. 2 shifts. Handles floor coverage + specialty tasks (paint mixing, lumber cutting). Reasonable.
- **3 Stock Associates (+ 1 part-time relief recommended)**: Continuous replenishment + cycle counting + BOPIS picking + DSD shelving + transfer handling + shelf label updates + weekly price audit scanning (W69) + layaway staging (W75) + ship-from-store picking (W19b). With ~700 SKUs to cycle count daily and all additional duties, 3 is the absolute minimum with no slack for absenteeism. Recommend 4 Stock Associates per store (or 3 full-time + 1 part-time relief) to ensure coverage during peak seasons, absenteeism, and promotional periods.

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
- Negative inventory resolution: system generates daily negative inventory alert listing all SKU-locations where on-hand < 0; at store level, Stock Associate investigates root cause (timing lag from offline POS transactions per W5g, receiving error, mispick, or cycle count needed); at DC level, Inventory Control clerk investigates (pending GR posting, allocation error, picking error); resolution action depends on cause — recount and adjust (W6), wait for pending transaction posting, or force adjustment with supervisor approval; system blocks negative-inventory locations from ecommerce ATP availability until resolved; monthly report of negative inventory frequency by location feeds into inventory accuracy improvement initiatives

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
- Early payment discount detection: system identifies invoices eligible for discount, calculates annualized ROI, and highlights during payment run; decision criteria — Treasury Analyst authorizes taking discount when (a) annualized ROI exceeds BuildRight's weighted average cost of capital (currently ~8–10%, configurable), (b) cash position (W30) supports early payment without creating liquidity risk, and (c) vendor is rated A or B on vendor scorecard (W44) — discounts for C/D-rated vendors are deferred to standard terms to preserve cash leverage; system auto-calculates annualized ROI per discount offer as: (discount % ÷ (365 ÷ days saved)) × 100 and displays alongside cash position impact in payment run review screen (W7.7a)
- AP aging report (W7.8)
- Payment file generation (bank formats) (W7.9–10)
- Expanded Withholding Tax (EWT): auto-computation per ATC in vendor master, net payment calculation (invoice − EWT), EWT Payable tracking, BIR 1601-E file generation (W7.9a)
- Vendor credit memo processing: credit note entry with source reference (RTV, rebate, price protection), auto-matching to original transactions, automatic application to open invoices, credit balance management (W7.9b)
- Non-PO / recurring expense invoice processing: 2-way match (invoice vs. contract or budget), store manager / department head approval routing, cost center allocation, utility and service bill capture (W7c.1–6)
- Shelf-life / expiry date management: capture manufacturing date and shelf-life at GR for date-sensitive items; system tracks expiry per batch; FEFO (First Expired First Out) pick direction in DC; alerting for near-expiry items; periodic expiry review feeds into slow-mover disposition (W3, W4, W6)
- GRNI aging management: AP Clerk runs weekly GRNI aging report showing all GRs without matching vendor invoices, grouped by aging bucket (0–30, 31–60, 61–90, 90+ days); items > 30 days flagged for Buyer follow-up with vendor; items > 60 days escalated to AP Supervisor for direct vendor contact; items > 90 days reviewed by Controller for potential permanent accrual or write-off; system tracks GRNI aging with vendor-level drill-down; weekly GRNI aging dashboard visible to AP Supervisor and Controller (W7, W9a.2a)
- Duplicate vendor invoice detection: system automatically checks incoming vendor invoices against the AP sub-ledger for duplicate invoice number, duplicate vendor + amount + date combinations, and duplicate PO reference + invoice number; if a potential duplicate is detected, system blocks the invoice and alerts AP Clerk with the matching existing invoice reference; AP Clerk investigates (true duplicate vs. sequential invoice numbers from same vendor) and either rejects the duplicate or overrides with documentation; monthly: AP Supervisor reviews duplicate detection override log as part of AP controls review (cross-reference CTL-42 in Internal Controls Matrix) (W7)
- Evaluated Receipt Settlement (ERS): for configured VMI vendors (W20) and select blanket PO vendors (W2c), system auto-generates vendor invoice from PO + Goods Receipt data without requiring vendor invoice submission; AP Clerk validates auto-generated invoice against PO and GR; if within tolerance, auto-approved for payment; reduces GRNI accumulation and manual invoice processing for high-volume, trusted vendor relationships

### Staffing Implication
- **8–10 AP Clerks**: total ~305–370 invoices/business-day across merchandise (~295/day per W7: 6,500 invoices/month ÷ 22 business days) and non-PO (~91–136/day per W7c: 2,000–3,000/month ÷ 22); at 5 min logging each = ~25–31 hours for basic processing; with ~20% requiring manual resolution at 25 min each = ~25–30 additional hours; total ~50–61 hours/business-day; with 10 clerks that's ~5–6 hours each; reasonable with payment runs, GRNI follow-up, vendor statement reconciliation (W7d), and other duties; note that month-end peaks (+50% per W7) push daily volume to ~460–550 invoices/day during close week, requiring temporary overtime or redeployment of 2–3 other Finance staff (Cost Accountant, Treasury Analyst) to AP to maintain processing SLA; peak staffing contingency documented in W7
- **1 AP Supervisor**: Oversight, aging review, GRNI escalation management, escalations.
- **2 Treasury Analysts**: Payment approval, bank file transmission, LC management. Shared with AR and other treasury duties.

### W7c. Non-PO / Recurring Expense Invoice Processing

| Field | Detail |
|---|---|
| **Trigger** | Utility bill, service invoice, rent, or other recurring expense received without a Purchase Order |
| **Frequency** | ~2,000–3,000 non-PO invoices/month across all locations (200 stores + 5 DCs + HQ); combined with ~6,500 merchandise/vendor invoices (W7), total AP invoice volume is ~8,500–9,500/month; the ~6,000–7,000 figure in the model-company-profile §10.2 refers to merchandise/vendor invoices only |
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

### W7d. AP Vendor Statement Reconciliation

| Field | Detail |
|---|---|
| **Trigger** | Monthly vendor statement received (email, mail, or vendor portal) |
| **Frequency** | Monthly for top 50 vendors (by spend); quarterly for remaining active vendors |
| **Volume** | ~50 monthly reconciliations + ~750 quarterly reconciliations; top 50 = 45% of COGS |
| **Owner** | AP Clerk |
| **Participants** | AP Clerk, AP Supervisor, Buyer (for discrepancies) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Vendor submits monthly or quarterly statement showing all invoices, credit memos, and payments for the period; AP Clerk receives and logs statement in system | AP Clerk | AP Supervisor | 5 min/vendor |
| 2 | System attempts auto-reconciliation: matches vendor statement line items to AP sub-ledger transactions (invoices, credit memos, payments) by invoice number, date, and amount | System | — | Automated |
| 3 | System generates reconciliation summary: matched items, unmatched vendor lines (vendor shows invoice not in AP), unmatched AP lines (AP shows invoice not on vendor statement), and amount variances | System | — | Automated |
| 4 | AP Clerk investigates unmatched items: (a) **unmatched vendor lines** — vendor invoice not yet received or not yet entered in AP; if invoice is valid and GR exists, AP Clerk enters invoice per W7; if no GR, flags for Buyer follow-up with vendor; (b) **unmatched AP lines** — payment made but vendor did not credit; AP Clerk provides payment reference (bank transfer date, amount) for vendor to apply; (c) **amount variances** — typically partial payments, discounts taken, or EWT deduction not reflected on vendor statement; AP Clerk explains variance with supporting documentation | AP Clerk | AP Supervisor | 15–30 min/vendor |
| 5 | AP Clerk documents reconciliation result: matched amount, unmatched items with explanation, and net variance; flags reconciling items > PHP 50,000 or items > 60 days unresolved for AP Supervisor review | AP Clerk | AP Supervisor | 10 min/vendor |
| 6 | Monthly: AP Supervisor reviews vendor reconciliation summary for top 50 vendors — total matched vs. unmatched, aging of reconciling items, recurring discrepancy patterns; escalating chronic discrepancies to Buyer for vendor relationship review per W44 | AP Supervisor | Controller | 1 hour/month |
| 7 | Quarterly: AP Supervisor includes vendor reconciliation metrics in AP controls review (cross-reference CTL-42 in Internal Controls Matrix); unreconciled balances > 90 days escalated to Controller for potential write-off or accrual adjustment | AP Supervisor | Controller | 30 min/quarter |

### System Touchpoints
- Vendor statement import: AP Clerk uploads vendor statement (PDF, Excel, or EDI); system parses line items for auto-matching (W7d.1–2)
- Auto-reconciliation engine: matches vendor statement lines to AP sub-ledger by invoice number, date, and amount with configurable tolerance (W7d.2)
- Reconciliation summary dashboard: matched, unmatched (vendor-side), unmatched (AP-side), and variance items with drill-down (W7d.3)
- Reconciliation documentation: auditor-ready log showing reconciliation result per vendor per period with aging of reconciling items (W7d.5)
- Vendor reconciliation analytics: match rate, average reconciliation time, recurring discrepancy vendors, aging of unresolved items (W7d.6)
- Integration with W7 (AP invoice processing), W7c (non-PO invoices), W44 (vendor performance — chronic reconciliation issues affect vendor scorecard)

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
| 8a | **AR legal collection escalation**: for accounts > 120 days overdue with no payment response after standard collection tiers (W8.6–8) — (a) AR Supervisor sends formal demand letter (demand collection letter per Philippine legal requirements) via registered mail with return card; letter states outstanding amount, original invoice references, payment deadline (15 business days), and notice of potential legal action; (b) if customer responds and disputes: AR Clerk coordinates investigation with Sales Rep and Store Manager to validate or resolve dispute; disputed amounts suspended from collection while under investigation; (c) if no response after demand letter deadline: AR Supervisor escalates to Finance Manager for referral to external collection agency or Legal for filing of collection case; (d) external collection agency engaged per W62 (service contract); agency fee typically 10–20% of collected amount; system tracks collection agency referral with agency reference and status; (e) if legal action warranted (amount > PHP 200,000 and customer solvent): Legal files collection case with appropriate court; Legal manages case with external counsel; system tracks legal case reference and status; (f) **Bad debt write-off**: if all collection efforts exhausted (demand letter + collection agency + legal if applicable) or customer confirmed insolvent/bankrupt, AR Clerk submits bad debt write-off request — tiered approval per W8.8b below; system posts Dr. Bad Debt Expense / Cr. Allowance for Doubtful Accounts (or direct write-off Dr. Bad Debt Expense / Cr. AR per company policy); BIR documentation retained: demand letter, collection agency report, court filing (if applicable), write-off approval; (g) **Write-off recovery**: if customer subsequently pays on a previously written-off account (recovery of bad debt), AR Clerk processes recovery payment; system posts Dr. Cash / Cr. Bad Debt Recovery (income); write-off recovery tracked separately from regular AR collections for reporting | AR Supervisor / Finance Manager / Legal / CFO | Controller | Varies |
| 8b | **Bad debt write-off approval**: (a) ≤ PHP 50,000: Finance Manager, (b) PHP 50,001–200,000: Controller + Finance Manager, (c) PHP 200,001–1,000,000: CFO, (d) > PHP 1,000,000: CEO | Approver | Approver | 15 min/write-off |
| 9 | Customer payment received; AR Clerk applies payment to open invoices | AR Clerk | AR Supervisor | 5 min/payment |
| 10 | Monthly reconciliation of AR sub-ledger to GL | AR Clerk | AR Supervisor | 2 hours/month |
11 | Customer credit memo: AR Clerk creates credit memo with reason code and source reference (pricing error, volume discount adjustment, short delivery, service failure, promotional adjustment); tiered approval (AR Supervisor ≤ PHP 10,000; Finance Manager ≤ PHP 50,000; CFO > PHP 50,000); system applies credit to oldest open invoice or creates credit balance; posts GL entry (Dr. Revenue or appropriate expense / Cr. Accounts Receivable); customer notified of credit | AR Clerk / AR Supervisor | Finance Manager | 10 min/credit memo |
12 | **Customer account closure**: customer requests trade/corporate account closure; AR Clerk verifies zero outstanding balance — if balance outstanding, arranges final payment or collection per W8.6–8; system settles any open credit memos (applies to outstanding invoices or processes refund); loyalty points: if customer has unredeemed points, system offers redemption before closure or forfeits per W17 terms; AR Clerk deactivates account in system; account status changed to "Closed"; system retains transaction history for 7-year BIR retention; PII anonymized after retention period per RA 10173 and W53 data retention policy; account closure logged with reason, date, and AR Clerk ID | AR Clerk | AR Supervisor | 15 min/closure |

### System Touchpoints
- AR invoice creation from POS/sales order (W8.1–2)
- Real-time credit limit check (W8.3)
- Credit hold override with tiered authorization, audit trail, and automatic expiry (W8.3a)
- Aging report generation (W8.5)
- Customer statement generation (W8.4)
- Customer credit memo processing: reason code and source reference, tiered approval, auto-application to open invoices, GL posting (Dr. Revenue/Expense / Cr. AR), credit balance management (W8.11)
- Dormant trade/corporate account management: system defines dormancy as zero transactions (sales or payments) for 6 consecutive months; monthly, system generates dormant account report listing all accounts meeting dormancy criteria; AR Clerk contacts dormant accounts via phone/email to confirm business status — (a) if customer confirms active but no current need: account remains active, no action; (b) if customer unresponsive after 2 contact attempts over 30 days: AR Supervisor places account on inactive status; system automatically reduces credit limit to PHP 0 (prevents new sales on account); account remains searchable for transaction history and reactivation; (c) if customer confirms business closure: AR Clerk processes formal account closure per W8 step 12 — verifies zero outstanding balance, settles open credit memos, manages loyalty points disposition, deactivates account, retains transaction history for 7-year BIR retention period, anonymizes PII after retention period per RA 10173 (cross-reference W53); for reactivation of inactive accounts: customer contacts Sales Rep or AR Clerk; AR Clerk reopens account with updated business documents per W24 (abbreviated credit assessment — if reactivation within 12 months, may reuse prior credit assessment with updated financials; if > 12 months, full W24 process required); AR Supervisor approves reactivation with new credit limit; annual: AR Supervisor reviews all dormant/inactive accounts and recommends write-off of any remaining immaterial balances (< PHP 5,000) with Finance Manager approval
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
| 6 | Inventory: Verify perpetual WAC (weighted average cost) calculations; post adjustments from cycle counts | Cost Accountant | Controller | 2 hours |
6a | WAC methodology: system calculates perpetual moving average cost at each goods receipt — new WAC = (prior inventory value + receipt value) ÷ (prior quantity + receipt quantity); COGS at POS uses current WAC at time of sale; at month-end, Cost Accountant verifies WAC accuracy by sampling high-value and high-volume SKUs, reconciles total inventory valuation to GL inventory accounts, and posts any adjustments from cycle counts (W6) or physical inventory (W42) | Cost Accountant | Controller | Part of 2 hours |
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
16c | Local Business Tax (LBT) per LGU: system generates LBT payment schedule per location (200 stores + 5 DCs + HQ) based on configured LGU calendars (annual or quarterly per LGU); Tax Accountant reviews schedule, validates amounts per LGU rate schedules (typically 1–2% of gross receipts for retail, varies by LGU); processes payments per LGU (online, over-the-counter, or LGU office); system posts payment per location (Dr. Local Business Tax Expense / Cr. Cash); tracks payment status and receipt per location; flags locations with upcoming or overdue LBT payments on monthly dashboard | Tax Accountant | Controller | 4 hours/month (distributed across LGU due dates) |
| 16a | EWT remittance: Tax Accountant generates EWT remittance file (BIR 1601-E) from accumulated Withholding Tax Payable per vendor per ATC; reconciles to vendor remittance list; transmits to BIR via eFPS; system posts remittance (Dr. Withholding Tax Payable / Cr. Cash) | Tax Accountant | CFO | 1 hour |
| 16b | Inventory net realizable value (NRV) review: Cost Accountant runs inventory aging report (days since last sale); for slow-moving items (> 180 days), system compares WAC to estimated NRV (clearance price × sell-through probability); Cost Accountant proposes write-down per SKU where NRV < cost; Controller approves write-downs > PHP 50,000; system posts Dr. Inventory Write-Down Expense / Cr. Inventory Provision (contra-asset); **NRV reversal treatment**: when a written-down item is subsequently sold — (a) system recognizes revenue at selling price (standard), (b) system recognizes COGS at the written-down carrying amount (not the original WAC), (c) difference between original WAC and written-down carrying amount represents the write-down previously recognized; for partial sales of written-down lots, COGS per unit is the written-down unit cost; no additional journal entry is required at point of sale because the provision was already posted; at next quarterly NRV review (W9a.16b), Cost Accountant reassesses remaining written-down items — if NRV has recovered above carrying amount (e.g., market price increase), Cost Accountant may reverse the provision up to the original write-down amount per PAS 2.31 with Controller approval; system posts reversal as Dr. Inventory Provision / Cr. Inventory Write-Down Recovery (P&L); reversal is limited to the original write-down amount per SKU — carrying value cannot exceed original WAC | Cost Accountant / Controller | Controller | 2 hours |
| 16d | Inventory write-off (obsolete / damaged beyond recovery): distinct from NRV write-down (step 16b) — for items that will never be sold (fully obsolete, expired, irrevocably damaged, or vendor refuses RTV and item has no residual value); Cost Accountant prepares write-off list per SKU with supporting evidence (photos, aging, disposition attempts); tiered approval: Store Manager ≤ PHP 10,000, Controller ≤ PHP 50,000, CFO ≤ PHP 500,000, CEO > PHP 500,000; system posts Dr. Inventory Write-Off Expense (loss) / Cr. Inventory — removes items from inventory register entirely (not a provision — permanent removal); BIR documentation retained: write-off approval, supporting evidence, and physical destruction or disposal certificate | Cost Accountant / Controller | CFO | 1 hour |
| 16e | Credit note / debit note reconciliation: Chief Accountant runs AP and AR credit note aging report — all unapplied credit memos and debit memos listed by entity, vendor/customer, age, and amount; credit memos > 60 days unapplied flagged for investigation; AP Clerk contacts vendor to resolve open AP credits (apply to next invoice, request refund, or confirm as settled); AR Clerk contacts customers to resolve open AR credits (apply to next sale, issue refund, or confirm as settled); unresolved items > 90 days escalated to Controller; summary of unapplied credit notes included in month-end close package | Chief Accountant / AP Clerk / AR Clerk | Controller | 1 hour |
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
- Inventory valuation engine: perpetual WAC verification (not periodic recalculation); month-end reconciliation of inventory valuation to GL (W9a.6a)
- Bank reconciliation (W9a.9)
- Local Business Tax (LBT) per LGU: per-location LBT calendar, payment tracking and schedule; LGU-specific rate schedules and forms; payment status dashboard with overdue alerting; BIR retention of LBT receipts (W9a.16c)
- Multi-entity financial statement generation (W9a.12–14)
- Period lock / close controls (W9a.17)
- BIR tax form generation (W9a.16)
- EWT remittance file generation per BIR 1601-E with per-vendor per-ATC breakdown; eFPS transmission (W9a.16a)
- Inventory NRV review: aging by days-since-last-sale, NRV calculator, write-down journal entry with approval, provision reversal on subsequent sale (PAS 2.31 compliant — reversal limited to original write-down; carrying value capped at original WAC; quarterly reassessment with Cost Accountant and Controller review) (W9a.16b)
- Inventory write-off: complete removal from inventory register (not provision); tiered approval with BIR-compliant documentation (photos, aging, disposition evidence, destruction certificate); distinct from NRV write-down (W9a.16d)
- Credit note / debit note reconciliation: AP and AR credit note aging report with unapplied memos > 60 days flagged; escalation at 90 days; resolution tracking (apply, refund, settle); summary in month-end close package (W9a.16e)

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
- Agency / manpower contractor worker management: for seasonal and peak-period staffing (Christmas season, bi-monthly sale events, new store openings), BuildRight engages licensed manpower agencies per DOLE Department Order No. 174 (Labor-Only Contracting rules); agency workers are NOT employees of BuildRight entities — they appear in the agency's payroll, not in BuildRight's W10 payroll run; system tracks agency worker headcount separately from regular headcount for workforce planning; Store Manager submits agency staffing request to HR with headcount, duration, and skill requirements; HR coordinates with approved agency partners; agency invoices are processed as non-PO service invoices per W7c with DOLE-compliant documentation (agency service agreement, worker deployment list, attendance records); agency workers are issued temporary POS and access badges with limited system permissions and defined expiry dates; system distinguishes agency hours from regular employee hours for labor cost reporting (agency cost is a contract service expense, not payroll); typical agency worker deployment: 2–5 per store during November–December peak, and 10–15 per new store opening (W16) for the first 2 weeks of operations
- Agency worker access provisioning: Store Manager submits agency worker access request to IT via W48 helpdesk ticket, specifying worker name, agency, assignment duration, and required access level; IT creates temporary system account with predefined "Agency Worker" permission template (POS transaction processing only — no voids, no price overrides, no manager functions, no reports); access badge created with defined expiry date matching deployment end date; system auto-revokes access on expiry date; at end of deployment, Store Manager verifies badge return and IT confirms system deactivation; if deployment extended, Store Manager submits extension request before expiry; system logs all agency worker access with agency name, worker name, store, start/end dates, and permission level; monthly: IT generates agency worker access report showing active, expired, and unreturned badges; unreturned badges flagged for Store Manager follow-up (W10, cross-reference W71 access badge management)

### Statutory Compliance Calendar

The following table shows all recurring statutory remittance deadlines per entity. System generates alerts 5 business days before each deadline.

| Statutory Obligation | Frequency | Deadline | Remittance Method | Responsible | Cross-Reference |
|---|---|---|---|---|---|
| SSS employee + employer contributions | Monthly | Last day of following month (or 10th of second month per SSS schedule) | PRN via SSS online portal or bank | Payroll Officer | W10.11 |
| PhilHealth contributions | Monthly | Every 10th of the following month | Electronic remittance via PhilHealth portal | Payroll Officer | W10.11 |
| Pag-IBIG contributions | Monthly | Every 10th of the following month | Online remittance via Pag-IBIG portal | Payroll Officer | W10.11 |
| BIR Withholding Tax on Compensation (1601-C) | Monthly | 10th of following month | eFPS / eBIRForms | Tax Accountant | W9a.16 |
| BIR Expanded Withholding Tax (1601-E) | Monthly | 10th of following month | eFPS / eBIRForms | Tax Accountant | W9a.16a |
| BIR VAT Return (2550M) | Monthly | 20th or 25th of following month (per BIR filing threshold) | eFPS / eBIRForms | Tax Accountant | W9a.16 |
| BIR Quarterly VAT / Income Tax (2550Q / 1702Q) | Quarterly | 25th of month following quarter end | eFPS / eBIRForms | Tax Accountant | W9a.16 |
| Local Business Tax per LGU | Per LGU calendar (annual or quarterly) | Per LGU deadline | Per LGU (online, OTC, or LGU office) | Tax Accountant | W9a.16c |
| 13th Month Pay distribution | Annual | On or before December 24 | Via payroll run | Payroll Officer | W10, W9b.18 |
| BIR Annual Income Tax Return (1702RT) | Annual | April 15 (or as extended) | eFPS / eBIRForms | Tax Accountant | W9b.21 |

> **Note**: Deadlines are based on current BIR and statutory agency guidelines; Payroll Manager reviews for regulatory changes quarterly. The 5-entity structure means each obligation is filed per-entity TIN; Payroll Officer and Tax Accountant process 5 submissions per deadline.

### Staffing Implication
- **2–3 Payroll Officers**: 5 entities × 2 runs = 10 runs/month. Each run takes ~6 hours. Total ~60 hours/month of payroll processing. 2 officers can handle this with time for reconciliation and inquiries.
- **1 Payroll Manager**: Approval, oversight, statutory compliance.
- **1–2 HR Assistants**: Leave and OT verification (data entry-heavy during payroll week).
- Fits within the ~16-person HR team.

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
- Ecommerce IC settlement for BOPIS: revenue is recognized by Depot Inc. at pickup (goods are Depot Inc. inventory); Digital Commerce Inc. (which collected payment online) remits collected payments to Depot Inc. monthly per W14 ecommerce payment collection IC flow; Digital Commerce Inc. charges Depot Inc. a per-order fulfillment fee per W14 ecommerce fulfillment IC flow; all IC settlements processed monthly via W14
- Ecommerce VAT for BOPIS: BOPIS transactions are subject to 12% VAT identical to in-store; output VAT is recognized by Depot Inc. (the entity recognizing revenue per IC model); Digital Commerce Inc. does not recognize VAT on payment collection (remitted to Depot Inc.); VAT on BOPIS transactions included in Depot Inc.'s BIR 2550M filing

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

### W12c. Cross-Store Returns (Purchased at Store A, Returned at Store B)

| Field | Detail |
|---|---|
| **Trigger** | Customer brings item to a different store than where it was purchased |
| **Frequency** | ~10–20% of returns = ~5,600–11,200/year; ~2–3 per store per month |
| **Volume** | Common for chain-wide customers (contractors, travelers) and loyalty members |
| **Owner** | Customer Service Rep (receiving store) |
| **Participants** | CSR (Store B), Store Manager (Store B), Stock Associate (Store B) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer presents item and receipt (or loyalty card for transaction lookup) at CSR counter of Store B (different from purchase Store A) | Customer | — | — |
| 2 | CSR looks up original transaction in system by receipt number or loyalty card; system supports cross-store transaction lookup across all 200 locations | CSR | — | 2 min |
| 3 | CSR inspects item condition (resalable, damaged, defective) per standard W12a.3 | CSR | — | 2 min |
| 4 | CSR processes cross-store return in system; Store Manager approval required for cross-store returns above PHP 5,000 (higher threshold than same-store due to fraud risk) | CSR | Store Manager | 3–5 min |
| 5 | System posts financial reversal to original purchase store (Store A): reverses revenue and COGS at Store A for correct store P&L attribution | System | — | Automated |
| 6 | System receives returned inventory at Store B: increases Store B inventory; system automatically creates an inter-store inventory adjustment to account for the physical inventory movement (Store B gains inventory, Store A's books already reflect the COGS reversal from step 5) | System | — | Automated |
| 7 | System processes refund to original tender method per W12a.6 split-tender rules; refund debited from Store A's cash accountability (system-level, not physical cash at Store B) | System / CSR | — | 2 min |
| 8 | Inventory returned to stock at Store B (if resalable) or flagged as damaged/defective per W12a.7–8 | Stock Associate | Dept. Supervisor | 5 min |

### System Touchpoints (Cross-Store Returns)
- Cross-store transaction lookup: system retrieves original transaction from any store location by receipt number or loyalty card (W12c.2)
- Cross-location financial posting: revenue reversal and COGS adjustment posted to original purchase store (Store A) for correct P&L attribution; inventory received at return store (Store B) (W12c.5–6)
- Automatic inter-store inventory adjustment: system accounts for physical inventory movement between locations without requiring a separate Transfer Order (W12c.6)
- Cross-store refund processing: refund debited from original store's tender accountability; physical cash disbursed at return store reconciled via centralized treasury (W12c.7)
- Manager approval threshold for cross-store returns (W12c.4)

### System Touchpoints (All Returns)
- Transaction lookup by receipt number / loyalty card, including cross-store lookup (W12a.2, W12c.2)
- Return policy enforcement (time window, condition rules) (W12a.4)
- Manager override for policy exceptions (W12a.5)
- Refund processing to original tender (W12a.6)
- Inventory status change (saleable vs. damaged) (W12a.7)
- RTV tracking (W12a.8)
- Online return initiation with QR authorization (W12b.2)
- Split-tender refund processing: pro-rata refund to each original tender method; cash availability threshold enforcement with automatic redirect to card/e-wallet for excess (W12a.6)
- Home delivery return reverse logistics: for bulky items that cannot be transported to store, system schedules carrier pickup via 3PL integration (W19 delivery partners); tracks return shipment to DC; DC inspection and disposition; refund processed upon inspection confirmation (cross-reference W19.12a)
- Loyalty points reversal on returns: when a return is processed (W12a, W12b, W12c), system automatically reverses loyalty points earned on the original transaction — points deducted from customer's loyalty balance based on the returned item's contribution to the original points earning (pro-rata for partial returns); if customer does not have sufficient points balance for reversal (points already redeemed), system creates a negative points balance (points debt) that is recovered from future earning; system logs points reversal with return transaction reference for audit; for cross-store returns (W12c), loyalty reversal posts to the loyalty account (chain-wide) not to a specific store; loyalty points reversal is enforced even for no-receipt returns where original transaction is identified via loyalty card lookup (W12a.5)
- Cross-store return processing: cross-location transaction lookup, financial reversal at original store, inventory receipt at return store, inter-store inventory adjustment (W12c)

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
- Vendor-funded promotional settlement: for promotions where the vendor funds the markdown (e.g., "buy paint at 20% off, funded by vendor"), system records vendor funding portion per transaction line at POS; accumulates vendor liability in a dedicated promo settlement accrual account; monthly settlement report generated per vendor showing units sold at promo price × vendor share; AP credit memo generated per W7.9b to settle vendor obligation; distinct from W27 (volume-based rebates) — vendor-funded promos are pre-agreed markdown reimbursements tied to specific promotional events
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
- Dual IC framework: BuildRight operates two intercompany models — (1) **Service-based IC** (primary): monthly fees for warehousing (Logistics Inc.), ecommerce fulfillment (Digital Commerce Inc.), rent (Property Mgmt Inc.), and management fees (Holdings Inc.) — no goods change ownership between entities; Depot Inc. owns all merchandise inventory throughout the supply chain; standard DC→Store replenishment (W4) and inter-DC transfers (W22) are intra-entity inventory movements, not IC goods transfers; (2) **Goods-based IC** (rare): if inter-entity goods transfer is needed (e.g., Digital Commerce Inc. purchases goods from Depot Inc. for direct resale, Property Mgmt Inc. purchases building materials for property maintenance), system creates IC sales order and IC purchase order at configured transfer price; IC invoice auto-generated at receipt; IC elimination during consolidation per W9a.13; system supports both models with different GL posting paths (W14)
- IC settlement timing: all IC flows (service-based and goods-based) are settled on a single monthly net settlement date (typically 5th of the following month) as part of W14 step 6; Digital Commerce Inc. remits collected ecommerce payments to Depot Inc. on this same schedule (not daily or weekly), which means Depot Inc. carries up to 30 days of ecommerce revenue as an IC receivable from Digital Commerce Inc.; Treasury accounts for this timing in cash flow forecasting (W30 step 8); if ecommerce GMV grows significantly (Year 2–3 target of PHP 250–350M/month), consider moving ecommerce payment remittance to twice-monthly to reduce IC receivable exposure

### Goods-Based IC Trigger Scenarios

While the primary IC model is service-based, the following concrete scenarios would trigger a goods-based intercompany transfer (Depot Inc. sells goods to another entity at arm's-length transfer price):

| Scenario | From | To | Trigger | IC Pricing Basis | Approval |
|---|---|---|---|---|---|
| Property Mgmt Inc. purchases building materials for property maintenance or tenant improvements | Depot Inc. | Property Mgmt Inc. | Property Mgmt Inc. submits material requisition for repair/renovation of leased premises (BuildRight stores, DC facilities, or HQ office) | Depot Inc. cost + 5% markup (arm's-length; below retail SRP) | Property Mgmt Inc. Facilities Coordinator + Depot Inc. Category Manager |
| Digital Commerce Inc. purchases office supplies or IT peripherals for internal use | Depot Inc. | Digital Commerce Inc. | Digital Commerce Inc. office manager requests items not available through standard IT procurement | Standard SRP (small volumes; immaterial) | Digital Commerce Inc. Dept. Head |
| Logistics Inc. purchases warehouse supplies (racking, safety equipment, packaging materials) from Depot Inc. inventory | Depot Inc. | Logistics Inc. | DC Supervisor identifies need for operational supplies stocked in Depot Inc. inventory | Depot Inc. cost + 5% markup | Logistics Inc. DC Manager + Depot Inc. Category Manager |

For each goods-based IC transfer: system creates IC Sales Order (selling entity) and IC Purchase Order (buying entity) at configured transfer price; goods physically transferred from Depot Inc. stock; IC invoice auto-generated; IC elimination during consolidation per W9a.13. Estimated volume: < 20 goods-based IC transactions/year across all entity pairs.

### Goods-Based IC System Flow Detail

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Requesting entity creates IC Purchase Requisition in system: item(s), quantity, justification, requesting entity, delivery location | Requesting entity staff | Requesting entity Dept. Head | 10 min |
| 2 | System checks Depot Inc. inventory availability at nearest DC/store with ATP; if available, auto-creates IC Sales Order in Depot Inc. and linked IC Purchase Order in requesting entity at configured transfer pricing rule (cost + 5% markup for materials; SRP for small office supplies) | System | — | Automated |
| 3 | If IC value > PHP 50,000: approval required from requesting entity Finance Manager and Depot Inc. Category Manager; if < PHP 50,000: auto-approved within contract parameters | Approver(s) | CFO | 15 min |
| 4 | Depot Inc. DC or store picks goods; scan-confirms shipment; system reduces Depot Inc. inventory, creates in-transit inventory | DC/Store Staff | DC Supervisor / Store Manager | Per W3/W22 |
| 5 | Requesting entity receives goods; scan-confirms receipt; system increases requesting entity inventory (if applicable) or posts directly to expense/consumption | Receiving Staff | Dept. Head | Per W3/W18 |
| 6 | System auto-generates IC invoice from IC Sales Order at transfer price; simultaneous posting: Depot Inc. Dr. IC Receivable / Cr. IC Revenue + Cr. Inventory (at cost); requesting entity Dr. Expense/Inventory / Cr. IC Payable | System | — | Automated |
| 7 | IC invoice included in monthly W14 IC reconciliation and settlement cycle | Chief Accountant | Controller | Per W14 |

### Annual IC Transfer Pricing Review

### IC Invoice Dispute Resolution

| Field | Detail |
|---|---|
| **Trigger** | One entity disputes an IC charge generated by another entity (e.g., Depot Inc. contests a Logistics Inc. warehousing fee calculation, or Digital Commerce Inc. disputes an ecommerce fulfillment fee) |
| **Frequency** | Occasional — estimated 2–5 disputes/year |
| **Owner** | Chief Accountant |
| **Participants** | Chief Accountant, disputing entity's Finance lead, CFO |

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Receiving entity's Finance lead identifies IC charge discrepancy: amount does not match agreed transfer pricing rule, volume calculation is incorrect, or charge was not anticipated | Entity Finance Lead | Chief Accountant | 15 min |
| 2 | Chief Accountant reviews the disputed IC invoice against the configured transfer pricing rule and underlying transaction data (e.g., number of orders fulfilled, square meters leased, payment collections remitted) | Chief Accountant | Controller | 30 min |
| 3 | If calculation error confirmed: Chief Accountant corrects the IC invoice in system; system reposts corrected entries in both entities; no further escalation needed | Chief Accountant | Controller | 15 min |
| 4 | If dispute is about pricing rule interpretation (not a calculation error): Chief Accountant escalates to CFO for ruling; CFO interprets the transfer pricing agreement per the documented IC framework (W14) | CFO | CEO | 30 min |
| 5 | CFO decision is final; Chief Accountant adjusts IC invoice if needed; Controller documents the interpretation precedent for inclusion in annual IC transfer pricing review (W14 annual review) | CFO / Chief Accountant | Controller | 15 min |
| 6 | If dispute reveals a systemic issue with the IC pricing rule: CFO initiates an early review of the applicable IC pricing rule (outside the annual cycle) and updates the system configuration | CFO | CEO | 1 hour |

**Dispute SLA**: All IC disputes must be resolved within the same monthly close period. Unresolved disputes block the close for both entities.

### IC Loan Lifecycle

| Field | Detail |
|---|---|
| **Trigger** | Subsidiary requires funding for working capital, capex, or seasonal cash flow needs beyond internal cash generation |
| **Frequency** | As needed; typically 5–10 IC loan events/year |
| **Owner** | CFO |
| **Participants** | CFO, Treasury Analyst, Chief Accountant, borrowing entity Finance lead |

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Subsidiary Finance lead identifies funding need; submits IC loan request to CFO with amount, purpose, proposed repayment schedule, and cash flow justification | Entity Finance Lead | CFO | 30 min |
| 2 | CFO approves IC loan; defines terms: principal, interest rate (at minimum the BIR-prescribed rate per RR 19-2020 for arm's-length compliance — currently 12% per annum or the applicable BIR rate), repayment schedule (lump sum or amortizing), and maturity date | CFO | CEO | 15 min |
| 3 | Treasury Analyst executes inter-entity bank transfer; system posts IC loan entry (Dr. IC Loan Receivable in lending entity / Cr. Cash; Dr. Cash / Cr. IC Loan Payable in borrowing entity) | Treasury Analyst | CFO | 15 min |
| 4 | System calculates monthly interest accrual per loan terms: Dr. IC Interest Receivable / Cr. IC Interest Income in lending entity; Dr. Interest Expense / Cr. IC Interest Payable in borrowing entity; interest accrual posts automatically at month-end as part of W9a close | System | Controller | Automated |
| 5 | Monthly: Chief Accountant reconciles IC loan balances (principal + accrued interest) across lending and borrowing entities as part of W14 step 4 IC reconciliation | Chief Accountant | Controller | Part of W14 |
| 6 | At repayment: Treasury Analyst executes repayment transfer; system posts principal repayment and any remaining accrued interest; IC loan balance reduced accordingly | Treasury Analyst | CFO | 15 min |
| 7 | At maturity: if loan not yet repaid, system alerts CFO 30 days before maturity; CFO decides to extend, demand repayment, or convert to equity (with Board approval if applicable) | System / CFO | CEO | Automated + 15 min decision |
| 8 | Annual: CFO reviews all IC loan balances and terms as part of W14 annual transfer pricing review; confirms arm's-length compliance; adjusts terms if regulatory rates change | CFO | CEO | Part of W14 annual review |

### System Touchpoints (IC Loans)
- IC loan record creation with principal, interest rate, repayment schedule, and maturity date (W14 IC Loans step 2)
- Automatic monthly interest accrual with GL posting in both entities (W14 IC Loans step 4)
- IC loan balance tracking with maturity alerting at 30 days (W14 IC Loans step 7)
- IC loan reconciliation integrated into monthly W14 IC matching (W14 IC Loans step 5)
- BIR arm's-length interest rate compliance: system validates that IC loan interest rate meets or exceeds BIR-prescribed minimum; flags loans below threshold for CFO review (W14 IC Loans step 2)
- Integration with W9a (interest accrual in month-end close), W14 (IC reconciliation), W30 (cash transfer execution), W26 (budget — IC borrowing planned in annual budget)

### Annual IC Transfer Pricing Review (continued)

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
| 3a | **Applicant tracking detail**: system tracks all applicants through a structured pipeline — Applied → Phone Screen → Interview (1st) → Interview (2nd) → Offer → Hired / Rejected; each pipeline stage records date, recruiter notes, interviewer feedback (rating 1–5), and outcome; system auto-sends rejection email to unsuccessful candidates at each stage with configurable template; for high-volume store roles (Sales Associates, Cashiers, Stock Associates), Recruitment Officer may use a walk-in hiring event model with batch applicant entry and bulk status updates; system generates recruitment analytics: time-to-fill by role, sourcing channel effectiveness (job boards, walk-in, referral, social media), offer acceptance rate, interviewer assessment scores; applicant data retained for 1 year per RA 10173 (with candidate consent) for potential future openings | Recruitment Officer | HR Head | Ongoing |
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

### Go-Live Day Cutover Plan (Grand Opening Day)

The following hour-by-hour plan covers the system activation sequence on the day of grand opening (W16 step 13). Executed by IT Team + Store Manager with Store Ops Director on-site.

| Time | Activity | Role (R) | Verification |
|---|---|---|---|
| T-120 min (6:00 AM) | IT activates store location in production ERP; runs final data validation (item master, price file, GL segments, tax registration, LGU permit data) | IT Team | System validation report — all checks green |
| T-90 min (6:30 AM) | POS terminals powered on; verify real-time connectivity to ERP; download current price file; print test receipt confirming BIR-registered format | IT Team + Cashier | Test receipt prints correctly with TIN, registered invoice number |
| T-75 min (6:45 AM) | Cash floats loaded into all 5 terminals; opening Z-report baseline verified at zero | Cashier | Z-report shows zero opening balance per terminal |
| T-60 min (7:00 AM) | Store Manager and IT conduct final walkthrough: verify shelf tags match system prices on 20 sample items across departments; verify signage, security systems, and alarm test | Store Manager + IT | Price verification checklist signed |
| T-45 min (7:15 AM) | DC dispatch confirms final pre-opening delivery has been received and posted; system inventory matches physical count from soft opening (W16 step 12) | Receiving Clerk + IT | System on-hand = physical count |
| T-30 min (7:30 AM) | Store Manager briefs all staff: operating procedures, escalation contacts for IT issues (W48 helpdesk), offline POS procedures (W5g) if connectivity fails | Store Manager | Staff acknowledgment |
| T-15 min (7:45 AM) | IT performs live test transaction: scan item, process loyalty enrollment, complete payment by card; void test transaction; verify all entries posted correctly in ERP | IT Team + Cashier | Transaction, loyalty, payment, and void all verified in system |
| T-0 (8:00 AM) | Doors open; first live customer transaction | All | Store Manager monitors first 10 transactions for anomalies |
| T+60 min (9:00 AM) | IT Team confirms all POS terminals stable; real-time inventory deduction verified; helpdesk monitors for incident tickets from new store | IT Team | No P1/P2 tickets |
| T+4 hrs (12:00 PM) | Store Manager runs midday spot-check: 5 random items scanned at POS — prices correct, inventory deducting | Store Manager | Spot-check log |
| End of day | Store Manager runs standard closing procedure (W5c); IT reviews day-end Z-reports; all transactions reconciled; any exceptions logged as W48 tickets | Store Manager + IT | Z-report balances, no unresolved exceptions |
| T+1 day | IT Team and Store Ops Director conduct post-go-live review: transaction volume, POS performance, any incidents, customer feedback | IT Team + Store Ops Director | Post-go-live report filed |
| T+2 to T+7 days | **IT shadow period**: 1 dedicated IT support staff remains on-site or on-standby (remote with < 15 min response) for the first full operating week post-opening; monitors POS stability, transaction processing, offline mode readiness, and connectivity; any P1/P2 incidents during shadow period receive immediate on-site resolution; shadow staff logs all incidents and resolutions in W48 helpdesk; at end of shadow week, IT confirms store is stable and transitions to standard W48 remote support | IT Shadow Staff + Store Manager | CIO |
| T+30 days | IT Team and Store Ops Director conduct 30-day post-go-live review: transaction volumes, system stability, incident history, store staff confidence assessment | IT Team + Store Ops Director | 30-day review filed |

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

### Loyalty Program Economics

| Parameter | Value | Notes |
|---|---|---|
| Earn rate | 1 point per PHP 100 spent | Applied to transaction value after discounts, before VAT |
| Redemption value | PHP 1.00 per point | Each point can be redeemed for PHP 1.00 discount at checkout |
| Face value of points | 1% of qualifying transaction value | Face value = (1 point × PHP 1.00) ÷ PHP 100 = 1% of spend |
| PFRS 15 deferred revenue allocation | ~0.75–0.85% of qualifying transaction value | Standalone selling price allocation = face value (1%) × expected redemption rate (~75–85%); this is the actual amount allocated to deferred revenue at POS earning; the ~1.0% face value is NOT the PFRS 15 allocation rate — the allocation rate is lower because ~15–25% of points are expected to expire unredeemed (breakage) and are excluded from the standalone selling price of the points |
| Estimated monthly points earned | ~50M points (PHP 5B revenue ÷ PHP 100 × 1 point) | Before breakage adjustment |
| Estimated monthly deferred revenue allocation (PFRS 15) | ~PHP 50M/month (PHP 5B qualifying revenue × 1.0% allocation) | Monthly flow: new deferred revenue from points earned; recognized proportionally at redemption or as breakage at expiry |
| Estimated cumulative loyalty points liability (balance sheet) | ~PHP 1.2–1.8B (outstanding unredeemed points × PHP 1.00 × expected redemption rate ~75–85%) | Cumulative stock: outstanding points not yet redeemed or expired; reconciled monthly by Cost Accountant per W17.11a |
| Breakage (unredeemed expired points) | Recognized at 24-month expiry per W17.11 | Historically ~15–25% of points expire unredeemed |
| Tier upgrade thresholds | Bronze: 0–PHP 50K/year; Silver: PHP 50K–150K; Gold: PHP 150K–300K; Platinum: > PHP 300K | Based on trailing 12-month spend |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer signs up for loyalty program (in-store, online, or via app) | Customer / CSR | Loyalty Manager | 3 min (in-store) |
| 2 | System creates loyalty account with tier status (Bronze default); captures data privacy consent flag with purpose, date, and consent version per RA 10173 (Data Privacy Act) | System | — | Automated |
| 3 | At each POS transaction, cashier scans loyalty card or enters mobile number | Cashier | — | 15 sec |
| 4 | System calculates points earned (1 point per PHP 100 spent on transaction value after discounts, before VAT) and updates balance; per PFRS 15, system allocates ~1.0% of transaction revenue to loyalty deferred revenue based on relative standalone selling price of points (Dr. Cash or Accounts Receivable / Cr. Revenue for product portion ~99%, Cr. Deferred Revenue — Loyalty Points for points portion ~1%); allocation rate configurable based on expected redemption rate | System | — | Automated |
| 5 | Customer checks points balance via app, receipt, or in-store kiosk | Customer | — | Self-service |
| 6 | At checkout, customer requests points redemption; cashier selects redemption option | Cashier | — | 30 sec |
| 7 | System validates sufficient points; converts to peso value; applies as discount; system recognizes deferred revenue proportionally for redeemed points (Dr. Deferred Revenue — Loyalty Points / Cr. Revenue) | System | — | Automated |
| 8 | Monthly: Loyalty Manager reviews tier movement (upgrade/downgrade based on trailing 12-month spend) | System | Loyalty Manager | Automated + 1 hour review |
| 8a | **Tier downgrade proactive communication**: 60 days before a tier downgrade would take effect (based on trailing 12-month spend trajectory), system generates an alert for the Loyalty Manager; Loyalty Manager reviews at-risk accounts and triggers proactive communication: (a) system sends personalized email/SMS to customer notifying them of impending downgrade with specific spend threshold needed to maintain current tier, (b) includes a "stay" offer if configured (e.g., double-points weekend, member-exclusive discount coupon), (c) tracks customer response and incremental spend during the 60-day save window; monthly: Loyalty Manager reviews save rate (percentage of at-risk customers who maintain their tier) as a program engagement KPI; system does not send downgrade notices to customers on the lowest tier (Bronze) | System / Loyalty Manager | Loyalty Manager | Automated + 2 hours/month review |
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
- Loyalty fraud resolution process: when W37 loyalty fraud detection flags a suspected fraud pattern — (a) LPO creates fraud investigation case in system with detection rule triggered, affected account(s), and evidence; (b) Loyalty Manager reviews case within 2 business days and classifies: confirmed fraud, suspected fraud (requires further monitoring), or false positive; (c) **if confirmed fraud** — Loyalty Manager suspends the affected loyalty account (account cannot earn or redeem points; customer notified via email/SMS of suspension with reason and contact for appeal); LPO deducts fraudulently earned points (manual adjustment per approval tier above); if fraud involves employee (cashier self-scanning), LPO escalates per W37.5 confirmed irregularity process; (d) **if suspected fraud** — Loyalty Manager places account on monitoring status (all transactions flagged for 30-day observation period; no account suspension); if fraud confirmed during monitoring, escalate to confirmed fraud; if no further suspicious activity in 30 days, remove monitoring status; (e) **customer appeal**: customer may appeal suspension by contacting Customer Service; Loyalty Manager reviews appeal within 5 business days; if appeal upheld, account reinstated with apology communication and compensatory points per W41 complaint resolution; if appeal denied, account remains suspended; (f) **permanent ban**: for repeat offenders (2+ confirmed fraud incidents), Loyalty Manager recommends permanent account ban to Marketing Head for approval; permanently banned accounts cannot be reactivated; (g) monthly: Loyalty Manager generates fraud resolution summary — cases opened, confirmed, false positive rate, accounts suspended, points recovered; feeds into W37 shrinkage reporting
- Customer data deduplication: system performs fuzzy-match deduplication at enrollment (blocks creation if > 85% match on name + phone or name + email); Loyalty Manager reviews weekly deduplication queue of potential duplicates; merges approved records with points consolidation; monthly data quality dashboard showing duplicate rate, incomplete records, and invalid contact info (W17.1–2)
- Ecommerce loyalty points earning: for online orders (W11 BOPIS and W19 home delivery), system awards points when order is fulfilled (picked up for BOPIS, delivered for home delivery), not at order placement, because revenue recognition occurs at fulfillment; customer identifies loyalty account at online checkout via registered account linkage; guest checkout customers do not earn points; system calculates points using the same earn rate (1 point per PHP 100); PFRS 15 deferred revenue allocation follows same logic as in-store earning (W17.4); order fulfillment event triggers points earning via ecommerce-to-ERP integration

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

### W18b. DSD Vendor Delivery Scheduling

| Field | Detail |
|---|---|
| **Trigger** | Weekly DSD delivery schedule coordination |
| **Frequency** | Weekly schedule per DSD vendor; ~500–600 DSD deliveries/month across 200 stores |
| **Volume** | ~2–3 DSD deliveries per store per week; each vendor serves multiple stores per region |
| **Owner** | Buyer (coordination); Receiving Clerk (store execution) |

#### DSD Vendor Scheduling Process

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Buyer maintains DSD vendor delivery calendar per vendor: assigned stores, delivery frequency, preferred delivery day(s), contact person, special handling requirements | Buyer | Category Manager | 1 hour/vendor/quarter |
| 2 | Vendor or Buyer confirms weekly delivery schedule: which stores, which day, approximate time window, PO references (if applicable) | Buyer / Vendor | Buyer | 30 min/vendor/week |
| 3 | System pushes DSD delivery schedule to affected store Receiving Clerks via handheld/tablet notification; includes expected vendor, PO references, and time window | System | — | Automated |
| 4 | Receiving Clerk plans receiving dock availability around DSD schedule and DC replenishment truck schedule (W4); flags scheduling conflicts to Store Manager | Receiving Clerk | Store Manager | 15 min/day |
| 5 | If vendor misses scheduled delivery: Receiving Clerk reports no-show to Buyer; Buyer follows up with vendor; reschedules within the same week if possible; tracks vendor delivery reliability in vendor scorecard (W44) | Receiving Clerk / Buyer | Category Manager | 10 min/occurrence |

#### System Touchpoints (DSD Scheduling)
- DSD vendor delivery calendar per vendor with assigned stores and frequency (W18b.1)
- Weekly delivery schedule communication to store receiving (W18b.3)
- Scheduling conflict alerting when DSD and DC deliveries overlap (W18b.4)
- Vendor no-show tracking feeding into vendor scorecard (W44) (W18b.5)
- Integration with W18 (DSD receiving), W4 (DC replenishment scheduling), W44 (vendor performance)

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
| 2 | System routes order to nearest DC (or store if DC out of stock); creates pick list; **multi-DC order splitting**: if order contains items stocked at different DCs (e.g., bulky items at DC3 Laguna but specialty items only at DC5 Manila), system evaluates fulfillment options — (a) single-DC fulfillment preferred: ship all items from one DC if ATP available, even if not the closest DC for some lines; (b) split fulfillment: if no single DC has ATP for all items, system splits order into sub-orders per fulfillment DC — each sub-order gets its own tracking number, carrier assignment, and delivery timeline; customer receives a single order confirmation with "Items shipping from multiple locations" notice and per-sub-order tracking links; (c) split cost allocation: additional shipping cost from split fulfillment (if any) is absorbed by BuildRight, not charged to customer; (d) partial delivery: first sub-order ships immediately; remaining sub-orders ship as ATP becomes available; customer notified per sub-order status; (e) returns for split orders: customer may return all items to any BuildRight store per W12b regardless of which DC fulfilled; system handles cross-location inventory adjustment per W12c; Supply Planner reviews split fulfillment frequency weekly — high split rates for specific items trigger replenishment parameter review per W31.8 | System | — | Automated |
| 3 | DC receives pick task; assigns to picker by zone | WMS / DC Supervisor | DC Supervisor | 2 min |
| 4 | Picker picks items; scans each for confirmation | Picker | DC Supervisor | 5–15 min/order |
| 5 | If item unavailable: system offers substitution or cancels line; notifies customer | System / CSR | — | 3 min |
| 6 | Packer packs items for shipping; generates shipping label and packing slip | Packer | DC Supervisor | 5 min/order |
| 7 | System creates delivery order with selected partner (Lalamove, Transportify, own fleet) | System | DC Dispatch | Automated |
| 8 | Delivery partner picks up package; system updates order status to "Shipped" | Delivery Partner | DC Dispatch | 5 min |
| 9 | System sends tracking link to customer via SMS/email | System | — | Automated |
| 10 | Delivery partner delivers to customer; obtains proof of delivery (photo, signature) | Delivery Partner | — | Varies by distance |
| 11 | System marks order as "Delivered"; inventory formally deducted | System | — | Automated |
| 12 | If delivery fails (customer unavailable): system initiates failed delivery lifecycle — (a) 1st attempt: delivery partner leaves notification (call/SMS); customer given 2-hour window to respond for same-day re-delivery attempt; (b) if no response or 2nd attempt fails: order returns to DC; system sends customer notification with reschedule options (next available date) or cancellation option; (c) if customer reschedules: system creates new delivery order with carrier; (d) if customer cancels: system initiates refund to original payment method (Dr. Revenue / Cr. Cash) and DC restocks item per W12a.7; (e) if customer does not respond within 3 business days after return-to-DC: system auto-cancels order and initiates refund | Delivery Partner / DC | DC Supervisor | 15 min + carrier transit time |
| 12a | **Home delivery return (reverse logistics)**: for bulky/large items (appliances, lumber, tiles, fixtures) that the customer cannot transport to a store, system schedules carrier pickup via 3PL integration; carrier collects item from customer address and returns to originating DC; DC Receiving Clerk inspects returned item; if resalable: system processes refund to original payment method and restocks per W12a.7; if damaged: disposition per W6.8a (markdown, scrap, RTV); refund processed upon DC inspection confirmation | System / DC Receiving Clerk / CSR | DC Supervisor | 15 min/setup + carrier transit time
12b | **Carrier damage vs. vendor defect liability assignment**: when a home delivery customer reports damaged goods, CSR creates a damage report at intake with customer-provided photos and damage description; system routes damage report for liability determination: (a) **carrier damage** — external packaging damage, dents/scratches consistent with transit handling, item damage on one side, water damage to outer carton — CSR files carrier damage claim via 3PL integration (W19.7); carrier's insurance covers loss; customer receives immediate replacement or refund; system posts Dr. Carrier Claim Receivable / Cr. Inventory; (b) **vendor/manufacturing defect** — item defective out of box with intact packaging, missing parts, functional failure without physical damage — CSR processes vendor warranty claim (W33) or RTV (W3.6a); system posts Dr. Vendor Claim Receivable / Cr. Inventory; (c) **undetermined** — if cause unclear from photos, DC inspects returned item and makes final determination; (d) monthly: DC Supervisor generates delivery damage report — carrier damage rate by carrier (feeds W44/W62b), vendor defect rate by vendor (feeds W44), customer impact (refund vs. replacement) | CSR / DC Receiving Clerk | DC Supervisor | 10 min/classification

### W19b. Ship from Store (Store-Fulfilled Home Delivery)

| Field | Detail |
|---|---|
| **Trigger** | Customer places home delivery order on website/app; nearest DC out of stock but nearby store has ATP |
| **Frequency** | ~1,000–2,000 ship-from-store orders/month; primarily bulky items (appliances, lumber, tiles) with limited DC coverage |
| **Volume** | Avg 1–3 items per order |
| **Owner** | Store Manager (store execution); DC Dispatch (carrier coordination) |
| **Participants** | System (order routing), Stock Associate (picker), DC Dispatch, 3PL carrier, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System evaluates order fulfillment options: (a) DC fulfillment (standard W19) preferred, (b) if DC ATP = 0 for any line item, system checks ATP at stores within delivery radius of customer address, (c) if store ATP available, system offers ship-from-store as fulfillment option with estimated delivery date | System | — | Automated |
| 2 | Supply Planner or DC Dispatch reviews ship-from-store suggestion; confirms store has sufficient stock and store is not in a peak selling period (system shows store's current day sales velocity); approves or overrides to wait for DC replenishment | Supply Planner / DC Dispatch | DC Supervisor | 5 min/order |
| 3 | System routes order to selected store; creates store pick list with item locations; creates outbound shipment record | System | — | Automated |
| 4 | Store receives notification (tablet/terminal alert); Stock Associate picks items from sales floor or backroom; scan-confirms each item | Stock Associate | Dept. Supervisor | 10–20 min/order |
| 5 | Stock Associate stages picked items at store receiving/dispatch area; packs for shipping using packaging materials | Stock Associate | Dept. Supervisor | 10 min/order |
| 6 | DC Dispatch creates delivery order with 3PL carrier (same W19.7 integration); carrier picks up from store during scheduled route or on-demand | DC Dispatch / Carrier | DC Supervisor | 15 min/setup + pickup wait |
| 7 | Carrier delivers to customer per standard W19.10; proof of delivery captured | Carrier | — | Varies |
| 8 | System marks order "Delivered"; inventory deducted at store location (not DC); revenue recognized by Depot Inc. per standard ecommerce IC model (W14) | System | — | Automated |
| 9 | If customer returns ship-from-store item: standard W12b (online return) or W19.12a (reverse logistics pickup) — item returns to the originating store (not DC) if store has capacity; otherwise to DC | System / CSR | Store Manager | Per W12/W19 |

**Delivery SLA**: 3–7 business days (slightly longer than DC fulfillment due to carrier pickup from store)

### System Touchpoints (Ship from Store)
- Multi-origin fulfillment engine: DC fulfillment preferred, store fulfillment fallback when DC ATP = 0; configurable delivery radius per store (typically 20–30 km) (W19b.1)
- Store ATP check with real-time available inventory (on-hand − allocated − safety stock buffer) (W19b.1)
- Store pick list generation and scan confirmation (W19b.3–4)
- Outbound shipment creation from store location with 3PL carrier dispatch (W19b.6)
- Inventory deduction at store location upon delivery confirmation (W19b.8)
- Ecommerce IC settlement: identical to standard home delivery — Depot Inc. recognizes revenue; Digital Commerce Inc. remits payment per W14; Logistics Inc. charges per-order fulfillment fee per W14 (store fulfillment may have a different fee rate than DC fulfillment) (W19b.8)
- Integration with W19 (home delivery), W4 (store replenishment — ship-from-store consumption reduces store inventory), W14 (IC settlement)

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
- Home delivery reverse logistics: for bulky items requiring carrier pickup, system integrates with 3PL carriers to schedule reverse pickup at customer address; tracks return shipment to DC; DC inspection and disposition (restock, markdown, scrap, RTV); refund triggered upon inspection confirmation (W19.12a)
- 3PL / delivery partner management: carrier master record with rate cards per zone/weight/tier and SLA terms; automated carrier selection by delivery zone, package weight, and cost; carrier performance dashboard tracking on-time delivery %, damage rate, cost per delivery, and customer complaint rate per carrier; monthly carrier invoice reconciliation (carrier fees matched to completed delivery orders); quarterly carrier performance review similar to W44 vendor scorecard; rate renegotiation triggered by SLA breach or market benchmarking (W19.7, W19.8, W19.10)
- Ecommerce IC settlement for home delivery: revenue is recognized by Depot Inc. at delivery (goods are Depot Inc. inventory fulfilled by Logistics Inc. DCs); Digital Commerce Inc. (which collected payment online) remits collected payments to Depot Inc. monthly per W14 ecommerce payment collection IC flow; Logistics Inc. charges Depot Inc. a per-order fulfillment fee per W14 ecommerce fulfillment IC flow; all IC settlements processed monthly via W14
- Ecommerce VAT for home delivery: ecommerce transactions are subject to 12% VAT identical to in-store; output VAT is recognized by Depot Inc. (the entity recognizing revenue per IC model); Digital Commerce Inc. does not recognize VAT on payment collection (remitted to Depot Inc.); system tracks input VAT and output VAT per entity; VAT on ecommerce transactions included in Depot Inc.'s BIR 2550M filing

### Staffing Implication
- **Per DC**: Home delivery adds 17,200 orders/month ÷ 30 days ÷ 5 DCs = **~115 orders/DC/day**. At ~15 min pick+pack per order, that's **~29 hours/DC/day** of additional DC labor. This requires 3–4 dedicated pickers/packers per DC for home delivery, within the existing ~150 DC headcount (total DC pick/pack team of 15–20 handles both store replenishment at ~33 orders/day and ~115 home delivery orders/day in shifts). Home delivery orders are typically smaller (3–4 items) and packed individually, while store replenishment orders are larger (~50 lines) and packed in bulk — different skills and pacing.
- **Staffing implication**: Home delivery fulfillment absorbs a significant portion of DC pick/pack capacity. The 25–30 pickers/packers per DC should be sufficient for combined W4 + W19 volume, but DC management should monitor utilization during ecommerce growth. Peak ecommerce periods (sale events at 3× normal volume per data volumes §1.1) may require temporary surge staffing or overtime. During these peak periods, DC Supervisors should coordinate with HR to deploy agency workers (per W10 agency/manpower contractor management) for temporary pick/pack surge capacity, or arrange overtime for existing DC staff. Additionally, 3PL carrier surge capacity should be pre-arranged with delivery partners (W19.7) at least 2 weeks before planned promotional events (W13) to handle elevated home delivery order volumes.

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
- Quarterly VMI vendor statement reconciliation: Cost Accountant generates VMI statement reconciliation report per vendor — compares BuildRight's recorded VMI sell-through (units sold × agreed price) to vendor's statement of goods shipped and settled; investigates discrepancies (unrecorded sell-through, missing GRs, pricing differences, timing gaps); reconciling items documented and resolved within 15 business days; unreconciled differences > PHP 50,000 escalated to Controller; results feed into annual IC audit and vendor scorecard (W44) (W20)
- Integration with W44 (vendor scorecard), W7 (AP settlement), W42 (physical inventory vendor-owned count)

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
9a | Transfer discrepancy resolution: (a) if source picking error confirmed → source location absorbs loss (system posts inventory adjustment at source, Dr. Inventory Loss / Cr. Inventory at source location); (b) if carrier damage → DC Supervisor or Store Manager files carrier damage claim with photos and delivery receipt notation per W3.6a insurance claim process; (c) if unexplained shortage after investigation → destination writes off with approval per tier (Store Manager ≤ PHP 10,000, DC Manager ≤ PHP 50,000, Controller > PHP 50,000); system posts adjustment at destination (Dr. Inventory Loss / Cr. Inventory) | Receiving Clerk / DC Supervisor / Store Manager | Controller | 15–30 min

### W22a. Store-Level Outbound Transfer Fulfillment

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

### W22b. Store-to-DC Return (Excess / Damaged Inventory)

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
- Store-to-DC Return Order creation with reason codes (excess, damaged, discontinued, RTV consolidation) (W22b.2)
- Supply Planner approval workflow with DC capacity/demand check (W22b.3)
- In-transit inventory tracking for reverse movement (W22b.5)
- Disposition routing based on return reason code with integration to W6.8a (damage), W13.9a (clearance), W3.6b (RTV) (W22b.7)
- Store-to-DC return analytics: frequency, reason, category, store (W22b.9)
- Integration with W4 (reverse logistics on delivery truck), W6 (damage reporting), W13 (clearance), W22 (standard transfers), W29 (recall), W68 (discontinuation)

### Staffing Implication
- **Store Manager**: ~0.5–1 return initiations/month × 25 min = ~15 min/month. Absorbed.
- **Supply Planner**: 5 min review per return × ~200/month = ~17 hours/month across all stores. Absorbed by existing planner team.
- **DC Receiving**: adds ~15–30 min per return shipment to existing receiving workload. With ~100–200/month ÷ 5 DCs = ~20–40/DC/month. Manageable.

### Staffing Implication (W22 overall)
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
- Quarterly consignment vendor statement reconciliation: Cost Accountant generates consignment reconciliation report per vendor — compares BuildRight's recorded consignment sell-through (units sold × consignment cost) to vendor's statement; reconciles on-hand quantities (system record vs. vendor record of goods shipped minus goods sold); investigates discrepancies (unrecorded sell-through, unreported returns, missing receipts, timing gaps); reconciling items documented and resolved within 15 business days; unreconciled differences > PHP 50,000 escalated to Controller; results feed into vendor scorecard (W44) (W23)

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
- Customer master creation with credit limit, payment terms, entity assignment, and VAT treatment classification (W24.6)
- VAT treatment per customer account: AR Clerk classifies account as Standard (12% VAT), VAT-Exempt (government agencies with BIR ruling, PEZA-registered entities), or Zero-Rated (export sales) during account setup based on supporting documents (BIR ruling, PEZA certificate, government purchase order, diplomatic note); system stores VAT treatment in customer master; applied automatically at POS (W5b.4c) and AR invoicing (W8) (W24.6)
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
- Store disbursement request for mid-range expenses (PHP 5,000–50,000): for expenses too large for petty cash but not suited to formal PO (emergency equipment repair, small equipment purchase, local contractor services, urgent supplies) — Store Manager or Department Supervisor submits disbursement request in system with business justification, vendor quotation (if available), and cost center; approval per tier (Store Manager approves up to PHP 20,000; Regional Manager approves PHP 20,001–50,000); upon approval, Custodian pays vendor and obtains receipt; AP Clerk posts expense with receipt attachment to GL; disbursements tracked per store per month in expense summary report; distinct from petty cash (W25.1–4) in requiring formal system request and approval before payment, and from PO-based purchasing (W2) in bypassing the PO/GR/invoice cycle for immediacy (W25)

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
- Gift card breakage accounting (PFRS 15 / PAS 20): buildRight recognizes gift card breakage (unredeemed expired balances) using the redemption-rate-based method — (a) system tracks historical redemption rates by gift card cohort (vintage analysis); estimated unredeemed portion = 1 − historical 24-month redemption rate (currently ~15–25%); (b) breakage is recognized proportionally over the expected redemption period as redemption occurs — for every redemption, system recognizes a proportional share of expected breakage (Dr. Deferred Revenue — Gift Cards / Cr. Breakage Income); (c) at 24-month expiry, any remaining unredeemed balance is recognized in full as breakage income; (d) Cost Accountant reviews breakage estimate quarterly against actual redemption experience and adjusts the recognition rate if actual redemption deviates by > 5% from estimate; (e) this method is distinct from the simpler expiry-based lump-sum approach and provides more accurate PFRS 15 revenue recognition over the gift card lifecycle
- Cross-channel gift card redemption: gift cards can be redeemed both online (ecommerce) and in-store; system validates card balance in real-time via ERP integration regardless of channel; gift card liability is maintained centrally on Depot Inc.'s balance sheet; when redeemed online for a BOPIS or home delivery order, Digital Commerce Inc. fulfills the order but Depot Inc. reduces the gift card liability and recognizes revenue per standard IC model; IC settlement between Digital Commerce Inc. and Depot Inc. processed monthly via W14; customer experience is seamless — same card works in-store and online

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
| 15 | Annual mock recall exercise: VP Merchandising and Internal Audit conduct a simulated recall on 2–3 randomly selected lot-tracked items; test forward and backward traceability (W29.3), POS blocking speed (W29.5), ecommerce removal (W29.6), and customer notification completeness; measure time from recall activation to all stores confirming quarantine; results documented and shared with Category Managers and Buyers; vendor recall clause compliance verified — all vendor contracts (W2c, W36) must include recall cooperation obligations (response SLA, cost responsibility, product replacement or credit terms) | VP Merchandising + Internal Audit | COO | 4 hours/year |

### System Touchpoints
- Lot/batch/serial number traceability: forward (sold-to) and backward (received-from) tracing (W29.3)
- POS blocking flag for recalled items with cashier alert (W29.5)
- Ecommerce automatic removal and refund processing (W29.6)
- Recall-specific returns processing without receipt requirement (W29.9)
- Recall tracking dashboard: quantities pulled, returned by customers, pending per location (W29.10–11)
- Regulatory reporting data generation: system produces traceability reports in DTI/BPS-prescribed format including lot/batch numbers, affected SKU list, quantities sold by location, customer contact list (from loyalty/B2B accounts), quantities remaining in inventory, disposition actions taken, and timeline of recall execution; reports exportable as PDF for submission to DTI/BPS, FDA (for chemical products), and vendor (W29.13) - RTV or destruction documentation (W29.12)

### Staffing Implication
- No dedicated headcount for recalls (2–5 events/year). When a recall occurs, it is managed by existing roles as a cross-functional effort led by VP Merchandising.
- Call center (30 people) absorbs inbound customer inquiries during active recalls.

---

## W5g. Offline POS Recovery & Reconciliation

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
- Offline transaction queuing and encrypted local storage (W5g.1)
- Automated upload and inventory conflict detection on reconnection (W5g.2–3)
- Offline-to-online GL and inventory reconciliation (W5g.5–6)
- Loyalty points reconciliation for transactions processed offline (W5g.5)
- Stale price detection for extended outages (W5g.8)

### Business Continuity — Operational Fallback

During a prolonged system outage (back-office ERP down beyond RTO of 4 hours per NFR-013), store operations continue in degraded mode:

- **POS**: continues selling offline per W5g (up to 8+ hours with local cache)
- **Goods receiving (W3/W18)**: stores suspend goods receipt processing until system restored; Receiving Clerk captures delivery details manually (DR number, vendor, item, quantity) on paper or offline spreadsheet for batch entry upon recovery
- **Ecommerce**: Digital Commerce Inc. platform displays maintenance notification; new orders suspended; in-progress orders held for fulfillment upon recovery
- **Loyalty**: points earning tracked offline at POS and reconciled upon reconnection; points redemption suspended during outage (cashier cannot verify balance)
- **AP / Treasury**: payment runs delayed until system restored; AP Clerk communicates with vendors if payment deadlines are at risk
- **Incident declaration**: IT Helpdesk declares DR event per incident response plan; CIO notified; Store Ops Director communicates to Regional Managers who notify Store Managers; estimated recovery time communicated within 30 minutes of declaration
- **Recovery**: upon system restoration, all offline transactions upload per W5g; manual receiving entries batch-posted; ecommerce order processing resumes; loyalty reconciliation runs automatically

### Staffing Implication
- No incremental headcount. Outage recovery is a Store Manager responsibility with IT support.
- Estimated 2–4 recoveries per store per year × 30 min each = ~1–2 hours/year per store.

---

## W30. Daily Treasury & Cash Position Management

| Field | Detail |
|---|---|
| **Trigger** | Daily treasury operations cycle |
| **Frequency** | Daily |
| **Volume** | 200 stores + 5 DCs + HQ cash positions; ~210 bank accounts total across 4 banks (BDO, BPI, Metrobank, Chinabank) and 5 entities: ~200 store deposit accounts (1 per store for daily cash collection), 5 DC operating accounts, 5 entity main operating accounts, 5 USD import accounts, and additional payroll, savings, and investment accounts per entity |
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
| 10a | **FX hedging policy**: CFO defines and documents the company's FX risk management strategy — (a) natural hedging: match USD payables (import POs per W2b) with USD receivables where possible; maintain USD bank account balances sufficient to cover near-term import payment obligations (typically 30–60 day forward cover); (b) forward contracts: for large committed import orders (> PHP 5M equivalent), Treasury Analyst may purchase USD forward contracts through the banking relationship to lock in exchange rate at PO creation date; forward contract details (notional amount, forward rate, maturity date, counterparty bank) recorded in system; (c) policy limits: unhedged FX exposure limited to 30-day rolling average of import payments; CFO approves all forward contracts; no speculative FX positions permitted (hedging only for committed import payables); (d) monthly: Treasury Analyst prepares FX exposure report — total USD payables outstanding, USD bank balances, forward contracts in place, net unhedged exposure, unrealized FX gain/loss on open forward contracts; included in weekly cash flow forecast (W30 step 8); (e) at forward contract maturity: Treasury settles with bank; system posts settlement with realized FX gain/loss vs. forward rate | Treasury Analyst / CFO | CFO | Monthly review + as needed for forward contracts |

### System Touchpoints
- Multi-bank statement import (BDO, BPI, Metrobank, Chinabank) via file formats or API (W30.2)
- Daily cash position dashboard per entity and consolidated (W30.3)
- Store cash deposit auto-matching to Z-report amounts (W30.4)
- Cash-in-transit confirmation: system records armored car pickup or bank deposit confirmation per store; auto-matches deposit amount to Z-report cash total; flags unmatched or short deposits for investigation (W30.4, cross-reference W5c.5a)
- Cash sweep scheduling and execution (W30.7)
- Rolling cash flow forecast (W30.8)
- Bank reconciliation per entity (W30.9; also linked to W9a step 9)
- Multi-currency (PHP/USD) account management with FX conversion tracking (W30.10)
- Petty cash reconciliation link: store-level petty cash replenishments (W25) are included in the daily cash position report (W30 step 3) as pending outflows; Treasury Analyst sees replenishment requests in the weekly cash flow forecast (W30 step 8); replenishment payments confirmed via bank transfer are auto-matched to store deposit accounts during bank reconciliation (W30 step 9); monthly petty cash replenishment totals per store are visible on the Treasury dashboard for monitoring unusual patterns (W30)
- Store-level cash position tracking: system aggregates per-store daily cash deposits (W5c), petty cash replenishments (W25), and store disbursement requests (W25 store disbursement) into a consolidated store cash movement report; Treasury Analyst reviews as part of daily cycle to detect unusual cash patterns at individual stores (W30)
- Bank account lifecycle management: Treasury Analyst maintains bank account register across all entities (~210 accounts: 200 store deposit accounts, 5 DC operating accounts, 5 entity main operating accounts, 5 USD import accounts, and additional payroll, savings, and investment accounts); new account opening triggered by new store (W16), new entity setup, or new banking relationship — Treasury Analyst submits account opening request to bank with Board Resolution (per entity), authorized signatory list, and business registration documents; signatory management: system tracks authorized signatories per account with signatory tier (single signatory, dual signatory, any-two-of-three); when a signatory changes role or separates (W43), Treasury Analyst updates bank signatory list within 10 business days — system alerts on signatory staleness (no update in > 12 months); account closure triggered by store closure (W45), account consolidation, or bank relationship termination — Treasury Analyst confirms zero balance, obtains bank closure confirmation, and deactivates account in system; system logs all account openings, signatory changes, and closures with full audit trail (W30)

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
| 8 | Quarterly: Demand Planner recalibrates forecast model parameters (alpha, beta, gamma for exponential smoothing); updates seasonal indices based on latest year of data; reviews and updates safety stock parameters per SKU-location based on forecast error and demand variability changes (feeds into W2a.1 ROP/safety stock calculation); reviews ROP parameter governance: (a) lead time accuracy per vendor — compares actual delivery lead time vs. system lead time and updates for vendors with > 20% variance, flagging chronic late vendors for W44 review; (b) demand averaging period appropriateness by SKU volatility class; (c) service level targets by ABC class (e.g., A-items: 98%, B-items: 95%, C-items: 90% or as configured); (d) order multiple / MOQ accuracy per vendor-SKU; cross-references vendor lead time variance to vendor scorecard (W44) | Demand Planner | Supply Planning Manager | 4–6 hours/quarter |

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
- ROP parameter governance and accuracy reporting: quarterly parameter review as part of W31.8 covering (a) lead time variance report per vendor (actual vs. system lead time); (b) service level target monitoring by ABC class; (c) demand averaging period appropriateness by volatility class; (d) order multiple / MOQ accuracy; (e) ROP exception report: SKUs where ROP parameters have not been reviewed in > 6 months; parameter accuracy feeds into vendor scorecard (W44) for lead time performance tracking
- DC multi-dimensional capacity planning dashboard: system aggregates all competing demands on DC resources into a single view per DC — (a) **inbound receiving capacity**: scheduled receipts (W3c) vs. dock door availability vs. receiving crew capacity (labor hours); (b) **outbound pick/pack capacity**: store replenishment orders (W4) + home delivery orders (W19) + promotional pre-positioning (W57) + backorder fulfillment (W56) — total pick lines and labor hours required vs. available pick/pack crew; (c) **outbound dock capacity**: scheduled dispatches vs. dock door availability vs. loading crew capacity; (d) **storage capacity**: current bin utilization vs. incoming inventory from POs and transfers; dashboard shows 3-day forward view with capacity utilization percentage per dimension; Supply Planner and DC Supervisor review daily during morning planning meeting; if any dimension exceeds 90% utilization, system highlights in amber; if exceeds 100%, system highlights in red and suggests mitigation (defer non-critical replenishment waves, redirect home delivery to alternate DC, schedule overtime, or engage agency workers per W10); during peak periods (Christmas season, bi-monthly sale events), Supply Planning Manager reviews capacity dashboard weekly with DC Manager and VP Supply Chain to proactively adjust labor scheduling (W34) and carrier capacity (W52/W62b) (W31)

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
- Attendance exception handling: system detects clock-in/out anomalies — (a) **missed punch**: employee forgot to clock in or out; system generates missed punch alert; employee submits missed punch request via self-service portal (W51) within 24 hours with estimated in/out time; Department Supervisor approves or adjusts; system retroactively calculates hours; (b) **biometric reader failure**: if biometric device malfunctions, Store Manager records attendance manually in system with reason code; IT Helpdesk (W48) notified as P2 incident for device repair; manual records reconciled upon device restoration; (c) **late arrival / early departure**: system flags employees clocking in > 15 minutes after shift start or clocking out > 15 minutes before shift end; Store Manager reviews daily exception list; habitual lateness (> 3 occurrences/month) triggers HR counseling; (d) **unmatched punch**: employee clocks in at one terminal and out at another, or forgets to clock out and clocks in next day; system generates unmatched punch alert; employee submits correction via self-service; supervisor approves; system resolves unmatched pair; all attendance exceptions logged per employee with timestamp, type, resolution, and approver; monthly: HR Assistant generates attendance exception summary per store for Regional Manager review (W34)
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
| 14a | Store utility consumption report: system aggregates per-store utility expense (electricity, water, internet) from non-PO invoice data (W7c); benchmarks kWh per sqm per store per month; flags stores with utility consumption > 20% above peer average (same store format, same region) for investigation — potential causes include equipment malfunction (W47), HVAC inefficiency, or unauthorized usage; Store Manager receives monthly utility scorecard as part of Store Performance Scorecard (W67); Facilities Coordinator investigates flagged stores and recommends corrective action (equipment upgrade, behavioral changes) | System / Facilities Coordinator | Store Ops Director | Automated + 2 hours/month review |
| 14 | Management committee meeting: CFO presents consolidated results; Department Heads present functional KPIs | CFO / Dept. Heads | CEO | Monthly (by day 10) |

### Quarterly

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 15 | Board pack preparation: consolidated financials, management discussion & analysis, KPI scorecard, risk register update | Controller + CFO | CEO | Quarterly |
| 16 | Vendor performance scorecard review (W44) | Buyer | VP Merchandising | Quarterly |
| 17 | Budget revision (if material changes warranted) (W26 step 13) | Controller | CFO | Quarterly |
| 18 | **Document retention compliance review**: Controller verifies that all document types (invoices, receipts, delivery receipts, import docs, capex records) meet 7-year BIR retention requirements; confirms expired documents are archived and accessible; flags any gaps in document attachment compliance | Controller | CFO | Quarterly |
| 19 | **Credit note / debit note aging review**: Chief Accountant presents summary of unapplied AP and AR credit memos > 60 days; Controller reviews resolution status; material unresolved items escalated to CFO | Chief Accountant / Controller | CFO | Quarterly |

### Ad-Hoc

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 20 | Department Heads request ad-hoc reports from BI Analyst or self-service via report builder | Dept. Heads / BI Analyst | — | As needed (~20/month) |
| 21 | BI Analyst creates custom analyses: product affinity, customer segmentation, promotional lift analysis, geographic trends | BI Analyst | Requestor | As needed |

### System Touchpoints
- Scheduled report auto-generation and distribution (email, portal, mobile) (W35.1, 4, 8–13)
- Executive dashboard with real-time KPIs (W35.2)
- Store P&L module (W35.10)
- Self-service report builder / ad-hoc query tool (W35.18)
- Mobile dashboard for executives (W35.2)
- Integration with all ERP modules (financials, inventory, POS, procurement, HR, ecommerce) for data aggregation
- Store P&L occupancy cost allocation: store rent is a direct charge per location based on individual lease agreements with Property Mgmt Inc. (not allocated from a pool); DC warehousing and distribution costs (IC payment to Logistics Inc. per W14) are allocated to stores monthly based on a configurable allocation key (recommended: proportional to replenishment order value or volume per store); utility costs are direct charges per store (each location has its own meter/account); corporate overhead from Holdings Inc. (management fees per W14) is shown as a separate line below store EBITDA, not embedded in store-level P&L; system auto-generates store P&L with all cost lines from configurable allocation rules
- Store-level budget variance tracking: annual budget (W26) is phased monthly per store with revenue, COGS, labor, occupancy, and shrinkage targets; system generates monthly store budget vs. actual report with variance flags (revenue > ±5%, gross margin > ±2%, operating expense > +10%); Regional Manager reviews store-level budget variance with Store Manager during monthly store visit; significant variances escalated to VP Store Operations; store-level budget accountability is a standing agenda item in monthly management committee meeting (W35.14)

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
| 7a | **Vendor bank account change control**: if an existing vendor requests a change to their bank account details (new account number, new bank), the change requires a mandatory out-of-band verification before system update — (a) AP Clerk receives vendor bank change request (email, letter, or portal submission); (b) AP Clerk contacts vendor using the **known** phone number or contact person from vendor master (NOT the contact information in the change request itself, to prevent authorized push payment fraud); (c) AP Clerk verbally confirms the bank change with an authorized vendor representative; (d) AP Supervisor approves the bank detail change in system with verification notes (who confirmed, date, phone number used); (e) system requires dual approval (AP Clerk entry + AP Supervisor approval) for all bank detail changes; (f) system logs change with old bank details, new bank details, verifying AP Clerk ID, approving AP Supervisor ID, verification method, and timestamp; (g) system temporarily blocks payment to the vendor for 48 hours after bank detail change as a cooling-off period; (h) first payment to new bank account is flagged for Treasury Analyst confirmation of receipt before subsequent payments are auto-processed | AP Clerk / AP Supervisor | AP Supervisor | 30 min/change |
| 7b | **Vendor master data change log**: all changes to vendor master data (bank details, payment terms, address, contact information, tax classification) are logged with full audit trail — old value, new value, changed by, approved by, date, reason; changes to bank details and payment terms require AP Supervisor approval; changes to tax classification require Finance Manager approval; monthly: AP Supervisor reviews vendor master change log as part of AP controls review (cross-reference CTL-42 in Internal Controls Matrix) | System / AP Clerk | AP Supervisor | Automated + 30 min/month review |
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
- Vendor lead time master data lifecycle: initial lead time entered during vendor onboarding per vendor-SKU (W36 step 8); ongoing maintenance — Buyer updates lead times when vendor notifies of changes (new warehouse, route change, seasonal factors); system auto-suggests lead time updates based on actual delivery performance (comparing actual GR date vs. PO promised date) and presents suggestions to Buyer for review and confirmation; quarterly review per W31 step 8 confirms or adjusts stale lead times; system tracks all lead time changes with full audit trail (old value, new value, reason, date, Buyer ID); lead time variance metric feeds vendor scorecard (W44) (W36.6, W36.8)
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
- Confirmed theft / inventory write-off process: documentation with supporting evidence, police report filing for theft, tiered approval per loss value, GL write-off posting, insurance claim integration, quarterly shrinkage reporting integration (W37.11–16)
- Exception threshold configuration and tuning (W37.9)
- CCTV integration specification: (a) system captures POS transaction timestamp and terminal ID; (b) POS integration layer sends transaction event to CCTV system via API or middleware; (c) CCTV system bookmarks associated video clip (configurable: ± 2 minutes around transaction event); (d) LPO retrieves correlated video from LP investigation dashboard by clicking transaction exception — system deep-links to CCTV playback at the transaction timestamp; (e) CCTV recording retention: minimum 30 days online storage, 90 days archived; (f) CCTV access restricted to LPO, Store Manager, Regional Manager, and Internal Audit via role-based access control; (g) for new store openings (W16), IT configures POS-to-CCTV integration as part of go-live readiness checklist (W16.9a); (h) system does not store video — only stores timestamp reference and CCTV clip ID for retrieval from the CCTV system's own storage
- Loyalty program fraud detection: system monitors for loyalty abuse patterns in addition to POS transaction exceptions; detection rules include: (a) cashier scanning the same loyalty card across > 20% of their transactions (self-scanning or family/friend farming), (b) loyalty points earned on subsequently voided transactions (points earned but not reversed), (c) unusually high points earning on single transaction (points-to-revenue ratio exceeding 3× normal), (d) multiple loyalty accounts with > 85% match on name, phone, or address (farming multiple accounts), (e) redemption velocity spike on dormant accounts; flagged patterns appear on LPO daily exception dashboard alongside POS exceptions; LPO investigates and escalates to Loyalty Manager for account action (W17 manual points adjustment); confirmed fraud cases result in account suspension per W17 manual adjustment approval tiers
- Gift card / store credit fraud detection: system monitors gift card and store credit transactions for fraud patterns: (a) multiple gift card balance inquiries from same terminal within short time window (potential brute-force balance checking), (b) gift card redemption at a different store within 24 hours of activation (potential barcode photocopying or stolen card), (c) return-to-store-credit followed by immediate cash-out attempt (return fraud), (d) employee-associated gift card transactions (employee purchasing or reloading their own gift card with subsequent return manipulation), (e) high-value gift card purchases paid in cash (potential money laundering); flagged patterns appear on LPO daily exception dashboard; LPO investigates and escalates to Store Manager for card suspension and customer verification; confirmed fraud results in gift card deactivation and loss reporting; monthly: LPO includes gift card fraud metrics in shrinkage report (W37.7); any manual gift card balance adjustment requires dual approval (Store Manager + AP Supervisor) with full audit trail

### Staffing Implication
- **2–3 Loss Prevention Officers** (reporting to Internal Audit or a dedicated LP function): Daily review (1–2 hours) + case investigation (5–10 active cases at any time) + monthly shrinkage reporting + quarterly reviews. This is a specialized role that may not exist in the current org chart. Recommend adding 2 LPOs to cover 200 stores (each covering ~70 stores, rotating through physical store visits).
- **Store Managers**: Review their store's exception report daily (~15 min). Absorbed into opening routine.
- **Internal Audit**: Incorporates LP findings into quarterly audit cycle. No incremental headcount.

### Confirmed Theft / Inventory Write-Off Process

When an LPO investigation confirms theft or irrecoverable loss:

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| W37.11 | LPO documents confirmed loss: investigation findings, supporting evidence (CCTV footage, transaction records, witness statements); for theft, files police report with local PNP station | LPO | Internal Audit | 1 hour/case |
| W37.12 | LPO submits inventory write-off request: SKU, quantity, value at WAC, root cause classification (internal theft, external shoplifting, vendor fraud, unexplained loss) | LPO | Internal Audit | 15 min/case |
| W37.13 | Approval per tier: (a) total loss ≤ PHP 10,000: Store Manager, (b) PHP 10,001–50,000: Regional Manager + Internal Audit, (c) PHP 50,001–500,000: Controller + Internal Audit, (d) > PHP 500,000: CFO + CEO | Approver | Approver | 15 min/case |
| W37.14 | System posts write-off: Dr. Inventory Loss / Cr. Inventory; removes items from inventory register; records loss in shrinkage tracking for store KPI | System | — | Automated |
| W37.15 | If loss is insured (e.g., large robbery, transit theft): LPO files insurance claim per W3.6a insurance claim process; Finance posts recovery upon settlement | LPO / Finance | Controller | Per W3.6a |
| W37.16 | Quarterly: LPO includes confirmed theft and write-off totals in shrinkage report (W37.7); feeds into store KPI scoring and loss prevention action plans | LPO | Internal Audit | Part of existing reporting |

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
| 6a | **Trade/corporate account customers**: if customer holds an active trade or corporate account (W24), deposit requirement is waived for orders within the customer's available credit limit; system checks credit limit at order creation — if credit available, Sales Associate or CSR selects "Charge to Account" and system posts order value to customer's AR account (W8) upon delivery (no deposit liability); if order exceeds available credit, system prompts for partial deposit covering the excess; for special orders > PHP 50,000 on account, system routes for AR Supervisor approval per W24 tiered matrix | Sales Associate / CSR | AR Supervisor | 2 min |
| 7 | System creates Sales Order linked to non-stock SKU with customer deposit recorded; reservation created against incoming PO | System | — | Automated |
| 8 | Buyer creates Special Order PO (links PO to Sales Order); routes for approval per standard tiered matrix (W2) | Buyer | Category Manager | Per W2 |
| 9 | Buyer tracks PO; follows up with vendor on delivery schedule | Buyer | Buyer | Per W2 |
| 10 | Goods received at store or DC (per W3 or W18); system matches GR to both PO and linked Sales Order | Receiving Clerk | Dept. Supervisor | Per W3/W18 |
| 11 | System alerts CSR that special order has arrived; CSR contacts customer for pickup or arranges delivery | System / CSR | Store Manager | Automated + 5 min |
| 12 | Customer picks up item (or receives delivery); pays remaining balance; system recognizes revenue (Dr. Customer Deposits / Cr. Revenue) and COGS (Dr. COGS / Cr. Inventory) at delivery; Sales Order closed | Cashier / CSR | — | 5 min |
| 13 | If customer cancels before PO is placed: CSR cancels Sales Order; deposit refunded; no PO created | CSR | Store Manager | 5 min |
| 14 | If customer cancels after PO is placed but before shipment: Buyer negotiates with vendor (restocking fee, return); Finance processes partial refund less any costs | Buyer + Finance | Category Manager | 30 min |
| 15 | Unclaimed deposit management: system tracks age of customer deposits linked to completed special orders (goods received but not picked up); after 30 days with no customer response post-delivery notification, system sends reminder notification (SMS/email); after 90 days with no response, system flags deposit for review; Store Manager or Finance approves recognition of abandoned deposit as other income (Dr. Customer Deposits Payable / Cr. Other Income); goods dispositioned per standard clearance (W13.9a), RTV (W3.6a), or return to shelf | System / Store Manager / Finance | Controller | Automated + 5 min/review |
| 16 | **Customer deposit refund (before goods receipt)**: if customer requests cancellation and refund before goods are received from vendor — (a) CSR processes deposit refund in system with reason code (customer cancellation, vendor cannot deliver, project cancelled); (b) system cancels linked Sales Order and triggers Buyer to cancel or reduce the linked PO per W2a PO cancellation process (if PO not yet shipped by vendor); (c) refund issued to original payment method: if deposit paid by cash, CSR disburses from cash drawer with Store Manager authorization; if paid by card/e-wallet, system processes electronic refund (Dr. Customer Deposits Payable / Cr. Cash); if paid by trade account credit, system applies deposit back to customer's AR account; (d) system logs refund with customer ID, original deposit transaction, refund amount, refund method, CSR ID, authorizing manager ID, and reason code; (e) BIR-compliant documentation: system generates official receipt for the refund transaction with all required BIR fields (TIN, registered invoice number, description "Refund of customer deposit — Sales Order #[number]"); refund receipts retained per 7-year BIR retention policy | CSR / Store Manager | Controller | 10 min/refund |

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
- Non-stock SKU archival and cleanup: over time, the item master accumulates non-stock/special-order SKUs (type = "Special Order / Non-Stock" per W38.3a) from one-time customer orders; to prevent item master bloat — (a) monthly: Merchandise Planner generates non-stock SKU aging report listing all non-stock SKUs with no sales activity in the past 12 months; (b) Merchandise Planner reviews each stale non-stock SKU and sets status to "Non-Stock — Archived" — item remains searchable in system for transaction history but is hidden from new Sales Order creation and Sales Associate lookup; (c) archived non-stock SKUs excluded from item count in reporting and system performance metrics; (d) if a customer subsequently requests the same item, Merchandise Planner reactivates the archived SKU (updates status to active) rather than creating a duplicate; system checks for archived SKUs matching the item description before allowing new non-stock SKU creation; (e) annually: Merchandise Planner reviews all archived non-stock SKUs older than 3 years with zero transaction history and proposes permanent deletion per BIR 7-year retention compliance (items with any transaction history retained for full 7 years regardless of archival status)
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

### Quantity Break Pricing Setup & Maintenance

| Field | Detail |
|---|---|
| **Trigger** | New product setup, category review, or competitive response |
| **Frequency** | Ongoing; ~50–100 quantity break rules active at any time |
| **Volume** | Primarily bulk-building categories: cement, lumber, nails, screws, paint, plumbing fittings |
| **Owner** | Pricing Analyst |
| **Participants** | Pricing Analyst, Category Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 15 | Pricing Analyst defines quantity break rules per SKU or category in system: threshold quantity, discount % or fixed price per tier (e.g., cement: 1–9 bags at SRP, 10–99 bags at 5% off, 100+ bags at 8% off); rules are date-effective with start/end dates | Pricing Analyst | Category Manager | 5 min/rule |
| 16 | Category Manager approves quantity break rules; VP Merchandising approves if aggregate margin impact exceeds threshold | Category Manager / VP | VP Merchandising | 15 min/batch |
| 17 | System stores quantity break rules linked to item master; POS automatically applies the correct tier when scanned quantity meets or exceeds threshold — no cashier intervention required | System | — | Automated |
| 18 | Discount stacking rules: if a promotional price (W13) is lower than the quantity break price, system applies the promo price (customer-friendly) and does not stack discounts; if quantity break price is lower, it applies; trade/corporate account pricing (W5b.4c) and quantity break pricing do not stack — the lower of the two applies | System | — | Automated |
| 18a | **Loyalty points on discounted transactions**: loyalty points (W17) are earned on the final amount paid by the customer (after all discounts — promotional, quantity break, trade account, price match) but before VAT; this means quantity break discounts reduce the points earned proportionally; PFRS 15 deferred revenue allocation (W17.4) is calculated on the net revenue after all discounts | System | — | Automated |
| 19 | Monthly: Pricing Analyst reviews quantity break utilization report: frequency of tier triggers by SKU, margin impact, average quantity per transaction for items with quantity breaks, and whether thresholds are driving incremental volume | Pricing Analyst | Category Manager | 1 hour/month |

### System Touchpoints
- Quantity break rule engine: configurable per SKU or category with multiple tiers, date-effective, threshold quantity, and discount method (% off SRP or fixed price) (W40.15)
- Automatic POS application when scanned quantity meets threshold — no cashier action needed (W40.17)
- Discount stacking rules: quantity breaks do not stack with promotional pricing or trade/corporate pricing — lower price wins (W40.18)
- Loyalty points on quantity break transactions: points earned on net discounted amount (after all discounts, before VAT); PFRS 15 deferred revenue allocation calculated on net revenue (W40.18a, W17.4)
- Quantity break utilization reporting: tier trigger frequency, margin impact, incremental volume analysis (W40.19)
- Integration with W5b.6 (system applies quantity breaks during total calculation) and W40.5 (approval workflow)

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

### Ecommerce Order Issue Resolution

For ecommerce-specific order issues (W11 BOPIS, W19 Home Delivery) — the primary workload for the 30-person call center team (~2,100–4,300 issue tickets/month at 5–10% issue rate on 42,900 orders/month):

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| E1 | Customer contacts call center (phone, chat, email) or submits issue via self-service portal/online form: order not received, wrong item received, item damaged in transit, wants to change delivery address, wants to cancel order, didn't receive BOPIS pickup notification | Customer / CSR | CS Manager | 3 min |
| E2 | System creates issue ticket linked to original order number; displays full order lifecycle (placement, payment, fulfillment status, carrier tracking) | CSR / System | CS Manager | 2 min |
| E3 | CSR resolves per issue type: (a) cancel-and-refund: system cancels unfulfilled order, initiates refund to original payment method (Dr. Revenue / Cr. Cash); (b) redelivery: system reschedules carrier pickup via 3PL integration (W19); (c) wrong/damaged item: initiates W12b return process and arranges replacement; (d) address change: updates delivery address if order not yet shipped; (e) BOPIS pickup issue: confirms correct store, resends notification, or extends hold period | CSR | CS Manager | 5–15 min |
| E4 | For partial refunds (damaged but usable item): CSR issues partial refund with CS Manager approval (Dr. Revenue / Cr. Cash); system logs partial refund with reason code and photo evidence if available | CSR / CS Manager | CS Manager | 10 min |
| E5 | System tracks issue SLA: target resolution within 24 hours for delivery issues, 48 hours for damaged/wrong items; escalated to CS Manager if SLA breached | System | CS Manager | Automated |
| E6 | Automated customer notifications at each status change: issue acknowledged, resolution proposed, refund processed, redelivery scheduled | System | — | Automated |

### System Touchpoints
- Multi-channel complaint ticket creation (in-store, phone, email, chat, web) (W41.1–2)
- Ticket categorization with auto-priority assignment (W41.2)
- Tiered escalation workflow with SLA timers (W41.5, W41.10)
- Resolution code tracking and financial action triggers (refund, voucher) (W41.4, W41.8)
- Customer satisfaction capture at resolution (W41.4)
- Data Subject Access Request (DSAR) handling per RA 10173: system logs DSAR requests (access, correction, deletion, consent withdrawal) with 72-hour acknowledgment and 30-day resolution tracking; supports data anonymization for deactivated accounts after retention period; customer consent preferences viewable and editable via self-service portal (W41.2, W17.2)
- Complaint analytics dashboard: volume, category, store, resolution rate, SLA compliance (W41.11)
- Root cause analysis reporting (W41.12–13)
- Ecommerce order issue resolution: ticket creation linked to original order number with full order lifecycle visibility (placement, payment, fulfillment, carrier tracking); issue type routing (cancel-and-refund, redelivery, partial refund, address change, BOPIS pickup issue); financial adjustment posting (refund, partial refund) with GL entries; carrier rescheduling via 3PL integration (W19); automated customer notification at each status change; SLA tracking with escalation (24-hour delivery issues, 48-hour damaged/wrong items) (W41.E1–E6)

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

> **Feasibility note**: Counting 35,000 SKUs per store with 35 staff in 2 days is infeasible for a full wall-to-wall count. BuildRight addresses this with a **tiered counting strategy**: (a) **A/B items** (~10,500 SKUs, 95% of inventory value) receive full physical count during the annual window; (b) **C items** (~24,500 SKUs) are validated by extrapolating from rolling cycle counts (W6) conducted throughout the year — the annual process confirms that cycle count accuracy for C-items meets the ≥ 97% threshold, rather than recounting every C-item. This reduces the per-store counting burden to ~10,500 SKUs ÷ 35 staff ÷ 2 days = ~150 SKUs/person/day, achievable at ~3 min/SKU including travel between locations. DCs, with higher item density and forklift-access racking, allocate 3–5 days for a full count of all SKUs.
>
> **C-item extrapolation methodology**: C-item inventory accuracy is validated using a statistical sampling approach — (a) throughout the year, W6 cycle counts cover all C-item SKUs at least once per quarter (per the quarterly cycle in W6); (b) each C-item's cycle count accuracy (physical vs. system quantity) is recorded per count event; (c) at year-end, Cost Accountant computes the aggregate C-item accuracy rate = (total C-item SKU-locations where physical matched system within tolerance) ÷ (total C-item SKU-locations counted during the year); (d) if aggregate accuracy ≥ 97%, C-items are considered validated and no additional count is required at year-end; (e) if aggregate accuracy < 97%, Cost Accountant identifies the worst-performing C-item categories (by variance rate) and adds them to the annual count scope; (f) sample size for interim confidence: to achieve 95% confidence that the true accuracy rate is within ±1% of the observed rate, a minimum of ~500 C-item SKU-locations must be cycle-counted per quarter per store (approximately 2% of C-item SKU-locations, achievable within W6 daily count volume of ~700 SKUs/day); (g) this methodology is reviewed and approved by Internal Audit annually as part of the W42 physical inventory observation; (h) **below-threshold contingency**: if aggregate C-item accuracy falls below 97%, Cost Accountant quantifies the gap and identifies worst-performing C-item categories by variance rate; additional items added to the annual count scope in priority order (highest-variance categories counted first); if additional scope threatens the 2-day count window, Cost Accountant escalates to Controller with a proposed extended count schedule (up to 5 days with staggered zone freezing per W42 system freeze mitigation); Controller approves or denies extension; if extension denied, Cost Accountant counts the highest-risk C-items within the standard window and accepts a qualified inventory opinion for the remaining C-items — Controller discloses the qualification in the year-end close package (W9b); Internal Audit documents the below-threshold outcome and includes it in the W42 observation report.

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
| 10 | Payroll Officer computes final pay per W10 step 12: pro-rated salary for final pay period, pro-rated 13th month pay (1/12 of annual basic salary × months worked ÷ 12), converted unused leave credits (VL to cash per company policy), less outstanding loans/advances and clearance deductions; final pay computation varies by separation type — resignation: pro-rated salary + 13th month + VL conversion; termination for cause: pro-rated salary + 13th month (VL conversion per company discretion); retirement: pro-rated salary + 13th month + VL conversion + retirement pay per Labor Code or company plan (whichever is higher); end of contract: pro-rated salary + 13th month + VL conversion + separation pay if applicable per DOLE; system auto-calculates final pay based on separation type classification from W43.2 with Payroll Officer review and validation | Payroll Officer | Payroll Manager | Per W10 |
| 11 | System generates final pay as separate payroll run or adjustment; final payslip issued (W10 step 13) | System | — | Automated |
| 12 | System updates employee status to "Separated"; deactivates payroll processing; retains record for regulatory retention (7 years) | System | — | Automated |
| 13 | System generates COE (Certificate of Employment) on request: dates of employment, position, compensation range (optional) | System / HR Assistant | HR Head | 5 min/request |
| 14 | HR Head includes separation data in monthly turnover report: rate by department, store, and separation type; exit interview themes | HR Head | CHRO | 1 hour/month |
| 15 | Cross-entity employee transfer (between legal entities, e.g., Depot Inc. → Logistics Inc.): HR Assistant initiates transfer with effective date, destination entity, and new position; system processes as simultaneous separation from source entity and onboarding in destination entity with continuity of service — accumulated leave credits, 13th month pay pro-ration, and seniority carry forward; system deactivates employee in source entity payroll, creates employee record in destination entity with transferred balances, reassigns SSS/PhilHealth/Pag-IBIG to new entity's remittance, and switches BIR withholding tax to new entity's TIN registration; final pay computed at source entity (pro-rated) and first pay at destination entity for the same period; no break in employment continuity | HR Assistant / Payroll Officer | HR Head | 30 min/transfer |

**Total cycle time**: 30 days (notice period) + 5 business days after last day for final pay release

### System Touchpoints
- Separation record creation with type classification (W43.2)
- Automated clearance form generation and routing (W43.4)
- Clearance status tracking per department (W43.5–9)
- System account deactivation trigger (W43.5)
- Final pay computation by separation type: system auto-calculates final pay based on separation type (resignation, termination, retirement, end of contract) including pro-rated salary, pro-rated 13th month pay per BIR rules (1/12 of basic salary × months worked), unused VL monetization, applicable separation/retirement pay per Labor Code, less outstanding loans and deductions; final tax withholding per BIR rules (different treatment for retirement pay vs. resignation); final statutory contribution period computed per SSS/PhilHealth/Pag-IBIG rules; Payroll Officer reviews system calculation before processing (W43.10)
- Employee status lifecycle: Active → On Notice → Separated (W43.12)
- Certificate of Employment generation (W43.13)
- Cross-entity employee transfer: simultaneous separation and onboarding across legal entities with continuity of service; automatic payroll entity switch with transferred leave balances, 13th month pro-ration, and statutory reassignment; SSS/PhilHealth/Pag-IBIG reassigned to new entity; BIR withholding tax switched to new entity's TIN; GL postings to both entity payrolls for the transfer period (W43.15)
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
| 9 | **Corrective action execution — Warning**: Buyer communicates performance gaps to vendor in writing (email or letter) with specific metrics from scorecard; establishes 30-day improvement period with clear targets (e.g., on-time delivery must improve from 75% to 90%); Buyer monitors PO performance during improvement period via weekly scorecard snapshot | Buyer | Category Manager | 30 min/vendor |
| 10 | **Corrective action execution — Probation**: if no improvement after Warning, Buyer initiates probation — (a) Category Manager sends formal probation notice to vendor with 90-day review period and specific improvement requirements; (b) system changes vendor master status to "Probation"; (c) system blocks creation of new POs for this vendor (existing committed POs unaffected); (d) Buyer identifies alternative vendor for affected SKUs per W36; (e) Buyer monitors vendor performance weekly during probation; (f) at 90-day mark: Buyer recommends to Category Manager either reinstatement (if targets met) or termination | Buyer / Category Manager | VP Merchandising | 1 hour/vendor (initial) + 30 min/week monitoring |
| 11 | **Corrective action execution — Termination**: VP Merchandising approves termination; (a) Category Manager sends formal termination notice to vendor per contract terms (typically 30–60 day notice); (b) Buyer reviews all open POs — decides per PO: cancel, allow to complete, or expedite; (c) AP Supervisor reviews outstanding invoices and credit memos — resolves all financial obligations; (d) system changes vendor master status to "Inactive"; (e) system blocks all transactions (POs, GRs, invoices); (f) Merchandise Planner reassigns affected SKUs to alternative vendors per W36; (g) termination date, reason, and all supporting documentation recorded in vendor master audit trail | Category Manager / Buyer / AP Supervisor | VP Merchandising | 2–4 hours/vendor |
| 12 | **Corrective action execution — Reactivation**: if Buyer requests reactivation of a previously terminated vendor — (a) Buyer provides evidence of improved capability (new ownership, new processes, reference customers, corrected quality issues); (b) Category Manager reviews evidence and approves or denies; (c) if approved, vendor re-enters abbreviated onboarding per W36 (skip trial PO if recent performance history exists within 12 months); (d) system changes vendor master status back to "Active"; (e) full audit trail of termination and reactivation retained | Buyer / Category Manager | VP Merchandising | 1 hour/vendor |

| Tier | Trigger | Action | System Impact |
|---|---|---|---|
| **Warning** | Scorecard rating drops to C, or single significant incident (major quality failure, delivery causing stockout) | Buyer communicates performance gaps to vendor in writing with specific metrics; establishes 30-day improvement period with clear targets | Vendor master status remains Active; Buyer monitors PO performance during improvement period |
| **Probation** | No improvement after Warning, or scorecard rating drops to D | Vendor suspended from receiving new POs; existing committed POs are fulfilled; 90-day formal review period; Category Manager notifies vendor in writing of probation status and improvement requirements | Vendor master status changed to Probation; system blocks creation of new POs for this vendor; existing POs unaffected |
| **Termination** | No improvement after Probation, or scorecard rating F, or vendor commits fraud/breach | VP Merchandising approves termination; Category Manager notifies vendor; all open POs cancelled or allowed to complete per agreement; vendor master deactivated | Vendor master status changed to Inactive; system blocks all transactions; termination date and reason recorded in audit trail; vendor record retained for regulatory and historical purposes |
| **Reactivation** | Buyer requests reactivation with evidence of improved capability (new ownership, new processes, reference customers) | Category Manager reviews evidence; if approved, vendor re-enters onboarding process per W36 (abbreviated: skip trial PO if recent history exists) | Vendor master status changed back to Active; full audit trail of termination and reactivation retained |

### System Touchpoints
- Automated vendor scorecard generation from operational data (W44.1)
- Multi-metric scoring: on-time delivery, fill rate, quality, invoice accuracy, lead time, return rate (W44.1)
- Vendor rating system with configurable thresholds (W44.3)
- Improvement plan tracking (W44.4)
- Vendor lifecycle status: Active → Warning → Probation → Inactive (terminated) → Active (reactivated); each status change logged with reason, approver, date, and supporting documentation; system enforces PO blocking for Probation and Inactive vendors (W44.5, corrective action tiers)
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
| 13a | **Financial close-out checklist** — Controller and Store Manager verify the following location-specific commitments are resolved before final close: (a) petty cash float (PHP 20K) returned to Treasury via bank transfer or armored car; custodian reconciliation completed per W25; (b) gift cards / store credit vouchers issued by closing store — system reissuance to customer's nearest store location with customer notification; unredeemed store credit balance recognized as revenue upon closure; (c) pending special orders (W38) — customer deposits either fulfilled from alternative store/DC or refunded per W38.16 deposit refund process; (d) pending warranty claims (W33) — items at vendor for repair reassigned to customer's nearest store for pickup upon return; (e) pending backorders (W56) — allocation released or redirected to nearest store with customer notification; (f) store-specific vendor contracts (e.g., local maintenance, cleaning) — terminated per W62 with final payment; (g) store-specific service contracts — final invoice verified and paid; (h) **loyalty profile default-store reassignment**: system identifies all loyalty members whose registered default store is the closing store; system automatically reassigns each member's default store to the nearest active BuildRight store based on geographic proximity; affected members notified via SMS/email with new default store information; loyalty points, tier status, and transaction history unaffected by reassignment | Controller / Store Manager / AR Clerk / AP Clerk | CFO | 1 day |
| 13b | **LGU permit retirement**: Regulatory Officer notifies LGU Business Permit and Licensing Office (BPLO) of store closure; files closure notification with final local business tax payment (covering period up to closure date); obtains LGU closure acknowledgment; system updates location master with closure date and LGU retirement confirmation per W54; failure to retire LGU permit may result in continued LBT billing — Regulatory Officer confirms retirement within 30 days of closure | Regulatory Officer | Legal Head | 2–4 hours/location |
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
- Financial close-out checklist: petty cash return, gift card/store credit reissuance, special order deposit refund or fulfillment, warranty claim reassignment, backorder release, vendor contract termination per W62, final service invoice verification (W45.13a)
- LGU permit retirement: closure notification to LGU BPLO, final LBT payment, LGU closure acknowledgment, location master update (W45.13b)
- Integration with W25 (petty cash return), W28 (gift card reissuance), W33 (warranty reassignment), W38 (special order deposit refund), W54 (LGU permit retirement), W56 (backorder release), W62 (vendor contract termination)

### Staffing Implication
- **Store Ops Director**: Leads closure process. ~20 hours per closure spread over 2–3 months.
- **Supply Planner**: Mass redistribution planning adds ~1 week per closure. Absorbed within existing team.
- **HR**: Up to 35 separations + redeployments per closure. Absorbed within existing HR team with advance planning.
- **IT**: 1 week per store decommission. 2–3 IT staff per closure. With 2–5 closures/year, this is ~5–15 staff-weeks. Absorbed within existing IT team.
- **Finance**: Final P&L close-out adds ~1 day per closure. Absorbed.

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

## W47. Store Facility Maintenance & Work Orders

| Field | Detail |
|---|---|
| **Trigger** | Equipment failure, scheduled preventive maintenance, safety inspection finding, or store staff report |
| **Frequency** | Continuous; preventive maintenance on fixed schedules per equipment type |
| **Volume** | ~2,000–3,000 maintenance work orders/month across 200 stores + 5 DCs (~10–15 per location per month) |
| **Owner** | Store Manager (store-level); Facilities Coordinator (HQ oversight) |
| **Participants** | Maintenance/Utility staff, Store Manager, Facilities Coordinator, external contractors, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Issue identified: (a) store staff reports equipment malfunction (POS terminal, paint mixer, lumber saw, forklift, HVAC, lighting, plumbing, roll-up door), (b) scheduled preventive maintenance triggers, (c) safety inspection reveals deficiency | Maintenance / Utility Staff | Store Manager | 5 min (reporting) |
| 2 | Maintenance staff or Store Manager creates work order in system: location, equipment/area, issue description, priority (critical / high / medium / low), photos if applicable | Store Manager / Maintenance | Store Manager | 5 min |
| 3 | System classifies work order: (a) in-store capability — Maintenance/Utility staff can resolve with available tools and parts, (b) requires external contractor (specialized repair: HVAC, electrical, plumbing, elevator/escalator), (c) requires equipment vendor service (POS, forklift, paint mixer under warranty or service contract), (d) requires capex (major repair exceeding PHP 50,000 → route to W21 capex workflow) | System | — | Automated |
| 4a | **In-store resolution**: Maintenance staff performs repair using on-hand parts or petty cash purchase (W25); completes work order with repair description, parts used, and labor time | Maintenance / Utility | Store Manager | Varies (15 min – 4 hours) |
| 4b | **External contractor**: Store Manager or Facilities Coordinator engages pre-approved contractor from approved vendor list; contractor scheduled for site visit; system tracks appointment and SLA | Facilities Coordinator / Store Manager | Store Ops Director | Scheduling: 15 min; repair: varies |
| 4c | **Vendor service call**: Store Manager contacts equipment vendor for warranty or service contract repair; system links to vendor master and warranty records (W33 for warranty process, W21 for asset records) | Store Manager | Facilities Coordinator | 10 min (coordination) |
| 5 | Work order completed: repair verified by Store Manager; work order closed in system with resolution code, actual labor hours, parts cost, and contractor/vendor cost | Store Manager / Maintenance | Store Manager | 10 min |
| 6 | System posts maintenance costs: parts and labor to store maintenance expense GL; contractor invoices routed to AP per W7c (non-PO) or against maintenance contract PO | System | — | Automated |
| 7 | Monthly: Facilities Coordinator reviews maintenance report by location: total cost per store, top issue categories, contractor response time SLA compliance, recurring issues | Facilities Coordinator | Store Ops Director | 2 hours/month |

### Preventive Maintenance Schedule

| Equipment / System | Frequency | Responsible | Notes |
|---|---|---|---|
| HVAC units | Quarterly filter change; annual service | External contractor | Critical for customer comfort; store sells HVAC — reputation risk if own units fail |
| Fire suppression / extinguishers | Annual inspection per BFP requirement | Certified inspector | Regulatory compliance; non-negotiable |
| Paint mixing station | Monthly cleaning and calibration | Maintenance / Utility | Accuracy affects customer satisfaction |
| Lumber cutting equipment | Weekly blade inspection; monthly sharpening/replace | Maintenance / Utility | Safety-critical; dull blades are injury risk |
| POS terminals and peripherals | Quarterly cleaning and cable check | IT + Maintenance | Cross-reference W48 |
| Roll-up doors / loading docks | Bi-annual servicing | External contractor | Security and receiving operations |
| Electrical panel and generators (if applicable) | Annual inspection | Licensed electrician | Safety compliance |
| Pest control | Monthly treatment | External contractor (pest control vendor) | Health and sanitation |
| Hazardous waste disposal | Per accumulation or quarterly | Licensed DENR-accredited transporter | Regulatory compliance (DENR/EMB) |
| Elevators / escalators (if applicable) | Monthly inspection per DOLE requirement | Licensed elevator contractor | Regulatory compliance |

### System Touchpoints
- Work order creation with priority classification and photo attachment (W47.2)
- Auto-classification of resolution path: in-store, contractor, vendor service, or capex (W47.3)
- Pre-approved contractor vendor list with rate cards and SLA terms (W47.4b)
- Maintenance cost posting to store-level GL (W47.6)
- Preventive maintenance scheduling with automated work order generation per equipment calendar (W47 preventive table)
- Maintenance reporting by location, cost, issue category, contractor performance (W47.7)
- Integration with W21 (capex routing for major repairs), W25 (petty cash for small parts), W33 (vendor warranty claims), W39 (asset retirement if equipment beyond repair), W48 (IT equipment maintenance)
- Hazardous waste disposal: paint mixing stations (W5b.3), chemical receiving areas, and lumber treatment areas generate hazardous waste (waste paint, solvents, chemical containers, treated wood offcuts) regulated under DENR Administrative Order No. 2013-22 (Revised Procedures and Requirements for the Management of Hazardous Wastes); Facilities Coordinator maintains a hazardous waste storage area at each store and DC — clearly labeled, ventilated, and segregated from general waste; waste accumulates in approved containers with proper labeling (waste type, date of first accumulation, hazard class); when accumulation reaches threshold (per DENR guidelines or when 90-day storage limit approaches), Facilities Coordinator arranges pickup by DENR-accredited hazardous waste transporter; transporter provides manifests (manifest system per DENR: 6-copy form tracking waste from generator to transporter to treater/disposer); system records hazardous waste disposal events: waste type, quantity, transporter, manifest number, disposal facility, date; manifest copies scanned and attached to disposal record; quarterly: Facilities Coordinator generates hazardous waste disposal report per location for DENR compliance; annual: DENR hazardous waste generator registration renewal per location (separate from W54 LGU business permit but tracked in the same Regulatory Officer calendar); Facilities Coordinator ensures all locations with paint mixing or chemical operations are registered as hazardous waste generators with DENR-EMB Regional Office; first violation of hazardous waste disposal regulations carries penalties of PHP 10,000–200,000 per DENR

### Staffing Implication
- **1 Maintenance/Utility per store** (already in model): handles ~10–15 work orders/month including routine preventive tasks. Viable for standard repairs and routine maintenance; relies on external contractors for specialized work.
- **1 Facilities Coordinator** (HQ, within Store Ops team): manages contractor relationships, preventive maintenance calendar compliance, and maintenance cost analysis across 200 stores. This is a new role recommendation.
- **External contractor network**: each store should have 3–5 pre-approved contractors (electrician, plumber, HVAC technician, general handyman) on retainer or call-out basis. Facilities Coordinator manages the approved list centrally.

---

## W48. IT Operations & Helpdesk Support

| Field | Detail |
|---|---|
| **Trigger** | User reports issue (phone, email, self-service portal); system generates automated alert; scheduled change window |
| **Frequency** | Continuous; ~800–1,200 support tickets/month across all locations |
| **Volume** | ~8,050 users; 1,000 POS terminals; 5 WMS systems; ~500 RF devices; 200+ network locations |
| **Owner** | IT Helpdesk Lead |
| **Participants** | IT Helpdesk, IT Infrastructure, IT Applications, end users, external vendors |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | User contacts IT Helpdesk via phone, email, or self-service portal; describes issue with system, hardware, network, or access | End User | — | 2 min |
| 2 | Helpdesk Agent creates support ticket: user, location, device, issue category, severity (see matrix below), description | Helpdesk Agent | IT Helpdesk Lead | 3 min |
| 3 | System auto-routes ticket based on category: (a) POS/retail → Retail IT support queue, (b) network/connectivity → Infrastructure queue, (c) ERP/application → Applications queue, (d) hardware → Hardware support queue, (e) access/permissions → Security queue | System | — | Automated |
| 4 | **Tier 1 — Remote resolution**: Helpdesk Agent attempts to resolve remotely (password reset, configuration fix, user guidance, system restart) | Helpdesk Agent | IT Helpdesk Lead | 5–15 min |
| 5 | If Tier 1 resolves: ticket closed with resolution code; user confirms | Helpdesk Agent | — | 2 min |
| 6 | If Tier 1 unresolved: ticket escalated to Tier 2 (specialist) with diagnostic notes; SLA timer restarts per severity | Helpdesk Agent | IT Helpdesk Lead | 2 min |
| 7 | **Tier 2 — Specialist resolution**: IT specialist investigates; may require remote session, configuration change, or system-level fix | IT Specialist | IT Helpdesk Lead | 15–60 min |
| 8 | If Tier 2 requires on-site presence (hardware failure, network cabling, POS terminal replacement): ticket assigned to IT Field Support with scheduled site visit | IT Specialist | CIO | Scheduling: 5 min |
| 9 | **Tier 3 — Vendor / escalation**: if issue requires vendor support (POS software bug, ERP vendor support, hardware warranty claim), IT engages vendor; tracks vendor response SLA | IT Specialist / CIO | CIO | Vendor-dependent |
| 10 | Resolution confirmed by user; ticket closed; system logs resolution time, root cause category, and recurring issue flag | Helpdesk Agent | IT Helpdesk Lead | 2 min |
| 11 | Monthly: IT Helpdesk Lead reviews ticket analytics: volume by category, resolution rate by tier, SLA compliance, mean time to resolution, top recurring issues per location | IT Helpdesk Lead | CIO | 2 hours/month |

### Severity & SLA Matrix

| Severity | Definition | Examples | Response SLA | Resolution SLA |
|---|---|---|---|---|
| **P1 — Critical** | System down affecting revenue or multiple users | All POS terminals down at a store, ERP system inaccessible, DC WMS failure | 15 min | 4 hours |
| **P2 — High** | Major function impaired but workaround exists | Single POS terminal down, ecommerce integration failure, reporting module error | 30 min | 8 hours |
| **P3 — Medium** | Non-critical issue affecting productivity | Printer malfunction, slow report generation, single user access issue | 2 hours | 24 hours |
| **P4 — Low** | Minor issue or enhancement request | Cosmetics, feature requests, non-urgent how-to questions | 8 hours | 72 hours |

### Change Management

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 1 | IT team member submits change request: description, affected systems, risk assessment, rollback plan, planned window | IT Team Member | IT Helpdesk Lead | As needed (~20–30 changes/month) |
| 2 | IT Helpdesk Lead reviews and classifies: (a) standard change (pre-approved, low risk — e.g., password policy update), (b) normal change (requires review and approval — e.g., POS software patch), (c) emergency change (unplanned, critical fix — e.g., security vulnerability patch) | IT Helpdesk Lead | CIO | 10 min/change |
| 3 | Normal changes: CIO approves; emergency changes: CIO verbal approval with post-hoc documentation; standard changes: auto-approved per catalog | CIO | — | 5–15 min/change |
| 4 | Change executed during maintenance window (typically Tuesday/Thursday 22:00–02:00 or Sunday 00:00–04:00 to avoid peak hours) | IT Infrastructure | CIO | Per change |
| 5 | Post-change verification: IT confirms system health; Helpdesk monitors for related ticket spikes in next 24 hours | IT Team | IT Helpdesk Lead | 15 min/change |

### System Touchpoints
- IT ticket management: create, route, escalate, resolve, close with full audit trail (W48.2–10)
- Auto-routing by issue category to specialist queues (W48.3)
- SLA timer per severity level with auto-escalation at 75% of SLA threshold (W48.4–9)
- Remote desktop / diagnostic tool integration (W48.4, 7)
- Knowledge base / self-service portal for common issues (W48.1)
- Change request workflow with classification and approval (W48 change management)
- Maintenance window scheduling (W48 change 4)
- Ticket analytics dashboard: volume, SLA compliance, MTTR, top issues by location (W48.11)
- SLA breach escalation protocol: (a) single P1 SLA miss (resolution > 4 hours): IT Helpdesk Lead conducts immediate root cause analysis and documents corrective action; (b) 2 consecutive P1 SLA misses on same issue category: Helpdesk Lead escalates to CIO with remediation plan within 24 hours; CIO reviews staffing, tooling, or vendor support adequacy; (c) 3 or more P1 SLA misses within 30 days (any category): CIO presents incident review to CEO with systemic improvement plan (may include additional headcount, vendor escalation, or infrastructure investment); (d) P2/P3 SLA misses trending > 20% breach rate for 2 consecutive months: Helpdesk Lead initiates category-specific improvement (process change, training, or automation); (e) all SLA breaches tracked in monthly ticket analytics dashboard with trend analysis and root cause classification; SLA performance included in IT team's quarterly performance review (W48)
- IT asset tracking: system maintains asset register for all IT equipment (POS terminals, RF devices, servers, networking equipment, laptops, tablets) with location assignment, warranty status, maintenance history, and lifecycle status; supports IT asset planning and budgeting (cross-reference W21 for capex, W39 for disposal)
- Integration with W5g (offline POS recovery), W16 (new store IT setup), W43 (employee separation — account deactivation)

### Staffing Implication
- **4–5 Helpdesk Agents (Tier 1)**: handle ~800–1,200 tickets/month ÷ 20 working days = ~40–60/day. At ~10 min average per ticket = ~7–10 hours/day. With shifts and coverage, 4–5 agents needed.
- **3–4 IT Specialists (Tier 2)**: Application support, infrastructure, retail IT, security. Specialists handle ~30% of tickets that Tier 1 cannot resolve = ~240–360/month.
- **1–2 IT Field Support**: physical site visits for hardware issues across 200 stores + 5 DCs. Estimated 50–80 on-site visits/month across the Philippines. With travel time, 1–2 dedicated field staff with regional coverage.
- **1 IT Helpdesk Lead**: manages helpdesk operations, SLA compliance, change management.
- **Total IT**: recommend expanding IT team from ~25 to ~28–30 to accommodate dedicated helpdesk function. Current ~25 includes infrastructure, applications, data, security, and BI but does not explicitly allocate helpdesk headcount.

---

## W49. Natural Disaster / Typhoon Business Continuity

| Field | Detail |
|---|---|
| **Trigger** | PAGASA raises tropical cyclone warning signal over a store/DC location; or earthquake, flooding, or volcanic activity alert |
| **Frequency** | ~10–20 typhoon-related events/year requiring action across Philippine store network; 2–4 significant events/year with store closures |
| **Volume** | Variable — from 1–2 stores affected (localized flooding) to 50+ stores (major typhoon crossing multiple regions) |
| **Owner** | COO (overall response); Store Manager (store-level execution) |
| **Participants** | COO, Store Ops Director, Regional Managers, Store Managers, DC Managers, IT, HR, Finance, Supply Chain, Marketing, Logistics |

### Background

The Philippines experiences an average of 20 tropical cyclones per year, of which 5–7 make landfall as typhoons (Signal 3 or higher). BuildRight's 200 stores span Luzon, Visayas, and Mindanao, meaning multiple regions can be affected simultaneously or sequentially. The primary risks are: (a) staff safety, (b) inventory damage (especially outdoor lumber yards and building materials), (c) facility structural damage, (d) supply chain disruption, and (e) revenue loss from store closures.

### Phase 1: Pre-Disaster Preparation (48–72 hours before projected landfall)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | COO monitors PAGASA bulletins and NDRRMC advisories; activates disaster monitoring protocol when Signal 1 is raised over any operating region | COO | CEO | Ongoing during typhoon season |
| 2 | Regional Managers notify Store Managers in affected regions to begin preparations; Store Managers brief all staff | Regional Manager | Store Ops Director | 1 hour |
| 3 | **Store preparations**: Store Manager directs staff to: (a) secure outdoor yard inventory — move lumber, cement, and building materials under cover or to higher ground; (b) protect floor-level merchandise from potential flooding (move to higher shelves or backroom); (c) secure display fixtures, signage, and loose items; (d) verify backup power (generator fuel level, battery backup for POS); (e) verify emergency supplies (flashlights, first aid kits, drinking water) | Store Manager | Regional Manager | 4–8 hours |
| 4 | **DC preparations**: DC Manager directs staff to: (a) prioritize outbound shipments to stores in safe zones before transport disruption; (b) secure outdoor inventory and yard areas; (c) verify backup power systems; (d) coordinate with carriers to suspend inbound shipments to affected areas | DC Manager | Supply Chain Manager | 4–8 hours |
| 5 | IT sends system advisory to all locations: reminder of offline POS procedures (W5g), system backup schedule accelerated | IT Team | CIO | 30 min |
| 6 | HR verifies emergency contact information for all employees in affected regions; prepares welfare check plan | HR Head | CHRO | 1 hour |
| 7 | Supply Planner reviews inventory levels at stores and DCs in projected path; identifies potential stockout risks for essential items (tarps, waterproofing, cement, plywood, flashlights, batteries, generators) | Supply Planner | Supply Chain Manager | 1 hour |

### Phase 2: Closure Decision & Execution (24–0 hours before projected landfall)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 8 | COO makes store closure decision based on: PAGASA signal level (Signal 2+ triggers automatic closure), LGU advisory, road conditions, staff safety assessment; decisions made by region, not chain-wide | COO | CEO | 30 min |
| 9 | Marketing communicates closure to customers: update website, social media, Google Business listings; send SMS/email to loyalty members in affected areas | Marketing | CMO | 1 hour |
| 10 | Ecommerce platform: Digital Commerce Inc. suspends BOPIS and delivery orders for closed stores/DCs; displays closure notice | Ecom Team | CMO | 30 min |
| 11 | Store Manager executes early closing procedure (abbreviated W5c): expedited Z-report, cash secured in safe (do NOT send with armored car during typhoon — hold in safe), POS shut down, building secured | Store Manager | Regional Manager | 30 min |
| 12 | Store Manager sends staff home with safety instructions; confirms all staff have departed safely | Store Manager | Regional Manager | 15 min |

### Phase 3: Post-Disaster Assessment & Recovery (0–72 hours after event)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 13 | Store Manager or designated contact conducts visual assessment of store exterior (drive-by or walk-by) as soon as safely possible after event passes; reports to Regional Manager: structural damage, flooding, power status, yard inventory status | Store Manager | Regional Manager | 30 min |
| 14 | Regional Manager compiles damage assessment across affected stores; reports to COO and Store Ops Director | Regional Manager | COO | 2 hours |
| 15 | COO makes reopening decision per store: (a) open immediately if no damage and power/connectivity restored, (b) delayed opening for minor cleanup and repair, (c) remain closed for significant damage requiring repair or insurance assessment | COO | CEO | 1 hour |
| 16 | **If inventory damaged**: Store Manager conducts damage inventory with photos; system creates damage report; disposition per W6.8a (scrap, markdown, RTV, insurance claim) | Store Manager / Maintenance | Regional Manager | 2–4 hours |
| 17 | **If facility damaged**: Facilities Coordinator engages contractors for emergency repair; Store Manager initiates insurance claim per W3.6a process (photos, documentation, claim filing) | Facilities Coordinator / Store Manager | Store Ops Director | Varies |
| 18 | Supply Planner triggers emergency replenishment for disaster-response items (tarps, plywood, cement, paint, waterproofing, tools, generators) to reopened stores; coordinates with DC for expedited shipment | Supply Planner | Supply Chain Manager | 2–4 hours |
| 19 | HR conducts welfare check on all employees in affected regions within 24 hours; provides assistance (advance salary, emergency loan, temporary shelter) per company policy | HR Head | CHRO | 4–8 hours |
| 20 | Marketing communicates reopening to customers; update website and social media; potential "rebuilding supplies" promotion to serve community needs | Marketing | CMO | 1 hour |
| 21 | System reconciles: process any offline POS transactions from pre-closure; reverse pending ecommerce orders for closed stores; update inventory for damaged/scrapped items | IT / Finance | Controller | 2–4 hours |

### Phase 4: Post-Event Review (1–2 weeks after)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 22 | COO conducts after-action review: preparation adequacy, response time, damage extent, recovery speed, staff safety outcomes | COO | CEO | 2 hours |
| 23 | Finance quantifies total loss: inventory damage, facility repair costs, revenue loss from closure days, insurance recovery | Controller | CFO | 1 day |
| 24 | Insurance claims finalized for major events; Finance tracks claim status and settlement | Treasury Analyst | CFO | Varies |
| 25 | Store Ops Director updates disaster response procedures based on lessons learned | Store Ops Director | COO | 2 hours |

### System Touchpoints
- Emergency communication channel integration (SMS blast to store managers, regional managers, employees) (W49.2, 6, 9)
- Store closure/reopening status tracking per location with real-time dashboard (W49.8, 15)
- Ecommerce platform store availability toggle for BOPIS/delivery (W49.10)
- Damage inventory recording with photo attachment and disposition workflow (W49.16)
- Emergency replenishment order generation with priority flag (W49.18)
- Insurance claim tracking per W3.6a process (W49.17, 24)
- Post-disaster inventory and financial reconciliation (W49.21, 23)
- Employee welfare check tracking with HR case management (W49.19)
- Integration with W5g (offline POS recovery), W3.6a (insurance claims), W22 (emergency transfers), W25 (emergency petty cash for cleanup supplies), W47 (facility emergency repair)

### Staffing Implication
- No dedicated disaster response team. Response is a cross-functional effort managed by existing roles (COO leads, Regional Managers execute, Store Managers act).
- **Facilities Coordinator** (recommended in W47) becomes critical during post-disaster recovery for coordinating emergency repairs across multiple affected stores.
- **IT Field Support** (recommended in W48) may need to deploy to affected stores for POS/network restoration.
- Post-disaster emergency replenishment adds temporary surge to Supply Planner and DC workload — absorbed with overtime during recovery period.

---

## W50. Product Information Management (PIM)

| Field | Detail |
|---|---|
| **Trigger** | New SKU creation (W1), seasonal item setup (W32), product content refresh cycle, vendor product update |
| **Frequency** | Continuous; ~1,500–2,500 new SKUs/year + seasonal rotations + content refreshes |
| **Volume** | 35,000 active SKUs requiring product content; ~55,000 total in item master |
| **Owner** | Marketing — Content Manager |
| **Participants** | Content Manager, Content Specialist, Merchandise Planner, Category Manager, Ecom Team, Photographer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Trigger: Merchandise Planner creates new SKU in item master per W1.7 (or seasonal setup per W32); system flags SKU as "content pending" — item cannot be published to ecommerce until content is complete | System | — | Automated |
| 2 | Content Manager receives new SKU content request from system queue; assigns to Content Specialist by category | Content Manager | — | 5 min |
| 3 | Content Specialist gathers product information: (a) vendor product data sheet (specs, dimensions, weight, material, finish, color options), (b) Category Manager input (key selling points, target customer, recommended use), (c) competitive product content benchmarking | Content Specialist | Content Manager | 15–30 min/SKU |
| 4 | Content Specialist enriches product data in PIM/ERP: (a) completes all mandatory attributes per category schema (e.g., tiles: material, size mm, thickness, finish, PEI rating, pieces per sqm; lumber: species, dimensions, treatment, grade; paint: base type, coverage area, drying time, finish), (b) writes short description (50–100 chars for search results), (c) writes long description (200–500 chars for product page — features, benefits, application), (d) maps to category navigation path, (e) assigns search keywords and synonyms, (f) links related accessories and cross-sell items | Content Specialist | Content Manager | 20–30 min/SKU |
| 5 | Product photography: (a) for new SKUs with high online potential (A/B items): schedule product shoot with photographer (studio or on-location for large items); produce 3–5 images per SKU (front, detail, lifestyle/context, dimensions reference, packaging), (b) for C-items and low online potential: use vendor-provided images or placeholder category image with "image coming soon" flag; system marks these items for prioritized photography during quarterly content refresh | Content Specialist / Photographer | Content Manager | Shoot: 5–10 min/SKU |
| 6 | Content Specialist uploads and links digital assets (images, PDFs for spec sheets, installation guides, safety data sheets) to SKU record in PIM/ERP | Content Specialist | Content Manager | 5 min/SKU |
| 7 | Content Manager reviews and approves completed content per SKU; checks attribute completeness, description quality, image quality, and keyword relevance | Content Manager | CMO | 5 min/SKU |
| 8 | System publishes approved content to ecommerce platform (catalog sync); updates in-store kiosk and POS product lookup if applicable; clears "content pending" flag | System | — | Automated |
| 9 | For items with vendor-provided content only: system publishes with "vendor content — not verified" tag visible to Content Manager; these items prioritized for enrichment during quarterly refresh | System | Content Manager | Automated |
| 10 | **Quarterly content refresh**: Content Manager reviews content quality metrics (incomplete attributes, missing images, low search ranking, high bounce rate on product pages); prioritizes 500–1,000 SKUs for content improvement per quarter | Content Manager | CMO | 8 hours/quarter |
| 11 | **Seasonal catalog refresh**: before each major promotional period (W13), Content Manager coordinates with Marketing for seasonal landing pages, featured product collections, and updated lifestyle imagery | Content Manager | CMO | Per W13 lead time |

### System Touchpoints
- PIM module or dedicated PIM system integrated with ERP item master (W50.4)
- Category-specific attribute schema with mandatory field enforcement (W50.4)
- Content workflow: Draft → In Review → Approved → Published → Refresh Needed (W50.7–8)
- Digital asset management: image storage, versioning, and linking to SKU records (W50.6)
- Ecommerce catalog sync with content completeness validation (W50.8)
- Content quality dashboard: attribute completeness % by category, missing images, search ranking, page views, bounce rate (W50.10)
- Integration with W1 (SKU creation trigger), W13 (promotional content), W32 (seasonal setup), W36 (vendor onboarding — vendor content import)

> **Seasonal PIM timeline coordination**: W32 seasonal buy planning requires SKU content to be ready for catalog/promo publication at least 6 weeks before season start. The PIM-to-seasonal timeline is: (a) W32 step 2 (Category Manager reviews seasonal forecast) triggers content request to Content Manager with target content-ready date = T-6 weeks before season; (b) W32 step 4 (Category Manager creates seasonal buy plan with SKU list) provides Content Manager with the final SKU list for content creation; (c) Content Manager prioritizes seasonal SKUs in the content queue — seasonal SKUs bypass the standard queue and are assigned to Content Specialists within 2 business days of receipt; (d) Content Specialists complete content (attributes, descriptions, images) within 2 weeks of assignment; (e) Content Manager reviews and approves within 3 business days; (f) system publishes approved content to ecommerce catalog at T-3 weeks before season start to allow Marketing to build seasonal landing pages and email campaigns; (g) if content is not ready by T-3 weeks, Content Manager escalates to CMO with risk assessment (incomplete content reduces ecommerce conversion for seasonal items); this timeline is tracked by Content Manager as part of the W50 quarterly content refresh calendar and reviewed in seasonal kick-off meetings with Category Managers and Marketing.

### Staffing Implication
- **1 Content Manager** (within Marketing team): manages content strategy, quality standards, and team output.
- **2–3 Content Specialists**: at ~1,500–2,500 new SKUs/year × 45 min/SKU average = ~1,100–1,900 hours/year. With 2–3 specialists, that's ~400–600 hours/year each = ~10–15 hours/week of new content, leaving time for quarterly refreshes and seasonal campaigns.
- **1 Photographer** (in-house or freelance retainer): product shoots scheduled in batches (50–100 SKUs per shoot day). With ~600–1,000 A/B items needing photography annually, that's ~10–15 shoot days/year.
- **Incremental headcount**: Content Manager + 2 Content Specialists should be added to the Marketing team (from ~20 to ~23) to support ecommerce content operations. These roles become increasingly critical as ecommerce penetration grows from 3% to 7% of revenue.

---

## W51. Employee Training & Skills Development

| Field | Detail |
|---|---|
| **Trigger** | New hire onboarding (W15), new system rollout, compliance requirement, periodic schedule, performance review finding |
| **Frequency** | Continuous; formal training sessions monthly per store; compliance training quarterly |
| **Volume** | ~8,050 employees; ~1,200–1,600 new hires/year requiring onboarding training; all employees require periodic refresher |
| **Owner** | HR — Training Officer |
| **Participants** | Training Officer, Department Supervisors, Store Managers, Category Managers (product knowledge), IT (system training), external trainers |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Training Officer maintains annual training calendar: (a) new hire onboarding (W15 step 10 — continuous), (b) quarterly compliance refreshers (safety, BIR procedures, data privacy), (c) semi-annual product knowledge updates (aligned with W1 assortment review and W32 seasonal planning), (d) annual system refresher (POS, ERP updates), (e) leadership development for supervisors and managers | Training Officer | HR Head | 4 hours/quarter (planning) |
| 2 | Training Officer develops or sources training materials per category: (a) creates in-house materials for company-specific processes (POS operations, returns handling, safety procedures, customer service standards), (b) sources external content for compliance topics (fire safety, first aid, hazmat handling for paint/chemicals), (c) coordinates with Category Managers for product knowledge content (new product features, seasonal items) | Training Officer | HR Head | Ongoing |
| 3 | Training delivery methods by audience: (a) **Store staff (7,000)**: monthly 30-minute department huddles led by Department Supervisors using provided materials; quarterly 2-hour group sessions at store level; (b) **DC staff (~750)**: quarterly safety and equipment training at DC; (c) **HQ staff (~300)**: quarterly system and process training at HQ; (d) **New hires**: W15 onboarding program (2–3 days); (e) **Managers and supervisors**: semi-annual leadership and management skills workshops | Training Officer / Dept. Supervisors / External Trainers | HR Head | Per schedule |
| 4 | System tracks training completion per employee: attendance recording, quiz/assessment scores (where applicable), certification status and expiry dates | System / HR Assistant | Training Officer | Automated + 15 min/session |
| 5 | Training Officer generates compliance dashboard: completion rates by training type, overdue trainings by location, certification expiries (e.g., forklift license, fire safety) | Training Officer | HR Head | 1 hour/month |
| 6 | Department Supervisors and Store Managers identify training needs from performance observations (W34 schedule adherence, W37 exception patterns, W41 complaint root causes) and submit training requests to Training Officer | Dept. Supervisor / Store Manager | HR Head | As needed |
| 7 | Annual: HR Head reviews training program effectiveness: training hours per employee, correlation between training completion and key metrics (POS accuracy, shrinkage rate, customer satisfaction), budget utilization | HR Head | CHRO | 4 hours/year |

### Training Categories

| Category | Frequency | Audience | Delivery Method | Assessment |
|---|---|---|---|---|
| **New hire onboarding** | Per W15 | New employees | In-person at store/DC + e-learning modules | POS competency test, safety quiz |
| **POS operations** | Annual refresher; ad-hoc for system updates | Cashiers, CSRs | Hands-on at POS terminal | Speed and accuracy test |
| **Product knowledge** | Quarterly (aligned with W1 assortment review) | Sales Associates, Dept. Supervisors | Department huddle with Category Manager materials | Informal — supervisor observation |
| **Safety & compliance** | Quarterly | All employees | E-learning (LMS) + annual practical drill | Mandatory quiz (pass/fail) |
| **Hazmat handling** | Annual (for paint/chemical departments) | Paint dept. staff, receiving clerks | In-person with certified trainer | Written test + practical demo |
| **Loss prevention awareness** | Semi-annual | All store staff | E-learning + LP officer presentation (W37) | Awareness quiz |
| **Leadership development** | Semi-annual | Store Managers, Dept. Supervisors, Asst. Managers | Workshop (2 days) | 360 feedback |
| **IT system updates** | Per system change (W48 change management) | Affected users | E-learning + release notes | N/A |

### System Touchpoints
- Training calendar management with automated scheduling (W51.1)
- Training material repository (document storage per category) (W51.2)
- Training attendance tracking with digital sign-in or manager confirmation (W51.4)
- Assessment and certification tracking with expiry alerts (W51.4–5)
- Compliance dashboard: completion rates, overdue trainings, certification status by location and employee (W51.5)
- Learning Management System (LMS) integration for e-learning modules and assessments (W51.3)
- Integration with W15 (onboarding), W34 (shift scheduling — training time scheduled), W37 (LP awareness), W43 (separation — training history retained), W48 (system change training)
- Employee self-service portal: system provides a web-based or mobile-accessible self-service portal for employees with the following capabilities — (a) **payslip viewing**: employees view and download current and historical payslips (secure, accessible only by the employee); (b) **leave management**: employees submit leave requests (VL, SL, maternity, paternity, etc.) with automatic routing to Department Supervisor / Store Manager for approval; view leave balance and approval status; (c) **personal information update**: employees update contact information (address, phone, emergency contact), bank account details for payroll crediting, and dependent information; changes require HR Assistant verification before updating the payroll master; (d) **tax document access**: employees view and download BIR Form 2316 (Certificate of Compensation Payment/Tax Withheld) annually; (e) **benefits inquiry**: view SSS, PhilHealth, Pag-IBIG contribution history and loan balances (linked to agency portals or displayed from payroll data); (f) **training enrollment**: browse and enroll in available training sessions from the W51 training calendar; view training history and certification status; (g) **announcement board**: HR and management post company announcements, policy updates, and employee engagement content; portal access is role-based (employees see their own data only; managers see additional team-level information such as team leave calendar); mobile-responsive design for access from smartphones; requirement priority: Should Have (not all features needed at go-live — payslips and leave management are highest priority)

### Staffing Implication
- **1 Training Officer** (within HR team): manages training calendar, develops materials, coordinates external trainers, and monitors compliance. With 8,050 employees across 200+ locations, this is a full-time role.
- **Department Supervisors (per store)**: deliver monthly department huddles (30 min/month) — absorbed into existing duties.
- **HR Assistants (2)**: support attendance recording and logistics — absorbed into existing duties.
- **External trainers**: engaged for specialized topics (fire safety, hazmat, first aid, forklift certification, leadership) on a per-event basis.

---

## W52. Fleet Management

| Field | Detail |
|---|---|
| **Trigger** | Vehicle registration renewal, scheduled maintenance, fuel purchase, driver assignment, route planning review |
| **Frequency** | Continuous; daily operations + periodic scheduled maintenance |
| **Volume** | ~30–40 owned vehicles (20% of total fleet); remainder 80% third-party (Lalamove, Transportify, contracted carriers) |
| **Owner** | Fleet Manager (within Supply Chain team) |
| **Participants** | Fleet Manager, Drivers, DC Dispatch, Finance, External carriers |

### Background

BuildRight's distribution fleet operates with a mixed model: ~20% owned vehicles (primarily 10-wheeler wing vans and 6-wheeler trucks for regular DC-to-store routes) and ~80% third-party carriers (for seasonal surge, inter-island routes, last-mile ecommerce delivery via Lalamove/Transportify). Owned vehicles are registered under BuildRight Logistics Inc. Third-party carrier management for ecommerce is covered in W19 (3PL management) and for general distribution in W4 (outbound logistics).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Driver assignment**: Fleet Manager assigns drivers to owned vehicles based on route schedule, driver qualifications (LTO license type — professional driver's license with restriction codes for heavy vehicles), and duty hour limits | Fleet Manager | Supply Chain Manager | 30 min/week |
| 2 | **Daily pre-trip inspection**: Driver conducts vehicle inspection checklist (tires, brakes, lights, fluid levels, cargo area, safety equipment) before departure; records in system via mobile app; vehicle not cleared for dispatch if critical items fail | Driver | Fleet Manager | 15 min/vehicle/day |
| 3 | **Fuel management**: Driver refuels at designated fuel stations using company fuel card; system captures fuel volume, odometer reading, and cost per transaction; Fleet Manager reviews fuel consumption per vehicle monthly (km/L benchmark per vehicle type; flags vehicles > 15% below benchmark for maintenance investigation) | Driver / Fleet Manager | Fleet Manager | 5 min/refuel + 1 hour/month review |
| 4 | **Scheduled maintenance**: Fleet Manager maintains maintenance calendar per vehicle based on manufacturer intervals (typically every 5,000–10,000 km or 3–6 months): (a) oil change and basic service, (b) tire rotation and replacement, (c) brake inspection, (d) annual comprehensive service; system alerts Fleet Manager 1 week before service due | Fleet Manager | DC Manager | Per schedule |
| 5 | **Unscheduled repair**: Driver reports vehicle issue; Fleet Manager assesses severity: (a) minor — schedule repair at next available slot, substitute 3PL for pending deliveries, (b) major — vehicle taken out of service, substitute vehicle or 3PL arranged | Fleet Manager | DC Manager | 30 min/occurrence |
| 6 | Maintenance or repair executed at company-approved workshop per region; Fleet Manager approves work order and cost; system tracks maintenance history per vehicle | Fleet Manager | DC Manager | Varies |
| 7 | **Vehicle registration & insurance**: Fleet Manager maintains calendar for LTO registration renewal (annual per vehicle), CTPL insurance renewal, and comprehensive insurance; system alerts 60 days before expiry; vehicles with expired registration blocked from dispatch | Fleet Manager | DC Manager | 30 min/vehicle/year |
| 8 | **Route performance review**: monthly, Fleet Manager reviews route metrics per vehicle: km driven, fuel efficiency, delivery punctuality (on-time % per W4 SLA), maintenance cost per km; identifies vehicles with declining performance for maintenance escalation or replacement planning | Fleet Manager | Supply Chain Manager | 2 hours/month |
| 9 | **3PL carrier performance**: Fleet Manager monitors third-party carrier performance per W19 (on-time delivery, damage rate, cost per delivery) in coordination with DC Dispatch; quarterly carrier review per W44 vendor scorecard methodology | Fleet Manager / DC Dispatch | Supply Chain Manager | Per W19/W44 |
| 10 | **Vehicle replacement planning**: annually, Fleet Manager evaluates vehicles > 5 years or > 300,000 km for replacement; submits capex request per W21; considers total cost of ownership (maintenance cost trajectory, fuel efficiency decline, reliability) vs. new vehicle cost plus financing | Fleet Manager | Supply Chain Manager | Annual (4 hours) |

### System Touchpoints
- Vehicle master record: plate number, VIN, model, year, capacity, assigned DC, registration expiry, insurance expiry, assigned driver (W52.1)
- Pre-trip inspection checklist on mobile app with defect reporting and dispatch block for critical failures (W52.2)
- Fuel card integration: automated fuel transaction capture with per-vehicle km/L tracking and anomaly alerting (W52.3)
- Maintenance scheduling with automated alerts per vehicle based on km or calendar interval (W52.4)
- Maintenance history tracking with cost per vehicle and cost per km (W52.6, 8)
- Registration and insurance calendar with expiry alerting and dispatch blocking (W52.7)
- Route and delivery performance tracking per vehicle (W52.8)
- Integration with W4 (route scheduling), W19 (3PL management), W21 (vehicle replacement capex), W39 (vehicle disposal), W30 (fuel expense GL posting)

### Staffing Implication
- **1 Fleet Manager** (within Supply Chain team): manages owned fleet (30–40 vehicles) and third-party carrier relationships. This role reports to Supply Chain Manager and coordinates daily with DC Dispatch.
- **30–40 Drivers** (BuildRight Logistics Inc. employees): assigned to owned vehicles; each driver covers ~1–2 routes/day, 5–6 days/week. Drivers are part of Logistics Inc. headcount (~750 total DC staff includes drivers).
- **Approved workshops**: 2–3 workshops per region (Davao, Cebu, Laguna, Clark, Manila) for scheduled and unscheduled maintenance. Fleet Manager manages workshop relationships and rate negotiations.
- **Fuel card program**: corporate fuel card (e.g., Petron Value Card, Shell Fleet Card) for all owned vehicles. Eliminates cash handling for fuel and enables automated consumption tracking.


---

## W53. Data Privacy Breach Response

| Field | Detail |
|---|---|
| **Trigger** | Suspected or confirmed breach of personal data (customer, employee, or vendor data) as defined by RA 10173 (Data Privacy Act of 2012) |
| **Frequency** | Rare; estimated 0–2 incidents/year requiring formal breach response |
| **Volume** | Variable — from a single record exposed to bulk data extraction |
| **Owner** | Data Protection Officer (DPO) |
| **Participants** | DPO, CIO, IT Security, Legal, affected department head, NPC (National Privacy Commission), affected data subjects |

### Background

Under RA 10173 and its Implementing Rules and Regulations (IRR), BuildRight Depot (as a PIC — Personal Information Controller) must: (a) notify the National Privacy Commission within 72 hours of discovering a breach involving sensitive personal information affecting 100+ data subjects, (b) notify affected data subjects within a reasonable time, (c) document all breaches regardless of size. BuildRight holds personal data for ~600,000 loyalty members, ~5,200 trade accounts, ~200 corporate accounts, ~8,050 employees, and ~1,000 vendors.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Breach discovered or suspected: IT Security alerts (automated monitoring), employee report, third-party notification, or customer complaint about unauthorized access | IT Security / Any employee | CIO | Immediate |
| 2 | CIO and DPO assess breach severity: (a) scope — how many records, what data types (name, contact, financial, government ID), (b) vector — how the breach occurred (external attack, insider, misconfiguration, lost device, vendor breach), (c) containment status — is the breach ongoing or contained | CIO + DPO | CEO | 1–2 hours |
| 3 | **Containment**: IT Security takes immediate action to stop the breach: isolate affected systems, revoke compromised credentials, block unauthorized access, preserve forensic evidence | IT Security | CIO | As needed |
| 4 | DPO classifies the breach per NPC guidelines: (a) **Notifiable breach** — involves sensitive personal info, affects 100+ data subjects, or involves significant harm; (b) **Non-notifiable breach** — limited scope, no sensitive data, quickly contained | DPO | CEO | 30 min |
| 5 | If notifiable: DPO prepares NPC notification within 72 hours: nature of breach, data subjects affected, data types exposed, measures taken, remedial actions planned; submits via NPC online portal or prescribed form | DPO | CEO | 2–4 hours |
| 6 | DPO prepares data subject notification: clear description of breach in plain language, data exposed, potential harm, mitigation steps data subjects should take, BuildRight contact for inquiries; notification via email, SMS, or website notice depending on breach scope | DPO + Legal | CMO | 2–4 hours |
| 7 | CIO directs forensic investigation: determine root cause, full scope, and whether any data was exfiltrated; engage external forensic firm if needed; preserve all logs and evidence | CIO | CEO | 1–5 days |
| 8 | Legal assesses regulatory and litigation risk: review NPC requirements, evaluate liability exposure, prepare responses to potential regulatory inquiry or customer claims | Legal | CEO | As needed |
| 9 | Affected department head implements immediate operational safeguards: e.g., if payment data breached — reset payment credentials, work with payment gateways; if employee data breached — offer credit monitoring | Dept. Head | CEO | As needed |
| 10 | DPO documents full incident in breach register: timeline, root cause, scope, notifications sent, remedial actions, resolution date; breach register retained for 5 years per NPC requirements | DPO | CEO | 2 hours |
| 11 | Post-incident: CIO and DPO conduct lessons-learned review; update security controls, access policies, and data handling procedures; implement preventive measures; schedule follow-up assessment in 30 days | CIO + DPO | CEO | 2 hours |
| 12 | Quarterly: DPO reviews breach register with CEO and Internal Audit; analyzes trends; reports aggregate breach statistics in annual privacy impact assessment | DPO | CEO | 30 min/quarter |

### System Touchpoints
- Breach register in system: incident ID, discovery date/time, classification, scope, root cause, notifications, resolution status (W53.10)
- Data access audit trail: system maintains immutable log of all access to personal data (customer records, employee records) with user ID, timestamp, and action; forensic extraction capability for breach investigation (W53.7)
- Data subject notification workflow: system generates notification list of affected data subjects from breach scope analysis; bulk email/SMS capability for notification delivery (W53.6)
- Role-based access enforcement: system enforces minimum-necessary access to personal data; access revocation capability for containment (W53.3)
- Data encryption at rest and in transit: customer and employee data encrypted in database and during transmission; encryption key management with emergency rotation capability (W53.3)
- Data Subject Access Request (DSAR) full lifecycle per RA 10173: (a) **access**: DPO acknowledges DSAR within 72 hours; system generates data package containing all personal data held for the requesting data subject (loyalty profile, transaction history, AR account data, complaint history) in machine-readable format (JSON or CSV) within 30 days; DPO reviews package for third-party data exclusion before release; (b) **rectification**: data subject requests correction of inaccurate personal data; DPO or AR Clerk updates record in system with change log; (c) **erasure / right to be forgotten**: upon verified request, DPO initiates erasure workflow — system anonymizes personal data in active records (replace name, email, phone with "ANONYMIZED-[hash]") while preserving transaction records for BIR 7-year retention requirement (transaction amounts, dates, VAT, and payment methods retained; personal identifiers removed); system flags anonymized records to prevent re-identification; for loyalty accounts with unredeemed points, DPO offers final redemption before erasure; erasure logged with request date, data subject verification method, scope of erasure, and DPO approval; (d) **data portability**: system exports data subject's personal data in structured, machine-readable format (JSON) via DPO-approved download link with 72-hour expiry; (e) **consent withdrawal**: data subject withdraws consent for marketing communications; system updates consent flag in customer master; suppresses customer from all marketing lists, email campaigns, and SMS notifications within 24 hours; transactional communications (order confirmations, warranty notifications) continue as service necessity; (f) DPO reports DSAR metrics quarterly: volume by type, average resolution time, backlog
- Integration with W41 (complaint intake as DSAR channel), W17 (loyalty data — loyalty account erasure), W24 (customer accounts — account closure with erasure), W8 (AR account closure — W8 step 12 references PII anonymization), W15/W43 (employee lifecycle — employee data erasure after 7-year retention)

### Staffing Implication
- **1 Data Protection Officer (DPO)**: required by RA 10173 for organizations processing personal data of 1,000+ individuals. BuildRight holds data for 600K+ customers and 8,000+ employees. The DPO role may be combined with Legal or Compliance but must have direct reporting to management. This is a new role recommendation (absorbed within Legal & Compliance team of ~5, expanding to ~6).
- No other incremental headcount. Breach response is a cross-functional effort by existing IT, Legal, and management.

---

## W54. LGU Business Permit Renewal per Location

| Field | Detail |
|---|---|
| **Trigger** | LGU business permit renewal calendar (typically annual, per LGU) |
| **Frequency** | Annual per location; 200 stores + 5 DCs + HQ = ~206 renewals/year, staggered across LGU calendars |
| **Volume** | ~206 locations across ~150 different LGUs (some LGUs have multiple stores); most LGUs require renewal in January–March |
| **Owner** | Legal & Compliance — Regulatory Officer |
| **Participants** | Regulatory Officer, Store Manager, DC Manager, Finance, Facilities Coordinator |

### Background

Each BuildRight Depot store and DC operates within a specific Local Government Unit (LGU — city or municipality). Each LGU requires an annual business permit (Mayor's Permit) to operate, with requirements, fees, and renewal calendars varying by LGU. Failure to maintain current permits risks closure orders, fines, and reputational damage. BuildRight's 200 stores span ~150 distinct LGUs across Luzon, Visayas, and Mindanao.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System maintains LGU permit calendar per location: renewal deadline, LGU name, LGU-specific requirements, required documents, fee schedule (based on LGU rate × estimated gross receipts), prior year permit reference | Regulatory Officer | Legal Head | 4 hours/year (setup) |
| 2 | System alerts Regulatory Officer 60 days before each location's permit renewal deadline | System | — | Automated |
| 3 | Regulatory Officer prepares renewal package per LGU requirements: (a) current year business permit, (b) SEC/DTI registration, (c) BIR registration, (d) lease contract or proof of occupancy, (e) barangay clearance, (f) fire safety inspection certificate (BFP), (g) sanitary/health permit (if applicable), (h) local business tax payment receipt, (i) authorized representative letter if not store manager filing | Regulatory Officer | Legal Head | 1–2 hours/location |
| 4 | Regulatory Officer coordinates with Store Manager: Store Manager obtains barangay clearance (requires physical visit to barangay hall), confirms fire safety inspection is current (W47 preventive maintenance — BFP annual inspection), and verifies physical signage matches registered business name | Store Manager | Regulatory Officer | 1–2 hours/location |
| 5 | Finance processes local business tax payment per LGU schedule (separate from W9a.16c LBT payment — the permit renewal requires payment first or concurrently) | Treasury Analyst | Controller | 30 min/location |
| 6 | Regulatory Officer (or designated Store Manager) submits renewal application to LGU Business Permit and Licensing Office (BPLO); many LGUs now accept online renewal via Business One-Stop Shop (BOSS) portals | Regulatory Officer / Store Manager | Legal Head | 1–4 hours/location |
| 7 | LGU processes renewal; may require inspection or hearing; issues new business permit | LGU | — | External (1–30 days) |
| 8 | Store Manager receives new permit; displays original in store (BIR and LGU requirement); sends copy to Regulatory Officer for system upload | Store Manager | Regulatory Officer | 15 min |
| 9 | Regulatory Officer uploads permit copy to system; updates location master with new permit number, issue date, and expiry date | Regulatory Officer | Legal Head | 5 min/location |
| 10 | System alerts Regulatory Officer if permit not received within 30 days of renewal deadline; escalates to Legal Head | System | — | Automated |
| 11 | Monthly: Regulatory Officer generates permit status dashboard: active, pending renewal, expired, at-risk locations; Legal Head reviews expired permits as priority escalation | Regulatory Officer | Legal Head | 1 hour/month |

### System Touchpoints
- LGU permit calendar per location with renewal deadlines, LGU-specific requirements, and document checklists (W54.1)
- Automated renewal alerts at 60, 30, and 7 days before expiry (W54.2)
- Location master integration: permit number, issue date, expiry date stored per location; active permit required for location to remain in "Operating" status (W54.9)
- Document storage: permit copies attached to location record per DOC-001 (W54.8–9)
- Permit status dashboard with expiry alerting and escalation (W54.11)
- Integration with W9a.16c (LBT payment), W47 (fire safety inspection scheduling), W16 (new store — initial permit acquisition)

### Staffing Implication
- **1 Regulatory Officer** (within Legal & Compliance): ~206 renewals/year × ~3 hours each = ~620 hours/year = ~4 days/month. Concentrated in Q1 when most LGUs require renewal. This role also manages BIR CAS registration (W54a) and regulatory inspection handling. Absorbed within Legal & Compliance team (recommend expanding from ~5 to ~6 with the DPO role in W53).
- **Store Managers**: ~2 hours/year for their location's permit renewal coordination. Absorbed.

### W54a. BIR Computerized Accounting System (CAS) Registration

| Field | Detail |
|---|---|
| **Trigger** | New entity incorporation, new ERP system deployment, major system upgrade requiring re-registration, or annual permit renewal |
| **Frequency** | Initial registration per entity (5 entities); annual renewal per BIR requirements; re-registration if system undergoes major changes |
| **Volume** | 5 entity registrations initially; 5 annual renewals thereafter |
| **Owner** | Regulatory Officer |
| **Participants** | Regulatory Officer, CIO, Controller, CFO, external ERP vendor, BIR Regional Office |

### Background

Under BIR Revenue Regulations No. 11-2018 and Revenue Memorandum Order (RMO) No. 29-2002, any business using a computerized accounting system (including ERP systems) must register the system with the BIR and obtain a CAS Permit before the system can legally generate BIR-registered receipts, invoices, and accounting records. Each of BuildRight's 5 legal entities must obtain its own CAS permit. The system must be able to produce books of accounts (general journal, general ledger, cash receipts journal, cash disbursements journal, sales journal, purchases journal) in the format prescribed by BIR.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Regulatory Officer obtains BIR CAS registration forms: BIR Form 1907 (Application for Registration of Books of Accounts), together with system documentation package | Regulatory Officer | Legal Head | 4 hours/entity |
| 2 | IT and ERP vendor prepare system documentation package per BIR requirements: (a) system overview and architecture diagram, (b) data flow diagram showing transaction processing from source to GL, (c) security and access control documentation, (d) sample outputs: BIR-registered receipt format, sales invoice, purchase invoice, journal voucher, official receipt, books of accounts (general journal, general ledger, cash receipts/disbursements journals, sales/purchases journals), (e) data retention and backup procedures, (f) audit trail documentation, (g) BIR permit application letter signed by entity's authorized representative | IT Team / ERP Vendor | CIO | 2–3 weeks/entity |
| 3 | Controller reviews and validates sample outputs for accounting accuracy: GL account mapping, journal entry formatting, books of accounts layout compliance with BIR-prescribed format | Controller | CFO | 4 hours/entity |
| 4 | Regulatory Officer submits CAS registration application to BIR Regional Office (or Revenue District Office) where the entity is registered; pays registration fee per BIR schedule | Regulatory Officer | Legal Head | 1 day/entity |
| 5 | BIR evaluates application; may conduct system demonstration or on-site inspection at BuildRight office; IT and Finance present system capabilities to BIR evaluators | BIR / IT / Finance | CFO | 1–2 days/entity (if inspection required) |
| 6 | BIR issues CAS Permit (Authority to Use Computerized Accounting System) per entity; permit includes registered system name, entity TIN, permit number, and conditions of use | BIR | — | External (2–6 months from submission) |
| 7 | Regulatory Officer records CAS permit in system: permit number, issue date, expiry date (if applicable — some permits are perpetual unless system changes), entity TIN, authorized system name; uploads permit document to entity master | Regulatory Officer | Legal Head | 15 min/entity |
| 8 | IT configures ERP to print BIR-registered receipt/invoice numbers per CAS permit: system generates sequential, non-skippable invoice/receipt numbers per BIR requirements; TIN, registered business name, and CAS permit number printed on all receipts per BIR format | IT Team | CIO | 2–3 days/entity |
| 9 | **Annual renewal** (if required per BIR ruling): Regulatory Officer submits renewal documentation before expiry; confirms no material system changes since last registration | Regulatory Officer | Legal Head | 2 hours/entity/year |
| 10 | **Re-registration triggers**: if ERP system undergoes major version upgrade, change of ERP platform, or change of entity legal name, Regulatory Officer files amended CAS registration with updated system documentation | Regulatory Officer / IT | CFO | Per initial process |

### System Touchpoints (BIR CAS)
- CAS permit tracking in entity master: permit number, issue date, expiry date, authorized system name (W54a.7)
- BIR-compliant sequential invoice/receipt numbering: system enforces non-skippable, sequential numbering per CAS permit per entity; voided transactions retain number with void indicator per BIR requirements; system prints or records a BIR-compliant void receipt referencing the original transaction number, void reason code, and authorizing manager ID per CAS permit conditions (W54a.8)
- BIR books of accounts generation: system produces general journal, general ledger, cash receipts journal, cash disbursements journal, sales journal, and purchases journal in BIR-prescribed format (per CAS registration commitment) (W54a.2)
- Entity-level CAS permit number printed on all receipts, invoices, and official receipts alongside entity TIN (W54a.8)
- Integration with W5b (BIR-registered receipt printing), W9a (books of accounts generation for close), W16 (new entity setup — CAS registration required before entity can transact), W54 (LGU permits — Regulatory Officer manages both)

### Staffing Implication
- **Regulatory Officer**: initial registration adds ~40–60 hours across 5 entities (concentrated during ERP implementation Phase 2); annual renewals add ~10 hours/year. Absorbed within existing role.
- **IT**: system documentation preparation adds ~2–3 weeks/entity during implementation; absorbed within implementation project.
- **Controller**: sample output validation adds ~4 hours/entity during implementation; absorbed.

---

## W55. IT Disaster Recovery & System Failover

| Field | Detail |
|---|---|
| **Trigger** | Core ERP system failure exceeding RTO (4 hours per NFR-013), data center outage, cloud service disruption, or cyber attack causing system unavailability |
| **Frequency** | Rare; estimated 0–2 DR events/year requiring failover |
| **Volume** | Affects all 8,050 users; 1,000 POS terminals; 200 stores; 5 DCs |
| **Owner** | CIO |
| **Participants** | CIO, IT Infrastructure team, IT Helpdesk, Store Ops Director, CFO, external DR service provider |

### Background

This workflow covers the IT system recovery process, distinct from W49 (typhoon/facility business continuity) which covers physical location response. NFR-013 defines: RPO ≤ 1 hour (max 1 hour of data loss), RTO ≤ 4 hours (max 4 hours of core system unavailability). POS terminals operate offline for 8+ hours per W5g.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | IT Infrastructure monitoring detects or is alerted to system failure: error rates, service health checks, connectivity loss, or user reports of system unavailability | IT Infrastructure / System | CIO | Immediate (automated detection) |
| 2 | IT Infrastructure assesses scope and severity: (a) single module failure (e.g., POS integration down), (b) full ERP outage, (c) data center / cloud region outage, (d) suspected cyber attack (ransomware, DDoS) | IT Infrastructure Lead | CIO | 15–30 min |
| 3 | CIO declares DR event if severity exceeds RTO: notifies CEO, COO, CFO; communicates estimated recovery time; Store Ops Director notifies Regional Managers and Store Managers | CIO | CEO | 15 min |
| 4 | **Stores**: continue selling in offline mode per W5g; POS transactions queue locally for upload upon recovery | Store Manager | Store Ops Director | Automated (W5g) |
| 5 | **DCs**: DC operations shift to manual processing — Receiving Clerks record goods receipts on paper/spreadsheet for batch entry upon recovery; picking and shipping suspended for non-critical orders | DC Manager | Supply Chain Manager | Manual fallback |
| 6 | **Ecommerce**: Digital Commerce platform displays maintenance notification; new orders suspended; in-progress orders held for fulfillment upon recovery | Ecom Team | CMO | 15 min |
| 7 | **Recovery execution**: IT Infrastructure initiates failover to DR site or secondary cloud region: (a) verify DR environment is current (data replication lag ≤ RPO), (b) switch DNS and network routing to DR environment, (c) validate core services: authentication, POS sync, inventory, financial posting, (d) incremental data replay from primary if replication lag exists | IT Infrastructure | CIO | 1–3 hours |
| 8 | If primary system restore (instead of failover): (a) identify root cause, (b) repair or restore from backup, (c) verify data integrity against last known good checkpoint, (d) bring services online sequentially (core first, then ancillary), (e) validate system health | IT Infrastructure | CIO | 2–4 hours |
| 9 | System restored: CIO communicates "all clear" to business; stores begin uploading offline transactions per W5g; DCs batch-enter manual receipts; ecommerce resumes order processing | CIO | CEO | 15 min |
| 10 | **Data integrity verification**: IT runs reconciliation checks: (a) offline POS transactions vs. central inventory, (b) any manual DC entries vs. expected receipts, (c) database transaction logs for completeness, (d) financial posting integrity (no partial journal entries) | IT Infrastructure + Finance | Controller | 1–2 hours |
| 11 | Post-recovery: CIO conducts root cause analysis within 5 business days; documents incident, root cause, recovery actions, data loss (if any), and preventive measures | CIO | CEO | 4 hours |
| 12 | Quarterly: IT Infrastructure conducts scheduled DR failover test during maintenance window; validates RTO and RPO targets; documents test results; updates DR runbook based on findings | IT Infrastructure | CIO | 4 hours/quarter |

### System Touchpoints
- Automated system health monitoring with configurable alerting thresholds (W55.1)
- DR environment: real-time data replication with RPO ≤ 1 hour (synchronous or near-synchronous); automated or one-click failover capability (W55.7)
- Backup integrity verification: automated checksum validation on backup files; periodic restore testing (W55.8)
- Offline POS transaction upload and reconciliation per W5g (W55.4, 10)
- Incident logging and root cause documentation (W55.11)
- DR test scheduling and results tracking (W55.12)
- DR test failure remediation: if quarterly DR test fails to meet RTO (4 hours) or RPO (1 hour) targets — (a) IT Infrastructure Lead documents the specific failure (failover latency, data replication lag, service recovery sequence, single point of failure); (b) CIO convenes emergency remediation meeting with IT Infrastructure within 5 business days; (c) remediation plan created with specific actions, responsible owners, and target completion date; (d) retest scheduled within 30 days of remediation completion; (e) if retest also fails: CIO escalates to CEO with capital investment request for infrastructure upgrade; (f) all test results (pass and fail) retained in DR test log for audit evidence; (g) External auditor may request DR test results as part of annual audit (W42.19, W55.12)
- Integration with W5g (offline POS), W48 (helpdesk incident management), W49 (physical disaster response — this workflow is system-level, W49 is facility-level)

### Staffing Implication
- No incremental headcount. DR response is executed by existing IT Infrastructure team (part of the recommended ~28–30 IT staff in W48).
- External DR service provider: if BuildRight uses a managed DR service or colocation DR site, the provider's SLA must align with BuildRight's RTO/RPO targets.

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
| 4 | System links backorder to next expected replenishment: (a) if PO already in progress (W2) with expected GR date — system shows estimated availability date, (b) if no PO exists — system flags to Supply Planner for PO creation (W2a), (c) if import item — shows import PO ETA (W2b) | System | — | Automated |
| 5 | System reserves backorder quantity against incoming PO or replenishment order (allocates to backorder before general store replenishment); backorder takes priority over routine replenishment allocation | System | — | Automated |
| 6 | Sales Associate communicates estimated availability date to customer; for trade/corporate accounts, Sales Rep manages the communication | Sales Associate / Sales Rep | — | 2 min |
| 7 | When goods are received at DC and backorder allocation is fulfilled: system routes allocated quantity to the customer's preferred store in the next replenishment wave (W4); or if customer prefers delivery, system creates home delivery order (W19) | System | Supply Planner | Automated |
| 8 | System sends customer notification (SMS/email/app): "Your item is on the way to [Store Name], expected availability [date]" | System | — | Automated |
| 9 | Item arrives at store; Stock Associate stages for customer pickup (similar to BOPIS W11); system sends "Ready for pickup" notification | Stock Associate / System | Store Manager | 5 min + automated |
| 10 | Customer picks up item; sale processed at POS (standard transaction or trade account per W5b.4c); backorder closed in system | Cashier / Customer | — | 5 min |
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

## W58. Corporate / Project Account Management

| Field | Detail |
|---|---|
| **Trigger** | Corporate account activated (W24) or new project added to existing corporate account |
| **Frequency** | ~200 active corporate accounts; ~50–100 active projects at any time |
| **Volume** | 10% of revenue (~PHP 6.2B/year); average project value PHP 1M–50M |
| **Owner** | Sales Rep (Trade & Corporate) |
| **Participants** | Sales Rep, AR Supervisor, Category Manager, Supply Planner, Store Manager, Finance Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Sales Rep onboards new corporate account post-credit approval (W24): assigns dedicated Sales Rep, default store for pickup, delivery preferences, billing contact, and project delivery schedule | Sales Rep | AR Supervisor | 2 hours/account |
| 1a | **Customer project quotation**: when a trade or corporate customer (existing or prospect) requests a materials quotation — (a) Sales Rep receives customer's materials list (bill of materials, project specifications, or verbal requirements) via email, site visit, or walk-in; (b) Sales Rep creates Quotation in system — selects SKUs, enters quantities, and selects pricing basis: standard SRP, trade discount tier, or project-specific pricing (to be negotiated); (c) system calculates line totals, applies current pricing, and shows margin per line and total; (d) Sales Prop adds delivery cost estimate using carrier rate card per delivery zone (W5d/W19); (e) Sales Rep submits quotation for Category Manager approval if discounted below standard trade discount; (f) system generates quotation document (PDF) with BuildRight letterhead, validity period (typically 30 days), quotation number, customer details, line items, pricing, delivery terms, and payment terms; (g) Sales Rep sends quotation to customer via email or provides printed copy; (h) system tracks quotation lifecycle: Draft → Submitted → Accepted → Converted to Sales Order / Expired / Rejected; (i) if customer accepts: Sales Rep converts Quotation to Sales Order with one click — system carries all line items, quantities, pricing, and delivery details to the order; if customer negotiates changes, Sales Rep creates revised quotation (versioned) and re-submits; (j) expired quotations (beyond validity period) flagged for Sales Rep follow-up or archival; (k) monthly: Sales Rep reviews quotation conversion report — win rate by customer, category, and average quotation-to-order cycle time | Sales Rep / Category Manager | VP Merchandising | 30–60 min/quotation |
| 2 | For project-based accounts: Sales Rep creates project record in system — project name, location, estimated total material requirement, project timeline (start date, phases, completion date), project manager contact, billing milestones | Sales Rep | Finance Manager | 1 hour/project |
| 3 | Category Manager sets up project-specific pricing (if negotiated): discounted price list per SKU category, validity period aligned with project timeline, minimum commitment quantity (if any) | Category Manager / Pricing Analyst | VP Merchandising | 2–4 hours/project |
| 4 | Sales Rep creates material requirement plan per project phase: estimated SKU quantities by month; system generates forward demand signal for Supply Planner to pre-position stock at the serving DC/store | Sales Rep | Supply Planner | 2–4 hours/project |
| 5 | During project: Sales Rep takes orders from corporate customer via phone, email, or site visit; creates Sales Order in system linked to project; applies project-specific pricing; arranges pickup at designated store or scheduled delivery (W19 or own fleet) | Sales Rep | Store Manager | 15–30 min/order |
| 6 | System tracks cumulative project spending vs. approved credit limit; alerts Sales Rep and AR Supervisor at 80% and 95% of project budget or credit limit | System | — | Automated |
| 7 | Monthly: Sales Rep generates project billing summary for customer: all orders delivered, quantities, amounts, remaining project budget; customer reconciles and processes payment per terms (Net 60–90) | Sales Rep | AR Supervisor | 1 hour/project/month |
| 8 | Monthly: AR Supervisor reviews corporate account aging; project accounts with payments > 60 days overdue escalated to Finance Manager for collection action per W8.7–8 | AR Supervisor | Finance Manager | Part of W8 |
| 9 | Upon project completion: Sales Rep closes project record; system generates final project summary (total revenue, margin, items purchased, variance from initial estimate); AR Supervisor confirms all invoices settled | Sales Rep / AR Supervisor | Finance Manager | 1 hour/project |
| 10 | Quarterly: Sales Rep and Category Manager review corporate account portfolio: account profitability, project win rate, competitive positioning, upsell opportunities | Sales Rep + Category Manager | VP Merchandising | 4 hours/quarter |

> **Billing model note**: the workflow above uses monthly billing summaries as the standard billing method for corporate/project accounts, which is a deliberate simplification aligned with BuildRight's retail-oriented billing cycle. For large construction projects where customers require milestone-based or progress billing (e.g., foundation, framing, finishing phases), Sales Rep structures the project into billing milestones during W58 step 2 — each milestone has a target date and estimated value; system generates a milestone invoice when Sales Rep confirms milestone completion; retention amounts (standard 10% in Philippine construction practice) may be configured per project if contractually required — system tracks retained amount separately from invoiced amount and releases retention upon project completion sign-off; architect/engineer progress certification, if required, is captured as an approval step before milestone invoice generation; project change orders are processed as adjustments to the project record with Category Manager approval, updating the material requirement plan and billing milestones accordingly

### System Touchpoints
- Corporate account master with project sub-accounts, project-specific pricing, and delivery preferences (W58.1–3)
- Quotation management: quotation creation with SKU selection and pricing; margin visibility per line; Category Manager approval for below-standard pricing; quotation document generation (PDF) with validity period; quotation lifecycle tracking (Draft → Submitted → Accepted → Converted / Expired / Rejected); one-click conversion from Quotation to Sales Order; versioned revisions; quotation conversion analytics (win rate, cycle time, by customer and category) (W58.1a)
- Project record with timeline, material requirements, and billing milestones (W58.2)
- Project-specific pricing linked to POS (W5b.4c) and Sales Order entry (W58.3, 5)
- Cumulative project spending and budget tracking with automated alerts (W58.6)
- Project billing summary generation (W58.7)
- Project close-out with financial summary (W58.9)
- Corporate account portfolio analytics (W58.10)
- Integration with W5b.4c (corporate pricing at POS), W8 (AR and collections), W19 (delivery), W24 (credit application), W56 (backorder priority for corporate accounts)

### Staffing Implication
- **3–4 Sales Reps (Trade & Corporate)**: 200 corporate accounts ÷ 3–4 reps = ~50–70 accounts each. With ~50–100 active projects, each rep manages ~15–25 active projects. At ~4–6 hours/project/month for order management and billing = ~60–150 hours/month. 3–4 dedicated trade/corporate Sales Reps can manage this within the Store Operations team or as a separate B2B sales team under the CMO.

---

## W59. Insurance Policy Lifecycle Management

| Field | Detail |
|---|---|
| **Trigger** | Annual insurance renewal cycle; or new insurance requirement (new store, new asset, regulatory change) |
| **Frequency** | Annual renewals; ~20–30 active policies across the group |
| **Volume** | Policy types: property (200 stores + 5 DCs), inventory (PHP 8–10B total), business interruption, general liability, vehicle fleet (30–40 owned), workers' compensation, employer's liability, cargo/in-transit, cyber liability, directors & officers (D&O) |
| **Owner** | Treasury Analyst (policy administration); CFO (coverage decisions) |
| **Participants** | Treasury Analyst, CFO, Facilities Coordinator, Fleet Manager, IT, Legal, external insurance broker |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System maintains insurance policy register: policy number, insurer, type, coverage amount, premium, deductible, renewal date, key terms and exclusions, broker contact | Treasury Analyst | CFO | 4 hours/year (maintenance) |
| 2 | System alerts Treasury Analyst 90 days before each policy renewal date | System | — | Automated |
| 3 | Treasury Analyst coordinates with insurance broker to obtain renewal quotation and market comparison; broker provides at least 2 alternative quotes for material policies (annual premium > PHP 500K) | Treasury Analyst | CFO | 1–2 hours/policy |
| 4 | CFO reviews coverage adequacy annually: (a) property coverage vs. current replacement cost of stores and DCs, (b) inventory coverage vs. current inventory value, (c) fleet coverage vs. current vehicle count, (d) business interruption coverage vs. current revenue run rate, (e) cyber liability adequacy given data volumes | CFO | CEO | 2–4 hours/year |
| 5 | CFO approves or adjusts coverage; authorizes Treasury Analyst to renew or switch insurer | CFO | CEO | 1 hour |
| 6 | Treasury Analyst processes premium payment per W7c (non-PO invoice) or against insurance broker PO; system posts premium to GL (Dr. Prepaid Insurance / Cr. Cash); monthly amortization per W9a step 8 | Treasury Analyst | CFO | 15 min/policy |
| 7 | Claims: when an insured event occurs (W3.6a goods damage, W49 typhoon damage, W37 confirmed theft, W52 vehicle accident), the process owner files claim with supporting documentation; Treasury Analyst tracks claim status in system; upon settlement, Finance posts recovery (Dr. Cash / Cr. Insurance Recovery Income or Cr. relevant asset/expense account) | Process Owner / Treasury Analyst | CFO | Per event |
| 8 | Monthly: Treasury Analyst reviews claims activity report: open claims, settlement status, claims vs. premiums ratio; flags policies where claims experience may affect renewal terms | Treasury Analyst | CFO | 30 min/month |
| 9 | Annual: CFO and external broker review claims history, coverage adequacy, and market conditions; adjust policy structure for upcoming year | CFO + Broker | CEO | 2 hours/year |

### System Touchpoints
- Insurance policy register with renewal calendar, coverage details, and document storage (W59.1)
- Automated renewal alerting at 90, 60, and 30 days (W59.2)
- Claims tracking with status lifecycle: Filed → Under Investigation → Approved → Settled / Denied; linked to triggering event (W3.6a, W49, W37) (W59.7)
- Premium payment processing and prepaid insurance amortization (W59.6)
- Claims vs. premium ratio reporting (W59.8)
- Integration with W3.6a (receiving damage), W25 (petty cash for minor incidents below deductible), W37 (theft write-off), W39 (asset disposal — insurance recovery on disposed assets), W47 (facility damage), W49 (disaster damage), W52 (vehicle insurance)

### Staffing Implication
- **Treasury Analyst**: adds ~4–6 hours/year for policy administration + ~30 min/month for claims review. Absorbed within existing Treasury team (2–3 analysts).
- **Insurance broker**: external partner managing market comparison, policy placement, and claims advocacy.

---

## W60. Emergency Procurement

| Field | Detail |
|---|---|
| **Trigger** | Urgent operational need that cannot wait for standard PO cycle (W2) and exceeds petty cash threshold (W25): critical equipment breakdown, emergency facility repair, urgent compliance requirement, sudden supply shortage threatening store operations |
| **Frequency** | ~20–30 emergency procurement events/month across all locations |
| **Volume** | PHP 50,000–500,000 per event; typically for emergency equipment, parts, or services |
| **Owner** | Requestor (Store Manager or Department Head) |
| **Participants** | Store Manager / Dept. Head, Procurement (Buyer), Finance (Controller), Vendor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Requestor identifies emergency need and justifies urgency: equipment failure impacting store operations (e.g., POS server failure, HVAC breakdown in peak summer, forklift failure at DC), compliance deadline (regulatory order), or supply emergency (critical stockout on A-item with no PO coverage) | Store Manager / Dept. Head | — | 10 min |
| 2 | Requestor submits emergency procurement request in system: item/service description, estimated cost, urgency justification, required delivery date (typically same day or next day), preferred vendor (if known) | Requestor | — | 10 min |
| 3 | System routes for expedited approval: (a) ≤ PHP 100,000: Store Manager (for stores) or Dept. Head (for HQ/DC) + Controller verbal approval, (b) PHP 100,001–500,000: CFO verbal approval required within 2 hours, (c) > PHP 500,000: CEO verbal approval required within 4 hours; system logs verbal approval with timestamp and approver ID | System | Controller / CFO / CEO | 15 min – 4 hours |
| 4 | Buyer (or Requestor for store-level purchases) contacts vendor immediately — phone call or direct purchase authorized; system allows "confirm vendor later" mode where PO is created with vendor TBD and updated after the fact | Buyer / Requestor | Category Manager | 15–30 min |
| 5 | Goods or services received immediately; standard Goods Receipt (W3) or service confirmation documented | Receiving Clerk / Requestor | Dept. Head | Per W3 |
| 6 | Within 5 business days: Buyer or AP Clerk completes documentation — formalize PO in system (if created informally), obtain vendor invoice, process 3-way match (W7) or 2-way match for services; system enforces that all emergency procurements are regularized within 5 days or escalates to Controller | Buyer / AP Clerk | Controller | 15–30 min |
| 7 | Monthly: Controller reviews emergency procurement report: total spend, frequency by location, category, and requester; flags locations or categories with excessive emergency procurement frequency for root cause analysis (supplier reliability issues, planning gaps, or maintenance neglect) | Controller | CFO | 1 hour/month |

### System Touchpoints
- Emergency procurement request form with urgency justification field (W60.2)
- Expedited approval workflow with verbal approval logging and configurable SLA timers (W60.3)
- "Vendor TBD" PO creation mode for immediate procurement with post-hoc vendor assignment (W60.4)
- Regularization enforcement: system tracks emergency procurements not yet formalized; auto-escalates at day 5 (W60.6)
- Emergency procurement analytics: spend, frequency, category, location, root cause (W60.7)
- Integration with W2 (standard PO — this is the expedited alternative), W3 (goods receipt), W7 (AP matching), W21 (capex — if emergency need is actually capex, route to W21 expedited path), W25 (petty cash — for amounts ≤ PHP 50K), W47 (facility emergency repair), W48 (IT emergency equipment)

### Staffing Implication
- No incremental headcount. Emergency procurement is absorbed by existing Buyers, Store Managers, and AP Clerks.
- The monthly review by Controller adds ~1 hour/month — absorbed.

---

## W61. Competitor Price Match Process

| Field | Detail |
|---|---|
| **Trigger** | Customer requests price match at POS based on competitor's current advertised price |
| **Frequency** | ~50–100 price match requests/day chain-wide; ~2–5 per store per week |
| **Volume** | Primarily on high-visibility items (power tools, paint, appliances, tiles) where customers actively compare prices |
| **Owner** | Cashier (execution); Store Manager (authorization) |
| **Participants** | Cashier, Store Manager, Pricing Analyst (review) |

### Price Match Policy Rules

| Rule | Detail |
|---|---|
| **Eligible competitors** | Named competitors with physical stores or authorized online retailers within the same city/province; excludes marketplace sellers (Shopee, Lazada individual sellers), auction sites, and clearance/closeout sales |
| **Proof required** | Current printed advertisement, competitor website screenshot (with date visible), or competitor physical catalog; Cashier visually verifies proof |
| **Matching scope** | Match applies to identical item (same brand, model, size, color); does not apply to bundles, limited-quantity offers, or membership-only pricing |
| **Price match limit** | Price matched to competitor's price; will not go below BuildRight's cost (WAC) unless authorized by Category Manager |
| **Frequency limit** | Max 3 identical items per price match request per customer per day |
| **Exclusions** | Installation services, delivery fees, gift cards, special orders (W38), clearance items (W13.9a) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer requests price match at checkout; presents competitor price proof (ad, screenshot, catalog) | Customer | — | — |
| 2 | Cashier verifies eligibility per policy rules: (a) competitor is on eligible list, (b) item is identical (brand, model, size), (c) proof is current (within 7 days), (d) quantity within limit | Cashier | — | 2 min |
| 3 | Cashier enters price override in POS with reason code "Competitor Price Match"; system prompts for competitor name and matched price; if override > 10% or > PHP 500: manager authorization required per W5b.4a | Cashier | Store Manager | 1 min |
| 4 | If matched price is below BuildRight's cost (WAC): system blocks override and alerts Store Manager; Store Manager contacts Category Manager for authorization; Category Manager may approve as strategic decision (customer retention, competitive response) with written justification in system | Store Manager / Category Manager | VP Merchandising | 5–10 min |
| 5 | System records price match transaction: original price, matched price, competitor name, cashier ID, authorizer ID, item, quantity, and reason code (W5b.4a audit trail) | System | — | Automated |
| 6 | Weekly: Pricing Analyst reviews price match report: frequency by SKU, competitor, and store; identifies items with high price match frequency (> 5 requests/week) for potential SRP adjustment (W40) or competitive response strategy | Pricing Analyst | Category Manager | 1 hour/week |

### System Touchpoints
- Price match reason code in POS price override workflow with competitor name capture (W61.3, W5b.4a)
- System enforces WAC floor price — blocks price match below cost without Category Manager override (W61.4)
- Price match analytics: frequency by SKU, competitor, store, and margin impact (W61.6)
- Eligible competitor list maintained by Pricing Analyst in system (configurable per region if needed) (W61 policy rules)
- Integration with W5b.4a (price override), W40 (potential SRP adjustment triggered by price match frequency)

### Staffing Implication
- No incremental headcount. Price match adds ~2 min to occasional POS transactions. Weekly review by Pricing Analyst adds ~1 hour/week — absorbed within existing Pricing Analyst duties (team of 3).

---

## W62. Vendor Contract Lifecycle (Non-PO Contracts)

| Field | Detail |
|---|---|
| **Trigger** | New service vendor engagement, contract renewal, or contract modification |
| **Frequency** | ~100–200 active service contracts at any time (IT services, cleaning, security, pest control, elevator maintenance, waste disposal, equipment leases, carrier contracts, banking services, professional services) |
| **Volume** | Peaks during annual budget cycle (W26) when contracts are reviewed and renewed |
| **Owner** | Requesting Department Head |
| **Participants** | Dept. Head, Procurement/Buyer, Finance, Legal, Vendor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Department Head identifies need for vendor service contract (new vendor, renewal, or replacement); defines scope of work, service level requirements, and budget | Dept. Head | VP / C-Suite | 1–2 hours |
| 2 | Buyer or Dept. Head solicits quotations from 3 vendors (or 2 for specialized services); evaluates on: price, capability, references, compliance (business permits, tax compliance, insurance coverage) | Buyer / Dept. Head | Dept. Head | 2–4 hours |
| 3 | Legal reviews contract terms: liability, termination clause, data privacy (RA 10173 compliance for vendors handling personal data), intellectual property, dispute resolution | Legal | Legal Head | 1–2 hours/contract |
| 4 | Approval per tiered matrix: (a) annual value ≤ PHP 500K: Dept. Head + Finance Manager, (b) PHP 500K–2M: VP + CFO, (c) > PHP 2M: CEO | Approver | Approver | 15–30 min |
| 5 | System creates vendor contract record: vendor, contract type, scope, start/end dates, value, payment terms, SLA terms, auto-renewal flag, document attachments (signed contract, vendor permits, insurance certificates) | Buyer / Dept. Head | Dept. Head | 15–30 min |
| 6 | System alerts Dept. Head 90 days before contract expiry for renewal decision; alerts 30 days before vendor insurance or permit expiry within contract period | System | — | Automated |
| 7 | Monthly: Dept. Head reviews vendor service performance against SLA terms; documents issues; escalates to Buyer or Legal for resolution | Dept. Head | VP / C-Suite | 30 min/vendor/month |
| 8 | Contract renewal: Dept. Head decides to (a) renew at existing terms, (b) renegotiate (repeat steps 2–4), or (c) terminate and re-bid; system blocks vendor invoices after contract expiry if not renewed | Dept. Head | VP / C-Suite | Per contract |
| 9 | Contract termination: Dept. Head provides notice per contract terms; coordinates vendor exit (return of company property, data deletion per RA 10173, final payment); system closes contract record and blocks future invoices | Dept. Head / Legal | VP / C-Suite | 1–2 hours |

### System Touchpoints
- Vendor contract register with full lifecycle: Draft → Active → Renewal Pending → Renewed / Terminated (W62.5, 8–9)
- Contract document storage with expiry alerting for contract, vendor permits, and insurance certificates (W62.6)
- SLA tracking with performance documentation per review period (W62.7)
- Auto-renewal management: system flags auto-renewal contracts 90 days before renewal for Dept. Head decision (W62.6)
- Invoice blocking after contract expiry (W62.8)
- Integration with W2c (blanket/contract POs for merchandise vendors), W7c (non-PO invoice processing), W36 (vendor onboarding), W44 (vendor performance review — service vendors included in annual review), W59 (insurance tracking for vendor insurance certificates)

### Staffing Implication
- No incremental headcount. Contract management is distributed across Department Heads as part of their operational responsibility. Legal reviews add ~1–2 hours/contract — absorbed within Legal team.

### W62b. 3PL / Delivery Partner Onboarding & Offboarding

| Field | Detail |
|---|---|
| **Trigger** | New delivery partner identified (new service area, capacity expansion, carrier diversification); or existing partner termination (performance failure, contract expiry, business exit) |
| **Frequency** | ~5–10 new partner evaluations/year; ~2–3 offboardings/year |
| **Volume** | Active partners: ~5–10 delivery partners (Lalamove, Transportify, own fleet surrogates, regional carriers, inter-island shipping lines) |
| **Owner** | Fleet Manager / DC Dispatch Supervisor |
| **Participants** | Fleet Manager, DC Dispatch, IT (API integration), Finance, Legal |

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Fleet Manager or DC Dispatch identifies need for new delivery partner: coverage gap, capacity constraint, cost benchmarking, or service quality issue with existing partner | Fleet Manager | Supply Chain Manager | 30 min |
| 2 | Fleet Manager solicits proposals from 2–3 candidate partners; evaluates on: delivery coverage (zones, islands), rate card per zone/weight/tier, SLA terms (on-time %, damage rate), API integration capability (order creation, tracking, proof of delivery), insurance coverage, business permits, tax compliance | Fleet Manager | Supply Chain Manager | 4–8 hours |
| 3 | IT evaluates API integration feasibility: order creation, real-time tracking, proof of delivery capture, webhook/callback for status updates; estimates integration timeline and cost | IT Team | CIO | 4 hours |
| 4 | Legal reviews contract terms: liability for lost/damaged goods, data privacy (RA 10173 — delivery partner may access customer name, phone, address), insurance requirements, termination clause | Legal | Legal Head | 1–2 hours |
| 5 | Approval per W62 tiered matrix (carrier contracts typically annual value ≤ PHP 2M → VP + CFO; > PHP 2M → CEO) | Approver | Approver | 15–30 min |
| 6 | IT configures API integration in staging environment; conducts integration testing with carrier test environment; validates order creation, status callbacks, and proof of delivery flow; Fleet Manager and DC Dispatch conduct pilot with limited order volume for 1–2 weeks | IT Team / Fleet Manager | CIO | 1–2 weeks |
| 7 | Go-live: IT activates API integration in production; DC Dispatch adds partner to carrier selection logic; system routes orders to new partner per configured zones and rates | IT Team / Fleet Manager | Supply Chain Manager | 1 day |
| 8 | Monthly: Fleet Manager monitors new partner performance per W19.7 3PL management dashboard (on-time %, damage rate, cost per delivery, customer complaint rate); underperformance escalated per W44 vendor scorecard methodology | Fleet Manager | Supply Chain Manager | 30 min/month |
| 9 | **Offboarding**: if partner termination required (performance, contract expiry, or business decision) — Fleet Manager coordinates with DC Dispatch to redirect order volume to alternative partners; IT deactivates API integration; system removes partner from carrier selection; Finance settles outstanding carrier invoices; Legal confirms data deletion per RA 10173 (partner must delete customer data collected during service); system archives partner record with termination date, reason, and performance history | Fleet Manager / IT / Finance / Legal | Supply Chain Manager | 1–2 weeks |

### System Touchpoints (3PL Partners)
- Carrier master record with rate cards per zone/weight/tier, SLA terms, API credentials, insurance details, and integration status (W62b.2, W62b.7)
- API integration: order creation, real-time tracking, status callbacks, proof of delivery capture (W62b.3, W62b.6)
- Carrier selection logic: automated carrier assignment by delivery zone, package weight, and cost (W62b.7)
- Pilot order routing and monitoring dashboard (W62b.6)
- Performance monitoring integrated into W19 3PL management dashboard and W44 vendor scorecard (W62b.8)
- Partner deactivation: API disconnect, carrier removal, data deletion confirmation (W62b.9)
- Carrier rate card maintenance: Fleet Manager receives rate change notification from carrier (quarterly or annual update); enters updated rate card per zone/weight/tier in carrier master record; Finance Manager approves rate card changes before activation (validates against contracted rates and budget impact); system stores rate card history with effective dates for audit trail; auto-calculated delivery fees in W5d and W19 use the currently active rate card; rate card changes effective on configured date — orders already in transit use the rate card active at time of order creation (W62b)
- Integration with W19 (home delivery), W52 (fleet), W44 (vendor scorecard), W62 (non-PO contracts)

### Staffing Implication (3PL Partners)
- **Fleet Manager**: absorbs 3PL partner management within existing role; ~5–10 evaluations/year × 4–8 hours = ~20–80 hours/year; ~30 min/month ongoing monitoring per partner.
- **IT**: API integration setup ~1–2 weeks per new partner; absorbed within existing IT team.
- No incremental headcount.

---

## W63. Shelf Label & Price Tag Distribution

| Field | Detail |
|---|---|
| **Trigger** | Price change batch approved (W40 step 5) or promotional pricing approved (W13 step 3) |
| **Frequency** | Price changes: ~2–3 batches/week; Promotional: 6 major events/year + 12 monthly hot deals |
| **Volume** | ~200–500 SKUs per price change batch × 200 stores = ~40,000–100,000 shelf labels per batch; promotional batches may be larger |
| **Owner** | Pricing Analyst (generation); Store Manager (execution) |
| **Participants** | Pricing Analyst, IT, Store Manager, Department Supervisors, Stock Associates |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | After price change approval (W40 step 5) or promo approval (W13 step 3), system generates shelf label print file: SKU, old price, new price, effective date, store assignment, aisle/shelf location (if location master populated) | System | — | Automated |
| 2 | System transmits print file to centralized label printer at HQ or to store-level label printers (if equipped); labels printed per store with store identifier, SKU barcode, item description, and new SRP | System / IT | IT Team | 15–30 min/batch (centralized) or 10 min/store (local) |
| 3 | If centralized printing: HQ packages labels by store; ships to stores via next available DC delivery truck (W4) with clear labeling by department and effective date | Stock Associate (HQ) | Store Ops Director | 1–2 hours/batch |
| 4 | Store Manager or Dept. Supervisor receives labels; sorts by department; assigns Stock Associates to apply labels before store opening on effective date | Dept. Supervisor | Store Manager | 15 min |
| 5 | Stock Associates walk aisles with label batch; match labels to shelf items by barcode or location; replace old labels with new; remove old labels from shelf edge | Stock Associate | Dept. Supervisor | 30–60 min/batch |
| 6 | Department Supervisor spot-checks label accuracy on effective date: scan 10–20 random items per department with RF gun; verify displayed price matches system price | Dept. Supervisor | Store Manager | 15 min |
| 7 | If discrepancy found: Dept. Supervisor immediately corrects label and reports root cause (missed label in batch, wrong location, system vs. print mismatch) | Dept. Supervisor | Store Manager | 5 min/correction |
| 8 | For electronic shelf labels (ESL) — if deployed at select stores: system pushes price changes to ESL devices overnight; Dept. Supervisor verifies ESL display matches system price during opening walkthrough (W5a step 2); no physical label handling required | System / Dept. Supervisor | Store Manager | Automated + 5 min verification |

### System Touchpoints
- Automated shelf label print file generation from approved price changes with store/location assignment (W63.1)
- Centralized or store-level label printing with barcode, description, and SRP (W63.2)
- Label shipment tracking if centralized (W63.3)
- Label verification via RF gun barcode scan against system price (W63.6)
- Electronic shelf label (ESL) integration for stores with ESL hardware (W63.8)
- Catch-weight / variable measure item shelf labels: for items sold by weight, length, or board foot (lumber, wire, bulk nails), shelf labels display unit pricing (e.g., "PHP 85.00 per board foot", "PHP 45.00 per linear meter", "PHP 350.00 per kilogram") rather than a fixed SRP; label includes the unit of measure, unit price, and a note "Price varies by actual measure"; system generates catch-weight labels from item master pricing per unit of measure; at POS (W5b.2), Sales Associate measures/weighs actual quantity and system calculates price = unit price × actual quantity; integration with W5b (POS catch-weight selling) and W40 (price changes — unit price updates reflected on catch-weight labels)
- Integration with W5a (opening — label application done before opening), W13 (promo labels), W40 (regular price changes)

### Staffing Implication
- **Stock Associates**: label application adds ~30–60 min per price change batch. With ~2–3 batches/week, this is ~1–3 hours/week. Absorbed within existing Stock Associate duties (3 per store), typically done during early morning before store opens.
- **Pricing Analyst**: print file generation adds ~15 min/batch. Absorbed.
- For centralized printing: 1 Stock Associate at HQ handles packaging and shipping. Absorbed.

---

## W64. New Product Pilot / Store Test

| Field | Detail |
|---|---|
| **Trigger** | Buyer or Category Manager proposes new SKU for chain-wide rollout but wants to validate demand before committing to full distribution |
| **Frequency** | ~20–30 product pilots/year |
| **Volume** | Typically 5–20 SKUs per pilot; tested in 10–20 stores for 4–8 weeks |
| **Owner** | Category Manager |
| **Participants** | Category Manager, Buyer, Pricing Analyst, Supply Planner, Store Managers (pilot stores) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Category Manager identifies new SKU for pilot testing; defines hypothesis: target customer segment, expected sell-through rate, margin target, shelf space requirement, and success criteria (units/week/store above threshold) | Category Manager | VP Merchandising | 1–2 hours/pilot |
| 2 | Category Manager selects pilot stores: criteria include (a) representative mix of store sizes and locations, (b) region diversity (Luzon/Visayas/Mindanao), (c) store manager capability and willingness, (d) existing demand for similar items in the category | Category Manager | VP Merchandising | 1 hour/pilot |
| 3 | Buyer sources pilot quantity from vendor (may negotiate consignment or vendor-funded trial terms); Merchandise Planner creates SKU in item master with "Pilot" status flag | Buyer / Merchandise Planner | Category Manager | Per W2/W1 |
| 4 | Supply Planner allocates pilot stock to selected stores only; system restricts SKU visibility and ordering to pilot stores (non-pilot stores cannot see or order the item during pilot phase) | Supply Planner | Supply Planning Manager | 30 min/pilot |
| 5 | Store Managers at pilot stores receive pilot communication: product details, target customer, shelf placement recommendation, any special handling instructions | Category Manager | Store Managers | 15 min/store |
| 6 | During pilot (4–8 weeks): Pricing Analyst monitors weekly sell-through per pilot store; compares to success criteria and to similar items in the category; tracks customer feedback via Sales Associates and loyalty data | Pricing Analyst | Category Manager | 30 min/week |
| 7 | At pilot conclusion: Category Manager conducts go/no-go review with Buyer and Pricing Analyst: (a) **Go** — meets or exceeds success criteria; proceed with chain-wide rollout (add to assortment per W1, create standard replenishment parameters per W31), (b) **No-Go** — fails to meet criteria; discontinue item; disposition remaining stock per W13.9a/b (clearance/RTV), (c) **Conditional Go** — meets some criteria; extend pilot or modify (adjust price, change assortment depth, restrict to specific store formats) | Category Manager | VP Merchandising | 2 hours/pilot |
| 8 | If Go: Merchandise Planner removes "Pilot" status flag; assigns standard replenishment parameters (ROP, safety stock, order multiple); adds SKU to standard assortment for all stores; Supply Planner plans chain-wide distribution | Merchandise Planner / Supply Planner | Category Manager | 2–4 hours |
| 9 | Post-rollout: Category Manager monitors chain-wide performance for 2–3 months; compares to pilot results; validates that pilot learnings scale | Category Manager | VP Merchandising | 30 min/month |

### System Touchpoints
- Item master "Pilot" status flag that restricts visibility and ordering to designated pilot stores (W64.3–4)
- Pilot store selection and assignment in system (W64.2)
- Pilot sell-through dashboard: weekly velocity per store vs. success criteria vs. category benchmark (W64.6)
- Pilot status removal and chain-wide assortment activation (W64.8)
- Integration with W1 (assortment management), W2 (PO for pilot stock), W13 (clearance if no-go), W31 (replenishment parameter setup for chain-wide rollout)

### Staffing Implication
- No incremental headcount. Pilot management is absorbed by existing Category Managers, Buyers, and Pricing Analysts as part of their assortment duties (W1). ~20–30 pilots/year × ~4 hours each = ~80–120 hours/year spread across 5 Category Managers = ~20 hours each/year.

---

## W65. Customer Satisfaction Measurement

| Field | Detail |
|---|---|
| **Trigger** | Ongoing measurement program; continuous collection and periodic review |
| **Frequency** | Continuous survey collection; monthly reporting; quarterly deep analysis |
| **Volume** | Target: ~5,000–10,000 survey responses/month (from ~2.8M POS transactions ≈ 0.2–0.4% response rate) |
| **Owner** | Marketing — CS Manager |
| **Participants** | CS Manager, Store Ops Director, Store Managers, BI Analyst |

### Measurement Methods

| Method | Frequency | Sample | Channel |
|---|---|---|---|
| **POS receipt survey** | Continuous | Every transaction (opt-in) | QR code printed on every receipt linking to 3-question mobile survey; incentivized with 50 loyalty points per completed survey |
| **Post-visit email** | Continuous | Loyalty members who made a purchase | Automated email 24 hours after purchase with 5-question NPS-style survey |
| **Ecommerce post-order survey** | Continuous | All completed ecommerce orders | Automated email after delivery confirmation with product and delivery satisfaction rating |
| **Mystery shopping** | Quarterly | 20–30 stores per quarter (rotating) | External mystery shopping agency evaluates store experience against standardized checklist (greeting, product knowledge, wait time, checkout, store cleanliness) |
| **Annual customer survey** | Annual | 10,000–20,000 loyalty members | Comprehensive brand perception and satisfaction survey via email/app notification |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | CS Manager configures survey instruments in system: POS receipt QR code generation, post-visit email templates with survey link, ecommerce post-order trigger | CS Manager | CMO | 4 hours (setup) + 1 hour/quarter (maintenance) |
| 2 | System collects survey responses continuously: POS receipt scans, email click-throughs, ecommerce ratings; all responses linked to transaction and store (where applicable) | System | — | Automated |
| 3 | System calculates monthly CSAT score (1–5 scale) and NPS (0–10 scale → % Promoters − % Detractors) per store and chain-wide | System | — | Automated |
| 4 | Monthly: CS Manager generates CSAT/NPS dashboard: scores by store, by department, trend vs. prior month and vs. target (≥ 85% CSAT per profile §12.3); flags stores below threshold for Store Manager attention | CS Manager | Store Ops Director | 1 hour/month |
| 5 | Monthly: Store Ops Director reviews CSAT/NPS scores in management committee meeting (W35 step 14); bottom 10 stores flagged for improvement action plans | Store Ops Director | COO | 30 min/month |
| 6 | Quarterly: CS Manager presents comprehensive satisfaction analysis: trends, root causes of low scores, complaint correlation (W41), mystery shopping findings; recommends specific improvement actions | CS Manager | CMO | 2 hours/quarter |
| 7 | Mystery shopping results: CS Manager shares individual store reports with Store Managers; Store Manager develops corrective action for identified gaps; results factored into Store Manager performance evaluation | CS Manager / Store Manager | Store Ops Director | Per quarter |

### System Touchpoints
- Survey platform integration: POS receipt QR code, email survey, ecommerce post-order survey; all feeding into centralized CSAT/NPS dashboard (W65.2)
- Survey response linked to transaction number, store, and customer account (where identifiable) for drill-down analysis (W65.2)
- CSAT/NPS calculation and trending per store, region, and chain-wide (W65.3–4)
- Mystery shopping results entry and reporting (W65.7)
- Integration with W5b (POS receipt printing — QR code), W17 (loyalty points incentive for survey completion), W35 (management reporting), W41 (complaint correlation — low CSAT stores often correlate with high complaint volume)

### Staffing Implication
- No incremental headcount. Survey management adds ~2–3 hours/month to CS Manager duties. Mystery shopping costs ~PHP 100–150K/quarter (external agency) — budgeted within Marketing operations.
- **BI Analyst**: adds ~1 hour/month for CSAT/NPS data analysis and dashboard maintenance. Absorbed.

---

## W66. Inter-Island Logistics & Freight Management

| Field | Detail |
|---|---|
| **Trigger** | Inter-DC transfer (W22) between islands (e.g., DC3 Luzon → DC2 Visayas, DC1 Mindanao → DC2 Visayas), or direct-to-store delivery to island locations not served by a DC on the same island |
| **Frequency** | ~10–15 inter-island shipments/month (supplementing ~30–40 inter-DC transfers/month in W22); additional ad-hoc shipments during peak season and disaster response (W49) |
| **Volume** | Typically 1–5 TEU containers per shipment; some loose cargo (LCL) for smaller transfers |
| **Owner** | Import Coordinator / Fleet Manager |
| **Participants** | Import Coordinator, Fleet Manager, DC Supervisor, Supply Planner, carrier (ro-ro or cargo vessel), Customs (if applicable) |

### Background

BuildRight's 5-DC footprint spans the Philippine archipelago: DC1 Davao (Mindanao), DC2 Cebu (Visayas), DC3 Laguna (South Luzon), DC4 Clark (North/Central Luzon), DC5 Manila (NCR). Inter-DC transfers between islands require sea transport via roll-on/roll-off (ro-ro) ferries or containerized cargo vessels. Lead times are 3–7 days longer than same-island transfers. Cost per TEU for inter-island shipping: ~PHP 20,000–50,000 depending on route and carrier.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Supply Planner identifies need for inter-island transfer (W22) when demand at a DC cannot be met from same-island supply and vendor PO lead time is too long; or when seasonal inventory rebalancing requires inter-island movement | Supply Planner | Supply Planning Manager | Per W22 |
| 2 | Import Coordinator or Fleet Manager selects inter-island carrier and route: (a) **ro-ro ferry** — for truck-loaded cargo; vehicle driven onto ferry; 12–36 hours transit; routes: Manila→Cebu, Cebu→Davao, Manila→Davao (via Matnog); (b) **container vessel** — for containerized cargo; 3–7 days transit depending on route and vessel schedule; (c) **LCL consolidator** — for small transfers that don't fill a container | Import Coordinator / Fleet Manager | Supply Chain Manager | 1–2 hours/shipment |
| 3 | System creates Transfer Order per W22 with "Inter-Island" transport mode flag; extended lead time applied (3–7 days vs. 1–3 days for same-island); in-transit insurance coverage confirmed per W59 (cargo/in-transit policy) | Supply Planner | Supply Planning Manager | Per W22 |
| 4 | Source DC picks and loads goods; for container shipments: DC packs into container and seals; for ro-ro: goods loaded on owned or 3PL truck | DC Team | DC Supervisor | Per W3/W4 |
| 5 | Import Coordinator books shipment with carrier; provides container number or truck plate number, commodity description, and destination DC; receives booking confirmation and estimated arrival date | Import Coordinator | Fleet Manager | 30 min/shipment |
| 6 | In-transit tracking: Import Coordinator monitors shipment status via carrier tracking or direct communication; updates system ETA; for ro-ro: monitors ferry schedule (weather delays common during typhoon season — W49) | Import Coordinator | Supply Chain Manager | 15 min/day per shipment |
| 7 | Goods arrive at destination port/DC; destination DC receives and processes Goods Receipt per W22 step 7; system records inter-island freight cost allocation to transferred inventory | Receiving Clerk (DC) | DC Supervisor | Per W22 |
| 8 | System allocates inter-island freight cost to transferred items: freight cost ÷ total transferred value × per-item value added to destination inventory cost (similar to landed cost allocation in W2b.12 but for domestic inter-island movement) | System | Finance | Automated |
| 9 | Monthly: Import Coordinator and Fleet Manager review inter-island logistics cost and performance: cost per TEU by route, on-time delivery %, damage rate, carrier comparison; recommends route or carrier optimization | Import Coordinator / Fleet Manager | Supply Chain Manager | 1 hour/month |

### System Touchpoints
- Inter-island transfer order with extended lead time and transport mode flag (W66.3)
- Carrier booking integration or manual booking reference capture (W66.5)
- In-transit tracking with ETA updates (W66.6)
- Freight cost allocation to transferred inventory (W66.8)
- Inter-island logistics cost and performance reporting by route and carrier (W66.9)
- Integration with W22 (inter-DC transfers — this is the inter-island variant), W2b (import logistics — similar carrier booking process), W49 (typhoon season — ferry disruptions), W52 (fleet — owned vehicles on ro-ro), W59 (cargo insurance)

### Staffing Implication
- **Import Coordinator**: absorbs inter-island coordination as an extension of existing import logistics duties. ~10–15 shipments/month × ~2 hours each = ~20–30 hours/month. Manageable given the Import Coordinator's existing workload managing ~20–30 import POs/month (W2b), as inter-island shipments use similar logistics skills.
- **Fleet Manager**: coordinates owned vehicle ro-ro transport when applicable. Absorbed.

---

## W67. Monthly Store Performance Review

| Field | Detail |
|---|---|
| **Trigger** | Monthly review calendar (by day 10 of each month, following W9a close and W35 monthly reporting) |
| **Frequency** | Monthly per store; conducted by Regional Manager |
| **Volume** | 200 stores ÷ 4 Regional Managers = 50 stores/Regional Manager/month; ~2–3 reviews/day over 15–20 working days |
| **Owner** | Regional Manager |
| **Participants** | Regional Manager, Store Manager, Assistant Store Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates Store Performance Scorecard per store (auto-distributed by day 7): revenue vs. budget and vs. prior year, gross margin %, labor cost % of revenue, shrinkage rate (from W6/W37), customer satisfaction score (from W65), BOPIS fill rate, receiving accuracy, training completion rate, safety incidents, cash variance incidents, POS exception count | System | Controller | Automated |
| 2 | Regional Manager reviews scorecards for all 50 assigned stores; identifies top 5 performers, bottom 5 performers, and stores with material variances (> ±5% revenue, > ±2% margin, > 1.5% shrinkage) | Regional Manager | Store Ops Director | 3–4 hours/month |
| 3 | Regional Manager conducts 45–60 minute review meeting (in-person or video call) with each Store Manager: (a) review scorecard performance vs. budget and vs. prior month, (b) discuss root causes for material variances, (c) review action items from prior month — status and results, (d) agree on 2–3 specific action items for next month (e.g., reduce shrinkage in lumber department, improve BOPIS pickup SLA, schedule training for new cashiers), (e) discuss HR matters (staffing gaps, performance issues, training needs) | Regional Manager | Store Ops Director | 45–60 min/store |
| 4 | For bottom 5 performers: Regional Manager develops targeted improvement plan with Store Manager — specific KPIs to improve, timeline, and resources needed; copies Store Ops Director | Regional Manager | Store Ops Director | 30 min/store |
| 5 | For top 5 performers: Regional Manager recognizes performance; discusses best practices to share with other stores; identifies candidates for store manager development or new store opening leadership | Regional Manager | Store Ops Director | 15 min/store |
| 6 | Regional Manager enters agreed action items into system per store; system tracks action item completion; Store Manager updates status before next review | Regional Manager / Store Manager | Store Ops Director | 10 min/store |
| 7 | Regional Manager presents monthly store portfolio summary to Store Ops Director: top/bottom performers, common themes, resource requests, capital needs; Store Ops Director decides on escalations and resource allocation | Regional Manager | Store Ops Director | 2 hours/month |
| 7a | **Competitive intelligence input**: as part of each monthly store review, Store Manager reports competitive activity observed during the month — (a) new competitor store openings or closures within the store's trade area, (b) competitor promotional events, pricing actions, or new product introductions observed by Sales Associates and Department Supervisors, (c) customer feedback referencing competitor offerings; Regional Manager consolidates competitive intelligence across stores in their region and reports to Store Ops Director; Store Ops Director routes competitive intelligence to VP Merchandising for incorporation into the quarterly assortment review (W1) and to Pricing Analyst for SRP review (W40); competitive intelligence is not a separate system module but is captured as a structured input in the W67 monthly review — Store Manager completes a competitive activity section in the store performance report with fields for competitor name, activity type, affected categories, and estimated impact | Store Manager / Regional Manager | Store Ops Director | 10 min/store/month |
| 8 | Quarterly: Store Ops Director includes store performance trends in management committee meeting (W35 step 14); bottom 10 stores flagged for COO attention | Store Ops Director | COO | Quarterly |

### System Touchpoints
- Auto-generated Store Performance Scorecard with KPIs from all modules: revenue, margin, labor, shrinkage, CSAT, BOPIS fill rate, receiving accuracy, training completion, safety incidents, cash variance, POS exceptions (W67.1)
- Monthly trend visualization with budget vs. actual vs. prior year comparison (W67.1)
- Action item tracking per store with status, owner, and due date; visible to Regional Manager and Store Ops Director (W67.6)
- Store portfolio dashboard for Regional Manager: heat map of store performance by KPI; drill-down to individual store scorecards (W67.2)
- Integration with W6 (shrinkage data), W9a (financial data), W11 (BOPIS fill rate), W34 (labor cost), W35 (management reporting), W37 (POS exceptions, shrinkage), W51 (training completion), W65 (CSAT/NPS)

### Staffing Implication
- **Regional Manager**: 50 stores × 45–60 min review = ~40–50 hours/month + 3–4 hours prep + 2 hours summary = ~45–55 hours/month. With 4 Regional Managers, this is ~12–14 hours each/month = ~3–4 hours/week. Tight but manageable with good time management and delegation to Assistant Store Managers for routine follow-ups.
- **Store Manager**: 1 review/month × 60 min + 10 min action item entry = ~70 min/month. Absorbed.

---

## W68. Product Lifecycle & Discontinuation

| Field | Detail |
|---|---|
| **Trigger** | Quarterly assortment review (W1) identifies SKUs for discontinuation; or vendor announces product end-of-life; or category rationalization decision |
| **Frequency** | ~4–8 discontinuation campaigns/year (aligned with W1 quarterly cycles); ~200–500 SKUs discontinued per campaign |
| **Volume** | ~1,000–2,000 SKUs discontinued/year (balanced by ~1,500–2,500 new SKUs/year from W1/W32); each SKU follows the same lifecycle |
| **Owner** | Category Manager |
| **Participants** | Category Manager, Buyer, Merchandise Planner, Pricing Analyst, Supply Planner, Marketing, Store Operations |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Category Manager identifies SKUs for discontinuation from W1.2 underperformer analysis (bottom 10% by revenue/sqm, negative margin, < 2 turns/year, or vendor product end-of-life notification); creates discontinuation candidate list per category | Category Manager | VP Merchandising | 2 hours/campaign |
| 2 | Buyer validates discontinuation impact per SKU: (a) remaining open POs — can they be cancelled or reduced?, (b) outstanding vendor commitments on blanket POs (W2c) — minimum commitment status, (c) active rebate agreements (W27) — impact on rebate tier achievement, (d) vendor relationship impact — is vendor sole-source for other SKUs? | Buyer | Category Manager | 3 hours/campaign |
| 3 | VP Merchandising approves discontinuation list; system sets "Discontinued — Pending" status on approved SKUs | VP Merchandising | VP Merchandising | 30 min/campaign |
| 4 | **Last buy decision**: for each discontinued SKU, Buyer determines: (a) cancel all open POs (standard action) or (b) place final buy order to cover estimated sell-through during clearance period if remaining stock is critically low and sufficient margin exists; final buy follows standard W2a PO process but flagged as "Last Buy" — no future auto-replenishment | Buyer | Category Manager | 1 hour/campaign |
| 5 | Supply Planner disables auto-replenishment (ROP) for discontinued SKUs; system stops generating suggested POs; remaining store replenishment continues until DC stock is exhausted; system auto-cancels all open backorders (W56) for discontinued SKUs across all stores; customers with cancelled backorders notified via SMS/email with apology and option to select a substitute item (directed to Sales Associate or CSR for assistance) | Supply Planner | Supply Planning Manager | 30 min/campaign |
| 6 | Merchandise Planner flags SKU as "Discontinued" in item master with effective date; item hidden from planogram tools and new store assortment assignments (W16.5); item remains visible in POS and ecommerce for selling remaining stock | Merchandise Planner | Category Manager | 1 hour/campaign |
| 7 | **Clearance execution**: Pricing Analyst sets clearance markdown per W13.9a — system applies clearance price at POS and ecommerce; POS displays clearance disclaimer; Dept. Supervisors move items to clearance section; clearance period typically 4–6 weeks (longer than promo clearance per W13.9a to allow complete sell-through) | Pricing Analyst / Dept. Supervisor | Category Manager | 2 hours/campaign |
| 7a | **Pricing conflict during discontinuation clearance**: if a regular price increase (W40) occurs while an item is in discontinuation clearance, the clearance price is NOT recalculated from the new regular price — the clearance price remains fixed at its originally set level (typically a percentage below the pre-clearance regular price) until the clearance period ends; if a regular price decrease (W40) occurs during clearance and the new regular price falls below the clearance price, system alerts Pricing Analyst, who must either lower the clearance price below the new regular price or accelerate the item's disposition to post-clearance (W68.9); this rule extends the W13 pricing conflict resolution logic to the discontinuation context — clearance price overrides regular price during the clearance period, and clearance items are excluded from standard price change batches (W63)
| 8 | **Weekly sell-through monitoring**: Pricing Analyst reviews discontinued SKU sell-through dashboard; if sell-through rate < 20% of remaining stock after 3 weeks, escalates to Category Manager for deeper markdown or accelerated disposition | Pricing Analyst | Category Manager | 30 min/week during clearance |
| 9 | **Post-clearance disposition**: at end of clearance period, remaining stock dispositioned per priority: (a) Return to Vendor (RTV) — Buyer coordinates per W3.6a, negotiate credit note; (b) bulk liquidation to discount buyers — Buyer arranges sale; (c) donation to partner organizations (Habitat for Humanity, local community organizations); (d) scrap/recycle — DC Supervisor authorizes per W3.6c; system removes remaining inventory and posts final loss | Buyer / DC Supervisor | Category Manager | 2 hours/campaign |
| 10 | **Vendor settlement**: AP Clerk processes any vendor credit memos from RTV per W7.9b; Buyer confirms vendor agreement termination or continued relationship on other SKUs; system releases any remaining blanket PO commitments per W2c | AP Clerk / Buyer | AP Supervisor | 1 hour/campaign |
| 11 | **System archival**: Merchandise Planner sets SKU status to "Discontinued — Inactive"; item removed from active search in POS (no longer scannable for new sales), removed from ecommerce catalog, excluded from inventory reports; item master record retained for 7 years per BIR retention (historical transaction references remain accessible); WAC and inventory value zeroed out | Merchandise Planner | Category Manager | 30 min/campaign |
| 12 | **Post-discontinuation review**: Category Manager compares actual recovery rate (clearance + RTV credits) vs. write-off loss; documents learnings for future discontinuation decisions; feeds into quarterly assortment review (W1) | Category Manager | VP Merchandising | 1 hour/campaign |

**Total discontinuation campaign cycle**: 6–10 weeks from approval to archival

### System Touchpoints
- SKU discontinuation status lifecycle: Active → Discontinued (Pending) → Discontinued (Clearance) → Discontinued (Inactive); each status change controls system behavior (POS scanning, ecommerce visibility, auto-replenishment, planogram inclusion) (W68.3, 6, 11)
- Last buy PO flag that triggers no future auto-replenishment while allowing one-time procurement (W68.4)
- Auto-replenishment disable per SKU-location with effective date (W68.5)
- Clearance markdown execution with extended clearance period (longer than W13.9a promotional clearance) (W68.7)
- Discontinued SKU sell-through dashboard with velocity tracking and escalation triggers (W68.8)
- Final disposition tracking: RTV, liquidation, donation, scrap — with GL posting for each outcome (W68.9)
- SKU archival with 7-year BIR retention compliance; historical transaction references preserved (W68.11)
- Integration with W1 (assortment review — trigger), W2 (last buy PO, blanket PO release), W3 (RTV), W7 (vendor credit memo), W13.9a–b (clearance), W16 (new store assortment — exclude discontinued), W31 (disable forecast), W36 (vendor relationship), W40 (price changes during clearance — W40 pricing conflict rules apply)

### Staffing Implication
- **Category Manager**: ~4–8 campaigns/year × 4 hours = ~16–32 hours/year. Absorbed within existing W1 quarterly duties.
- **Buyer**: ~4–8 campaigns × 4 hours = ~16–32 hours/year. Absorbed.
- **Pricing Analyst**: clearance setup + weekly monitoring = ~4 hours/campaign × 6–8 = ~24–32 hours/year. Absorbed.
- **Merchandise Planner**: ~1 hour/campaign for status changes. Absorbed.
- No incremental headcount.

---

## W69. Price Compliance Audit

| Field | Detail |
|---|---|
| **Trigger** | Weekly price audit schedule (every store, every week) |
| **Frequency** | Weekly per store; integrated into daily operations |
| **Volume** | 50 items audited per store per week (~0.14% of 35,000 SKUs); 200 stores × 50 items = 10,000 price checks/week chain-wide |
| **Owner** | Department Supervisor |
| **Participants** | Stock Associate (auditor), Department Supervisor (reviewer) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates weekly price audit list per store: 50 random items stratified by department (proportional to department SKU count) plus any items with price changes in the past 7 days (W40/W63) as mandatory audit items; audit list pushed to Stock Associate's handheld device | System | — | Automated (nightly) |
| 2 | Stock Associate walks aisles with handheld; for each item on the audit list: (a) scans shelf barcode or item barcode, (b) system displays current SRP on handheld, (c) Stock Associate visually compares displayed shelf price tag to system price, (d) enters result: Match / Mismatch / No Tag / Wrong Tag | Stock Associate | Dept. Supervisor | 20–30 min/week (50 items at ~25 sec each) |
| 3 | If mismatch detected: Stock Associate photographs shelf tag; handheld captures item barcode, displayed price, system price, and photo as audit evidence | Stock Associate | Dept. Supervisor | 1 min/mismatch |
| 4 | Department Supervisor reviews audit results on handheld or terminal: (a) for mismatches — immediately corrects shelf tag (reprints from store label printer or applies manual correction tag pending W63 batch); (b) for missing tags — requests Stock Associate to print and apply; (c) investigates root cause (missed label in W63 batch, customer moved item to wrong location, tag fell off, promotional tag not removed after promo ended) | Dept. Supervisor | Store Manager | 10 min/week |
| 5 | System records all audit results with item, store, auditor, timestamp, match/mismatch status, and corrective action taken; weekly audit compliance rate calculated per store (audits completed ÷ audits assigned) | System | — | Automated |
| 6 | Weekly: Store Manager reviews price audit compliance dashboard — stores must achieve ≥ 98% price accuracy on audited items and ≥ 95% audit completion rate; stores below threshold receive additional focus in monthly store performance review (W67) | Store Manager | Regional Manager | 10 min/week |
| 7 | Monthly: Regional Manager reviews price audit results across all assigned stores; identifies stores with persistent accuracy issues; feeds into Store Performance Scorecard (W67) and loss prevention review (W37) | Regional Manager | Store Ops Director | 30 min/month |
| 8 | Quarterly: Pricing Analyst analyzes price audit data chain-wide — identifies categories, SKUs, or store formats with systematically higher mismatch rates; recommends shelf tag process improvements (e.g., switch to electronic shelf labels for high-change categories) | Pricing Analyst | Category Manager | 1 hour/quarter |

### System Touchpoints
- Weekly price audit list generation: random stratified sample + mandatory recently-changed items (W69.1)
- Handheld barcode scan with real-time SRP display for visual comparison (W69.2)
- Mismatch capture with photo evidence, displayed price, system price, and item barcode (W69.3)
- Audit results repository: per-store, per-week accuracy rate with item-level detail and root cause (W69.5)
- Price audit compliance dashboard: completion rate and accuracy rate per store per week (W69.6)
- Chain-wide price accuracy analytics by category, SKU, and store format (W69.8)
- Integration with W40 (price changes feed mandatory audit items), W63 (shelf label distribution — label accuracy verification), W67 (store performance scorecard), W37 (loss prevention — price discrepancies may indicate fraud or process failure)

### Staffing Implication
- **Stock Associate**: 20–30 min/week for audit walk. Absorbed within existing 3 stock associates — can be rotated weekly (one associate audits each week on a 3-week rotation).
- **Department Supervisor**: 10 min/week review. Absorbed.
- **Store Manager**: 10 min/week dashboard review. Absorbed into opening routine (W5a) or weekly planning.
- No incremental headcount.

---

## W70. Credit Note & Debit Note Aging Reconciliation

| Field | Detail |
|---|---|
| **Trigger** | Month-end close (W9a step 16e) and weekly AP/AR aging review |
| **Frequency** | Weekly aging review (AP and AR); monthly formal reconciliation during close; quarterly deep review in management reporting (W35) |
| **Volume** | ~100–200 open credit/debit notes at any time across AP and AR |
| **Owner** | Chief Accountant |
| **Participants** | AP Clerk, AR Clerk, AP Supervisor, AR Supervisor, Chief Accountant, Controller |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates credit/debit note aging report across AP and AR: note number, vendor/customer, amount, date created, source (RTV, rebate, price protection, pricing error, volume discount, complaint resolution, promotional adjustment), status (unapplied / partially applied), and age bucket (0–30, 31–60, 61–90, 90+ days) | System | — | Automated |
| 2 | **AP credit memos** (vendor credits): AP Clerk reviews unapplied vendor credit memos weekly; for each: (a) if vendor has open invoices, applies credit to oldest invoice — system reduces vendor balance; (b) if vendor has no open invoices, contacts vendor to request refund or confirms credit will be applied to next invoice; (c) if credit > 90 days and vendor is unresponsive, escalates to AP Supervisor for write-off decision | AP Clerk | AP Supervisor | 30 min/week |
| 3 | **AR credit memos** (customer credits): AR Clerk reviews unapplied customer credit memos weekly; for each: (a) if customer has open invoices, applies credit to oldest invoice; (b) if customer has no open invoices, contacts customer to arrange refund or confirm credit for next purchase; (c) if credit > 90 days and customer is unresponsive, escalates to AR Supervisor for write-off as other income | AR Clerk | AR Supervisor | 30 min/week |
| 4 | **AP debit memos** (vendor chargebacks): AP Clerk reviews open debit memos — these represent amounts BuildRight is deducting from vendor payments (short shipments, damage claims, pricing disputes); confirms debit memos are resolved with next vendor payment; unresolved debits > 60 days escalated to Buyer for vendor negotiation | AP Clerk | AP Supervisor | 15 min/week |
| 5 | **AR debit memos** (customer chargebacks): AR Clerk reviews open AR debit memos — these represent amounts owed by customers beyond normal invoices (bounced checks, disputed deductions); follows up with customer per W8 collection tiers; unresolved debits > 90 days escalated to Finance Manager for bad debt provision | AR Clerk | AR Supervisor | 15 min/week |
| 6 | **Month-end reconciliation** (W9a step 16e): Chief Accountant reviews total unapplied credit/debit note balances; confirms AP credit memo sub-ledger agrees with GL Accounts Payable; confirms AR credit memo sub-ledger agrees with GL Accounts Receivable; unresolved items > 90 days summarized for Controller | Chief Accountant | Controller | 1 hour/month |
| 7 | **Quarterly deep review** (W35 step 19): Chief Accountant presents credit/debit note aging summary to Controller and CFO; highlights chronic vendors/customers with recurring unapplied credits; recommends process improvements (e.g., auto-application rules, vendor/customer communication templates); material write-offs approved per standard tiers | Chief Accountant / Controller | CFO | 30 min/quarter |

### System Touchpoints
- Credit/debit note aging report with AP and AR views; filterable by age, vendor/customer, source, and status (W70.1)
- Auto-application rules: system auto-applies credit memos to oldest open invoices for the same vendor/customer if configured; manual override available (W70.2–3)
- Sub-ledger to GL reconciliation: AP/AR credit memo sub-ledger totals reconcile to GL control accounts (W70.6)
- Write-off workflow for stale credits/debits: tiered approval (AR/AP Supervisor ≤ PHP 50K, Controller ≤ PHP 200K, CFO > PHP 200K); system posts write-off with GL entry (W70.2–5)
- Chronic vendor/customer analysis: identifies accounts with recurring unapplied credits over rolling 12-month period (W70.7)
- Integration with W7 (AP credit memos from vendor), W7.9b (vendor credit memo processing), W8 (AR credit memos), W8.11 (customer credit memo processing), W9a.16e (month-end credit note reconciliation), W35.19 (quarterly review)

### Staffing Implication
- **AP Clerk**: adds ~30 min/week for AP credit memo review. Absorbed.
- **AR Clerk**: adds ~30 min/week for AR credit memo review. Absorbed.
- **Chief Accountant**: adds ~1 hour/month + 30 min/quarter for reconciliation. Absorbed within month-end close duties.
- No incremental headcount.

---

## W71. Store Physical Security & Access Control

| Field | Detail |
|---|---|
| **Trigger** | Daily security operations; alarm events; periodic access audits; security incidents |
| **Frequency** | Continuous; daily guard operations; monthly access reviews; quarterly security audits |
| **Volume** | 200 stores × 24/7 security; 5 DCs × 24/7 security; ~8,050 active access credentials |
| **Owner** | Store Manager (store-level); DC Manager (DC-level); Facilities Coordinator (oversight) |
| **Participants** | Security guards (contracted), Store Manager, DC Manager, Facilities Coordinator, HR, IT, Loss Prevention Officer |

### Daily Security Operations

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Opening: guard on duty disarms alarm (or receives handoff from night-shift guard); performs exterior walkthrough checking for signs of break-in, vandalism, or tampering with outdoor yard inventory; reports findings to Store Manager before staff arrival (W5a step 2) | Security Guard | Store Manager | 15 min |
| 2 | During operating hours: guard monitors store entrance/exit; controls access to receiving dock and backroom areas (only authorized personnel via access badge); assists with customer bag checks on exit per company policy | Security Guard | Store Manager | Continuous |
| 3 | Closing: guard monitors final customer exit; secures receiving dock; performs exterior walkthrough; arms alarm system after Store Manager confirms all staff departed (W5c step 9) | Security Guard | Store Manager | 15 min |
| 4 | Night shift (if applicable): guard patrols exterior perimeter hourly; checks outdoor yard inventory area; monitors alarm system; responds to alarm activations per incident response protocol | Security Guard | Facilities Coordinator | Continuous |

### Key & Access Badge Management

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 5 | New employee access: HR Assistant creates access badge during onboarding (W15 step 9); system assigns access level by role (cashier = POS area + backroom; stock associate = sales floor + backroom + receiving; store manager = all areas); badge activated in access control system | HR Assistant / IT | Store Manager | 10 min/employee |
| 6 | Access deactivation: upon employee separation (W43 step 5), IT deactivates access badge within same business day; Store Manager collects physical badge; system logs deactivation with timestamp; if badge not returned, system notes "badge not returned" and access is blocked electronically | IT / Store Manager | Store Manager | 5 min/employee |
| 7 | Lost badge: employee reports lost badge to Store Manager immediately; Store Manager deactivates lost badge in system and issues replacement; system logs lost badge event with employee ID and replacement badge number; if pattern of repeated lost badges (> 2 in 12 months), escalated to HR for review | Store Manager / IT | Facilities Coordinator | 10 min/occurrence |
| 8 | Master key / safe key control: Store Manager holds master key and safe key; Assistant Store Manager holds backup; keys inventoried monthly; key issuance log maintained for all mechanical keys (backroom, electrical room, roof access); Facilities Coordinator audits key logs quarterly across all stores | Store Manager / Facilities Coordinator | Store Ops Director | 30 min/month |

### Alarm & CCTV System Monitoring

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 9 | Alarm activation after hours: alarm monitoring company contacts designated Store Manager (or backup contact list); if no response within 15 minutes, monitoring company dispatches guard and contacts Facilities Coordinator; for confirmed intrusion, monitoring company contacts PNP and Store Manager proceeds to store | Alarm Monitoring Co. / Store Manager | Facilities Coordinator | As needed |
| 10 | Alarm event documentation: Store Manager investigates cause of alarm (false alarm, intrusion attempt, animal, weather); documents findings in system with alarm event reference, CCTV footage review timestamp, and resolution; false alarm frequency tracked per store per month; stores with > 5 false alarms/month flagged for alarm system maintenance (W47) | Store Manager | Facilities Coordinator | 15 min/event |
| 11 | CCTV system health monitoring: system automatically checks CCTV camera status every 4 hours (online/offline); if camera goes offline, system alerts IT Helpdesk (W48) and Store Manager; IT prioritizes CCTV camera restoration as P2 incident (W48 SLA matrix); Facilities Coordinator reviews weekly CCTV health report across all stores; stores with > 10% cameras offline for > 24 hours flagged for immediate action | System / IT / Facilities Coordinator | CIO | Automated + 30 min/week review |
| 12 | CCTV recording retention: minimum 30 days online storage, 90 days archived per W37 CCTV integration specification; Facilities Coordinator validates retention compliance quarterly; recording storage capacity monitored by IT; capacity expansion planned before reaching 80% threshold | IT / Facilities Coordinator | CIO | Quarterly review |

### Security Incident Response

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 13 | Break-in / robbery: Store Manager (or night guard) contacts PNP immediately; secures scene; Facilities Coordinator and Store Ops Director notified within 1 hour; Loss Prevention Officer activated for investigation; inventory loss assessed per W37 confirmed theft write-off process; insurance claim filed per W59 if loss exceeds deductible | Store Manager / LPO | Store Ops Director | Varies |
| 14 | Vendor / contractor access: visiting vendors and contractors sign in at guard station; issued temporary visitor badge with time-limited access; guard verifies vendor identity against scheduled appointment list (W18b for DSD, W47 for maintenance contractors); visitor badge collected on exit; sign-in log retained for 90 days | Security Guard / Vendor | Store Manager | 5 min/visitor |
| 15 | Monthly: Facilities Coordinator generates security incident summary per store: alarm events, break-in attempts, false alarm frequency, badge incidents, camera downtime; includes in monthly report to Store Ops Director | Facilities Coordinator | Store Ops Director | 2 hours/month |
| 16 | Quarterly: LPO includes physical security incidents in loss prevention review (W37); Facilities Coordinator conducts physical security audit at 10–15 sampled stores per quarter (rotating): checks alarm functionality, camera coverage adequacy, key control compliance, guard force performance, and outdoor yard security | Facilities Coordinator / LPO | Store Ops Director | Quarterly audit |

### Guard Force Management

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 17 | Security services contracted through licensed security agency (separate from BuildRight entities); Facilities Coordinator manages contract per W62 (non-PO vendor contract); contract specifies guard deployment (typically 2 guards per store: 1 day + 1 night shift), qualifications (licensed, trained, vetted), equipment (uniforms, radios, flashlights), and response protocols | Facilities Coordinator | Store Ops Director | Per W62 |
| 18 | Store Manager rates guard performance daily (attendance, alertness, incident response); monthly aggregate rating submitted to Facilities Coordinator; Facilities Coordinator escalates underperforming guard agencies to contract review per W62 SLA tracking | Store Manager / Facilities Coordinator | Store Ops Director | 15 min/month |
| 19 | Annual: Facilities Coordinator and Legal review security service contract; benchmarks rates and service quality against alternative agencies; renews or re-tenders per W62 contract lifecycle | Facilities Coordinator / Legal | Store Ops Director | Per W62 |

### System Touchpoints
- Access control system integration with HR employee lifecycle (W15 onboarding creates badge, W43 separation deactivates badge) (W71.5–6)
- Alarm system event logging with cause classification and resolution documentation (W71.10)
- CCTV health monitoring dashboard: camera status per store, offline alerts, retention compliance (W71.11–12)
- Security incident register: break-in, robbery, vandalism, false alarm — linked to insurance claims (W59) and loss prevention investigation (W37) (W71.13)
- Visitor/contractor sign-in log with temporary badge management (W71.14)
- Guard force performance rating integrated into vendor contract SLA tracking (W62) (W71.18)
- Key and badge inventory management with audit trail (W71.5–8)
- Integration with W5a (opening security check), W5c (closing alarm activation), W37 (loss prevention — CCTV integration, confirmed theft), W47 (alarm system maintenance), W48 (IT helpdesk — CCTV camera restoration), W59 (insurance claims for theft/vandalism), W62 (security agency contract management)

### Staffing Implication
- **Security guards**: 2 guards per store × 200 stores = 400 guards (contracted through security agency, not BuildRight employees); 3–4 guards per DC × 5 DCs = 15–20 guards; relief/absence coverage adds ~10% buffer; total contracted guard force: ~460–480 including reliefs.
- **Facilities Coordinator**: adds ~4–6 hours/month for physical security oversight across 200 stores. Absorbed within existing recommended role.
- **No incremental BuildRight headcount.** Guard force is a contracted service.

---

## W72. Employee Performance Management

| Field | Detail |
|---|---|
| **Trigger** | Annual performance review cycle; or periodic performance improvement need |
| **Frequency** | Annual formal review; quarterly check-in; ongoing performance coaching |
| **Volume** | ~8,050 employees; all employees reviewed annually |
| **Owner** | Department Head (for direct reports); Store Manager (for store staff) |
| **Participants** | Store Manager, Department Supervisors, Department Heads, HR Head, employees |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Annual goal-setting** (January): Department Heads and Store Managers set performance goals for each direct report aligned with department/store KPIs — (a) quantitative goals (sales targets, accuracy rates, shrinkage targets for Dept. Supervisors; transaction speed, cash variance for Cashiers; receiving accuracy for Receiving Clerks; cycle count accuracy for Stock Associates), (b) qualitative goals (customer service standards, teamwork, adherence to company policies), (c) development goals (training completion per W51, skill acquisition, cross-training); goals entered in system with measurable targets and timeline | Dept. Head / Store Manager | VP / Store Ops Director | 30 min/employee |
| 2 | **Quarterly check-in**: Store Manager or Department Supervisor conducts 15-minute check-in with each direct report — review progress against goals, identify obstacles, adjust goals if business conditions changed; system sends quarterly reminder to managers; check-in notes documented in system | Store Manager / Dept. Supervisor | Dept. Head | 15 min/employee/quarter |
| 3 | **Mid-year calibration** (June): Store Ops Director conducts calibration session with Regional Managers to ensure consistent performance standards across stores; HR Head provides aggregate performance data by department and region; significant rating adjustments documented | Store Ops Director / HR Head | COO | 4 hours/year |
| 4 | **Annual performance review** (December): manager completes formal assessment per employee — (a) rates performance against each goal (Exceeds Expectations, Meets Expectations, Needs Improvement, Does Not Meet Expectations), (b) documents key achievements and areas for development, (c) proposes overall rating, (d) submits to next-level manager for review and approval | Store Manager / Dept. Supervisor | Dept. Head / Store Ops Director | 45 min/employee |
| 5 | **Employee acknowledgment**: employee reviews assessment in system; provides written comments (optional); signs acknowledgment (digital signature); if employee disagrees, may submit written rebuttal retained in system alongside the assessment | Employee | — | 15 min |
| 6 | **Rating confirmation and compensation action**: Dept. Head or Store Ops Director confirms final rating; HR Head approves ratings distribution (ensures no grade inflation); ratings linked to: (a) merit increase (if budgeted — typically 3–5% for Meets Expectations, 5–8% for Exceeds), (b) 13th month pay is statutory and not performance-linked, (c) promotional readiness identification, (d) performance improvement plan trigger for Needs Improvement/Does Not Meet | HR Head / CFO | CEO | 1 week/year |
| 7 | **Performance Improvement Plan (PIP)**: for employees rated Needs Improvement or Does Not Meet — (a) manager creates PIP in system with specific improvement targets, timeline (typically 30–60 days), and support resources (training per W51, closer supervision, mentoring), (b) employee acknowledges PIP, (c) manager conducts weekly check-ins during PIP period, (d) at PIP conclusion: manager assesses outcome — improved (close PIP, continue standard monitoring), insufficient improvement (extend PIP 30 days or initiate separation per W43 with HR Head approval), (e) system tracks PIP status and outcomes for HR reporting | Store Manager / Dept. Head | HR Head | 2 hours/PIP |
| 8 | **Promotion and transfer identification**: during annual review cycle, managers identify employees meeting promotion criteria — (a) consistent Exceeds Expectations ratings for 2+ years, (b) demonstrated readiness for next-level responsibilities, (c) completed required training per W51; promotion recommendations submitted to HR Head for review and inclusion in annual headcount plan; inter-store or inter-entity transfers processed per W43.15 (cross-entity transfer) or simplified location transfer within same entity | Store Manager / Dept. Head | HR Head | Part of annual review |
| 9 | **Analytics**: HR Head generates annual performance dashboard — rating distribution by department, store, region, and entity; year-over-year rating trend; correlation between training completion (W51) and performance ratings; PIP completion rate and outcomes; promotion rate; turnover rate by performance tier | HR Head | CHRO | 4 hours/year |

### System Touchpoints
- Performance goal entry with measurable targets and timeline (W72.1)
- Quarterly check-in reminder and documentation (W72.2)
- Annual assessment form with goal-by-goal rating, comments, and digital signature (W72.4–5)
- Rating workflow: manager proposes → next-level manager reviews → HR Head approves distribution (W72.6)
- PIP creation with improvement targets, timeline, weekly check-in logging, and outcome tracking (W72.7)
- Promotion/transfer identification linked to performance history (W72.8)
- Performance analytics dashboard: rating distribution, trends, training correlation, PIP outcomes (W72.9)
- Integration with W10 (merit increase in payroll), W15 (onboarding — initial goal-setting during first 90 days), W43 (PIP failure may lead to separation), W51 (training completion feeds into performance assessment), W67 (store performance KPIs inform goal-setting for store staff)

### Staffing Implication
- **No incremental headcount.** Performance reviews are distributed across ~230 managers (Store Managers, Dept. Supervisors, Dept. Heads). Annual cycle adds ~45 min/employee/year for ~8,050 employees = ~6,000 hours total effort, distributed across the management team.
- **HR Head**: adds ~8 hours/year for calibration and rating distribution approval. Absorbed.

---

## W73. Data Migration Validation & Parallel-Run Testing

> This workflow describes the operational participation of business users in data migration validation and parallel-run testing during ERP implementation. It is an implementation-phase workflow, not a steady-state operational process.

| Field | Detail |
|---|---|
| **Trigger** | Implementation roadmap Phase 2 (data migration) and Phase 3 (pilot go-live with parallel run) per Implementation Roadmap |
| **Frequency** | Once per implementation; validation cycles repeated per migration iteration |
| **Volume** | All master data (55,000 SKUs, 1,000 vendors, 600,000+ customers, 8,050 employees, 205 locations) + open transaction data (open POs, open AR/AP, inventory balances, fixed assets) |
| **Owner** | Implementation Project Manager (overall); Department Heads (validation per domain) |
| **Participants** | Store Managers, Cashiers, AP/AR Clerks, Category Managers, Buyers, Cost Accountant, IT, external implementation partner |

### Data Migration Validation

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Item master validation**: Merchandise Planners verify migrated SKU data — sample 500–1,000 SKUs across categories; confirm item description, unit of measure, cost, SRP, category assignment, and attributes (catch-weight flags, shelf-life flags, consignment/VMI flags) match source system; report discrepancies to implementation partner for correction | Merchandise Planner | Category Manager | 8 hours/iteration |
| 2 | **Customer master validation**: AR Clerks verify sample of 500 trade/corporate accounts — confirm credit limits, payment terms, VAT treatment classification, and contact details; Loyalty Manager verifies sample of 1,000 loyalty accounts — points balance, tier status, contact information | AR Clerk / Loyalty Manager | AR Supervisor | 8 hours/iteration |
| 3 | **Vendor master validation**: Buyers verify sample of 200 vendors — confirm payment terms, lead times, bank details, tax classification (ATC codes), and pricing tolerance | Buyer | Category Manager | 4 hours/iteration |
| 4 | **Inventory balance validation**: Cost Accountant and DC Supervisors verify opening inventory balances per location (200 stores + 5 DCs) — reconcile migrated quantities and values (WAC) to legacy system closing balances; identify discrepancies > 1% by value | Cost Accountant / DC Supervisor | Controller | 8 hours/location group |
| 5 | **Financial opening balance validation**: Controller and Chief Accountant verify migrated opening trial balance per entity (5 entities) — GL account balances, open AP invoices, open AR invoices, fixed asset register, bank balances; reconcile to legacy closing trial balance | Controller / Chief Accountant | CFO | 16 hours/iteration |
| 6 | **Employee master validation**: HR Head verifies sample of 200 employees across entities — confirm salary, tax status, statutory deduction registration, leave balances, and organizational assignment | HR Head | CHRO | 4 hours/iteration |
| 7 | All validation exceptions logged in implementation issue tracker; corrected in next migration iteration; re-validated until zero material discrepancies | All validators | Project Manager | Ongoing |

### Parallel-Run Testing (Pilot Phase)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 8 | **Payroll parallel run**: for 1 payroll cycle (semi-monthly), Payroll Officer processes payroll in both legacy and new ERP simultaneously; compares output per employee — gross pay, deductions, net pay, employer contributions; discrepancies > PHP 100 per employee flagged for investigation; Finance validates GL postings match between systems | Payroll Officer / Finance | CFO | 1 payroll cycle |
| 9 | **Month-end close parallel run**: for 1 month-end period, Chief Accountant performs close steps (W9a) in both systems; compares trial balance, financial statements, and key reconciliation outputs (bank rec, GRNI, AR aging, AP aging) | Chief Accountant | Controller | 1 close cycle |
| 10 | **POS parallel run** (pilot stores only): during pilot go-live (Implementation Roadmap Phase 3), pilot store Cashiers process live transactions in new POS while legacy POS runs in shadow mode; Store Manager compares daily Z-reports (transaction count, revenue by tender, cash total) between systems; discrepancies > 1% by revenue flagged for investigation | Cashier / Store Manager | Store Ops Director | 2–4 weeks |
| 11 | **Inventory transaction parallel run**: for pilot stores and serving DC, Receiving Clerks and Stock Associates process key inventory transactions (goods receipt, transfer receipt, cycle count, POS sales deduction) in both systems; Cost Accountant compares ending inventory balances | Receiving Clerk / Cost Accountant | Controller | 2–4 weeks |
| 12 | **User acceptance testing (UAT)**: before each go-live wave, designated power users from each department execute scripted UAT test cases covering their critical workflows (AP clerk tests W7, Buyer tests W2, Cashier tests W5b, etc.); all test cases must pass with zero critical defects for wave go-live approval | Department power users | Project Manager | 1–2 weeks/wave |
| 13 | **Sign-off**: after successful parallel run and UAT, Department Heads sign off on their domain's readiness per go-live wave; Controller signs off on financial accuracy; CFO gives final go/no-go for each wave | Department Heads / CFO | CEO | 1 day/wave |

### System Touchpoints
- Data migration validation workbench: compare migrated data to source with side-by-side display and discrepancy flagging (W73.1–7)
- Parallel-run comparison reports: payroll output comparison, trial balance comparison, Z-report comparison, inventory balance comparison (W73.8–11)
- UAT test case management: scripted test cases with pass/fail tracking and defect logging (W73.12)
- Go-live readiness sign-off workflow with department-level approval (W73.13)
- Integration with all operational workflows (each workflow validated during UAT)

### Staffing Implication
- **Business user time**: data migration validation requires ~50–80 hours of business user effort per iteration (typically 2–3 iterations); parallel-run testing requires ~40–60 hours per cycle; UAT requires ~20–30 hours per wave; total business user effort across implementation: ~400–600 hours spread over 12–18 months
- **This is a one-time implementation cost**, not steady-state headcount. Business users participate alongside their normal duties during implementation. Implementation project plan should allocate dedicated validation windows.

---

## W74. Employee Expense Reimbursement

| Field | Detail |
|---|---|
| **Trigger** | Employee incurs business expense not covered by petty cash (W25), purchase order (W2), or corporate card |
| **Frequency** | ~300–500 expense claims/month across all locations; peaks at month-end and during travel periods |
| **Volume** | Average claim value PHP 1,000–5,000; primarily travel, meals, training materials, field supplies, client entertainment |
| **Owner** | Employee (claimant); Department Head (approval) |
| **Participants** | Employee, Department Head / Store Manager, AP Clerk, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Employee submits expense claim in system (self-service portal or mobile app): expense date, category (travel, meals, supplies, training, entertainment, other), amount, business purpose, cost center, and receipt attachment (photo or PDF) | Employee | — | 10 min/claim |
| 2 | System validates claim: (a) receipt amount matches claimed amount, (b) expense date within allowable claim window (typically 30 days from expense date), (c) expense category is valid for employee's role, (d) total monthly claims for employee do not exceed department expense budget allocation | System | — | Automated |
| 3 | System routes claim for approval per tier: (a) ≤ PHP 5,000: immediate supervisor, (b) PHP 5,001–20,000: Department Head / Store Manager, (c) > PHP 20,000: VP / C-Suite; entertainment expenses always require Department Head approval regardless of amount | System | — | Automated routing |
| 4 | Approver reviews claim: validates business purpose, checks receipt authenticity, confirms expense is within policy (meal per diem limits, travel class restrictions, entertainment pre-approval); approves, returns for correction, or rejects with reason | Approver | Finance Manager | 5 min/claim |
| 5 | Approved claim routed to AP Clerk for processing; AP Clerk validates GL coding and cost center; posts expense to GL (Dr. Department Expense / Cr. Employee Payable) | AP Clerk | AP Supervisor | 5 min/claim |
| 6 | Reimbursement: system includes approved expense reimbursement in the next semi-monthly payroll run (W10) as a separate line item on the payslip — not taxed as compensation if supported by receipts per BIR rules; alternatively, for large reimbursements (> PHP 20,000), AP Clerk processes via separate bank transfer per W7 payment run | Payroll Officer / AP Clerk | AP Supervisor | Per W10 / W7 |
| 7 | Monthly: AP Supervisor generates expense report by department, category, and employee; Finance Manager reviews for policy compliance and unusual patterns; includes in department budget variance report per W26 | AP Supervisor | Finance Manager | 1 hour/month |

### Expense Policy Parameters (Configurable in System)

| Category | Limit | Notes |
|---|---|---|
| **Meal per diem** | PHP 500/day (local); PHP 1,000/day (provincial travel) | Receipt required for amounts exceeding per diem; per diem is non-taxable per BIR rules with supporting travel order |
| **Travel — airfare** | Economy class for domestic; requires pre-approved travel order | Receipt required; booked through admin or approved booking platform |
| **Travel — lodging** | PHP 2,000/night maximum (provincial); requires hotel receipt | Exceptions require VP approval |
| **Transportation** | Taxi, grab, or shuttle receipts | Fuel claims only for authorized vehicle users per W52 |
| **Client entertainment** | PHP 3,000/event maximum; requires pre-approval from Dept. Head | Must specify client name, attendees, and business purpose |
| **Training materials** | Per approved training plan per W51 | Requires training enrollment confirmation |
| **Claim window** | 30 days from expense date | Claims > 30 days require Finance Manager approval |
| **Monthly claim limit** | PHP 20,000 per employee (standard) | Exceptions require VP approval |

### System Touchpoints
- Employee expense claim form in self-service portal (W74.1) with receipt photo upload, category selection, and business justification (W51 employee self-service portal)
- Automated validation rules: receipt matching, claim window enforcement, monthly limit check (W74.2)
- Tiered approval workflow with routing by amount and category (W74.3–4)
- GL posting with cost center allocation (W74.5)
- Payroll integration: approved reimbursements included in semi-monthly payroll as non-taxable line items (per BIR rules — reimbursement of substantiated business expenses is not compensation); alternatively processed via AP payment run for large amounts (W74.6)
- Expense policy parameter configuration by category with limits and approval rules (W74 policy table)
- Monthly expense reporting by department, category, and employee with budget variance integration (W74.7)
- Integration with W7 (AP processing), W10 (payroll — reimbursement payment), W25 (petty cash — boundary: petty cash is for small operational expenses at location; employee expense claims are for individual employee-incurred business expenses), W26 (budget — expense tracking against department budgets), W51 (self-service portal)

### Staffing Implication
- **AP Clerk**: ~300–500 claims/month × 5 min each = ~25–42 hours/month. Absorbed within existing AP team (~8–10 clerks); ~3–5 hours/clerk/month.
- **Department Heads / Store Managers**: ~5 min per claim × average 2–5 claims/approver/month = ~10–25 min/month. Absorbed.
- No incremental headcount.

---

## W75. Layaway / Installment Sales

| Field | Detail |
|---|---|
| **Trigger** | Customer wants to reserve a big-ticket item (appliance, tiles, fixtures, power tools) and pay in installments over a defined period |
| **Frequency** | ~1,000–1,500 layaway agreements/month chain-wide; ~5–8 per store per month |
| **Volume** | Average agreement value PHP 5,000–50,000; primarily appliances, tiles, bathroom fixtures, power tools |
| **Owner** | Customer Service Rep (agreement creation); Store Manager (approvals) |
| **Participants** | CSR, Cashier, Store Manager, Stock Associate, Customer |

### Background

Layaway ("reserved items, installment payment") is a standard practice in Philippine retail, especially for big-ticket items where customers may not qualify for credit cards or trade accounts. The customer selects an item, pays a deposit to reserve it, and makes periodic installment payments over 30–90 days. When fully paid, the customer receives the item. This is distinct from credit sales (W8) — layaway items are not released until fully paid.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer selects item(s) for layaway; CSR confirms item is in stock at store; explains layaway terms: deposit (20% of item price), installment period (30, 60, or 90 days), payment frequency (weekly, bi-weekly, or monthly), cancellation/forfeiture policy | CSR | Store Manager | 5 min |
| 2 | CSR creates layaway agreement in POS/terminal: scans item(s), enters deposit amount, selects installment plan (number of payments, dates); system generates layaway agreement number; customer signs digital agreement (or printed form) acknowledging terms | CSR | Store Manager | 5 min |
| 3 | Customer pays deposit (cash, card, e-wallet); system records deposit as liability (Dr. Cash / Cr. Layaway Deposits Payable); not recognized as revenue until item is released; system creates inventory reservation against the layaway agreement — reserved quantity excluded from ATP for BOPIS (W11) and ecommerce (W19) | Cashier | Store Manager | 2 min |
| 4 | Stock Associate stages the reserved item(s) in backroom layaway holding area with layaway agreement number label; items physically segregated from saleable stock | Stock Associate | Dept. Supervisor | 10 min |
| 5 | Customer returns per agreed schedule to make installment payments; Cashier looks up layaway agreement, records payment; system updates payment schedule and shows remaining balance; each payment posted Dr. Cash / Cr. Layaway Deposits Payable | Cashier | Store Manager | 3 min/payment |
| 6 | If customer misses a scheduled payment by > 7 days: system sends reminder notification (SMS/email); if payment not received within 14 days of due date: Store Manager contacts customer to discuss continuation or cancellation | System / Store Manager | Store Manager | 5 min/overdue |
| 7 | **Completion**: when all installments paid, CSR releases item to customer; system recognizes revenue (Dr. Layaway Deposits Payable / Cr. Revenue) and COGS (Dr. COGS / Cr. Inventory); inventory reservation released; customer receives item with receipt | CSR / Cashier | Store Manager | 5 min |
| 8 | **Customer cancellation**: customer cancels layaway before completion — (a) CSR processes cancellation in system with reason code; (b) system refunds payments received less cancellation fee (configurable, typically 10% of deposit or PHP 200, whichever is higher); cancellation fee retained as other income; (c) remaining refund issued to original payment methods; (d) Stock Associate returns item to sales floor; inventory reservation released, ATP restored | CSR / Stock Associate | Store Manager | 10 min |
| 9 | **Forfeiture**: if customer does not make any payment for 30 consecutive days and does not respond to Store Manager contact — (a) system flags agreement for forfeiture; (b) Store Manager approves forfeiture; (c) all payments received forfeited to BuildRight (recognized as Layaway Forfeiture Income — Dr. Layaway Deposits Payable / Cr. Layaway Forfeiture Income); (d) Stock Associate returns item to sales floor; inventory reservation released; (e) customer notified of forfeiture via SMS/email with finality statement | Store Manager | Regional Manager | 10 min |
| 10 | **Price change during layaway**: if SRP changes (W40) while item is on layaway, the layaway price is the price at time of agreement creation — not affected by subsequent price increases or decreases; if customer cancels and re-purchases at new price, that is a separate transaction | System | — | Automated |
| 11 | Monthly: Store Manager generates layaway activity report — active agreements, completion rate, cancellation rate, forfeiture rate, average days to completion, total liability outstanding; Regional Manager reviews in monthly store performance review (W67) | Store Manager | Regional Manager | 30 min/month |

### System Touchpoints
- Layaway agreement creation in POS/terminal with item reservation, deposit collection, and installment schedule (W75.2–3)
- Inventory reservation: reserved quantity excluded from ATP for BOPIS (W11), ecommerce (W19), and backorder allocation (W56) (W75.3)
- Layaway deposit liability tracking on balance sheet with revenue recognition trigger at item release (W75.3, W75.7)
- Installment payment recording with balance tracking and overdue alerting (W75.5–6)
- Cancellation with configurable fee and refund processing (W75.8)
- Forfeiture with income recognition and inventory restoration (W75.9)
- Price protection during layaway period — agreement price locked at creation (W75.10)
- Layaway activity and liability reporting (W75.11)
- Integration with W5b (POS selling), W6 (cycle counting — layaway items counted separately in backroom holding), W11 (ATP exclusion), W19 (ATP exclusion), W42 (physical inventory — layaway items counted as BuildRight inventory with reserved status)

### Staffing Implication
- **CSR**: ~5–8 layaway agreements/store/month × ~10 min each (creation + payment processing) = ~1–1.5 hours/store/month. Absorbed.
- **Stock Associate**: staging items in layaway holding adds ~10 min/agreement. Absorbed.
- **No incremental headcount.**

---

## W76. Employee Loans & Advances

| Field | Detail |
|---|---|
| **Trigger** | Employee requests salary advance, calamity loan, or company-internal loan |
| **Frequency** | ~100–200 loan/advance requests/month chain-wide; spikes after typhoons (W49) and during enrollment season (May–August) |
| **Volume** | Salary advances: PHP 5,000–20,000; Calamity loans: PHP 10,000–50,000; Company loans: PHP 10,000–100,000 |
| **Owner** | HR Assistant (intake); Payroll Officer (processing) |
| **Participants** | Employee, Department Head / Store Manager, HR Assistant, Payroll Officer, Finance Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Employee submits loan/advance request in self-service portal (W51) or paper form to HR Assistant: type (salary advance, calamity loan, company loan), amount, reason, proposed repayment period | Employee | — | 10 min |
| 2 | HR Assistant verifies eligibility: (a) salary advance — employee must be regular status, employed ≥ 6 months, no outstanding salary advance; limit = 1× basic monthly salary; (b) calamity loan — triggered by declared natural disaster (W49) affecting employee's residence; limit = 2× basic monthly salary; requires disaster declaration or barangay certification; (c) company loan — employee must be regular status, employed ≥ 1 year, no outstanding loan delinquency; limit = 3× basic monthly salary; requires documented purpose (medical, education, housing repair) | HR Assistant | HR Head | 15 min/request |
| 3 | Approval per tier: (a) salary advance ≤ PHP 20,000: Store Manager / Dept. Head; (b) calamity loan ≤ PHP 50,000: HR Head + Finance Manager; (c) company loan ≤ PHP 100,000: HR Head + CFO; (d) > PHP 100,000: CEO | Approver | Approver | 10 min/request |
| 4 | Payroll Officer creates loan record in system: principal amount, disbursement date, repayment schedule (typically 3–6 monthly installments for salary advance; 6–12 months for calamity/company loan), interest rate (salary advance: 0% per company policy; calamity loan: 0% per DOLE guidance; company loan: 6% per annum or BIR-prescribed minimum per arm's-length rules if officer/owner), monthly deduction amount | Payroll Officer | Payroll Manager | 10 min/loan |
| 5 | System disburses loan: salary advance included in next semi-monthly payroll run as a separate non-taxable line item (Dr. Employee Loans Receivable / Cr. Cash); calamity and company loans processed via separate bank transfer (Dr. Employee Loans Receivable / Cr. Cash) within 3 business days of approval | System / Treasury Analyst | Payroll Manager | Automated + 15 min |
| 6 | System automatically deducts monthly loan repayment from employee's payroll per schedule (Dr. Cash / Cr. Employee Loans Receivable); deduction appears as separate line on payslip; if employee's net pay would fall below minimum wage after deduction, system reduces deduction amount and extends repayment period | System | — | Automated |
| 7 | Monthly: Payroll Officer generates loan portfolio report — total outstanding loans by type, aging (current vs. overdue), delinquency rate, new disbursements, collections; Finance Manager reviews for provisioning adequacy | Payroll Officer | Finance Manager | 1 hour/month |
| 8 | **Employee separation with outstanding loan**: at separation (W43), Payroll Officer settles outstanding loan balance from final pay (W10 step 12) — system deducts remaining principal and accrued interest from final pay before other deductions; if final pay insufficient to cover full loan balance, employee signs promissory note for remaining balance and Payroll Officer tracks post-employment collection; write-off per Controller approval if uncollectible | Payroll Officer / Controller | Finance Manager | Per W43 |

### System Touchpoints
- Loan/advance request form in self-service portal with eligibility validation (employment status, tenure, outstanding loans) (W76.1–2)
- Loan record creation with amortization schedule and automatic payroll deduction (W76.4, W76.6)
- Loan disbursement via payroll or bank transfer with GL posting (W76.5)
- Loan portfolio reporting: outstanding, aging, delinquency, disbursements, collections (W76.7)
- Final pay settlement of outstanding loans at separation (W76.8)
- Minimum wage protection: system ensures net pay does not fall below minimum wage after loan deduction (W76.6)
- Integration with W10 (payroll deduction), W43 (separation — final pay settlement), W49 (calamity loan trigger), W51 (self-service portal)

### Staffing Implication
- **HR Assistant**: ~100–200 requests/month × 15 min = ~25–50 hours/month. Absorbed within existing 2 HR Assistants.
- **Payroll Officer**: loan creation + portfolio reporting adds ~15 hours/month. Absorbed within existing payroll team.
- **No incremental headcount.**

---

## W77. BIR Tax Audit Response

| Field | Detail |
|---|---|
| **Trigger** | BIR issues Letter of Authority (LOA) or audit notification to any BuildRight entity |
| **Frequency** | Occasional; estimated 1–2 BIR audits/year across 5 entities; higher probability for entities with large revenue or import activity |
| **Volume** | Audit scope varies — from specific tax type (VAT only) to comprehensive (income tax, VAT, withholding tax) for 1–3 taxable years |
| **Owner** | Tax Accountant (operational); Controller (oversight); CFO (escalation) |
| **Participants** | Tax Accountant, Controller, CFO, Chief Accountant, AP Clerk, AR Clerk, IT, Legal, external tax advisor, BIR Revenue Officers |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | BIR Revenue Officer presents Letter of Authority (LOA) at entity's registered office or BIR Regional Office; Tax Accountant receives and logs LOA in system: LOA number, audit period, tax types under audit, assigned Revenue Officers, deadline for submission | Tax Accountant | Controller | 30 min |
| 2 | Controller and CFO assess audit scope and risk; engage external tax advisor (CPA firm) for audit representation if assessment is complex or potential exposure is material (> PHP 1M) | Controller / CFO | CEO | 1 hour |
| 3 | Tax Accountant gathers documents per BIR requirements — system generates: (a) books of accounts (general journal, general ledger, cash receipts/disbursements journals, sales/purchases journals) per BIR format and CAS permit (W54a), (b) VAT returns and supporting schedules for audit period, (c) withholding tax returns (1601-E, 1601-C) and alphalist of payees, (d) income tax returns and supporting financial statements, (e) summary of credit/debit notes, (f) list of related-party transactions and IC pricing documentation per W14, (g) fixed asset register and depreciation schedules, (h) inventory records and physical count reports (W42) | Tax Accountant / Chief Accountant | Controller | 2–5 days |
| 4 | Tax Accountant prepares working papers reconciling tax returns to books of accounts; identifies and documents any discrepancies or areas of exposure before submission to BIR | Tax Accountant | Controller | 3–5 days |
| 5 | Tax Accountant or external tax advisor submits documents to BIR Revenue Officers per LOA deadline; logs submission date and receipt confirmation in system | Tax Accountant | Controller | 1 day |
| 6 | BIR conducts examination: Revenue Officers may request additional documents, clarifications, or schedule meetings/walkthroughs; Tax Accountant coordinates responses within 5 business days per BIR practice | Tax Accountant / Controller | CFO | Varies (weeks to months) |
| 7 | BIR issues Preliminary Assessment Notice (PAN) if deficiencies found; Tax Accountant and external tax advisor review PAN; prepare protest or rebuttal within 15 days of receipt if assessment is disputed | Tax Accountant / External Advisor | CFO | 3–5 days |
| 8 | If protest accepted by BIR: case closed; Tax Accountant documents final resolution. If BIR issues Final Assessment Notice (FAN): Tax Accountant evaluates options — (a) accept assessment and pay deficiency tax + surcharge + interest; (b) escalate to Court of Tax Appeals or file motion for reconsideration within 30 days | Tax Accountant / CFO / Legal | CEO | 3–10 days |
| 9 | If payment required: Treasury processes payment per W30; system posts payment (Dr. Tax Payable / Dr. Tax Penalty Expense / Cr. Cash); Tax Accountant files amended returns if applicable | Treasury Analyst / Tax Accountant | CFO | Per W30 |
| 10 | Post-audit: Controller and Tax Accountant conduct lessons-learned review; document findings and corrective actions to prevent recurrence; update internal tax compliance procedures (W9a) if needed; include audit outcomes in next quarterly management committee meeting (W35.14) | Controller / Tax Accountant | CFO | 2 hours/audit |
| 11 | Quarterly: Tax Accountant maintains BIR audit readiness checklist: confirm books of accounts are current and BIR-compliant, withholding tax alphalists reconcile to returns, IC transfer pricing documentation is complete per W14, CAS permit is current per W54a, all tax returns filed on time | Tax Accountant | Controller | 2 hours/quarter |

### System Touchpoints
- BIR audit register: LOA number, audit period, tax types, Revenue Officers, submission deadlines, assessment amounts, protest status, resolution date (W77.1)
- Books of accounts generation in BIR-prescribed format per CAS permit (W77.3, cross-reference W54a)
- Tax return and supporting schedule retrieval for audit periods (W77.3)
- Document submission tracking with deadline alerting (W77.5)
- Assessment tracking with protest deadline management (W77.7–8)
- Integration with W9a (month-end close — source of audit documents), W14 (IC transfer pricing documentation), W30 (payment of deficiencies), W35 (management reporting), W54a (CAS permit compliance)

### Staffing Implication
- **Tax Accountant**: audit response adds ~40–80 hours per audit over 2–4 months. Absorbed within existing role with priority reallocation during active audits.
- **External tax advisor**: engaged for complex audits; budgeted within Finance operations.
- **No incremental headcount.**

---

## W78. Government / Institutional Procurement Participation

| Field | Detail |
|---|---|
| **Trigger** | Government agency, LGU, or state-owned enterprise issues Invitation to Bid or Request for Quotation (RFQ) for construction materials, hardware, or related supplies |
| **Frequency** | ~20–40 government procurement opportunities/year; primarily infrastructure agencies (DPWH), LGUs, DepEd, DOH, and state universities |
| **Volume** | Individual contract values PHP 500K–20M; represents ~5–8% of total revenue |
| **Owner** | Sales Rep (Trade & Corporate) — dedicated government accounts representative |
| **Participants** | Sales Rep, Category Manager, Pricing Analyst, Legal, Finance, Supply Planner |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Sales Rep monitors government procurement opportunities: PHILGEPS (Philippine Government Electronic Procurement System) portal, agency websites, and newspaper postings per RA 9184 (Government Procurement Reform Act); identifies opportunities matching BuildRight's product range | Sales Rep | VP Merchandising | 2 hours/week |
| 2 | Sales Rep evaluates opportunity viability: (a) product match — does BuildRight carry the specified items or equivalents, (b) delivery capability — can BuildRight deliver to the agency's required locations within the specified timeline, (c) pricing competitiveness — can BuildRight meet the Approved Budget for the Contract (ABC), (d) eligibility — does BuildRight meet PHILGEPS registration, BIR tax compliance, and other bidder eligibility requirements | Sales Rep | Category Manager | 1–2 hours/opportunity |
| 3 | Sales Rep prepares bid/quote documents per agency requirements: (a) PHILGEPS registration certificate, (b) BIR tax compliance certificate, (c) business permits per W54, (d) audited financial statements (most recent year from W9b), (e) similar completed projects or supply contracts, (f) product specifications and pricing, (g) delivery schedule and terms, (h) bid security (if required) | Sales Rep / Legal | VP Merchandising | 4–8 hours/bid |
| 4 | Category Manager and Pricing Analyst review proposed pricing: ensure margin is adequate (minimum gross margin target for government contracts, typically 10–15%); verify that pricing does not violate any existing contract pricing or trade agreements | Category Manager / Pricing Analyst | VP Merchandising | 1–2 hours/bid |
| 5 | Sales Rep submits bid/quote per agency deadline (sealed bid, electronic submission, or direct quotation depending on procurement method per RA 9184) | Sales Rep | VP Merchandising | Per deadline |
| 6 | **If awarded**: Sales Rep creates Sales Order in system linked to government Purchase Order; applies government-specific pricing and delivery schedule; system creates delivery plan per W19 or in-store pickup per W11 (BOPIS); revenue recognized at delivery per standard process | Sales Rep | Finance Manager | Per W58 |
| 7 | **Billing**: Sales Rep generates billing documents per government agency requirements — (a) standard sales invoice with BIR-registered format, (b) delivery receipt signed by agency receiving officer, (c) collection receipt per agency's accounting procedures; government accounts typically on Net 30–60 terms; collection requires submission of complete billing documents per agency-specific procedures (some agencies require liquidation documents or progress reports) | Sales Rep / AR Clerk | AR Supervisor | Per W8 |
| 8 | **Collection**: AR Clerk follows up on government receivables per W8 collection tiers; government payments may be delayed due to budget processing — Sales Rep coordinates with agency procurement officer and accounting division; system tracks government receivable aging separately from trade accounts for reporting | AR Clerk / Sales Rep | AR Supervisor | Per W8 |
| 9 | Quarterly: Sales Rep and Category Manager review government account portfolio: win rate, revenue, margin, collection timeliness, and bid pipeline; VP Merchandising reviews as part of corporate account portfolio (W58.10) | Sales Rep / Category Manager | VP Merchandising | 2 hours/quarter |

### System Touchpoints
- PHILGEPS registration tracking in vendor/customer master with renewal alerting (W78.1)
- Government customer account with specialized billing requirements, delivery terms, and collection procedures (W78.6–8)
- Government-specific pricing and margin validation per W40 approval workflow (W78.4)
- Government receivable aging separate from trade accounts for reporting and collection management (W78.8)
- Integration with W8 (AR and collections), W19 (delivery), W24 (credit application — government accounts may use purchase orders instead of credit), W40 (pricing), W54 (LGU permits — build compliance documentation), W58 (corporate account management)

### Staffing Implication
- **1 Sales Rep (dedicated government accounts)**: within the existing 3–4 Sales Reps (Trade & Corporate) per W58, one rep should specialize in government accounts given the unique procurement regulations and document requirements; PHILGEPS monitoring and bid preparation add ~8–12 hours/week during active bidding periods.
- **No incremental headcount.** Absorbed within existing B2B sales team.

---

## W79. Employee Grievance & Whistleblower Process

| Field | Detail |
|---|---|
| **Trigger** | Employee files a grievance regarding workplace conditions, policy violations, harassment, discrimination, or unethical conduct; or whistleblower report of fraud, corruption, or legal non-compliance |
| **Frequency** | Estimated 20–50 grievance/whistleblower reports/year across all locations |
| **Volume** | Grievance categories: workplace conflict (30%), policy/procedure concern (25%), compensation/benefits dispute (20%), harassment/discrimination (15%), safety concern (10%) |
| **Owner** | HR Head (grievance); Internal Audit (whistleblower reports involving management) |
| **Participants** | Employee, HR Head, Internal Audit, Legal, Department Head / Store Manager, CHRO |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Employee submits grievance or whistleblower report via: (a) **grievance form** in self-service portal (W51) or paper form to HR — identifies issue, parties involved, date(s), and desired resolution; (b) **whistleblower channel** — dedicated email or anonymous hotline (managed by HR Head or third-party hotline provider) for reports of fraud, corruption, or legal non-compliance where anonymity is protected | Employee | — | 15 min |
| 2 | HR Head (grievance) or Internal Audit (whistleblower) acknowledges receipt within 24 hours; assigns case number; classifies severity: (a) low — interpersonal conflict, minor policy concern, (b) medium — repeated policy violation, compensation dispute, (c) high — harassment, discrimination, safety violation, (d) critical — fraud, corruption, legal non-compliance | HR Head / Internal Audit | CHRO | 15 min/case |
| 3 | **For low/medium severity (HR Head investigates)**: (a) HR Head interviews employee (complainant) within 3 business days — documents complaint details; (b) HR Head interviews respondent(s) and any witnesses within 5 business days — documents responses; (c) HR Head reviews relevant evidence (system records, CCTV, emails, documents) | HR Head | CHRO | 4–8 hours/case |
| 4 | **For high/critical severity**: (a) harassment/discrimination — HR Head and Legal jointly investigate; respondent may be placed on preventive suspension (with pay) per Labor Code during investigation if warranted by severity; (b) fraud/corruption — Internal Audit investigates; if management is implicated, CHRO and CEO are notified directly (bypassing implicated management); (c) safety concern — HR Head and Facilities Coordinator investigate per W47 | HR Head / Legal / Internal Audit | CHRO / CEO | 8–20 hours/case |
| 5 | **Resolution options**: (a) mediation — HR Head facilitates mediation between parties for interpersonal conflicts; both parties agree to resolution terms; (b) corrective action — policy violation confirmed; HR Head issues written warning or corrective action per progressive discipline policy; (c) policy clarification — grievance resolved by clarifying or correcting a policy/procedure; (d) escalation — if unresolved at HR Head level, employee may escalate to CHRO within 5 business days; (e) grievance committee — for complex or unresolved cases, CHRO convenes a 3-person grievance committee (HR, Legal, and independent management representative) for hearing and binding recommendation | HR Head / CHRO | CEO | Varies |
| 6 | HR Head documents resolution in system: case number, investigation summary, evidence reviewed, findings, resolution action, date resolved; all documentation retained per 7-year BIR/regulatory retention; whistleblower identity protected in documentation | HR Head | CHRO | 30 min/case |
| 7 | **Retaliation protection**: system flags if any adverse action (demotion, transfer, schedule change, disciplinary action) is taken against an employee with an active or recently resolved grievance/whistleblower case within 90 days of filing; such actions require CHRO approval to prevent retaliation | System / HR Head | CHRO | Automated flag + 15 min/review |
| 8 | Quarterly: HR Head generates grievance/whistleblower summary for CHRO — volume by category, severity, location, resolution time, corrective actions taken, repeat offenders, systemic issues identified; CHRO reports aggregate metrics (anonymized) to CEO in quarterly management committee (W35.14) | HR Head | CHRO | 2 hours/quarter |
| 9 | Annual: CHRO reviews grievance trends with Legal; recommends policy or training improvements; findings feed into W51 training calendar and W72 performance management process | CHRO / Legal | CEO | 2 hours/year |

### System Touchpoints
- Grievance submission form in self-service portal with category, severity, and desired resolution fields (W79.1)
- Anonymous whistleblower channel (email or third-party hotline) integration with case management (W79.1)
- Case management with severity classification, investigation tracking, evidence attachment, and resolution documentation (W79.2–6)
- Retaliation protection: system flags adverse actions against grievance filers within 90-day lookback (W79.7)
- Grievance/whistleblower analytics: volume, category, severity, location, resolution time (W79.8)
- Integration with W10 (payroll — preventive suspension with pay), W43 (separation — pending grievance resolved before clearance), W47 (safety concerns), W51 (self-service portal, training improvements), W72 (corrective action and progressive discipline)
- Whistleblower anonymity technical controls: the anonymous whistleblower channel (dedicated email or third-party hotline) is configured with the following technical safeguards: (a) no IP address logging on the whistleblower submission form; (b) no employee ID or session token capture on anonymous submissions; (c) if third-party hotline is used, the provider contractually commits to not disclosing reporter identity to BuildRight management; (d) system stores whistleblower case records with a pseudonymous case ID — the real identity is accessible only to the DPO and Internal Audit lead (dual-access control); (e) retaliation protection (W79.7) is extended to anonymous reporters where identity is later inferred or disclosed; (f) annual: DPO reviews whistleblower channel anonymity safeguards as part of privacy impact assessment (W53)

### Staffing Implication
- **HR Head**: grievance investigation adds ~20–40 hours/year. Absorbed within existing role.
- **Internal Audit**: whistleblower investigation adds ~10–20 hours/year. Absorbed.
- **No incremental headcount.** Grievance handling is a core HR function distributed across existing management.

---

### HQ Departments

| Department | Roles | Count | Key Workflows | Validation |
|---|---|---|---|---|
| **Merchandising & Buying** | VP, Category Managers, Buyers, Pricing Analysts, Merch Planners | ~40 | W1, W2, W13, W20, W23, W27, W29, W32, W36, W40, W44, W68 | ✅ Adequate for daily PO review + quarterly assortment cycles + VMI/consignment oversight + rebate management + seasonal planning + vendor onboarding + price maintenance + product discontinuation lifecycle; includes 1–2 dedicated Buyers for trade/special orders (W38) within the ~40 team |
| **Finance & Accounting** | Controller, Chief Accountant, AP/AR Clerks, Treasury, Tax | ~35 | W7, W7d, W8, W9, W14, W21, W24, W25, W26, W27, W28, W30, W39, W42, W54a (CAS permit validation), W59, W60, W70, W74 | ✅ Stretched during close week; capex/credit/petty cash absorbed; treasury daily cycle manageable with 2–3 analysts; asset disposal and annual physical inventory absorbed; insurance lifecycle and emergency procurement review absorbed; credit/debit note reconciliation absorbed into month-end close and weekly AP/AR review; AP staffing recalculated on business-day basis: ~305–370 invoices/business-day (6,500 merchandise + 2,000–3,000 non-PO per month ÷ 22 business days) requiring 10 clerks at ~5–6 hrs each/day; month-end peak (+50%) requires overtime or Finance staff redeployment; vendor statement reconciliation (W7d) absorbed into monthly AP cycle; employee expense reimbursement (W74) adds ~25–42 hours/month absorbed across AP team |
| **Supply Chain & Logistics** | Supply Planners, Demand Planners, Import Coordinator, Fleet Manager, DC Ops managers | ~31 | W3, W3c, W4, W4b, W19, W19b, W22, W22b, W31, W52, W56, W57, W62b, W66 | ✅ 2–3 planners handle replenishment + store-initiated requests + transfers + backorder fulfillment + promo allocation; home delivery and ship-from-store picked by DC/store staff; 1–2 dedicated demand planners handle forecasting; 1 Fleet Manager manages owned vehicles and 3PL relationships; Import Coordinator absorbs inter-island logistics; DC inbound scheduling (W3c) absorbed by DC Receiving Supervisor; 3PL partner onboarding (W62b) absorbed by Fleet Manager; allocation rule governance reviewed quarterly as part of W31.8 parameter cycle |
| **HR & Payroll** | HR Head, Recruitment, Payroll, Training Officer, HR Assistants | ~16 | W10, W15, W51, W72 | ✅ 2–3 payroll officers + 2 recruiters + 1 Training Officer handle the volume; employee performance management absorbed by ~230 managers |
| **Marketing** | Brand, Promo, Loyalty, Ecommerce, Digital, Content, CS Manager | ~24 | W13, W17, W50, W61, W65 | ✅ Loyalty is largely automated; promo work is cyclical; dedicated Content Manager + 2–3 Content Specialists for ecommerce product content; CS Manager owns customer satisfaction measurement; price match review absorbed by Pricing Analysts |
| **Store Operations** | Director, Regional Managers, CS Manager, Ops Standards, Facilities Coordinator | ~23 | W5, W5d (in-store delivery), W5e (opening delay), W16, W29, W5f (offline recovery), W34, W37, W41, W47, W49, W54a, W67, W69, W71 | ✅ 4 Regional Managers × 50 stores each; oversee new openings and monthly store performance reviews; in-store delivery uses existing 3PL carrier infrastructure; opening delay procedure is Store Mgr responsibility; offline recovery is Store Mgr responsibility; shift scheduling and complaint handling absorbed; 2–3 LPOs recommended for loss prevention; 1 Facilities Coordinator manages store maintenance, disaster response, and physical security oversight; weekly price compliance audits absorbed by Dept. Supervisors and Stock Associates |
| **IT** | Infrastructure, Apps, Data, Security, BI Analyst, Helpdesk | ~28–30 | W16 (store setups), W35 (reporting), W48 (helpdesk & IT ops) | ✅ 4–5 helpdesk agents + 3–4 specialists handle ~800–1,200 tickets/month; 2–3 per store setup + BAU support; 1 BI Analyst supports management reporting; note: for physical IT support across the Philippine archipelago (200 stores + 5 DCs across Mindanao, Visayas, Luzon), 1–2 dedicated field staff may not provide adequate same-day response for P1 incidents in remote locations — recommend (a) training designated Store Managers as first-level hardware troubleshooters (certified on basic POS terminal swap, cable reseat, network restart), (b) contracting regional IT service providers in each major region (Davao, Cebu, Manila, Clark) for emergency on-site support, and (c) maintaining a spare POS terminal and network equipment swap stock at each DC for rapid dispatch |
| **Other** | Legal, Internal Audit, DPO, Regulatory Officer, Customer Service (call center), Executive | ~52 | W41 (complaints), W42 (audit observation), W53 (data privacy breach, DSAR lifecycle, data portability/erasure), W54 (LGU permits), W54a (BIR CAS registration), W62 (vendor contracts) | ✅ Support functions; call center handles multi-channel complaint intake; Legal expanded to include DPO (W53 with full DSAR lifecycle) and Regulatory Officer (W54 LGU + W54a BIR CAS); total Legal & Compliance expands from ~5 to ~7 |

### Per-Store Staffing (35 people)

| Role | Count | Key Workflows | Workload Validation |
|---|---|---|---|
| Store Manager | 1 | W5 (open/close), W5d (in-store delivery coordination), W5e (opening delay handling), W6 (approvals), W12 (returns), W16 (opening), W22b (store-to-DC returns), W54 (LGU permit coordination), W67 (monthly performance review), W69 (price audit review) | Manageable; delegates floor ops to supervisors |
| Asst. Store Manager | 1 | W5 (open/close backup), W6, W12 | Shares management load; covers days off |
| Dept. Supervisors | 4 | W5b (floor selling), W6 (cycle count review), W12 (restock), W69 (price compliance audit execution and review) | 4 depts × 1 supervisor; handles floor + counts + weekly price audits |
| Sales Associates | 16 | W5b (selling, paint mixing, lumber cutting), W5d (in-store delivery staging), W11 (BOPIS pick), W56 (backorder intake), W61 (price match verification) | 4/dept × 2 shifts = adequate for floor coverage |
| Cashiers | 6 | W5b (checkout), W17 (loyalty scan), W28 (gift card sell/reload) | 5 terminals + 1 float; 2 shifts of 3; tight on coverage |
| Receiving Clerks | 2 | W4 (store receiving from DC), W18 (DSD receiving), W22 (transfer receiving), W22b (store-to-DC return staging) | 2–3 DC trucks/week + 2–3 DSD/week + transfers + return staging; 2 clerks in shifts handle it |
| Stock Associates | 3 | W4 (shelf stocking), W4b (store replenishment request), W6 (cycle counting), W11 (BOPIS pick), W18 (DSD shelving), W19b (ship-from-store picking), W22 (transfer pick/receive), W22b (store-to-DC return packing), W34 (shift adherence), W42 (annual count), W57 (promo stock staging), W63 (shelf label application), W69 (price audit scanning) | 700 SKUs/day counting + stocking + DSD + transfers + label updates + weekly price audit; adequate but minimal slack |
| Customer Service Rep | 1 | W11 (BOPIS handoff), W12 (returns), W24 (credit application assistance), W28 (store credit), W29 (recall returns), W33 (warranty claims), W38 (special order intake), W41 (complaints) | ~4 BOPIS + ~2 returns + ~0.5 gift cards + ~2 warranty claims + ~0.5 special orders + ~10 complaints/day = moderate; also handles special orders |
| Maintenance | 1 | W5c (closing checklist), W47 (facility maintenance & work orders), general upkeep | Standard for big-box format; handles ~10–15 maintenance work orders/month including preventive tasks; external contractors engaged for specialized repairs |
| **Total** | **35** | | **Validated — headcount is lean but supportable** |

### Per-DC Staffing (~150 people)

| Function | Count | Key Workflows | Workload Validation |
|---|---|---|---|
| DC Manager + Supervisors | 5 | W3, W4 (oversight) | 1 manager + 4 shift/area supervisors |
| Receiving | 10–13 | W3 (receiving & putaway), W20 (VMI receipt) | ~40 receipts/day × 1.5–3 hrs; 3–4 clerks + 4–6 putaway + 1–2 QC |
| Picking & Packing | 25–30 | W4 (pick/pack/ship), W19 (home delivery pick/pack) | ~33 store orders + ~115 home delivery orders/day; 15–20 pickers + 8–10 packers; 3–4 dedicated to home delivery; peak ecommerce periods may require surge staffing |
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
| **POS / Retail** | W5 (store selling, in-store delivery order creation at POS, opening delay procedure, offline recovery, void transactions, trade/corporate account pricing with new customer application cross-reference, VAT-exempt/zero-rated sales processing, VMI/consignment GL routing), W12 (returns including cross-store returns, split-tender refunds, loyalty points reversal), W17 (loyalty at POS), W18 (DSD receiving), W23 (consignment sale), W28 (gift card/store credit), W29 (recall blocking), W33 (warranty claims), W38 (special order deposit, customer deposit refund), W58 (quotation-to-order conversion at POS), W61 (competitor price match with WAC floor enforcement), W69 (price compliance audit scanning at POS/handheld) |
| **Inventory Management** | W3 (GR posting, shelf-life/expiry tracking, perpetual WAC at receipt, inventory ownership clarification, RTV logistics tracking, DC RTV consolidation & vendor batch shipment, quality inspection standards with category-specific checklists and AQL sampling, quality hold process), W4 (replenishment, FEFO picking, intra-entity ownership note, new store demand ramp-up), W4b (store-initiated replenishment request with supply position dashboard), W6 (cycle counting, near-expiry alerting), W11 (BOPIS pick), W12c (cross-store return inventory adjustment, loyalty points reversal), W18 (DSD GR, shelf-life capture), W20 (VMI stock, quarterly vendor statement reconciliation), W22 (transfers, transfer discrepancy resolution, customer-initiated inter-store transfer, catch-weight item measurement), W22b (store-to-DC return with reason-based disposition routing), W23 (consignment tracking, consignment returns, quarterly vendor statement reconciliation), W29 (recall quarantine), W37 (confirmed theft write-off, shrinkage tracking), W42 (annual physical inventory, vendor-owned inventory count, tiered counting strategy with C-item extrapolation methodology, freeze mitigation), W46 (kit assembly/disassembly), W56 (backorder allocation and reservation), W57 (promo stock allocation tracking), W66 (inter-island freight cost allocation), W68 (product discontinuation — status lifecycle, last buy, clearance with pricing conflict rules, archival), W69 (price audit — shelf tag accuracy verification), negative inventory resolution |
| **Procurement** | W2 (PO cycle, PO amendment/cancellation/close lifecycle), W3 (receiving vs. PO), W18 (DSD PO/GR), W20 (VMI ASN), W21 (capex PO), W36 (vendor onboarding, lead time master data lifecycle, bank account change control, vendor master data change log), W38 (special order PO), W57 (expedited promo stock PO), W60 (emergency procurement with vendor TBD mode) |
| **Warehouse Management** | W3 (putaway, cross-dock, forward-pick replenishment), W4 (pick/pack/ship), W19 (home delivery pick/pack), W22 (transfer pick), W42 (DC count), W46 (kit assembly) |
| **Financials (GL/AP/AR)** | W7 (AP, EWT, vendor credit memos, non-PO recurring expenses, total AP volume reconciliation), W8 (AR, credit hold override, customer credit memos, dormant account management), W9 (close, NRV review, WAC verification, inventory write-off, credit note reconciliation, LBT per LGU, VAT-exempt/zero-rated sales reporting), W14 (intercompany, IC settlement timing, goods-based IC trigger scenarios, IC invoice dispute resolution), W21 (capex & FA), W24 (credit approval, VAT treatment classification), W25 (petty cash, store disbursement requests, petty cash-to-treasury reconciliation link), W26 (budget), W27 (rebates), W28 (gift card liability, cross-channel redemption IC), W30 (treasury & cash management, ecommerce payment reconciliation, cash-in-transit, petty cash reconciliation, store-level cash position tracking), W37 (confirmed theft write-off), W39 (asset disposal), W42 (inventory adjustments), W59 (insurance policy lifecycle, claims tracking), W60 (emergency procurement regularization), W70 (credit/debit note aging reconciliation, auto-application, sub-ledger reconciliation, write-off workflow) |
| **Supply Chain Planning** | W2a (auto-replenishment), W4 (replenishment calculation), W4b (store-initiated replenishment request review and approval), W22 (transfer planning), W22b (store-to-DC return approval), W27 (rebate accrual triggers), W31 (demand forecasting, multi-echelon DC replenishment sourcing, ROP parameter governance, DC multi-dimensional capacity planning dashboard), W32 (seasonal buy planning), W56 (backorder demand linkage to PO), W57 (promo stock allocation and pre-positioning), W64 (new product pilot store allocation), W66 (inter-island freight planning) |
| **HR & Payroll** | W10 (payroll), W15 (onboarding), W34 (shift scheduling, attendance exception handling), W43 (separation & offboarding, cross-entity employee transfer), W72 (employee performance management) |
| **Ecommerce** | W11 (BOPIS order flow, IC settlement, ecommerce VAT), W12b (online returns, home delivery reverse logistics), W19 (home delivery fulfillment, payment reconciliation, 3PL management, reverse logistics, IC settlement, ecommerce VAT), W19b (ship from store — multi-origin fulfillment, store pick and carrier dispatch) |
| **CRM / Loyalty** | W17 (loyalty program, manual points adjustment, customer deduplication, ecommerce points earning, tier downgrade proactive communication, clarified deferred revenue accounting), W24 (credit application, VAT treatment classification), W41 (complaint management), W56 (backorder customer notifications), W58 (corporate/project account management), W65 (CSAT/NPS measurement) |
| **Pricing / Merchandising** | W13 (promotions, pricing conflict rules, vendor-funded promo settlement), W27 (vendor rebates), W40 (regular price changes, price protection, quantity break pricing setup & maintenance, loyalty points on discounted transactions), W61 (competitor price match analytics), W63 (shelf label generation from price changes, catch-weight / variable measure item labels) |
| **Master Data** | W1 (SKU lifecycle, sample/demo inventory, slow-mover review), W16 (new store/location creation, capex project tracking), W20 (VMI item setup), W23 (consignment item setup), W36 (vendor onboarding, lead time lifecycle), W38 (non-stock item creation, unclaimed deposit aging), W46 (kit BOM), W54 (LGU permit data per location), W64 (pilot SKU status flag), W68 (product discontinuation status lifecycle and archival) |
| **Reporting / Analytics** | W1 (assortment analysis, competitive intelligence monitoring), W9 (financial statements), W13 (promo analysis), W19 (delivery performance), W21 (capex vs. budget), W26 (budget variance), W27 (rebate ROI), W28 (gift card liability), W29 (recall tracking), W30 (cash flow forecast), W31 (forecast accuracy, ROP parameter governance), W35 (management reporting rhythm, store P&L occupancy cost allocation, store utility consumption benchmarking), W37 (shrinkage/exception reports), W40 (price change analytics, quantity break utilization), W41 (complaint analytics), W42 (physical inventory summary), W44 (vendor scorecards), W56 (backorder aging), W59 (insurance claims vs. premiums), W60 (emergency procurement frequency), W61 (price match analytics), W65 (CSAT/NPS trending), W66 (inter-island logistics cost) |
| **Loss Prevention** | W37 (POS exception monitoring, shrinkage tracking, confirmed theft write-off, CCTV integration with POS timestamp correlation, loyalty fraud detection) |
| **Store Lifecycle** | W16 (new store opening, go-live cutover plan, demand ramp-up first 90 days), W45 (store closure / relocation, financial close-out checklist, LGU permit retirement), W54a (BIR CAS registration — new entity setup before POS transactions), W67 (monthly store performance review), W71 (store physical security & access control) |
| **Facility Maintenance** | W47 (store & DC maintenance, work orders, preventive maintenance scheduling) |
| **IT Operations** | W48 (helpdesk, incident management, change management, IT asset tracking) |
| **Business Continuity** | W49 (natural disaster preparation, response, recovery, insurance claims) |
| **Product Information** | W50 (PIM, content creation, ecommerce catalog management, digital assets, seasonal PIM timeline coordination with W32) |
| **Training & Development** | W51 (training calendar, compliance tracking, certification management, LMS, employee self-service portal) |
| **Fleet Management** | W52 (vehicle lifecycle, fuel management, maintenance scheduling, 3PL carrier oversight) |
| **Data Privacy & Compliance** | W53 (data privacy breach response, breach register, NPC notification, forensic audit trail, DSAR full lifecycle — access, rectification, erasure with BIR retention preservation, data portability, consent withdrawal), W54a (BIR CAS registration, permit tracking, books of accounts compliance) |
| **Regulatory Operations** | W54 (LGU business permit renewal per location, permit status dashboard, location master integration) |
| **IT Disaster Recovery** | W55 (system failover, RTO/RPO enforcement, offline POS reconciliation, DR testing) |
| **Customer Order Management** | W56 (backorder creation, allocation against incoming PO, customer notification, aging escalation) |
| **Corporate Account Management** | W58 (project record, project-specific pricing, cumulative budget tracking, project billing, milestone/progress billing with retention amounts, change orders, account portfolio analytics, customer project quotation lifecycle with one-click conversion to Sales Order, quotation conversion analytics) |
| **Vendor Contract Management** | W62 (non-PO service contract lifecycle, contract register, SLA tracking, auto-renewal management, invoice blocking), W62b (3PL / delivery partner onboarding & offboarding, API integration, carrier master, pilot testing, performance monitoring, partner deactivation with data deletion) |
| **Customer Experience** | W65 (CSAT/NPS measurement, survey platform integration, mystery shopping, satisfaction trending) |
| **Store Operations Management** | W67 (monthly store performance review, store scorecard, action item tracking, Regional Manager review cadence) |
| **Product Lifecycle** | W68 (product discontinuation lifecycle, last buy decision, clearance execution, system archival, vendor settlement) |
| **Price Compliance** | W69 (weekly price compliance audit, shelf tag accuracy verification, audit analytics by category/store) |
| **Credit/Debit Note Reconciliation** | W70 (AP/AR credit/debit note aging, auto-application, sub-ledger reconciliation, write-off workflow, quarterly deep review) |
| **Physical Security** | W71 (store & DC physical security, guard force management, alarm monitoring, key/access badge management, CCTV system health, break-in incident response, security agency contract management) |
| **Employee Performance** | W72 (annual performance review, goal-setting, quarterly check-ins, PIP, promotion identification, performance analytics) |
| **Data Migration & Parallel Run** | W73 (data migration validation per domain, parallel-run testing for payroll/month-end/POS/inventory, UAT, go-live readiness sign-off) |

---

*Document Version: 19.0 | Date: 2026-05-31 | Wave 17: comprehensive gap closure — GAP-01: added W22a store-level outbound transfer fulfillment; GAP-02: added price dispute resolution at POS (W5b.11); GAP-03: added carrier damage vs. vendor defect liability assignment (W19.12b); GAP-04: added goods-based IC system flow detail (W14); GAP-05: added vendor rebate dispute resolution with 15-day SLA (W27); GAP-06: added IT shadow protocol for new store first week (W16); GAP-07: added gift card fraud detection to W37; GAP-08: added employee purchase policy at POS (W5b.12); GAP-09: added dual-sourced item management (W4); GAP-10: added backorder price protection rule (W56); GAP-11: added trade account deposit waiver for special orders (W38.6a); GAP-12: added auto-replenishment queuing during count freeze (W42); GAP-13: added discontinued SKU backorder auto-cancellation (W68.5); GAP-14: added loyalty profile default-store reassignment on closure (W45.13a); GAP-15: expanded applicant tracking in W15; GAP-16: added whistleblower anonymity technical controls (W79); GAP-17: added carrier rate card maintenance with Finance approval (W62b); GAP-18: clarified PFRS 15 gift card breakage accounting method (W28); GAP-19: added DR test failure remediation (W55); GAP-20: fixed all W5d/W5g cross-reference inconsistencies; GAP-21: added AP peak staffing contingency note; GAP-22: separated loyalty face value from PFRS 15 allocation rate; GAP-23: recommended 4 Stock Associates (+1 part-time relief); GAP-24: updated HQ staffing for dedicated special order buyers; GAP-25: added regional IT support recommendations; GAP-26: added 24-hour deposit confirmation enforcement; GAP-27: added CTL-49 to internal controls; GAP-28: added BIR-compliant void receipt documentation*
