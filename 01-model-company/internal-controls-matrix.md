# BuildRight Depot Corp. — Internal Controls Matrix

> Defines the key internal controls embedded in the ERP system and operational processes.
> Organized by control objective. Each control references the workflows that implement it.
> This matrix complements the operational workflows and ERP requirements — it does not
> replace them but provides an auditable controls framework.

---

## How to Read This Matrix

| Field | Meaning |
|---|---|
| **Control ID** | Unique identifier (CTL-XX) |
| **Control Objective** | What the control prevents or detects |
| **Control Type** | Preventive (P) or Detective (D) |
| **Control Activity** | What is done |
| **Owner** | Role accountable for the control |
| **Workflows** | Where this control is exercised |
| **ERP Requirement** | Supporting requirement from erp-requirements.md |

---

## C1. Authorization & Approval Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-01 | Prevent unauthorized purchases | P | PO approval per tiered matrix (> PHP 50K → Category Manager, > PHP 500K → VP, > PHP 2M → CFO for imports) | Category Manager / VP / CFO | W2a.5–6, W2b.2 | PUR-010 |
| CTL-02 | Prevent unauthorized capital expenditure | P | Capex request approval per tiered matrix (> PHP 100K → Finance Mgr, > PHP 500K → CFO, > PHP 5M → CEO, > PHP 5M → Board) | CFO / CEO / Board | W21.4 | FIN-016 |
| CTL-03 | Prevent unauthorized price overrides at POS | P | System requires manager authorization for price overrides > 10% or > PHP 500; logs override with cashier ID, manager ID, reason code | Store Manager | W5b.4a | POS-006 |
| CTL-04 | Prevent unauthorized transaction voids | P | Manager authorization required for all voids; system logs void with cashier ID, manager ID, reason, timestamp; queued void authorization if no manager available | Store Manager | W5b.10 | POS-006 |
| CTL-05 | Prevent unauthorized credit limit overrides | P | Credit hold override requires tiered approval (AR Supervisor ≤ 110%, Finance Mgr ≤ 130%); 24-hour validity; logged with authorizer and reason | AR Supervisor / Finance Manager | W8.3a | CRM-003 |
| CTL-06 | Prevent unauthorized vendor onboarding | P | Category Manager approval required for vendor master creation; Finance validates TIN and business permit; system blocks expired-document vendors from POs | Category Manager / AP Clerk | W36.5, W36 vendor doc tracking | PUR-003, MDM-004 |
| CTL-07 | Prevent unauthorized pricing changes | P | Price changes require Category Manager approval; VP Merchandising approves if aggregate impact > PHP 500K/month | Category Manager / VP | W40.5, W13.3 | MDM-005 |
| CTL-08 | Prevent unauthorized promotional pricing | P | VP Merchandising approves all promotional pricing before push to POS | VP Merchandising | W13.3 | POS-014 |

## C2. Segregation of Duties Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-09 | Separate purchasing from receiving | P | Buyer creates PO; Receiving Clerk processes GR; system validates 3-way match (PO → GR → Invoice) | Buyer / Receiving Clerk / AP Clerk | W2a, W3, W7.2 | PUR-005, FIN-004 |
| CTL-10 | Separate payment initiation from approval | P | AP Clerk generates payment file; Treasury Analyst reviews and approves; CFO authorizes | AP Clerk / Treasury / CFO | W7.9–10 | FIN-004 |
| CTL-11 | Separate inventory counting from adjustment approval | P | Stock Associate counts; Department Supervisor reviews; Store Manager approves adjustments > PHP 10K | Stock Associate / Dept. Supervisor / Store Manager | W6.6–7 | INV-006 |
| CTL-12 | Separate credit approval from sales execution | P | AR Clerk/Credit Committee approves credit; Cashier executes sale; system enforces approved limit | AR Clerk / Cashier | W24.5, W8.3 | CRM-008 |
| CTL-13 | Separate payroll computation from approval | P | Payroll Officer computes; Payroll Manager approves; Treasury transmits to bank | Payroll Officer / Payroll Mgr / Treasury | W10.5–8 | HR-001 |

