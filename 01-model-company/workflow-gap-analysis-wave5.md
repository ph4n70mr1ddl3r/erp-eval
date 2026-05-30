# Workflow Gap Analysis — Wave 5 (Independent Review)

> A fresh, independent gap analysis cross-referencing all 48 operational workflows
> (`operational-workflows.md`) against the ERP requirements (`erp-requirements.md`),
> company profile (`model-company-profile.md`), and data volumes
> (`data-volumes-and-integrations.md`). This Wave 5 review targets gaps that
> Waves 1–4 missed — specifically: cross-document numerical inconsistencies,
> operational processes that no workflow describes, detail gaps in high-impact
> workflows, and requirements whose workflow coverage is nominal but insufficient
> for ERP evaluators to assess fit.

---

## Executive Summary

Waves 1–4 resolved 37 gaps and achieved strong operational coverage of the retail
value chain. This Wave 5 review identified **15 remaining gaps**: 1 cross-document
numerical inconsistency, 10 business activities without workflows, 3 detail gaps
in existing workflows, and 1 requirement with insufficient coverage.

**All 15 gaps have been resolved.**

| Gap Category | Count | Status |
|---|---|---|
| **A. Cross-document inconsistency** | 1 | ✅ Resolved |
| **B. Business activities with no workflow** | 10 | ✅ All 10 resolved |
| **C. Detail gaps in existing workflows** | 3 | ✅ All 3 resolved |
| **D. Requirements with insufficient coverage** | 1 | ✅ Resolved |

| Metric | Wave 4 Claimed | After Wave 5 Resolution |
|---|---|---|
| Total workflows | 48 | **49** (48 + W7c) |
| Cross-document inconsistencies | 0 claimed | **1 found → 0 remaining** |
| Business activities without workflows | 0 claimed | **10 found → 0 remaining** |
| Detail gaps | 0 claimed | **3 found → 0 remaining** |

---

## A. Cross-Document Inconsistency

### A1. ✅ Resolved — POS ATV × Transaction Count vs. Revenue Split

| Location | Value |
|---|---|
| Profile §5 | Monthly POS Transactions: 2,800,000; ATV: PHP 1,800 |
| Profile §9.4 (before fix) | In-Store: PHP 4.89B + Ecommerce: PHP 150M = Total: PHP 5.04B |
| Calculation | 2,800,000 × PHP 1,800 = PHP 5.04B (in-store POS revenue) |
| Problem | POS × ATV = PHP 5.04B but total was also stated as PHP 5.04B. The in-store revenue alone equals PHP 5.04B, so total including ecommerce should be PHP 5.19B. |

**Resolution**: ✅ Updated model company profile §9.4: POS transactions (2,800,000 × PHP 1,800) = PHP 5.04B in-store revenue. Ecommerce adds PHP 150M. **Total monthly revenue = PHP 5.19B**. Ecommerce = 2.9% of total. Annual revenue updated to ~PHP 62.3B. COGS updated to ~PHP 42–45B. Updated ecommerce penetration target note in §8.5 to match.

---

## B. Business Activities With No Workflow

### B1. ✅ Resolved — Recurring Store Expense Processing

| Attribute | Detail |
|---|---|
| **Gap** | No workflow for store-level recurring expenses (electricity, water, internet, rent, security, cleaning, waste disposal) — ~2,000–3,000 non-PO invoices/month. W7 only covered PO-based 3-way match. |
| **Resolution** | ✅ Added **W7c: Non-PO / Recurring Expense Invoice Processing** sub-workflow: utility bills and service invoices received without POs; 2-way match (invoice vs. contract/budget); cost center owner approval routing (Store Manager for store expenses, Department Head for HQ); variance flagging; EWT computation for service invoices; monthly expense summary review by AP Supervisor. Added system touchpoints. |

### B2. ✅ Resolved — Shelf-Life / Expiry Date Management

| Attribute | Detail |
|---|---|
| **Gap** | ~5,000 SKUs (paint, adhesives, cement, chemicals) have limited shelf life but no workflow described expiry tracking, FEFO picking, or near-expiry disposition. |
| **Resolution** | ✅ Added shelf-life/expiry management to W3 (capture manufacturing date and shelf-life at GR, expiry date per batch, expiry flagging), W4 (FEFO-directed pick sequence in DC), W6 (near-expiry alerting during cycle counts with disposition workflow linking to W13.9a and W3.6a), and W18 (DSD receiving: shelf-life capture). |

### B3. ✅ Resolved — Ecommerce Payment Reconciliation

| Attribute | Detail |
|---|---|
| **Gap** | PHP 150M/month through multiple payment gateways (PayMongo, Dragonpay, GCash, Maya) with no reconciliation workflow. |
| **Resolution** | ✅ Added ecommerce payment reconciliation to W19 system touchpoints: system imports daily settlement reports from each gateway; matches to individual orders; reconciles gross payments, gateway fees, chargebacks, and refunds; posts gateway fees to GL; Treasury verifies bank deposits daily as part of W30. |

