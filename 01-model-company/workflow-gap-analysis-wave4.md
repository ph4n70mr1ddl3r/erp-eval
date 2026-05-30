# Workflow Gap Analysis — Wave 4 (Independent Review)

> An independent, from-scratch gap analysis cross-referencing all 48 operational workflows
> (`operational-workflows.md`) against the ERP requirements (`erp-requirements.md`),
> company profile (`model-company-profile.md`), and data volumes
> (`data-volumes-and-integrations.md`). This review specifically targets gaps that
> Waves 1–3 may have missed — focusing on accounting completeness, operational edge cases,
> and process-to-requirement traceability gaps.

---

## Executive Summary

The 47 workflows (pre-Wave 4) provided strong coverage of the end-to-end retail value chain.
Waves 1–3 resolved 25 gaps and achieved ~99% requirement coverage.

This Wave 4 independent review identified **12 remaining gaps** — 4 HIGH priority,
6 MEDIUM priority, and 2 LOW priority. **All 12 gaps have been resolved.**

| Gap Category | Count | Status |
|---|---|---|
| **A. Requirements with insufficient workflow coverage** | 4 | ✅ All 4 resolved |
| **B. Business activities referenced but not workflowed** | 6 | ✅ All 6 resolved |
| **C. Detail gaps in existing workflows** | 2 | ✅ All 2 resolved |

| Metric | Before Wave 4 | After Resolution |
|---|---|---|
| Total workflows | 47 | **48** (+W46 Kit Assembly) |
| Requirements fully covered | ~130 (99%) | **~130 (99%)** |
| Open gaps | 0 claimed | 12 found → **0 remaining** |

---

## Resolved Gaps

### G1. ✅ Resolved — Expanded Withholding Tax (EWT) in AP Payment

| Attribute | Detail |
|---|---|
| **Req ID** | FIN-007 (Withholding Tax — Expanded) |
| **Gap** | No workflow step described EWT computation at vendor payment time or subsequent BIR remittance. With ~6,500 AP invoices/month and PHP 41–43B annual COGS, EWT (1–10% per ATC) is a material cash flow and compliance matter. |
| **Resolution** | ✅ Added step W7.9a (EWT computation per vendor ATC, net payment calculation, EWT Payable posting). Added step W9a.16a (EWT remittance: BIR 1601-E file generation, eFPS transmission, reconciliation). Added system touchpoints for both. |

### G2. ✅ Resolved — Inventory Write-Down / NRV Provision (IAS 2 / PFRS)

| Attribute | Detail |
|---|---|
| **Req ID** | INV-011 (Inventory Aging Analysis), FIN-003 (PFRS/IFRS compliant) |
| **Gap** | No workflow described the periodic process of identifying slow-moving inventory requiring write-down to net realizable value per PFRS/IAS 2. With PHP 4–6B in inventory, this is material. |
| **Resolution** | ✅ Added step W9a.16b (Inventory NRV review): Cost Accountant runs aging by days-since-last-sale; system compares WAC to estimated NRV; write-down proposed and approved per tier; GL posting (Dr. Write-Down Expense / Cr. Inventory Provision); provision reversal on subsequent sale above written-down value. Added system touchpoints. |

### G3. ✅ Resolved — Loyalty Points Deferred Revenue Liability

| Attribute | Detail |
|---|---|
| **Req ID** | CRM-001 (Loyalty Points Engine), FIN-003 (PFRS/IFRS compliant) |
| **Gap** | No workflow described PFRS 15/IFRS 15 accounting for loyalty points as deferred revenue. With 600K members and 2.8M transactions/month, this is a material balance sheet item. |
| **Resolution** | ✅ Expanded W17 step 4 (revenue allocation at earning: Cr. Deferred Revenue — Loyalty Points), step 7 (proportional recognition at redemption: Dr. Deferred Revenue / Cr. Revenue), step 11 (breakage recognition at expiry). Added step 11a (monthly liability estimation and reconciliation by Cost Accountant). Added system touchpoints for deferred revenue lifecycle. |

### G4. ✅ Resolved — Multi-Tender Payment Reconciliation at Store Close

| Attribute | Detail |
|---|---|
| **Req ID** | POS-004 (Multi-Tender), POS-009 (EOD Reconciliation) |
| **Gap** | W5c only reconciled cash. No reconciliation of card (36%) and e-wallet (15%) payments against settlement reports. |
| **Resolution** | ✅ Added steps W5c.3a (system auto-imports electronic payment settlement reports; compares to Z-report by tender type) and W5c.3b (variance flagging and investigation). Added system touchpoints for electronic payment reconciliation. |

### G5. ✅ Resolved — Kit / Bundle Assembly & Disassembly

| Attribute | Detail |
|---|---|
| **Gap** | Profile §6.4 lists "Kit / Bundle" as an item type. No workflow described BOM definition, assembly orders, component consumption, or disassembly. |
| **Resolution** | ✅ Added **W46: Kit / Bundle Assembly & Disassembly** — 9 steps covering: BOM definition, assembly order generation (demand-driven or batch), component picking and consumption, kit creation with automatic costing, and disassembly reversal. Full system touchpoints and staffing implications included. |

### G6. ✅ Resolved — Vendor Credit Memo Processing

| Attribute | Detail |
|---|---|
| **Gap** | No general vendor credit memo process: receiving a credit note, matching to source (RTV, rebate, price protection), and applying to vendor balance. |
| **Resolution** | ✅ Added step W7.9b (vendor credit memo processing): AP Clerk receives credit note, selects source, system auto-matches to original transaction, posts GL entry, applies to open invoices. Added system touchpoints. |

