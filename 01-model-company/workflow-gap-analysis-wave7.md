# Workflow Gap Analysis — Wave 7 (Independent Review)

> A fresh, independent gap analysis cross-referencing all 49 operational workflows
> (`operational-workflows.md`) against the ERP requirements (`erp-requirements.md`),
> company profile (`model-company-profile.md`), and data volumes
> (`data-volumes-and-integrations.md`). This Wave 7 review targets gaps that
> Waves 1–6 missed: intercompany model ambiguities, pricing mechanics not covered
> by workflows, cross-workflow integration gaps, and operational edge cases that
> affect ERP vendor evaluation.

---

## Executive Summary

Waves 1–6 resolved 62 gaps and achieved excellent operational coverage of the retail
value chain. This Wave 7 review identified **11 remaining gaps**: 3 HIGH priority
(intercompany model ambiguity, trade pricing at POS, quantity break pricing),
4 MEDIUM priority (ecommerce IC settlement, VMI at POS, ROP parameter governance,
loyalty points on ecommerce), and 4 LOW priority (RTV logistics, gift card online
redemption, store occupancy cost allocation, ecommerce VAT handling).

**All 11 gaps have been resolved.**

| Gap Category | Count | Status |
|---|---|---|
| **A. Cross-workflow model ambiguity** | 1 | ✅ Resolved |
| **B. Business activities without sufficient workflow coverage** | 6 | ✅ All 6 resolved |
| **C. Cross-workflow integration gaps** | 3 | ✅ All 3 resolved |
| **D. Detail gaps in existing workflows** | 1 | ✅ Resolved |

| Metric | Wave 6 Claimed | After Wave 7 Resolution |
|---|---|---|
| Total workflows | 49 | **49** (additions are steps/notes within existing) |
| Requirements fully covered | ~130 (99%) | **~130 (99%)** |
| Cross-workflow model issues | 0 claimed | **1 found → 0 remaining** |
| Business activities insufficiently covered | 0 claimed | **6 found → 0 remaining** |
| Cross-workflow integration gaps | 0 claimed | **3 found → 0 remaining** |

---

## A. Cross-Workflow Model Ambiguity

### A1. ✅ IC Inventory Ownership Model — W4 vs. W22 vs. W14 Contradiction

