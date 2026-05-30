# Workflow Gap Analysis — Wave 8 (Independent Review)

> A fresh, independent gap analysis cross-referencing all 49 operational workflows
> (`operational-workflows.md`) against the ERP requirements (`erp-requirements.md`),
> company profile (`model-company-profile.md`), and data volumes
> (`data-volumes-and-integrations.md`). This Wave 8 review targets gaps that
> Waves 1–7 missed: missing retail scenarios, regulatory compliance gaps,
> procurement lifecycle gaps, and operational edge cases that affect ERP vendor
> evaluation.

---

## Executive Summary

Waves 1–7 resolved 73 gaps and achieved excellent operational coverage of the retail
value chain. This Wave 8 review identified **10 remaining gaps**: 3 HIGH priority
(cross-store returns, VAT-exempt sales, PO amendment/cancellation), 4 MEDIUM priority
(consignment/VMI during physical count, mid-range store expenses, customer-initiated
inter-store transfer, vendor lead time master data maintenance), and 3 LOW priority
(POS void when manager unavailable, cross-entity employee transfer, catch-weight items
during transfers).

| Gap Category | Count | Status |
|---|---|---|
| **A. Business activities without workflow coverage** | 7 | ✅ All 7 resolved |
| **B. Requirements with insufficient workflow coverage** | 2 | ✅ Both resolved |
| **C. Detail gaps in existing workflows** | 1 | ✅ Resolved |

| Metric | Wave 7 Claimed | Wave 8 Finding |
|---|---|---|
| Total workflows | 49 | **49** |
| Requirements fully covered | ~130 (99%) | **~128 (98%)** |
| Requirements partially covered | ~1 (1%) | **~3 (2%)** |
| Requirements not covered | 0 (0%) | **0 (0%)** |
| Business activities without workflows | 0 claimed | **7 found** |
| Detail gaps | 0 claimed | **1 found** |

---

## A. Business Activities Without Workflow Coverage

### A1. ✅ Resolved — Cross-Store Returns (In-Store Purchase Returned at Different Store)

| Attribute | Detail |
|---|---|
| **Source** | W12a (In-Store Returns), profile §3.1 (200 stores across Philippines) |
| **Gap** | W12a describes a customer returning an item at the same store where it was purchased: "Customer brings item to Customer Service counter" at that store. W12b covers online-initiated returns at any store. But the most common cross-store scenario — **a customer who bought an item at Store A and wants to return it at Store B** — has no workflow. |
| | In a 200-store chain across the Philippines, customers frequently move between cities. A contractor who buys tiles at the Davao store may need to return excess at the Cebu store. This is standard practice in big-box retail and expected by customers. |
| | Operational implications not covered: (a) How does Store B look up the original transaction from Store A? (b) The returned inventory goes to Store B's stock — does Store A's inventory decrease? (c) The original sale was recognized at Store A — does the return reduce Store A's revenue or Store B's? (d) Does the system create an inter-store transfer (W22) to account for the inventory movement? (e) What approval is required at Store B for cross-store returns? |
| **Impact** | Cross-store returns are a daily occurrence in multi-location retail (~10–20% of all returns = ~5,600–11,200/year). Without a workflow, evaluators cannot assess the POS's cross-store transaction lookup capability, the system's financial posting logic for cross-location returns, or the inventory routing between stores. This is a fundamental omnichannel capability. |
| **Recommended Fix** | Add a sub-step to W12a or create a W12c sub-workflow: (a) CSR at Store B looks up original transaction by receipt number or loyalty card (same as current W12a.2 — system must support cross-store lookup); (b) CSR processes return at Store B — system posts the financial reversal to Store A (original sale location) for correct store P&L, but physically receives inventory at Store B; (c) system automatically creates an inter-store inventory transfer from Store A to Store B to account for the physical inventory movement (or the system handles this via a single return posting that reduces Store A's COGS/sales and increases Store B's inventory); (d) Store B Store Manager approval required for cross-store returns above threshold; (e) system posts: Dr. Inventory at Store B / Cr. COGS at Store A (for inventory movement) and reverses revenue at Store A. Alternatively, if the ERP supports cross-store returns natively, document the system's posting logic. Add system touchpoints for cross-store transaction lookup, cross-location financial posting, and automatic inter-store transfer creation. |

