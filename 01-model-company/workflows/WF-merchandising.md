# Merchandising & Pricing Workflows

> Assortment planning, promotions, pricing, product lifecycle, PIM, vendor rebate management, markdown & clearance pricing, sample & demo inventory management, category performance review & P&L ownership, pricing hierarchy governance, private label development, competitor intelligence, store-level price tag printing & verification, store promotional setup & visual merchandising, and seasonal merchandise transition & display rotation.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W1. Merchandise Planning & Assortment Review](#merchandise-planning-assortment-review)
- [W13. Promotions & Pricing Execution](#promotions-pricing-execution)
- [W27. Vendor Rebate Accrual & Settlement](#vendor-rebate-accrual-settlement)
- [W40. Regular Price Change Execution](#regular-price-change-execution)
- [W50. Product Information Management (PIM)](#product-information-management-pim)
- [W63. Shelf Label & Price Tag Distribution](#shelf-label-price-tag-distribution)
- [W64. New Product Pilot / Store Test](#new-product-pilot-store-test)
- [W68. Product Lifecycle & Discontinuation](#product-lifecycle-discontinuation)
- [W93. Markdown & Clearance Pricing Execution](#markdown-clearance-pricing-execution)
- [W97. Sample & Demo Inventory Management](#sample-demo-inventory-management)
- [W102. Category Performance Review & P&L Ownership](#category-performance-review-pl-ownership)
- [W107. Pricing Hierarchy Governance & Compliance Audit](#pricing-hierarchy-governance-compliance-audit)
- [W129. Private Label / In-house Brand Development](#private-label-in-house-brand-development)
- [W130. Competitor Price Intelligence Gathering](#competitor-price-intelligence-gathering)
- [W181. Store-Level Price Tag Printing & Verification](#store-level-price-tag-printing--verification)
- [W262. Store Promotional Setup & Visual Merchandising Execution](#store-promotional-setup--visual-merchandising-execution)
- [W264. Seasonal Merchandise Transition & Display Rotation](#seasonal-merchandise-transition--display-rotation)

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
- Slow-mover / dead stock operational review: monthly cross-functional review where Category Managers, Supply Planner, and Cost Accountant examine the slow-mover report (system-generated: items with > 90 days since last sale, < 2 turns/year, or current stock > 6 months forward demand); disposition decided per SKU — continue selling (monitor), markdown and clearance (W13.9a), RTV (W3.6a), bulk liquidation (W13.9b), donation, or scrap; results feed into quarterly assortment review (W1) for potential discontinuation; accounting consequences (NRV write-down) processed per W9A.16b
- Competitive intelligence monitoring: as part of the quarterly assortment review cycle, Category Managers review competitive landscape per category — (a) new competitor store openings or closures within BuildRight trade areas (sourced from Store Manager reports and publicly available data), (b) competitor promotional events and pricing actions (sourced from Sales Associate and Pricing Analyst field observations, competitor websites/flyers), (c) new competitor product introductions in overlapping categories; findings documented per category and inform SKU add/drop decisions (W1.4), pricing adjustments (W40), and promotional planning (W13); Store Managers report competitive activity in their monthly performance review (W67); competitive intelligence is not a separate system module but is embedded in the W1 quarterly cycle with data sourced from operational channels


### Staffing Implication
5 Category Managers each handling ~2 categories per quarterly cycle = manageable at ~18 hours/category. The 3 Pricing Analysts handle data pulls and analysis in parallel. 10–12 Buyers handle vendor validation. Current team of ~40 in Merchandising is adequate.

> **Buyer staffing note**: At 800–1,000 active vendors ÷ 10–12 buyers = ~67–100 vendors per buyer, which is above the industry average of 30–50. This lean buying model is viable because (a) ~70% of vendors are replenished via auto-generated POs (W2A), reducing daily buyer intervention; (b) top 20 vendors (45% of COGS) are on blanket contracts (W2C) requiring less transactional management; and (c) VMI vendors (12) are largely self-managing. However, during seasonal planning cycles (W32), the team may be stretched. Consider expanding to 15–17 buyers if vendor management quality suffers.

---



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
| 18 | Discount stacking rules: if a promotional price (W13) is lower than the quantity break price, system applies the promo price (customer-friendly) and does not stack discounts; if quantity break price is lower, it applies; trade/corporate account pricing (W5B.4c) and quantity break pricing do not stack — the lower of the two applies | System | — | Automated |
| 18a | **Loyalty points on discounted transactions**: loyalty points (W17) are earned on the final amount paid by the customer (after all discounts — promotional, quantity break, trade account, price match) but before VAT; this means quantity break discounts reduce the points earned proportionally; PFRS 15 deferred revenue allocation (W17.4) is calculated on the net revenue after all discounts | System | — | Automated |
| 19 | Monthly: Pricing Analyst reviews quantity break utilization report: frequency of tier triggers by SKU, margin impact, average quantity per transaction for items with quantity breaks, and whether thresholds are driving incremental volume | Pricing Analyst | Category Manager | 1 hour/month |

### System Touchpoints
- Quantity break rule engine: configurable per SKU or category with multiple tiers, date-effective, threshold quantity, and discount method (% off SRP or fixed price) (W40.15)
- Automatic POS application when scanned quantity meets threshold — no cashier action needed (W40.17)
- Discount stacking rules: quantity breaks do not stack with promotional pricing or trade/corporate pricing — lower price wins (W40.18)
- Loyalty points on quantity break transactions: points earned on net discounted amount (after all discounts, before VAT); PFRS 15 deferred revenue allocation calculated on net revenue (W40.18a, W17.4)
- Quantity break utilization reporting: tier trigger frequency, margin impact, incremental volume analysis (W40.19)
- Integration with W5B.6 (system applies quantity breaks during total calculation) and W40.5 (approval workflow)

---



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
| 8 | For electronic shelf labels (ESL) — if deployed at select stores: system pushes price changes to ESL devices overnight; Dept. Supervisor verifies ESL display matches system price during opening walkthrough (W5A step 2); no physical label handling required | System / Dept. Supervisor | Store Manager | Automated + 5 min verification |

### System Touchpoints
- Automated shelf label print file generation from approved price changes with store/location assignment (W63.1)
- Centralized or store-level label printing with barcode, description, and SRP (W63.2)
- Label shipment tracking if centralized (W63.3)
- Label verification via RF gun barcode scan against system price (W63.6)
- Electronic shelf label (ESL) integration for stores with ESL hardware (W63.8)
- Catch-weight / variable measure item shelf labels: for items sold by weight, length, or board foot (lumber, wire, bulk nails), shelf labels display unit pricing (e.g., "PHP 85.00 per board foot", "PHP 45.00 per linear meter", "PHP 350.00 per kilogram") rather than a fixed SRP; label includes the unit of measure, unit price, and a note "Price varies by actual measure"; system generates catch-weight labels from item master pricing per unit of measure; at POS (W5B.2), Sales Associate measures/weighs actual quantity and system calculates price = unit price × actual quantity; integration with W5B (POS catch-weight selling) and W40 (price changes — unit price updates reflected on catch-weight labels)
- Integration with W5A (opening — label application done before opening), W13 (promo labels), W40 (regular price changes)

### Staffing Implication
- **Stock Associates**: label application adds ~30–60 min per price change batch. With ~2–3 batches/week, this is ~1–3 hours/week. Absorbed within existing Stock Associate duties (3 per store), typically done during early morning before store opens.
- **Pricing Analyst**: print file generation adds ~15 min/batch. Absorbed.
- For centralized printing: 1 Stock Associate at HQ handles packaging and shipping. Absorbed.

---



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
| 2 | Buyer validates discontinuation impact per SKU: (a) remaining open POs — can they be cancelled or reduced?, (b) outstanding vendor commitments on blanket POs (W2C) — minimum commitment status, (c) active rebate agreements (W27) — impact on rebate tier achievement, (d) vendor relationship impact — is vendor sole-source for other SKUs? | Buyer | Category Manager | 3 hours/campaign |
| 3 | VP Merchandising approves discontinuation list; system sets "Discontinued — Pending" status on approved SKUs | VP Merchandising | VP Merchandising | 30 min/campaign |
| 4 | **Last buy decision**: for each discontinued SKU, Buyer determines: (a) cancel all open POs (standard action) or (b) place final buy order to cover estimated sell-through during clearance period if remaining stock is critically low and sufficient margin exists; final buy follows standard W2A PO process but flagged as "Last Buy" — no future auto-replenishment | Buyer | Category Manager | 1 hour/campaign |
| 5 | Supply Planner disables auto-replenishment (ROP) for discontinued SKUs; system stops generating suggested POs; remaining store replenishment continues until DC stock is exhausted; system auto-cancels all open backorders (W56) for discontinued SKUs across all stores; customers with cancelled backorders notified via SMS/email with apology and option to select a substitute item (directed to Sales Associate or CSR for assistance) | Supply Planner | Supply Planning Manager | 30 min/campaign |
| 6 | Merchandise Planner flags SKU as "Discontinued" in item master with effective date; item hidden from planogram tools and new store assortment assignments (W16.5); item remains visible in POS and ecommerce for selling remaining stock | Merchandise Planner | Category Manager | 1 hour/campaign |
| 7 | **Clearance execution**: Pricing Analyst sets clearance markdown per W13.9a — system applies clearance price at POS and ecommerce; POS displays clearance disclaimer; Dept. Supervisors move items to clearance section; clearance period typically 4–6 weeks (longer than promo clearance per W13.9a to allow complete sell-through) | Pricing Analyst / Dept. Supervisor | Category Manager | 2 hours/campaign |
| 7a | **Pricing conflict during discontinuation clearance**: if a regular price increase (W40) occurs while an item is in discontinuation clearance, the clearance price is NOT recalculated from the new regular price — the clearance price remains fixed at its originally set level (typically a percentage below the pre-clearance regular price) until the clearance period ends; if a regular price decrease (W40) occurs during clearance and the new regular price falls below the clearance price, system alerts Pricing Analyst, who must either lower the clearance price below the new regular price or accelerate the item's disposition to post-clearance (W68.9); this rule extends the W13 pricing conflict resolution logic to the discontinuation context — clearance price overrides regular price during the clearance period, and clearance items are excluded from standard price change batches (W63)
| 8 | **Weekly sell-through monitoring**: Pricing Analyst reviews discontinued SKU sell-through dashboard; if sell-through rate < 20% of remaining stock after 3 weeks, escalates to Category Manager for deeper markdown or accelerated disposition | Pricing Analyst | Category Manager | 30 min/week during clearance |
| 9 | **Post-clearance disposition**: at end of clearance period, remaining stock dispositioned per priority: (a) Return to Vendor (RTV) — Buyer coordinates per W3.6a, negotiate credit note; (b) bulk liquidation to discount buyers — Buyer arranges sale; (c) donation to partner organizations (Habitat for Humanity, local community organizations); (d) scrap/recycle — DC Supervisor authorizes per W3.6c; system removes remaining inventory and posts final loss | Buyer / DC Supervisor | Category Manager | 2 hours/campaign |
| 10 | **Vendor settlement**: AP Clerk processes any vendor credit memos from RTV per W7.9b; Buyer confirms vendor agreement termination or continued relationship on other SKUs; system releases any remaining blanket PO commitments per W2C | AP Clerk / Buyer | AP Supervisor | 1 hour/campaign |
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



## W93. Markdown & Clearance Pricing Execution

| Field | Detail |
|---|---|
| **Trigger** | Seasonal end-of-cycle clearance; slow-moving inventory identified by W85 (margin analysis) or W1 (assortment review); damaged-but-saleable items from W91; overstock identified by W6 (cycle count) or W31 (demand planning); or product discontinuation (W68) |
| **Frequency** | Ongoing (as items are identified); seasonal clearance events ~4–6/year |
| **Volume** | ~500–2,000 SKUs per seasonal clearance event; ~50–200 ad-hoc markdowns/month |
| **Owner** | Pricing Analyst |
| **Participants** | Pricing Analyst, Category Manager, Cost Accountant, Store Manager, VP Merchandising |

### Background

Markdowns and clearance pricing are distinct from promotional pricing (W13) and product discontinuation (W68). W13 creates temporary price reductions to drive traffic and volume with planned recovery at end of promo. W68 manages the exit of a product from the assortment entirely. Markdowns are permanent price reductions on specific inventory lots to accelerate sell-through of slow-moving, seasonal, or damaged-but-saleable items. Without a dedicated workflow, markdowns are applied inconsistently, margin impact is not tracked, and clearance inventory lingers on shelves consuming valuable retail space. This workflow supports FIN-011 (inventory aging), INV-010 (catch-weight), and W85 (margin analysis).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Markdown candidate identification**: Sources of markdown candidates: (a) **Seasonal clearance**: end-of-season items identified per seasonal calendar (Christmas décor after Dec, flood control after rainy season); (b) **Slow-movers**: SKUs with inventory aging > 90 days and < 2 units sold/month flagged by system from W85 monthly margin report; (c) **Damaged-but-saleable**: items with cosmetic damage but functional per W91 disposition decision (dented cans, box-damaged appliances, scratched tiles); (d) **Overstock**: locations with > 12 weeks of supply vs. forecast per W31; (e) **Near-expiry**: date-sensitive items within 30% of shelf life per W6 near-expiry alerting | Category Manager / Pricing Analyst / System | VP Merchandising | 2 hours/clearance event; ongoing for ad-hoc |
| 2 | **Markdown pricing calculation**: Pricing Analyst calculates markdown price for each candidate SKU: (a) current SRP, (b) current WAC (from inventory valuation), (c) minimum acceptable price (WAC + minimum margin % — configurable per category, typically 0–10% above cost; for clearance, may go below cost with approval), (d) recommended markdown price based on: markdown percentage tiers (25%, 33%, 50%, 75% off SRP), aging velocity (slower movers get deeper markdown), quantity on hand, and weeks of supply; (e) estimated total markdown loss (markdown amount × quantity); (f) estimated recovery value (markdown price × expected sell-through %) | Pricing Analyst | Category Manager | 5 min/SKU |
| 3 | **Authorization** (tiered by markdown value): (a) **≤ PHP 50,000 total markdown loss per SKU**: Category Manager approves; (b) **> PHP 50,000 and ≤ PHP 500,000 total markdown loss**: VP Merchandising approves; (c) **> PHP 500,000 total markdown loss**: CFO approves; (d) **Below-cost markdown**: CFO approval required regardless of amount (loss recognition trigger) | Per tier above | VP Merchandising / CFO | 5–15 min/approval |
| 4 | **Markdown execution in system**: (a) Pricing Analyst enters markdown in system with: effective date, markdown price, markdown reason code (seasonal, slow-mover, damaged, overstock, near-expiry), and authorization reference; (b) system updates price in POS (W5B) and ecommerce (W11/W19) — regular SRP preserved as reference; markdown price displayed as "Now" or "Clearance" on shelf label (W63); (c) system posts GL entry: Dr. Markdown Expense (or Dr. COGS-Clearance) / Cr. Inventory — at markdown amount per unit × quantity on hand (if below WAC, recognize loss immediately; if above WAC, no immediate GL impact — margin reduction recognized at sale) | Pricing Analyst / System | Cost Accountant | 3 min/SKU |
| 5 | **Shelf label and display update**: (a) System generates clearance shelf labels per W63 with clearance pricing and distinctive visual treatment (e.g., yellow/orange tag); (b) Stock Associate replaces shelf labels at store; (c) for damaged-but-saleable items: Stock Associate moves to designated clearance rack or area with appropriate signage; (d) ecommerce catalog updated with clearance badge and price per W50 | System / Stock Associate | Store Manager | 30 min/store/event |
| 6 | **Sell-through monitoring**: (a) System tracks markdown sell-through daily: markdown price × units sold = recovery; remaining markdown inventory × markdown price = remaining recovery; (b) **Escalation tiers**: if < 30% sell-through after 2 weeks: Category Manager reviews — consider deeper markdown; if < 50% sell-through after 4 weeks: Pricing Analyst applies second markdown (additional 25% off) with Level 2 re-authorization; if < 30% sell-through after 6 weeks: proceed to final disposition per W68.9 (RTV, donation, scrap) | Pricing Analyst / Category Manager | VP Merchandising | 30 min/week during clearance |
| 7 | **Post-clearance analysis**: After clearance period: Pricing Analyst prepares clearance performance report per event: (a) original markdown value vs. actual recovery, (b) sell-through %, (c) days to clear, (d) margin impact by category, (e) lessons learned (markdown timing, depth, vendor quality issues); feeds into W85 annual margin strategy and W1 assortment decisions | Pricing Analyst | VP Merchandising | 1 hour/event |

### Pricing Conflict Rules
- Markdown price vs. promotional price: if an item is on both markdown (W93) and promotion (W13), system applies the **lower** of the two prices at POS (customer-friendly); if the promotional price is higher than markdown, system ignores the promotion
- Markdown price vs. employee discount: employee discount (W5B.12) does **not** stack on top of markdown; the lower of employee discount price or markdown price applies
- Markdown price vs. loyalty points: loyalty points earned on markdown sales calculated on markdown price (not original SRP)
- Markdown price vs. competitor price match (W61): markdown price is the effective SRP for price match comparison

### System Touchpoints
- Markdown candidate identification: aging analysis, slow-mover flagging, seasonal calendar integration (W93.1)
- Markdown pricing calculator: WAC floor, markdown % tiers, recovery estimation (W93.2)
- Tiered authorization workflow with amount-based routing (W93.3)
- Markdown price execution: POS and ecommerce price update with original SRP reference preserved (W93.4)
- Clearance shelf label generation per W63 (W93.5)
- Markdown sell-through dashboard with velocity tracking and escalation triggers (W93.6)
- Post-clearance performance analysis with recovery and margin impact reporting (W93.7)
- Pricing conflict rules engine: markdown vs. promo vs. employee discount vs. price match (W93 pricing conflicts)
- Integration with W1 (assortment — slow-mover exit), W13 (promotions — pricing conflict rules), W31 (demand — overstock identification), W40 (price changes — markdown as a permanent price change), W50 (PIM — ecommerce catalog clearance), W63 (shelf labels — clearance tags), W68 (discontinuation — clearance as part of exit), W85 (margin analysis — markdown as margin recovery strategy), W91 (damaged goods — markdown disposition)

### Staffing Implication
- **Pricing Analysts**: add ~4 hours/seasonal clearance event (3 analysts) + ~2 hours/month ad-hoc markdowns. With 4–6 seasonal events/year, this is ~20–30 hours/year incremental. Absorbed.
- **Store Associates**: clearance re-labeling adds ~30 min/store/event × 4–6 events = ~2–3 hours/store/year. Absorbed.
- **No incremental headcount.**

---



## W97. Sample & Demo Inventory Management

| Field | Detail |
|---|---|
| **Trigger** | New product introduction requiring display samples; category reset (W1) requiring demo units; vendor-supplied display items; or existing samples needing replacement |
| **Frequency** | ~50–100 new samples/demos per month across all stores; seasonal resets ~2/year |
| **Volume** | ~3,000–5,000 sample/demo units across 200 stores at any time |
| **Owner** | Category Manager |
| **Participants** | Category Manager, Store Manager, Stock Associate, Cost Accountant, Buyer, Visual Merchandiser |

### Background

In big-box home improvement retail, physical product samples and demo units are critical sales tools — tile and flooring swatches, paint color chips, tool demonstration units, appliance display models, fixture showrooms, and material sample boards. These items are inventory (they have cost) but are not for sale to customers. Without proper tracking, samples become unaccounted inventory, are accidentally sold (POS scan conflict), are not replaced when worn, or remain on the books after disposal. This workflow manages the lifecycle of non-sellable sample and demo inventory from procurement to disposal.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Sample/demo request**: (a) Category Manager identifies need for sample/demo: new SKU introduction (W64), category reset (W1), vendor product launch, or replacement of worn/damaged existing sample; (b) creates sample/demo request specifying: SKU(s), quantity per store (may vary by store format/size), purpose (display, demo, color swatch, showroom model), expected useful life (3–12 months depending on item type) | Category Manager | VP Merchandising | 15 min/request |
| 2 | **Procurement**: (a) **From existing inventory**: Buyer approves conversion of regular stock items to sample/demo status; system transfers items from saleable inventory to sample/demo inventory (not deducted from available-to-promise); (b) **From vendor**: Buyer orders samples from vendor — may be free-of-charge (vendor-funded display), at cost, or at special sample pricing; received at DC per W3 with "Sample" receipt type; (c) **Custom fabricated**: Visual Merchandiser designs custom display boards or sample kits; procured as non-stock items per W38 | Buyer / Visual Merchandiser | Category Manager | Per W2/W38 |
| 3 | **Inventory classification**: System classifies sample/demo items with: (a) inventory status = "Sample/Demo" (blocked from POS sale, blocked from replenishment calculation, excluded from ATP, excluded from cycle count of saleable inventory — but included in total inventory valuation for GL purposes); (b) assigned to specific store location; (c) cost center = store-level merchandising display cost; (d) useful life start date; (e) expected replacement date | System | Category Manager | Automated |
| 4 | **Distribution to stores**: (a) DC picks and ships sample/demo items to stores per standard W4 replenishment (but with "Sample" designation — not counted against store replenishment allocation); (b) Store Manager or Dept. Supervisor receives and places on display per planogram (W86); (c) Stock Associate confirms receipt and placement in system | DC Team / Store Manager | Store Manager | Per W4 |
| 5 | **Periodic condition assessment**: (a) Quarterly: Dept. Supervisor assesses sample/demo condition at each store: "Good" (continue display), "Fair" (schedule replacement), "Poor" (remove and dispose); (b) for tool demo units: check functional condition (power tools, appliance demos); (c) for tile/paint swatches: check for fading, staining, chipping; (d) system tracks condition by sample/demo item | Dept. Supervisor | Store Manager | 30 min/store/quarter |
| 6 | **Replacement cycle**: (a) At end of useful life or when condition reaches "Poor": system auto-generates replacement sample request to Category Manager; (b) Category Manager approves replacement and initiates procurement per step 2; (c) new sample received and displayed before old sample removed (continuous display) | Category Manager | VP Merchandising | 10 min/replacement |
| 7 | **Disposal of old samples**: (a) System creates disposal request for sample/demo item reaching end of life; (b) disposition options: (i) return to vendor if vendor-funded with return provision, (ii) donate to trade school or community program, (iii) scrap/dispose (most common for worn samples); (c) Store Manager authorizes disposal; system removes from sample/demo inventory and posts GL: Dr. Sample/Display Expense / Cr. Sample Inventory (at original WAC); (d) for vendor-funded samples: if vendor requires return, ship to DC for consolidation per W88 | Store Manager / Stock Associate | Category Manager | 10 min/disposal |
| 8 | **Financial reporting**: (a) Cost Accountant tracks total sample/demo inventory value: by category, by store, by age; (b) monthly: sample/demo value included in total inventory valuation for GL (W9A.6) but excluded from saleable inventory reports; (c) quarterly: Category Manager reviews sample/demo investment vs. sales lift in that category (ROI analysis); (d) annual: sample/demo expense budgeted as merchandising display cost in W26 | Cost Accountant / Category Manager | Controller / VP Merchandising | 1 hour/quarter |

### System Touchpoints
- Sample/demo inventory status: blocked from POS sale, ATP, and replenishment; included in GL inventory valuation (W97.3)
- Sample/demo request and procurement workflow (from existing stock, vendor order, or custom fabrication) (W97.1–2)
- Distribution tracking with receipt confirmation and planogram placement (W97.4)
- Periodic condition assessment with Good/Fair/Poor status tracking (W97.5)
- Auto-replacement request at end of useful life or poor condition (W97.6)
- Disposal workflow with GL posting (expense recognition at disposal, not procurement) (W97.7)
- Sample/demo inventory reporting: value by category, store, age; ROI analysis (W97.8)
- Integration with W1 (assortment — sample needs from category resets), W2/W38 (procurement — sample orders), W3 (receiving — sample receipt type), W4 (distribution — sample shipments), W42 (physical inventory — sample/demo items counted separately), W50 (PIM — sample images in ecommerce catalog), W63 (shelf labels — sample/display designation), W86 (planogram — sample placement), W91 (damaged goods — damaged sample disposal)

### Staffing Implication
- **Category Managers**: add ~2 hours/month for sample management across their categories. Absorbed within existing merchandising duties.
- **Dept. Supervisors**: add ~30 min/quarter per store for condition assessment. Absorbed.
- **Cost Accountant**: add ~1 hour/quarter for sample/demo reporting. Absorbed.
- **No incremental headcount.**

---



## W102. Category Performance Review & P&L Ownership

| Field | Detail |
|---|---|
| **Trigger** | Monthly category P&L review calendar (5th business day of following month) |
| **Frequency** | Monthly review; quarterly deep-dive aligned with W1 assortment review |
| **Volume** | 12 product categories across 200 stores + 4 DCs; reviewed by 5 Category Managers |
| **Owner** | Category Manager |
| **Participants** | Category Manager, Pricing Analyst, Buyer, Cost Accountant, VP Merchandising, Store Ops Director |

### Background

W1 (Merchandise Planning & Assortment Review) covers quarterly assortment decisions — add, drop, or adjust SKUs. However, there is no monthly workflow where Category Managers are held accountable for their category's profit contribution. In standard retail merchandising practice, Category Managers own a "mini-P&L" for their categories, reviewing revenue, gross margin, markdowns, shrinkage, and inventory productivity monthly. This workflow bridges the gap between W1 (strategic assortment) and W35 (management reporting) by creating a structured monthly accountability review at the category level.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates monthly category P&L report per category (and per Category Manager, covering 2–3 categories each): (a) **Revenue**: gross sales, returns, net sales — by store, by channel (in-store, ecommerce, B2B), by SKU count, (b) **COGS**: cost of goods sold at WAC, inbound freight allocation, landed cost adjustments, (c) **Gross Margin**: gross margin $ and % — vs. budget (W26) and vs. prior year, (d) **Markdowns & Clearance**: total markdown value, markdown % of revenue — by reason (seasonal, slow-mover, damaged, promotional), per W93, (e) **Shrinkage**: inventory loss by category from W92 shrinkage report, (f) **Net Margin**: gross margin − markdowns − shrinkage = contribution margin by category, (g) **Inventory Productivity**: inventory turns, weeks of supply, GMROI (Gross Margin Return on Inventory Investment), sell-through %, (h) **Vendor Performance**: on-time delivery %, fill rate %, quality reject rate for top vendors in category per W44 | System | — | Automated (nightly batch, available T+3 business days) |
| 2 | Category Manager reviews their category P&L and prepares analysis: (a) identify top 3 positive and top 3 negative variance drivers vs. budget, (b) explain margin erosion or improvement (cost changes from W40, promotional impact from W13, markdown impact from W93), (c) highlight store-level outliers (top 5 and bottom 5 stores by category margin), (d) identify SKUs with significant margin decline (cost up but SRP not adjusted per W40), (e) assess inventory productivity — categories with declining turns or excess weeks of supply need action plan | Category Manager | VP Merchandising | 3–4 hours/category/month |
| 3 | Pricing Analyst provides supporting analysis: (a) price elasticity observations from recent W40 price changes, (b) promotional ROI from recent W13 events, (c) competitive pricing benchmarking updates, (d) quantity break utilization from W40.19 | Pricing Analyst | Category Manager | 2 hours/month |
| 4 | Cost Accountant provides: (a) WAC verification per category (any unusual WAC movements from import FX, landed cost adjustments), (b) intercompany margin impact (if category products flow through IC per W14), (c) NRV (Net Realizable Value) review for slow-moving categories per W9A.16b | Cost Accountant | Controller | 1 hour/month |
| 5 | Category Manager presents category P&L review to VP Merchandising in monthly category review meeting (30–45 min per category): (a) performance summary — did the category meet revenue, margin, and inventory targets?, (b) variance explanations with root cause, (c) action plan for underperforming areas (pricing adjustment per W40, assortment change per W1, vendor negotiation, markdown acceleration per W93, replenishment parameter adjustment per W31.8), (d) forward-looking outlook — upcoming seasonal factors, promotional plans, vendor cost changes | Category Manager | VP Merchandising | 30–45 min/category |
| 6 | VP Merchandising and Category Manager agree on action items with owners and deadlines; system tracks action items to closure | VP Merchandising | Category Manager | 10 min/category |
| 7 | Quarterly (aligned with W1): deeper analysis including (a) category contribution to total company P&L, (b) category market share analysis (if data available), (c) competitive category benchmarking, (d) SKU rationalization opportunities (further depth beyond W1), (e) vendor portfolio review for category (continue, expand, reduce, or exit vendor relationships per W44) | Category Manager / VP Merchandising | VP Merchandising | 2 hours/category/quarter |

### System Touchpoints
- Category P&L report with revenue, COGS, gross margin, markdowns, shrinkage, net margin, inventory turns, GMROI (W102.1)
- Budget vs. actual variance analysis by category (integration with W26 budget data) (W102.1)
- Store-level drill-down by category for top/bottom store identification (W102.2)
- Action item tracking with owner, deadline, and status (W102.6)
- Integration with W1 (assortment review), W13 (promotional impact), W26 (budget), W31 (demand forecast accuracy), W35 (management reporting), W40 (pricing changes), W44 (vendor performance), W85 (product costing), W93 (markdown analysis)

### Staffing Implication
- **Category Managers**: ~3–4 hours/category/month × 2–3 categories each = ~8–12 hours/month. This is a core part of their role. Absorbed.
- **Pricing Analysts**: ~2 hours/month for supporting analysis across all categories. Absorbed.
- **Cost Accountant**: ~1 hour/month. Absorbed.
- **VP Merchandising**: ~30–45 min × 5 Category Managers = ~3–4 hours/month for review meetings. Absorbed.
- **No incremental headcount.**

---



## W107. Pricing Hierarchy Governance & Compliance Audit

| Field | Detail |
|---|---|
| **Trigger** | Quarterly pricing governance review calendar; or ad-hoc triggered by pricing conflict (W13/W40 conflict), competitive price war, or regulatory inquiry |
| **Frequency** | Quarterly governance review; annual comprehensive audit |
| **Volume** | 35,000 active SKUs across 6+ pricing types (SRP, trade, corporate, promotional, quantity break, employee) |
| **Owner** | Pricing Analyst (governance); Internal Audit (compliance) |
| **Participants** | Pricing Analyst, Category Manager, VP Merchandising, Internal Audit, IT, Store Operations |

### Background

BuildRight operates 5+ concurrent pricing mechanisms: regular SRP (W40), promotional pricing (W13), trade/corporate account pricing (W5B.4c, W24), quantity break pricing (W40.15–19), competitor price matching (W61), and employee discount (W5B.12). Each has its own workflow, but there is no unified governance framework defining the pricing rule hierarchy (which price wins when multiple prices apply), periodic compliance verification (are shelf tags, POS, and ecommerce prices aligned?), and audit of pricing override patterns. This workflow creates that governance layer.

### Pricing Hierarchy Rules (System-Enforced)

| Priority | Price Type | When Applied | Override Authority |
|---|---|---|---|
| 1 | Clearance/Markdown (W93) | Item flagged as clearance | Category Manager |
| 2 | Promotional Price (W13) | Within active promo date range | Pricing Analyst (setup); system auto-applies |
| 3 | Competitor Price Match (W61) | Customer request with proof | Cashier + Store Manager authorization |
| 4 | Quantity Break Price (W40.15) | Scanned quantity meets threshold | System auto-applies — no override |
| 5 | Trade/Corporate Account Price (W5B.4c) | Customer identified at POS | Cashier selects account; system auto-applies |
| 6 | Employee Discount (W5B.12) | Employee ID scanned | Cashier; system enforces limits |
| 7 | Regular SRP (W40) | Default — no other price applies | N/A |

**Conflict resolution**: When two or more pricing rules could apply, system applies the lowest price (customer-friendly) and logs the conflict for Pricing Analyst review. Exceptions: (a) employee discount does not stack with promotional or quantity break pricing — lower of employee discount or promo/QB applies, (b) trade account pricing and quantity break pricing do not stack — lower of the two applies, (c) clearance price is absolute — no further discounts apply on clearance items (W93 shelf labels display "Clearance — Final Sale — No Returns").

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **System conflict log review**: Pricing Analyst reviews weekly pricing conflict log generated by system — instances where multiple pricing rules applied to the same SKU at POS or ecommerce; each conflict shows: SKU, store/channel, prices compared, price applied, transaction reference; Pricing Analyst validates that the system applied the correct hierarchy rule | Pricing Analyst | Category Manager | 1 hour/week |
| 2 | **Override audit**: Pricing Analyst reviews weekly POS price override report (W5B.4a) — all manual price overrides by cashier, authorizing manager, original price, override price, and reason code; flags: (a) cashiers with high override frequency (> 2× store average), (b) overrides exceeding 20% of original price without competitive price match documentation, (c) overrides in categories not typically subject to negotiation (e.g., small hardware), (d) pattern of overrides concentrated on specific SKUs (possible shelf tag/system price error requiring W63 correction) | Pricing Analyst | Category Manager | 1 hour/week |
| 3 | **Quarterly shelf tag vs. POS vs. ecommerce price alignment**: (a) system generates price alignment report: compares current shelf tag price (from W63 print file), POS system price, and ecommerce published price for all active SKUs; (b) Pricing Analyst reviews discrepancies — any SKU where the three prices do not match; (c) discrepancies routed for correction: POS mismatch → IT (W48), shelf tag mismatch → Store Operations (W63), ecommerce mismatch → Ecommerce Team (W50); (d) Pricing Analyst tracks resolution; uncorrected mismatches > 5 business days escalated to VP Merchandising | Pricing Analyst / IT / Store Ops | VP Merchandising | 4 hours/quarter |
| 4 | **Quarterly pricing rule review**: Pricing Analyst and Category Manager review pricing rule configuration: (a) quantity break thresholds — are tiers driving incremental volume per W40.19 analytics?, (b) trade account discount tiers — are they aligned with current margin targets and competitive positioning?, (c) promotional pricing rules — are promo-to-base price ratios consistent with promotional ROI targets from W13.10?, (d) employee discount rate — is current rate (default 10%) appropriate given margin impact? | Pricing Analyst / Category Manager | VP Merchandising | 2 hours/quarter |
| 5 | **Annual comprehensive pricing audit**: Internal Audit conducts full pricing compliance audit: (a) sample 200 transactions per store (20 stores sampled) — verify correct price was applied per hierarchy rules, (b) verify all price changes during the year followed W40/W13 approval workflows (audit trail completeness), (c) verify pricing master data security — only authorized Pricing Analysts and Category Managers can create/modify price records, (d) verify promotional pricing auto-reverts after promo period (W13.9), (e) verify BIR-compliant price display on receipts (SRP inclusive of VAT per Consumer Act RA 7394), (f) report findings to CFO and VP Merchandising with recommendations | Internal Audit | CFO | 40 hours/year (1 week) |
| 6 | **Pricing change approval compliance review**: Monthly, Pricing Analyst generates pricing change audit report showing all price changes (W40) and promotional price changes (W13) during the period — for each change: who initiated, who approved, was the correct approval tier used per W40.5 thresholds, was margin impact documented; report submitted to VP Merchandising for review | Pricing Analyst | VP Merchandising | 1 hour/month |

### System Touchpoints
- Weekly pricing conflict log from POS and ecommerce transactions with hierarchy rule details (W107.1)
- Weekly POS price override report with cashier, manager, and reason code analysis (W107.2)
- Quarterly price alignment report comparing shelf tag, POS system, and ecommerce prices (W107.3)
- Pricing rule configuration review with utilization analytics from W40.19 (W107.4)
- Annual pricing compliance audit sampling and workflow trail verification (W107.5)
- Monthly pricing change audit report with approval compliance check (W107.6)
- Pricing hierarchy engine: configurable priority rules, conflict resolution logic, and stacking rules enforced at POS and ecommerce checkout (W107 pricing hierarchy table)
- Integration with W5B (POS pricing), W13 (promotional pricing), W24 (trade account pricing), W40 (regular pricing and quantity breaks), W61 (price matching), W63 (shelf labels), W69 (price compliance audit — W69 is store-level daily scanning; W107 is centralized governance), W93 (clearance pricing)

### Staffing Implication
- **Pricing Analysts**: adds ~3 hours/week for conflict log and override review + ~6 hours/quarter for shelf tag alignment and pricing rule review + ~1 hour/month for change audit = ~20 hours/month. With 3 Pricing Analysts, this is ~7 hours each/month. Absorbed.
- **Internal Audit**: 40 hours/year for annual comprehensive pricing audit. Absorbed within annual audit plan.
- **No incremental headcount.**

---

## W129. Private Label / In-house Brand Development

| Field | Detail |
|---|---|
| **Trigger** | Category strategy (white space identification) or high-volume item with margin expansion potential |
| **Frequency** | Periodic; 10–20 new products per year |
| **Volume** | Managing ~5–10 in-house brands |
| **Owner** | Private Label Manager |
| **Participants** | Category Manager, Quality Assurance (QA), Legal (IP), Sourcing |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Concept Design: Identify high-turn items for private label substitution/complement | Private Label Mgr | VP Merch | 1 week |
| 2 | Sourcing: Identify and vet manufacturers (domestic or international) | Sourcing Spec | VP Merch | 2–4 weeks |
| 3 | Product Specs & Sampling: Define quality benchmarks and review prototypes | QA Specialist | Private Label Mgr | 1–3 months |
| 4 | Brand & Packaging: Design logo/packaging and file IP (W126) | Marketing / Legal | CMO | 2 weeks |
| 5 | Initial Order & Quality Inspection: Place first PO (W2) and conduct AQL testing | Sourcing Spec | QA Specialist | 2 months |
| 6 | Launch: Set price (W40), create PIM record (W50), and allocate to stores (W57) | Private Label Mgr | Category Mgr | 1 week |

---

## W130. Competitor Price Intelligence Gathering

| Field | Detail |
|---|---|
| **Trigger** | Weekly pricing review cycle |
| **Frequency** | Weekly |
| **Volume** | ~500–1,000 "KVIs" (Known Value Items) tracked per competitor |
| **Owner** | Pricing Analyst |
| **Participants** | Store Staff (manual checks), Web Scraping Tools (digital) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Define KVI List: Top 1,000 SKUs that drive price perception | Pricing Analyst | Category Mgr | Quarterly |
| 2 | Manual Price Check: Store associates visit local competitors to record prices | Store Assoc | Store Manager | 4 hours/week |
| 3 | Digital Price Check: Automated scraping of competitor ecommerce sites | Pricing Analyst | System | Daily |
| 4 | Data Consolidation: Upload manual and digital prices into ERP/Pricing Tool | Pricing Analyst | Pricing Analyst | 1 day/week |
| 5 | Gap Analysis: Identify items where BuildRight is > 5% above market | Pricing Analyst | Category Mgr | 2 hours/week |
| 6 | Price Adjustment: Propose markdowns/updates per W40 or W61 | Pricing Analyst | Category Mgr | 1 hour/week |

---

### System Touchpoints (Merchandising Extensions)
- Private label status flag in Item Master
- Competitor price entry portal (mobile-ready for store associates)
- Pricing gap analysis dashboard with "Actionable" alerts
- Integration with IP management for brand protection (W126)
- Quality Assurance test result logging for private label samples

---

---

## W181. Store-Level Price Tag Printing & Verification

| Field | Detail |
|---|---|
| **Trigger** | Central price update (W40/W13); or shelf tag discrepancy report (W5B.11) |
| **Frequency** | Daily / As-needed |
| **Owner** | Store Manager |
| **Participants** | Stock Associate, Cashier (Verification) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Batch Generation**: ERP flags items with price changes; system creates "Price Tag Print Batch" per store | System | — | Automated |
| 2 | **Printing**: Stock Associate prints new shelf tags at the store office using dedicated label printers | Stock Associate | — | 15 min |
| 3 | **Tag Replacement**: Associate walks floor; replaces old tags; scans new tag with handheld to "Confirm Replacement" | Stock Associate | Dept Supervisor | 1 hour |
| 4 | **Verification**: Cashier or Supervisor performs random "Price Scan Audit" (W69): scans 20 items on shelf; system verifies shelf price matches POS | Cashier | Store Manager | 15 min |
| 5 | **Error Correction**: If mismatch found, system triggers immediate re-print and investigates sync lag | System | Store Manager | 5 min |

### System Touchpoints
- Automated price tag batching based on W40/W13
- Handheld scan-confirmation of tag replacement
- Real-time audit dashboard


## W262. Store Promotional Setup & Visual Merchandising Execution

| Field | Detail |
|---|---|
| **Workflow ID** | W262 |
| **Name** | Store Promotional Setup & Visual Merchandising Execution |
| **Trigger** | Promotional calendar activation (bi-monthly sale events, monthly hot deals, seasonal transitions) |
| **Frequency** | 6 major catalog-based promotions/year + 12 monthly hot deal cycles + 6 seasonal transitions = ~24 cycles/year |
| **Volume** | ~200 stores per cycle; ~10–20 featured items for monthly hot deals; ~50–150 items for bi-monthly catalog sales |
| **Owner** | Department Supervisor |
| **Participants** | Department Supervisor (4/store), Stock Associate (4/store), Store Manager (1/store), Visual Merchandising Coordinator (HQ, 2) |
| **Time Estimate** | 4–8 hours per major promotion; 1–2 hours per monthly hot deal cycle |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Promotional Brief Receipt**: Store receives promotional setup brief from HQ Visual Merchandising team: (a) planogram showing display location, shelf positioning, and endcap layout; (b) item list with promotional SKUs, expected quantities, and backup stock requirements; (c) POS signage and shelf tag files (auto-generated from W13 pricing push); (d) visual reference photos or renders for display standards; (e) setup deadline (typically 2 days before promo start date) | System / VM Coordinator | Store Manager | 15 min review |
| 2 | **Material & Signage Preparation**: Stock Associate prints promotional materials: (a) shelf tags and price labels auto-generated from W13/W40 pricing data via W181 price tag printing; (b) promotional banners, posters, and point-of-purchase (POP) displays from HQ design assets (W190); (c) POS-triggered promotional messaging for customer-facing displays; (d) "Sale Starts [Date]" and "Sale Ends [Date]" signage | Stock Associate | Department Supervisor | 1–2 hours |
| 3 | **Stock Pulling & Staging**: Stock Associate pulls promotional inventory from backroom: (a) system generates pick list of promotional SKUs with required display quantities per planogram; (b) Stock Associate picks from backroom stock; (c) if backroom stock insufficient: system flags for W4B store-initiated replenishment or W22 inter-store transfer; (d) promotional stock staged near display area before setup | Stock Associate | Department Supervisor | 1–2 hours |
| 4 | **Display Construction**: Department Supervisor leads display setup: (a) endcap displays for top promotional items (build fixture, arrange products, attach pricing); (b) promotional islands/gondola ends for mid-tier items; (c) sale bins or pallet displays for clearance/bulk items; (d) category cross-merchandising displays (e.g., paint + brushes + tarps as "painting starter kit" per W13 bundle offers); (e) display must match planogram photo from HQ within 90% compliance | Department Supervisor | Store Manager | 2–4 hours |
| 5 | **Signage & Tag Placement**: Stock Associate places all pricing and promotional signage: (a) shelf tags replaced with promotional tags (W181); (b) large-format price signs on displays; (c) promotional banners at store entrance and category aisles; (d) "Bundle Offer" signs for kit deals; (e) QR codes linking to ecommerce promo page for BOPIS orders | Stock Associate | Department Supervisor | 1–2 hours |
| 6 | **Compliance Self-Check**: Department Supervisor performs visual compliance check: (a) all promotional SKUs present and correctly priced (scan test at POS to verify promo price auto-applies per POS-014); (b) display matches planogram reference photo; (c) signage is accurate (correct prices, dates, terms and conditions); (d) sufficient stock on display (minimum display quantity per planogram); (e) photographs display setup and uploads to HQ VM portal for compliance tracking | Department Supervisor | Store Manager | 30 min |
| 7 | **Promotional Period Monitoring**: During promotion: (a) Stock Associate monitors display stock levels; replenishes from backroom as needed; (b) if display stock depleted and backroom empty: Department Supervisor escalates to Store Manager for emergency replenishment (W60) or display consolidation; (c) Department Supervisor replaces damaged signage; (d) system tracks promotional sell-through vs. forecast for HQ merchandising team (W13.8) | Stock Associate / Dept Supervisor | Store Manager | Daily, 15 min |
| 8 | **Promotion Teardown & Reset**: At promotion end: (a) Stock Associate removes all promotional signage and shelf tags; (b) system auto-reverts prices to regular SRP per W13 end-date; (c) unsold promotional stock returned to regular shelf positions or backroom; (d) clearance items (if applicable) moved to clearance section per W93 markdown process; (e) display fixtures disassembled and stored; (f) Department Supervisor confirms teardown completion in system; (g) system generates promotional sell-through summary: units sold, revenue, margin, remaining stock | Stock Associate / Dept Supervisor | Store Manager | 2–3 hours |

### System Touchpoints
- Promotional setup brief distribution (HQ → Store) with planogram, item list, and visual references
- Auto-generation of promotional shelf tags and signage via W181 integration with W13 pricing
- Pick list generation for promotional stock pulling from backroom inventory
- Planogram compliance photo upload and HQ review portal
- POS scan verification for promotional pricing accuracy
- Real-time promotional sell-through dashboard (units, revenue, margin vs. forecast)
- Auto price-revert at promotion end date
- Post-promotion stock disposition workflow (return to shelf, clearance, RTV)

### Pain Points / Risks
- **Stock availability**: Promotional display requires pulling stock from regular shelves; if backroom is empty, display is incomplete and sell-through suffers
- **Planogram non-compliance**: Stores in different formats (corner lots vs. stand-alone) may not be able to replicate planogram exactly; need format-specific fallback plans
- **Signage timing**: If shelf tags printed too early, customers see promotional price before promo starts; if too late, first-day sales missed
- **Teardown delay**: Store staff may delay teardown after promo ends, causing customer confusion about pricing; system auto-revert helps but physical signage must be removed promptly
- **Cross-store inconsistency**: Without photo compliance, display quality varies significantly across 200 stores; HQ has limited visibility into execution quality
- **Seasonal transition bottleneck**: Seasonal transitions (§13.2) involve 50+ SKUs changing simultaneously; requires dedicated team effort over 1–2 days

## W264. Seasonal Merchandise Transition & Display Rotation

| Field | Detail |
|---|---|
| **Workflow ID** | W264 |
| **Name** | Seasonal Merchandise Transition & Display Rotation |
| **Trigger** | Seasonal calendar transition point (6 per year per §13.2) |
| **Frequency** | 6 major transitions/year (Jan–Feb post-holiday, Mar–Apr summer, May school build-out, Jun–Aug rainy season, Sep–Oct ber-months, Nov–Dec Christmas) |
| **Volume** | ~50–150 SKUs transitioning per season across 200 stores = 10,000–30,000 store-SKU transitions per cycle |
| **Owner** | Category Manager |
| **Participants** | Category Manager (6), Buyer (8), Store Manager (200), Department Supervisor (800), VP Merchandising (1), Visual Merchandising Coordinator (2) |
| **Time Estimate** | 3–5 weeks per transition cycle (planning 2 weeks + execution 1–2 weeks + review 1 week) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Seasonal Review & Planning**: Category Manager reviews upcoming season (per §13.2 calendar): (a) analyzes prior-year seasonal performance: sell-through rate, margin, markdown depth, dead stock units; (b) identifies carry-forward SKUs (perennial seasonal items), new SKUs to introduce, and outgoing SKUs to discontinue or markdown; (c) determines seasonal assortment quantity per store cluster (high-demand vs. low-demand regions — e.g., summer garden items sell more in Visayas; rainy season items sell more in flood-prone areas); (d) Category Manager presents seasonal plan to VP Merchandising for approval | Category Manager | VP Merchandising | 3–5 days |
| 2 | **Incoming Seasonal PO Placement**: Buyer places purchase orders for incoming seasonal merchandise: (a) import POs (W2B) for seasonal imports with 60–90 day lead time (e.g., Christmas lights from China ordered in Aug–Sep); (b) domestic POs for locally sourced seasonal items with 14–30 day lead time; (c) seasonal buy planning per W32 with forward-buy quantities based on forecast; (d) PO delivery timed to arrive at DCs 2–3 weeks before in-store display date | Buyer | Category Manager | 2–3 days |
| 3 | **Outgoing Seasonal Markdown Trigger**: System identifies outgoing seasonal SKUs for markdown per W93: (a) items from ending season not carried year-round; (b) system calculates markdown depth based on: weeks of supply remaining, historical sell-through curve, target clearance date; (c) Category Manager approves markdown schedule: (i) first markdown 20% at season end, (ii) second markdown 40% after 2 weeks, (iii) final clearance 60% + consolidation to select stores; (d) markdown prices pushed to POS per W93 approval workflow | System / Category Manager | VP Merchandising | 1 day |
| 4 | **Store Communication & Setup Brief**: HQ distributes seasonal transition brief to all stores: (a) seasonal setup guide with new planograms, display layouts, and visual references; (b) list of incoming seasonal SKUs with expected DC delivery dates; (c) list of outgoing SKUs with markdown schedule and display removal dates; (d) seasonal promotional calendar (W13) with promotional pricing and bundle offers specific to season; (e) Store Manager assigns seasonal setup to Department Supervisors by category | VM Coordinator / Category Manager | Store Manager | 1 day |
| 5 | **Outgoing Display Teardown**: At store level: (a) Department Supervisor removes outgoing seasonal displays per teardown schedule; (b) unsold outgoing stock disposition: (i) markdown items remaining → move to clearance section per W93, (ii) carry-forward items → return to regular shelf position, (iii) discontinued items → initiate RTV per W88 or consolidate to high-volume stores per W22; (c) Department Supervisor confirms teardown completion in system | Department Supervisor | Store Manager | 4–8 hours |
| 6 | **Incoming Stock Receiving & Display Build**: (a) DC ships incoming seasonal stock per W4 replenishment with seasonal allocation priority; (b) store receives and stages incoming seasonal stock per W109; (c) Department Supervisor builds new seasonal displays per planogram: (i) high-impact endcap or island display for top 10 seasonal items, (ii) category aisle seasonal section for secondary items, (iii) seasonal cross-merchandising displays (e.g., summer: garden tools + soil + planters displayed together); (d) Stock Associate places shelf tags and promotional signage per W262 | Department Supervisor / Stock Associate | Store Manager | 4–8 hours |
| 7 | **Launch & In-Season Monitoring**: (a) seasonal merchandise goes live on promotional calendar start date; (b) Category Manager monitors daily sell-through dashboard: units sold, revenue, margin, weeks of supply, sell-through % vs. plan; (c) early-season adjustments: (i) if sell-through > plan by 20%: Buyer places supplemental PO (W60 emergency or W2A auto-replenishment), (ii) if sell-through < plan by 30% after 2 weeks: Category Manager considers markdown acceleration or promotional bundle (W13); (d) weekly seasonal review with VP Merchandising | Category Manager / Buyer | VP Merchandising | Ongoing (daily 30 min + weekly 1 hour) |
| 8 | **Post-Season Review**: At season end: (a) Category Manager prepares seasonal post-mortem: (i) total seasonal revenue vs. plan, (ii) sell-through rate by SKU and store cluster, (iii) markdown depth and cost, (iv) dead stock units and disposition cost, (v) margin impact, (vi) customer feedback themes (W87); (b) lessons learned documented for next year's seasonal planning; (c) carry-forward decisions: which items to stock year-round vs. seasonal-only; (d) feed into annual assortment review (W1) and next year's seasonal buy plan (W32) | Category Manager | VP Merchandising | 1–2 days |

### System Touchpoints
- Seasonal merchandise planning module linked to W32 seasonal buy planning and W31 demand forecasting
- Prior-year seasonal performance analytics (sell-through, margin, markdown)
- Seasonal assortment allocation engine with store clustering (regional demand patterns)
- Markdown trigger engine (W93) with automated schedule based on sell-through curves
- Seasonal planogram distribution (HQ → Store) with compliance photo tracking
- Real-time seasonal sell-through dashboard (daily units, revenue, margin, WOS vs. plan)
- Supplemental PO generation for high-demand seasonal items
- Post-season analytics package (revenue, margin, markdown cost, dead stock)

### Pain Points / Risks
- **Import lead time mismatch**: Seasonal imports with 60–90 day lead times must be ordered before sell-through data confirms demand; risk of overbuying or underbuying
- **Regional demand variance**: Summer items sell differently in Mindanao vs. Luzon; store clustering must account for climate and cultural differences across Philippine regions
- **Markdown timing**: Starting markdowns too early erodes margin; starting too late leaves dead stock; optimal markdown curve requires continuous tuning
- **Display labor intensity**: Each seasonal transition requires 4–8 hours of store labor across 200 stores = 800–1,600 store-hours per transition; conflicts with daily operations staffing
- **Dead stock carry cost**: Unsold seasonal items occupying backroom space reduce available storage for core replenishment; disposition decisions delayed due to reluctance to recognize losses
- **Typhoon disruption**: Philippines' typhoon season (Jun–Nov per W49) can disrupt DC shipments during critical seasonal transition windows; need contingency logistics plan
