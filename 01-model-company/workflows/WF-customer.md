# Customer Experience Workflows

> Complaint resolution, corporate/project accounts, price matching, and satisfaction measurement.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W41. Customer Complaint Resolution](#customer-complaint-resolution)
- [W58. Corporate / Project Account Management](#corporate-project-account-management)
- [W61. Competitor Price Match Process](#competitor-price-match-process)
- [W65. Customer Satisfaction Measurement](#customer-satisfaction-measurement)

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



---

