# BuildRight Depot Corp. — Assumptions & Design Decisions

> This document consolidates the key assumptions and design decisions embedded across the
> model company documents. It serves as a single reference for understanding *why* certain
> parameters were chosen. Each assumption is cross-referenced to its source document.

---

## A1. Scale & Revenue Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A1.1 | All 200 stores are mature | Revenue figures assume all stores are past ramp-up | Simplifies modeling; real-world would have 10–15 stores in ramp-up at any time | Profile §9.4 |
| A1.2 | Average Transaction Value | PHP 1,800 | Benchmarked against Philippine big-box home improvement retail; ~90% of Wilcon's estimated ATV reflecting more provincial footprint | Profile §9.4 |
| A1.3 | Monthly POS transactions per store | 14,000 (~467/day) | Derived from 2.8M monthly ÷ 200 stores; consistent with high-traffic big-box retail | Profile §5 |
| A1.4 | Ecommerce penetration Year 1 | ~3% of revenue | Conservative for Philippine retail; aligns with early-stage omnichannel in the market | Profile §8.5 |
| A1.5 | Gross margin | 28–32% | Below Wilcon's ~30–33% reflecting newer stores and provincial mix | Profile §9.4 |
| A1.6 | EBITDA margin | 12–14% | Below Wilcon's ~14–16% due to higher logistics costs from 4-DC provincial footprint | Profile §9.4 |