### G7. ✅ Resolved — Price Protection / Retroactive Cost Adjustment

| Attribute | Detail |
|---|---|
| **Gap** | W40 covered forward-looking cost increases. No workflow for retroactive vendor price reductions (price protection) — common for commodity-linked categories. |
| **Resolution** | ✅ Added **Price Protection / Retroactive Cost Adjustment** sub-section to W40 (steps 11–14): Buyer enters price protection notice, system calculates retroactive credit, revalues on-hand inventory, triggers SRP review. Added system touchpoints. |

### G8. ✅ Resolved — Forward-Pick Zone Replenishment in DC

| Attribute | Detail |
|---|---|
| **Gap** | No workflow described internal DC replenishment from reserve/bulk storage to forward-pick locations. |
| **Resolution** | ✅ Added DC forward-pick zone replenishment system touchpoint to W3: system monitors forward-pick quantities, generates replenishment tasks when below minimum, RF-directed moves from reserve to forward-pick, prioritized ahead of picking waves. |

### G9. ✅ Resolved — Promotional vs. Regular Price Conflict Resolution

| Attribute | Detail |
|---|---|
| **Gap** | No rules defined for when regular price changes and promotional prices overlap for the same SKU. |
| **Resolution** | ✅ Added pricing conflict resolution rules to W13 system touchpoints: (1) promo overrides regular during promo period, (2) alerts Pricing Analyst if base price changed since promo setup, (3) lower price wins on overlap, (4) post-promo reverts to CURRENT regular price. |

### G10. ✅ Resolved — Credit Hold Override for Trade/Corporate Accounts

| Attribute | Detail |
|---|---|
| **Gap** | W8.3 blocked over-limit sales but no controlled override process existed for trusted customers. |
| **Resolution** | ✅ Added step W8.3a: credit hold override with tiered authorization (AR Supervisor up to 110%, Finance Manager up to 130%), audit trail, 24-hour validity, and credit exposure tracking. Added system touchpoint. |

### G11. ✅ Resolved — Sample / Demo Inventory Management

| Attribute | Detail |
|---|---|
| **Gap** | Display items (tile galleries, appliance demos, tool displays) not tracked — become "ghost inventory." |
| **Resolution** | ✅ Added sample/demo inventory management note to W1 system touchpoints: system supports 'Sample/Demo' inventory status, excluded from available stock and replenishment, quarterly review for markdown/return/scrap. |

### G12. ✅ Resolved — Store-Level GRNI Follow-Up (DSD)

| Attribute | Detail |
|---|---|
| **Gap** | No explicit assignment of store-level responsibility for DSD GRNI follow-up at month-end. |
| **Resolution** | ✅ Added DSD GRNI follow-up note to W18 system touchpoints: AP Clerk contacts the store Receiving Clerk who processed the original GR to confirm received quantities and resolve discrepancies. |

---

## Cross-Document Consistency Check

No numerical inconsistencies were found across documents. Specific validations:

| Check | Result |
|---|---|
| POS volume: profile §5 vs. W5b vs. data volumes §1.1 | ✅ All say 2.8M transactions/month |
| Revenue: profile §9.4 split vs. W5b volume | ✅ PHP 4.89B + PHP 150M = PHP 5.04B |
| Headcount: profile §4 vs. §12.1 + §3.2 + §3.3 | ✅ 7,000 + 750 + 300 = 8,050 |
| AP volume: profile §10.2 vs. W7 vs. data volumes | ✅ All ~6,500/month |
| Store replenishment: profile §7.2 vs. W4 vs. data volumes | ✅ All ~5,000/month |
| DSD volume: profile §7.1 vs. W18 vs. data volumes | ✅ ~500–600/month |
| Ecommerce: profile §8.5 vs. W11 + W19 | ✅ 25,700 + 17,200 = 42,900 |
| DC count: profile §3.2 vs. W3 vs. W4 | ✅ Consistent |
| Cycle count: W6 vs. profile §12.2 | ✅ Consistent |
| Intercompany flows: profile §2 vs. W14 | ✅ All 6 flows covered |

---

## Summary

All 12 Wave 4 gaps resolved through the following changes:

1. **New workflow**: W46 (Kit Assembly & Disassembly)
2. **New sub-section**: W40 Price Protection / Retroactive Cost Adjustment (steps 11–14)
3. **New steps**: W5c.3a–b (multi-tender recon), W7.9a (EWT), W7.9b (credit memos), W8.3a (credit hold override), W9a.16a (EWT remittance), W9a.16b (NRV review), W17.11a (loyalty liability reconciliation)
4. **Expanded steps**: W17.4 (deferred revenue at earning), W17.7 (recognition at redemption), W17.11 (breakage at expiry)
5. **New system touchpoints**: W1 (sample/demo), W3 (forward-pick replenishment), W7 (EWT, credit memos), W8 (credit hold override), W9a (EWT remittance, NRV review), W13 (pricing conflict rules), W17 (deferred revenue lifecycle), W18 (DSD GRNI follow-up), W40 (price protection)
6. **Updated module map**: W46 added to Inventory, WMS, and Master Data modules; expanded descriptions for Financials, Pricing, and WMS modules

Total workflows now: **48** (W1–W46 + W2c + W3b + W5d)

---

*Document Version: 1.1 | Date: 2026-05-30 | All 12 Wave 4 gaps resolved*