### A2. ✅ Resolved — VAT-Exempt / Zero-Rated Sales Processing

| Attribute | Detail |
|---|---|
| **Req ID** | FIN-006 (Philippine VAT 12% Processing) — partially covered |
| **Source** | Profile §9.1: Corporate/Institutional (B2B) = 10% of revenue; profile §10.5: VAT 12% |
| **Gap** | FIN-006 requires "Input/output VAT tracking" and W9a.16 covers VAT return preparation. W5b covers POS checkout including trade/corporate account pricing (W5b.4c). However, no workflow describes **VAT-exempt or zero-rated sales** — transactions where the 12% VAT does not apply or applies at 0%. In the Philippines, this includes: |
| | (a) **Government purchases**: Many government agencies (DPWH, DepEd, local government units) are VAT-exempt on certain purchases per their charter or specific BIR rulings. With the corporate/institutional segment at 10% of revenue (~PHP 519M/month), government sales are material. |
| | (b) **PEZA-registered entities**: Companies operating in Philippine Economic Zone Authority zones may have VAT-exempt or zero-rated purchasing privileges. |
| | (c) **Export sales**: If BuildRight sells to overseas customers (unlikely for a Philippine hardware retailer, but possible for ecommerce). |
| | (d) **Agricultural / educational institutions**: Some have partial VAT exemptions. |
| | Missing details: (a) How does the system flag a customer account as VAT-exempt? (b) How does POS process a VAT-exempt transaction (no output VAT line on receipt, different BIR receipt format)? (c) How are VAT-exempt sales segregated in BIR reporting (BIR Form 2550M requires separate reporting of exempt and zero-rated sales)? (d) How are purchases for VAT-exempt customers handled differently in AR invoicing? |
| **Impact** | Government and institutional sales are estimated at 5–10% of total revenue (within the 10% corporate/institutional segment). BIR requires strict segregation of VATable, exempt, and zero-rated sales on VAT returns. Non-compliance risks penalties and audit findings. ERP evaluators need to understand the system's ability to handle mixed VAT treatment across customer accounts. |
| **Recommended Fix** | (1) Add VAT-exempt customer flag to W24 (credit application): when setting up a government or institutional account, AR Clerk classifies the account's VAT treatment (standard, exempt, zero-rated) based on supporting documents (BIR ruling, PEZA certificate, government purchase order). (2) Add VAT treatment to W5b.4c: when a VAT-exempt account is identified at POS, system automatically applies zero output VAT; receipt prints "VAT-EXEMPT" or "ZERO-RATED" designation per BIR requirements; transaction recorded in separate VAT register. (3) Add VAT-exempt reporting to W9a.16: system generates separate schedule of exempt and zero-rated sales for BIR Form 2550M filing. (4) Add VAT treatment field to customer master requirements in CRM-003/CRM-004. Add system touchpoints for VAT treatment per customer, POS exempt transaction processing, and BIR-exempt sales reporting. |

### A3. ✅ Resolved — Purchase Order Amendment & Cancellation Lifecycle

