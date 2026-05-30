# Workflow Gap Analysis — Wave 6 (Independent Review)

> A fresh, independent gap analysis cross-referencing all 49 operational workflows
> (`operational-workflows.md`) against the ERP requirements (`erp-requirements.md`),
> company profile (`model-company-profile.md`), and data volumes
> (`data-volumes-and-integrations.md`). This Wave 6 review targets gaps that
> Waves 1–5 missed: numerical errors with staffing implications, operational edge cases,
> and detail gaps in existing workflows.

---

## Executive Summary

Waves 1–5 resolved 52 gaps and achieved comprehensive coverage of the retail value chain.
This Wave 6 review identified **10 remaining gaps**: 1 numerical error with staffing impact,
6 business activities with no or insufficient workflow coverage, and 3 detail gaps.

**All 10 gaps have been resolved.**

| Gap Category | Count | Status |
|---|---|---|
| **A. Numerical error with staffing impact** | 1 | ✅ Resolved |
| **B. Business activities without workflows** | 6 | ✅ All 6 resolved |
| **C. Detail gaps in existing workflows** | 3 | ✅ All 3 resolved |

| Metric | Wave 5 Claimed | After Wave 6 Resolution |
|---|---|---|
| Total workflows | 49 | **49** (no new workflow; additions are steps within existing) |
| Cross-document errors | 0 claimed | **1 found → 0 remaining** |
| Business activities without workflows | 0 claimed | **6 found → 0 remaining** |
| Detail gaps | 0 claimed | **3 found → 0 remaining** |

---

## A. Numerical Error With Staffing Impact

### A1. ✅ Resolved — W19 Home Delivery Staffing Arithmetic Error

| Location | Value |
|---|---|
| W19 Header | "~17,200 delivery orders/month; ~573/day" |
| W19 Staffing (before fix) | "Per DC: Home delivery adds ~115 orders/day ÷ 5 DCs = ~23 orders/DC/day. At ~15 min pick+pack per order, that's ~6 hours/day" |
| Correct calculation | 17,200 ÷ 30 = 573 total/day. 573 ÷ 5 DCs = **~115 orders/DC/day** |
| Correct effort | 115 orders × 15 min = **~1,725 min ≈ 29 hours/DC/day** |

**Issue**: The staffing section substituted the per-DC figure (~115) as the total, then divided by 5 again, yielding ~23 instead of ~115. The labor estimate of ~6 hours/day should be ~29 hours/day — a material understatement affecting capacity planning.

**Impact**: Each DC needs 3–4 dedicated pickers/packers for home delivery alone, within the existing ~150 DC headcount. The 25–30 pickers/packers per DC must absorb both store replenishment (~33 orders/day with ~50 lines each) and home delivery (~115 orders/day with 3–4 items each). Peak ecommerce periods (3× normal per data volumes §1.1) could spike to ~345 home delivery orders/DC/day.

**Resolution**: ✅ Updated W19 staffing to reflect ~115 orders/DC/day, ~29 hours/DC/day, 3–4 dedicated pickers/packers per DC. Added monitoring note for ecommerce growth. Updated DC staffing validation table in Workflow-to-Headcount Summary.

---

## B. Business Activities With No or Insufficient Workflow Coverage

### B1. ✅ Resolved — Local Business Tax (LBT) Compliance Per LGU

| Attribute | Detail |
|---|---|
| **Source** | Profile §10.5: "Local Business Tax — Annual / Quarterly — Paid to LGU where each store/DC operates" |
| **Gap** | No workflow described LBT calculation, payment, and tracking for 200+ store locations + 5 DCs + HQ, each under a different LGU jurisdiction. With 206 locations across Mindanao, Visayas, and Luzon, each LGU has its own schedule, form, and rate structure. |
| **Why It Matters** | LBT is a material compliance obligation. Failure to pay results in penalties and potential business closure. ERP evaluators need to assess whether the system can track LBT obligations per location and generate LGU-specific filings. |
| **Resolution** | ✅ Added step W9a.16c: system generates LBT payment schedule per location based on configured LGU calendars; Tax Accountant validates amounts per LGU rate schedules; processes payments; system posts per location; tracks payment status with overdue alerting. Added system touchpoints for per-location LBT calendar and payment tracking. |

### B2. ✅ Resolved — Customer Credit Memo / AR Adjustment