### B4. ✅ Resolved — Slow-Mover / Dead Stock Operational Review

| Attribute | Detail |
|---|---|
| **Gap** | W9a.16b covered the accounting (NRV write-down) but no operational cross-functional review existed for ~3,500–5,000 slow-moving SKUs. |
| **Resolution** | ✅ Added **Slow-Mover / Dead Stock Operational Review** to W1 system touchpoints: monthly review by Category Managers, Supply Planner, and Cost Accountant; system-generated report (> 90 days since last sale, < 2 turns/year, stock > 6 months demand); disposition decisions per SKU; results feed into quarterly assortment review (W1) and accounting NRV write-down (W9a.16b). |

### B5. ✅ Resolved — Negative Inventory Resolution

| Attribute | Detail |
|---|---|
| **Gap** | Multiple workflows reference negative inventory scenarios but no standard investigation and resolution process was documented. |
| **Resolution** | ✅ Added **Negative Inventory Resolution** to W1 system touchpoints: daily negative inventory alert per SKU-location; investigation by Stock Associate (store) or Inventory Control (DC); resolution actions (recount and adjust, wait for pending transaction, force adjustment with supervisor approval); system blocks negative-inventory locations from ecommerce ATP; monthly frequency report. |

### B6. ✅ Resolved — 3PL / Delivery Partner Management

| Attribute | Detail |
|---|---|
| **Gap** | W19 referenced delivery partners for individual orders but no ongoing 3PL relationship management. 80% of outbound fleet is third-party. |
| **Resolution** | ✅ Added 3PL management to W19 system touchpoints: carrier master with rate cards and SLA terms; automated carrier selection by zone/weight/cost; carrier performance dashboard (on-time %, damage %, cost per delivery); monthly carrier invoice reconciliation; quarterly carrier performance review similar to W44. |

### B7. ✅ Resolved — DC-to-DC Systematic Replenishment Planning

| Attribute | Detail |
|---|---|
| **Gap** | W31 worked at DC level but didn't describe the sourcing decision (internal transfer vs. external PO) when a DC runs low. |
| **Resolution** | ✅ Expanded W31 system touchpoints with **multi-echelon DC replenishment sourcing**: when DC inventory drops below ROP, system evaluates available stock at other DCs, transfer cost/lead time vs. vendor PO cost/lead time; recommends optimal source; auto-generates Transfer Order (W22) or suggested PO (W2a). |

### B8. ✅ Resolved — Customer Loyalty Points Manual Adjustment

| Attribute | Detail |
|---|---|
| **Gap** | W17 covered automated earning/redemption but not manual corrections, goodwill adjustments, or dispute resolution — ~2,800–14,000 adjustments/month. |
| **Resolution** | ✅ Added manual points adjustment to W17 system touchpoints: authorized CSR or Loyalty Manager initiates with reason code; tiered approval (> 500 points: Loyalty Manager; > 5,000: Marketing Head); full audit trail; monthly audit of all adjustments. |

### B9. ✅ Resolved — Consignment Goods Return to Vendor

| Attribute | Detail |
|---|---|
| **Gap** | W23 step 10 mentioned "returns slow movers to vendor" but didn't describe the logistics or system processing of returning vendor-owned goods. |
| **Resolution** | ✅ Expanded W23 step 10 with full consignment return detail: Buyer identifies slow movers; coordinates pickup; Receiving Clerk processes return shipment (reduces non-valuated consignment inventory, no GL posting since vendor-owned); vendor issues updated stock list; system updates on-hand quantities. Added system touchpoint. |

### B10. ✅ Resolved — Customer Deposit Aging / Unclaimed Deposits

| Attribute | Detail |
|---|---|
| **Gap** | W38 tracked customer deposits for special orders but no process for when customers never return — deposits remain as liability indefinitely. |
| **Resolution** | ✅ Added step W38.15 (unclaimed deposit management): system tracks deposit age from goods-receipt date; automated reminder at 30 days; escalation flag at 90 days; abandonment recognition with approval (Dr. Customer Deposits Payable / Cr. Other Income); goods dispositioned per existing clearance/RTV workflows. Added system touchpoint. |

---

## C. Detail Gaps in Existing Workflows

### C1. ✅ Resolved — W12 (Returns): Split-Tender Refund Processing

| Attribute | Detail |
|---|---|
| **Gap** | W12a.6 said "refund to original tender" but didn't address split-tender refunds (e.g., customer paid PHP 1,000 cash + PHP 800 card). |
| **Resolution** | ✅ Updated W12a.6: for split-tender transactions, system refunds pro-rata to each original tender method; if cash refund exceeds store cash availability threshold, system defaults to card or e-wallet for excess; Store Manager can override with authorization. Added system touchpoint. |

### C2. ✅ Resolved — W5b (POS): Void Transaction Process

