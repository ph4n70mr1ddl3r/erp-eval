# Warehouse & Logistics Workflows

> Receiving, putaway, kit assembly, fleet management, and inter-island logistics.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W3. Warehouse Receiving & Putaway](#warehouse-receiving-putaway)
- [W46. Kit / Bundle Assembly & Disassembly](#kit-bundle-assembly-disassembly)
- [W52. Fleet Management](#fleet-management)
- [W66. Inter-Island Logistics & Freight Management](#inter-island-logistics-freight-management)

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



---