| Attribute | Detail |
|---|---|
| **Source** | FIN-005 (AR for B2B), W8 (AR operations) |
| **Gap** | W7.9b added vendor credit memo processing. No equivalent workflow existed for customer-side credit memos — when a trade/corporate customer needs a credit for pricing errors, volume discount adjustments, short deliveries, service failures, or promotional adjustments that don't involve a physical return (W12). With ~5,200 active trade accounts, credit adjustments are a regular occurrence. |
| **Why It Matters** | Customer credit memos are a standard AR process with different approval requirements than vendor credits. Evaluators need to understand the workflow: credit creation, matching to source, approval, application to open invoices, and GL posting. |
| **Resolution** | ✅ Added step W8.11: AR Clerk creates credit memo with reason code and source reference (pricing error, volume discount, short delivery, service failure, promo adjustment); tiered approval (AR Supervisor ≤ PHP 10K, Finance Manager ≤ PHP 50K, CFO > PHP 50K); system applies to oldest open invoice or creates credit balance; GL posting (Dr. Revenue or Expense / Cr. Accounts Receivable). Added system touchpoints. |

### B3. ✅ Resolved — Vendor-Funded Promotional Settlement

| Attribute | Detail |
|---|---|
| **Source** | Profile §13.3: "Vendor-Funded Promos: Co-op advertising, vendor rebates" |
| **Gap** | W13 covered promotional pricing execution. W27 covered vendor rebate accrual and settlement. But vendor-funded promotions are a distinct financial flow: a vendor agrees to fund a temporary markdown (e.g., "buy paint at 20% off, funded by Boysen"). The retailer discounts at POS, then bills the vendor for the difference. This is different from a rebate (retroactive credit based on volume) because the discount is applied at the point of sale and the vendor reimbursement is a separate settlement. |
| **Why It Matters** | Vendor-funded promos are standard in Philippine retail. The system must track the gap between SRP and promo price per transaction, accumulate the vendor's share, and generate a settlement claim. Without this workflow, evaluators can't assess promo cost allocation capabilities. |
| **Resolution** | ✅ Added vendor-funded promo settlement to W13 system touchpoints: at POS, system records vendor funding portion per transaction line; accumulates vendor liability in dedicated promo settlement accrual account; monthly settlement report generated per vendor showing units sold at promo price × vendor share; AP credit memo generated per W7.9b. Distinguished from W27 (volume-based rebates). |

### B4. ✅ Resolved — Home Delivery Return Reverse Logistics

| Attribute | Detail |
|---|---|
| **Source** | ECOM-007 (Return Initiation Online), W12b (Online-Initiated Returns) |
| **Gap** | W12b covered online-initiated returns completed in-store. But for home delivery items that are large/bulky (appliances, lumber, tiles, fixtures), the customer cannot bring the item to a store. No workflow described the reverse logistics: scheduling a carrier pickup from the customer's address, returning the item to the DC, inspecting, and restocking. |
| **Why It Matters** | With 17,200 home delivery orders/month and ~5% return rate = ~860 returns/month. Even if only 10–20% are bulky items requiring pickup, that's ~85–170 reverse logistics events/month. Evaluators need to assess 3PL reverse logistics integration. |
| **Resolution** | ✅ Added step W19.12a: for bulky items exceeding in-store return size limits, system schedules carrier pickup via 3PL integration (W19 delivery partners); carrier collects from customer; item returned to DC for inspection; refund processed upon inspection confirmation; disposition per existing workflows (W12a.7, W6.8a). Added system touchpoints to W19 and cross-reference to W12. |

### B5. ✅ Resolved — Store Cash Deposit / Cash-in-Transit Logistics

| Attribute | Detail |
|---|---|
| **Source** | W5c (store closing), W30.1 (daily cash deposit) |
| **Gap** | W5c covered counting cash and preparing the deposit. W30.1 mentioned "armored car or bank branch deposit" in one sentence. But the daily cash logistics for 200 stores — each depositing PHP 200K–500K/day in cash — is a significant operational process: armored car scheduling, pickup confirmation, deposit slip reconciliation, and exception handling. |
| **Why It Matters** | At PHP 5.04B monthly in-store revenue with ~42% cash = ~PHP 2.1B/month in cash deposits across 200 stores. The cash-in-transit operation is material and has security implications. ERP evaluators may need to assess cash management integration with armored car providers. |
| **Resolution** | ✅ Added steps W5c.5a–b: sealed deposit bag procedure with tamper-evident bags; armored car pickup confirmation logging; bank deposit fallback for missed pickups; exception flagging. Added system touchpoints for cash-in-transit tracking to W5c and W30. Brief treatment — this is partially outside core ERP scope but the system must track deposit confirmations. |

### B6. ✅ Resolved — Confirmed Theft / Inventory Write-Off Process