| Attribute | Detail |
|---|---|
| **Gap** | W37 monitored voids for fraud but no operational void process was documented — one of the highest-risk POS operations. |
| **Resolution** | ✅ Added step W5b.10 (void transaction): Cashier or Store Manager initiates void; manager authorization required; system logs with cashier ID, manager ID, original transaction number, reason code, timestamp; system reverses inventory, payment, loyalty points, and promo usage; voided transaction retained in full audit trail. Added system touchpoint. |

### C3. ✅ Resolved — W16 (New Store Opening): Budget and Cost Tracking

| Attribute | Detail |
|---|---|
| **Gap** | Each store opening is a PHP 15–30M capex project (10–15/year = PHP 150–450M) but no project-level cost tracking was described. |
| **Resolution** | ✅ Added capex project tracking to W16 system touchpoints: each store opening tracked as a capex project; all POs, invoices, and expenses tagged to project code; Cost Accountant tracks actual vs. budgeted cost per project; post-opening review includes cost variance analysis; total cost capitalized per W21.7. |

---

## D. Requirements With Insufficient Workflow Coverage

### D1. ✅ Resolved — MDM-003: Customer Data Quality — Deduplication

| Attribute | Detail |
|---|---|
| **Req ID** | MDM-003 |
| **Requirement** | Customer Data Quality — deduplication, validation rules for 600K+ customer records |
| **Gap** | No workflow for identifying, preventing, or merging duplicate customer records across 600K+ loyalty members. |
| **Resolution** | ✅ Added customer data deduplication to W17 system touchpoints: fuzzy-match deduplication at enrollment (> 85% match on name + phone or name + email blocks creation); weekly deduplication queue for Loyalty Manager review; merge with points consolidation; monthly data quality dashboard (duplicate rate, incomplete records, invalid contact info). |

---

## E. Recommendations Priority Matrix (All Resolved)

| Priority | Gap ID | Action | Status |
|---|---|---|---|
| 🔴 **P1** | A1 (ATV inconsistency) | Fix profile §5 and §9.4 numerical consistency | ✅ Done |
| 🟡 **P2** | B1 (Recurring expenses) | Add non-PO AP sub-section W7c | ✅ Done |
| 🟡 **P2** | B2 (Shelf-life/expiry) | Add expiry management to W3, W4, W6, W18 | ✅ Done |
| 🟡 **P2** | B4 (Slow-mover review) | Add operational slow-mover review to W1 | ✅ Done |
| 🟡 **P2** | C1 (Split-tender refund) | Add split-tender refund detail to W12 | ✅ Done |
| 🟡 **P2** | C2 (Void process) | Add void transaction step W5b.10 | ✅ Done |
| 🟡 **P2** | B3 (Ecom payment recon) | Add ecommerce payment reconciliation to W19 | ✅ Done |
| 🟢 **P3** | B5 (Negative inventory) | Add negative inventory resolution to W1 | ✅ Done |
| 🟢 **P3** | B6 (3PL management) | Add 3PL management notes to W19 | ✅ Done |
| 🟢 **P3** | B7 (DC-to-DC planning) | Expand W31 with multi-echelon sourcing | ✅ Done |
| 🟢 **P3** | B8 (Points adjustment) | Add manual adjustment steps to W17 | ✅ Done |
| 🟢 **P3** | B9 (Consignment return) | Expand W23 step 10 | ✅ Done |
| 🟢 **P3** | B10 (Deposit aging) | Add unclaimed deposit step W38.15 | ✅ Done |
| 🟢 **P3** | C3 (Store budget tracking) | Add project tracking note to W16 | ✅ Done |
| 🟢 **P3** | D1 (Customer dedup) | Add dedup process to W17 | ✅ Done |

---

## F. Updated Workflow-to-Requirement Coverage

No requirement changed status from ✅ to ❌. All gaps were additive detail
or new sub-workflows. All 130+ requirements remain covered.

---

## G. Non-Blocking Items (Acknowledged, Outside This Review)

| # | Item | Reason |
|---|---|---|
| NB1 | BIR CAS registration | One-time regulatory filing |
| NB2 | BIR e-invoicing readiness | Emerging regulation; no clear mandate date |
| NB3 | Business continuity / DR testing | IT operations concern |
| NB4 | Ongoing user training / change management | Post-go-live concern |
| NB5 | Fleet / fuel / vehicle management | May be outside ERP scope |
| NB6 | Sales commission / incentive tracking | May be handled in payroll or outside ERP |
| NB7 | Competitive price monitoring | Typically done manually or via separate tools |
| NB8 | Data migration strategy (NFR-014) | Project-phase activity (acknowledged since Wave 1) |
| NB9 | Integration monitoring / incident response | IT operations runbook (acknowledged since Wave 1) |
| NB10 | Batch processing failure handling | IT operations concern (acknowledged since Wave 1) |

---

*Document Version: 1.1 | Date: 2026-05-30 | Wave 5: 15 gaps identified; all 15 resolved*