| Attribute | Detail |
|---|---|
| **Source** | W4 (Store Replenishment), W22 (Stock Transfers), W14 (Intercompany Transactions) |
| **Issue** | The corporate structure places DCs under **BuildRight Logistics, Inc.** and stores under **BuildRight Depot, Inc.** Every DC→Store replenishment (W4) is therefore an inter-entity transfer. However: |
| | **W22 system touchpoints** (added in Wave 6, gap J9) state: *"for transfers between legal entities (e.g., DC owned by Logistics Inc. → store owned by Depot Inc.), system automatically generates IC invoice at configured transfer price upon receipt confirmation."* |
| | **W14 Intercompany Flows** table lists *"DC warehousing fees: Depot Inc. → Logistics Inc. — Storage and distribution fees — Monthly"* — suggesting a monthly service-fee model, not per-transfer IC goods sales. |
| | **W4 (Store Replenishment)** handles ~5,000 orders/month — the highest-volume inter-location flow — but makes **no mention whatsoever of IC invoicing**, IC goods transfer, or entity-level inventory ownership. |
| | These three presentations are contradictory: either (a) goods are owned by Depot Inc. throughout and Logistics Inc. provides warehousing services billed monthly (W14 model), or (b) Logistics Inc. owns DC inventory and sells to Depot Inc. per replenishment (W22 model). The correct model determines whether W4 needs IC invoicing or not. |
| **Why This Matters** | This is the single highest-volume inter-entity flow (~5,000 transfers/month). ERP evaluators cannot assess IC automation capabilities without knowing the ownership model. The contradiction between W14 (monthly fee) and W22 (per-TO IC invoice) needs resolution. If the per-TO model applies, W4 must reference IC invoicing. If the monthly-fee model applies, W22's IC invoice note should be qualified to exclude standard DC→Store replenishment. |
| ✅ **Resolution Applied** | (1) **Clarify in the model company profile** which entity owns inventory in DCs. Recommended: Depot Inc. owns all merchandise; Logistics Inc. is a service company providing warehousing and distribution. This is the standard model in Philippine multi-entity retail. (2) **Update W22 system touchpoints** to clarify that the IC invoice trigger applies to inter-entity transfers of goods owned by the sending entity — which would NOT apply to standard W4 replenishment (Depot Inc.'s goods moving between its own inventory locations stored in Logistics Inc. facilities). (3) **Add note to W4** clarifying inventory ownership: Depot Inc. owns goods at both DC and store locations; Logistics Inc. provides warehousing services billed monthly per W14. (4) **Add note to W3** similarly clarifying that goods received into DCs are owned by Depot Inc. even though the facility belongs to Logistics Inc. |

---

## B. Business Activities Without Sufficient Workflow Coverage

### B1. ✅ Trade / Corporate Account Pricing at POS

| Attribute | Detail |
|---|---|
| **Source** | CRM-003 (Trade Account Management), CRM-004 (Corporate Account Management), profile §9.3 (Trade Price: 5–15% discount; Corporate/Project Price: Negotiated contract pricing) |
| **Gap** | Trade accounts (~5,200) and corporate accounts (~200) generate an estimated **40% of revenue** (30% trade + 10% corporate per profile §9.1). Yet no workflow describes how account-specific pricing is **applied at POS** when a trade/corporate customer makes a purchase. W8 covers the AR/credit side (invoice posting, credit check). W5b covers checkout mechanics. But the bridge — how the system identifies the customer's pricing tier and applies the correct price — is missing. |
| | Specifically: (a) How does the Cashier indicate a trade/corporate sale at POS? (b) How does the system apply the customer's negotiated pricing tier (5–15% off SRP for trade; contract price for corporate)? (c) How are trade/corporate price lists maintained in the system? (d) What happens when a trade customer buys items that have promotional pricing — does the trade discount stack with the promo? |
| **Why This Matters** | 40% of revenue flows through account-specific pricing. This is a core POS + pricing master data integration point. ERP evaluators need to understand: customer price list management, POS account identification, discount stacking rules, and approval workflows for off-contract pricing. |
| ✅ **Resolution Applied** | Add to W5b a sub-step (e.g., W5b.4c) for trade/corporate account checkout: (a) Cashier identifies customer via loyalty card, account card, or mobile number lookup; (b) system loads customer's pricing tier (trade discount %, corporate contract price list); (c) system applies account-specific pricing to scanned items — trade discount off SRP or corporate contract price per SKU; (d) if promo price is lower than account price, system applies lower price (customer-friendly) and alerts cashier; (e) if account has special terms (e.g., project-specific pricing), cashier selects applicable price list. Add system touchpoints for customer price list management, POS account lookup, and discount stacking rules. Cross-reference W40 for price list maintenance and W24 for account setup with pricing tier. |

### B2. ✅ Quantity Break Pricing Setup & Maintenance (POS-010)

| Attribute | Detail |
|---|---|
| **Req ID** | POS-010 (Quantity Break Pricing — Auto-tiered pricing at POS) |
| **Priority** | Must Have |
| **Gap** | W5b.6 says "System calculates totals: applies promos, quantity breaks, loyalty discounts" — but this is the only mention of quantity break pricing in all 49 workflows. No workflow describes how quantity break rules are **set up, approved, maintained, and reviewed**. W13 covers promotional pricing and W40 covers regular SRP changes, but quantity break pricing (e.g., "buy 10+ bags of cement, get 5% off per bag") is a distinct pricing mechanism that is neither a promotion nor an SRP change. |
| | Missing details: (a) Who creates quantity break rules? (b) What's the approval workflow? (c) How are rules assigned to categories or specific SKUs? (d) Are rules date-effective? (e) How do quantity breaks interact with promotional pricing and trade discounts? |
| **Why This Matters** | POS-010 is a Must Have requirement. Quantity break pricing is standard in hardware retail (contractors buy in bulk). The system must support configurable, date-effective, SKU-level quantity break rules with automatic POS application. Without a workflow, evaluators cannot assess configuration and governance capabilities. |
| ✅ **Resolution Applied** | Add to W40 (Regular Price Change Execution) or W13 (Promotions) a **Quantity Break Pricing** sub-section: (a) Pricing Analyst defines quantity break rules per SKU or category (threshold quantity, discount % or fixed price per tier); (b) Category Manager approves; (c) rules are date-effective with start/end dates; (d) system auto-applies at POS when quantity threshold is met, stacking rules defined (quantity break does not stack with promo — lower of the two applies); (e) monthly: Pricing Analyst reviews quantity break utilization and margin impact. Add system touchpoints for quantity break rule engine. |

### B3. ✅ Ecommerce IC Revenue Recognition & Settlement

| Attribute | Detail |
|---|---|
| **Source** | W11 (BOPIS), W19 (Home Delivery), W14 (Intercompany Transactions) |
| **Gap** | W14 lists two ecommerce-related IC flows: (1) *"Ecommerce fulfillment: Digital Commerce Inc. → Depot Inc. (BOPIS) or Logistics Inc. (delivery) — Fulfillment fees per order — Monthly"* and (2) *"Ecommerce payment collection: Digital Commerce Inc. → Depot Inc. — Remittance of in-store BOPIS revenue — Monthly."* However, neither W11 nor W19 references these IC flows. |
| | When a customer places a BOPIS order on buildright.com.ph (operated by Digital Commerce Inc.), pays online via PayMongo, and picks up at a Depot Inc. store: who recognizes the revenue? The payment is collected by Digital Commerce Inc., but the goods are fulfilled by Depot Inc. Similarly for home delivery: Digital Commerce Inc. collects payment, Logistics Inc. fulfills. |
| | W11 and W19 describe the operational flow but not the IC revenue settlement mechanics. This is critical for a 5-entity structure where ecommerce is a separate legal entity. |
| **Why This Matters** | With PHP 150M/month ecommerce GMV (growing to PHP 350M by Year 3), the IC settlement between Digital Commerce Inc., Depot Inc., and Logistics Inc. is material. ERP evaluators need to understand the revenue recognition split and IC settlement design. |
| ✅ **Resolution Applied** | Add IC settlement notes to W11 and W19 system touchpoints: for BOPIS (W11), revenue is recognized by Depot Inc. at pickup; Digital Commerce Inc. remits collected payments to Depot Inc. monthly per W14 (ecommerce payment collection IC flow); Digital Commerce Inc. charges Depot Inc. a fulfillment fee per order per W14 (ecommerce fulfillment IC flow). For home delivery (W19), revenue is recognized by Depot Inc. at delivery; Digital Commerce Inc. remits collected payments to Depot Inc.; Logistics Inc. charges Depot Inc. a fulfillment fee per order. All IC settlements processed monthly per W14. |

### B4. ✅ VMI Item Handling at POS — System Awareness

| Attribute | Detail |
|---|---|
| **Source** | W20 (VMI), W5b (In-Store Selling) |
| **Gap** | W20 step 8 says "At POS: system records sell-through event per VMI SKU; ownership transfers at point of sale." W20 step 6 describes the GL posting: "Dr. Cost of Goods Sold / Cr. Consignment Vendor Payable" — a fundamentally different GL treatment than a standard item sale (Dr. COGS / Cr. Inventory). W23 step 6 describes the same for consignment items. |
| | However, W5b (the POS selling workflow) makes no mention of VMI or consignment items requiring any special system handling at checkout. The Cashier "scans barcodes" (W5b.4) and the system "calculates totals" (W5b.6). But the system must know that a scanned item is VMI/consignment to trigger the different GL posting path. Without this being documented, evaluators don't know if POS handles VMI items transparently or requires cashier intervention. |
| **Why This Matters** | VMI and consignment items (~300 VMI SKUs + ~500–1,000 consignment SKUs) require fundamentally different GL treatment at POS. The system must differentiate them from standard items without cashier intervention. This is a POS-to-GL integration design point. |
| ✅ **Resolution Applied** | Add a note to W5b system touchpoints: system automatically identifies VMI and consignment items at POS via item master flags (no cashier intervention needed); at scan, system routes the transaction line to the appropriate GL posting path — standard items post Dr. COGS / Cr. Inventory; VMI items post Dr. COGS / Cr. VMI Vendor Payable; consignment items post Dr. COGS / Cr. Consignment Vendor Payable. Cashier experience is identical regardless of item ownership type. |

### B5. ✅ ROP / EOQ Parameter Governance

| Attribute | Detail |
|---|---|
| **Source** | W2a (Auto-Replenishment), W31 (Demand Forecasting) |
| **Gap** | W2a step 1 says "System calculates ROP breaches based on: avg daily demand × lead time + safety stock." W31 step 8 added safety stock review as part of quarterly model recalibration. But no workflow describes the governance of the **other ROP parameters**: |
| | (a) **Lead time per vendor-SKU**: Who enters and maintains vendor lead times? How often are they reviewed against actual performance? (b) **Demand averaging period**: How many weeks of historical sales are used for avg daily demand? Who configures this? (c) **Service level targets**: What service level drives safety stock calculations? Is it uniform or differentiated by ABC class? (d) **Order multiple / pallet quantities**: Who maintains order multiples per vendor-SKU? |
| | With 35,000 active SKUs, these parameters number in the hundreds of thousands. Stale parameters lead to overstocking or stockouts. |
| **Why This Matters** | ROP parameter accuracy directly drives inventory investment and fill rate. ERP evaluators need to understand parameter governance to assess the system's ability to support parameter maintenance, auto-tuning, and exception reporting. |
| ✅ **Resolution Applied** | Expand W31 step 8 to include full parameter governance review: quarterly, Demand Planner and Supply Planner review (a) lead time accuracy per vendor (actual vs. system) and update system lead times for vendors with > 20% variance; (b) demand averaging period appropriateness by SKU volatility class; (c) service level targets by ABC class (A-items: 98%, B-items: 95%, C-items: 90% or as configured); (d) order multiple accuracy. Add system touchpoints for parameter accuracy reporting (lead time variance report, ROP exception report). Cross-reference W44 (vendor performance — lead time variance feeds vendor scorecard). |

### B6. ✅ Loyalty Points Earning on Ecommerce Orders

| Attribute | Detail |
|---|---|
| **Source** | CRM-001 (Loyalty Points Engine), W17 (Loyalty Operations), W11 (BOPIS), W19 (Home Delivery) |
| **Gap** | W17 steps 3–4 describe points earning at POS: "At each POS transaction, cashier scans loyalty card or enters mobile number. System calculates points earned." But the 42,900 ecommerce orders/month (~PHP 150M GMV) also earn points. No workflow step describes how points are earned for online transactions. |
| | The customer journey is: customer places order online → pays online → order fulfilled. When does the system calculate and award loyalty points? At order placement? At fulfillment/delivery? At pickup (BOPIS)? The W17 workflow only describes in-store earning. |
| | Additionally: how does the customer identify their loyalty account online? Profile §8.1 says "Optional registration; guest checkout available." Registered customers would link their account, but guest checkout customers wouldn't earn points. |
| **Why This Matters** | Ecommerce is 2.9% of revenue growing to 7% by Year 3. Points earning must work across channels. With PFRS 15 deferred revenue accounting (W17.4), the system must allocate transaction revenue at the point of earning regardless of channel. ERP evaluators need to understand omnichannel loyalty integration. |
| ✅ **Resolution Applied** | Expand W17 step 4 with a note on ecommerce points earning: for online orders, system awards points when order is fulfilled (delivered for home delivery, picked up for BOPIS), not at order placement, because revenue recognition occurs at fulfillment. Customer identifies loyalty account at online checkout via registered account; guest checkout customers do not earn points. System calculates points using the same earn rate (1 point per PHP 100). Points allocation for deferred revenue (PFRS 15) follows same logic as in-store. Add system touchpoint for ecommerce-to-loyalty integration: order fulfillment event triggers points earning via customer account linkage. |

---

## C. Cross-Workflow Integration Gaps

### C1. ✅ RTV Physical Logistics & Tracking

| Attribute | Detail |
|---|---|
| **Source** | W3.6a–b (receiving damage RTV), W6.8a (in-store damage RTV), W12a.8 (defective returns RTV), W23.10 (consignment returns), W33.6–7 (warranty claim RTV) |
| **Gap** | At least five workflows initiate RTVs, and W3.6b says "Buyer reviews RTV request; coordinates with vendor for credit note or replacement shipment." But no workflow describes the **physical logistics** of returning goods to the vendor: |
| | (a) How are RTV items packed and shipped? (b) Who selects the carrier? (c) How are RTV shipments tracked? (d) When does the vendor confirm receipt? (e) When is the credit note triggered — at shipment or at vendor receipt? (f) What happens if the vendor disputes the RTV? |
| | For DC-initiated RTVs, goods need to move from DC back to vendor (reverse logistics). For store-initiated RTVs, goods need to move from store to vendor (or store → DC → vendor). The physical flow and system tracking are absent. |
| **Why This Matters** | RTVs are a regular occurrence (damage from ~6,000 DC receipts/month + ~600 DSD receipts/month + in-store damage + warranty claims + consignment returns). Without RTV logistics documentation, evaluators can't assess reverse logistics tracking, RTV shipment lifecycle management, or credit note timing. |
| ✅ **Resolution Applied** | Add RTV physical logistics to W3 system touchpoints: (a) for DC RTVs, Receiving Clerk stages RTV items in designated RTV area; system creates RTV shipment record; DC dispatch arranges carrier pickup or vendor pickup per agreement; (b) for store RTVs, Stock Associate stages items in backroom; system creates RTV shipment record; Buyer coordinates with vendor for pickup or ships to DC for consolidation; (c) system tracks RTV shipment lifecycle: Initiated → Shipped → In Transit → Vendor Received → Credit Note Issued → Settled; (d) vendor credit note triggered upon vendor confirmation of receipt; if vendor disputes, Buyer negotiates resolution per W3.6b; (e) system maintains RTV tracking dashboard with aging by status. |

### C2. ✅ Gift Card Online Redemption & IC Settlement

| Attribute | Detail |
|---|---|
| **Source** | W28 (Gift Card & Store Credit), POS-015 (Gift Card / Store Credit), W14 (Intercompany) |
| **Gap** | W28 covers gift card sale, activation, and redemption at POS (in-store). W28.7 mentions reload "at POS or online." But W28 does not describe: |
| | (a) Can gift cards be redeemed online on the ecommerce platform? (b) If a customer buys a gift card in-store (Depot Inc.) and redeems it online (Digital Commerce Inc.), how is the IC settlement handled? The liability was created in Depot Inc.'s books, but the revenue would be recognized by Digital Commerce Inc. (or Depot Inc. if revenue recognition follows the fulfillment entity). (c) How does the ecommerce platform validate gift card balance and process redemption in real-time against the ERP gift card liability? |
| **Why This Matters** | Gift cards are a cross-channel instrument. With ~8,000–12,000 active cards/month and omnichannel retail, customers expect to buy in-store and redeem online (and vice versa). The IC settlement dimension is specific to the 5-entity structure. |
| ✅ **Resolution Applied** | Expand W28 with online redemption notes: (a) gift cards can be redeemed online and in-store; (b) system validates card balance in real-time via ERP integration; (c) for IC settlement: gift card liability is maintained centrally by Depot Inc.; when redeemed online, Digital Commerce Inc. fulfills the order but Depot Inc. reduces the gift card liability and recognizes revenue (or settlement is processed monthly per W14); (d) gift card liability remains on Depot Inc.'s balance sheet regardless of redemption channel. Add system touchpoints for cross-channel gift card validation and IC settlement. |

### C3. ✅ Store Occupancy Cost Allocation for Store P&L

| Attribute | Detail |
|---|---|
| **Source** | W35.10 (Store P&L reporting), W14 (Intercompany — store rent), profile §9.4 |
| **Gap** | W35.10 lists the store P&L components: "revenue, COGS, gross margin, labor cost, occupancy, shrinkage, EBITDA per store." But no workflow describes how **occupancy cost** (the largest fixed cost after labor) is allocated per store: |
| | (a) Store rent is an IC payment from Depot Inc. to Property Mgmt Inc. (W14). Is each store's rent a direct charge (easy) or allocated from a consolidated lease cost pool? (b) DC warehousing and distribution costs (IC payment to Logistics Inc.) — are these allocated to stores? If so, how — by sales volume, by replenishment orders, by weight? (c) How are utility costs allocated per store (direct meter vs. estimated)? (d) Corporate overhead allocation from Holdings Inc. — is this included in store P&L or shown separately? |
| **Why This Matters** | Store P&L accuracy depends on correct cost allocation. The occupancy line item is the difference between gross margin and EBITDA. If the system can't automate occupancy allocation, store profitability reporting requires manual spreadsheets — defeating a core ERP value proposition. ERP evaluators need to understand the allocation methodology. |
| ✅ **Resolution Applied** | Add occupancy cost allocation notes to W35 system touchpoints: (a) store rent is a direct charge per location based on individual lease agreements with Property Mgmt Inc. (not allocated); (b) DC warehousing and distribution costs are allocated to stores monthly based on a configurable allocation key (recommended: proportional to replenishment order value or volume); (c) utility costs are direct charges per store (each location has its own meter/account); (d) corporate overhead is shown as a separate line below store EBITDA, not embedded in store P&L. Add system touchpoints for configurable cost allocation rules and automatic store P&L generation. |

---

## D. Detail Gaps in Existing Workflows

### D1. ✅ Ecommerce VAT Handling & BIR Compliance

| Attribute | Detail |
|---|---|
| **Source** | FIN-006 (Philippine VAT 12%), W9a.16 (VAT return), W11 (BOPIS), W19 (Home Delivery) |
| **Gap** | W9a.16 describes VAT return preparation (BIR 2550M). W5b covers in-store VAT implicitly (POS calculates totals). But no workflow describes VAT handling for ecommerce transactions: |
| | (a) Are BOPIS and home delivery transactions subject to the same 12% VAT as in-store? (Yes, under Philippine tax law.) (b) Which entity remits the output VAT — Depot Inc. (fulfillment entity) or Digital Commerce Inc. (collection entity)? (c) How are input VAT and output VAT tracked for ecommerce transactions? (d) How are ecommerce VAT-exempt items (if any) handled? (e) Does the system generate separate VAT reports for ecommerce vs. in-store for BIR audit purposes? |
| **Why This Matters** | BIR requires accurate VAT reporting per entity. With PHP 150M+ monthly ecommerce GMV across multiple entities and payment gateways, VAT tracking must be precise. The multi-entity structure adds complexity: output VAT must be recognized by the correct entity. This is low priority because the VAT rate is the same (12%) regardless of channel, but the entity-level reporting dimension matters. |
| ✅ **Resolution Applied** | Add VAT handling note to W11 and W19 system touchpoints: (a) ecommerce transactions are subject to 12% VAT identical to in-store; (b) output VAT is recognized by Depot Inc. (the entity that recognizes revenue per the IC model); Digital Commerce Inc. does not recognize VAT on payment collection (it remits to Depot Inc.); (c) system tracks input VAT and output VAT per entity; (d) VAT on ecommerce transactions is included in the same BIR 2550M filing per entity. Note: this follows from the IC model clarification in A1 — if Depot Inc. recognizes revenue, Depot Inc. recognizes the output VAT. |

---

## E. Recommendations Priority Matrix

| Priority | Gap ID | Action | Status |
|---|---|---|---|
| 🔴 **P1** | A1 (IC ownership model) | Clarify inventory ownership; reconcile W4, W14, W22 | ✅ Resolved |
| 🔴 **P1** | B1 (Trade pricing at POS) | Add account-specific pricing step to W5b | ✅ Resolved |
| 🔴 **P1** | B2 (Quantity break pricing) | Add quantity break sub-section to W40/W13 | ✅ Resolved |
| 🟡 **P2** | B3 (Ecommerce IC settlement) | Add IC notes to W11 and W19 | ✅ Resolved |
| 🟡 **P2** | B4 (VMI at POS) | Add VMI/consignment POS handling note to W5b | ✅ Resolved |
| 🟡 **P2** | B5 (ROP parameters) | Expand W31 step 8 with full parameter governance | ✅ Resolved |
| 🟡 **P2** | B6 (Loyalty on ecommerce) | Add ecommerce points earning to W17 | ✅ Resolved |
| 🟢 **P3** | C1 (RTV logistics) | Add RTV physical logistics to W3 touchpoints | ✅ Resolved |
| 🟢 **P3** | C2 (Gift card online) | Add online redemption and IC notes to W28 | ✅ Resolved |
| 🟢 **P3** | C3 (Store cost allocation) | Add occupancy allocation to W35 touchpoints | ✅ Resolved |
| 🟢 **P3** | D1 (Ecommerce VAT) | Add VAT note to W11/W19 | ✅ Resolved |

---

## F. Cross-Document Consistency Check

All numerical checks from Waves 1–6 re-verified. No new numerical inconsistencies found.

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
| **NEW: W22 IC note vs. W14 IC model** | ⚠️ **Contradiction identified (gap A1)** |
| Customer segments: profile §9.1 (55+30+10+5 = 100%) | ✅ Sums to 100% |

---

## G. What Changed vs. Previous Waves

Previous waves focused on **coverage completeness** (does every requirement have a supporting
workflow?), **accounting depth** (GL postings, accruals, PFRS compliance), **operational
edge cases** (reverse logistics, cash-in-transit, theft write-off), and **numerical
accuracy** (W19 staffing error, revenue split).

Wave 7 shifts focus to **cross-workflow integration and model clarity**:

1. **IC model ambiguity** (A1): Previous waves added IC references individually to W22
   (Wave 6) and W14 (Wave 3) without reconciling the underlying inventory ownership model.
   This created a contradiction that Wave 7 identifies.

2. **Pricing mechanics gaps** (B1, B2): Previous waves thoroughly covered promotional
   pricing (W13), regular SRP changes (W40), and price overrides (W5b.4a). But they missed
   two pricing mechanisms: account-specific pricing (40% of revenue) and quantity break
   pricing (a Must Have requirement).

3. **Cross-channel gaps** (B6, C2): Previous waves ensured both in-store and ecommerce
   workflows existed but didn't verify that shared capabilities (loyalty, gift cards)
   worked seamlessly across channels with correct IC settlement.

4. **Parameter governance** (B5): Previous waves covered the outputs of automated systems
   (PO suggestions, replenishment orders) but not the governance of the input parameters
   that drive those outputs.

This pattern — Waves 1–6 addressed structural coverage and depth, Wave 7 addresses
cross-workflow integration and model-level clarity — confirms that the workflow
documentation has reached a high level of maturity. The remaining gaps are narrower
and more architectural than operational.

---

## H. Overall Assessment

**The workflow documentation is comprehensive and fully ready for ERP vendor evaluation.**

The most impactful gap is the IC inventory ownership model ambiguity (A1), which affects
how the highest-volume inter-entity flow (DC→Store replenishment, ~5,000 orders/month) is
represented in the system. Resolving this single gap clarifies the architecture for W3, W4,
W14, and W22 simultaneously.

The trade/corporate pricing gap (B1) is the most commercially significant: 40% of revenue
flows through account-specific pricing that has no operational workflow description.

All 11 gaps can be resolved through targeted additions to existing workflows — no new
workflows are needed.

| Metric | v9.0 (Pre-Wave 7) | v10.0 (After Wave 7) |
|---|---|---|
| Total workflows | 49 | **49** |
| Requirements fully covered | ~130 (99%) | **~130 (99%)** |
| Cross-workflow model issues | 0 known | **0** |
| Total gaps resolved (all waves) | 62 | **73** (62 + 11) |
| Non-blocking carried forward | 2 | 2 |

---

## I. Non-Blocking Items (Acknowledged)

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

*Document Version: 1.1 | Date: 2026-05-30 | Wave 7: 11 gaps identified (3 HIGH, 4 MEDIUM, 4 LOW); all 11 resolved*
