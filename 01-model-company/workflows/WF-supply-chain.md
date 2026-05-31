# Supply Chain Planning Workflows

> Demand forecasting and seasonal buy planning.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W31. Demand Forecasting Cycle](#demand-forecasting-cycle)
- [W32. Seasonal Buy Planning](#seasonal-buy-planning)
- [W133. Sales & Operations Planning (S&OP) Cycle](#sales-operations-planning-sop-cycle)

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

## W133. Sales & Operations Planning (S&OP) Cycle

| Field | Detail |
|---|---|
| **Trigger** | Monthly management rhythm |
| **Frequency** | Monthly |
| **Volume** | Covers all 5 entities and 12 product categories |
| **Owner** | VP for Supply Chain & Logistics |
| **Participants** | COO, CFO, VP Merchandising, VP Store Ops, CMO |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Sales Review: Compare actual sales (W5) vs. forecast (W31); update demand | Demand Planner | CMO | 2 days |
| 2 | Supply Review: Assess inventory levels, lead times, and DC capacity | Supply Planner | VP Supply Chain | 2 days |
| 3 | Financial Review: Evaluate margin (W85) and working capital vs. budget (W26) | Finance Manager | CFO | 1 day |
| 4 | Pre-S&OP Meeting: Reconcile gaps between demand, supply, and finance | Supply/Demand | VP Supply Chain | 4 hours |
| 5 | Executive S&OP: Approve final demand plan and supply constraints | C-Suite | CEO | 2 hours |
| 6 | Cascade Plan: Adjust POs (W2), Replenishment (W4), and Promos (W13) | Dept Heads | — | Ongoing |

---

### System Touchpoints (Supply Chain Extensions)
- Consolidated S&OP dashboard: Demand vs. Supply vs. Financials
- Scenario modeling (What-if analysis for port delays or sales spikes)
- Executive consensus forecast record
- Automated alerts for S&OP plan vs. actual deviations (> 10%)

---



---