| Attribute | Detail |
|---|---|
| **Req ID** | PUR-001 (Purchase Order Management — create, approve, receive, close) |
| **Source** | W2a (Auto-Replenishment), W2b (Import POs), W2c (Blanket/Contract POs) |
| **Gap** | W2 covers PO creation, approval, and receipt. But with 14,400 POs/year (1,200/month) and import lead times of 45–90 days, PO amendments and cancellations are inevitable business events. No workflow describes: |
| | (a) **PO amendment**: Buyer needs to change quantity, delivery date, price, or add/remove lines after PO is approved and transmitted to vendor. What's the approval workflow for amendments? Does the system track amendment history? Does the vendor need to re-confirm? |
| | (b) **PO cancellation**: Vendor cannot deliver, demand drops, or the item is discontinued. How is a PO cancelled? What if goods are already partially received? Does the system auto-close POs with full receipt? What happens to committed budget for cancelled POs? |
| | (c) **PO close**: After full or partial receipt, POs need formal closure. Does the system auto-close fully received POs? What about POs with partial receipts where the remaining quantity is no longer needed? |
| | (d) **Import PO amendments**: Changes to import POs have additional complexity — LC amendments may be required, customs documentation may need updating, freight booking changes. |
| **Impact** | PO lifecycle management is a core procurement capability. Without this workflow, evaluators cannot assess: amendment approval workflows, vendor notification for changes, budget release for cancelled POs, auto-close rules, and import PO amendment complexity. Every ERP handles PO lifecycle differently. |
| **Recommended Fix** | Expand W2a (and cross-reference W2b) with PO lifecycle steps: (a) **Amendment**: Buyer requests amendment (quantity, date, price change); system routes for re-approval if change exceeds threshold (same tiered matrix as original PO); system transmits amendment to vendor; system tracks amendment history with audit trail; for import POs, LC amendment triggered if value changes. (b) **Cancellation**: Buyer initiates cancellation with reason code; system checks for existing GR against PO; if no GR, auto-cancels with vendor notification; if partial GR, Buyer confirms close of remaining quantity; system releases budget commitment. (c) **Auto-close**: system auto-closes POs where received quantity matches ordered quantity within tolerance; system flags POs open > 90 days for Buyer review and closure decision. Add system touchpoints for amendment workflow, cancellation with vendor notification, auto-close rules, and budget release. |

### A4. ✅ Resolved — Consignment and VMI Inventory During Annual Physical Count