| Attribute | Detail |
|---|---|
| **Source** | INV-011 (Inventory Aging), W37 (Loss Prevention), W9a.16b (NRV Write-Down) |
| **Gap** | W37 monitored shrinkage and investigated theft. W9a.16b covered NRV write-down for slow-moving inventory. W6.8a covered damage disposition. But no workflow described the full write-off process for confirmed theft or irrecoverable loss: police report filing, insurance claim (if covered), management approval for write-off, GL posting, and removal from inventory register. |
| **Why It Matters** | With shrinkage target of < 1.5% of sales = ~PHP 75M/month, confirmed losses require a formal write-off process with proper approvals and documentation. BIR may require supporting documents (police reports) for inventory loss deductions. |
| **Resolution** | ✅ Added W37.11–16: confirmed theft/loss write-off process — LPO documents with evidence, police report for theft, tiered approval per loss value (Store Manager ≤ PHP 10K, Regional Manager ≤ PHP 50K, Controller ≤ PHP 500K, CFO+CEO > PHP 500K), GL write-off posting (Dr. Inventory Loss / Cr. Inventory), insurance claim integration per W3.6a, quarterly shrinkage reporting link. Added system touchpoints. |

---

## C. Detail Gaps in Existing Workflows

### C1. ✅ Resolved — Transfer Order Receipt Discrepancy Resolution

| Attribute | Detail |
|---|---|
| **Source** | W22.9 |
| **Gap** | W22.9 flagged discrepancies but didn't describe the financial resolution: Who bears the cost of lost/damaged goods in transit? Does the destination write off? Does the source get debited? Is there a carrier claim? |
| **Resolution** | ✅ Added step W22.9a with three resolution paths: (a) source picking error → source absorbs loss with GL posting at source; (b) carrier damage → insurance claim per W3.6a; (c) unexplained → destination writes off with tiered approval and GL posting. Added system touchpoints. |

### C2. ✅ Resolved — Intercompany Invoice from Transfer Order

| Attribute | Detail |
|---|---|
| **Source** | W14 (IC Transactions), W22 (Stock Transfers) |
| **Gap** | W14 described IC invoice generation and W22 described transfers, but the trigger linking TO receipt confirmation to IC invoice generation wasn't explicit. When a DC (Logistics Inc.) transfers goods to a store (Depot Inc.), the system must auto-generate an IC invoice at the configured transfer price. |
| **Resolution** | ✅ Added cross-reference in W22 system touchpoints: for inter-entity transfers, system auto-generates IC invoice at configured transfer price upon receipt confirmation (W22.8 → W14.1); IC AP/AR posted simultaneously per W14; transfer pricing rules maintained per annual IC review. |

### C3. ✅ Resolved — WAC Recalculation Timing Clarification

| Attribute | Detail |
|---|---|
| **Source** | INV-003 (WAC), W9a.6 |
| **Gap** | W9a.6 said "Run monthly inventory valuation (WAC)" which implied periodic recalculation. Philippine retail standard is perpetual WAC (moving average recalculated at each receipt). The month-end step is verification/reconciliation, not recalculation. |
| **Why It Matters** | WAC methodology is a fundamental ERP design decision. If perpetual (standard in Philippine retail), the month-end step is reconciliation. If periodic, interim COGS may differ. Evaluators need clarity. |
| **Resolution** | ✅ Updated W9a.6 to "Verify perpetual WAC (weighted average cost) calculations; post adjustments from cycle counts." Added step W9a.6a explaining perpetual methodology: new WAC = (prior inventory value + receipt value) ÷ (prior quantity + receipt quantity) at each GR; COGS at POS uses current WAC; month-end is sampling, reconciliation, and adjustment posting. Added WAC recalculation to W3.7 system touchpoints. Updated W9a inventory valuation engine touchpoint. |

---

## D. Cross-Document Consistency Check

All numerical checks from Waves 1–5 re-verified plus additional checks:

| Check | Result |
|---|---|
| POS volume: profile §5 vs. W5b vs. data volumes §1.1 | ✅ All say 2.8M transactions/month |
| Revenue: profile §9.4 split vs. W5b volume | ✅ PHP 4.89B + PHP 150M = PHP 5.04B in-store + PHP 150M ecommerce = PHP 5.19B total |
| Headcount: profile §4 vs. §12.1 + §3.2 + §3.3 | ✅ 7,000 + 750 + 300 = 8,050 |
| AP volume: profile §10.2 vs. W7 vs. data volumes | ✅ All ~6,500/month |
| W19 order volume: 17,200/month ÷ 30 = 573/day | ✅ Correct |
| **W19 per-DC volume: 573 ÷ 5 = 115/DC/day** | ✅ **Fixed (was incorrectly 23)** |
| DC staffing: updated pick/pack validates against 150/DC | ✅ Absorbed but significant |
| DSD volume: profile §7.1 vs. W18 | ✅ ~500–600/month |
| Ecommerce: profile §8.5 vs. W11 + W19 | ✅ 25,700 + 17,200 = 42,900 |
| Cycle count: W6 vs. profile §12.2 | ✅ Consistent |
| Intercompany flows: profile §2 vs. W14 | ✅ All 6 flows covered |

---

