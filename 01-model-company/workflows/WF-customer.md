# Customer Experience Workflows

> Complaint resolution, corporate/project accounts, price matching, satisfaction measurement, account reactivation, and feedback-to-action loop.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W41. Customer Complaint Resolution](#customer-complaint-resolution)
- [W58. Corporate / Project Account Management](#corporate-project-account-management)
- [W61. Competitor Price Match Process](#competitor-price-match-process)
- [W65. Customer Satisfaction Measurement](#customer-satisfaction-measurement)
- [W84. Customer Account Reactivation](#customer-account-reactivation)
- [W87. Customer Feedback-to-Action Loop](#customer-feedback-to-action-loop)
- [W103. Trade Sales Pipeline & Territory Management](#trade-sales-pipeline-territory-management)
- [W112. Trade Counter / Pro Desk Operations](#trade-counter--pro-desk-operations)
- [W156. Customer Data Platform (CDP) & Hyper-Personalization](#customer-data-platform-cdp--hyper-personalization)
- **[Project-Based B2B & Trade Sales Workflows (W162–W166)](./WF-project-sales.md)**

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

## W84. Customer Account Reactivation

| Field | Detail |
|---|---|
| **Trigger** | Former customer (dormant, closed, or written-off) requests to resume business; or Sales Rep identifies reactivation opportunity during prospecting |
| **Frequency** | ~20–40 reactivation requests/month; peaks during construction season (October–March) |
| **Volume** | ~5,200 active accounts; ~300–500 dormant/inactive accounts at any time; ~10–20 written-off accounts per year potentially recoverable |
| **Owner** | AR Supervisor |
| **Participants** | Sales Rep, AR Clerk, AR Supervisor, Finance Manager, Credit Committee (if large account) |

### Background

Customer accounts may become dormant (no transactions for 6+ months, per W8), closed (per W8 step 12), or written off (per W81). When these customers wish to resume business — often driven by new construction projects, change of ownership, or settlement of prior obligations — a formal reactivation process ensures appropriate risk assessment while avoiding unnecessary friction. This workflow covers all reactivation scenarios.

### Reactivation Scenarios

| Scenario | Prior Status | Risk Level | Reactivation Path |
|---|---|---|---|
| **Dormant reactivation** | Inactive (credit limit reduced to PHP 0) | Low | Abbreviated credit review |
| **Voluntarily closed → reopen** | Closed by customer request | Low–Medium | Standard W24 credit application |
| **Written-off → repayment & reactivate** | Written off per W81 | High | Enhanced credit review + approval |
| **Written-off → new entity** | New company formed by same principal | High | Full W24 + legal review |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer or Sales Rep initiates reactivation request: provides customer name or prior account number, reason for reactivation, and current business status | Customer / Sales Rep | AR Clerk | 10 min |
| 2 | AR Clerk retrieves prior account record from system; reviews account history: (a) prior credit limit and payment history, (b) reason for dormancy/closure/write-off, (c) outstanding balance (if any), (d) any pending disputes or unresolved issues | AR Clerk | AR Supervisor | 15 min |
| 3 | **Dormant reactivation** (no write-off, reactivation within 12 months): (a) AR Clerk contacts customer to confirm business is active and update contact details, (b) if prior credit assessment is < 12 months old, AR Clerk reactivates account with prior credit limit (AR Supervisor approval required), (c) if prior credit assessment is > 12 months old, process abbreviated W24 credit review — updated financial statements + trade references, (d) system changes account status from "Inactive" to "Active"; restores credit limit per approval | AR Clerk / AR Supervisor | AR Supervisor | 30 min–1 hour |
| 4 | **Voluntarily closed → reopen** (customer previously closed account per W8.12 with zero balance): (a) AR Clerk processes standard W24 credit application with updated business documents, (b) if closed within 12 months and prior payment history was good (no > 60-day overdue), AR Supervisor may approve with prior credit limit, (c) if closed > 12 months ago or prior payment issues, full W24 credit assessment required | AR Clerk / AR Supervisor | Finance Manager | Per W24 |
| 5 | **Written-off account reactivation** (customer previously written off per W81 and now wishes to resume): (a) AR Clerk confirms prior written-off balance has been fully settled (payment, settlement agreement per W81.11, or court-approved compromise) — no reactivation while prior balance is outstanding, (b) customer must provide: updated business registration, current financial statements, and explanation of circumstances leading to prior write-off (e.g., ownership change, resolved dispute, business recovery), (c) AR Clerk processes enhanced credit review: full W24 credit assessment + additional trade reference checks + external credit bureau inquiry (if available), (d) mandatory Finance Manager review regardless of amount, (e) Credit Committee approval (CFO + Finance Manager + AR Supervisor) required for reactivated credit limit > PHP 200,000, (f) initial credit limit set conservatively (typically 50% of prior limit) with 6-month probationary period — system flags all transactions on reactivated accounts for first 6 months | AR Clerk / Finance Manager / Credit Committee | CFO | 2–4 hours |
| 5a | **New entity with same principal** (customer formed new company after prior entity was written off): (a) AR Clerk and Legal review relationship between new entity and prior written-off entity — shared directors, officers, or beneficial owners per SEC records, (b) if affiliation confirmed: prior written-off balance must be settled or covered by a payment plan before new account is considered, (c) full W24 credit assessment required for new entity with no credit history reuse, (d) Credit Committee approval mandatory regardless of requested credit limit, (e) system links new entity record to prior entity for ongoing risk monitoring | AR Clerk / Legal / Credit Committee | CFO | 4–8 hours |
| 6 | System reactivates account: (a) status changed from "Inactive"/"Closed"/"Written Off" to "Active — Reactivated", (b) credit limit set per approved amount, (c) payment terms assigned per approval, (d) reactivation date and approver logged in audit trail, (e) if probationary period applies, system schedules automatic review at 6-month mark | System / AR Clerk | AR Supervisor | 10 min |
| 7 | AR Clerk notifies customer and assigned Sales Rep of reactivation: approved credit limit, payment terms, and any probationary conditions | AR Clerk | — | 10 min |
| 8 | **6-month probationary review** (for written-off reactivations): AR Supervisor reviews reactivated account payment history at 6 months — (a) if all payments on time and no credit limit breaches: AR Supervisor recommends standard account status with potential credit limit increase per W24 annual review, (b) if any payment delays > 30 days: extend probationary period 6 months with credit limit review, (c) if payment defaults: Finance Manager decides between continued probation with reduced limit or account closure | AR Supervisor | Finance Manager | 30 min/account |
| 9 | Monthly: AR Supervisor generates reactivation report — number of reactivations by scenario, approval tier utilization, probationary account performance, recovered revenue from reactivated accounts; includes in monthly AR aging review | AR Supervisor | Finance Manager | 30 min/month |

### System Touchpoints
- Account reactivation workflow with scenario-based routing (dormant, closed, written-off, new entity) (W84.3–5a)
- Prior account history retrieval with write-off/dormancy reason display (W84.2)
- Enhanced credit review flag for written-off account reactivation (W84.5)
- Probationary account status with 6-month automatic review scheduling (W84.6, 8)
- Entity linkage: new entity linked to prior written-off entity for risk monitoring (W84.5a)
- Reactivation analytics: volume by scenario, approval tier, probationary performance, recovered revenue (W84.9)
- Integration with W8 (AR management — dormant account management, account closure), W24 (credit application), W58 (corporate account management), W81 (bad debt write-off — settlement confirmation)

### Staffing Implication
- **AR Clerk**: ~20–40 reactivations/month × 30 min average = ~10–20 hours/month. Absorbed within existing AR team.
- **AR Supervisor**: review and approval adds ~5 hours/month. Absorbed.
- **Finance Manager**: Credit Committee participation for written-off reactivations adds ~2–4 hours/month. Absorbed.
- **No incremental headcount.**

---

## W87. Customer Feedback-to-Action Loop

| Field | Detail |
|---|---|
| **Trigger** | Monthly complaint analytics review (W41.11); or quarterly CSAT/NPS deep analysis (W65.6); or recurring pattern identified by BI Analyst |
| **Frequency** | Monthly review; quarterly action planning; annual strategic review |
| **Volume** | ~2,000–3,000 complaints/month + ~5,000–10,000 survey responses/month feeding into the loop |
| **Owner** | CS Manager (operational); Store Ops Director (store-level actions); CMO (strategic) |
| **Participants** | CS Manager, Store Ops Director, Regional Managers, Category Managers, Training Officer, BI Analyst, CMO |

### Background

BuildRight collects rich customer feedback through multiple channels: complaint tickets (W41), CSAT/NPS surveys (W65), loyalty program data (W17), mystery shopping results (W65), and social media monitoring. However, there is no formal workflow for systematically converting this feedback into operational improvements, product changes, or service enhancements. This workflow closes the loop — ensuring that customer insights drive continuous improvement rather than remaining as reports.

### Monthly Feedback Review (by day 15 of each month, after W41 and W65 reporting)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | CS Manager compiles monthly feedback synthesis from: (a) W41 complaint analytics — top 5 complaint categories, top 10 stores by complaint volume, recurring root causes, unresolved escalations, (b) W65 CSAT/NPS scores — stores below threshold (< 85% CSAT), trending decline, specific department-level issues from survey comments, (c) W17 loyalty data — points redemption patterns, tier movement, enrollment drop-offs, loyalty program feedback, (d) social media sentiment — review of mentions, reviews, and direct messages aggregated by social media monitoring tool, (e) W58 corporate account feedback — Sales Rep reports of customer dissatisfaction with pricing, delivery, or service | CS Manager | CMO | 4 hours/month |
| 2 | CS Manager categorizes feedback into actionable themes: (a) **Quick wins** — individual issues resolvable by a single department within 1 week (e.g., specific store cleanliness issue, individual staff behavior, specific SKU pricing error), (b) **Process improvements** — recurring issues requiring process or procedure changes across multiple locations (e.g., BOPIS pickup SLA not met consistently, DSD receiving causing customer wait times, returns policy confusion), (c) **Training needs** — patterns indicating skill or knowledge gaps (e.g., product knowledge complaints in specific departments, POS error rates by store), (d) **Product/service changes** — feedback suggesting product assortment gaps, new service needs, or pricing concerns, (e) **Strategic themes** — fundamental customer experience shifts (e.g., channel preference changes, competitive threats, brand perception issues) | CS Manager | CMO | 2 hours/month |
| 3 | CS Manager assigns quick wins to responsible department with specific action items and 1-week resolution SLA: (a) store-level issues → Regional Manager → Store Manager, (b) product issues → Category Manager, (c) pricing issues → Pricing Analyst, (d) delivery issues → DC Dispatch / Fleet Manager, (e) website/app issues → Ecom Team | CS Manager | Department Head | 1 hour/month |
| 4 | CS Manager follows up on prior month's quick win resolution status; reports completion rate to CMO; unresolved items escalated to department head | CS Manager | CMO | 30 min/month |

### Quarterly Action Planning (aligned with W35 quarterly management review)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 5 | CS Manager prepares quarterly customer experience improvement report: (a) complaint trend analysis — month-over-month volume, resolution rate, SLA compliance trend, (b) CSAT/NPS trend with store heat map, (c) top 5 recurring root causes with frequency and business impact (estimated revenue at risk from unresolved issues), (d) process improvement recommendations — specific process changes with expected impact, (e) training recommendations — specific programs with target audience, (f) product/service change recommendations — new products, discontinued products, service enhancements based on customer demand | CS Manager | CMO | 8 hours/quarter |
| 6 | CS Manager presents quarterly report to cross-functional customer experience review meeting — attended by Store Ops Director, VP Merchandising, Training Officer, BI Analyst, and CMO; meeting reviews each recommendation and assigns owners, deadlines, and success metrics | CS Manager / CMO | COO | 2 hours/quarter |
| 7 | **Process improvements**: Store Ops Director (for operational changes), VP Merchandising (for product/pricing changes), or CIO (for system changes) implements approved process improvements; changes documented in system with expected completion date; CS Manager tracks implementation status | Department Head | COO | Varies |
| 8 | **Training needs**: Training Officer incorporates approved training recommendations into W51 training calendar — develops targeted training materials for identified gaps (e.g., product knowledge for specific departments, returns handling refresher for CSRs, delivery communication for ecommerce team); training completion tracked and reported to CS Manager | Training Officer | HR Head | Per W51 |
| 9 | **Product/service changes**: Category Managers review product feedback recommendations during next W1 quarterly assortment review; CMO reviews service enhancement proposals for feasibility and budget; approved changes implemented through existing workflows (W1, W13, W40, W58) | Category Manager / CMO | VP Merchandising / COO | Per existing workflows |
| 10 | CS Manager tracks all quarterly action items to completion; reports status at next quarterly review; closed action items archived with outcome measurement (did the action reduce complaints or improve CSAT?) | CS Manager | CMO | 2 hours/quarter |

### Annual Strategic Review (aligned with W26 annual budget cycle)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 11 | CMO and CS Manager prepare annual customer experience strategic review: (a) year-over-year CSAT/NPS trend, (b) complaint volume and resolution efficiency trend, (c) customer retention rate (loyalty member active rate, trade account retention), (d) voice-of-customer themes for the year, (e) competitive customer experience benchmarking (where available), (f) investment recommendations — technology, staffing, training, or service enhancements to improve customer experience, (g) proposed customer experience KPIs for next year | CMO / CS Manager | CEO | 8 hours/year |
| 12 | CMO presents annual CX review to CEO and management committee; approved investments included in next year's budget (W26) | CMO | CEO | 1 hour/year |

### Feedback Loop Tracking Dashboard

| Metric | Source | Frequency | Target |
|---|---|---|---|
| Quick win resolution rate | W87.4 | Monthly | ≥ 90% within 1-week SLA |
| Process improvement implementation rate | W87.7 | Quarterly | ≥ 80% of approved improvements implemented on schedule |
| Training completion rate for CX-targeted programs | W87.8 | Quarterly | 100% completion by target date |
| CSAT/NPS improvement vs. prior quarter | W65 | Quarterly | Positive trend in bottom 10 stores |
| Complaint reduction in top 5 root causes | W41 | Quarterly | ≥ 15% reduction per quarter |
| Revenue at risk from unresolved feedback | W87.5c | Quarterly | Decreasing trend |

### System Touchpoints
- Feedback synthesis dashboard: aggregates W41 complaint data, W65 CSAT/NPS scores, W17 loyalty insights, social media sentiment, and W58 corporate account feedback into a single view (W87.1)
- Action item tracking: assigns ownership, deadline, and success metrics per recommendation; tracks completion status (W87.3–4, 6–10)
- Quarterly improvement report generation with trend analysis and store heat map (W87.5)
- Annual CX strategic review archive with year-over-year comparison (W87.11)
- Integration with W1 (assortment changes from product feedback), W13 (promotional adjustments), W41 (complaint data source), W51 (training improvements), W65 (CSAT/NPS data source), W67 (store performance review — CX action items in store scorecard), W83 (marketing campaign feedback)

### Staffing Implication
- **CS Manager**: adds ~8 hours/month for feedback synthesis and action tracking + ~10 hours/quarter for quarterly planning = ~130 hours/year. Absorbed within existing CS Manager role.
- **BI Analyst**: adds ~2 hours/month for feedback data analysis and dashboard support. Absorbed.
- **No incremental headcount.** Cross-functional action execution is absorbed by respective departments.

---



## W103. Trade Sales Pipeline & Territory Management

| Field | Detail |
|---|---|
| **Trigger** | Monthly sales review calendar; new lead qualification; territory rebalancing decision |
| **Frequency** | Weekly pipeline review; monthly territory performance review; quarterly territory rebalancing |
| **Volume** | ~5,000 trade accounts + 200 corporate accounts generating 30% of revenue (~PHP 18.7B/year); managed by ~10–12 Sales Reps |
| **Owner** | Sales Rep (pipeline); Sales Manager / AR Supervisor (territory) |
| **Participants** | Sales Rep, Sales Manager, AR Supervisor, Category Manager, VP Merchandising, Store Manager |

### Background

W58 (Corporate/Project Account Management) covers the operational management of existing corporate accounts — quoting, ordering, delivery, and billing. However, there is no workflow governing the sales pipeline itself: how new trade/corporate leads are qualified, how the sales team manages their pipeline from prospect to closed account, how territories are assigned and balanced, and how sales targets are tracked and reviewed. With B2B trade and corporate accounts representing 30% of total revenue (PHP 18.7B/year), this is a significant operational gap.

### Steps

### Weekly Pipeline Review

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Sales Rep updates CRM pipeline: for each active prospect/lead — (a) company name, contact person, estimated annual potential (based on project size or trade volume), (b) pipeline stage: Prospect → Qualified → Quotation Sent → Negotiation → Won/Lost, (c) next action and target close date, (d) probability weighting (Prospect 10%, Qualified 25%, Quotation 50%, Negotiation 75%), (e) competitive situation (which competitor currently supplies, switching barriers) | Sales Rep | Sales Manager | 30 min/week |
| 2 | Sales Manager reviews pipeline dashboard: (a) total weighted pipeline value per Sales Rep, (b) pipeline stage distribution (healthy pipeline has 3× quota in qualified+ stages), (c) stalled opportunities — no activity in 14 days flagged for Sales Rep action, (d) upcoming target close dates at risk, (e) win/loss ratio for the quarter | Sales Manager | VP Merchandising | 1 hour/week |
| 3 | Sales Manager conducts weekly 15-min pipeline coaching call with each Sales Rep (10–12 calls = ~3 hours/week): review top 5 opportunities, discuss strategy for stalled deals, provide coaching on competitive positioning | Sales Manager | VP Merchandising | 15 min/Sales Rep |
| 4 | **New lead qualification**: Sources of new trade/corporate leads — (a) walk-in contractor/builder at store referred by Sales Associate or CSR, (b) inbound inquiry via website/phone, (c) Sales Rep proactive prospecting (construction site visits, industry events, referrals from existing accounts), (d) marketing campaign response (W83), (e) new business permit filings in trade area (public data); Sales Rep qualifies lead: (i) Is the prospect a legitimate business? (DTI/SEC registration, TIN), (ii) Estimated annual material spend in BuildRight categories?, (iii) Geographic fit — does the prospect operate within a store's trade area?, (iv) Competitive incumbent — is there an opportunity to displace?, (v) Payment capability — will they qualify for trade credit per W24? | Sales Rep | Sales Manager | 30 min/lead |

### Monthly Territory Performance Review

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 5 | System generates monthly territory performance report per Sales Rep: (a) total revenue from trade/corporate accounts in territory vs. target, (b) new account openings vs. target, (c) active account count and revenue per account (identify top 10 and dormant accounts), (d) average order value and order frequency per account, (e) credit utilization (outstanding AR as % of total credit limits in territory), (f) win rate on quotations submitted (W58.1a), (g) average quotation-to-close cycle time | System | — | Automated |
| 6 | Sales Manager reviews territory performance with each Sales Rep: (a) revenue vs. target — on track, ahead, or behind, (b) new account acquisition — sufficient pipeline to meet annual target?, (c) dormant account reactivation — identify accounts with no orders in 90+ days for W84 reactivation outreach, (d) high-value account deepening — top accounts with potential for increased share-of-wallet, (e) territory issues — competitive pressure, geographic coverage gaps, account conflicts with neighboring Sales Reps | Sales Manager / Sales Rep | VP Merchandising | 30 min/Sales Rep |
| 7 | Sales Manager and Sales Rep agree on monthly action plan: top 5 accounts to grow, top 5 prospects to close, top 5 dormant accounts to reactivate; system tracks action items | Sales Manager | VP Merchandising | 10 min/Sales Rep |

### Quarterly Territory Rebalancing

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 8 | Sales Manager reviews territory balance: (a) revenue per territory — flag imbalances > 20% from average, (b) account count per territory, (c) geographic coverage — are new store trade areas adequately covered?, (d) account-to-revenue ratio — are some Sales Reps overburdened with small accounts? | Sales Manager | VP Merchandising | 2 hours/quarter |
| 9 | If rebalancing needed: Sales Manager proposes territory realignment — reassigns accounts between Sales Reps based on geographic proximity, account size fit, and Sales Rep capability; VP Merchandising approves; system updates account assignments; affected Sales Reps briefed; customers notified of new contact if relationship changes | Sales Manager | VP Merchandising | 1 hour/rebalancing |
| 10 | Annual: VP Merchandising and Sales Manager set territory revenue targets for next year based on: (a) prior year actual by territory, (b) known project pipeline in each territory, (c) new store openings (W16) creating new trade areas, (d) market growth assumptions, (e) competitive landscape; targets feed into W26 annual budget | VP Merchandising / Sales Manager | CEO | 4 hours/year |

### Territory Assignment Rules

| Territory Dimension | Assignment Logic |
|---|---|
| **Geographic** | Each Sales Rep assigned a primary region (Mindanao, Visayas, Luzon-South, Luzon-North, Metro Manila) with defined store coverage |
| **Account size** | Corporate accounts (> PHP 5M annual) may have dedicated Sales Rep; trade accounts shared within region |
| **Industry vertical** | Sales Reps may specialize: construction contractors, interior designers, government/institutional (W78), property developers |
| **Account conflicts** | If customer operates across territories, primary Sales Rep assigned based on customer HQ location; cross-territory orders credited to primary Sales Rep with secondary credit to fulfilling store |

### System Touchpoints
- CRM pipeline management with stage tracking, probability weighting, and activity logging (W103.1)
- Pipeline dashboard: weighted value, stage distribution, stalled opportunities, win/loss ratio (W103.2)
- Territory performance reporting: revenue vs. target, new accounts, dormant accounts, credit utilization (W103.5)
- Territory assignment master data with geographic, account size, and vertical dimensions (W103 territory table)
- Account-to-Sales-Rep assignment with change history and approval trail (W103.9)
- Integration with W24 (credit application — new accounts enter pipeline), W41 (complaints — can trigger at-risk account review), W58 (corporate account operations — won pipeline accounts transition to W58 management), W84 (account reactivation — dormant accounts identified in territory review), W26 (annual budget — sales targets feed budget)

### Staffing Implication
- **10–12 Sales Reps** (Trade & Corporate): already assumed within the model company's ~310 HQ headcount; this workflow formalizes their operating cadence. Weekly pipeline maintenance (~30 min) + monthly territory review (~30 min) = ~4 hours/month per Sales Rep. This is core sales activity.
- **1 Sales Manager**: manages 10–12 Sales Reps. Weekly pipeline review (~3 hours) + monthly territory reviews (~6 hours) + quarterly rebalancing (~3 hours) = ~12 hours/month. This is a full-time management role.
- **No incremental headcount** — these roles are implied by the 30% B2B revenue but were not formalized in a workflow.

---

## W112. Trade Counter / Pro Desk Operations

| Field | Detail |
|---|---|
| **Trigger** | Professional trade customer (contractor, builder, architect, interior designer, electrician, plumber) arrives at store or contacts Sales Rep for project-level assistance |
| **Frequency** | ~15–25 trade counter interactions per store per week; ~3,000–5,000/week chain-wide |
| **Volume** | 30% of revenue from professional/trade B2B customers (~PHP 18.7B/year); avg trade transaction value ~PHP 5,000–25,000 |
| **Owner** | Sales Associate (trade counter); Sales Rep (field/pro desk) |
| **Participants** | Sales Associate, Sales Rep, Department Supervisor, Store Manager, Customer (trade professional) |

### Background

Big-box home improvement retailers globally operate dedicated trade counters or "pro desks" — specialized service points where professional customers (contractors, builders, tradespeople) receive tailored service: bulk pricing, project estimation, job site delivery coordination, account management, and credit access. BuildRight's trade customers represent 30% of revenue (~PHP 18.7B/year) across ~5,000 trade accounts, yet there is no workflow defining how trade counter service operates in-store. While W58 covers corporate/project account management and W103 covers sales pipeline, this workflow addresses the daily in-store operational process for serving trade customers at the pro desk — the physical touchpoint where most trade revenue is captured.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Customer check-in**: Trade customer arrives at store and proceeds to trade counter / pro desk (designated area near customer service counter with dedicated Sales Associate); Sales Associate identifies customer: (a) scans loyalty card or enters mobile number — system loads customer profile, trade account status, credit limit, and purchase history; (b) if not yet a trade account holder: Sales Associate provides W24 credit application form and explains trade account benefits (trade pricing, credit terms, bulk ordering); (c) system displays customer's open orders (W56 backorders, W38 special orders), recent purchases, and any account alerts (credit limit approaching, overdue balance) | Sales Associate | Department Supervisor | 2 min |
| 2 | **Needs assessment**: Sales Associate conducts needs assessment: (a) **Project-based** — customer describes project (e.g., "building a 2-story residential, 150 sqm floor area, 3 bathrooms"); Sales Associate helps estimate material requirements using system's project estimation tool (pre-built project templates per project type: residential build, bathroom renovation, kitchen remodel, electrical wiring for a house); (b) **Replenishment** — customer provides material list (paper, digital, or photo); Sales Associate enters items in system for availability check and pricing; (c) **Emergency / same-day** — customer needs specific items immediately; Sales Associate checks real-time inventory and provides immediate availability | Sales Associate | Department Supervisor | 5–15 min |
| 3 | **Material list and quotation**: (a) Sales Associate builds material list in system — adds items, quantities, checks real-time inventory at this store and nearby stores; (b) system applies trade account pricing (trade discount tier per W5b.4c); (c) for project-based orders: Sales Associate applies project-specific price list if customer has negotiated project pricing (W58); (d) system calculates total with trade discount, quantity breaks (W40.15–19), and VAT; (e) Sales Associate presents quotation to customer — printed or emailed; (f) for large projects (estimated > PHP 100,000): Sales Associate involves Sales Rep for on-site visit and detailed project estimation per W103 | Sales Associate / Sales Rep | Department Supervisor | 10–20 min |
| 4 | **Order placement**: Customer confirms order: (a) **Immediate in-store purchase**: items in stock at this store — customer collects items or Sales Associate arranges store pickup staging; processed as standard POS transaction with trade account pricing (W5b.4c); (b) **Bulk delivery order**: items to be delivered to job site — Sales Associate creates Sales Order with delivery address, delivery date, and delivery instructions; delivery processed per W5d (in-store delivery scheduling) or W19 (home delivery) depending on item size and distance; (c) **Backorder / special order**: items not in stock — Sales Associate creates backorder per W56 or special order per W38; (d) **Project billing**: for corporate/project accounts — order charged to project account with project code; billing per W58 milestone/progress billing | Sales Associate | Store Manager | 5–10 min |
| 5 | **Delivery coordination for trade orders**: For orders requiring job site delivery: (a) Sales Associate coordinates delivery date and time with customer (contractors often need early morning delivery before work starts); (b) system creates delivery order with job site address, contact person, special instructions (e.g., "deliver to 3rd floor under construction", "call 30 min before arrival"); (c) for recurring delivery orders (multi-phase construction project): Sales Associate sets up recurring delivery schedule in system — customer calls or emails when next batch of materials is needed; system retains project material list for easy reorder | Sales Associate | Store Manager | 5 min |
| 6 | **Trade customer relationship management**: (a) Sales Associate or Sales Rep documents interaction in CRM: project type, estimated project value, competing supplier information, customer satisfaction; (b) for active construction projects: Sales Rep schedules periodic follow-up calls/visits to check material needs for next project phase; (c) Sales Associate tracks trade customer visit frequency and purchase pattern — alerts Sales Rep if regular trade customer hasn't visited in > 30 days (may have switched to competitor); (d) system tracks lifetime trade customer value (total spend, frequency, margin contribution) for loyalty tier and account management decisions | Sales Associate / Sales Rep | Sales Manager | 5 min/interaction |
| 7 | **Trade account statement and payment**: (a) Trade customers on credit terms receive monthly statement per W8; (b) walk-in trade customers (COD/cash) can pay at trade counter via cash, card, or e-wallet; (c) Sales Associate can pull up customer's AR statement on request — outstanding balance, available credit, payment due dates; (d) for overdue accounts: Sales Associate informs customer of credit hold status and directs to AR for resolution per W108 | Sales Associate | Department Supervisor | 2 min |
| 8 | **Weekly trade counter performance**: Store Manager reviews weekly trade counter metrics: (a) trade counter transactions — count and value, (b) average trade transaction value, (c) trade customer visit frequency and retention, (d) top 10 trade customers by spend (store-level), (e) conversion rate — quotations generated vs. orders placed, (f) material list completion rate — how often were all items on the customer's list available? | Store Manager | Regional Manager | 30 min/week |

### System Touchpoints
- Trade customer identification via loyalty card or mobile number with account profile and purchase history (W112.1)
- Project estimation tool with pre-built templates per project type (residential build, bathroom renovation, electrical wiring) (W112.2)
- Material list builder with real-time inventory check, trade pricing application, and quantity break auto-calculation (W112.3)
- Quotation generation (print or email) with trade account pricing and VAT (W112.3)
- Sales Order creation with delivery scheduling and job site address (W112.4)
- Recurring delivery order setup for multi-phase construction projects (W112.5)
- CRM interaction logging with project type, estimated value, and follow-up scheduling (W112.6)
- Trade customer visit frequency tracking with inactivity alerting (W112.6)
- AR statement access at trade counter for account balance and credit status (W112.7)
- Weekly trade counter performance dashboard (W112.8)
- Integration with W5b (POS selling — trade account pricing), W5d (in-store delivery scheduling), W8 (AR — credit limit check, statement), W12 (returns — trade customer returns), W17 (loyalty — trade customer points), W24 (credit application — new trade customer signup), W38 (special orders — non-stock items for trade), W56 (backorders — stock items not available), W58 (corporate/project accounts — project billing), W61 (price matching — trade customers may request), W103 (sales pipeline — trade counter is a primary lead source), W108 (collections — overdue trade accounts)

### Staffing Implication
- **1 dedicated Sales Associate per store** at the trade counter / pro desk during operating hours: handles ~15–25 trade interactions/week × 20 min average = ~5–8 hours/week; remainder of time on floor coverage, special order follow-up, and delivery coordination. This is a specialized role within the existing 16 Sales Associates per store — not incremental headcount but a designated assignment.
- **Sales Reps** (10–12 at HQ): support large project quotes and on-site visits triggered from trade counter. Absorbed within existing W103 pipeline management.
- **No incremental headcount.**

---

---

## W156. Customer Data Platform (CDP) & Hyper-Personalization

| Field | Detail |
|---|---|
| **Trigger** | Real-time customer interaction (web visit, POS sale, app notification) |
| **Frequency** | Continuous |
| **Volume** | 600,000+ member profiles |
| **Owner** | Digital Marketing Manager |
| **Participants** | Data Analyst, CRM Team, IT, CMO |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Data Ingestion**: Aggregate data from POS (W5), Ecommerce (W11), and Loyalty (W17) into a unified "Golden Record" | System | IT Mgr | Real-time |
| 2 | **Segmentation**: System auto-assigns segments based on behavior: "DIY Hobbyist," "Professional Contractor," "Lapsed Buyer" | Data Analyst | Digital Mktg Mgr | Weekly |
| 3 | **Triggered Journeys**: Auto-trigger email/SMS based on events: "Abandoned Cart," "Project Follow-up," or "Refill Reminder" (for paint/consumables) | CRM Team | Digital Mktg Mgr | Automated |
| 4 | **Personalized Offers**: Push unique promo codes to the Mobile App based on individual purchase history | Digital Mktg Mgr | CMO | 1 hour |

---

## W258. Omni-channel Customer Ticketing & Support Management

| Field | Detail |
|---|---|
| **Trigger** | Customer reaches out via email, social media, phone, or live chat for inquiries, order status, or support |
| **Frequency** | Continuous |
| **Volume** | ~3,000 - 5,000 tickets/month |
| **Owner** | Customer Service Manager |
| **Participants** | CS Agents, Store Managers, DC Operations, Delivery Partners |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Ticket Creation**: System automatically consolidates omnichannel inputs (social, email, chat) into a single CRM ticketing queue | System | CS Manager | Automated |
| 2 | **Triage & Assignment**: Auto-assign ticket to specific agent or queue (e.g., "Ecommerce Delivery", "Product Inquiry", "Store Feedback") based on keywords and customer tier | System | CS Manager | Automated |
| 3 | **Resolution**: CS Agent reviews customer 360-degree profile (W156), accesses ERP for order status/inventory, and provides resolution or update | CS Agent | CS Manager | 10-15 min |
| 4 | **Escalation**: If issue requires store action (e.g., missing BOPIS item) or logistics action (e.g., lost package), agent escalates ticket to respective department | CS Agent | CS Manager | 5 min |
| 5 | **Closure & CSAT**: Ticket resolved; system automatically sends CSAT/NPS survey to customer (W65) to measure satisfaction with support | System | CS Manager | Automated |
---
