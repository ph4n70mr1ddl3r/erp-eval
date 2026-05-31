# Store Operations Workflows

> Daily store selling, POS, returns, loyalty, DSD receiving, gift cards, new store opening/closure, warranty, facility maintenance, performance review, and planogram compliance.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W5. Daily Store Operations](#daily-store-operations)
- [W5g. Offline POS Recovery & Reconciliation](#offline-pos-recovery-reconciliation)
- [W12. Returns & Exchanges](#returns-exchanges)
- [W16. New Store Opening](#new-store-opening)
- [W17. Customer Loyalty Program Operations](#customer-loyalty-program-operations)
- [W18. Direct Store Delivery (DSD) Receiving](#direct-store-delivery-dsd-receiving)
- [W28. Gift Card & Store Credit Lifecycle](#gift-card-store-credit-lifecycle)
- [W29. Product Recall Execution](#product-recall-execution)
- [W33. Warranty Claim Processing](#warranty-claim-processing)
- [W45. Store Closure / Relocation](#store-closure-relocation)
- [W47. Store Facility Maintenance & Work Orders](#store-facility-maintenance-work-orders)
- [W67. Monthly Store Performance Review](#monthly-store-performance-review)
- [W69. Price Compliance Audit](#price-compliance-audit)
- [W71. Store Physical Security & Access Control](#store-physical-security-access-control)
- [W75. Layaway / Installment Sales](#layaway-installment-sales)
- [W86. Planogram Compliance & Store Layout Verification](#planogram-compliance-store-layout-verification)
- [W96. Store Renovation & Remodel Project](#store-renovation-remodel-project)
- [W109. Store-Level Inventory Receiving & Putaway](#store-level-inventory-receiving-putaway)
- [W111. Store Energy & Utility Consumption Management](#store-energy-utility-consumption-management)
- [W170. Senior Citizen & PWD Discount Compliance (PH Legal)](#senior-citizen--pwd-discount-compliance-ph-legal)
- [W171. Store Physical Security & Yard Patrol Routine](#store-physical-security--yard-patrol-routine)
- [W173. Store-Level Solar Energy Monitoring](#store-level-solar-energy-monitoring)
- [W176. Store-to-DC Reverse Logistics (Consolidation)](#store-to-dc-reverse-logistics-consolidation)
- [W177. Vending & Concessionaire Management](#vending--concessionaire-management)
- [W182. Gift / Home Registry Lifecycle](#gift--home-registry-lifecycle)
- [W205. Employee Purchase Program & Internal Staff Sales](#employee-purchase-program--internal-staff-sales)
- [W206. Mobile POS (mPOS) & Queue-Busting Operations](#mobile-pos-mpos--queue-busting-operations)

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

---

## W75. Layaway & Installment Sales

| Field | Detail |
|---|---|
| **Trigger** | Customer requests to pay for high-ticket item in installments (Layaway or 3rd Party Financing) |
| **Frequency** | ~500–1,000 transactions/month (primarily appliances, tile sets, furniture) |
| **Owner** | Customer Service Rep (CSR) |
| **Participants** | CSR, Cashier, 3rd Party Finance Provider (e.g., Home Credit, Maya), Stock Associate |

### Steps (Layaway — In-house)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer selects items for Layaway; CSR creates **Layaway Order** in system | CSR | — | 15 min |
| 2 | Customer pays initial deposit (typically 20%); system generates Layaway Receipt and payment schedule (e.g., 3 monthly payments) | Cashier | — | 5 min |
| 3 | **Inventory Hold**: System reserves stock in backroom (or specific "Layaway Area"); item status set to "Reserved — Layaway" | Stock Associate | Dept Supervisor | 15 min |
| 4 | Periodic Payments: Customer returns to pay installments; system updates Layaway balance; prints updated schedule | Cashier | — | 5 min |
| 5 | Final Payment: Once balance is zero, system releases stock for pick-up/delivery | System / CSR | — | 5 min |
| 6 | **Default Handling**: If customer fails to pay within agreed period (e.g., 90 days), system alerts CSR; store contacts customer; if cancelled, stock returned to shelf; deposit forfeited or converted to Store Credit (W28) per policy | CSR | Store Manager | 15 min |

### Steps (3rd Party Installment / Financing)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer selects item; applies for financing via 3rd party partner (in-store kiosk or app) | Customer | — | 15–30 min |
| 2 | Partner provides Approval Code; CSR enters Approval Code into POS as "Financing" tender type | CSR / Cashier | — | 5 min |
| 3 | System treats as "Fully Paid" (Partner owes BuildRight); releases stock for immediate delivery | System | — | Automated |
| 4 | **Settlement**: Finance reconciles Partner payments against POS Approval Codes weekly; posts Partner commission/fees | Finance | — | 1 hour/week |

### System Touchpoints (Layaway/Installment)
- Layaway Order type with deposit and balance tracking
- Inventory reservation (soft-commit vs. hard-commit to backroom)
- Automated payment schedule and overdue alerts
- 3rd Party Financing tender type at POS with reference code capture
- Partner settlement reconciliation reports

### Staffing Implication
- **CSR**: ~4–6 warranty claims/store/month × ~15 min each = ~1–1.5 hours/store/month. Absorbed within existing CSR role.
- **Buyer**: Warranty claims that need vendor follow-up add ~5 min/claim. With ~800–1,200 claims/month, not all require buyer intervention (many are direct replacements). Estimated ~200–300 needing buyer action = ~20–25 hours/month across 10–12 buyers = ~2 hours/buyer/month. Absorbed.
- No incremental headcount needed.

---



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
| 3 | Closing: guard monitors final customer exit; secures receiving dock; performs exterior walkthrough; arms alarm system after Store Manager confirms all staff departed (W5f step 9) | Security Guard | Store Manager | 15 min |
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
- Integration with W5a (opening security check), W5f (closing alarm activation), W37 (loss prevention — CCTV integration, confirmed theft), W47 (alarm system maintenance), W48 (IT helpdesk — CCTV camera restoration), W59 (insurance claims for theft/vandalism), W62 (security agency contract management)

### Staffing Implication
- **Security guards**: 2 guards per store × 200 stores = 400 guards (contracted through security agency, not BuildRight employees); 3–4 guards per DC × 5 DCs = 15–20 guards; relief/absence coverage adds ~10% buffer; total contracted guard force: ~460–480 including reliefs.
- **Facilities Coordinator**: adds ~4–6 hours/month for physical security oversight across 200 stores. Absorbed within existing recommended role.
- **No incremental BuildRight headcount.** Guard force is a contracted service.

---



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



---


## W86. Planogram Compliance & Store Layout Verification

| Field | Detail |
|---|---|
| **Trigger** | Monthly planogram audit schedule; or new planogram release from Merchandising; or post-reset verification after promotional display change |
| **Frequency** | Monthly audit per store (all 200 stores); ad-hoc after planogram resets or new store openings (W16) |
| **Volume** | 200 stores × 4–6 departments per store = ~800–1,200 department-level audits/month; each department contains 50–200 SKUs in the planogram |
| **Owner** | Department Supervisor (in-store execution); Merchandise Planner (planogram design) |
| **Participants** | Department Supervisor, Stock Associate, Merchandise Planner, Store Manager, Regional Manager |

### Background

Planograms define the visual layout of products on store shelves — which SKUs go where, how many facings, at what height, and in what sequence. Planogram compliance ensures that stores display products according to the approved layout, maximizing sell-through, customer navigation, and brand consistency across all 200 locations. While W63 covers shelf label accuracy and W69 covers price compliance, there is no workflow for verifying that products are physically placed in the correct locations according to the planogram.

### Planogram Design & Distribution

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Merchandise Planner creates or updates planogram per category using planogram design tool: (a) defines shelf layout — bay heights, shelf positions, SKU-to-shelf assignment, number of facings, adjacent product rules, (b) incorporates category management insights from W1 assortment review — new SKUs added, discontinued SKUs removed, space allocation adjusted based on sales velocity, (c) considers fixture type per store format (standard vs. compact stores), (d) generates planogram document per department per store format with visual layout, SKU placement map, and compliance checklist | Merchandise Planner | Category Manager | 4–8 hours/category/update |
| 2 | Category Manager reviews and approves planogram; VP Merchandising approves for major category resets (occurring 2–4 times/year aligned with W1 quarterly cycles) | Category Manager | VP Merchandising | 1 hour/review |
| 3 | System distributes planogram to stores: Merchandise Planner uploads approved planogram to system; Store Managers and Department Supervisors access planogram view on tablet/terminal; planogram includes visual shelf map, SKU images, facing counts, and before/after photos for resets | System / Merchandise Planner | Store Ops Director | Automated distribution |
| 4 | **Planogram reset execution** (for major category resets): Department Supervisors execute planogram reset during non-business hours (evening or before opening) — Stock Associates remove products from shelves per old layout, reposition shelves if needed, place products per new planogram using tablet visual guide; Stock Associate scan-confirms each SKU placement against planogram using handheld; system records compliance per SKU position | Dept. Supervisor / Stock Associate | Store Manager | 2–4 hours/department/reset |

### Monthly Planogram Compliance Audit

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 5 | System generates monthly planogram audit sample per store: 2–3 departments per month (rotating so all departments are audited over 2–3 months); 20–30 SKU positions per department randomly selected for verification | System | — | Automated (nightly) |
| 6 | Department Supervisor or designated Stock Associate conducts planogram audit: walks assigned department with handheld showing current planogram; for each sampled SKU position: (a) scans shelf location barcode (if location-level barcoding available) or selects position on planogram map, (b) scans item barcode at that position, (c) system compares scanned item to planogram-expected item and facing count, (d) enters result: Correct / Wrong Item / Wrong Position / Out of Stock / Facing Count Mismatch | Dept. Supervisor / Stock Associate | Store Manager | 20–30 min/department |
| 7 | System calculates planogram compliance score per department: (correct positions ÷ total positions audited) × 100; stores must achieve ≥ 90% planogram compliance score | System | — | Automated |
| 8 | Department Supervisor investigates non-compliant positions: (a) wrong item in position — Stock Associate placed wrong SKU during replenishment or reset, (b) out of stock — SKU allocated to position but no inventory available (feeds into W4 replenishment), (c) facing count mismatch — insufficient facings maintained due to low stock or over-crowding from adjacent SKUs, (d) wrong position — SKU present but in incorrect location (often from customer browsing returns) | Dept. Supervisor | Store Manager | 15 min/department |
| 9 | Department Supervisor corrects non-compliant positions immediately during audit (where stock is available): repositions SKUs to match planogram, adjusts facing counts | Stock Associate | Dept. Supervisor | 15–30 min/department |
| 10 | Department Supervisor documents non-compliance exceptions that cannot be resolved immediately (out of stock, fixture issue) with photos and reason code in system; exception flagged for Store Manager review | Dept. Supervisor | Store Manager | 5 min/department |
| 11 | Store Manager reviews planogram compliance dashboard weekly: compliance score per department, trend vs. prior month, top non-compliance reasons; departments below 90% require corrective action plan from Department Supervisor | Store Manager | Regional Manager | 15 min/week |
| 12 | Monthly: Regional Manager reviews planogram compliance scores across all 50 assigned stores; identifies stores consistently below 90% for targeted coaching; compliance score included in W67 Store Performance Scorecard | Regional Manager | Store Ops Director | 1 hour/month |
| 13 | Quarterly: Merchandise Planner reviews planogram compliance data chain-wide — identifies categories with systematically low compliance across stores (indicating planogram design issues rather than execution issues); feeds into W1 category review for planogram redesign | Merchandise Planner | VP Merchandising | 2 hours/quarter |

### Planogram Compliance for New Store Openings

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 14 | During new store opening (W16 step 10 — receiving and stocking): Department Supervisors execute initial planogram using planogram view on tablet; Stock Associates place every SKU per planogram with scan confirmation; Merchandise Planner or Store Ops representative verifies initial placement before store opens | Dept. Supervisor / Stock Associate | Store Manager | Per W16 (1–2 days) |
| 15 | At new store 30-day post-opening review (W16 T+30): Merchandise Planner reviews initial planogram compliance report for new store; identifies positioning issues caused by local fixture variations or stock availability; adjusts planogram if needed | Merchandise Planner | Category Manager | 2 hours/store |

### System Touchpoints
- Planogram design tool integrated with item master and category management (W86.1)
- Planogram visual layout display on store tablet/terminal with SKU images and facing counts (W86.3)
- Scan-verified planogram reset execution with handheld barcode confirmation (W86.4)
- Monthly planogram audit sampling and compliance scoring per department (W86.5–7)
- Non-compliance exception documentation with photos and reason codes (W86.10)
- Planogram compliance dashboard: score per department, per store, chain-wide trend (W86.11–12)
- Chain-wide planogram analytics: category-level compliance, design vs. execution issue identification (W86.13)
- Integration with W1 (assortment review — planogram redesign trigger), W4 (replenishment — out-of-stock positions), W16 (new store — initial planogram execution), W63 (shelf labels — label matches planogram position), W67 (store performance — compliance KPI), W68 (product discontinuation — remove from planogram), W83 (campaign — promotional display planograms)

### Staffing Implication
- **Department Supervisors**: ~30 min/month for audit + 15 min/month for corrections per department = ~45 min/department/month. With 4–6 departments audited per month, this is ~2–3 hours/month. Absorbed into existing duties.
- **Stock Associates**: audit walk + corrections add ~45 min/department/month. Absorbed within existing 3–4 Stock Associates per store.
- **Merchandise Planner**: adds ~4–8 hours per planogram update + 2 hours/quarter for chain-wide review. Absorbed within existing Merchandising team (~40).
- **No incremental headcount.**

---



## W96. Store Renovation & Remodel Project

| Field | Detail |
|---|---|
| **Trigger** | Store lease renewal with renovation requirement; store performance decline requiring refresh; category reset requiring fixture changes; or store format upgrade (e.g., adding appliance showroom, expanding lumber yard) |
| **Frequency** | ~10–15 renovations/year across 200 stores (~5–7% of fleet per year; industry benchmark: major renovation every 7–10 years per store) |
| **Volume** | 1 store per renovation project; duration 2–8 weeks depending on scope |
| **Owner** | Store Ops Director |
| **Participants** | Store Ops Director, Store Manager, VP Merchandising, Category Manager, Controller, Facilities Manager, IT Manager, Visual Merchandiser, contractors |

### Background

Store renovation and remodel projects sit between W16 (New Store Opening) and W47 (Facility Maintenance & Work Orders). W16 covers establishing a brand-new store from scratch. W47 handles routine maintenance (plumbing, electrical, HVAC repairs). Store renovation is a distinct mid-life-cycle event: a mature store undergoes significant layout changes, fixture replacement, category expansion/contraction, or lease-required improvements. Renovations involve capex approval, continued store operations during construction (or planned temporary closure), merchandising layout redesign, and post-renovation sales ramp monitoring. With ~10–15 renovations/year across 200 stores, this is a regular operational process requiring dedicated workflow.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Renovation need identification**: (a) **Lease-triggered**: Property Management Inc. (W14 lessor) communicates lease renewal requires tenant improvements (common in Philippine retail leases); (b) **Performance-triggered**: W67 monthly store performance review identifies store with declining sales trend > 2 consecutive quarters; Store Ops Director recommends renovation as part of turnaround plan; (c) **Merchandising-triggered**: VP Merchandising identifies category requiring expanded space (e.g., appliance section growth) or new fixture type (e.g., paint mixing station upgrade); (d) **Facility-triggered**: W47 facility assessment identifies major infrastructure needs (floor replacement, roof repair, electrical upgrade) that warrant comprehensive renovation vs. piecemeal maintenance | Store Ops Director / VP Merchandising / Facilities Manager | COO | 2 hours |
| 2 | **Scope definition**: Store Ops Director, Store Manager, VP Merchandising, and Facilities Manager jointly define renovation scope: (a) **Light refresh**: repaint, new signage, updated lighting, repositioned checkout area (2–3 weeks, PHP 2–5M); (b) **Partial remodel**: department relocation, new fixtures, expanded category space, updated floor covering (4–6 weeks, PHP 5–15M); (c) **Full renovation**: complete layout redesign, all new fixtures, expanded selling area, new receiving area, major infrastructure (6–8 weeks, PHP 15–40M); (d) identify phasing options: full-store (temporary closure 2–8 weeks) vs. phased (store remains open, renovate department by department) | Store Ops Director / VP Merchandising | COO | 4–8 hours |
| 3 | **Capex request and approval**: Store Ops Director submits capex request per W21: renovation scope, contractor bids (minimum 3 quotations), expected sales uplift, payback period, and timeline; approval follows W21 tiered approval matrix; budget charged to Store Renovation capex category in W26 | Store Ops Director | COO / CFO / CEO (per W21 tiers) | Per W21 |
| 4 | **Design and planogram update**: (a) Visual Merchandiser creates revised store layout based on approved scope; (b) Merchandise Planner updates planogram per W86 for new layout; (c) IT Manager plans POS terminal relocation, network cabling, WiFi coverage adjustments; (d) Facilities Manager creates construction schedule with contractor | Visual Merchandiser / Merchandise Planner / IT Manager | Store Ops Director | 8–16 hours |
| 5 | **Pre-renovation inventory management**: (a) If full-store closure: Supply Planner reduces replenishment orders 4–6 weeks before renovation start to draw down inventory; excess stock transferred to nearby stores per W22 or returned to DC per W22b; (b) If phased renovation: Merchandise Planner identifies affected departments; Stock Associates relocate merchandise to temporary display areas or backroom; system updates planogram temporarily to reflect reduced shelf space | Supply Planner / Merchandise Planner | VP Merchandising | 4–8 hours |
| 6 | **Construction execution**: (a) Contractor mobilizes per agreed schedule; (b) Facilities Manager supervises construction on behalf of BuildRight; (c) weekly construction progress meetings: Facilities Manager, Store Manager (if open), contractor; (d) construction quality checkpoints: Facilities Manager inspects at foundation, framing, electrical rough-in, and finishing stages; (e) if store is open during phased renovation: Store Manager ensures customer safety (barriers, signage, dust control, noise management) | Facilities Manager / Contractor | Store Ops Director | Ongoing (2–8 weeks) |
| 7 | **IT and systems setup** (during final construction phase): (a) IT team installs/relocates POS terminals, network equipment, CCTV (W71), WiFi access points, handheld charging stations; (b) IT verifies POS connectivity and offline capability (W5g); (c) system updates location master if selling area changes | IT Manager | CIO | 2–4 days |
| 8 | **Restocking and planogram execution**: (a) Stock Associates stock shelves per updated planogram (W86.4 — scan-verified placement); (b) DC resumes replenishment to store (W4); (c) Merchandise Planner verifies initial stock levels per planogram; (d) new shelf labels generated per W63 | Stock Associates / Merchandise Planner | Store Manager | 1–3 days |
| 9 | **Reopening / reveal**: (a) If store was closed: "Grand Reopening" event coordinated with W83 marketing campaign; (b) Store Manager conducts full store walkthrough with Dept. Supervisors; (c) verify all planogram positions correct, all POS terminals operational, all safety features in place (fire exits, emergency lighting, CCTV); (d) store opens to customers | Store Manager | Store Ops Director | 1 day |
| 10 | **Post-renovation monitoring** (first 90 days): (a) Weekly sales tracking vs. pre-renovation baseline and vs. projected uplift from capex request (W21); (b) W67 monthly store performance review includes renovation ROI tracking; (c) Merchandise Planner monitors category sales in expanded/renovated sections vs. expectations; (d) if sales uplift < 50% of projection by day 90: Store Ops Director and VP Merchandising conduct diagnostic review; (e) at day 90: Facilities Manager conducts post-renovation punch list walk — any construction defects reported to contractor for rectification under warranty | Store Ops Director / Store Manager | COO | 2 hours/week for 90 days |
| 11 | **Financial close-out**: Controller reviews renovation capex vs. budget; posts capex to fixed assets per W21; contractor retention (typically 10% held for 6 months) recorded as AP retention; final capex report submitted to CFO | Controller | CFO | 2 hours/project |

### System Touchpoints
- Renovation project tracking with scope, timeline, budget, and milestone tracking (W96.2–3)
- Inventory draw-down planning: reduced replenishment and excess transfer to nearby stores (W96.5)
- Planogram update for revised store layout (W96.4, W96.8)
- POS and IT infrastructure relocation tracking (W96.7)
- Post-renovation sales monitoring vs. projected uplift (W96.10)
- Capex vs. budget tracking and fixed asset capitalization (W96.11)
- Integration with W4 (replenishment — resume/adjust for renovation), W16 (new store — shares setup procedures for IT, planogram, restocking), W21 (capex — renovation funding), W22 (transfers — excess inventory redistribution), W22b (store-to-DC returns — inventory draw-down), W47 (facility maintenance — renovation scope may originate from maintenance assessment), W63 (shelf labels — updated for new layout), W67 (store performance — renovation ROI tracking), W83 (marketing — re-opening campaign), W86 (planogram — updated layout), W97 (sample/demo — reinstall or replace display samples)

### Staffing Implication
- **Store Ops Director**: oversees ~10–15 renovation projects/year; each project requires ~8–16 hours of planning + ~2 hours/week during construction + ~8 hours post-renovation. With staggered projects, peak load is 2–3 concurrent renovations = ~10–15 hours/week during peak. May delegate day-to-day supervision to Facilities Manager for smaller projects.
- **Facilities Manager**: serves as on-site construction supervisor; adds ~10 hours/week per active renovation. With 1–2 concurrent renovations, this is manageable.
- **Visual Merchandiser**: design and layout work adds ~8–16 hours per renovation. Absorbed within existing Marketing team.
- **IT Manager**: adds ~2–4 days per renovation for IT relocation. Absorbed with support from IT team.
- **No incremental headcount.**

---

## W109. Store-Level Inventory Receiving & Putaway

| Field | Detail |
|---|---|
| **Trigger** | DC delivery truck arrives at store; or DSD vendor delivery; or inter-store transfer arrives; or customer return processed for restocking |
| **Frequency** | 2–3 DC deliveries per store per week; ~5–10 DSD deliveries per store per month; occasional transfers and returns |
| **Volume** | ~6–10 receiving events per store per week; avg 20–50 lines per DC delivery; 5–15 lines per DSD |
| **Owner** | Receiving Clerk (store) |
| **Participants** | Receiving Clerk, Stock Associate, Department Supervisor, Store Manager, DC Driver |

### Background

W3 covers DC receiving in detail — barcode-directed putaway, quality inspection, cross-dock flows, and yard management. However, store-level receiving is fundamentally different: (a) no WMS-directed putaway — stores use handheld RF devices or mobile tablets, not full WMS; (b) putaway means moving stock to the sales floor (shelf replenishment) or backroom (overflow), not to bin locations; (c) stores receive from multiple sources (DC delivery, DSD vendor, inter-store transfer, customer return restocking); (d) receiving happens during store operating hours with customers present, unlike DC receiving which is a warehouse-only activity. This workflow fills the gap between DC outbound dispatch (W106) and store shelf availability.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pre-arrival preparation**: System alerts Receiving Clerk of scheduled inbound deliveries for the day (from DC delivery schedule per W106, DSD schedule per W18b, or transfer ETA per W22); Clerk reviews expected receiving volume and coordinates with Stock Associates for putaway support | Receiving Clerk | Store Manager | 10 min/morning |
| 2 | **Truck arrival and dock check**: Driver arrives at store receiving area; Receiving Clerk checks delivery manifest against system-scheduled deliveries; if unscheduled delivery (no matching PO/TO): Clerk checks with Store Manager before accepting | Receiving Clerk / Driver | Store Manager | 5 min |
| 3 | **Unloading**: Receiving Clerk and Stock Associates unload truck; stage goods in receiving area sorted by department (lumber, plumbing, tiles, tools, hardware, paint, appliances); catch-weight items (lumber, wire) measured and verified at unload | Receiving Clerk / Stock Associate | Department Supervisor | 20–45 min/delivery |
| 4 | **Scan receiving against Transfer Order / PO**: Receiving Clerk scans each case/tote/item barcode using handheld RF device against the Transfer Order (DC delivery) or PO (DSD); system displays expected SKU and quantity per line; Clerk confirms or enters actual quantity received | Receiving Clerk | Department Supervisor | 15–30 min/delivery |
| 5 | **Discrepancy handling**: (a) **Shortage** (received less than expected): Clerk enters actual quantity; system posts partial receipt; shortage logged; if > 5% variance: Clerk notifies Store Manager and DC Dispatch per W22.9a; (b) **Overage** (received more than expected): Clerk flags in system; Store Manager decides to accept (updates TO/PO quantity) or reject excess; (c) **Wrong item** (SKU doesn't match TO/PO): Clerk rejects item; Driver takes back or DC Dispatch notified; (d) **Damage**: Clerk documents damage with photos per W91 damage report process; routes to disposition (W93 markdown, W88 RTV, or scrap) | Receiving Clerk | Store Manager | 5 min/discrepancy |
| 6 | **Quality spot-check**: For DSD items (fresh delivery from vendor, no DC quality inspection): Department Supervisor spot-checks 3–5 items per delivery for damage, correct labeling, and shelf-life; DC-delivered items already inspected at W3 AQL checkpoint — no additional store inspection unless visibly damaged | Department Supervisor | Store Manager | 5 min/delivery |
| 7 | **Confirm receipt in system**: Receiving Clerk confirms Goods Receipt in handheld; system posts: (a) store inventory increases (perpetual), (b) in-transit inventory clears (for DC deliveries), (c) inventory ownership at store confirmed (Depot Inc.), (d) receiving timestamp and Clerk ID logged | Receiving Clerk / System | Department Supervisor | 2 min |
| 8 | **Putaway to sales floor (primary)**: Stock Associate moves received goods from receiving staging area to sales floor: (a) system provides shelf location guidance on handheld (aisle/bay) based on planogram (W86); (b) Stock Associate places items on shelf in designated location; scan-confirms shelf placement; (c) for promotional items (W57): Stock Associate places in designated promo display area, not regular shelf; (d) for catch-weight items: Stock Associate places in yard or designated cut-to-length area per store layout; (e) putaway priority: promotional items first, then A-items (fast movers), then B/C-items | Stock Associate | Department Supervisor | 30–60 min/delivery |
| 9 | **Putaway to backroom (overflow)**: If sales floor shelf is full (no space for all received quantity): (a) Stock Associate places excess in backroom stock area; (b) system records backroom location (zone-level, not bin-level — stores do not have bin-level location tracking); (c) backroom inventory tracked separately from floor inventory in system; (d) Stock Associates replenish from backroom to floor during daily shelf restocking (W5a step 7) | Stock Associate | Department Supervisor | 10 min/delivery |
| 10 | **Packaging and waste disposal**: Stock Associate breaks down empty cartons, pallets, and packaging materials; cardboard recycled or compacted; packaging waste disposed per store waste management protocol; wooden pallets stacked for DC truck backhaul on next delivery | Stock Associate | Department Supervisor | 10 min/delivery |
| 11 | **Receiving completion**: Receiving Clerk closes receiving session in handheld; system generates receiving confirmation with: TO/PO number, total lines received, discrepancies noted, receiving completion timestamp; Driver signs delivery receipt (proof of delivery for DC) and departs | Receiving Clerk / Driver | Store Manager | 5 min |

**Total time per DC delivery**: ~1.5–2.5 hours (unloading + scanning + putaway)
**Total time per DSD delivery**: ~30–60 minutes

### Receiving by Source

| Source | Receiving Document | Scan Against | Discrepancy Route | Putaway Priority |
|---|---|---|---|---|
| **DC delivery** (W4, W106) | Transfer Order | TO lines | W22.9a (transfer discrepancy) | Promo → A-items → B/C-items |
| **DSD vendor** (W18) | Purchase Order | PO lines | W18 discrepancy process | Direct to shelf/yard |
| **Inter-store transfer** (W22) | Transfer Order | TO lines | W22.9a | Per dept priority |
| **Customer return restock** (W12) | Return transaction | Return line items | N/A — already processed | Direct to shelf |
| **RTV backhaul from vendor** (W88) | RTV shipment | RTV record | W88 vendor dispute | To RTV holding area |

### System Touchpoints
- Daily inbound delivery schedule from W106 DC dispatch, W18b DSD schedule, and W22 transfers (W109.1)
- Handheld RF barcode scanning against Transfer Order or Purchase Order with line-level quantity confirmation (W109.4)
- Partial receipt posting with discrepancy logging and auto-notification (W109.5)
- Shelf location guidance from planogram integration (W86) on handheld (W109.8)
- Dual inventory tracking: sales floor vs. backroom at zone level (W109.9)
- Receiving confirmation with proof of delivery for DC truck (W109.11)
- Catch-weight item measurement capture at receiving (W109.3)
- Integration with W4 (replenishment — the orders being received), W18 (DSD — vendor delivery receiving), W22 (transfers — inter-store receiving), W42 (physical inventory — receiving affects count accuracy), W47 (facility — receiving dock maintenance), W86 (planogram — shelf placement guidance), W91 (damage handling), W106 (DC dispatch — proof of delivery loop), W63 (shelf labels — new items may need labels)

### Staffing Implication
- **2 Receiving Clerks per store**: already in staffing model (35/store). Each handles ~3–5 deliveries/week × 2 hours = ~6–10 hours/week. Remainder of time on backroom management, BOPIS staging, and other duties.
- **3 Stock Associates per store**: putaway adds ~1–1.5 hours per delivery event × ~6–10 events/week = ~6–15 hours/week. Balanced with daily shelf replenishment (W5a.7), cycle counting (W6), and damage handling (W91).
- **No incremental headcount.**

---

## W111. Store Energy & Utility Consumption Management

| Field | Detail |
|---|---|
| **Trigger** | Monthly utility bill received; quarterly energy review calendar; or ad-hoc triggered by abnormal consumption alert |
| **Frequency** | Monthly bill processing; quarterly consumption review; annual energy budget |
| **Volume** | 200 stores × 3–4 utility types (electricity, water, internet, waste disposal) = ~600–800 utility bills/month; 5 DCs × 3–4 utility types = ~15–20 DC bills/month |
| **Owner** | Store Manager (store-level); DC Manager (DC-level); Facilities Manager (chain-wide) |
| **Participants** | Store Manager, DC Manager, Facilities Manager, AP Clerk, Finance Manager, VP Operations |

### Background

BuildRight operates 200 stores (8,000–15,000 sqm each) and 5 DCs (25,000–40,000 sqm each) across the Philippines. Utility costs — particularly electricity for lighting, HVAC, and equipment — are a significant operating expense. At an estimated PHP 80–150 per sqm per month for electricity in Philippine big-box retail, annual electricity cost alone is ~PHP 1.5–2.7B (3–4% of revenue). W7c processes utility bills as non-PO invoices, but there is no workflow for monitoring consumption trends, benchmarking across stores/DCs, identifying energy waste, and tracking sustainability KPIs. This workflow creates that operational layer.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Utility bill processing**: AP Clerk receives utility bill (electricity, water, internet, waste disposal) per W7c non-PO invoice process; system captures: utility provider, meter reading (if available), consumption units (kWh, cubic meters), total amount, billing period, and store/DC location code; AP Clerk enters consumption data in utility tracking module alongside financial data | AP Clerk | AP Supervisor | Per W7c + 5 min/bill for consumption entry |
| 2 | **Consumption normalization**: System calculates normalized consumption metrics per location: (a) kWh per sqm per month, (b) kWh per PHP revenue per month, (c) water consumption per sqm per month, (d) total utility cost as % of store revenue; normalizes for billing period length (some bills span 28–35 days) | System | — | Automated |
| 3 | **Automated anomaly detection**: System compares each location's current month consumption to: (a) same month prior year (seasonal comparison), (b) trailing 3-month average (trend comparison), (c) peer group average (stores of similar size and format in same region); flags locations where consumption exceeds comparison by > 20%; generates anomaly alert to Store Manager and Facilities Manager | System | — | Automated |
| 4 | **Store Manager anomaly response**: Upon receiving anomaly alert, Store Manager investigates: (a) check for operational causes — extended HVAC use during heat wave, new equipment added, construction/renovation activity (W96), increased lighting for promotional displays; (b) check for maintenance issues — HVAC running inefficiently, water leak, lighting left on during non-business hours; (c) if maintenance issue identified: Store Manager creates facility maintenance work order per W47; (d) response documented in system with root cause and corrective action | Store Manager | Regional Manager | 30 min/alert |
| 5 | **Monthly utility dashboard**: Facilities Manager reviews monthly utility dashboard: (a) total utility spend by type and trend, (b) top 20 highest-consuming stores/DCs, (c) top 20 stores with highest utility cost as % of revenue, (d) anomaly alerts and resolution status, (e) comparison of actual utility spend to budget (W26); dashboard available to VP Operations, CFO, and Store Managers (own store only) | Facilities Manager | VP Operations | 1 hour/month |
| 6 | **Quarterly energy review**: Facilities Manager conducts quarterly energy review with Store Ops Director and VP Operations: (a) chain-wide utility consumption trend and cost trajectory, (b) store-level benchmarking — best and worst performers by kWh/sqm and utility cost/revenue, (c) seasonal patterns and preparation for peak consumption periods (summer HVAC, holiday lighting), (d) energy efficiency project pipeline — proposed initiatives (LED lighting retrofit, HVAC upgrades, motion-sensor lighting in backroom, solar panel feasibility for select stores) with cost-benefit analysis, (e) review of approved energy efficiency capex projects (per W21) — actual vs. projected savings | Facilities Manager | VP Operations | 2 hours/quarter |
| 7 | **Annual energy budget**: As part of W26 annual budget preparation, Facilities Manager prepares utility budget per location based on: (a) historical consumption by month (3-year trend), (b) planned changes (new store openings W16, renovations W96, equipment replacements), (c) known rate increases from utility providers (Meralco, Davao Light, VECO rate adjustments), (d) projected savings from energy efficiency initiatives; submits per-location utility budget to Finance Manager for consolidation into W26 | Facilities Manager / Finance Manager | VP Operations / CFO | Annual (8 hours) |
| 8 | **DC utility management**: DC Manager monitors DC utility consumption with focus on: (a) refrigeration and cold-chain equipment (if applicable to paint/chemical storage), (b) warehouse lighting and ventilation, (c) charging stations for electric forklifts and handheld devices, (d) yard lighting for outdoor lumber/building materials area; DC utility benchmarking uses DC-specific metrics (kWh per sqm, kWh per TEU processed) | DC Manager | Supply Chain Manager | 30 min/month |

### System Touchpoints
- Utility bill processing with consumption data capture (kWh, cubic meters) alongside financial data per W7c (W111.1)
- Automated consumption normalization: kWh/sqm, kWh/revenue, cost/revenue (W111.2)
- Automated anomaly detection with configurable thresholds (> 20% deviation from seasonal, trend, or peer benchmarks) (W111.3)
- Monthly utility dashboard with multi-dimensional benchmarking (W111.5)
- Quarterly energy review with efficiency project pipeline and capex integration (W111.6)
- Annual utility budget per location integrated with W26 budget module (W111.7)
- Integration with W7c (utility bill processing), W16 (new store — initial utility setup), W21 (energy efficiency capex), W26 (annual budget), W47 (facility maintenance — HVAC/lighting repair), W67 (store performance — utility cost as P&L line), W86 (planogram — lighting for displays), W96 (renovation — utility impact)

### Staffing Implication
- **1 Facilities Manager** (within Store Operations team of ~23 at HQ): manages chain-wide energy management, utility vendor relationships, and energy efficiency projects. This role is already implied by W47 (facility maintenance coordination) but formalized here.
- **Store Managers**: 30 min per anomaly alert (estimated 1–2 alerts/quarter/store). Absorbed.
- **AP Clerks**: 5 min additional per utility bill for consumption data entry = ~60–80 hours/month for 800+ bills. Absorbed within existing AP team.
- **No incremental headcount.**

---

## W170. Senior Citizen & PWD Discount Compliance (PH Legal)

| Field | Detail |
|---|---|
| **Trigger** | Customer presents Senior Citizen (SC) or Person with Disability (PWD) ID at POS |
| **Frequency** | High; ~5–10% of retail transactions in the Philippines |
| **Volume** | ~70,000–140,000 transactions/month chain-wide |
| **Owner** | Lead Cashier |
| **Participants** | Cashier, SC/PWD Customer, Store Manager (for high-value overrides) |

### Background

Philippine law (RA 9994 and RA 10754) mandates a 20% discount and 12% VAT exemption on specific "basic necessities and prime commodities" for SCs and PWDs. For hardware stores, this applies to specific items like light bulbs, batteries, and certain construction materials used for home repair, subject to DTI/DA quantity limits.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Identification**: Customer presents OSCA (Senior) or PWD ID card + Purchase Book | Cashier | — | 1 min |
| 2 | **Validation**: Cashier verifies ID authenticity and matches name to the customer; checks Purchase Book for prior purchases of the same items to ensure within weekly quantity limits (e.g., PHP 1,300/week for basic goods) | Cashier | — | 2 min |
| 3 | **POS Entry**: Cashier selects "SC/PWD Discount" in POS; system prompts for ID number and Name; system automatically filters items eligible for discount/VAT-exempt status per BIR/DTI rules | Cashier | — | 1 min |
| 4 | **Transaction**: System applies 20% discount on eligible items and removes 12% VAT; receipt prints with mandatory SC/PWD disclosure (Name, ID#, Gross Sale, Discount, VAT Exempt Sales) | System | — | Automated |
| 5 | **Logbook Entry**: Cashier manually records transaction in the mandatory BIR/OSCA Logbook (Legal requirement for audit) | Cashier | Lead Cashier | 2 min |
| 6 | **Filing**: Monthly: Finance consolidates SC/PWD sales for BIR Form 2550M (VAT) and 1702 (Income Tax) reporting, claiming the discount as a deductible expense | Finance | Controller | 4 hours |

---

## W171. Store Physical Security & Yard Patrol Routine

| Field | Detail |
|---|---|
| **Trigger** | Hourly patrol requirement; or high-risk alert (storm, local unrest) |
| **Frequency** | Hourly (24/7) |
| **Volume** | Covers all 200 stores and 5 DCs |
| **Owner** | Store Security Lead |
| **Participants** | Security Guard, Store Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Patrol Start**: Guard initiates patrol on handheld device/app; scans NFC tag at the Guard Post | Security Guard | — | 1 min |
| 2 | **Perimeter Check**: Walk exterior walls; check for structural breaches, fence tampering, or unauthorized loitering | Security Guard | — | 10 min |
| 3 | **Lumber Yard/Outdoor Inventory**: Verify seals on outdoor containers; check that bulky stock (cement, steel) is covered/secured; scan NFC tags at yard corners | Security Guard | — | 15 min |
| 4 | **Utility & Fire Check**: Inspect fire pump room, generator set (check fuel/oil levels), and electrical sub-station for any leaks or abnormal noise | Security Guard | — | 10 min |
| 5 | **Backroom/Receiving**: Verify that the receiving dock is locked and no staff are in restricted areas after-hours | Security Guard | — | 5 min |
| 6 | **Digital Log**: Guard submits patrol report via app with photos of any "Alert" items; Store Manager receives instant notification for "Critical" issues | Security Guard | Store Mgr | 2 min |

---

## W173. Store-Level Solar Energy Monitoring

| Field | Detail |
|---|---|
| **Trigger** | Daily performance tracking; or "Inverter Failure" alert from IoT system |
| **Frequency** | Daily monitoring; Quarterly cleaning |
| **Volume** | Applicable to ~80 stores with rooftop solar installations |
| **Owner** | Facilities Coordinator |
| **Participants** | Store Maintenance, Solar Vendor (External) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Generation Tracking**: System pulls data from Solar Inverters; compares "Actual Generation" vs. "Expected" (based on weather/irradiance) | System | Facilities Coord | Automated |
| 2 | **Anomaly Detection**: If generation drops > 15% below expected: system creates a W47 maintenance ticket; Facilities Coordinator reviews CCTV/Drone footage for panel obstructions (dust, debris) | System | Facilities Coord | 15 min |
| 3 | **Cleaning Routine**: Quarterly: Store Maintenance or Vendor performs panel cleaning to remove soot/dust (critical in high-traffic/industrial areas) | Maintenance | Store Mgr | 4 hours |
| 4 | **Savings Verification**: Monthly: Finance compares Solar Generation (Self-Consumption) against Meralco/Utility bill reduction to verify ROI | Finance | Controller | 1 hour |

---

## W176. Store-to-DC Reverse Logistics (Consolidation)

| Field | Detail |
|---|---|
| **Trigger** | Accumulation of customer returns, overstock, or defective items at store level requiring vendor return |
| **Frequency** | Bi-weekly per store |
| **Volume** | ~2–5 pallets per shipment |
| **Owner** | Store Receiving Clerk |
| **Participants** | Store Receiving Clerk, DC Receiving Clerk, Logistics (Fleet) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Consolidation**: Store Receiving Clerk identifies items in "RTV Staging Area" (from W12 returns or W91 damage); groups by Vendor and Reason (Defective, Overstock) | Store Clerk | Asst Store Mgr | 1 hour |
| 2 | **Transfer Creation**: Clerk creates a "Reverse Stock Transfer Order (RSTO)" in ERP from Store to Hub DC; system ensures items are non-saleable in store inventory | Store Clerk | — | 15 min |
| 3 | **Palletization**: Items are boxed and palletized; "Return Shipment" labels generated from ERP | Store Clerk | — | 30 min |
| 4 | **Backhaul Pickup**: Logistics truck (after making a store delivery, W4) picks up the return pallets (Backhaul) | Driver | — | 15 min |
| 5 | **DC Receipt**: DC Receiving Clerk receives pallets; scan-verifies against RSTO; moves to DC RTV Zone for consolidated shipment to Vendor (W88) | DC Clerk | DC Supervisor | 30 min |

### System Touchpoints
- Reverse Stock Transfer Order (RSTO) creation
- Backhaul load planning (Logistics integration)
- Consolidated RTV tracking (Store -> DC -> Vendor)

---

## W177. Vending & Concessionaire Management

| Field | Detail |
|---|---|
| **Trigger** | New concessionaire application; monthly rent/commission calculation |
| **Owner** | Store Manager |
| **Participants** | Concessionaire, Finance (AR), Store Operations |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Onboarding**: Store Manager reviews application for in-store cafe, snack bar, or ATM space; validates compliance with safety/health standards | Store Mgr | — | 2 hours |
| 2 | **Contract Setup**: Legal/Finance setup lease in ERP (W117); defines Rent or % Commission on Sales | Finance | — | 1 hour |
| 3 | **Sales Tracking**: If commission-based: Concessionaire sales are rung through a dedicated "Non-Inventory" SKU at POS; system tracks total monthly throughput | Cashier | — | Continuous |
| 4 | **Billing**: Monthly: Finance generates invoice for Rent + Utilities + Commission; offsets any payments collected on behalf of concessionaire | AR Clerk | Controller | 30 min |

### System Touchpoints
- Lease management integration (W117)
- Non-inventory POS SKU for concessionaire sales tracking
- Automated monthly billing

---

## W182. Gift / Home Registry Lifecycle

| Field | Detail |
|---|---|
| **Trigger** | Customer (Home Builder/Renovator) creates a "Project Wishlist" or "Registry" |
| **Frequency** | ~50–100 new registries per month |
| **Owner** | Customer Service Rep (CSR) |
| **Participants** | Customer, Sales Associate, Gift Givers |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Creation**: Customer creates Registry via Website or In-store Tablet; specifies "Housewarming" or "Renovation Project" | Customer | — | 15 min |
| 2 | **Item Selection**: Customer walks store with Sales Associate; scans items into Registry using Mobile App | Customer / Assoc | — | 1 hour |
| 3 | **Sharing**: Customer shares Registry link with family/friends; or provides "Registry ID" for in-store lookup | Customer | — | — |
| 4 | **Purchase**: Giver buys item from Registry (In-store or Online); system marks item as "Purchased" to prevent duplicates | Cashier / System | — | 2 min |
| 5 | **Fulfillment**: Items can be picked up by Giver, or held at CSR counter for "Consolidated Delivery" to the Registry Owner | CSR | Store Mgr | 10 min |
| 6 | **Completion**: Registry Owner receives "Completion Discount" (e.g., 10% off remaining items) after the event date | System | — | Automated |

### System Touchpoints
- Registry master data (Customer + Items + Event Date)
- Real-time "Purchased" status sync across channels
- Completion discount logic (Promo engine integration)

---

## W205. Employee Purchase Program & Internal Staff Sales

| Field | Detail |
|---|---|
| **Trigger** | Employee wishes to purchase merchandise for personal use |
| **Frequency** | Daily; ~1,000 transactions/month across group |
| **Volume** | Covers all 8,060+ employees |
| **Owner** | Store Manager / HR Manager |
| **Participants** | Employee (Buyer), Cashier, HR (for eligibility) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Eligibility Check**: Employee presents ID at POS; System verifies active employment status and "Monthly Purchase Limit" (e.g., PHP 20,000/month) | Cashier / System | HR Manager | 1 min |
| 2 | **Discount Application**: System applies "Staff Discount" (e.g., Cost + 5% or 15% off SRP) based on product category rules | System | — | Real-time |
| 3 | **Payment**: Employee pays via Cash, Card, or "Payroll Deduction" (W10/W76) | Employee | Cashier | 2 min |
| 4 | **Verification**: Manager signs receipt; confirms items are for personal use (not resale) | Store Manager | — | 1 min |
| 5 | **Audit**: LP Team reviews high-frequency staff purchases for potential abuse (W37) | LP Analyst | VP Compliance | Monthly |

---

## W212. Automated Store Cash Management & Smart Safe Integration

| Field | Detail |
|---|---|
| **Trigger** | Shift end; or cash drawer limit reached |
| **Frequency** | 2–3 times per day per cashier |
| **Volume** | Covers all 200 stores; ~1,000 POS terminals |
| **Owner** | Store Cashier Supervisor |
| **Participants** | Cashier, Supervisor, CIT (Cash-in-Transit) Partner |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Drawer Limit Alert**: System triggers alert when POS cash drawer exceeds threshold (e.g., PHP 50,000) | System | Cashier | Real-time |
| 2 | **Cash Skimming**: Cashier counts excess cash; Supervisor verifies; records "Skim" in POS | Cashier | Supervisor | 5 min |
| 3 | **Smart Safe Deposit**: Cashier inserts bills into the in-store Smart Safe; safe validates bills and counts in real-time | Cashier | — | 3 min |
| 4 | **Credit Recognition**: Smart Safe API sends deposit confirmation to ERP/Bank; Bank provides "Same-Day Credit" to BuildRight's account | System | Finance | Automated |
| 5 | **EOD Reconciliation**: At EOD, system reconciles POS Sales vs. Smart Safe Deposits vs. Remaining Drawer Cash; flags variances | System | Supervisor | Automated |
| 6 | **CIT Pickup**: CIT partner (e.g., G4S/Securicor) empties safe when full; system logs pickup; safe resets for next cycle | CIT Partner | — | 20 min |

### System Touchpoints
- Smart Safe API integration with ERP and Bank (W30)
- POS cash limit alerts and skimming workflow
- Automated daily bank reconciliation for cash deposits
- CIT pickup tracking and safe capacity monitoring

---

## W206. Mobile POS (mPOS) & Queue-Busting Operations

| Field | Detail |
|---|---|
| **Trigger** | High foot traffic / long queues at main checkout; or customer needing checkout in Yard/Materials area |
| **Frequency** | Peak hours (weekends, holidays); and for bulky outdoor sales |
| **Volume** | ~5–10% of total store transactions |
| **Owner** | Store Manager |
| **Participants** | Sales Associate (mPOS Operator), Cashier (for cash handling if needed), Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Deployment**: Store Manager monitors queues; dispatches Sales Associates with tablets/mPOS devices to the floor | Store Manager | — | 2 min |
| 2 | **Scanning**: Associate scans items in customer's cart or in the Yard area; system applies real-time pricing and promos | Associate | — | 3–5 min |
| 3 | **Customer Lookup**: Associate scans Loyalty Card or looks up customer via phone/email (W17) | Associate | — | 1 min |
| 4 | **Tendering**: (a) If Card/E-wallet: Associate processes payment on the mPOS device; (b) If Cash: Associate generates "Pre-order Barcode" and directs customer to "Express Cash" lane | Associate | — | 2 min |
| 5 | **Receipt**: System generates Digital Receipt (Email/SMS) or prints via Bluetooth belt printer | System | — | 30 sec |
| 6 | **Fulfillment**: If items are in Yard: Associate marks items as "Released" in system; guard verifies digital receipt at gate | Associate | — | 2 min |
| 7 | **Sync**: Transactions sync instantly with central ERP inventory and Finance; no manual EOD re-entry required | System | — | Automated |

### System Touchpoints
- mPOS tablet application with full SKU/Price/Loyalty integration
- Bluetooth printer / Digital receipt integration
- Yard-gate verification dashboard
- Real-time inventory deduction (same as fixed POS)