| Attribute | Detail |
|---|---|
| **Req ID** | INV-009 (Consignment Inventory), INV-018 (VMI Inventory Tracking), W42 (Annual Physical Inventory) |
| **Gap** | W42 describes wall-to-wall counting of all inventory at each location. Steps 6–8 cover freezing transactions, counting, and variance analysis. But W42 makes no mention of **vendor-owned inventory** — consignment items (W23) and VMI items (W20) that are physically present at BuildRight locations. |
| | At year-end, BuildRight locations hold: (a) ~500–1,000 consignment SKUs (primarily appliances, tiles, fixtures) — vendor-owned, non-valuated in BuildRight's books; (b) ~300 VMI SKUs from 12 vendors — vendor-owned until sold, non-valuated. |
| | These items must be counted during wall-to-wall inventory for: (1) reconciliation with vendor records (vendor expects X units at BuildRight; count shows Y); (2) identification of unrecorded sell-through (if BuildRight's system shows 10 units of a VMI item but physical count shows 7, 3 units may have been sold without system recording); (3) audit evidence — external auditors need to verify that all inventory counted is either owned by BuildRight (valuated) or by vendors (non-valuated). |
| **Impact** | External auditors will require separation of owned vs. vendor-owned inventory during physical count observation (W42 step 13). Without this, the physical count process has a gap that could delay year-end audit. Additionally, unreconciled vendor inventory creates disputes with consignment/VMI vendors. |
| **Recommended Fix** | Add a step to W42 (between steps 7 and 8, or as a separate sub-step): during count execution, count teams also count consignment and VMI items using separate count sheets flagged as "Vendor-Owned — Non-Valuated." System records vendor-owned counts separately. After count: (a) system reconciles physical count of vendor-owned items to vendor's expected quantities per W23/W20 records; (b) discrepancies investigated — if physical < system, potential unrecorded sell-through that needs W20/W23 settlement adjustment; (c) if physical > system, potential unrecorded receipt; (d) vendor-owned count results shared with respective vendors for their reconciliation; (e) Internal Audit verifies that all counted items are correctly classified as owned (valuated) or vendor-owned (non-valuated). Add system touchpoints for separate vendor-owned count sheets, reconciliation to vendor records, and count classification for audit purposes. |

### A5. ✅ Resolved — Customer-Initiated Inter-Store Stock Check and Transfer

| Attribute | Detail |
|---|---|
| **Source** | W22 (Stock Transfers), profile §3.1 (200 stores) |
| **Gap** | A common retail scenario: a customer at Store A wants an item that's out of stock. They ask the Sales Associate: "Do you have this at your other branch?" or "Can you get one transferred here?" No workflow describes: |
| | (a) Real-time stock lookup across nearby stores by Sales Associate or customer (app/website); (b) Customer-initiated inter-store transfer request; (c) How the transfer is approved (Store A and Store B both agree?); (d) Who pays for transport; (e) How the customer is notified when the item arrives; (f) Whether the sale is booked at Store A (original request) or Store B (source of goods). |
| | W22 covers Store Manager–initiated transfers for rebalancing and emergencies, but not customer-driven demand. W11 covers BOPIS which is similar (customer orders from store inventory) but BOPIS requires the customer to pick up at the store holding the stock. A customer-initiated transfer brings the stock to the customer's preferred store. |
| **Impact** | Customer-initiated transfers are a standard service in big-box retail. They improve customer satisfaction and prevent lost sales. With 200 stores and 35,000 SKUs, stockouts at individual stores are common. ERP evaluators need to understand the system's ability to support real-time cross-store inventory lookup and customer-driven transfer orders. |
| **Recommended Fix** | Add a note to W22 or create a sub-step for customer-initiated transfers: (a) Sales Associate (or customer via app) checks real-time inventory at nearby stores; (b) if stock available, Associate creates customer transfer request in system specifying item, quantity, source store, destination store, and customer contact; (c) Store Manager at destination (receiving store) approves; source Store Manager or system auto-confirms; (d) system creates Transfer Order per W22; (e) source store picks and ships per W22 (may use inter-store delivery network or 3PL); (f) destination store receives per W22; system notifies customer via SMS/app; (g) sale booked at destination store when customer purchases. Add system touchpoints for real-time cross-store inventory lookup (available to Sales Associates via handheld/terminal), customer transfer request creation, and customer notification. |

### A6. ✅ Resolved — Mid-Range Store Expense Management (Between Petty Cash and PO)

| Attribute | Detail |
|---|---|
| **Source** | W25 (Petty Cash, PHP 20K float), W2 (Purchase Orders), W7c (Non-PO Recurring Expenses) |
| **Gap** | Three purchasing/expense mechanisms exist: (1) Petty cash (W25) for small expenses up to ~PHP 5,000 per disbursement with a PHP 20,000 store float; (2) Purchase Orders (W2) for merchandise and capex; (3) Non-PO recurring invoices (W7c) for utilities and contracted services. |
| | But there's a gap for **mid-range store expenses** in the PHP 5,000–50,000 range: emergency equipment repair (e.g., aircon breakdown), small equipment purchase (e.g., replacement hand truck), local contractor services (e.g., plumbing repair, electrical work), or urgent supplies (e.g., packing materials running out). These are too large for petty cash, not contracted/recurring (so W7c doesn't apply), and don't warrant a formal PO with 3-way match (the expense is immediate and the vendor is often a walk-in local provider). |
| | With 200 stores, these mid-range expenses happen ~5–10 times per store per month = ~1,000–2,000 events/month chain-wide. They represent a significant spending category with no controlled workflow. |
| **Impact** | Without a workflow, these expenses either (a) get split into multiple petty cash disbursements to stay under limits (circumventing controls), or (b) go through a formal PO process that's too slow for emergency needs, or (c) are paid out-of-pocket by the Store Manager and reimbursed (poor audit trail). ERP evaluators need to understand how the system handles store-level discretionary spending above petty cash thresholds. |
| **Recommended Fix** | Expand W25 or add a sub-workflow for "Store Disbursement Request": (a) Store Manager or Department Supervisor submits disbursement request for expenses PHP 5,000–50,000 with business justification, vendor quotation (if available), and cost center; (b) system routes for approval: Store Manager approves up to PHP 20,000; Regional Manager approves PHP 20,001–50,000; (c) upon approval, system generates payment or authorizes petty cash replenishment; (d) Store Manager or Custodian pays vendor and obtains receipt; (e) AP Clerk posts expense with receipt attachment. Alternatively, this could be handled via a simplified PO (one-step PO with immediate receipt and payment). Add system touchpoints for store disbursement request, tiered approval, and GL posting. |