## C3. Transaction Integrity Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-14 | Ensure AP invoices match PO and GR | P | 3-way match engine auto-approves within tolerance; exceptions routed to AP Clerk; unresolved exceptions escalated at day 5 | AP Supervisor | W7.2–6, W7.6a–b | FIN-004, PUR-005 |
| CTL-15 | Ensure accurate landed cost on imports | D | System auto-calculates landed cost from duty, freight, insurance at GR; Finance reconciles actual vs. estimated | Cost Accountant | W2b.12–13 | FIN-013 |
| CTL-16 | Ensure perpetual WAC accuracy | D | Cost Accountant verifies WAC at month-end by sampling high-value/high-volume SKUs; reconciles total inventory valuation to GL | Cost Accountant | W9a.6a | INV-003 |
| CTL-17 | Ensure GRNI completeness | D | Weekly GRNI aging report; items > 30 days flagged for Buyer follow-up; > 60 days escalated; > 90 days reviewed for accrual | AP Supervisor / Controller | W7 GRNI aging | FIN-004 |
| CTL-18 | Ensure IC balance agreement | D | Monthly IC reconciliation across all entity pairs; mismatches resolved before consolidation | Chief Accountant | W14.4–5 | IC-005 |
| CTL-19 | Ensure bank reconciliation completeness | D | Daily bank statement import; Treasury auto-matches deposits; monthly full reconciliation per entity | Treasury Analyst / Controller | W30.2, W30.9 | FIN-009 |
| CTL-20 | Ensure POS cash accountability | D | Daily Z-report vs. physical cash count; variance > PHP 200 investigated and documented; electronic payment settlement auto-reconciled | Store Manager | W5c.2–4 | POS-009 |
| CTL-21 | Ensure inventory accuracy | D | Cycle counting with blind recounts; quarterly full coverage; adjustments require tiered approval; accuracy target ≥ 97% | Dept. Supervisor / Store Manager | W6, W42 | INV-006, INV-007 |
| CTL-22 | Ensure correct VAT computation | D | System auto-computes VAT per transaction; VAT-exempt/zero-rated customers classified in customer master with supporting docs; monthly VAT return reconciliation | Tax Accountant | W5b.4c, W9a.16 | FIN-006 |

## C4. Asset Safeguarding Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-23 | Detect POS fraud / theft | D | Real-time exception monitoring: excessive voids, manual price overrides, sweet-hearting, no-sale drawer opens; daily summary; LPO investigation | Loss Prevention Officer | W37.1–5 | NFR-007 |
| CTL-24 | Detect receiving fraud | D | GR monitored against PO; frequent damage claims flagged by vendor; receiving outside scheduled appointments flagged | DC Manager | W37.6 | PUR-011 |
| CTL-25 | Safeguard inventory in transit | D | In-transit inventory visibility for all DC→Store and inter-DC transfers; transfer discrepancies investigated per W22.9a | Supply Planner / DC Supervisor | W4.8, W22.9a | INV-014 |
| CTL-26 | Control fixed asset disposals | P | Disposal requires tiered approval based on NBV; IT ensures data wipe for IT assets per RA 10173; gain/loss on disposal auto-calculated | Controller / CFO / CEO | W39 | FIN-011 |
| CTL-27 | Safeguard customer data | P | Role-based access to personal data; encryption at rest and in transit; data subject access request tracking; breach register maintained | DPO | W53 | NFR-010, NFR-016 |
| CTL-28 | Control petty cash funds | D | Per-store and per-DC float limits; replenishment requires voucher submission; monthly reconciliation by custodian; AP reviews replenishment requests | Store Manager / AP Clerk | W25 | FIN-017 |

