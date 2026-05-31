# Ecommerce Workflows

> BOPIS order fulfillment and home delivery fulfillment.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W11. Ecommerce — BOPIS Order Fulfillment](#ecommerce-bopis-order-fulfillment)
- [W19. Ecommerce — Home Delivery Fulfillment](#ecommerce-home-delivery-fulfillment)

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



---