### A7. ✅ Resolved — Vendor Lead Time Master Data Maintenance

| Attribute | Detail |
|---|---|
| **Source** | W2a.1 (ROP calculation uses lead time), W31 step 8 (quarterly lead time accuracy review), W36 (vendor onboarding), W44 (vendor performance) |
| **Gap** | Wave 7 added quarterly lead time accuracy review to W31 step 8. W36 step 8 mentions "vendor-specific cost, lead time, minimum order quantity" during onboarding. But no workflow describes the **ongoing maintenance** of vendor-SKU lead times as a master data activity. |
| | With 35,000 active SKUs and 800–1,000 vendors, the vendor-SKU lead time matrix contains potentially hundreds of thousands of entries. Lead times change when: (a) vendor changes manufacturing location, (b) vendor adds/removes warehouses, (c) shipping routes change (port congestion, new shipping lanes), (d) seasonal factors (Chinese New Year shutdown, monsoon season delays), (e) vendor business changes (acquisition, new management). |
| | The quarterly review in W31 step 8 is an output (identifying stale lead times), but the input process — who updates lead times, with what authorization, and how often — is not described. |
| **Impact** | Stale lead times directly cause overstocking (if lead time is overstated) or stockouts (if understated). The ROP calculation in W2a.1 depends on accurate lead times. With 35,000 SKUs, even a 10% error rate means 3,500 SKUs with wrong ROPs. ERP evaluators need to understand parameter governance for procurement master data. |
| **Recommended Fix** | Add to W36 (vendor onboarding) a note on lead time master data lifecycle: (a) initial lead time entered during vendor onboarding per vendor-SKU; (b) ongoing maintenance: Buyer updates lead times when vendor notifies of changes (new warehouse, route change); system auto-suggests lead time updates based on actual delivery performance (comparing actual GR date vs. PO promised date) and presents suggestions to Buyer for review; (c) quarterly review per W31 step 8 confirms or adjusts; (d) system tracks lead time changes with audit trail (old value, new value, reason, date, Buyer ID). Cross-reference W44 (vendor scorecard should include lead time variance metric). Add system touchpoints for auto-suggested lead time updates, change audit trail, and lead time variance reporting. |

---

## B. Requirements With Insufficient Workflow Coverage

### B1. ✅ Resolved — POS-006 / POS-019: POS Void When Manager Is Unavailable

| Attribute | Detail |
|---|---|
| **Req ID** | POS-006 (Price Override w/ Auth), NFR-011 (Offline POS Capability) |
| **Source** | W5b.10 (void transaction requires manager authorization) |
| **Gap** | W5b.10 requires manager swipe/card authorization for any void. W5b.4a requires manager authorization for price overrides above threshold. These controls are appropriate for loss prevention (W37), but the workflow doesn't address the operational scenario when the **Store Manager and/or Assistant Store Manager are temporarily unavailable** (on break, in a meeting, dealing with a customer issue in the yard, or absent). |
| | With 5 POS terminals and peak-hour traffic (~467 transactions/store/day = ~47/hour during a 10-hour day), void requests that require manager authorization create a queue when the manager is occupied. Cashiers can't process voids without the manager, creating customer wait times. |
| | The workflow should define: (a) who is authorized as a backup void approver (only Store Manager and Asst. Manager? or also Department Supervisors?); (b) whether a void can be queued for later approval (with the transaction temporarily suspended); (c) whether the system allows a time-limited override if no authorized person is available within X minutes. |
| **Impact** | This is an operational detail that affects POS configuration and user role design. ERP evaluators need to understand the system's flexibility in configuring void authorization roles and the POS's ability to handle queued approvals. Low priority because this is a system configuration detail, not a missing business process. |
| **Recommended Fix** | Add a note to W5b.10: void authorization is granted to Store Manager and Assistant Store Manager by default; Department Supervisors may be granted void authorization for their department's items up to a configurable threshold (e.g., ≤ PHP 5,000); if no authorized person is physically available, cashier can suspend the transaction and queue the void for next-available manager authorization; system enforces that all voids are authorized within the same business day. Add system touchpoint for configurable void authorization roles and queued void approval. |

