# Finance & Treasury Workflows

> AP, AR, financial close, intercompany, capex, budget, treasury, insurance, credit/debit notes, management reporting, FX hedging, bad debt management, product costing & margin analysis, and customer credit collection & escalation.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W7. Accounts Payable — Vendor Invoice Processing](#accounts-payable-vendor-invoice-processing)
- [W8. Accounts Receivable — Trade & Corporate Accounts](#accounts-receivable-trade-corporate-accounts)
- [W9. Financial Close & Reporting](#financial-close-reporting)
- [W14. Intercompany Transactions & Settlement](#intercompany-transactions-settlement)
- [W21. Capital Expenditure (Capex) Request & Approval](#capital-expenditure-capex-request-approval)
- [W24. Trade & Corporate Credit Application](#trade-corporate-credit-application)
- [W25. Petty Cash Management](#petty-cash-management)
- [W26. Annual Budget Preparation & Monthly Variance Review](#annual-budget-preparation-monthly-variance-review)
- [W30. Daily Treasury & Cash Position Management](#daily-treasury-cash-position-management)
- [W35. Management Reporting Rhythm](#management-reporting-rhythm)
- [W39. Fixed Asset Disposal & Retirement](#fixed-asset-disposal-retirement)
- [W59. Insurance Policy Lifecycle Management](#insurance-policy-lifecycle-management)
- [W70. Credit Note & Debit Note Aging Reconciliation](#credit-note-debit-note-aging-reconciliation)
- [W80. FX Hedging & Forward Contract Management](#fx-hedging-forward-contract-management)
- [W81. Bad Debt Provisioning, Write-Off & Recovery](#bad-debt-provisioning-write-off-recovery)
- [W85. Product Costing & Margin Analysis Review](#product-costing-margin-analysis-review)
- [W89. Bank Reconciliation](#bank-reconciliation)
- [W90. Monthly Tax Filing & Statutory Remittance](#monthly-tax-filing-statutory-remittance)
- [W94. Customer Deposit & Advance Payment Management](#customer-deposit-advance-payment-management)
- [W99. Payment Settlement Reconciliation (Card / E-Wallet / Online)](#payment-settlement-reconciliation-card-e-wallet-online)
- [W100. Vendor Statement Reconciliation](#vendor-statement-reconciliation)
- [W101. Customer Refund & Credit Processing](#customer-refund-credit-processing)
- [W108. Customer Credit Collection & Escalation](#customer-credit-collection-escalation)
- [W137. Intercompany Dividend & Loan Management](#intercompany-dividend-loan-management)
- [W174. Store-Level Cash-in-Transit (CIT) & Armored Car Management](#store-level-cash-in-transit-cit--armored-car-management)
- [W175. Employee Gratuity & Retirement Fund Management (RA 7641)](#employee-gratuity--retirement-fund-management-ra-7641)

---

## W7. Accounts Payable — Vendor Invoice Processing

| Field | Detail |
|---|---|
| **Trigger** | Vendor invoice received (email, mail, or vendor portal) |
| **Frequency** | ~6,500 invoices/month |
| **Volume** | ~217 invoices/day; peaks at month-end (+50%) |
| **Owner** | AP Supervisor |
| **Participants** | AP Clerk, Buyer (for discrepancies), Treasury (for payment), AP Supervisor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | AP Clerk receives and scans/logs vendor invoice (via email, mail, or vendor portal submission) | AP Clerk | AP Supervisor | 5 min/invoice |
| 2 | System attempts auto-match: PO → Goods Receipt → Invoice (3-way match) | System | — | Automated |
| 3 | If matched (quantities and price within tolerance): auto-approve for payment | System | AP Supervisor | Automated |
| 4 | If mismatch (price, quantity, or missing GR): route to AP Clerk for review | AP Clerk | AP Supervisor | 10 min/invoice |
| 5 | If price discrepancy: AP Clerk contacts Buyer for resolution | AP Clerk | Buyer | 15 min/invoice |
| 6 | If quantity discrepancy (partial receipt): verify GR status; wait for remaining delivery or adjust | AP Clerk | AP Supervisor | 10 min/invoice |
| 6a | Exception SLA: all unmatched invoices must be resolved within 5 business days; system tracks aging of exceptions | System | AP Supervisor | Automated |
| 6b | If exception unresolved after 5 days: system escalates to AP Supervisor; AP Supervisor coordinates with Buyer and vendor for resolution | AP Supervisor | Controller | 15 min/invoice |
| 7 | Approved invoices queued for payment per vendor terms (Net 30, Net 60) | System | — | Automated |
| 7a | System identifies invoices eligible for early payment discount (e.g., 2/10 Net 30); displays discount amount, discount deadline, and annualized return on taking discount; Treasury Analyst includes discount opportunities in weekly cash flow planning (W30 step 8); AP Supervisor prioritizes discounted invoices in payment run when Treasury authorizes | System / AP Supervisor | CFO | 15 min/review |
| 8 | AP Supervisor reviews AP aging weekly; prioritize payments by due date and vendor relationship | AP Supervisor | CFO | 2 hours/week |
| 9 | Twice-weekly payment run: system generates payment file (checks, bank transfers) | AP Clerk | AP Supervisor | 1 hour/run |
| 9a | System calculates Expanded Withholding Tax (EWT) per vendor invoice based on configured Alphanumeric Tax Code (ATC) in vendor master (e.g., WI010 for purchases of goods at 1%, WI020 for services at 2%, WC010 for rentals at 5%); net payment to vendor = invoice amount − EWT; system posts EWT to Withholding Tax Payable (liability); AP Clerk validates EWT computation before payment run | System / AP Clerk | AP Supervisor | Automated + 15 min validation/run |
| 9b | Vendor credit memo processing: AP Clerk receives vendor credit note (mail, email, portal); selects source — RTV reference (W3.6a), rebate settlement (W27.9), price protection (W40.11), or manual entry; system attempts auto-match to original PO/invoice/RTV; AP Clerk posts credit memo: system reduces vendor balance and posts to GL (Dr. Accounts Payable / Cr. COGS or appropriate expense); if vendor has open invoices, system applies credit memo against oldest open invoice; if net vendor credit balance results, AP Clerk decides to request refund, apply to next invoice, or offset | AP Clerk | AP Supervisor | 10 min/credit memo |
| 10 | Treasury reviews and approves payment batch; transmits to bank | Treasury Analyst | CFO | 30 min/run |
| 11 | System posts payment; updates vendor balance | System | — | Automated |

**Match rate target**: ≥ 80% auto-matched (no manual intervention)

### System Touchpoints
- Invoice scanning / OCR / digital capture from email, mail, or vendor portal (W7.1)
- 3-way match engine (PO → GR → Invoice) (W7.2)
- Auto-approval with tolerance thresholds (W7.3)
- Exception routing and workflow (W7.4–6)
- Exception aging tracker with SLA enforcement and auto-escalation at day 5 (W7.6a–b)
- Early payment discount detection: system identifies invoices eligible for discount, calculates annualized ROI, and highlights during payment run; decision criteria — Treasury Analyst authorizes taking discount when (a) annualized ROI exceeds BuildRight's weighted average cost of capital (currently ~8–10%, configurable), (b) cash position (W30) supports early payment without creating liquidity risk, and (c) vendor is rated A or B on vendor scorecard (W44) — discounts for C/D-rated vendors are deferred to standard terms to preserve cash leverage; system auto-calculates annualized ROI per discount offer as: (discount % ÷ (365 ÷ days saved)) × 100 and displays alongside cash position impact in payment run review screen (W7.7a)
- AP aging report (W7.8)
- Payment file generation (bank formats) (W7.9–10)
- Expanded Withholding Tax (EWT): auto-computation per ATC in vendor master, net payment calculation (invoice − EWT), EWT Payable tracking, BIR 1601-E file generation (W7.9a)
- Vendor credit memo processing: credit note entry with source reference (RTV, rebate, price protection), auto-matching to original transactions, automatic application to open invoices, credit balance management (W7.9b)
- Non-PO / recurring expense invoice processing: 2-way match (invoice vs. contract or budget), store manager / department head approval routing, cost center allocation, utility and service bill capture (W7c.1–6)
- Shelf-life / expiry date management: capture manufacturing date and shelf-life at GR for date-sensitive items; system tracks expiry per batch; FEFO (First Expired First Out) pick direction in DC; alerting for near-expiry items; periodic expiry review feeds into slow-mover disposition (W3, W4, W6)
- GRNI aging management: AP Clerk runs weekly GRNI aging report showing all GRs without matching vendor invoices, grouped by aging bucket (0–30, 31–60, 61–90, 90+ days); items > 30 days flagged for Buyer follow-up with vendor; items > 60 days escalated to AP Supervisor for direct vendor contact; items > 90 days reviewed by Controller for potential permanent accrual or write-off; system tracks GRNI aging with vendor-level drill-down; weekly GRNI aging dashboard visible to AP Supervisor and Controller (W7, W9a.2a)
- Duplicate vendor invoice detection: system automatically checks incoming vendor invoices against the AP sub-ledger for duplicate invoice number, duplicate vendor + amount + date combinations, and duplicate PO reference + invoice number; if a potential duplicate is detected, system blocks the invoice and alerts AP Clerk with the matching existing invoice reference; AP Clerk investigates (true duplicate vs. sequential invoice numbers from same vendor) and either rejects the duplicate or overrides with documentation; monthly: AP Supervisor reviews duplicate detection override log as part of AP controls review (cross-reference CTL-42 in Internal Controls Matrix) (W7)
- Evaluated Receipt Settlement (ERS): for configured VMI vendors (W20) and select blanket PO vendors (W2c), system auto-generates vendor invoice from PO + Goods Receipt data without requiring vendor invoice submission; AP Clerk validates auto-generated invoice against PO and GR; if within tolerance, auto-approved for payment; reduces GRNI accumulation and manual invoice processing for high-volume, trusted vendor relationships

### Staffing Implication
- **8–10 AP Clerks**: total ~305–370 invoices/business-day across merchandise (~295/day per W7: 6,500 invoices/month ÷ 22 business days) and non-PO (~91–136/day per W7c: 2,000–3,000/month ÷ 22); at 5 min logging each = ~25–31 hours for basic processing; with ~20% requiring manual resolution at 25 min each = ~25–30 additional hours; total ~50–61 hours/business-day; with 10 clerks that's ~5–6 hours each; reasonable with payment runs, GRNI follow-up, vendor statement reconciliation (W7d), and other duties; note that month-end peaks (+50% per W7) push daily volume to ~460–550 invoices/day during close week, requiring temporary overtime or redeployment of 2–3 other Finance staff (Cost Accountant, Treasury Analyst) to AP to maintain processing SLA; peak staffing contingency documented in W7
- **1 AP Supervisor**: Oversight, aging review, GRNI escalation management, escalations.
- **2 Treasury Analysts**: Payment approval, bank file transmission, LC management. Shared with AR and other treasury duties.

### W7c. Non-PO / Recurring Expense Invoice Processing

| Field | Detail |
|---|---|
| **Trigger** | Utility bill, service invoice, rent, or other recurring expense received without a Purchase Order |
| **Frequency** | ~2,000–3,000 non-PO invoices/month across all locations (200 stores + 5 DCs + HQ); combined with ~6,500 merchandise/vendor invoices (W7), total AP invoice volume is ~8,500–9,500/month; the ~6,000–7,000 figure in the model-company-profile §10.2 refers to merchandise/vendor invoices only |
| **Volume** | ~10–15 recurring vendor invoices per store per month (electricity, water, internet, rent to Property Mgmt Inc., security, cleaning, waste disposal) |
| **Owner** | AP Supervisor |
| **Participants** | AP Clerk, Store Manager / Department Head (approval), AP Supervisor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | AP Clerk receives and logs non-PO invoice (utility bill, service invoice, lease payment); classifies as recurring or one-time | AP Clerk | AP Supervisor | 5 min/invoice |
| 2 | System attempts 2-way match: invoice amount vs. contract amount or budget allocation per cost center | System | — | Automated |
| 3 | If invoice within tolerance of contract/budget: route to cost center owner for approval (Store Manager for store expenses, Department Head for HQ expenses) | System | Cost center owner | 1 min/auto-approved |
| 4 | If invoice exceeds budget or no contract on file: route to cost center owner for review with explanation of variance | AP Clerk / Cost center owner | AP Supervisor | 5 min/invoice |
| 5 | Approved non-PO invoices queued for payment in standard payment run (W7.9–11); EWT computed per ATC for service invoices (W7.9a) | System | AP Supervisor | Automated |
| 6 | Monthly: AP Supervisor reviews non-PO expense summary by cost center; flags locations with unusual expense patterns for management review | AP Supervisor | Controller | 1 hour/month |

**Match rate target**: ≥ 70% auto-matched for recurring expenses (contract-based)

### W7d. AP Vendor Statement Reconciliation

| Field | Detail |
|---|---|
| **Trigger** | Monthly vendor statement received (email, mail, or vendor portal) |
| **Frequency** | Monthly for top 50 vendors (by spend); quarterly for remaining active vendors |
| **Volume** | ~50 monthly reconciliations + ~750 quarterly reconciliations; top 50 = 45% of COGS |
| **Owner** | AP Clerk |
| **Participants** | AP Clerk, AP Supervisor, Buyer (for discrepancies) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Vendor submits monthly or quarterly statement showing all invoices, credit memos, and payments for the period; AP Clerk receives and logs statement in system | AP Clerk | AP Supervisor | 5 min/vendor |
| 2 | System attempts auto-reconciliation: matches vendor statement line items to AP sub-ledger transactions (invoices, credit memos, payments) by invoice number, date, and amount | System | — | Automated |
| 3 | System generates reconciliation summary: matched items, unmatched vendor lines (vendor shows invoice not in AP), unmatched AP lines (AP shows invoice not on vendor statement), and amount variances | System | — | Automated |
| 4 | AP Clerk investigates unmatched items: (a) **unmatched vendor lines** — vendor invoice not yet received or not yet entered in AP; if invoice is valid and GR exists, AP Clerk enters invoice per W7; if no GR, flags for Buyer follow-up with vendor; (b) **unmatched AP lines** — payment made but vendor did not credit; AP Clerk provides payment reference (bank transfer date, amount) for vendor to apply; (c) **amount variances** — typically partial payments, discounts taken, or EWT deduction not reflected on vendor statement; AP Clerk explains variance with supporting documentation | AP Clerk | AP Supervisor | 15–30 min/vendor |
| 5 | AP Clerk documents reconciliation result: matched amount, unmatched items with explanation, and net variance; flags reconciling items > PHP 50,000 or items > 60 days unresolved for AP Supervisor review | AP Clerk | AP Supervisor | 10 min/vendor |
| 6 | Monthly: AP Supervisor reviews vendor reconciliation summary for top 50 vendors — total matched vs. unmatched, aging of reconciling items, recurring discrepancy patterns; escalating chronic discrepancies to Buyer for vendor relationship review per W44 | AP Supervisor | Controller | 1 hour/month |
| 7 | Quarterly: AP Supervisor includes vendor reconciliation metrics in AP controls review (cross-reference CTL-42 in Internal Controls Matrix); unreconciled balances > 90 days escalated to Controller for potential write-off or accrual adjustment | AP Supervisor | Controller | 30 min/quarter |

### System Touchpoints
- Vendor statement import: AP Clerk uploads vendor statement (PDF, Excel, or EDI); system parses line items for auto-matching (W7d.1–2)
- Auto-reconciliation engine: matches vendor statement lines to AP sub-ledger by invoice number, date, and amount with configurable tolerance (W7d.2)
- Reconciliation summary dashboard: matched, unmatched (vendor-side), unmatched (AP-side), and variance items with drill-down (W7d.3)
- Reconciliation documentation: auditor-ready log showing reconciliation result per vendor per period with aging of reconciling items (W7d.5)
- Vendor reconciliation analytics: match rate, average reconciliation time, recurring discrepancy vendors, aging of unresolved items (W7d.6)
- Integration with W7 (AP invoice processing), W7c (non-PO invoices), W44 (vendor performance — chronic reconciliation issues affect vendor scorecard)

---



---

## W8. Accounts Receivable — Trade & Corporate Accounts

| Field | Detail |
|---|---|
| **Trigger** | Sales invoice generated for trade/corporate account at POS or by Sales Rep |
| **Frequency** | ~3,500 AR invoices/month |
| **Volume** | ~117 invoices/day; ~5,200 active AR accounts |
| **Owner** | AR Supervisor |
| **Participants** | AR Clerk, Sales Rep (trade accounts), AR Supervisor, Finance Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer purchase on trade/corporate account; invoice created at POS or by Sales Rep | Cashier / Sales Rep | Department Supervisor | Part of sale |
| 2 | System posts AR invoice; updates customer balance | System | — | Automated |
| 3 | System checks customer credit limit; blocks further sales if exceeded | System | AR Supervisor | Automated |
| 3a | Credit hold override: if sales rep or Store Manager requests sale despite credit block, system prompts for authorizer and reason; override requires AR Supervisor approval for up to 110% of credit limit, Finance Manager approval for up to 130%; override logged with customer ID, authorizer, overridden amount, reason, and 24-hour validity; system counts overridden amount against credit exposure for monitoring | Sales Rep / AR Supervisor / Finance Manager | Finance Manager | 5 min/override |
| 4 | AR Clerk sends monthly statement to each active account (1st of month) | AR Clerk | AR Supervisor | 4 hours/month (batch) |
| 5 | AR Clerk reviews aging report weekly; flags accounts > 30 days past due | AR Clerk | AR Supervisor | 1 hour/week |
| 6 | For 30-day overdue: AR Clerk contacts customer (phone/email) for follow-up | AR Clerk | AR Supervisor | 15 min/account |
| 7 | For 60-day overdue: escalate to Sales Rep for relationship-based collection | Sales Rep | AR Supervisor | 15 min/account |
| 8 | For 90-day overdue: escalate to Finance Manager; consider credit hold | Finance Manager | CFO | 30 min/account |
| 8a | **AR legal collection escalation**: for accounts > 120 days overdue with no payment response after standard collection tiers (W8.6–8) — (a) AR Supervisor sends formal demand letter (demand collection letter per Philippine legal requirements) via registered mail with return card; letter states outstanding amount, original invoice references, payment deadline (15 business days), and notice of potential legal action; (b) if customer responds and disputes: AR Clerk coordinates investigation with Sales Rep and Store Manager to validate or resolve dispute; disputed amounts suspended from collection while under investigation; (c) if no response after demand letter deadline: AR Supervisor escalates to Finance Manager for referral to external collection agency or Legal for filing of collection case; (d) external collection agency engaged per W62 (service contract); agency fee typically 10–20% of collected amount; system tracks collection agency referral with agency reference and status; (e) if legal action warranted (amount > PHP 200,000 and customer solvent): Legal files collection case with appropriate court; Legal manages case with external counsel; system tracks legal case reference and status; (f) **Bad debt write-off**: if all collection efforts exhausted (demand letter + collection agency + legal if applicable) or customer confirmed insolvent/bankrupt, AR Clerk submits bad debt write-off request — tiered approval per W8.8b below; system posts Dr. Bad Debt Expense / Cr. Allowance for Doubtful Accounts (or direct write-off Dr. Bad Debt Expense / Cr. AR per company policy); BIR documentation retained: demand letter, collection agency report, court filing (if applicable), write-off approval; (g) **Write-off recovery**: if customer subsequently pays on a previously written-off account (recovery of bad debt), AR Clerk processes recovery payment; system posts Dr. Cash / Cr. Bad Debt Recovery (income); write-off recovery tracked separately from regular AR collections for reporting | AR Supervisor / Finance Manager / Legal / CFO | Controller | Varies |
| 8b | **Bad debt write-off approval**: (a) ≤ PHP 50,000: Finance Manager, (b) PHP 50,001–200,000: Controller + Finance Manager, (c) PHP 200,001–1,000,000: CFO, (d) > PHP 1,000,000: CEO | Approver | Approver | 15 min/write-off |
| 9 | Customer payment received; AR Clerk applies payment to open invoices | AR Clerk | AR Supervisor | 5 min/payment |
| 10 | Monthly reconciliation of AR sub-ledger to GL | AR Clerk | AR Supervisor | 2 hours/month |
11 | Customer credit memo: AR Clerk creates credit memo with reason code and source reference (pricing error, volume discount adjustment, short delivery, service failure, promotional adjustment); tiered approval (AR Supervisor ≤ PHP 10,000; Finance Manager ≤ PHP 50,000; CFO > PHP 50,000); system applies credit to oldest open invoice or creates credit balance; posts GL entry (Dr. Revenue or appropriate expense / Cr. Accounts Receivable); customer notified of credit | AR Clerk / AR Supervisor | Finance Manager | 10 min/credit memo |
12 | **Customer account closure**: customer requests trade/corporate account closure; AR Clerk verifies zero outstanding balance — if balance outstanding, arranges final payment or collection per W8.6–8; system settles any open credit memos (applies to outstanding invoices or processes refund); loyalty points: if customer has unredeemed points, system offers redemption before closure or forfeits per W17 terms; AR Clerk deactivates account in system; account status changed to "Closed"; system retains transaction history for 7-year BIR retention; PII anonymized after retention period per RA 10173 and W53 data retention policy; account closure logged with reason, date, and AR Clerk ID | AR Clerk | AR Supervisor | 15 min/closure |

### System Touchpoints
- AR invoice creation from POS/sales order (W8.1–2)
- Real-time credit limit check (W8.3)
- Credit hold override with tiered authorization, audit trail, and automatic expiry (W8.3a)
- Aging report generation (W8.5)
- Customer statement generation (W8.4)
- Customer credit memo processing: reason code and source reference, tiered approval, auto-application to open invoices, GL posting (Dr. Revenue/Expense / Cr. AR), credit balance management (W8.11)
- Dormant trade/corporate account management: system defines dormancy as zero transactions (sales or payments) for 6 consecutive months; monthly, system generates dormant account report listing all accounts meeting dormancy criteria; AR Clerk contacts dormant accounts via phone/email to confirm business status — (a) if customer confirms active but no current need: account remains active, no action; (b) if customer unresponsive after 2 contact attempts over 30 days: AR Supervisor places account on inactive status; system automatically reduces credit limit to PHP 0 (prevents new sales on account); account remains searchable for transaction history and reactivation; (c) if customer confirms business closure: AR Clerk processes formal account closure per W8 step 12 — verifies zero outstanding balance, settles open credit memos, manages loyalty points disposition, deactivates account, retains transaction history for 7-year BIR retention period, anonymizes PII after retention period per RA 10173 (cross-reference W53); for reactivation of inactive accounts: customer contacts Sales Rep or AR Clerk; AR Clerk reopens account with updated business documents per W24 (abbreviated credit assessment — if reactivation within 12 months, may reuse prior credit assessment with updated financials; if > 12 months, full W24 process required); AR Supervisor approves reactivation with new credit limit; annual: AR Supervisor reviews all dormant/inactive accounts and recommends write-off of any remaining immaterial balances (< PHP 5,000) with Finance Manager approval
- Payment application and matching (W8.9)
- AR sub-ledger to GL reconciliation (W8.10)

### Staffing Implication
- **3–4 AR Clerks**: 117 invoices/day is relatively low volume (retail is mostly cash/card). Main workload is collections on ~5,200 accounts. At any time, ~15% (780) may need follow-up. 3 clerks can manage with monthly statement runs and weekly aging reviews.
- **1 AR Supervisor**: Oversight and escalation handling.

---



---

## W9. Financial Close & Reporting

### W9a. Month-End Close

| Field | Detail |
|---|---|
| **Trigger** | Last calendar day of the month |
| **Frequency** | Monthly |
| **Volume** | 5 entities × 12 months = 60 entity-month closes/year |
| **Owner** | Chief Accountant / Controller |
| **Participants** | Chief Accountant, AP Supervisor, AR Supervisor, Treasury Analyst, Tax Accountant, Cost Accountant, CFO |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Verify all store day-end closings are posted; follow up on any outstanding | Chief Accountant | Controller | 2 hours |
| 2 | AP: Ensure all vendor invoices received before cut-off are entered and matched | AP Supervisor | Controller | 2 hours |
| 2a | GRNI reconciliation: system generates Goods Received Not Invoiced report showing all GRs without matching AP invoices; Finance verifies completeness; if system uses GR/IR clearing account, verify clearing account balance reconciles to open GRNI list; accrue provision for estimated costs where invoices are expected but not yet received | AP Supervisor / Chief Accountant | Controller | 1 hour |
| 3 | AR: Post all AR invoices and payments received through month-end | AR Clerk | Controller | 1 hour |
| 4 | Accruals: Book accrual entries for expenses incurred but not yet invoiced (utilities, freight, rent) | Chief Accountant | Controller | 3 hours |
| 5 | Intercompany: Verify all IC transactions are posted; run IC matching | Chief Accountant | Controller | 2 hours |
| 5a | FX Revaluation: System revalues all open foreign-currency AP and AR balances at month-end BIR exchange rate; posts unrealized FX gain/loss to P&L and FX revaluation reserve to BS; auto-reverses the revaluation entries at start of next period | System / Chief Accountant | Controller | Automated + 30 min review |
| 6 | Inventory: Verify perpetual WAC (weighted average cost) calculations; post adjustments from cycle counts | Cost Accountant | Controller | 2 hours |
6a | WAC methodology: system calculates perpetual moving average cost at each goods receipt — new WAC = (prior inventory value + receipt value) ÷ (prior quantity + receipt quantity); COGS at POS uses current WAC at time of sale; at month-end, Cost Accountant verifies WAC accuracy by sampling high-value and high-volume SKUs, reconciles total inventory valuation to GL inventory accounts, and posts any adjustments from cycle counts (W6) or physical inventory (W42) | Cost Accountant | Controller | Part of 2 hours |
| 7 | Fixed Assets: Post monthly depreciation | Cost Accountant | Controller | 30 min |
| 8 | Prepayments: Amortize prepaid expenses (insurance, rent) | Chief Accountant | Controller | 30 min |
| 9 | Bank reconciliation: Match bank statements to GL cash accounts (all bank accounts, all entities) | Treasury Analyst | Controller | 3 hours |
| 10 | Run trial balance per entity; review for unusual balances | Chief Accountant | Controller | 1 hour |
| 11 | Post adjusting entries as needed | Chief Accountant | Controller | 1 hour |
| 12 | Generate preliminary financial statements per entity (BS, IS, CF) | System / Chief Accountant | Controller | 30 min |
| 13 | Run intercompany elimination entries for consolidation | Chief Accountant | CFO | 1 hour |
| 14 | Generate consolidated financial statements (5 entities) | System / Chief Accountant | CFO | 30 min |
| 15 | CFO reviews consolidated statements; queries variances | CFO | CFO | 1 hour |
| 16 | Tax Accountant prepares VAT return (BIR 2550M) and withholding tax returns (1601-E, 1601-C) | Tax Accountant | CFO | 3 hours |
16c | Local Business Tax (LBT) per LGU: system generates LBT payment schedule per location (200 stores + 5 DCs + HQ) based on configured LGU calendars (annual or quarterly per LGU); Tax Accountant reviews schedule, validates amounts per LGU rate schedules (typically 1–2% of gross receipts for retail, varies by LGU); processes payments per LGU (online, over-the-counter, or LGU office); system posts payment per location (Dr. Local Business Tax Expense / Cr. Cash); tracks payment status and receipt per location; flags locations with upcoming or overdue LBT payments on monthly dashboard | Tax Accountant | Controller | 4 hours/month (distributed across LGU due dates) |
| 16a | EWT remittance: Tax Accountant generates EWT remittance file (BIR 1601-E) from accumulated Withholding Tax Payable per vendor per ATC; reconciles to vendor remittance list; transmits to BIR via eFPS; system posts remittance (Dr. Withholding Tax Payable / Cr. Cash) | Tax Accountant | CFO | 1 hour |
| 16b | Inventory net realizable value (NRV) review: Cost Accountant runs inventory aging report (days since last sale); for slow-moving items (> 180 days), system compares WAC to estimated NRV (clearance price × sell-through probability); Cost Accountant proposes write-down per SKU where NRV < cost; Controller approves write-downs > PHP 50,000; system posts Dr. Inventory Write-Down Expense / Cr. Inventory Provision (contra-asset); **NRV reversal treatment**: when a written-down item is subsequently sold — (a) system recognizes revenue at selling price (standard), (b) system recognizes COGS at the written-down carrying amount (not the original WAC), (c) difference between original WAC and written-down carrying amount represents the write-down previously recognized; for partial sales of written-down lots, COGS per unit is the written-down unit cost; no additional journal entry is required at point of sale because the provision was already posted; at next quarterly NRV review (W9a.16b), Cost Accountant reassesses remaining written-down items — if NRV has recovered above carrying amount (e.g., market price increase), Cost Accountant may reverse the provision up to the original write-down amount per PAS 2.31 with Controller approval; system posts reversal as Dr. Inventory Provision / Cr. Inventory Write-Down Recovery (P&L); reversal is limited to the original write-down amount per SKU — carrying value cannot exceed original WAC | Cost Accountant / Controller | Controller | 2 hours |
| 16d | Inventory write-off (obsolete / damaged beyond recovery): distinct from NRV write-down (step 16b) — for items that will never be sold (fully obsolete, expired, irrevocably damaged, or vendor refuses RTV and item has no residual value); Cost Accountant prepares write-off list per SKU with supporting evidence (photos, aging, disposition attempts); tiered approval: Store Manager ≤ PHP 10,000, Controller ≤ PHP 50,000, CFO ≤ PHP 500,000, CEO > PHP 500,000; system posts Dr. Inventory Write-Off Expense (loss) / Cr. Inventory — removes items from inventory register entirely (not a provision — permanent removal); BIR documentation retained: write-off approval, supporting evidence, and physical destruction or disposal certificate | Cost Accountant / Controller | CFO | 1 hour |
| 16e | Credit note / debit note reconciliation: Chief Accountant runs AP and AR credit note aging report — all unapplied credit memos and debit memos listed by entity, vendor/customer, age, and amount; credit memos > 60 days unapplied flagged for investigation; AP Clerk contacts vendor to resolve open AP credits (apply to next invoice, request refund, or confirm as settled); AR Clerk contacts customers to resolve open AR credits (apply to next sale, issue refund, or confirm as settled); unresolved items > 90 days escalated to Controller; summary of unapplied credit notes included in month-end close package | Chief Accountant / AP Clerk / AR Clerk | Controller | 1 hour |
| 17 | Final close: lock period in system | Controller | CFO | 15 min |

**Target**: Close within 5 working days of month-end

### W9b. Year-End Close

Additional steps on top of month-end close (December):

| # | Activity | Role (R) | Duration |
|---|---|---|---|
| 18 | 13th month pay accrual reconciliation | Payroll Accountant | 2 hours |
| 19 | Physical inventory (wall-to-wall) count and adjustment | Cost Accountant + all store staff | 1–2 days |
| 20 | Year-end tax provisions and adjustments | Tax Accountant | 4 hours |
| 21 | Annual income tax return preparation (BIR 1702RT) | Tax Accountant | 1 week |
| 22 | External audit preparation and coordination | Controller + CFO | Ongoing (Q1) |
| 23 | SEC annual report preparation | Controller | 1 week |

### System Touchpoints
- Store day-end posting monitoring (W9a.1)
- GRNI reconciliation report and clearing account balance verification (W9a.2a)
- Accrual and journal entry workflow (W9a.4–8, 11)
- IC matching and elimination automation (W9a.5, 13)
- Inventory valuation engine: perpetual WAC verification (not periodic recalculation); month-end reconciliation of inventory valuation to GL (W9a.6a)
- Bank reconciliation (W9a.9)
- Local Business Tax (LBT) per LGU: per-location LBT calendar, payment tracking and schedule; LGU-specific rate schedules and forms; payment status dashboard with overdue alerting; BIR retention of LBT receipts (W9a.16c)
- Multi-entity financial statement generation (W9a.12–14)
- Period lock / close controls (W9a.17)
- BIR tax form generation (W9a.16)
- EWT remittance file generation per BIR 1601-E with per-vendor per-ATC breakdown; eFPS transmission (W9a.16a)
- Inventory NRV review: aging by days-since-last-sale, NRV calculator, write-down journal entry with approval, provision reversal on subsequent sale (PAS 2.31 compliant — reversal limited to original write-down; carrying value capped at original WAC; quarterly reassessment with Cost Accountant and Controller review) (W9a.16b)
- Inventory write-off: complete removal from inventory register (not provision); tiered approval with BIR-compliant documentation (photos, aging, disposition evidence, destruction certificate); distinct from NRV write-down (W9a.16d)
- Credit note / debit note reconciliation: AP and AR credit note aging report with unapplied memos > 60 days flagged; escalation at 90 days; resolution tracking (apply, refund, settle); summary in month-end close package (W9a.16e)

### Staffing Implication
- **Controller**: Owns the close process. 1 person sufficient with support.
- **1 Chief Accountant**: Handles most close entries. Stretched during close week (~30 hours of close work in 5 days).
- **1 Cost Accountant**: Inventory valuation + fixed assets.
- **1 Tax Accountant**: VAT + withholding monthly; income tax quarterly/annual.
- **Total Finance team (~35)**: During close week, 8–10 people are heavily involved. The rest of the month is lighter. Current headcount supports this.

---



---

## W14. Intercompany Transactions & Settlement

| Field | Detail |
|---|---|
| **Trigger** | Ongoing business operations between the 5 legal entities |
| **Frequency** | Monthly processing and settlement |
| **Volume** | ~100–200 IC transactions/month |
| **Owner** | Chief Accountant |
| **Participants** | Chief Accountant, AP/AR Clerks, Treasury, CFO |

### Intercompany Flows

| Flow | From → To | Nature | Frequency |
|---|---|---|---|
| Store rent | Depot Inc. → Property Mgmt Inc. | Monthly lease payments | Monthly |
| DC warehousing fees | Depot Inc. → Logistics Inc. | Storage and distribution fees | Monthly |
| Ecommerce fulfillment | Digital Commerce Inc. → Depot Inc. (BOPIS) or Logistics Inc. (delivery) | Fulfillment fees per order | Monthly |
| Ecommerce payment collection | Digital Commerce Inc. → Depot Inc. | Remittance of in-store BOPIS revenue | Monthly |
| Management fees | All subsidiaries → Holdings Inc. | Corporate overhead allocation | Monthly |
| Intercompany loans | Holdings → subsidiaries as needed | Cash advances / funding | As needed |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System auto-generates IC invoices based on configured transfer pricing rules | System | Chief Accountant | Automated |
| 2 | Chief Accountant reviews IC invoice batch for accuracy | Chief Accountant | Controller | 1 hour/month |
| 3 | System posts IC AP in buying entity and IC AR in selling entity simultaneously | System | — | Automated |
| 4 | Monthly: run IC reconciliation report — verify balances match across all entity pairs | Chief Accountant | Controller | 2 hours/month |
| 5 | Resolve any IC mismatches (timing differences, missing entries) | Chief Accountant | Controller | 1 hour/month |
| 6 | Prepare net settlement schedule (offset IC balances; only net amounts paid) | Chief Accountant | CFO | 1 hour/month |
| 7 | CFO approves IC settlement; Treasury executes bank transfers | Treasury Analyst | CFO | 30 min/month |
| 8 | At month-end close: system runs IC elimination entries for consolidation | System | — | Automated |
| 9 | Verify consolidation eliminates all IC revenue, expense, AP, AR | Chief Accountant | CFO | 1 hour/month |

### System Touchpoints
- Automated IC invoice generation with transfer pricing rules (W14.1)
- Simultaneous IC AP/AR posting across entities (W14.3)
- IC reconciliation report across entity pairs (W14.4)
- IC elimination automation during consolidation (W14.8)
- Consolidated financial statement generation with IC lines eliminated (W14.9)
- Transfer pricing rule maintenance with annual review documentation per BIR RR 19-2020 (W14.1)
- Dual IC framework: BuildRight operates two intercompany models — (1) **Service-based IC** (primary): monthly fees for warehousing (Logistics Inc.), ecommerce fulfillment (Digital Commerce Inc.), rent (Property Mgmt Inc.), and management fees (Holdings Inc.) — no goods change ownership between entities; Depot Inc. owns all merchandise inventory throughout the supply chain; standard DC→Store replenishment (W4) and inter-DC transfers (W22) are intra-entity inventory movements, not IC goods transfers; (2) **Goods-based IC** (rare): if inter-entity goods transfer is needed (e.g., Digital Commerce Inc. purchases goods from Depot Inc. for direct resale, Property Mgmt Inc. purchases building materials for property maintenance), system creates IC sales order and IC purchase order at configured transfer price; IC invoice auto-generated at receipt; IC elimination during consolidation per W9a.13; system supports both models with different GL posting paths (W14)
- IC settlement timing: all IC flows (service-based and goods-based) are settled on a single monthly net settlement date (typically 5th of the following month) as part of W14 step 6; Digital Commerce Inc. remits collected ecommerce payments to Depot Inc. on this same schedule (not daily or weekly), which means Depot Inc. carries up to 30 days of ecommerce revenue as an IC receivable from Digital Commerce Inc.; Treasury accounts for this timing in cash flow forecasting (W30 step 8); if ecommerce GMV grows significantly (Year 2–3 target of PHP 250–350M/month), consider moving ecommerce payment remittance to twice-monthly to reduce IC receivable exposure

### Goods-Based IC Trigger Scenarios

While the primary IC model is service-based, the following concrete scenarios would trigger a goods-based intercompany transfer (Depot Inc. sells goods to another entity at arm's-length transfer price):

| Scenario | From | To | Trigger | IC Pricing Basis | Approval |
|---|---|---|---|---|---|
| Property Mgmt Inc. purchases building materials for property maintenance or tenant improvements | Depot Inc. | Property Mgmt Inc. | Property Mgmt Inc. submits material requisition for repair/renovation of leased premises (BuildRight stores, DC facilities, or HQ office) | Depot Inc. cost + 5% markup (arm's-length; below retail SRP) | Property Mgmt Inc. Facilities Coordinator + Depot Inc. Category Manager |
| Digital Commerce Inc. purchases office supplies or IT peripherals for internal use | Depot Inc. | Digital Commerce Inc. | Digital Commerce Inc. office manager requests items not available through standard IT procurement | Standard SRP (small volumes; immaterial) | Digital Commerce Inc. Dept. Head |
| Logistics Inc. purchases warehouse supplies (racking, safety equipment, packaging materials) from Depot Inc. inventory | Depot Inc. | Logistics Inc. | DC Supervisor identifies need for operational supplies stocked in Depot Inc. inventory | Depot Inc. cost + 5% markup | Logistics Inc. DC Manager + Depot Inc. Category Manager |

For each goods-based IC transfer: system creates IC Sales Order (selling entity) and IC Purchase Order (buying entity) at configured transfer price; goods physically transferred from Depot Inc. stock; IC invoice auto-generated; IC elimination during consolidation per W9a.13. Estimated volume: < 20 goods-based IC transactions/year across all entity pairs.

### Goods-Based IC System Flow Detail

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Requesting entity creates IC Purchase Requisition in system: item(s), quantity, justification, requesting entity, delivery location | Requesting entity staff | Requesting entity Dept. Head | 10 min |
| 2 | System checks Depot Inc. inventory availability at nearest DC/store with ATP; if available, auto-creates IC Sales Order in Depot Inc. and linked IC Purchase Order in requesting entity at configured transfer pricing rule (cost + 5% markup for materials; SRP for small office supplies) | System | — | Automated |
| 3 | If IC value > PHP 50,000: approval required from requesting entity Finance Manager and Depot Inc. Category Manager; if < PHP 50,000: auto-approved within contract parameters | Approver(s) | CFO | 15 min |
| 4 | Depot Inc. DC or store picks goods; scan-confirms shipment; system reduces Depot Inc. inventory, creates in-transit inventory | DC/Store Staff | DC Supervisor / Store Manager | Per W3/W22 |
| 5 | Requesting entity receives goods; scan-confirms receipt; system increases requesting entity inventory (if applicable) or posts directly to expense/consumption | Receiving Staff | Dept. Head | Per W3/W18 |
| 6 | System auto-generates IC invoice from IC Sales Order at transfer price; simultaneous posting: Depot Inc. Dr. IC Receivable / Cr. IC Revenue + Cr. Inventory (at cost); requesting entity Dr. Expense/Inventory / Cr. IC Payable | System | — | Automated |
| 7 | IC invoice included in monthly W14 IC reconciliation and settlement cycle | Chief Accountant | Controller | Per W14 |

### Annual IC Transfer Pricing Review

### IC Invoice Dispute Resolution

| Field | Detail |
|---|---|
| **Trigger** | One entity disputes an IC charge generated by another entity (e.g., Depot Inc. contests a Logistics Inc. warehousing fee calculation, or Digital Commerce Inc. disputes an ecommerce fulfillment fee) |
| **Frequency** | Occasional — estimated 2–5 disputes/year |
| **Owner** | Chief Accountant |
| **Participants** | Chief Accountant, disputing entity's Finance lead, CFO |

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Receiving entity's Finance lead identifies IC charge discrepancy: amount does not match agreed transfer pricing rule, volume calculation is incorrect, or charge was not anticipated | Entity Finance Lead | Chief Accountant | 15 min |
| 2 | Chief Accountant reviews the disputed IC invoice against the configured transfer pricing rule and underlying transaction data (e.g., number of orders fulfilled, square meters leased, payment collections remitted) | Chief Accountant | Controller | 30 min |
| 3 | If calculation error confirmed: Chief Accountant corrects the IC invoice in system; system reposts corrected entries in both entities; no further escalation needed | Chief Accountant | Controller | 15 min |
| 4 | If dispute is about pricing rule interpretation (not a calculation error): Chief Accountant escalates to CFO for ruling; CFO interprets the transfer pricing agreement per the documented IC framework (W14) | CFO | CEO | 30 min |
| 5 | CFO decision is final; Chief Accountant adjusts IC invoice if needed; Controller documents the interpretation precedent for inclusion in annual IC transfer pricing review (W14 annual review) | CFO / Chief Accountant | Controller | 15 min |
| 6 | If dispute reveals a systemic issue with the IC pricing rule: CFO initiates an early review of the applicable IC pricing rule (outside the annual cycle) and updates the system configuration | CFO | CEO | 1 hour |

**Dispute SLA**: All IC disputes must be resolved within the same monthly close period. Unresolved disputes block the close for both entities.

### IC Loan Lifecycle

| Field | Detail |
|---|---|
| **Trigger** | Subsidiary requires funding for working capital, capex, or seasonal cash flow needs beyond internal cash generation |
| **Frequency** | As needed; typically 5–10 IC loan events/year |
| **Owner** | CFO |
| **Participants** | CFO, Treasury Analyst, Chief Accountant, borrowing entity Finance lead |

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Subsidiary Finance lead identifies funding need; submits IC loan request to CFO with amount, purpose, proposed repayment schedule, and cash flow justification | Entity Finance Lead | CFO | 30 min |
| 2 | CFO approves IC loan; defines terms: principal, interest rate (at minimum the BIR-prescribed rate per RR 19-2020 for arm's-length compliance — currently 12% per annum or the applicable BIR rate), repayment schedule (lump sum or amortizing), and maturity date | CFO | CEO | 15 min |
| 3 | Treasury Analyst executes inter-entity bank transfer; system posts IC loan entry (Dr. IC Loan Receivable in lending entity / Cr. Cash; Dr. Cash / Cr. IC Loan Payable in borrowing entity) | Treasury Analyst | CFO | 15 min |
| 4 | System calculates monthly interest accrual per loan terms: Dr. IC Interest Receivable / Cr. IC Interest Income in lending entity; Dr. Interest Expense / Cr. IC Interest Payable in borrowing entity; interest accrual posts automatically at month-end as part of W9a close | System | Controller | Automated |
| 5 | Monthly: Chief Accountant reconciles IC loan balances (principal + accrued interest) across lending and borrowing entities as part of W14 step 4 IC reconciliation | Chief Accountant | Controller | Part of W14 |
| 6 | At repayment: Treasury Analyst executes repayment transfer; system posts principal repayment and any remaining accrued interest; IC loan balance reduced accordingly | Treasury Analyst | CFO | 15 min |
| 7 | At maturity: if loan not yet repaid, system alerts CFO 30 days before maturity; CFO decides to extend, demand repayment, or convert to equity (with Board approval if applicable) | System / CFO | CEO | Automated + 15 min decision |
| 8 | Annual: CFO reviews all IC loan balances and terms as part of W14 annual transfer pricing review; confirms arm's-length compliance; adjusts terms if regulatory rates change | CFO | CEO | Part of W14 annual review |

### System Touchpoints (IC Loans)
- IC loan record creation with principal, interest rate, repayment schedule, and maturity date (W14 IC Loans step 2)
- Automatic monthly interest accrual with GL posting in both entities (W14 IC Loans step 4)
- IC loan balance tracking with maturity alerting at 30 days (W14 IC Loans step 7)
- IC loan reconciliation integrated into monthly W14 IC matching (W14 IC Loans step 5)
- BIR arm's-length interest rate compliance: system validates that IC loan interest rate meets or exceeds BIR-prescribed minimum; flags loans below threshold for CFO review (W14 IC Loans step 2)
- Integration with W9a (interest accrual in month-end close), W14 (IC reconciliation), W30 (cash transfer execution), W26 (budget — IC borrowing planned in annual budget)

### Annual IC Transfer Pricing Review (continued)

| Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|
| CFO and Controller review all IC pricing schedules (store rent, DC fees, ecommerce fulfillment, management fees, IC loans, ecommerce payment collection) against market benchmarks and arm's-length principles | CFO + Controller | CEO | Annually (during budget cycle, W26) |
| Update transfer pricing rules in system for new fiscal year; prepare and store transfer pricing documentation per BIR RR 19-2020 requirements | Controller | CFO | Annually |
| CFO approves updated IC pricing; system updates IC invoice generation rules effective new fiscal year | CFO | CEO | Annually |

### Staffing Implication
- IC processing adds ~6–8 hours/month to the Chief Accountant's workload. No dedicated IC clerk needed — it's absorbed into the month-end close cycle within the current ~35-person Finance team.

---



---

## W21. Capital Expenditure (Capex) Request & Approval

| Field | Detail |
|---|---|
| **Trigger** | Need identified for asset acquisition (equipment, vehicles, fixtures, IT hardware, store build-out) |
| **Frequency** | ~50–80 capex requests/year |
| **Volume** | Peaks during new store openings (W16) and annual budget cycle |
| **Owner** | Requesting Department Head |
| **Participants** | Requestor, Department Head, Finance (Capex Analyst), CFO, CEO/Board |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Requestor submits capex request: item description, justification, quotations (min. 3), expected useful life, budget code | Requestor | Dept. Head | 30 min |
| 2 | Department Head reviews and approves or returns for revision | Dept. Head | Dept. Head | 15 min |
| 3 | Finance (Capex Analyst) validates against approved annual budget; checks ROI calculation | Capex Analyst | CFO | 30 min |
| 4 | Route for approval per tiered matrix (see below) | System | As per tier | 15–30 min |
| 5 | Approved capex → Purchase Order created (standard PO workflow W2) or direct purchase | Buyer / Requestor | Dept. Head | Per W2 |
| 6 | Goods/asset received; Goods Receipt posted | Receiving Clerk / IT | Dept. Head | Per W3 |
| 7 | Finance capitalizes asset in Fixed Asset module: asset tag, location, depreciation schedule, useful life | Cost Accountant | Controller | 15 min/asset |
| 8 | System begins monthly depreciation per schedule | System | — | Automated |
| 9 | Post-implementation review: actual vs. budgeted cost; in-service date | Capex Analyst | CFO | Quarterly |

### Approval Matrix

| Amount | Approval Required |
|---|---|
| ≤ PHP 100,000 | Finance Manager |
| PHP 100,001 – 500,000 | CFO |
| PHP 500,001 – 5,000,000 | CEO |
| > PHP 5,000,000 | Board of Directors |

### System Touchpoints
- Capex request form with quotation attachments (W21.1)
- Tiered approval workflow (W21.4)
- Budget availability check against annual capex budget (W21.3)
- PO creation from approved capex (W21.5)
- Fixed Asset creation and capitalization (W21.7)
- Depreciation schedule auto-generation (W21.8)
- Capex vs. budget reporting (W21.9)

### Staffing Implication
- **1 Capex Analyst** (within Finance): 50–80 requests/year. Each requires ~30 min validation. ~40 hours/year = ~1 day/month. Absorbed by existing Finance team (~35). May be the Cost Accountant or a dedicated analyst role during peak store-opening periods.

---



---

## W24. Trade & Corporate Credit Application

| Field | Detail |
|---|---|
| **Trigger** | Customer applies for trade or corporate credit account |
| **Frequency** | ~100–150 new credit applications/month |
| **Volume** | ~5,200 active trade accounts; ~200 corporate accounts |
| **Owner** | AR Supervisor |
| **Participants** | Sales Rep, AR Clerk, AR Supervisor, Finance Manager, Credit Committee |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer submits credit application (in-store, via Sales Rep, or online form) | Customer / Sales Rep | AR Clerk | 15 min |
| 2 | AR Clerk verifies application completeness: business registration, financial statements, trade references | AR Clerk | AR Supervisor | 30 min |
| 3 | AR Clerk runs credit check (bank references, trade references, external credit bureau if available) | AR Clerk | AR Supervisor | 30 min |
| 4 | AR Clerk prepares credit assessment with recommended limit and terms | AR Clerk | AR Supervisor | 15 min |
| 5 | Approval per tier (see matrix below) | Approver | Approver | 10–30 min |
| 6 | System creates customer account with approved credit limit, payment terms, and entity assignment | AR Clerk | AR Supervisor | 15 min |
| 7 | Customer notified of approval; account activated | AR Clerk | — | 10 min |
| 8 | Annual credit review: AR Clerk reviews all accounts for limit adjustment (increase, decrease, or suspension) | AR Clerk | AR Supervisor | 5 min/account |

### Credit Approval Matrix

| Credit Limit | Approver |
|---|---|
| ≤ PHP 200,000 | AR Supervisor |
| PHP 200,001 – 1,000,000 | Finance Manager |
| > PHP 1,000,000 | Credit Committee (CFO + Finance Manager + AR Supervisor) |

### System Touchpoints
- Credit application form (online or in-store) (W24.1)
- Customer master creation with credit limit, payment terms, entity assignment, and VAT treatment classification (W24.6)
- VAT treatment per customer account: AR Clerk classifies account as Standard (12% VAT), VAT-Exempt (government agencies with BIR ruling, PEZA-registered entities), or Zero-Rated (export sales) during account setup based on supporting documents (BIR ruling, PEZA certificate, government purchase order, diplomatic note); system stores VAT treatment in customer master; applied automatically at POS (W5b.4c) and AR invoicing (W8) (W24.6)
- Credit limit enforcement at POS/sales order (W24.6 → W8.3)
- Annual credit review scheduling and workflow (W24.8)

### Staffing Implication
- **AR Clerks** (3–4): 100–150 applications/month × ~90 min each = 150–225 hours/month. Spread across 3–4 clerks = ~50 hours/clerk/month. Absorbed within existing AR team workload, primarily in the first half of the month when collection activity is lighter.

---



---

## W25. Petty Cash Management

| Field | Detail |
|---|---|
| **Trigger** | Small expense incurred at store or DC that cannot go through standard PO/AP process |
| **Frequency** | ~10–15 petty cash disbursements per store per month; ~2,000–3,000/month chain-wide |
| **Volume** | PHP 20,000 float per store; PHP 50,000 float per DC |
| **Owner** | Store Manager / DC Supervisor |
| **Participants** | Employee (requestor), Store Manager, Petty Cash Custodian, AP Clerk |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Employee requests petty cash for small expense (supplies, minor repairs, transport, miscellaneous) | Employee | Store Manager | 5 min |
| 2 | Store Manager approves request (verifies business purpose) | Store Manager | Store Manager | 5 min |
| 3 | Petty Cash Custodian disburses cash; employee signs petty cash voucher | Custodian | Store Manager | 5 min |
| 4 | Employee provides receipt and any change back to Custodian | Employee | — | 5 min |
| 5 | Custodian records transaction in petty cash log (physical or system) | Custodian | Store Manager | 5 min |
| 6 | When fund runs low (~70% disbursed): Custodian prepares replenishment request with all vouchers | Custodian | Store Manager | 30 min |
| 7 | Store Manager reviews vouchers; approves replenishment | Store Manager | Store Manager | 15 min |
| 8 | AP Clerk processes replenishment; creates petty cash voucher in system; posts expense to GL | AP Clerk | AP Supervisor | 15 min |
| 9 | Treasury / bank transfers replenishment amount to store custodian | Treasury Analyst | CFO | 10 min |
| 10 | Monthly: Custodian reconciles petty cash (cash on hand + outstanding vouchers = fund amount) | Custodian | Store Manager | 15 min |

### System Touchpoints
- Petty cash voucher recording (W25.5)
- Replenishment request and approval workflow (W25.6–7)
- GL posting for petty cash expenses (W25.8)
- Petty cash reconciliation reporting (W25.10)
- Store disbursement request for mid-range expenses (PHP 5,000–50,000): for expenses too large for petty cash but not suited to formal PO (emergency equipment repair, small equipment purchase, local contractor services, urgent supplies) — Store Manager or Department Supervisor submits disbursement request in system with business justification, vendor quotation (if available), and cost center; approval per tier (Store Manager approves up to PHP 20,000; Regional Manager approves PHP 20,001–50,000); upon approval, Custodian pays vendor and obtains receipt; AP Clerk posts expense with receipt attachment to GL; disbursements tracked per store per month in expense summary report; distinct from petty cash (W25.1–4) in requiring formal system request and approval before payment, and from PO-based purchasing (W2) in bypassing the PO/GR/invoice cycle for immediacy (W25)

### Staffing Implication
- **Petty Cash Custodian**: Typically the Assistant Store Manager or a designated cashier. Not a separate role.
- **AP impact**: ~2,000–3,000 replenishment requests/year. Most stores replenish once or twice monthly. Absorbed by existing AP clerks.

---



---

## W26. Annual Budget Preparation & Monthly Variance Review

| Field | Detail |
|---|---|
| **Trigger** | Annual budget calendar (typically Q4 for following year) |
| **Frequency** | Annual budget cycle; monthly variance review |
| **Volume** | 5 entities × 200+ cost centers; ~500–800 GL accounts per entity |
| **Owner** | Controller |
| **Participants** | Controller, CFO, Department Heads, Category Managers (merchandising budget), Store Ops Director (store-level budget), HR (payroll budget), IT (capex budget) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | CFO issues budget circular with guidelines, assumptions (revenue growth, inflation, headcount plan, new store openings) | CFO | CEO | 1 week |
| 2 | Department Heads prepare department-level budget: opex, headcount, capex requests | Dept. Heads | VP / C-Suite | 2–3 weeks |
| 3 | Category Managers prepare merchandise purchase budget by category (COGS, margin targets, inventory levels) | Category Manager | VP Merchandising | 1–2 weeks |
| 4 | Store Ops Director prepares store-level P&L budgets (revenue per store, labor, utilities, shrinkage) | Store Ops Director | COO | 1–2 weeks |
| 5 | HR prepares payroll budget (salary adjustments, new hires, statutory increases) | HR Head | CHRO | 1 week |
| 6 | Controller consolidates all department budgets into draft company budget per entity | Controller | CFO | 1 week |
| 7 | CFO and CEO review consolidated draft; negotiate adjustments with Department Heads | CFO / CEO | CEO | 1–2 weeks |
| 8 | Board approves annual budget | Board | CEO | 1 meeting |
| 9 | System loads approved budget per entity, per cost center, per GL account (monthly phasing) | Controller / System | CFO | 2–3 days |
| 10 | Monthly: Controller generates budget vs. actual report per entity and consolidated | Controller | CFO | 2 hours/month |
| 11 | Department Heads review their variances; provide explanations for material deviations (> 10%) | Dept. Heads | VP / C-Suite | 1 hour/month each |
| 12 | CFO reviews consolidated variance report; identifies risks and corrective actions | CFO | CEO | 1 hour/month |
| 13 | Quarterly: if material changes warranted, Controller prepares budget revision for CFO/Board approval | Controller | CFO | 4 hours/quarter |

**Total annual budget cycle**: ~8–10 weeks (Q4)
**Monthly variance review**: ~1 day total effort across Finance and Department Heads

### System Touchpoints
- Budget entry by department, cost center, GL account with monthly phasing (W26.2–5)
- Consolidation of department budgets into entity and group budgets (W26.6)
- Budget loading and lock-down after Board approval (W26.9)
- Budget vs. actual reporting with variance % and drill-down (W26.10–11)
- Budget revision workflow with approval (W26.13)
- Budget availability check during PO and capex creation (links to W2, W21)

### Staffing Implication
- **Controller**: Owns the budget process. ~30 hours during annual cycle + ~4 hours/month for variance review.
- **Department Heads**: ~3–5 hours each during annual cycle + ~1 hour/month variance review. Absorbed into existing management duties.
- No additional headcount needed.

---



---

## W30. Daily Treasury & Cash Position Management

| Field | Detail |
|---|---|
| **Trigger** | Daily treasury operations cycle |
| **Frequency** | Daily |
| **Volume** | 200 stores + 5 DCs + HQ cash positions; ~210 bank accounts total across 4 banks (BDO, BPI, Metrobank, Chinabank) and 5 entities: ~200 store deposit accounts (1 per store for daily cash collection), 5 DC operating accounts, 5 entity main operating accounts, 5 USD import accounts, and additional payroll, savings, and investment accounts per entity |
| **Owner** | Treasury Analyst |
| **Participants** | Treasury Analyst, Store Managers (cash deposits), CFO, Banks |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Store Managers prepare daily cash deposit from POS takings per W5f; armored car or bank branch deposit | Store Manager | COO | 30 min/day per store |
| 2 | System imports daily bank statements from all bank accounts (BDO, BPI, Metrobank, Chinabank) via BPI BizLink, BDO Corporate, or equivalent bank APIs | System | Treasury Analyst | Automated (daily) |
| 3 | Treasury Analyst reviews daily cash position report: bank balances per entity, pending inflows (store deposits), pending outflows (AP payment runs, payroll) | Treasury Analyst | CFO | 30 min/day |
| 4 | System auto-matches store cash deposits to expected amounts from Z-reports; flags shortages or delayed deposits | System | Treasury Analyst | Automated |
| 5 | Treasury Analyst identifies surplus or deficit per entity; recommends inter-entity cash transfers or short-term placements | Treasury Analyst | CFO | 15 min/day |
| 6 | If inter-entity transfer needed: Treasury Analyst initiates transfer with CFO approval; system posts IC loan entry | Treasury Analyst | CFO | 15 min/transfer |
| 7 | Twice weekly: Treasury executes cash sweep from store collection accounts to main operating accounts per entity | Treasury Analyst | CFO | 30 min/run |
| 8 | Weekly: Treasury prepares cash flow forecast (2-week rolling) based on AP aging, AR collection schedule, payroll dates, and capex commitments | Treasury Analyst | CFO | 2 hours/week |
| 9 | Monthly: Treasury reconciles all bank accounts per entity; posts bank charges, interest income, FX gains/losses | Treasury Analyst | Controller | 1 day/month |
| 10 | Import payments: Treasury manages USD accounts; executes FX conversions for import vendor payments based on LC/TT schedule | Treasury Analyst | CFO | As needed |
| 10a | **FX hedging policy**: CFO defines and documents the company's FX risk management strategy — (a) natural hedging: match USD payables (import POs per W2b) with USD receivables where possible; maintain USD bank account balances sufficient to cover near-term import payment obligations (typically 30–60 day forward cover); (b) forward contracts: for large committed import orders (> PHP 5M equivalent), Treasury Analyst may purchase USD forward contracts through the banking relationship to lock in exchange rate at PO creation date; forward contract details (notional amount, forward rate, maturity date, counterparty bank) recorded in system; (c) policy limits: unhedged FX exposure limited to 30-day rolling average of import payments; CFO approves all forward contracts; no speculative FX positions permitted (hedging only for committed import payables); (d) monthly: Treasury Analyst prepares FX exposure report — total USD payables outstanding, USD bank balances, forward contracts in place, net unhedged exposure, unrealized FX gain/loss on open forward contracts; included in weekly cash flow forecast (W30 step 8); (e) at forward contract maturity: Treasury settles with bank; system posts settlement with realized FX gain/loss vs. forward rate | Treasury Analyst / CFO | CFO | Monthly review + as needed for forward contracts |

### System Touchpoints
- Multi-bank statement import (BDO, BPI, Metrobank, Chinabank) via file formats or API (W30.2)
- Daily cash position dashboard per entity and consolidated (W30.3)
- Store cash deposit auto-matching to Z-report amounts (W30.4)
- Cash-in-transit confirmation: system records armored car pickup or bank deposit confirmation per store; auto-matches deposit amount to Z-report cash total; flags unmatched or short deposits for investigation (W30.4, cross-reference W5f.5a)
- Cash sweep scheduling and execution (W30.7)
- Rolling cash flow forecast (W30.8)
- Bank reconciliation per entity (W30.9; also linked to W9a step 9)
- Multi-currency (PHP/USD) account management with FX conversion tracking (W30.10)
- Petty cash reconciliation link: store-level petty cash replenishments (W25) are included in the daily cash position report (W30 step 3) as pending outflows; Treasury Analyst sees replenishment requests in the weekly cash flow forecast (W30 step 8); replenishment payments confirmed via bank transfer are auto-matched to store deposit accounts during bank reconciliation (W30 step 9); monthly petty cash replenishment totals per store are visible on the Treasury dashboard for monitoring unusual patterns (W30)
- Store-level cash position tracking: system aggregates per-store daily cash deposits (W5f), petty cash replenishments (W25), and store disbursement requests (W25 store disbursement) into a consolidated store cash movement report; Treasury Analyst reviews as part of daily cycle to detect unusual cash patterns at individual stores (W30)
- Bank account lifecycle management: Treasury Analyst maintains bank account register across all entities (~210 accounts: 200 store deposit accounts, 5 DC operating accounts, 5 entity main operating accounts, 5 USD import accounts, and additional payroll, savings, and investment accounts); new account opening triggered by new store (W16), new entity setup, or new banking relationship — Treasury Analyst submits account opening request to bank with Board Resolution (per entity), authorized signatory list, and business registration documents; signatory management: system tracks authorized signatories per account with signatory tier (single signatory, dual signatory, any-two-of-three); when a signatory changes role or separates (W43), Treasury Analyst updates bank signatory list within 10 business days — system alerts on signatory staleness (no update in > 12 months); account closure triggered by store closure (W45), account consolidation, or bank relationship termination — Treasury Analyst confirms zero balance, obtains bank closure confirmation, and deactivates account in system; system logs all account openings, signatory changes, and closures with full audit trail (W30)

### Staffing Implication
- **2–3 Treasury Analysts**: Daily cash position (30 min) + sweep execution (30 min × 2/week) + weekly forecast (2 hours) + monthly bank reconciliation (1 day) + import payments + inter-entity transfers. This is a full-time role for 2 analysts with a 3rd covering during peaks (month-end, import payment seasons).
- **Store Managers**: Daily cash deposit preparation adds ~30 min to closing routine — absorbed into W5f.

---



---

## W35. Management Reporting Rhythm

| Field | Detail |
|---|---|
| **Trigger** | Reporting calendar (daily, weekly, monthly, quarterly cadences) |
| **Frequency** | Daily flash, weekly review, monthly close reporting, quarterly board pack |
| **Volume** | ~50 standard reports on recurring schedules; ~20 ad-hoc requests/month |
| **Owner** | Controller |
| **Participants** | Controller, CFO, CEO, Department Heads, BI Analyst |

### Steps

### Daily

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 1 | System generates daily flash report (auto-distributed by 7:00 AM): total chain revenue, transactions, avg ticket, same-store sales vs. prior year, top/bottom 10 stores | System | Controller | Daily (automated) |
| 2 | CFO reviews daily flash on mobile dashboard | CFO | — | 5 min/day |
| 3 | System generates daily inventory exception report: negative stock alerts, stockouts at store level, critical DC shortages | System | Supply Planning Manager | Daily (automated) |

### Weekly

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 4 | Week-on-week sales report by store, category, and channel (POS vs. ecommerce); auto-distributed every Monday | System | Controller | Weekly (automated) |
| 5 | Supply chain KPI report: fill rate, on-time delivery (DC→store), PO overdue rate, forecast accuracy | Demand Planner | Supply Planning Manager | Weekly |
| 6 | AP aging summary: total payables, overdue invoices, payment run schedule | AP Supervisor | Controller | Weekly |
| 7 | Treasury: weekly cash flow forecast (W30 step 8) | Treasury Analyst | CFO | Weekly |

### Monthly

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 8 | Financial statements per entity and consolidated (from W9 close process) | Chief Accountant | Controller | Monthly (by day 5) |
| 9 | Budget vs. actual variance report per entity, per department (from W26) | Controller | CFO | Monthly (by day 7) |
| 10 | Store P&L: revenue, COGS, gross margin, labor cost, occupancy, shrinkage, EBITDA per store | System | Store Ops Director | Monthly (by day 7) |
| 11 | Merchandising performance: category sales, margin, inventory turns, sell-through, vendor rebate realization | Pricing Analyst | VP Merchandising | Monthly (by day 7) |
| 12 | AR aging and collections performance: DSO, overdue %, write-offs | AR Supervisor | CFO | Monthly |
| 13 | HR metrics: turnover rate, time-to-fill, absenteeism, overtime hours, headcount vs. plan | HR Head | CHRO | Monthly |
| 14a | Store utility consumption report: system aggregates per-store utility expense (electricity, water, internet) from non-PO invoice data (W7c); benchmarks kWh per sqm per store per month; flags stores with utility consumption > 20% above peer average (same store format, same region) for investigation — potential causes include equipment malfunction (W47), HVAC inefficiency, or unauthorized usage; Store Manager receives monthly utility scorecard as part of Store Performance Scorecard (W67); Facilities Coordinator investigates flagged stores and recommends corrective action (equipment upgrade, behavioral changes) | System / Facilities Coordinator | Store Ops Director | Automated + 2 hours/month review |
| 14 | Management committee meeting: CFO presents consolidated results; Department Heads present functional KPIs | CFO / Dept. Heads | CEO | Monthly (by day 10) |

### Quarterly

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 15 | Board pack preparation: consolidated financials, management discussion & analysis, KPI scorecard, risk register update | Controller + CFO | CEO | Quarterly |
| 16 | Vendor performance scorecard review (W44) | Buyer | VP Merchandising | Quarterly |
| 17 | Budget revision (if material changes warranted) (W26 step 13) | Controller | CFO | Quarterly |
| 18 | **Document retention compliance review**: Controller verifies that all document types (invoices, receipts, delivery receipts, import docs, capex records) meet 7-year BIR retention requirements; confirms expired documents are archived and accessible; flags any gaps in document attachment compliance | Controller | CFO | Quarterly |
| 19 | **Credit note / debit note aging review**: Chief Accountant presents summary of unapplied AP and AR credit memos > 60 days; Controller reviews resolution status; material unresolved items escalated to CFO | Chief Accountant / Controller | CFO | Quarterly |

### Ad-Hoc

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 20 | Department Heads request ad-hoc reports from BI Analyst or self-service via report builder | Dept. Heads / BI Analyst | — | As needed (~20/month) |
| 21 | BI Analyst creates custom analyses: product affinity, customer segmentation, promotional lift analysis, geographic trends | BI Analyst | Requestor | As needed |

### System Touchpoints
- Scheduled report auto-generation and distribution (email, portal, mobile) (W35.1, 4, 8–13)
- Executive dashboard with real-time KPIs (W35.2)
- Store P&L module (W35.10)
- Self-service report builder / ad-hoc query tool (W35.18)
- Mobile dashboard for executives (W35.2)
- Integration with all ERP modules (financials, inventory, POS, procurement, HR, ecommerce) for data aggregation
- Store P&L occupancy cost allocation: store rent is a direct charge per location based on individual lease agreements with Property Mgmt Inc. (not allocated from a pool); DC warehousing and distribution costs (IC payment to Logistics Inc. per W14) are allocated to stores monthly based on a configurable allocation key (recommended: proportional to replenishment order value or volume per store); utility costs are direct charges per store (each location has its own meter/account); corporate overhead from Holdings Inc. (management fees per W14) is shown as a separate line below store EBITDA, not embedded in store-level P&L; system auto-generates store P&L with all cost lines from configurable allocation rules
- Store-level budget variance tracking: annual budget (W26) is phased monthly per store with revenue, COGS, labor, occupancy, and shrinkage targets; system generates monthly store budget vs. actual report with variance flags (revenue > ±5%, gross margin > ±2%, operating expense > +10%); Regional Manager reviews store-level budget variance with Store Manager during monthly store visit; significant variances escalated to VP Store Operations; store-level budget accountability is a standing agenda item in monthly management committee meeting (W35.14)

### Staffing Implication
- **1 BI Analyst** (within IT or Finance): Handles ~20 ad-hoc requests/month + maintains standard report templates + supports self-service tool adoption. This may be a new role or absorbed by a data-savvy Finance team member.
- **Controller**: Monthly reporting adds ~8 hours/month (review + variance analysis + board pack quarterly). Absorbed into existing duties.
- Most standard reports are auto-generated; the human effort is in review, interpretation, and action.

---



---

## W39. Fixed Asset Disposal & Retirement

| Field | Detail |
|---|---|
| **Trigger** | Asset reaches end of useful life, becomes uneconomic to maintain, or is replaced by new asset |
| **Frequency** | ~50–100 asset disposals/year; peaks during store renovations and IT refresh cycles |
| **Volume** | ~8,050 fixed assets across all entities (POS terminals, forklifts, vehicles, fixtures, IT servers, office equipment) |
| **Owner** | Cost Accountant |
| **Participants** | Cost Accountant, Requestor (dept), CFO, IT (for IT assets), Procurement (if resale), Legal (if land/building) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Requestor identifies asset for disposal: reason (end of life, beyond repair, obsolete, replacement, store closure) | Requestor (Dept. Head) | Dept. Head | 15 min |
| 2 | Cost Accountant reviews asset record: original cost, accumulated depreciation, net book value (NBV), remaining useful life, any outstanding encumbrances | Cost Accountant | Controller | 15 min/asset |
| 3 | If NBV is material (> PHP 50,000): Requestor obtains disposal valuation or market quotation for resale | Requestor | Dept. Head | 1–2 hours |
| 4 | Disposal request routed for approval per tier: (a) NBV ≤ PHP 50,000: Controller, (b) NBV PHP 50,001–500,000: CFO, (c) NBV > PHP 500,000: CEO, (d) Land/building: Board | Approver | Approver | 15–30 min |
| 5 | Cost Accountant determines disposal method: (a) trade-in (against new asset purchase), (b) public sale/auction, (c) scrap/recycle, (d) donation, (e) write-off (no residual value) | Cost Accountant | Controller | 15 min/asset |
| 6 | If sale: Procurement or Admin conducts sale; system records proceeds | Procurement / Admin | Controller | Varies |
| 7 | If IT asset: IT ensures data wipe and compliance with Data Privacy Act (RA 10173) before physical disposal | IT Team | CIO | 30 min/asset |
| 8 | Physical disposal or handover executed; asset tag removed; documented with photos | Requestor / Admin | Dept. Head | 30 min/asset |
| 9 | Cost Accountant posts disposal entry in system: (a) remove asset at original cost from fixed asset register, (b) remove accumulated depreciation, (c) recognize gain/loss on disposal = proceeds − NBV (or NBV if scrapped), (d) post to GL disposal P&L account | Cost Accountant | Controller | 15 min/asset |
| 10 | System updates fixed asset register; asset status changed to "Disposed" with disposal date; asset no longer depreciated | System | — | Automated |
| 11 | Quarterly: Cost Accountant reviews disposed assets report; reconciles disposal gain/loss to GL | Cost Accountant | Controller | 30 min/quarter |

### System Touchpoints
- Fixed asset disposal workflow with approval tiers (W39.4)
- Asset record with NBV calculation at any point (W39.2)
- Disposal entry auto-generation: cost removal, depreciation reversal, gain/loss calculation (W39.9)
- Asset status lifecycle: Active → Pending Disposal → Disposed (W39.10)
- Disposal gain/loss reporting (W39.11)
- Integration with W21 (Capex → Asset creation) for full asset lifecycle tracking

### Staffing Implication
- **Cost Accountant**: 50–100 disposals/year × ~30 min each = ~25–50 hours/year = ~2–4 hours/month. Absorbed within existing Finance team.
- No incremental headcount needed.

---



---

## W59. Insurance Policy Lifecycle Management

| Field | Detail |
|---|---|
| **Trigger** | Annual insurance renewal cycle; or new insurance requirement (new store, new asset, regulatory change) |
| **Frequency** | Annual renewals; ~20–30 active policies across the group |
| **Volume** | Policy types: property (200 stores + 5 DCs), inventory (PHP 8–10B total), business interruption, general liability, vehicle fleet (30–40 owned), workers' compensation, employer's liability, cargo/in-transit, cyber liability, directors & officers (D&O) |
| **Owner** | Treasury Analyst (policy administration); CFO (coverage decisions) |
| **Participants** | Treasury Analyst, CFO, Facilities Coordinator, Fleet Manager, IT, Legal, external insurance broker |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System maintains insurance policy register: policy number, insurer, type, coverage amount, premium, deductible, renewal date, key terms and exclusions, broker contact | Treasury Analyst | CFO | 4 hours/year (maintenance) |
| 2 | System alerts Treasury Analyst 90 days before each policy renewal date | System | — | Automated |
| 3 | Treasury Analyst coordinates with insurance broker to obtain renewal quotation and market comparison; broker provides at least 2 alternative quotes for material policies (annual premium > PHP 500K) | Treasury Analyst | CFO | 1–2 hours/policy |
| 4 | CFO reviews coverage adequacy annually: (a) property coverage vs. current replacement cost of stores and DCs, (b) inventory coverage vs. current inventory value, (c) fleet coverage vs. current vehicle count, (d) business interruption coverage vs. current revenue run rate, (e) cyber liability adequacy given data volumes | CFO | CEO | 2–4 hours/year |
| 5 | CFO approves or adjusts coverage; authorizes Treasury Analyst to renew or switch insurer | CFO | CEO | 1 hour |
| 6 | Treasury Analyst processes premium payment per W7c (non-PO invoice) or against insurance broker PO; system posts premium to GL (Dr. Prepaid Insurance / Cr. Cash); monthly amortization per W9a step 8 | Treasury Analyst | CFO | 15 min/policy |
| 7 | Claims: when an insured event occurs (W3.6a goods damage, W49 typhoon damage, W37 confirmed theft, W52 vehicle accident), the process owner files claim with supporting documentation; Treasury Analyst tracks claim status in system; upon settlement, Finance posts recovery (Dr. Cash / Cr. Insurance Recovery Income or Cr. relevant asset/expense account) | Process Owner / Treasury Analyst | CFO | Per event |
| 8 | Monthly: Treasury Analyst reviews claims activity report: open claims, settlement status, claims vs. premiums ratio; flags policies where claims experience may affect renewal terms | Treasury Analyst | CFO | 30 min/month |
| 9 | Annual: CFO and external broker review claims history, coverage adequacy, and market conditions; adjust policy structure for upcoming year | CFO + Broker | CEO | 2 hours/year |

### System Touchpoints
- Insurance policy register with renewal calendar, coverage details, and document storage (W59.1)
- Automated renewal alerting at 90, 60, and 30 days (W59.2)
- Claims tracking with status lifecycle: Filed → Under Investigation → Approved → Settled / Denied; linked to triggering event (W3.6a, W49, W37) (W59.7)
- Premium payment processing and prepaid insurance amortization (W59.6)
- Claims vs. premium ratio reporting (W59.8)
- Integration with W3.6a (receiving damage), W25 (petty cash for minor incidents below deductible), W37 (theft write-off), W39 (asset disposal — insurance recovery on disposed assets), W47 (facility damage), W49 (disaster damage), W52 (vehicle insurance)

### Staffing Implication
- **Treasury Analyst**: adds ~4–6 hours/year for policy administration + ~30 min/month for claims review. Absorbed within existing Treasury team (2–3 analysts).
- **Insurance broker**: external partner managing market comparison, policy placement, and claims advocacy.

---



---

## W70. Credit Note & Debit Note Aging Reconciliation

| Field | Detail |
|---|---|
| **Trigger** | Month-end close (W9a step 16e) and weekly AP/AR aging review |
| **Frequency** | Weekly aging review (AP and AR); monthly formal reconciliation during close; quarterly deep review in management reporting (W35) |
| **Volume** | ~100–200 open credit/debit notes at any time across AP and AR |
| **Owner** | Chief Accountant |
| **Participants** | AP Clerk, AR Clerk, AP Supervisor, AR Supervisor, Chief Accountant, Controller |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates credit/debit note aging report across AP and AR: note number, vendor/customer, amount, date created, source (RTV, rebate, price protection, pricing error, volume discount, complaint resolution, promotional adjustment), status (unapplied / partially applied), and age bucket (0–30, 31–60, 61–90, 90+ days) | System | — | Automated |
| 2 | **AP credit memos** (vendor credits): AP Clerk reviews unapplied vendor credit memos weekly; for each: (a) if vendor has open invoices, applies credit to oldest invoice — system reduces vendor balance; (b) if vendor has no open invoices, contacts vendor to request refund or confirms credit will be applied to next invoice; (c) if credit > 90 days and vendor is unresponsive, escalates to AP Supervisor for write-off decision | AP Clerk | AP Supervisor | 30 min/week |
| 3 | **AR credit memos** (customer credits): AR Clerk reviews unapplied customer credit memos weekly; for each: (a) if customer has open invoices, applies credit to oldest invoice; (b) if customer has no open invoices, contacts customer to arrange refund or confirm credit for next purchase; (c) if credit > 90 days and customer is unresponsive, escalates to AR Supervisor for write-off as other income | AR Clerk | AR Supervisor | 30 min/week |
| 4 | **AP debit memos** (vendor chargebacks): AP Clerk reviews open debit memos — these represent amounts BuildRight is deducting from vendor payments (short shipments, damage claims, pricing disputes); confirms debit memos are resolved with next vendor payment; unresolved debits > 60 days escalated to Buyer for vendor negotiation | AP Clerk | AP Supervisor | 15 min/week |
| 5 | **AR debit memos** (customer chargebacks): AR Clerk reviews open AR debit memos — these represent amounts owed by customers beyond normal invoices (bounced checks, disputed deductions); follows up with customer per W8 collection tiers; unresolved debits > 90 days escalated to Finance Manager for bad debt provision | AR Clerk | AR Supervisor | 15 min/week |
| 6 | **Month-end reconciliation** (W9a step 16e): Chief Accountant reviews total unapplied credit/debit note balances; confirms AP credit memo sub-ledger agrees with GL Accounts Payable; confirms AR credit memo sub-ledger agrees with GL Accounts Receivable; unresolved items > 90 days summarized for Controller | Chief Accountant | Controller | 1 hour/month |
| 7 | **Quarterly deep review** (W35 step 19): Chief Accountant presents credit/debit note aging summary to Controller and CFO; highlights chronic vendors/customers with recurring unapplied credits; recommends process improvements (e.g., auto-application rules, vendor/customer communication templates); material write-offs approved per standard tiers | Chief Accountant / Controller | CFO | 30 min/quarter |

### System Touchpoints
- Credit/debit note aging report with AP and AR views; filterable by age, vendor/customer, source, and status (W70.1)
- Auto-application rules: system auto-applies credit memos to oldest open invoices for the same vendor/customer if configured; manual override available (W70.2–3)
- Sub-ledger to GL reconciliation: AP/AR credit memo sub-ledger totals reconcile to GL control accounts (W70.6)
- Write-off workflow for stale credits/debits: tiered approval (AR/AP Supervisor ≤ PHP 50K, Controller ≤ PHP 200K, CFO > PHP 200K); system posts write-off with GL entry (W70.2–5)
- Chronic vendor/customer analysis: identifies accounts with recurring unapplied credits over rolling 12-month period (W70.7)
- Integration with W7 (AP credit memos from vendor), W7.9b (vendor credit memo processing), W8 (AR credit memos), W8.11 (customer credit memo processing), W9a.16e (month-end credit note reconciliation), W35.19 (quarterly review)

### Staffing Implication
- **AP Clerk**: adds ~30 min/week for AP credit memo review. Absorbed.
- **AR Clerk**: adds ~30 min/week for AR credit memo review. Absorbed.
- **Chief Accountant**: adds ~1 hour/month + 30 min/quarter for reconciliation. Absorbed within month-end close duties.
- No incremental headcount.

---



---

## W80. FX Hedging & Forward Contract Management

| Field | Detail |
|---|---|
| **Trigger** | Import purchase order confirmed with USD vendor (W2b); or quarterly FX exposure review |
| **Frequency** | Forward contracts placed as needed (typically monthly or quarterly aligned with import PO schedule); quarterly exposure review |
| **Volume** | ~40% of COGS from imports ≈ PHP 1.4B/month; USD-denominated payables ~PHP 600M–1B/month at current exchange rates; ~10–20 active forward contracts at any time |
| **Owner** | Treasury Analyst |
| **Participants** | Treasury Analyst, CFO, Import Coordinator, Cost Accountant |

### Background

BuildRight's import purchasing (~40% of COGS) is primarily denominated in USD, exposing the company to PHP/USD exchange rate fluctuations. With import lead times of 45–90 days (W2b), the company faces FX risk from PO creation through LC payment. The company's FX hedging policy is conservative: hedging is limited to covering committed import payables (no speculative positions). Forward contracts are the primary hedging instrument.

### Policy
- **Hedging scope**: Only committed import payables (POs confirmed with vendor) — no speculative positions
- **Hedging ratio target**: 50–80% of forecasted USD payables for the next 90 days
- **Counterparty banks**: BDO, BPI, Metrobank (same banks used for operational accounts per FIN-009)
- **Maturity matching**: Forward contract maturity dates aligned with expected LC/TT payment dates per W2b
- **Approval**: Forward contracts ≤ USD 500K → CFO; > USD 500K → CEO

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Exposure identification**: system generates FX exposure report from open import POs (W2b) — for each open import PO with USD or other foreign-currency denomination: PO number, vendor, foreign currency amount, PHP equivalent at budget rate, expected payment date, current spot rate, unrealized FX gain/loss | System | Treasury Analyst | Automated (weekly) |
| 2 | Treasury Analyst reviews FX exposure report; identifies payables requiring hedge coverage based on policy (hedging ratio target, maturity horizon) | Treasury Analyst | CFO | 30 min/week |
| 3 | Treasury Analyst obtains forward contract quotations from 2–3 counterparty banks for required tenors and amounts | Treasury Analyst | CFO | 30 min/hedge |
| 4 | Treasury Analyst selects bank based on: (a) forward rate competitiveness, (b) counterparty credit risk (bank credit rating), (c) existing facility limits and available margin; prepares forward contract recommendation: notional amount, forward rate, maturity date, counterparty bank, corresponding import PO reference(s) | Treasury Analyst | CFO | 15 min/hedge |
| 5 | CFO approves forward contract; if notional > USD 500K, CEO approval required | CFO / CEO | CEO | 15 min/hedge |
| 6 | Treasury Analyst executes forward contract with selected bank; receives contract confirmation; records forward contract in system: contract number, counterparty bank, notional amount (USD), forward rate (PHP/USD), trade date, maturity date, settlement type (physical delivery or cash net settlement), linked import PO reference(s) | Treasury Analyst | CFO | 15 min/hedge |
| 7 | **Ongoing monitoring**: weekly, Treasury Analyst reviews forward contract portfolio vs. open USD payables — (a) hedge coverage ratio (total forward notional ÷ total USD payables), (b) MTM (mark-to-market) gain/loss per forward contract using current spot rate, (c) maturity ladder — forward contracts maturing in next 30 days flagged for settlement planning | Treasury Analyst | CFO | 30 min/week |
| 8 | **Settlement at maturity**: when import LC/TT payment is due (W2b step 13), Treasury Analyst coordinates forward contract settlement — (a) for physical delivery: forward contract provides USD at contracted rate; bank debits PHP account at forward rate and credits USD for LC/TT payment; (b) for cash net settlement: if spot rate at maturity differs from forward rate, bank pays or receives the difference; Treasury Analyst settles the actual import payment at spot rate and separately receives/pays the forward contract settlement | Treasury Analyst | CFO | 30 min/settlement |
| 9 | **System posting**: at settlement, system posts realized FX hedge result — (a) difference between forward rate and original PO budget rate allocated to the import PO's landed cost (W2b.12) or recognized as FX hedging gain/loss; (b) any premium or discount amortized over the contract period per PFRS 9; (c) system links forward contract settlement to corresponding AP payment for full audit trail | System / Treasury Analyst | Controller | Automated + 15 min review |
| 10 | **Monthly**: Treasury Analyst includes forward contract portfolio summary in monthly cash position report (W30) — total notional, weighted average forward rate, MTM gain/loss, hedge coverage ratio, upcoming maturities | Treasury Analyst | CFO | 30 min/month |
| 11 | **Quarterly**: CFO reviews hedging effectiveness — (a) actual FX cost (hedged vs. unhedged payables), (b) hedge coverage ratio vs. policy target, (c) counterparty concentration, (d) recommendations for hedging strategy adjustments; results presented to CEO quarterly | CFO | CEO | 1 hour/quarter |
| 12 | **Early termination** (exception): if an import PO is cancelled (W2a PO cancellation) and linked forward contract no longer has an underlying payable, Treasury Analyst may: (a) hold forward contract to maturity and use for another import PO (if tenor matches), (b) terminate early with bank and recognize termination gain/loss, or (c) sell forward contract to offset new exposure; early termination requires CFO approval | Treasury Analyst | CFO | 30 min/occurrence |

### System Touchpoints
- FX exposure report from open import POs with unrealized gain/loss (W80.1)
- Forward contract register: contract number, counterparty, notional, forward rate, trade date, maturity, settlement type, linked PO(s) (W80.6)
- MTM (mark-to-market) calculation per forward contract using current spot rate (W80.7)
- Hedge coverage ratio dashboard: forward notional ÷ USD payables with trend (W80.7)
- Settlement posting with realized FX hedge result and PFRS 9 accounting (W80.9)
- Forward contract portfolio summary integrated into monthly cash position report (W80.10)
- Linkage to import PO lifecycle (W2b) and AP payment (W7) for full audit trail
- Integration with W2b (import POs — exposure source), W7 (AP payment), W9a.5a (month-end FX revaluation — forward contracts included in revaluation), W26 (budget — hedging costs budgeted), W30 (treasury — forward contract cash flows)

### Staffing Implication
- **Treasury Analyst**: adds ~1–2 hours/week for FX exposure monitoring, forward contract management, and settlement. With 2 Treasury Analysts on the team, this is absorbed.
- **CFO**: adds ~1 hour/quarter for hedging effectiveness review. Absorbed.
- No incremental headcount.

---



---

## W81. Bad Debt Provisioning, Write-Off & Recovery

| Field | Detail |
|---|---|
| **Trigger** | Monthly AR aging review; or specific account identified for write-off after collection escalation (W8.8a) |
| **Frequency** | Monthly provision review; write-offs as needed (typically quarterly batch) |
| **Volume** | ~5,200 trade and corporate AR accounts; target bad debt rate < 0.5% of AR balance; estimated 10–20 write-off events/year |
| **Owner** | AR Supervisor (collections and write-off initiation); Controller (provisioning) |
| **Participants** | AR Supervisor, AR Clerk, Finance Manager, Controller, CFO, Legal, Sales Rep |

### Background

This workflow covers the complete bad debt lifecycle from initial provisioning through write-off and potential recovery. It formalizes and expands the bad debt steps embedded in W8.8a/8b into a standalone process with dedicated BIR documentation, provisioning methodology, and recovery tracking. The AR collection escalation process (W8 steps 6–8a) feeds into this workflow when accounts reach the write-off stage.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Monthly AR aging review**: AR Clerk generates AR aging report by bucket (current, 1–30, 31–60, 61–90, 91–120, > 120 days); identifies accounts > 90 days overdue for bad debt assessment | AR Clerk | AR Supervisor | 30 min/month |
| 2 | **Individual account assessment**: for each account > 90 days overdue, AR Clerk and Sales Rep assess collectibility — (a) customer financial status (still operating, declared bankruptcy, unreachable), (b) collection history (payment promises made and broken, partial payments), (c) dispute status (customer disputes amount vs. simple non-payment), (d) security or collateral held (if any) | AR Clerk / Sales Rep | AR Supervisor | 15 min/account |
| 3 | **Bad debt provision computation**: monthly, Controller computes bad debt provision using: (a) **specific provision**: for individually assessed accounts > 90 days where collection is uncertain — provision at 50–100% of outstanding amount based on assessment, (b) **general provision**: portfolio-level provision based on historical loss rate applied to remaining AR portfolio (e.g., 0.5–1% of total AR not specifically provided); system calculates provision suggestion based on configured aging percentages per bucket | Controller | CFO | 1 hour/month |
| 4 | Controller reviews and approves monthly bad debt provision adjustment; system posts Dr. Bad Debt Expense / Cr. Allowance for Doubtful Accounts (balance sheet contra-asset) | Controller | CFO | 30 min/month |
| 5 | **Write-off trigger**: when all collection efforts exhausted per W8.8a escalation tiers — (a) demand letter sent and no response after deadline, OR (b) external collection agency confirms account uncollectible, OR (c) customer confirmed insolvent/bankrupt (court filing or public record), OR (d) cost of collection exceeds amount recoverable — AR Supervisor initiates formal write-off process | AR Supervisor | Controller | 15 min/account |
| 6 | **Write-off documentation package**: AR Supervisor prepares BIR-compliant write-off documentation: (a) **demand letter**: copy of formal demand letter sent via registered mail with return card, (b) **collection report**: summary of all collection actions taken with dates (phone calls, emails, demand letters, collection agency referral, legal filing if applicable), (c) **account history**: full AR transaction history showing original invoices, payments received, and outstanding balance, (d) **evidence of insolvency** (if applicable): court filing, SEC dissolution notice, or other public record, (e) **write-off recommendation**: amount, reason, and supporting evidence summary | AR Supervisor | Controller | 1–2 hours/account |
| 7 | **Write-off approval**: tiered by amount — (a) ≤ PHP 50,000: Finance Manager + Controller, (b) PHP 50,001–200,000: CFO, (c) PHP 200,001–1,000,000: CEO + CFO, (d) > PHP 1,000,000: Board resolution | Approver(s) | CEO / Board | 15–30 min/write-off |
| 8 | **System posting**: system posts write-off — Dr. Allowance for Doubtful Accounts / Cr. Accounts Receivable (if provision exists) or Dr. Bad Debt Expense / Cr. Accounts Receivable (direct write-off if no prior provision); AR balance reduced; account status changed to "Written Off"; customer blocked from new credit sales; full transaction history retained for 7-year BIR retention | System / AR Clerk | Controller | 5 min/write-off |
| 9 | **Post write-off tracking**: system maintains written-off accounts register — original amount, write-off date, reason, approving authority; written-off accounts excluded from standard AR aging but tracked separately for potential recovery | System | — | Automated |
| 10 | **Recovery — partial or full**: if customer subsequently pays on a previously written-off account — (a) AR Clerk receives payment (cash, bank transfer, or settlement agreement), (b) system posts recovery: Dr. Cash / Cr. Bad Debt Recovery (income — P&L), (c) recovery tracked separately from regular AR collections in GL and reporting, (d) if partial recovery: remaining balance remains in written-off register; if full recovery: account closed | AR Clerk / AR Supervisor | Controller | 10 min/recovery |
| 11 | **Recovery via settlement agreement**: if customer offers reduced settlement (e.g., 60% of outstanding), AR Supervisor negotiates; Finance Manager approves settlement terms; system posts: Dr. Cash (settled amount) / Cr. Bad Debt Recovery (settled amount); remaining written-off balance confirmed as final loss | AR Supervisor / Finance Manager | Controller | 30 min/settlement |
| 12 | **Quarterly**: Controller presents bad debt summary to CFO — (a) provision movement (opening balance + new provisions − write-offs + recoveries), (b) write-off volume and root cause analysis (customer bankruptcy, fraud, collection failure), (c) recovery rate on previously written-off accounts, (d) AR aging trend, (e) adequacy of general provision rate, (f) recommendation for provision rate adjustment if loss experience changes | Controller | CFO | 30 min/quarter |
| 13 | **Annual**: CFO reviews bad debt provisioning methodology with external auditors as part of year-end audit (W9b); auditors assess adequacy of provision against actual loss history; methodology adjustments documented and approved | CFO | Board | 2 hours/year |

### BIR Documentation Requirements

For a bad debt write-off to be deductible for Philippine income tax purposes (per BIR Revenue Regulations), the following must be maintained:
- Proof that the debt was previously reported as income (sales invoices, official receipts)
- Demand letter sent via registered mail with return card
- Documentation of collection efforts (call logs, email correspondence, collection agency reports)
- Court filing (if legal action was pursued)
- Evidence of insolvency or bankruptcy (if applicable)
- Board resolution (for amounts requiring Board approval)
- Write-off approval with sign-off by authorized officer
- All documentation retained for 7 years per BIR retention requirements

### System Touchpoints
- AR aging report with configurable bucket thresholds (W81.1)
- Individual account collectibility assessment with reason codes and supporting notes (W81.2)
- Automated bad debt provision calculator: specific provision per account + general provision based on aging matrix (W81.3)
- Provision posting with GL integration: Dr. Bad Debt Expense / Cr. Allowance for Doubtful Accounts (W81.4)
- Write-off documentation package generation with BIR-required attachments (W81.6)
- Tiered write-off approval workflow (W81.7)
- Write-off posting: provision drawdown or direct expense with AR reduction; account status change to "Written Off" with credit block (W81.8)
- Written-off accounts register with separate tracking from active AR (W81.9)
- Bad debt recovery posting: Dr. Cash / Cr. Bad Debt Recovery (separate P&L line from regular revenue) (W81.10–11)
- Quarterly bad debt summary dashboard: provision movement, write-off analysis, recovery rate, aging trend (W81.12)
- Integration with W8 (AR collections — W8.8a escalation feeds into W81 write-off trigger), W9a (month-end — provision posting included in close), W9b (year-end — bad debt methodology review with auditors), W24 (credit application — written-off customers blocked from new credit), W35 (management reporting — bad debt KPIs), W44 (vendor scorecard — recovery process mirrors vendor collection logic)

### Staffing Implication
- **AR Supervisor**: adds ~2 hours/month for write-off initiation and documentation. Absorbed.
- **Controller**: adds ~1 hour/month for provision review + 30 min/quarter for summary presentation. Absorbed within existing close duties.
- **AR Clerk**: adds ~30 min/month for aging review escalation. Absorbed.
- No incremental headcount.

---



---


## W85. Product Costing & Margin Analysis Review

| Field | Detail |
|---|---|
| **Trigger** | Monthly margin variance review during W9a close; or quarterly assortment review (W1); or ad-hoc triggered by significant vendor cost change (W40) or competitive pricing pressure (W61) |
| **Frequency** | Monthly margin monitoring; quarterly deep-dive review; annual category-level strategy review |
| **Volume** | 35,000 active SKUs across 200 stores + 5 DCs; ~20–25 product categories |
| **Owner** | Cost Accountant |
| **Participants** | Cost Accountant, Controller, Category Managers, Pricing Analysts, VP Merchandising, CFO |

### Background

Product costing and margin analysis is currently fragmented: WAC verification happens during month-end close (W9a.6a), margin impact assessment occurs during price changes (W40.2), and assortment review (W1) considers category-level margin targets. This workflow consolidates these into a structured periodic review that ensures margin erosion is detected early, cost changes are proactively managed, and pricing strategy decisions are data-driven. It bridges the Finance and Merchandising functions.

### Monthly Margin Monitoring (by day 10, after W9a close)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates monthly margin analysis report per category and per SKU: (a) gross margin % by category (current month vs. prior month vs. same month prior year vs. budget), (b) top 50 margin-declining SKUs (by margin % change month-over-month), (c) top 50 margin-improving SKUs, (d) SKUs with gross margin below minimum threshold (configurable per category, typically 15–20%), (e) WAC movement analysis — SKUs with cost change > 5% in the month, (f) promo margin impact: SKUs on promotion during the month with actual vs. planned margin, (g) category-level contribution to total gross profit | System | — | Automated |
| 2 | Cost Accountant reviews margin analysis report; investigates SKUs with margin below threshold or significant margin decline: (a) cost increase not passed to SRP (W40 not executed after cost increase), (b) promotional pricing eroding margin below plan, (c) WAC distortion from small-quantity receipts at high cost, (d) vendor cost change not yet reflected in SRP decision | Cost Accountant | Controller | 2–3 hours/month |
| 3 | Cost Accountant prepares margin exception report for Controller: top 20 margin concerns with root cause analysis and recommended action (SRP increase per W40, vendor negotiation per W44, assortment exit per W68, or accept lower margin with strategic justification) | Cost Accountant | Controller | 1 hour/month |
| 4 | Controller reviews margin exception report with VP Merchandising in monthly margin review meeting; agrees on action items with deadlines; action items tracked in system | Controller / VP Merchandising | CFO | 30 min/month |

### Quarterly Deep-Dive Review (aligned with W1 assortment review)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 5 | Cost Accountant prepares quarterly category margin deep-dive per category: (a) category gross margin % trend over 4 quarters, (b) category margin vs. budget and vs. target, (c) top 10 margin contributors (SKUs generating highest absolute gross profit), (d) bottom 10 margin drags (SKUs with lowest margin % and significant revenue), (e) vendor-level margin analysis — margin by vendor within each category, (f) cost structure breakdown per category: material cost, landed cost components (duty, freight, insurance), (g) import vs. domestic margin comparison, (h) promotional margin impact analysis: average margin during promo periods vs. non-promo periods | Cost Accountant | Controller | 8 hours/quarter |
| 6 | Cost Accountant and Pricing Analyst jointly prepare pricing strategy recommendations per category: (a) categories where SRP increases are recommended (cost has risen but SRP not adjusted), (b) categories where competitive pricing pressure (W61 data) is limiting margin, (c) categories where vendor cost reduction should be negotiated (W44), (d) categories with structural low margin requiring assortment changes (W1, W68), (e) categories where quantity break pricing (W40.15–19) is eroding margin below acceptable levels | Cost Accountant / Pricing Analyst | Controller | 4 hours/quarter |
| 7 | Controller and VP Merchandising review quarterly margin deep-dive together with Category Managers; each Category Manager presents margin improvement plan for categories below target; agreed actions integrated into W1 assortment review and W40 pricing execution | Controller / VP Merchandising | CFO | 2 hours/quarter |
| 8 | Cost Accountant updates system margin thresholds per category if needed (based on strategic pricing decisions); updates category margin targets for next quarter's monitoring | Cost Accountant | Controller | 30 min/quarter |

### Annual Category-Level Strategy Review (aligned with W26 budget cycle)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 9 | Cost Accountant prepares annual margin strategy report: (a) 12-month margin trend by category with quarterly granularity, (b) year-over-year margin movement by category with driver analysis (cost, mix, promo, pricing), (c) vendor rebate impact on effective margin (W27), (d) category margin vs. industry benchmarks (where available), (e) proposed margin targets by category for next year, (f) margin improvement opportunities with estimated P&L impact | Cost Accountant | Controller | 16 hours/year |
| 10 | CFO reviews annual margin strategy with VP Merchandising and CEO; agreed category margin targets feed into W26 annual budget as gross profit targets; significant pricing strategy changes approved and scheduled for execution through W40 | CFO / VP Merchandising | CEO | 2 hours/year |

### System Touchpoints
- Automated monthly margin analysis report: category-level and SKU-level margin % with trend comparison (W85.1)
- Margin exception reporting: SKUs below threshold with root cause classification (W85.3)
- Quarterly category margin deep-dive: vendor-level analysis, import vs. domestic, promo vs. non-promo (W85.5)
- Configurable margin thresholds per category with alerting (W85.8)
- Annual margin strategy report with driver analysis and proposed targets (W85.9)
- Integration with W1 (assortment review — margin is a key input to SKU add/drop decisions), W9a (WAC verification and month-end inventory valuation), W13 (promo margin impact), W27 (vendor rebate impact on effective margin), W40 (SRP changes — margin impact calculator), W44 (vendor cost negotiation), W61 (competitive pricing pressure), W68 (product discontinuation — margin as exit criterion), W83 (campaign ROI — margin data feeds campaign performance analysis)

### Staffing Implication
- **Cost Accountant**: adds ~4 hours/month for monthly review + ~12 hours/quarter for deep-dive + ~16 hours/year for annual review = ~100 hours/year. Absorbed within existing Finance team.
- **Pricing Analysts**: add ~4 hours/quarter for joint pricing strategy recommendations. Absorbed.
- **No incremental headcount.**

---



## W89. Bank Reconciliation

| Field | Detail |
|---|---|
| **Trigger** | Bank statements received (monthly paper/electronic from BDO, BPI, Metrobank, Chinabank across 5 entities) |
| **Frequency** | Monthly per bank account per entity; ~25 bank accounts (5 entities × ~5 accounts each: PHP operating, PHP payroll, USD import, PHP savings/deposit, PHP petty cash replenishment) |
| **Volume** | ~3,000–4,000 bank statement lines/month across all accounts |
| **Owner** | Treasury Analyst |
| **Participants** | Treasury Analyst, Controller, AP Clerk, AR Clerk |

### Background

Bank reconciliation is a fundamental financial control ensuring that the general ledger cash balances match actual bank balances. With 5 legal entities, ~25 bank accounts across 4 banks (BDO, BPI, Metrobank, Chinabank), multi-currency (PHP and USD), and high transaction volume from store deposits, vendor payments, payroll crediting, and ecommerce settlement, a structured reconciliation workflow is essential. This workflow is distinct from W30 (daily treasury cash position management) which focuses on operational cash visibility; bank reconciliation is the periodic accounting control that validates GL accuracy.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Statement import**: Treasury Analyst imports electronic bank statements (BDO, BPI, Metrobank, Chinabank formats) into ERP bank reconciliation module; for accounts receiving paper statements only, AP Clerk scans and enters key transactions manually | Treasury Analyst / AP Clerk | Controller | 30 min/account |
| 2 | **Auto-matching — system level**: System attempts to auto-match bank statement lines to GL transactions: (a) vendor payment (W7) matched by payment reference and amount, (b) customer receipt (W8) matched by deposit reference, (c) payroll bank file (W10) matched by batch reference and total, (d) intercompany settlement (W14) matched by IC reference, (e) treasury sweeps and transfers (W30) matched by transfer reference, (f) tax payments (W90) matched by BIR payment reference, (g) capex payments (W21) matched by PO/invoice reference | System | — | Automated |
| 3 | **Review auto-matched items**: Treasury Analyst reviews auto-matched items for accuracy; system displays match confidence score (high: exact reference + amount match; medium: amount match only; low: fuzzy match); high-confidence matches auto-accepted; medium and low reviewed manually | Treasury Analyst | Controller | 15 min/account |
| 4 | **Manual matching — unmatched items**: Treasury Analyst investigates unmatched bank statement lines: (a) bank charges and fees (not in GL — post as bank charges expense), (b) deposit discrepancies (store cash deposit variance per W5f), (c) timing differences (checks issued but not yet cleared), (d) unknown items requiring investigation, (e) payment gateway settlement deposits (cross-reference W99), (f) interest income/expense (post as incurred) | Treasury Analyst | Controller | 30 min/account |
| 5 | **Outstanding items review**: (a) Outstanding checks > 90 days: investigate with AP — stale check per Philippine law (6 months); if stale, AP re-issues or reverses; (b) Outstanding deposits > 7 days: investigate with store operations — missing deposit; (c) Unrecorded bank fees: post to bank charges expense; (d) FX gains/losses on USD accounts: post FX revaluation per W9a.5a | Treasury Analyst | Controller | 15 min/account |
| 6 | **Reconciliation sign-off**: Treasury Analyst completes bank reconciliation per account; system generates reconciliation report showing: opening GL balance, plus/minus reconciling items, ending GL balance, ending bank balance, unreconciled difference (must be zero); Treasury Analyst signs off electronically | Treasury Analyst | Controller | 5 min/account |
| 7 | **Controller review**: Controller reviews completed bank reconciliations for all accounts; focuses on: (a) accounts with high unmatched volume, (b) unusual items, (c) stale checks, (d) deposit discrepancies > PHP 5,000; approves or returns for correction | Controller | CFO | 1 hour/month |
| 8 | **Journal entries**: System auto-generates journal entries for: (a) bank charges and fees, (b) interest income, (c) FX gains/losses on USD accounts, (d) stale check reversals, (e) deposit discrepancy adjustments; all auto-posted to GL with bank reconciliation reference | System | Controller | Automated |
| 9 | **Aging of reconciling items**: System tracks aging of all unreconciled items: items > 30 days flagged for Treasury Analyst follow-up; items > 60 days escalated to Controller; items > 90 days require write-off or resolution per Controller | System | Controller | Automated |

### Multi-Entity Considerations
- Each entity's bank accounts reconciled separately
- Intercompany bank transfers (W14 settlements) must clear in both entities' bank reconciliations in the same month
- USD accounts (for import payments) reconciled with FX revaluation per W9a.5a
- Ecommerce payment gateway accounts (PayMongo, Dragonpay) reconciled via W99 and cross-referenced here

### System Touchpoints
- Electronic bank statement import (BDO, BPI, Metrobank, Chinabank file formats) (W89.1)
- Auto-matching engine: payment reference, deposit reference, batch reference matching with confidence scoring (W89.2)
- Bank reconciliation module with GL-to-bank matching screen (W89.3–4)
- Outstanding items aging tracker with escalation triggers (W89.5, W89.9)
- Auto-journal entry generation for bank charges, interest, FX, stale checks (W89.8)
- Multi-entity, multi-currency bank reconciliation with consolidated dashboard (W89 multi-entity)
- Integration with W7 (AP payments), W8 (AR receipts), W10 (payroll bank files), W14 (IC settlements), W21 (capex payments), W25 (petty cash replenishment), W30 (treasury sweeps), W90 (tax payments), W99 (payment gateway settlements)

### Staffing Implication
- **Treasury Analysts**: ~25 accounts × ~90 min each = ~37.5 hours/month. With 2 Treasury Analysts, that's ~19 hours each/month. Absorbed within existing Finance team (month-end close week is the heaviest period).
- **Controller**: 1 hour/month for review. Absorbed.
- **No incremental headcount.**

---



## W90. Monthly Tax Filing & Statutory Remittance

| Field | Detail |
|---|---|
| **Trigger** | Monthly tax filing deadlines per BIR calendar; payroll statutory deduction deadlines per SSS/PhilHealth/Pag-IBIG schedules |
| **Frequency** | Monthly (VAT, EWT, SSS, PhilHealth, Pag-IBIG); quarterly (corporate income tax); annual (1702RT, 1604-C/E) |
| **Volume** | 5 entities × multiple tax types = ~25 monthly filings; plus payroll statutory for 5 entities |
| **Owner** | Tax Accountant |
| **Participants** | Tax Accountant, Controller, Treasury Analyst, Payroll Officer, HR Manager |

### Background

FIN-008 requires BIR tax return generation as a Must Have. W9 (Financial Close) produces the tax data and generates the returns, but the operational process of reviewing, validating, filing, and remitting taxes is a distinct workflow. Philippine tax compliance involves strict monthly deadlines (VAT 2550M by 20th/25th, EWT 1601-E by 10th, withholding on compensation 1601-C by 10th), quarterly filings (1702Q income tax), and annual returns (1702RT). Late filing incurs penalties (25% surcharge + 12% annual interest + compromise penalty). This workflow bridges the financial close (W9) to actual regulatory compliance.

### Monthly Tax Filing Cycle

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Tax data extraction** (after W9a month-end close day 3–4): Tax Accountant extracts from ERP: (a) VAT data — output VAT (sales) and input VAT (purchases) per entity; sales/purchases split by VAT-able, VAT-exempt, zero-rated; (b) EWT data — withholding tax per vendor per ATC (Alphanumeric Tax Code) from AP (W7.9a); (c) Withholding on compensation — per employee per entity from payroll (W10.4); (d) Local business tax — per LGU per location from W9a.16c | Tax Accountant | Controller | 2 hours/month |
| 2 | **VAT return preparation** (BIR Form 2550M — monthly, or 2550Q — quarterly): (a) Tax Accountant reviews VAT data for completeness: all sales transactions captured, all purchase VAT claimed, intercompany VAT elimination correct per W14; (b) prepares 2550M per entity: gross sales, VAT-able sales, output VAT, total purchases, VAT-able purchases, input VAT, adjustments (prior period corrections), net VAT payable or refundable; (c) validates input VAT claims against supporting documents — BIR-registered sales invoices, official receipts, import entry declarations; (d) cross-references with W9a.16 VAT return schedule | Tax Accountant | Controller | 3 hours/month |
| 3 | **EWT return preparation** (BIR Form 1601-E): (a) Tax Accountant reviews EWT computations per vendor per ATC; validates against AP records (W7.9a); (b) reconciles total EWT withheld per entity vs. vendor creditable withholding tax certificates (BIR Form 2307) to be issued; (c) prepares 1601-E per entity: total withholding per ATC category, taxes remitted prior months, current month liability | Tax Accountant | Controller | 2 hours/month |
| 4 | **Withholding on compensation** (BIR Form 1601-C): (a) Payroll Officer provides monthly withholding tax per entity from W10 payroll processing; (b) Tax Accountant validates against TRAIN law tax tables and payroll register; (c) prepares 1601-C per entity | Tax Accountant / Payroll Officer | Controller | 1 hour/month |
| 5 | **Statutory remittance — SSS, PhilHealth, Pag-IBIG**: (a) Payroll Officer generates monthly contribution schedules per entity from W10: employer share, employee share, total per employee; (b) validates against PRN (Payment Reference Number) from each agency; (c) submits payment via bank transfer or agency portal per deadline (SSS by last day of month, PhilHealth by every 10th, Pag-IBIG by every 14th) | Payroll Officer | HR Manager | 2 hours/month |
| 6 | **BIR eFPS filing**: Tax Accountant files returns via BIR Electronic Filing and Payment System (eFPS) or eBIRForms for non-eFPS-covered entities: (a) uploads prepared returns (2550M, 1601-E, 1601-C); (b) system validates return data against BIR validation rules; (c) receives confirmation and payment reference | Tax Accountant | Controller | 1 hour/month |
| 7 | **Tax payment**: Treasury Analyst processes tax payments via bank: (a) eFPS auto-debit for covered entities; (b) manual bank transfer for non-eFPS entities; (c) verifies payment confirmation against filed return amounts | Treasury Analyst | Controller | 30 min/month |
| 8 | **Tax certificate generation**: Tax Accountant generates and distributes: (a) BIR Form 2307 (creditable withholding tax certificates) to vendors — monthly for top vendors, quarterly for others; (b) BIR Form 2316 (certificate of compensation payment/tax withheld) to all employees — annually or upon separation (W43); (c) alphalist of payees (1604-E) and employees (1604-C) — annual | Tax Accountant | Controller | 2 hours/month |
| 9 | **Tax reconciliation**: Monthly: Tax Accountant reconciles tax liability accounts (VAT payable, EWT payable, WTC payable) per entity: (a) beginning balance + current month liability − payments = ending balance; (b) ending balance must agree with GL (W9a); (c) investigates and resolves discrepancies before next filing cycle | Tax Accountant | Controller | 1 hour/month |
| 10 | **Tax calendar compliance dashboard**: System maintains tax compliance calendar per entity showing: filing deadline, filing status (pending/filed/paid), responsible person, penalty exposure for late filing; Controller reviews weekly | System / Controller | CFO | 15 min/week |

### Quarterly / Annual Filing Additions

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 11 | **Quarterly income tax return** (BIR Form 1702Q): Tax Accountant prepares quarterly corporate income tax return per entity: taxable income, tax due, quarterly installment; validates against quarterly financial statements (W9a) | Tax Accountant | Controller | Quarterly |
| 12 | **Annual income tax return** (BIR Form 1702RT): Tax Accountant prepares annual corporate income tax return per entity; incorporates year-end adjustments from W9b; cross-references with external auditor's tax computations (W95) | Tax Accountant | Controller / CFO | Annual |
| 13 | **Annual information returns** (BIR Forms 1604-C, 1604-E): Tax Accountant prepares and files annual alphalist of employees and payees; reconciles with full-year withholding records | Tax Accountant | Controller | Annual (January) |
| 14 | **Local business tax reconciliation**: Tax Accountant reconciles quarterly LBT payments per LGU (from W9a.16c) against LGU assessment; prepares any variance explanations; LGU assessments reconciled during W54 permit renewals | Tax Accountant | Controller | Quarterly |

### System Touchpoints
- Automated tax data extraction: VAT, EWT, WTC per entity with intercompany elimination (W90.1)
- BIR return generation: 2550M/Q, 1601-E, 1601-C, 1702Q/RT, 1604-C/E in BIR-prescribed format (W90.2–4)
- BIR eFPS/eBIRForms integration or export: prepared returns uploadable to BIR systems (W90.6)
- Tax calendar compliance dashboard with deadline tracking and penalty exposure (W90.10)
- Vendor withholding tax certificate (2307) generation and distribution (W90.8)
- Employee withholding tax certificate (2316) generation (W90.8, W43.10)
- Tax liability account reconciliation: VAT payable, EWT payable, WTC payable per entity (W90.9)
- Statutory contribution schedules: SSS, PhilHealth, Pag-IBIG with employer/employee split per entity (W90.5)
- Integration with W7 (AP — EWT computation), W8 (AR — VAT on sales), W9 (financial close — tax data source), W10 (payroll — withholding on compensation, statutory contributions), W14 (IC — VAT elimination), W30 (treasury — tax payment processing), W54 (LGU — local business tax), W77 (BIR audit — returns serve as audit support), W95 (external audit — tax provision validation)

### Staffing Implication
- **Tax Accountant**: adds ~12–15 hours/month for monthly filings + ~8 hours/quarter for quarterly returns + ~20 hours for annual returns = ~210 hours/year. This is a full-time responsibility; if a dedicated Tax Accountant does not exist, the Controller or Senior Accountant absorbs this work at the cost of ~25% of their capacity. **Recommend: 1 dedicated Tax Accountant** given 5 entities and Philippine tax complexity.
- **Payroll Officer**: statutory remittance adds ~2 hours/month. Absorbed.
- **Treasury Analyst**: tax payment processing adds ~30 min/month. Absorbed.

---



## W94. Customer Deposit & Advance Payment Management

| Field | Detail |
|---|---|
| **Trigger** | Customer places special order (W38); corporate/project account requires advance payment for large order; layaway deposit (W75); or customer requests credit balance refund |
| **Frequency** | ~800–1,200 customer deposits/month (special orders, project accounts, layaway) |
| **Volume** | Avg PHP 5,000–50,000 per deposit; project deposits can reach PHP 500,000+ |
| **Owner** | AR Accountant |
| **Participants** | AR Accountant, CSR / Sales Associate, Store Manager, Treasury Analyst, Customer |

### Background

Customer deposits (advance payments) are a common retail scenario for big-box home improvement: special orders for non-stock items, large project orders requiring down payments, layaway deposits, and corporate accounts with credit balances. Without a structured workflow, deposits can be mishandled — unapplied to invoices, forgotten refunds, or misallocated across entities. This workflow manages the full deposit lifecycle from receipt to application, refund, or forfeiture. It supports FIN-005 (AR for B2B) and POS-020 (layaway/installment sales).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Deposit collection**: (a) **At POS** (store): Sales Associate or CSR collects deposit from customer for special order (W38), layaway (W75), or large in-store project order; system creates deposit receipt with deposit reference, customer account (loyalty, trade, or corporate), amount, and linked sales order or special order reference; payment captured via standard POS tender (cash, card, e-wallet); system posts to GL: Dr. Cash / Cr. Customer Deposits (liability); (b) **Online** (ecommerce): Customer prepays for BOPIS (W11) or home delivery (W19); system treats as advance payment captured by Digital Commerce Inc. and remitted to Depot Inc. per W14 IC model; (c) **Bank transfer** (corporate/project accounts): Corporate customer wires advance payment for large project order (W58); AR Accountant receives bank credit advice; posts deposit to customer account with project order reference | Sales Associate / CSR / AR Accountant | Store Manager / Controller | 5 min/POS deposit; 15 min/bank transfer |
| 2 | **Deposit tracking**: System maintains deposit register per customer showing: deposit reference, date, amount, linked order, status (open/partially applied/fully applied/forfeited/refunded), aging; deposits are customer-level liability (not order-level revenue) until applied to invoice at fulfillment | System | — | Automated |
| 3 | **Deposit application — at fulfillment**: (a) When linked sales order is fulfilled and invoice is generated (POS sale, special order delivery, project billing per W58), system auto-applies deposit to invoice: system reduces customer deposit liability (Dr. Customer Deposits) and reduces AR (Cr. Accounts Receivable) or cash balance; (b) if deposit exceeds invoice amount: system applies deposit to invoice and maintains residual credit balance on customer account for next invoice or refund; (c) if deposit is less than invoice amount: system applies full deposit and customer pays remaining balance at POS or via standard AR terms | System / AR Accountant | Controller | Automated + 5 min/review |
| 4 | **Deposit refund**: (a) Customer requests cancellation of special order before fulfillment: CSR processes deposit refund per cancellation policy (full refund, less cancellation fee per W38, or forfeiture per W75 layaway rules); (b) system creates refund transaction: Dr. Customer Deposits / Cr. Cash (for POS refunds) or Cr. AP (for bank transfer refunds); (c) refund processed within 3–5 business days per customer-facing SLA; (d) for card/e-wallet deposits: refund to original payment method; for cash deposits: cash refund at store; for bank transfer deposits: bank transfer back to customer | CSR / AR Accountant | Store Manager | 10 min/refund |
| 5 | **Unclaimed deposit aging**: System monitors unapplied/unrefunded deposits with aging: (a) 0–90 days: normal; (b) 90–180 days: system sends customer notification (deposit reminder); (c) 180–365 days: CSR contacts customer for disposition (apply, refund, or forfeit); (d) > 365 days: per Philippine law and BuildRight policy, unclaimed deposits may be recognized as revenue with Controller approval; system generates unclaimed deposit report for Controller review | System / CSR | Controller | 15 min/week |
| 6 | **Layaway deposit forfeiture** (W75 integration): (a) If customer cancels layaway or defaults on installment payments per W75 cancellation rules, system forfeits deposit per layaway agreement terms; (b) forfeiture amount posted as Dr. Customer Deposits / Cr. Other Income (cancellation fee) or Cr. Revenue (if goods retained); (c) inventory reservation released per W75 | System / CSR | Store Manager | Per W75 |
| 7 | **Project account advance billing** (W58 integration): For corporate/project accounts with milestone billing: (a) project contract may specify advance payment (e.g., 30% down, 40% at delivery, 30% at completion); (b) each advance collected per step 1; (c) at each billing milestone (W58), system applies collected deposits to milestone invoice; (d) retention amounts (typically 10% held for 90–180 days post-completion) tracked separately in deposit register with scheduled release date | AR Accountant | Controller | Per W58 |
| 8 | **Monthly reconciliation**: AR Accountant reconciles customer deposit liability account: (a) total deposit liability per GL must agree with deposit register total per system; (b) aging analysis of unapplied deposits; (c) investigate and resolve discrepancies; (d) report to Controller as part of W9a month-end close | AR Accountant | Controller | 2 hours/month |

### System Touchpoints
- Deposit receipt creation at POS or AR with linked order reference (W94.1)
- Customer deposit register: per-customer, per-order deposit tracking with status and aging (W94.2)
- Auto-application of deposit to invoice at fulfillment (W94.3)
- Deposit refund processing with cancellation policy enforcement (W94.4)
- Unclaimed deposit aging report with escalation triggers (W94.5)
- Integration with W11 (BOPIS — prepayment), W12 (returns — refund from deposit), W19 (home delivery — prepayment), W38 (special orders — deposit collection and cancellation fee), W58 (project accounts — milestone advance billing), W75 (layaway — deposit and installment payments, forfeiture), W89 (bank reconciliation — deposit refunds in bank statement)

### Staffing Implication
- **AR Accountant**: adds ~2–3 hours/week for deposit management and reconciliation. Absorbed within existing Finance team.
- **CSRs**: deposit collection and refund adds ~5 min per transaction; with ~800–1,200 deposits/month across 200 stores = ~4–6 per store/month. Absorbed.
- **No incremental headcount.**

---



## W99. Payment Settlement Reconciliation (Card / E-Wallet / Online)

| Field | Detail |
|---|---|
| **Trigger** | Daily settlement reports received from payment processors (card acquirers, e-wallet providers, payment gateways) |
| **Frequency** | Daily reconciliation; weekly summary review; monthly comprehensive reconciliation |
| **Volume** | ~1,400,000 non-cash transactions/month (card 36% + e-wallet 15% = 51% of 2.8M POS transactions) + ~42,900 ecommerce payment transactions/month |
| **Owner** | Treasury Analyst |
| **Participants** | Treasury Analyst, AR Accountant, Controller, POS Administrator, Store Manager (for deposit variances) |

### Background

With 51% of POS transactions paid via non-cash methods (credit/debit cards ~36%, e-wallets like GCash and Maya ~15%) and all ecommerce orders paid online, payment settlement reconciliation is a critical daily operational process. Payment processors (card acquirers, GCash, Maya, PayMongo, Dragonpay) settle to BuildRight's bank accounts on varying schedules (T+1 for cards, T+1 to T+3 for e-wallets, T+2 to T+5 for payment gateways), each with different fee structures, chargeback processes, and settlement reporting formats. Without a structured reconciliation workflow, settlement discrepancies go undetected, fees are not properly recorded, and cash is misstated.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Settlement report import**: System imports daily settlement reports from each payment channel: (a) card acquirer settlement (BDO, BPI merchant acquiring — per-terminal breakdown of gross sales, refunds, chargebacks, interchange fees, acquiring fees, net settlement); (b) e-wallet settlement (GCash, Maya — per-transaction or batch settlement with per-transaction fees); (c) ecommerce payment gateway (PayMongo, Dragonpay — per-order settlement with gateway fees, payment method fees) | System | Treasury Analyst | Automated |
| 2 | **Auto-matching**: System attempts to match settlement report lines to POS/ecommerce transactions: (a) match by transaction reference (card approval code, e-wallet reference, payment gateway order ID); (b) match by amount and date; (c) system calculates variance per settlement batch: gross transactions − refunds − chargebacks − fees = expected net settlement; compare to actual bank credit | System | — | Automated |
| 3 | **Fee validation**: (a) System validates processing fees per transaction against contracted rates per payment processor: card acquiring fees (1.5–2.5% + PHP 10–15 per transaction), e-wallet fees (1.0–2.0% + PHP 5–10), payment gateway fees (2.0–3.5% + PHP 15–25); (b) flags transactions with fees exceeding contracted rate by > 0.5% for investigation; (c) monthly: Treasury Analyst compares actual effective fee rate (total fees ÷ total processed) vs. contracted blended rate per processor | System / Treasury Analyst | Controller | 15 min/day |
| 4 | **Chargeback management**: (a) System receives chargeback notification from card acquirer; (b) creates chargeback case with transaction details; (c) Store Manager or CSR provides supporting documentation (signed receipt, delivery proof, CCTV if fraud); (d) Treasury Analyst submits representment (dispute) within acquirer deadline (typically 7–14 days); (e) if chargeback upheld: system posts Dr. Chargeback Expense / Cr. AR-Card Processor; if reversed: system posts Dr. AR-Card Processor / Cr. Chargeback Expense; (f) monthly chargeback rate monitored: target < 0.5% of card transaction volume | Treasury Analyst / CSR / Store Manager | Controller | 20 min/chargeback |
| 5 | **Unreconciled items investigation**: Treasury Analyst investigates unmatched items: (a) settlement received but no matching POS transaction (possible: delayed posting from offline POS per W5g, multi-tender split transaction), (b) POS transaction but no matching settlement (possible: transaction on cutoff date, settlement in next day's batch), (c) amount discrepancy (partial refund, fee dispute, FX conversion for international cards) | Treasury Analyst | Controller | 30 min/day |
| 6 | **GL posting**: System posts daily settlement entries: (a) Dr. Cash (net settlement received in bank) / Cr. AR-Card Processor (gross transactions); (b) Dr. Payment Processing Expense / Cr. AR-Card Processor (processing fees); (c) Dr. AR-Card Processor / Cr. Revenue (refunds/chargebacks); (d) net effect: system AR-Card Processor clearing account should net to zero daily; any residual balance investigated | System | Treasury Analyst | Automated |
| 7 | **Weekly summary**: Treasury Analyst prepares weekly payment settlement summary: total processed per channel, total fees, effective fee rate per channel, chargeback count and rate, unreconciled items aging; submits to Controller | Treasury Analyst | Controller | 30 min/week |
| 8 | **Monthly comprehensive reconciliation**: (a) Treasury Analyst reconciles monthly totals per payment channel: gross transactions (from POS/ecommerce system) vs. processed volume (from processor statements) vs. net settlement (from bank statements per W89); (b) validates monthly fee accrual vs. actual fees charged; adjusts accrual if variance > 2%; (c) confirms all chargeback cases resolved; (d) part of W9a month-end close supporting schedules | Treasury Analyst | Controller | 2 hours/month |

### Per-Channel Settlement Timing

| Channel | Settlement Schedule | Fee Structure |
|---|---|---|
| Credit/Debit Card (BDO acquiring) | T+1 business day | 1.5–2.5% + PHP 10–15/txn |
| Credit/Debit Card (BPI acquiring) | T+1 business day | 1.5–2.5% + PHP 10–15/txn |
| GCash | T+1 business day | 1.0–2.0% + PHP 5–10/txn |
| Maya | T+1 to T+2 business day | 1.0–2.0% + PHP 5–10/txn |
| PayMongo (ecommerce) | T+2 to T+3 business day | 2.0–3.5% + PHP 15–25/txn |
| Dragonpay (bank transfer) | T+1 to T+5 business day | PHP 15–30/txn (fixed) |

### System Touchpoints
- Settlement report import from multiple processors in their respective formats (W99.1)
- Auto-matching engine: transaction reference, amount, date matching across POS, ecommerce, and settlement data (W99.2)
- Fee validation against contracted rates with variance alerting (W99.3)
- Chargeback case management with document collection and deadline tracking (W99.4)
- AR-Card Processor clearing account with daily zero-balance target (W99.6)
- Weekly payment settlement summary and monthly comprehensive reconciliation (W99.7–8)
- Integration with W5b (POS transactions — source of card/e-wallet payments), W5g (offline POS — delayed settlement), W11 (BOPIS payments), W12 (returns — refund processing), W19 (ecommerce payments), W25 (petty cash — small cash refunds), W30 (treasury — cash position includes settlement deposits), W89 (bank reconciliation — settlement deposits in bank statements)

### Staffing Implication
- **Treasury Analysts**: add ~1 hour/day for daily reconciliation + 30 min/week summary + 2 hours/month comprehensive = ~25 hours/month. With 2 Treasury Analysts, this is ~12.5 hours each/month. Absorbed within existing Finance team.
- **CSRs / Store Managers**: chargeback documentation adds ~5–10 min per chargeback case. With ~50–100 chargebacks/month across 200 stores, this is minimal per store.
- **No incremental headcount.**

---



## W100. Vendor Statement Reconciliation

| Field | Detail |
|---|---|
| **Trigger** | Monthly reconciliation calendar (10th business day of following month) |
| **Frequency** | Monthly for top 100 vendors (by spend); quarterly for remaining active vendors |
| **Volume** | Top 100 vendors = ~80% of AP spend; remaining ~700–900 vendors reconciled quarterly |
| **Owner** | AP Supervisor |
| **Participants** | AP Clerk, AP Supervisor, Buyer (discrepancy resolution), Controller (escalation) |

### Background

Referenced as "W7d" in W3 (RTV credit note aging report feeding into vendor statement reconciliation), this workflow fills a critical AP control gap. Without systematic vendor statement reconciliation, the company risks overpayment (duplicate invoices not caught by auto-matching), underpayment (vendor disputes damaging relationships), and inaccurate liability reporting (AP sub-ledger diverges from actual amounts owed). This is a standard month-end close control for any company with 800–1,000 active vendors and ~8,500–9,500 monthly invoices.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | AP Clerk requests or receives vendor statement of account (SOA) — via email, vendor portal, or mail; top vendors provide monthly SOA automatically; for remaining vendors, AP Clerk sends batch request at month-end | AP Clerk | AP Supervisor | 30 min/batch (top 100) |
| 2 | System prepares BuildRight's AP sub-ledger summary per vendor for the reconciliation period: total invoices received, payments made, credit memos applied, debit memos issued, and resulting AP balance | System | — | Automated |
| 3 | AP Clerk compares vendor SOA to BuildRight's AP sub-ledger per vendor: (a) match invoices — vendor SOA invoices vs. BuildRight recorded invoices, (b) match payments — vendor SOA payments received vs. BuildRight payments issued, (c) match credit/debit memos — vendor SOA adjustments vs. BuildRight credit memos (W7.9b) and debit notes (W70), (d) compare ending balances | AP Clerk | AP Supervisor | 15 min/vendor |
| 4 | **If balances match**: AP Clerk marks vendor as reconciled for the period; no further action | AP Clerk | AP Supervisor | 2 min/vendor |
| 5 | **If balances do not match**: AP Clerk documents reconciling items by type: (a) **Timing differences** — payments in transit (BuildRight issued but vendor not yet received), invoices received after SOA cutoff, GRs posted but vendor invoices not yet received (GRNI per W7), (b) **Missing invoices** — vendor shows invoice not in BuildRight's system (possible loss, email misrouted, or vendor error), (c) **Missing payments** — BuildRight shows payment not on vendor SOA (check not cleared, bank transfer not yet credited to vendor), (d) **Unrecorded credit memos** — vendor issued credit not yet in BuildRight's system (RTV credit note pending per W3, rebate settlement pending per W27), (e) **Disputed items** — vendor shows charge that BuildRight disputes (quality rejection, pricing discrepancy, unauthorized charge) | AP Clerk | AP Supervisor | 15–30 min/vendor with variances |
| 6 | AP Clerk resolves reconciling items: (a) timing differences — document and carry forward to next period, (b) missing invoices — request from vendor; if legitimate, process per W7, (c) missing payments — provide payment proof (bank reference, check copy) to vendor, (d) unrecorded credits — verify against RTV log (W88), rebate settlement log (W27), price protection log (W40); if valid, request vendor credit memo or record in system, (e) disputed items — route to Buyer for resolution with vendor per W44 dispute process | AP Clerk / Buyer | AP Supervisor | 15–60 min/item |
| 7 | AP Clerk prepares reconciliation summary per vendor: BuildRight balance, vendor SOA balance, reconciling items (with aging), net agreed balance; system stores reconciliation record with full documentation | AP Clerk | AP Supervisor | 5 min/vendor |
| 8 | AP Supervisor reviews reconciliation summary for top 20 vendors (by spend or by reconciliation complexity); approves or requests additional investigation | AP Supervisor | Controller | 1 hour/month |
| 9 | Unresolved items > 60 days auto-escalate to Controller for review; Controller decides: write-off, pursue with vendor, or adjust AP balance | Controller | CFO | 30 min/month |
| 10 | Quarterly: AP Supervisor generates vendor reconciliation KPI report: (a) reconciliation completion rate (% of top 100 vendors reconciled within SLA), (b) average reconciling items per vendor, (c) aging of unresolved items, (d) top vendors by reconciliation complexity (chronic discrepancies signal vendor billing quality issues — feed into W44 vendor scorecard), (e) duplicate payment recovery amount (if any duplicates caught during reconciliation) | AP Supervisor | Controller | 1 hour/quarter |

**Reconciliation SLA**: Top 100 vendors reconciled within 15 business days of month-end; remaining vendors reconciled within 30 business days of quarter-end.

### System Touchpoints
- Vendor AP sub-ledger summary generation per vendor per period (W100.2)
- Reconciliation workspace: side-by-side comparison of vendor SOA vs. BuildRight AP records with line-level matching (W100.3)
- Reconciling item classification and documentation: timing, missing invoice, missing payment, unrecorded credit, disputed (W100.5)
- Integration with W7 (invoice and payment records), W27 (rebate credits), W70 (debit note aging), W88 (RTV credit notes), W44 (vendor scorecard — reconciliation complexity as quality metric)
- Aging tracker for unresolved reconciling items with auto-escalation at 60 days (W100.9)
- Reconciliation KPI dashboard (W100.10)
- Audit trail: all reconciliation actions logged with AP Clerk ID, timestamp, and documentation

### Staffing Implication
- **AP Clerks**: Top 100 vendors × 15 min average = ~25 hours/month for monthly reconciliation. Remaining ~800 vendors quarterly × 15 min ÷ 3 months = ~67 hours/quarter = ~22 hours/month. Total ~47 hours/month. With 8–10 AP Clerks, this is ~5–6 hours each/month. Absorbed within existing team, with some overtime during peak month-end close periods.
- **AP Supervisor**: 1 hour/month for top-20 review + 1 hour/quarter for KPI report. Absorbed.
- **Controller**: 30 min/month for escalations. Absorbed.

---



## W101. Customer Refund & Credit Processing

| Field | Detail |
|---|---|
| **Trigger** | Customer return approved (W12), ecommerce cancellation (W98), special order deposit refund (W38), customer deposit refund (W94), loyalty points reversal (W17), or credit note issuance from complaint resolution (W41) |
| **Frequency** | ~5,000–7,000 refund/credit transactions/month across all channels |
| **Volume** | ~2,800 in-store return refunds + ~2,250 ecommerce refunds + ~50–100 deposit refunds + ~50–200 credit notes/month |
| **Owner** | CSR (in-store refunds); Ecommerce Customer Support (online refunds); AR Supervisor (trade/corporate credit notes) |
| **Participants** | CSR, Cashier, Store Manager, AR Supervisor, AR Clerk, Ecommerce Customer Support, Treasury Analyst, Controller |

### Background

Refund and credit processing is currently scattered across multiple workflows: W12 (returns), W38 (special order deposits), W94 (customer deposits), W98 (ecommerce cancellations), and W41 (complaint credits). Each handles its specific trigger but there is no unified workflow governing authorization tiers, payment method routing, GL posting consistency, BIR compliance, reconciliation, and fraud prevention across all refund/credit channels. This workflow provides the common processing framework that all trigger workflows reference.

### Refund Authorization Matrix

| Refund Amount | In-Store (CSR/Cashier) | Online (Ecom Support) | Trade/Corporate (AR) |
|---|---|---|---|
| ≤ PHP 1,000 | CSR approves | Auto-approved | AR Clerk |
| PHP 1,001–5,000 | Store Manager | CS Manager | AR Clerk |
| PHP 5,001–50,000 | Store Manager + photo evidence | CS Manager + VP approval | AR Supervisor |
| > PHP 50,000 | Regional Manager + Controller | CMO + Controller | Controller + CFO |

### Refund by Payment Method

| Original Payment | Refund Method | Processing | GL Posting |
|---|---|---|---|
| Cash (in-store) | Cash from drawer or store petty cash (W25) if drawer insufficient | Immediate at POS | Dr. Revenue / Cr. Cash |
| Credit/Debit Card | Electronic refund to original card via POS terminal or card processor portal | T+1–3 business days settlement | Dr. Revenue / Cr. AR-Card Processor |
| E-Wallet (GCash, Maya) | Electronic refund to original e-wallet via payment gateway | T+1–2 business days settlement | Dr. Revenue / Cr. AR-E-Wallet |
| Loyalty Points | Points reversal (deduct from balance) | Immediate in system | Dr. Revenue / Cr. Deferred Revenue-Loyalty |
| Gift Card | Reload to original gift card | Immediate in system | Dr. Revenue / Cr. Deferred Revenue-Gift Cards |
| Trade Account (charge) | AR credit memo — reduces outstanding balance | Immediate in system | Dr. Revenue / Cr. AR-Trade |
| Ecommerce (online payment) | Refund to original payment method via PayMongo/Dragonpay | T+2–5 business days settlement | Dr. Revenue / Cr. AR-Ecommerce |
| Split Tender | Pro-rata refund to each method per W12a.6 | Combination of above | Split per method |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Trigger workflow** creates refund request: (a) W12 (return) — CSR processes return in POS; system creates refund request, (b) W98 (ecommerce cancellation) — system auto-creates refund for unfulfilled orders, (c) W38 (deposit refund) — CSR processes deposit refund with reason code, (d) W94 (advance payment refund) — CSR or AR Clerk processes with reason code, (e) W41 (complaint credit) — CS Manager authorizes refund or credit as complaint resolution, (f) W17 (loyalty reversal) — system auto-reverses points on return | Per trigger workflow | Per authorization matrix | Per trigger workflow |
| 2 | System validates refund request: (a) original transaction exists and is within refund policy window, (b) refund amount does not exceed original transaction amount, (c) no prior refund already processed against same transaction (duplicate refund prevention), (d) authorization per matrix above is met — system enforces approval routing by amount and channel | System | — | Automated |
| 3 | System determines refund payment method(s) from original transaction: for split-tender transactions, system identifies each payment method and calculates pro-rata refund amount per method | System | — | Automated |
| 4 | **Cash refund**: Cashier disburses from cash drawer; system reduces cash drawer accountability; if cash in drawer insufficient, Cashier uses petty cash float (W25) with Store Manager override; system logs cash refund with cashier ID and drawer balance impact | Cashier | Store Manager | 2 min |
| 5 | **Card/e-wallet refund**: System initiates electronic refund via payment processor integration; if terminal-based refund: Cashier processes refund on POS terminal; if gateway-based refund (ecommerce): system processes via PayMongo/Dragonpay API; system tracks refund settlement status (initiated → settled → confirmed) | System / Cashier | — | 2 min (terminal) / automated (gateway) |
| 6 | **Trade account credit**: AR Clerk posts credit memo to customer's AR account; system reduces outstanding balance; credit memo reference linked to original invoice and trigger workflow | AR Clerk | AR Supervisor | 5 min |
| 7 | **Gift card / loyalty reversal**: System reloads gift card balance or deducts loyalty points; reversal posted with reference to original earning transaction | System | — | Automated |
| 8 | System posts GL entries: (a) Dr. Revenue (or Dr. Sales Returns) / Cr. Cash (or AR-Card/E-Wallet/Ecommerce) — revenue reversal at original amount, (b) Dr. Inventory / Cr. COGS — if physical goods returned to stock (for non-damaged returns), (c) Dr. VAT Output / Cr. VAT Payable — output VAT reversal on refund (BIR requirement: refund must reverse the VAT portion), (d) system generates BIR-compliant credit memo or refund receipt with all required fields (TIN, original invoice reference, credit memo number, reason code, VAT reversal) | System | — | Automated |
| 9 | Weekly: AR Supervisor and Treasury Analyst review unsettled electronic refund report — refunds initiated but not yet settled by card processors or payment gateways; aged items > 7 business days investigated with processor | AR Supervisor / Treasury Analyst | Controller | 30 min/week |
| 10 | Monthly: Controller reviews refund analytics: (a) total refund volume by channel (in-store, ecommerce, trade), (b) refund rate as % of revenue by channel (target: in-store < 3%, ecommerce < 8%), (c) top refund reasons, (d) refund processing time (initiation to settlement), (e) authorization compliance — spot-check 20 random refunds per tier for proper approval, (f) refund fraud indicators — high-refund stores, high-refund employees, repeat refund customers | Controller | CFO | 1 hour/month |

### System Touchpoints
- Unified refund request record with link to original transaction and trigger workflow (W101.1)
- Automated validation: original transaction lookup, amount check, duplicate refund prevention, authorization tier enforcement (W101.2)
- Payment method routing from original transaction with pro-rata split calculation (W101.3)
- Cash refund with drawer balance tracking and petty cash fallback (W101.4)
- Electronic refund initiation via POS terminal and payment gateway integration (W101.5)
- Trade account credit memo posting (W101.6)
- Gift card reload and loyalty points reversal (W101.7)
- GL posting with VAT reversal and BIR-compliant credit memo / refund receipt generation (W101.8)
- Unsettled electronic refund tracking with aging and processor follow-up (W101.9)
- Monthly refund analytics dashboard with fraud indicators (W101.10)
- Integration with W12 (in-store returns), W17 (loyalty reversal), W28 (gift card reload), W38 (deposit refund), W41 (complaint credit), W94 (advance payment refund), W98 (ecommerce cancellation), W99 (payment settlement reconciliation), W5b (POS refund processing)

### Staffing Implication
- **CSRs / Cashiers**: refund processing is part of existing return and cancellation workflows — no incremental effort
- **AR Supervisor**: adds ~30 min/week for unsettled refund review. Absorbed.
- **Controller**: adds 1 hour/month for refund analytics review. Absorbed.
- **No incremental headcount.**

---

## W108. Customer Credit Collection & Escalation

| Field | Detail |
|---|---|
| **Trigger** | Trade or corporate account customer exceeds invoice payment terms (Net 30 or Net 60–90); or monthly scheduled collection review cycle |
| **Frequency** | Daily collection activities; weekly escalation review; monthly portfolio review |
| **Volume** | ~5,200 active AR accounts (5,000 trade + 200 corporate); ~3,500 AR invoices/month; ~30–40% of accounts typically carrying an overdue balance at any time |
| **Owner** | AR Collector (daily); AR Supervisor (escalation); Finance Manager (legal escalation) |
| **Participants** | AR Collector, AR Supervisor, Finance Manager, Sales Rep, Sales Manager, Controller, Legal, Collection Agency |

### Background

W8 covers AR processing — invoice generation, credit limit enforcement, and credit memo handling. W81 covers bad debt provisioning, write-off, and recovery. However, the active collection workflow between an invoice becoming overdue and reaching bad debt write-off is not detailed. At ~5,200 B2B accounts carrying ~30% of company revenue (~PHP 18.7B/year), effective collections directly impact cash flow and working capital. Philippine collections practice involves specific legal requirements (demand letters, BIR documentation) and cultural considerations (relationship-based collection approach). This workflow bridges W8 (AR processing) and W81 (bad debt write-off).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Daily overdue identification**: System generates daily AR aging report with overdue accounts grouped by aging bucket: Current, 1–30 days overdue, 31–60 days, 61–90 days, 91–180 days, 181+ days; each account shows: customer name, account number, total overdue amount, oldest invoice date, assigned Sales Rep, last payment date, and last contact date | System | — | Automated |
| 2 | **1–30 days overdue (soft collection)**: (a) System sends automated payment reminder via email/SMS on day 1 past due and day 15 past due with outstanding invoice details and payment instructions; (b) AR Collector reviews accounts > 15 days overdue; calls customer contact to confirm receipt of invoice and understand payment timeline; (c) AR Collector logs contact attempt, customer response, and committed payment date in system; (d) if customer disputes invoice: AR Collector coordinates with Sales Rep and Billing to resolve dispute within 5 business days | AR Collector / System | AR Supervisor | 10–15 min/account |
| 3 | **31–60 days overdue (active collection)**: (a) AR Collector makes weekly follow-up call/email per account; (b) AR Collector and assigned Sales Rep make joint call to customer (Sales Rep relationship leverage); (c) if customer acknowledges debt but requests extension: AR Collector processes payment term extension request with AR Supervisor approval (maximum 30-day extension, one-time per invoice); (d) if customer is unresponsive after 3 contact attempts: system flags account as "Unresponsive" and escalates to AR Supervisor | AR Collector / Sales Rep | AR Supervisor | 20 min/account |
| 4 | **61–90 days overdue (escalation)**: (a) AR Supervisor sends formal demand letter (first demand) via registered mail with return card — includes outstanding amount, invoice references, payment demand within 15 days, and notice of potential credit hold; (b) system places account on **credit hold** — new orders blocked until overdue balance resolved; credit hold override per CTL-05 requires Finance Manager approval; (c) AR Supervisor contacts customer's management (not just accounts payable contact) to negotiate payment plan; (d) if customer agrees to payment plan: AR Supervisor records plan in system with installment dates and amounts; system monitors compliance and auto-escalates if any installment missed | AR Supervisor | Finance Manager | 30 min/account |
| 5 | **91–180 days overdue (legal escalation)**: (a) Finance Manager sends second demand letter via registered mail with notice of potential legal action; (b) Finance Manager and Sales Manager jointly evaluate account: (i) is the customer still active (recent orders, store visits)?, (ii) is there a legitimate dispute?, (iii) is the business still operating?, (iv) what is the total exposure including unbilled orders?; (c) for active customers with temporary cash flow issues: Finance Manager may approve structured payment plan (maximum 6 months) with personal guarantee or post-dated checks; (d) for unresponsive or unwilling customers: Finance Manager escalates to Legal for legal demand letter (third and final demand per Philippine legal practice); (e) Legal reviews account documentation (invoices, delivery receipts signed by customer, demand letters sent, contact logs) and issues final demand letter; (f) system reclassifies receivable to "Litigation" status | Finance Manager / Legal | Controller | 1 hour/account |
| 6 | **181+ days overdue (external collection / write-off)**: (a) Controller reviews all accounts in 181+ day bucket monthly; (b) for accounts with total exposure > PHP 200,000: Controller recommends engagement of external collection agency per W62 service contract; (c) for accounts where Legal confirms no viable recovery path: Controller initiates bad debt write-off per W81 with supporting documentation (demand letters, contact logs, Legal opinion, agency report); (d) for accounts where customer has partially paid and committed to remaining balance: AR Supervisor monitors payment plan compliance; (e) system maintains full collection history per account for future credit decisions | Controller / AR Supervisor | CFO | 30 min/account review |
| 7 | **Collection agency coordination**: (a) Finance Manager engages licensed collection agency per W62 non-PO contract; (b) AR Supervisor provides agency with complete account documentation package; (c) agency operates on contingency fee basis (typically 10–20% of recovered amount); (d) AR Supervisor monitors agency performance monthly; (e) recovered amounts posted by AR Collector against customer's outstanding balance; (f) agency fees invoiced and processed per W7 | AR Supervisor / Finance Manager | Controller | Ongoing |
| 8 | **Weekly collection review**: AR Supervisor conducts weekly collection team meeting: (a) review accounts entering new aging buckets, (b) track contact completion rates (target: 100% of accounts contacted within SLA), (c) review payment plan compliance, (d) assign escalated accounts to collectors, (e) identify accounts requiring Sales Rep intervention | AR Supervisor | Finance Manager | 1 hour/week |
| 9 | **Monthly collection performance reporting**: AR Supervisor prepares monthly collection performance report for Controller and CFO: (a) total AR aging by bucket and trend, (b) days sales outstanding (DSO) — target: < 45 days, (c) collection effectiveness index (CEI) — target: ≥ 85%, (d) bad debt write-off rate as % of revenue — target: < 0.3%, (e) accounts on credit hold — count and value, (f) payment plan portfolio — total value, compliance rate, (g) top 20 overdue accounts by value with status and action plan, (h) Sales Rep territory collection performance comparison | AR Supervisor | Controller | 2 hours/month |
| 10 | **Quarterly credit review trigger**: Accounts that reached 61+ days overdue during the quarter are flagged for credit limit review in the next quarterly credit review cycle per W24; AR Supervisor provides collection history and recommendation (maintain limit, reduce limit, convert to COD-only, or close account) to Credit Committee | AR Supervisor | Finance Manager | Part of W24 quarterly cycle |

### System Touchpoints
- Automated daily AR aging report with customer contact details, Sales Rep assignment, and collection status (W108.1)
- Automated payment reminders via email/SMS at configurable intervals (W108.2)
- Collection activity logging: contact attempts, customer responses, committed payment dates, dispute notes (W108.2–3)
- Payment term extension request workflow with AR Supervisor approval (W108.3c)
- Credit hold automation: system places hold at 61 days overdue; manual override per CTL-05 (W108.4b)
- Payment plan creation and compliance monitoring with auto-escalation on missed installments (W108.4d)
- Demand letter generation with registered mail tracking (W108.4a, W108.5a)
- Collection agency engagement and performance tracking (W108.7)
- Monthly collection performance dashboard: DSO, CEI, aging trend, write-off rate (W108.9)
- Integration with W7 (AP — collection agency fee processing), W8 (AR — invoice aging, credit memos, credit holds), W24 (credit application — credit limit review triggered by collection history), W58 (corporate accounts — project billing collection), W81 (bad debt write-off — accounts reaching write-off threshold), W84 (customer account reactivation — written-off accounts)

### Staffing Implication
- **2–3 AR Collectors** (within existing ~35-person Finance team): ~5,200 active accounts with ~30–40% overdue at any time = ~1,500–2,000 accounts requiring active collection management. At ~15 min average per account per month = ~375–500 hours/month. With 2–3 collectors that's ~150–250 hours each/month = ~8–15 hours/day. This is a full-time role for 2–3 staff. Current AR team can absorb with dedicated collectors.
- **AR Supervisor**: adds ~1 hour/week for team meeting + ~2 hours/month for performance reporting + escalation handling. Absorbed within existing AR Supervisor role.
- **No incremental headcount.**

---

## W137. Intercompany Dividend & Loan Management

| Field | Detail |
|---|---|
| **Trigger** | Cash flow optimization or profit distribution request |
| **Frequency** | Quarterly or Annual |
| **Volume** | ~10–20 intercompany loan/dividend movements per year |
| **Owner** | Treasury Manager |
| **Participants** | CFO, CEO, Legal (W124), Tax Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Cash Surplus Identification: Determine excess cash in subsidiary entities | Treasury Mgr | CFO | 2 days |
| 2 | Loan/Dividend Structuring: Determine optimal transfer method (Loan vs. Dividend) | Tax Manager | CFO | 3 days |
| 3 | Documentation: Draft loan agreement or board resolution (W124) | Legal Counsel | Corp Secretary | 3 days |
| 4 | Execution: Process fund transfer and record in ERP (W14) | Treasury Analyst | Treasury Mgr | 1 day |
| 5 | Monitoring: Track interest accruals (for loans) and withholding tax (for dividends) | GL Accountant | Tax Manager | Monthly |
| 6 | Elimination: Ensure intercompany loans/dividends are eliminated in consolidation (W9) | Consolidation Mgr | CFO | Monthly |

---

### System Touchpoints (Finance Extensions)
- Intercompany loan sub-ledger with auto-interest calculation
- Withholding tax tracking for intercompany dividends (BIR Form 1601-E)
- Automated IC elimination rules in Consolidation module
- Treasury dashboard showing liquidity across all 5 legal entities

---

---

## W174. Store-Level Cash-in-Transit (CIT) & Armored Car Management

| Field | Detail |
|---|---|
| **Trigger** | Daily store cash accumulation exceeds threshold; scheduled armoured car pickup |
| **Frequency** | Daily per store (365 days/year) |
| **Volume** | ~PHP 2.1M/day average cash per store (42% of PHP 5B monthly retail sales) |
| **Owner** | Treasury Manager |
| **Participants** | Store Manager, Lead Cashier, Armoured Car Vendor, Treasury Analyst |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Cash Consolidation**: Lead Cashier performs EOD cash count; reconciles with POS Z-reports (W5f) | Lead Cashier | Store Manager | 30 min |
| 2 | **Secure Bagging**: Reconciled cash placed in tamper-evident CIT bags with serialized seals; system logs seal numbers | Store Manager | Store Manager | 10 min |
| 3 | **Pickup Verification**: Armoured car arrives; Store Manager verifies guard IDs and vehicle number against authorized list | Store Manager | Store Manager | 5 min |
| 4 | **Handover**: Guard scans CIT bags; Store Manager and Guard sign electronic/physical manifest; copy stored in ERP | Store Manager / Guard | Store Manager | 5 min |
| 5 | **System Posting**: Store Manager marks cash as "In-Transit to Bank"; ERP reduces Store Cash account, increases CIT account | Store Manager | — | Automated |
| 6 | **Bank Acknowledgment**: Bank/CIT vendor processes cash; sends daily credit report | CIT Vendor | — | Next Day |
| 7 | **Reconciliation**: Treasury Analyst matches Bank Credit to Store CIT record; investigates variances > PHP 100 | Treasury Analyst | Treasury Mgr | 2 hours/day |

### System Touchpoints
- POS EOD / Z-report integration
- Serialized CIT bag/seal tracking
- Guard/Vehicle authorization whitelist
- Bank credit file auto-matching (W30)
- Shortage/Overage exception reporting

---

## W175. Employee Gratuity & Retirement Fund Management (RA 7641)

| Field | Detail |
|---|---|
| **Trigger** | Employee retirement; annual actuarial valuation; monthly fund contribution |
| **Owner** | CFO |
| **Participants** | HR Manager, Controller, External Actuary, Trust Bank |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Provisioning**: Monthly: Finance calculates retirement expense provision based on salary and service years per RA 7641 | System | Controller | Automated |
| 2 | **Fund Contribution**: Quarterly: Treasury remits cash to the retirement trust fund managed by a Trust Bank | Treasury Mgr | CFO | 30 min |
| 3 | **Annual Valuation**: External Actuary performs PFRS-compliant valuation (PAS 19) of the defined benefit obligation | Actuary | CFO | 1 week |
| 4 | **Retirement Trigger**: Employee reaches retirement age or qualifies for early retirement | HR Manager | — | — |
| 5 | **Computation**: HR calculates retirement pay per law (at least 1/2 month salary per year of service) | HR Manager | CFO | 1 hour |
| 6 | **Disbursement**: Trust Bank releases funds to the employee; Finance adjusts the retirement liability in ERP | Finance Clerk | Controller | 1 day |

### System Touchpoints
- Employee service-year tracking
- Automatic monthly provision (Accrual) posting
- Integration with Payroll (W10) for final pay computation
- Actuarial gain/loss adjustment entry (OCI)