## E. Non-Blocking Items (Acknowledged)

| # | Item | Reason |
|---|---|---|
| NB1 | Batch processing failure handling | IT operations runbook (acknowledged since Wave 1) |
| NB2 | Integration monitoring / incident response | IT operations runbook (acknowledged since Wave 1) |
| NB3 | Data migration strategy (NFR-014) | Project-phase activity (acknowledged since Wave 1) |
| NB4 | Employee performance review / merit increase | Typically handled by separate HRIS |
| NB5 | Training management & tracking | Typically handled by separate LMS |
| NB6 | Ecommerce inventory allocation priority (BOPIS vs. delivery) | ATP configuration design point, not a separate workflow |
| NB7 | BIR CAS registration | One-time regulatory filing |
| NB8 | BIR e-invoicing readiness | Emerging regulation; no clear mandate date |
| NB9 | Peak load calendar not reflected in workflows | Implementation-phase concern |
| NB10 | Sales commission / incentive tracking | May be handled in payroll or outside ERP |

---

## F. Recommendations Priority Matrix (All Resolved)

| Priority | Gap ID | Action | Status |
|---|---|---|---|
| 🔴 **P1** | A1 (W19 staffing) | Fix arithmetic; reassess DC staffing for home delivery | ✅ Done |
| 🟡 **P2** | B1 (LBT) | Add LBT compliance step to W9a | ✅ Done |
| 🟡 **P2** | B2 (Customer credit) | Add customer credit memo to W8 | ✅ Done |
| 🟡 **P2** | B3 (Vendor-funded promo) | Add vendor-funded promo settlement to W13 | ✅ Done |
| 🟡 **P2** | B4 (Reverse logistics) | Add reverse pickup to W19 + cross-ref W12 | ✅ Done |
| 🟡 **P2** | B6 (Theft write-off) | Add theft write-off process to W37 | ✅ Done |
| 🟢 **P3** | B5 (Cash-in-transit) | Add cash logistics steps to W5c | ✅ Done |
| 🟢 **P3** | C1 (Transfer discrepancy) | Add financial resolution to W22.9a | ✅ Done |
| 🟢 **P3** | C2 (IC from TO) | Add cross-reference W22 → W14 | ✅ Done |
| 🟢 **P3** | C3 (WAC timing) | Clarify perpetual WAC in W9a.6 | ✅ Done |

---

## G. Summary

All 10 Wave 6 gaps resolved through the following changes:

1. **Fixed numerical error**: W19 staffing corrected from ~23 to ~115 orders/DC/day, labor from ~6 to ~29 hours/DC/day
2. **New steps**: W5c.5a–b (cash-in-transit), W8.11 (customer credit memo), W9a.6a (WAC methodology), W9a.16c (LBT per LGU), W19.12a (reverse logistics), W22.9a (transfer discrepancy resolution), W37.11–16 (confirmed theft write-off)
3. **New system touchpoints**: W5c (cash-in-transit tracking), W8 (customer credit memo), W9a (LBT calendar, WAC perpetual verification), W12 (reverse logistics cross-ref), W13 (vendor-funded promo settlement), W19 (reverse logistics), W22 (IC invoice trigger, discrepancy resolution), W30 (cash-in-transit confirmation), W37 (theft write-off)
4. **Updated module map**: Expanded Financials, Inventory, Ecommerce, Loss Prevention, and Pricing/Merchandising entries

### What Changed vs. Previous Waves

Previous waves focused on **coverage completeness** (does every requirement have a supporting
workflow?) and **accounting depth** (GL postings, accruals, PFRS compliance). They achieved
excellent results. Wave 6 found fewer structural gaps and more **operational edge cases**
(reverse logistics for bulky returns, vendor-funded promos, LBT compliance, cash-in-transit,
theft write-off) and **numerical accuracy** (W19 staffing error). The gaps are narrower and
more specialized than earlier waves, confirming diminishing returns from further analysis.

### Overall Assessment

**The workflow documentation is comprehensive and ready for ERP vendor evaluation.**
All 130+ requirements have supporting workflow coverage with actionable process steps,
system touchpoints, staffing implications, and GL postings. The remaining non-blocking items
are operational concerns to be addressed during implementation design.

| Metric | v8.0 (Pre-Wave 6) | v9.0 (After Wave 6) |
|---|---|---|
| Total workflows | 49 | **49** |
| Requirements fully covered | ~130 (99%) | **~130 (99%)** |
| Requirements partially covered | ~1 (1%) | **~1 (1%)** |
| Requirements not covered | 0 (0%) | **0 (0%)** |
| Total gaps resolved (all waves) | 52 | **62** |
| Non-blocking carried forward | 2 | 2 |

---

*Document Version: 1.0 | Date: 2026-05-30 | Wave 6: 10 gaps identified; all 10 resolved*