## C5. Financial Reporting Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-29 | Ensure accurate consolidated reporting | D | IC elimination automated; consolidated statements generated from verified entity-level closes; CFO reviews consolidated before distribution | CFO / Chief Accountant | W9a.12–15 | FIN-003, IC-003 |
| CTL-30 | Ensure complete month-end close | P | Close checklist with 17 defined steps; period lock after close; Controller signs off | Controller / CFO | W9a.1–17 | FIN-015 |
| CTL-31 | Ensure NRV provisions are adequate | D | Monthly inventory aging review; write-downs where NRV < cost; Controller approves write-downs > PHP 50K | Cost Accountant / Controller | W9a.16b | INV-011 |
| CTL-32 | Ensure loyalty liability accuracy | D | Monthly Cost Accountant estimate of loyalty liability vs. deferred revenue balance; adjusted if estimate differs | Cost Accountant | W17.11a | CRM-001 |
| CTL-33 | Ensure gift card liability accuracy | D | Monthly gift card liability report with aging; breakage recognized at 24-month inactivity expiry; Finance reviews | Cost Accountant | W28.10–11 | POS-015 |
| CTL-34 | Ensure complete tax compliance | D | Monthly VAT, EWT, and statutory contribution reconciliation; quarterly BIR filing review; annual income tax preparation | Tax Accountant / CFO | W9a.16, W10.11 | FIN-008, HR-002 |
| CTL-35 | Ensure budget adherence | D | Monthly budget vs. actual variance report; PO and capex creation checks budget availability; > 10% variance requires explanation | Controller / Department Heads | W26.10–11 | FIN-012 |

## C6. Operational Process Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-36 | Ensure recall execution | P | System blocks recalled items at POS; ecommerce auto-removes; store quarantine tracked; recall coverage measured | VP Merchandising | W29.5–7 | INV-016 |
| CTL-37 | Ensure warranty claim validity | D | System verifies warranty period from original transaction; defect documented with photos; SLA tracking on vendor response | CSR / Buyer | W33 | POS-019 |
| CTL-38 | Ensure consignment settlement accuracy | D | System auto-records sell-through at POS; monthly settlement report confirmed by Buyer before payment; period-end accrual for sold-but-unsettled | Buyer / Cost Accountant | W23.6–9, W23.6a | FIN-018, INV-017 |
| CTL-39 | Ensure vendor rebate accuracy | D | System auto-accrues rebates at purchase/sale; monthly Cost Accountant validates against agreement; Buyer confirms settlement before payment | Cost Accountant / Buyer | W27.3–9 | FIN-019, PUR-015 |
| CTL-40 | Ensure emergency procurement regularization | D | Emergency procurements must be formalized within 5 business days; system auto-escalates if not; monthly Controller review of emergency procurement frequency | Controller | W60.6–7 | PUR-001 |
| CTL-41 | Ensure LGU permit compliance | D | System alerts 60 days before permit expiry; expired permits escalated; locations blocked if permits lapse (operational risk) | Regulatory Officer | W54.2, W54.10 | NFR-017 |

---

## C7. Vendor & Customer Master Data Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-42 | Prevent vendor payment fraud via bank account change | P | All vendor bank account detail changes require out-of-band verification (phone call to known contact, not the change request itself); dual approval (AP Clerk entry + AP Supervisor approval); 48-hour cooling-off period before first payment to new account; first payment flagged for Treasury confirmation of receipt; full audit trail of old/new bank details, verifier, approver, and timestamp | AP Clerk / AP Supervisor / Treasury | W36.7a | PUR-003, NFR-007 |
| CTL-43 | Prevent Sales Rep self-approval of credit limits on own accounts | P | System enforces that the Sales Rep assigned to a trade/corporate account cannot also be the credit approver for that same account; credit limit approval follows the standard W24 tiered matrix (AR Supervisor / Finance Manager / Credit Committee); if Sales Rep requests a credit limit increase, system routes approval directly to AR Supervisor (bypassing the requesting Sales Rep); quarterly: Internal Audit samples credit approvals to verify no self-dealing occurred | AR Supervisor / Finance Manager | W24, W58 | CRM-003, CRM-008 |

---

## Controls Summary by Category

| Category | Preventive Controls | Detective Controls | Total |
|---|---|---|---|
| Authorization & Approval | 8 | 0 | 8 |
| Segregation of Duties | 5 | 0 | 5 |
| Transaction Integrity | 2 | 8 | 10 |
| Asset Safeguarding | 2 | 4 | 6 |
| Financial Reporting | 1 | 7 | 8 |
| Operational Process | 2 | 4 | 6 |
| Vendor & Customer Master Data | 2 | 0 | 2 |
| **Total** | **22** | **23** | **45** |

---

*Date: 2026-05-30 (v2 — added CTL-42: vendor bank account change control, CTL-43: credit limit self-approval prevention)*