## A2. Organizational Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A2.1 | Single format (big-box only) | No Express/small format | Simplifies the model; tests one format thoroughly vs. two superficially | Profile §2 |
| A2.2 | Store staffing: 28 per store | Lean model | Viable with 35K curated SKUs (vs. Wilcon's 60K+); fewer departments to cover | Profile §12.1 |
| A2.3 | HQ in Davao City | Provincial HQ | Deliberately non-Manila to test provincial operations and connectivity | Profile §2 |
| A2.4 | 5 legal entities | Separate Holdings, Depot, Logistics, Digital Commerce, Property Mgmt | Tests multi-entity/intercompany capability; each entity has a distinct role | Profile §2 |
| A2.5 | Depot Inc. owns all inventory | Even though Logistics Inc. operates DCs | Simplifies inventory accounting; Logistics Inc. charges service fees, not goods transfer | Profile §2, W14 |
| A2.6 | Revenue per employee | ~PHP 7.7M/year | Higher than Wilcon's ~PHP 5.2M due to lean staffing model; sustainable with automation | Profile §4 |

## A3. Supply Chain Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A3.1 | 4 DCs for 200 stores | DC-to-selling-area ratio ~8–12% | Industry norm for big-box retail; 4 DCs reduces average store-to-DC distance in archipelago | Profile §3.2 |
| A3.2 | DC4 (Clark) oversized at 25K sqm | Only 20 stores currently | Intentional: absorbs planned North/Central Luzon expansion | Profile §3.2 |
| A3.3 | 30% DSD by value | Cement, lumber, sand, gravel | Bulky items uneconomical to double-handle through DCs | Profile §7.1 |
| A3.4 | ~400–600 TEUs/month imports | ~40% of COGS from imports | Consistent with Philippine home improvement import volumes at this scale | Profile §7.1 |
| A3.5 | Inventory turns target: 6–8x | Curated 35K SKU assortment | Philippine island geography and import lead times make higher turns aspirational | Profile §12.3 |
| A3.6 | Shrinkage target: <1.5% | Aspirational for Philippine retail | Industry average ~1.5–2.5%; requires mature LP systems | Profile §12.3 |

## A4. Product & Merchandise Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A4.1 | 35,000 active SKUs | Curated assortment | Leaner than Wilcon's 60K+; focused on faster turn; 2.3–4.4 SKUs/sqm | Profile §6.1 |
| A4.2 | Inventory valuation: WAC | Weighted Average Cost | Standard in Philippine retail; simpler than FIFO for big-box | Profile §6.3 |
| A4.3 | ~800–1,000 active vendors | 60% local, 40% import | Realistic mix for Philippine home improvement at this scale | Profile §6.5 |
| A4.4 | Top 20 vendors = 45% of COGS | Vendor concentration | Realistic for organized retail; drives blanket PO and rebate strategies | Profile §6.5 |

## A5. Financial Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A5.1 | PHP functional currency | PHP base; USD for imports | Philippine company; imports in USD | Profile §10.1 |
| A5.2 | VAT 12% | Standard Philippine VAT | Applied to most goods; some exempt/zero-rated customers exist | Profile §10.5 |
| A5.3 | Monthly IC settlement | All IC flows settled monthly on 5th | Simplifies cash management; may need twice-monthly for ecommerce as it grows | W14 |
| A5.4 | Loyalty deferred revenue ~1% | PFRS 15 allocation | Face value of points; actual allocation may differ based on expected redemption rate | W17 |
| A5.5 | Month-end close ≤ 5 days | Target | Achievable with automated IC elimination and bank reconciliation | Profile §15.3 |

## A6. IT & System Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A6.1 | POS offline ≥ 8 hours | Local cache of product/price | Philippine internet reliability; stores must sell during outages | NFR-011 |
| A6.2 | No strict PH data residency | Asia-Pacific hosting recommended | Philippines has no mandatory data residency law; latency matters more | Technical Guidelines §2.1 |
| A6.3 | Ecommerce platform: build vs buy | Decision deferred to ERP evaluation | Each ERP platform offers different ecommerce options (native, integrated, or third-party); evaluator should recommend | This document |
| A6.4 | Mobile app: branded native app | iOS + Android | Required for BOPIS pickup notifications, loyalty, and customer engagement; built on ERP-provided APIs or third-party | This document |
| A6.5 | 7-year data retention | BIR requirement | Drives storage sizing (~700 GB uncompressed over 7 years) | Profile §15.3 |

## A7. Implementation Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A7.1 | Phased rollout (not big-bang) | Pilot 5 stores → 7 waves | De-risks POS cutover for 2.8M monthly transactions | Implementation Roadmap §1 |
| A7.2 | Pilot in Mindanao (Davao) | Near HQ | Faster support response; learn before scaling to other regions | Implementation Roadmap §1 |
| A7.3 | 26-month total project duration | Phase 0 through Phase 5 | Includes pilot, 7 waves, and optimization | Implementation Roadmap §7 |
| A7.4 | Parallel run during pilot | 1 payroll cycle + 1 month-end close | Validates accuracy before cutover | Implementation Roadmap §3 |

---

## Design Decisions

| Decision | Choice Made | Alternative Considered | Why This Choice |
|---|---|---|---|
| DC network | 4 regional DCs | 3 mega-DCs | Better island coverage; lower outbound transport cost; industry-norm DC-to-selling-area ratio |
| IC model | Service-based (primary) | Goods-based between all entities | Depot Inc. owns all merchandise; simpler inventory accounting; Logistics Inc. charges service fees |
| SKU depth | 35,000 curated | 60,000+ deep | Faster turns; less floor coverage needed; viable with fewer store staff |
| Store format | Big-box only | Multi-format (Depot + Express) | Simpler model; single format tests one scenario thoroughly |
| Loyalty earn rate | 1 point per PHP 100 | Tiered earn by membership | Simpler to implement and communicate; standard in Philippine retail |
| BOPIS hold period | 5 days | 3 days or 7 days | 5 days balances customer convenience with inventory hold cost |
| POS terminals per store | 5 | 3–8 variable | 3 handles ~467 daily transactions across 10 operating hours with reasonable queues |
| Payroll frequency | Semi-monthly (15th & 30th) | Monthly | Philippine standard; mandated by many CBAs and DOLE guidelines |
| Fiscal year | Calendar year (Jan–Dec) | April–March or other | Aligned with Philippine tax year (BIR) |
| Blanket PO coverage | ~45% of COGS | Higher or lower | Aligned with top-20 vendor concentration; remaining 55% on standard POs |

---

*Date: 2026-05-30*