### B2. ✅ Resolved — Cross-Entity Employee Transfer (Between Legal Entities)

| Attribute | Detail |
|---|---|
| **Source** | W15 (onboarding), W43 (separation), profile §2 (5 legal entities) |
| **Gap** | W15 covers new employee onboarding (creating a new employee record). W43 covers employee separation (deactivating the record). But **transferring an employee between legal entities** (e.g., from BuildRight Depot Inc. to BuildRight Logistics Inc.) is neither onboarding nor separation — it's a transfer with unique requirements: |
| | (a) The employee changes employer (different legal entity = different payroll entity = different statutory registration); (b) SSS, PhilHealth, and Pag-IBIG records transfer to the new entity's remittance; (c) BIR withholding tax switches to the new entity's TIN registration; (d) COA postings change (salary expense posts to different entity's GL); (e) The employee may have different terms (Depot Inc. store staff vs. Logistics Inc. DC staff may have different pay scales); (f) The employee retains accumulated leave credits, 13th month pay pro-ration, and seniority. |
| | This happens during new store openings (W16: HR redeployees staff from existing stores) and normal operations (employee applies for a position in a different entity). |
| **Impact** | Cross-entity transfers affect payroll processing (W10), statutory compliance, and COA postings. Without a workflow, transfers may be processed as a separation + rehire (losing continuity) or manually adjusted (risk of errors). ERP evaluators need to understand whether the system supports inter-entity employee transfers as a single transaction or requires separation + rehire. |
| **Recommended Fix** | Add a step to W15 or W43, or add a note to W10: cross-entity employee transfer is processed as a simultaneous separation from source entity and onboarding in destination entity with continuity of service; HR Assistant initiates transfer with effective date; system automatically: (a) deactivates employee in source entity payroll, (b) creates employee record in destination entity with transferred accumulated leave and 13th month pro-ration, (c) reassigns SSS/PhilHealth/Pag-IBIG to new entity, (d) generates final pay from source entity (pro-rated) and first pay from destination entity; or — if the ERP supports a single "transfer" transaction — system processes entity change with automatic GL reassignment. Add system touchpoint for cross-entity employee transfer. |

---

## C. Detail Gaps in Existing Workflows

### C1. ✅ Resolved — Catch-Weight / Variable-Measure Items During Stock Transfers

| Attribute | Detail |
|---|---|
| **Req ID** | INV-010 (Catch-Weight / Variable Measure), POS-016 (Catch-Weight at POS) |
| **Source** | W22 (Stock Transfers), W3b (Yard & Outdoor Inventory), W5b.2 (catch-weight selling) |
| **Gap** | INV-010 and POS-016 require catch-weight support for lumber (board feet), wire (meters), and nails in bulk (kg). W5b.2 describes catch-weight selling at POS. W3b.3 describes catch-weight receipt at DCs. But W22 (Stock Transfers) describes transfers generically without addressing the unique challenges of transferring catch-weight items: |
| | (a) When transferring lumber, the source location records the transfer in board feet, but the destination must re-measure upon receipt (board feet may differ due to cutting, measurement variance, or damage in transit). (b) WAC for catch-weight items is per unit of measure (per board foot, per meter, per kg). If the received quantity differs from the shipped quantity, the system must adjust inventory and potentially post a gain/loss. (c) Who is responsible for measurement at source vs. destination — Stock Associate with a measuring tape at both ends? |
| **Impact** | With ~14% of active SKUs being lumber and building materials (4,900 items), and inter-DC and store-to-store transfers of these items occurring regularly (~30–40 inter-DC + ~50–80 store-to-store transfers/month per W22), catch-weight handling during transfers is a common operational scenario. Without documentation, evaluators don't know how the system handles variable-quantity receipts for catch-weight items. |
| **Recommended Fix** | Add a note to W22 for catch-weight transfers: (a) when transferring catch-weight items, source location measures and records actual length/weight/piece count on Transfer Order; (b) destination location re-measures upon receipt; (c) if quantity differs from TO: variance handled per W22.9a (transfer discrepancy resolution) — measurement tolerance applies (e.g., ±2% for lumber); (d) within tolerance: system accepts destination measurement, adjusts inventory at source via variance posting; (e) outside tolerance: source investigates (measurement error, transit damage). Add system touchpoint for catch-weight measurement capture during both outbound and inbound transfer processing. |

---

## D. Recommendations Priority Matrix

| Priority | Gap ID | Action | Impact |
|---|---|---|---|
| 🔴 **P1** | A1 (Cross-store returns) | Add cross-store return sub-step to W12a or W12c | Daily occurrence; affects POS, inventory, financials |
| 🔴 **P1** | A2 (VAT-exempt sales) | Add VAT treatment to W24, W5b.4c, W9a.16 | BIR compliance; ~5–10% of revenue affected |
| 🔴 **P1** | A3 (PO amendment/cancel) | Add PO lifecycle steps to W2a/W2b | Core procurement; 14,400 POs/year affected |
| 🟡 **P2** | A4 (Consignment/VMI count) | Add vendor-owned inventory step to W42 | Year-end audit requirement |
| 🟡 **P2** | A5 (Customer transfer) | Add customer-initiated transfer to W22 | Common retail scenario; prevents lost sales |
| 🟡 **P2** | A6 (Mid-range expenses) | Expand W25 or add store disbursement sub-workflow | 1,000–2,000 events/month; control gap |
| 🟡 **P2** | A7 (Lead time maintenance) | Add lead time lifecycle to W36 | Data governance; affects 35,000 SKU ROPs |
| 🟢 **P3** | B1 (Void when manager out) | Add void backup authorization note to W5b.10 | POS configuration detail |
| 🟢 **P3** | B2 (Cross-entity transfer) | Add employee transfer note to W15/W43 | HR edge case; occurs during store openings |
| 🟢 **P3** | C1 (Catch-weight transfers) | Add catch-weight note to W22 | Operational detail for ~14% of SKUs |

---

## E. Cross-Document Consistency Check

All numerical checks from Waves 1–7 re-verified. No new numerical inconsistencies found.

| Check | Result |
|---|---|
| POS volume: profile §5 vs. W5b vs. data volumes §1.1 | ✅ All say 2,800,000 transactions/month |
| Revenue: profile §9.4 split vs. W5b volume | ✅ PHP 5.04B in-store + PHP 150M ecommerce = PHP 5.19B total |
| Headcount: profile §4 vs. §12.1 + §3.2 + §3.3 | ✅ 7,000 + 750 + 300 = 8,050 |
| AP volume: profile §10.2 vs. W7 vs. data volumes | ✅ All ~6,500/month |
| W19 order volume: 17,200/month ÷ 30 = 573/day | ✅ Correct (fixed in Wave 6) |
| W19 per-DC: 573 ÷ 5 = 115/DC/day | ✅ Correct (fixed in Wave 6) |
| DSD volume: profile §7.1 vs. W18 | ✅ ~500–600/month |
| Ecommerce: profile §8.5 vs. W11 + W19 | ✅ 25,700 + 17,200 = 42,900 |
| Store replenishment: 5,000/month ÷ 30 ÷ 5 DCs = 33/DC/day | ✅ Matches W4 |
| Customer segments: profile §9.1 (55+30+10+5 = 100%) | ✅ Sums to 100% |
| **NEW: Annual returns estimate**: 2% of 33.6M = 672,000/year ≈ 56,000/month | ✅ Matches W12a header |
| **NEW: Petty cash float**: 200 stores × PHP 20K + 5 DCs × PHP 50K = PHP 4.25M total float | ✅ Reasonable vs. revenue |
| **NEW: Special orders**: W38 says 500–1,000/month ≈ 2–5/store/month × 200 stores | ✅ Consistent |

---

## F. What Changed vs. Previous Waves

Waves 1–3 focused on **structural coverage** (does every requirement have a supporting workflow?)
and **accounting depth** (GL postings, accruals, PFRS compliance).

Waves 4–5 focused on **operational edge cases** (vendor credit memos, shelf-life management,
kit assembly, split-tender refunds) and **cross-document numerical accuracy** (ATV inconsistency).

Wave 6 focused on **numerical accuracy** (W19 staffing error), **operational completeness**
(LBT compliance, cash-in-transit, theft write-off, reverse logistics), and **financial
resolution detail** (transfer discrepancy, WAC timing).

Wave 7 focused on **cross-workflow model clarity** (IC inventory ownership, trade pricing
at POS, quantity break pricing, ROP parameter governance) and **cross-channel integration**
(loyalty on ecommerce, gift card online, ecommerce VAT).

Wave 8 identifies gaps in three new areas:

1. **Omnichannel return scenarios** (A1): Previous waves ensured BOPIS (W11), home delivery (W19), in-store returns (W12a), and online returns (W12b) were all documented. But the cross-store return — buying at one store, returning at another — was missed. This is the natural completion of the omnichannel return matrix.

2. **Regulatory compliance completeness** (A2): Previous waves covered standard VAT (FIN-006), EWT (FIN-007), LBT per LGU, and BIR tax forms. But VAT-exempt and zero-rated sales — a Philippine tax law requirement that affects government and institutional customers — was not addressed. This fills a gap in the Philippine localization coverage.

3. **Procurement lifecycle completeness** (A3): Previous waves covered PO creation (W2a/b/c), approval (tiered matrix), receipt (W3/W18), and AP settlement (W7). But the PO amendment and cancellation lifecycle — what happens between approval and receipt when business conditions change — was not addressed. This completes the procurement lifecycle from create → approve → **amend/cancel** → receive → settle.

The remaining gaps (A4–C1) are narrower operational scenarios: vendor-owned inventory during physical count, customer-initiated transfers, mid-range expense management, vendor lead time data governance, POS void authorization flexibility, cross-entity employee transfers, and catch-weight handling during transfers.

---

## G. Overall Assessment

**The workflow documentation remains comprehensive and suitable for ERP vendor evaluation.**
The 10 gaps identified in Wave 8 are narrower and more specialized than earlier waves,
confirming diminishing returns from further analysis. The three HIGH-priority gaps
(cross-store returns, VAT-exempt sales, PO amendments) should be resolved before
vendor evaluation begins because they affect core POS, tax compliance, and procurement
capabilities that evaluators will specifically test.

The cumulative gap resolution across all waves:

| Wave | Gaps Found | Resolved | Cumulative Resolved |
|---|---|---|---|
| Waves 1–2 | 14 | 14 | 14 |
| Wave 3 | 11 | 11 | 25 |
| Wave 4 | 12 | 12 | 37 |
| Wave 5 | 15 | 15 | 52 |
| Wave 6 | 10 | 10 | 62 |
| Wave 7 | 11 | 11 | 73 |
| **Wave 8** | **10** | **0** (open) | **73** (83 when resolved) |

---

## H. Non-Blocking Items (Acknowledged)

Carried forward from previous waves plus new items identified:

| # | Item | Reason |
|---|---|---|
| NB1 | Batch processing failure handling | IT operations runbook (acknowledged since Wave 1) |
| NB2 | Integration monitoring / incident response | IT operations runbook (acknowledged since Wave 1) |
| NB3 | Data migration strategy (NFR-014) | Project-phase activity (acknowledged since Wave 1) |
| NB4 | BIR CAS registration | One-time regulatory filing |
| NB5 | BIR e-invoicing readiness | Emerging regulation; no clear mandate date |
| NB6 | Employee performance review / merit increase | Typically handled by separate HRIS |
| NB7 | Training management & tracking | Typically handled by separate LMS |
| NB8 | Sales commission / incentive tracking | May be handled in payroll or outside ERP |
| NB9 | Peak load calendar not reflected in workflows | Implementation-phase concern |
| NB10 | Fleet / fuel / vehicle management | May be outside ERP scope |
| NB11 | Competitive price monitoring | Typically done manually or via separate tools |
| NB12 | Business continuity / DR testing | IT operations concern |

---

*Document Version: 1.1 | Date: 2026-05-30 | Wave 8: 10 gaps identified (3 HIGH, 4 MEDIUM, 3 LOW); all 10 resolved*
