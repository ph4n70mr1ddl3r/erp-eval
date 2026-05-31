# Procurement & Vendor Management Workflows

> Purchase orders, vendor onboarding, VMI, special orders, vendor performance, and contracts.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W2. Procurement — Purchase Order Cycle](#procurement-purchase-order-cycle)
- [W2a. Procurement — Auto-Replenishment (ROP/MRP)](#procurement--auto-replenishment-ropmrp)
- [W2b. Import Purchase Orders & Landed Cost](#import-purchase-orders--landed-cost)
- [W2c. Blanket Purchase Orders](#blanket-purchase-orders)
- [W20. Vendor Managed Inventory (VMI)](#vendor-managed-inventory-vmi)
- [W36. Vendor Onboarding](#vendor-onboarding)
- [W38. Special Order / Non-Stock Item Fulfillment](#special-order-non-stock-item-fulfillment)
- [W44. Vendor Performance Review](#vendor-performance-review)
- [W60. Emergency Procurement](#emergency-procurement)
- [W62. Vendor Contract Lifecycle (Non-PO Contracts)](#vendor-contract-lifecycle-non-po-contracts)
- [W62b. 3PL / Logistics Partner Onboarding & Contract Lifecycle](#3pl--logistics-partner-onboarding--contract-lifecycle)
- [W88. Return to Vendor (RTV) Processing](#rtv-processing)
- [W110. Supplier Quality & CAPA (Corrective and Preventive Action)](#supplier-quality-capa-corrective-and-preventive-action)
- [W115. Supplier Diversity & MSME Development Program](#supplier-diversity-msme-development-program)
- [W136. Indirect / Non-Merchandise Procurement](#indirect-non-merchandise-procurement)
- [W150. Product Quality Testing & Certification](#product-quality-testing--certification)
- [W155. Vendor Strategic Collaboration & Joint Business Planning (JBP)](#vendor-strategic-collaboration--joint-business-planning-jbp)
- [W160. Private Label Factory Audit & Social Compliance](#private-label-factory-audit--social-compliance)
- [W161. Vendor Price Protection & Market Markdown Claims](#vendor-price-protection--market-markdown-claims)
- [W244. Vendor Invoice Dispute & Discrepancy Resolution](#vendor-invoice-dispute--discrepancy-resolution)
- [W245. Vendor Performance Chargebacks & Penalties Management](#vendor-performance-chargebacks--penalties-management)

---

## W2. Procurement — Purchase Order Cycle

### W2a. Auto-Replenishment (Stocking Items)

| Field | Detail |
|---|---|
| **Trigger** | SKU hits reorder point (ROP) in system |
| **Frequency** | Daily review; POs generated daily |
| **Volume** | ~1,200 merchandise POs/month (auto-replenishment + ad-hoc); ~18,000 PO lines/month; excludes ~80–240 blanket/contract release orders/month (W2c), ~20–30 import POs/month (W2b), and ~30–50 non-merchandise POs/month (capex, IT, supplies); total all types: ~1,400–1,600 POs/month |

> **PO-to-GR ratio**: ~1,200 merchandise POs generate ~6,000 DC goods receipts/month (W3) — an average of ~5 GRs per PO. This ratio reflects partial shipments (vendors delivering across multiple drops), scheduled phased deliveries for large POs, and blanket PO releases each generating a separate GR. Import POs (W2b) typically generate 1 GR per container. DSD POs delivered to stores generate store-level GRs (W18) outside the DC receiving workflow.
| **Owner** | Buyer |
| **Participants** | System (auto-suggest), Buyer, Category Manager (approval if > PHP 50K) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System calculates ROP breaches based on: avg daily demand × lead time + safety stock | System | — | Automated |
| 2 | System generates suggested POs grouped by vendor, consolidated across DCs | System | — | Automated |
| 3 | Buyer reviews suggested PO list each morning: check quantities, adjust if needed | Buyer | Category Manager | 1–2 hours/day |
| 4 | Buyer confirms or modifies PO quantities, delivery dates, and DC destinations | Buyer | Category Manager | 1–2 hours/day |
| 5 | If PO total > PHP 50K: route to Category Manager for approval | Category Manager | Category Manager | 15 min/PO |
| 6 | If PO total > PHP 500K: route to VP Merchandising for approval | VP Merchandising | VP Merchandising | 15 min/PO |
| 7 | Approved PO transmitted to vendor (email, EDI, or vendor portal); vendors with portal access can view PO details, confirm delivery dates, and submit invoices through the portal | System / Buyer | Buyer | Automated |
| 8 | Buyer tracks open POs; follows up on overdue deliveries | Buyer | Buyer | 1 hour/day |

**Total buyer effort**: ~3–5 hours/day for daily PO review and follow-up

### PO Lifecycle: Amendment, Cancellation & Close

| Activity | Trigger | Approval | System Action |
|---|---|---|---|
| **PO Amendment** | Buyer needs to change quantity, delivery date, price, or add/remove lines on an approved PO | Re-approval per tiered matrix (same thresholds as original PO: > PHP 50K → Category Manager, > PHP 500K → VP Merchandising, > PHP 2M → CFO for imports) if change exceeds materiality threshold (quantity change > 20%, price change > 5%, or any delivery date change); minor changes (within threshold) auto-approved with Buyer note | System transmits amendment to vendor (email, EDI, or portal); tracks amendment history with full audit trail (original values, amended values, reason code, approver ID, timestamp); for import POs (W2b), Finance notifies bank if LC amendment is required for value changes |
| **PO Cancellation** | Vendor cannot deliver, demand drops, item discontinued, or PO no longer needed | Buyer initiates with reason code; Category Manager approval required for cancellations > PHP 50K; VP Merchandising for > PHP 500K | System checks for existing GR against PO: if no GR, auto-cancels with vendor notification; if partial GR, Buyer confirms close of remaining quantity; system releases budget commitment; cancelled PO retained in audit trail |
| **PO Auto-Close** | PO fully received (GR quantity matches ordered quantity within tolerance) or PO open beyond configured age limit | Automated | System auto-closes fully received POs; system flags POs open > 90 days for Buyer review (dashboard alert); Buyer reviews aged POs weekly and decides: close remaining quantity, extend delivery date (amendment), or escalate to Category Manager |

### System Touchpoints (PO Lifecycle)
- PO amendment workflow with materiality thresholds triggering re-approval (W2a)
- Amendment history with full audit trail: original vs. amended values, reason, approver (W2a)
- Vendor notification on amendment (email/EDI/portal) (W2a)
- Import PO LC amendment trigger (cross-reference W2b) (W2a)
- PO cancellation with reason code and budget release (W2a)
- Partial-receipt PO close workflow (W2a)
- Auto-close rules: tolerance-based for fully received POs; aging threshold for open POs (W2a)

### W2b. Import Purchase Orders

| Field | Detail |
|---|---|
| **Trigger** | Seasonal buy plan or replenishment of import SKUs |
| **Frequency** | ~20–30 import POs/month |
| **Volume** | ~400–600 TEUs/month across all import vendors (per model-company-profile §7.1); ~15–25 TEUs per major import PO |
| **Owner** | Buyer (with Import Coordinator) |
| **Participants** | Buyer, Import Coordinator, Finance (LC), Customs Broker, Warehouse (receiving) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Buyer creates import PO with estimated landed cost (FOB + freight + duty + insurance) | Buyer | Category Manager | 30 min/PO |
| 2 | Route for approval (> PHP 50K → Category Manager; > PHP 500K → VP Merchandising; > PHP 2M → CFO) | Category Manager / VP / CFO | As per tier | 15–30 min/PO |
| 3 | Finance opens Letter of Credit (LC) with bank or arranges TT payment | Treasury Analyst | CFO | 1–2 hours/PO |
| 4 | Buyer confirms order with vendor; vendor provides Proforma Invoice | Buyer | Buyer | 30 min/PO |
| 5 | Import Coordinator arranges freight booking (container) | Import Coordinator | Buyer | 1 hour/PO |
| 6 | Vendor ships; provides Bill of Lading (BL), Packing List, Commercial Invoice | Vendor | — | External |
| 7 | Import Coordinator receives shipping docs; engages customs broker | Import Coordinator | Import Coordinator | 1 hour/PO |
| 8 | Customs broker files import entry; pays duties/taxes | Customs Broker | Import Coordinator | 1–2 days |
| 9 | Import Coordinator tracks shipment status; updates ETA in system | Import Coordinator | Buyer | 15 min/day per PO |
| 10 | Goods arrive at port; customs clearance and release | Customs Broker | Import Coordinator | 1–3 days |
| 11 | Transport to DC; Receiving clerk processes Goods Receipt | Receiving Clerk (DC) | DC Manager | 2–4 hours/container |
| 12 | System calculates actual landed cost (duty, freight, insurance allocated per SKU) using GR exchange rate | System | Finance | Automated |
| 13 | Finance reconciles LC/TT payment with PO and Goods Receipt; system posts FX gain/loss if invoice rate differs from GR rate | Treasury Analyst | CFO | 30 min/PO |

**Total cycle time**: 45–90 days from PO to receipt

### System Touchpoints
- ROP/EOQ auto-calculation per SKU per location (W2a.1–2)
- PO creation with multi-tier approval workflow (W2a.5–6)
- Vendor PO transmission (W2a.7)
- Open PO tracking / overdue alerts (W2a.8)
- Import PO tracking with LC/BL/container fields (W2b.1–9)
- Landed cost calculation engine (W2b.12)
- 3-way match: PO → Goods Receipt → Vendor Invoice (W2b.13)
- FX rate capture at PO creation (budget rate), goods receipt (spot rate or BSR), and invoice (actual rate); automatic FX gain/loss posting (W2b.12–13)
- Month-end FX revaluation of open foreign-currency balances at BIR exchange rate with unrealized FX gain/loss posting and auto-reversal (W9a.5a)

### W2c. Blanket / Contract Purchase Orders

| Field | Detail |
|---|---|
| **Trigger** | Annual supply agreement negotiation cycle |
| **Frequency** | ~40–60 active contracts at any time; new contracts and renewals throughout the year |
| **Volume** | Primarily with top 50 vendors (by spend); typically covers 20–60% of purchasing volume for staple categories (cement, paint, lumber, electrical cable, plumbing fittings) |
| **Owner** | Buyer |
| **Participants** | Buyer, Category Manager, VP Merchandising, Finance (budget), Vendor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Buyer negotiates annual supply agreement with vendor: product range, pricing tiers, minimum/maximum commitment quantities, delivery schedule, payment terms, rebate structure | Buyer | Category Manager | 4–8 hours/vendor |
| 2 | Category Manager approves contract terms; VP Merchandising approves if total contract value > PHP 5M | Category Manager / VP | VP Merchandising | 30 min |
| 3 | Finance validates contract commitment against annual purchase budget | Controller | CFO | 30 min |
| 4 | Buyer creates Blanket PO in system: vendor, SKU lines with contract price, validity period (typically 1 year), min/max commitment quantities, agreed delivery schedule or release parameters | Buyer | Category Manager | 30–60 min |
| 5 | System enforces contract pricing on all release orders; alerts Buyer if release quantity would exceed maximum commitment | System | — | Automated |
| 6 | Buyer or system creates Release Order against Blanket PO (per agreed schedule or triggered by ROP): specifies exact quantity and delivery date for this release | Buyer / System | Buyer | 10 min |
| 7 | Release Order follows standard PO approval (W2a.5–6) if release value exceeds threshold; otherwise auto-approved within contract parameters | System | — | Automated |
| 8 | Vendor ships per release order; standard receiving (W3) and AP matching (W7) apply | Vendor | Buyer | Per W3/W7 |
| 9 | System tracks cumulative released quantity and value against contract commitment; Buyer monitors to ensure min-commit targets are met | System | Buyer | Automated |
| 10 | Monthly: Buyer reviews contract utilization report; identifies contracts below minimum commitment pace (risk of penalty or unfavorable renegotiation) | Buyer | Category Manager | 1 hour/month |
| 11 | Quarterly: Buyer and Category Manager evaluate contract performance vs. spot buying; decide renewal, renegotiation, or termination | Buyer + Category Manager | VP Merchandising | 2 hours/quarter |
| 12 | At contract expiry: system alerts Buyer 60 days before; if not renewed, system blocks further release orders | System | — | Automated |

**Contract coverage**: ~40–60 active blanket/contract POs at any time, representing ~45% of annual COGS (aligned with top-20 vendor concentration)

### Vendor Rebate Dispute Resolution

| Field | Detail |
|---|---|
| **Trigger** | Vendor disputes rebate settlement amount calculated by BuildRight's system (W27 step 6) |
| **Frequency** | Occasional — estimated 5–10 disputes/year |
| **Dispute SLA** | 15 business days from dispute raised to resolution |
| **Owner** | Buyer |
| **Participants** | Buyer, Category Manager, Cost Accountant, Finance Manager |

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|
| 1 | Vendor disputes settlement amount: Buyer receives vendor's written objection with vendor's calculation | Buyer | Category Manager | 15 min |
| 2 | Buyer and Cost Accountant jointly review: compare BuildRight's settlement data (qualifying volume, rebate rate applied) to vendor's claim; identify specific discrepancy (volume count difference, rate tier interpretation, timing gap, excluded transactions) | Buyer / Cost Accountant | Category Manager | 30–60 min |
| 3 | If BuildRight calculation confirmed correct: Buyer responds to vendor with supporting data; dispute closed; no settlement adjustment | Buyer | Category Manager | 15 min |
| 4 | If partial vendor claim valid: Buyer proposes adjusted settlement; Category Manager approves adjustment; Cost Accountant posts adjustment with Category Manager approval and documentation in system | Buyer / Category Manager / Cost Accountant | Finance Manager | 30 min |
| 5 | If dispute unresolved within 15 business days: Buyer escalates to Finance Manager for mediation; Finance Manager reviews both calculations and makes binding recommendation within 5 business days | Finance Manager | CFO | 30 min |
| 6 | Monthly: Cost Accountant tracks rebate dispute frequency and resolution time per vendor; feeds into vendor scorecard (W44); chronic disputing vendors flagged for contract renegotiation (W2c) | Cost Accountant | Controller | 15 min/month |

### System Touchpoints
- Blanket/contract PO creation with SKU lines, pricing tiers, validity dates, and commitment quantities (W2c.4)
- Contract pricing enforcement on release orders (W2c.5)
- Release order creation against blanket PO with quantity tracking (W2c.6–7)
- Cumulative commitment tracking: released vs. minimum vs. maximum (W2c.9)
- Contract utilization reporting (W2c.10)
- Contract expiry alerting with release order blocking (W2c.12)
- Integration with W27 (vendor rebates — rebates may be tied to contract commitment achievement; rebate dispute resolution per W27 dispute SLA of 15 business days)

### Staffing Implication
- **Buyers**: 40–60 contracts ÷ 10–12 buyers = ~4–5 contracts each. Monthly review adds ~1 hour/buyer/month. Quarterly evaluation adds ~2 hours/buyer/quarter. Absorbed within existing team.
- No incremental headcount beyond existing Buyer and Finance teams.

---



---

## W20. Vendor Managed Inventory (VMI)

| Field | Detail |
|---|---|
| **Trigger** | VMI vendor reviews sell-through data or system sends replenishment signal |
| **Frequency** | Varies by vendor (typically weekly or bi-weekly) |
| **Volume** | ~300 SKUs from 12 key vendors |
| **Owner** | Buyer (oversight) |
| **Participants** | VMI Vendor, Buyer, Receiving Clerk (DC or Store), AP Clerk |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System shares sell-through data and current stock levels with VMI vendor (EDI or portal) | System | Buyer | Automated |
| 2 | VMI vendor analyzes data and determines replenishment quantities | VMI Vendor | VMI Vendor | External |
| 3 | VMI vendor creates shipment; provides Advance Shipping Notice (ASN) to system | VMI Vendor | Buyer | External |
| 4 | Buyer reviews and confirms ASN; or system auto-confirms if within agreed parameters | Buyer / System | Buyer | 10 min/batch |
| 5 | Vendor ships goods to DC or store per agreement | VMI Vendor | — | External |
| 6 | Receiving Clerk processes Goods Receipt against ASN (standard receiving process) | Receiving Clerk | Dept. Supervisor / DC Supervisor | Per W3 or W18 |
| 7 | Goods recorded as vendor-owned inventory in system (non-valuated until sold) | System | — | Automated |
| 7a | At month-end close (W9): system accrues VMI liability for all VMI goods sold but not yet settled with vendor; Cost Accountant includes VMI accrual in monthly close entries | System / Cost Accountant | Controller | Automated + 15 min/month |
| 8 | At POS: system records sell-through event per VMI SKU; ownership transfers at point of sale | System | — | Automated |
| 9 | Monthly: system generates VMI sell-through report per vendor showing units sold × agreed price | System | Buyer | Automated |
| 10 | Buyer reviews sell-through report; confirms settlement | Buyer | Category Manager | 1 hour/month/vendor |
| 11 | System generates AP invoice from sell-through data; vendor payment processed | System / AP Clerk | AP Supervisor | Automated + 30 min |

**Settlement cycle**: Monthly per VMI vendor

### System Touchpoints
- Sell-through data export to vendor (EDI/portal/API) (W20.1)
- ASN receipt and processing from vendor (W20.3)
- Non-valuated (vendor-owned) inventory tracking (W20.7)
- Sell-through event capture at POS (W20.8)
- VMI settlement report generation (W20.9)
- Auto-generation of AP from sell-through (W20.11)
- Quarterly VMI vendor statement reconciliation: Cost Accountant generates VMI statement reconciliation report per vendor — compares BuildRight's recorded VMI sell-through (units sold × agreed price) to vendor's statement of goods shipped and settled; investigates discrepancies (unrecorded sell-through, missing GRs, pricing differences, timing gaps); reconciling items documented and resolved within 15 business days; unreconciled differences > PHP 50,000 escalated to Controller; results feed into annual IC audit and vendor scorecard (W44) (W20)
- Integration with W44 (vendor scorecard), W7 (AP settlement), W42 (physical inventory vendor-owned count)

### Staffing Implication
- **Buyer time**: 12 VMI vendors × 1 hour/month review = 12 hours/month. Spread across 10–12 buyers, this is ~1 hour each per month. Minimal impact.
- **AP**: VMI settlement adds 12 additional AP invoices/month. Negligible incremental load.

---



---

## W36. Vendor Onboarding

| Field | Detail |
|---|---|
| **Trigger** | New vendor identified by Buyer or Category Manager (new product sourcing, alternative supplier, new brand) |
| **Frequency** | ~50–100 new vendors/year (replacing churned vendors + new categories) |
| **Volume** | Peaks during seasonal planning (W32) and new store openings (W16) |
| **Owner** | Buyer |
| **Participants** | Buyer, Category Manager, AP Clerk, Finance (credit assessment), IT (portal setup) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Buyer identifies need for new vendor; collects basic information: company name, contact person, product categories offered, business registration | Buyer | Category Manager | 30 min |
| 2 | Buyer sends vendor application form to prospective vendor; vendor provides: DTI/SEC registration, BIR TIN, business permit, tax compliance certificate, bank certificate, product catalog with SRP | Buyer | Category Manager | External (vendor-dependent) |
| 3 | AP Clerk or Finance validates vendor documents: confirms TIN is valid, business permit is current, bank details verified | AP Clerk | AP Supervisor | 30 min |
| 4 | Buyer evaluates vendor capability: product quality (sample review), pricing competitiveness (vs. current vendors), delivery lead time, minimum order quantities, payment terms offered | Buyer | Category Manager | 2–4 hours |
| 5 | Category Manager approves vendor for onboarding (or rejects with reason) | Category Manager | VP Merchandising | 15 min |
| 6 | Buyer creates vendor master record in system: name, TIN, address, contact details, payment terms, bank account, currency, lead time, assigned category, entity(ies) | Buyer | Category Manager | 15 min |
| 7 | System assigns vendor number; configures: approval tier for PO amounts, default PO delivery location(s), matching tolerance for invoice price variance | System | — | Automated |
| 7a | **Vendor bank account change control**: if an existing vendor requests a change to their bank account details (new account number, new bank), the change requires a mandatory out-of-band verification before system update — (a) AP Clerk receives vendor bank change request (email, letter, or portal submission); (b) AP Clerk contacts vendor using the **known** phone number or contact person from vendor master (NOT the contact information in the change request itself, to prevent authorized push payment fraud); (c) AP Clerk verbally confirms the bank change with an authorized vendor representative; (d) AP Supervisor approves the bank detail change in system with verification notes (who confirmed, date, phone number used); (e) system requires dual approval (AP Clerk entry + AP Supervisor approval) for all bank detail changes; (f) system logs change with old bank details, new bank details, verifying AP Clerk ID, approving AP Supervisor ID, verification method, and timestamp; (g) system temporarily blocks payment to the vendor for 48 hours after bank detail change as a cooling-off period; (h) first payment to new bank account is flagged for Treasury Analyst confirmation of receipt before subsequent payments are auto-processed | AP Clerk / AP Supervisor | AP Supervisor | 30 min/change |
| 7b | **Vendor master data change log**: all changes to vendor master data (bank details, payment terms, address, contact information, tax classification) are logged with full audit trail — old value, new value, changed by, approved by, date, reason; changes to bank details and payment terms require AP Supervisor approval; changes to tax classification require Finance Manager approval; monthly: AP Supervisor reviews vendor master change log as part of AP controls review (cross-reference CTL-42 in Internal Controls Matrix) | System / AP Clerk | AP Supervisor | Automated + 30 min/month review |
| 8 | Merchandise Planner maps vendor's product catalog to item master: creates new SKUs or links to existing SKUs; sets vendor-specific cost, lead time, minimum order quantity, order multiple | Merchandise Planner | Buyer | 1–2 hours/vendor (varies by catalog size) |
| 9 | IT configures vendor portal access (if vendor uses portal): credentials, PO visibility, invoice submission capability | IT Team | Buyer | 15 min |
| 10 | Buyer places trial PO (small initial order) to validate vendor reliability, product quality at scale, and delivery performance | Buyer | Category Manager | Per W2 |
| 11 | After 3 trial orders: Buyer completes vendor scorecard baseline (delivery on-time %, quality reject rate, invoice accuracy) for future performance tracking (W44) | Buyer | Category Manager | 30 min |

**Total onboarding cycle**: 2–4 weeks from identification to first PO

### System Touchpoints
- Vendor master creation with document attachments (W36.6)
- TIN validation and business permit tracking with expiry alerts (W36.3, W36.6)
- Vendor-specific configuration: payment terms, tolerance thresholds, approval tiers (W36.7)
- Item-vendor mapping with cost, lead time, MOQ (W36.8)
- Vendor portal provisioning (W36.9)
- Vendor document tracking with expiry alerts: system tracks business permit, tax compliance certificate, and other regulatory document expiry dates; alerts Buyer and AP Clerk 30 days before expiry; vendor blocked from new POs if documents expired
- Vendor lead time master data lifecycle: initial lead time entered during vendor onboarding per vendor-SKU (W36 step 8); ongoing maintenance — Buyer updates lead times when vendor notifies of changes (new warehouse, route change, seasonal factors); system auto-suggests lead time updates based on actual delivery performance (comparing actual GR date vs. PO promised date) and presents suggestions to Buyer for review and confirmation; quarterly review per W31 step 8 confirms or adjusts stale lead times; system tracks all lead time changes with full audit trail (old value, new value, reason, date, Buyer ID); lead time variance metric feeds vendor scorecard (W44) (W36.6, W36.8)
- Integration with vendor performance scorecard (W36.11 → W44)

### Staffing Implication
- **Buyer**: 50–100 new vendors/year × ~4–6 hours of buyer time each = 200–600 hours/year = ~1–3 hours/week. Absorbed across 10–12 buyers.
- **AP Clerk**: 30 min per vendor for document validation = ~25–50 hours/year. Negligible.
- **Merchandise Planner**: Item-vendor mapping is the most labor-intensive step at 1–2 hours per vendor. With 50–100 vendors = ~100 hours/year. Absorbed within existing team.

---



---

## W38. Special Order / Non-Stock Item Fulfillment

| Field | Detail |
|---|---|
| **Trigger** | Customer requests an item not carried in regular store assortment |
| **Frequency** | ~500–1,000 special orders/month chain-wide; ~2–5 per store per month |
| **Volume** | Primarily professional trade customers (contractors, builders) and project-specific items; avg order value ~PHP 5,000–15,000 |
| **Owner** | Customer Service Rep (order intake); Buyer (fulfillment) |
| **Participants** | CSR, Sales Rep (trade accounts), Buyer, Receiving Clerk, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer requests non-stock item at store (CSR counter) or via Sales Rep; provides product description, specification, quantity needed, and desired delivery date | Customer | — | — |
| 2 | CSR or Sales Rep searches item in system: (a) checks if item exists in item master as non-stock/Special Order type, (b) if not found, creates a non-stock item request with description, specs, and estimated price | CSR / Sales Rep | Dept. Supervisor | 5–10 min |
| 3 | System routes non-stock item creation request to Merchandise Planner for item master setup (category assignment, unit of measure, tax classification) | System | Merchandise Planner | Automated routing |
| 3a | Merchandise Planner creates non-stock SKU in item master with type = "Special Order / Non-Stock"; flags as non-stocking (no ROP, no safety stock, no replenishment) | Merchandise Planner | Category Manager | 10 min |
| 4 | Buyer identifies vendor, obtains quotation (price, lead time, minimum quantity); enters quote in system linked to the non-stock SKU | Buyer | Category Manager | 30–60 min |
| 5 | CSR or Sales Rep communicates quote to customer: price, estimated delivery date, payment terms (typically 50% deposit, 50% on delivery) | CSR / Sales Rep | — | 10 min |
| 6 | Customer confirms order and pays deposit; system records deposit as liability (Cr. Customer Deposits Payable / Dr. Cash); not recognized as revenue until delivery | Customer / Cashier | — | 5 min |
| 6a | **Trade/corporate account customers**: if customer holds an active trade or corporate account (W24), deposit requirement is waived for orders within the customer's available credit limit; system checks credit limit at order creation — if credit available, Sales Associate or CSR selects "Charge to Account" and system posts order value to customer's AR account (W8) upon delivery (no deposit liability); if order exceeds available credit, system prompts for partial deposit covering the excess; for special orders > PHP 50,000 on account, system routes for AR Supervisor approval per W24 tiered matrix | Sales Associate / CSR | AR Supervisor | 2 min |
| 7 | System creates Sales Order linked to non-stock SKU with customer deposit recorded; reservation created against incoming PO | System | — | Automated |
| 8 | Buyer creates Special Order PO (links PO to Sales Order); routes for approval per standard tiered matrix (W2) | Buyer | Category Manager | Per W2 |
| 9 | Buyer tracks PO; follows up with vendor on delivery schedule | Buyer | Buyer | Per W2 |
| 10 | Goods received at store or DC (per W3 or W18); system matches GR to both PO and linked Sales Order | Receiving Clerk | Dept. Supervisor | Per W3/W18 |
| 11 | System alerts CSR that special order has arrived; CSR contacts customer for pickup or arranges delivery | System / CSR | Store Manager | Automated + 5 min |
| 12 | Customer picks up item (or receives delivery); pays remaining balance; system recognizes revenue (Dr. Customer Deposits / Cr. Revenue) and COGS (Dr. COGS / Cr. Inventory) at delivery; Sales Order closed | Cashier / CSR | — | 5 min |
| 13 | If customer cancels before PO is placed: CSR cancels Sales Order; deposit refunded; no PO created | CSR | Store Manager | 5 min |
| 14 | If customer cancels after PO is placed but before shipment: Buyer negotiates with vendor (restocking fee, return); Finance processes partial refund less any costs | Buyer + Finance | Category Manager | 30 min |
| 15 | Unclaimed deposit management: system tracks age of customer deposits linked to completed special orders (goods received but not picked up); after 30 days with no customer response post-delivery notification, system sends reminder notification (SMS/email); after 90 days with no response, system flags deposit for review; Store Manager or Finance approves recognition of abandoned deposit as other income (Dr. Customer Deposits Payable / Cr. Other Income); goods dispositioned per standard clearance (W13.9a), RTV (W3.6a), or return to shelf | System / Store Manager / Finance | Controller | Automated + 5 min/review |
| 16 | **Customer deposit refund (before goods receipt)**: if customer requests cancellation and refund before goods are received from vendor — (a) CSR processes deposit refund in system with reason code (customer cancellation, vendor cannot deliver, project cancelled); (b) system cancels linked Sales Order and triggers Buyer to cancel or reduce the linked PO per W2a PO cancellation process (if PO not yet shipped by vendor); (c) refund issued to original payment method: if deposit paid by cash, CSR disburses from cash drawer with Store Manager authorization; if paid by card/e-wallet, system processes electronic refund (Dr. Customer Deposits Payable / Cr. Cash); if paid by trade account credit, system applies deposit back to customer's AR account; (d) system logs refund with customer ID, original deposit transaction, refund amount, refund method, CSR ID, authorizing manager ID, and reason code; (e) BIR-compliant documentation: system generates official receipt for the refund transaction with all required BIR fields (TIN, registered invoice number, description "Refund of customer deposit — Sales Order #[number]"); refund receipts retained per 7-year BIR retention policy | CSR / Store Manager | Controller | 10 min/refund |

**Total cycle time**: 7–30 days from order to delivery (depends on vendor lead time and whether domestic or import)

### System Touchpoints
- Non-stock item type in item master with no auto-replenishment (W38.3a)
- Item creation request workflow (W38.3)
- Sales Order creation with customer deposit and PO linkage (W38.7–8)
- PO-to-Sales-Order reservation and matching (W38.8, W38.10)
- Customer deposit liability tracking (Cr. Customer Deposits Payable) with revenue recognition trigger at delivery (W38.6, W38.12)
- Customer notification upon receipt (W38.11)
- Sales Order lifecycle: open → PO linked → goods received → customer notified → closed (W38.7–12)
- Cancellation handling with deposit refund workflow (W38.13–14)
- Non-stock SKU archival and cleanup: over time, the item master accumulates non-stock/special-order SKUs (type = "Special Order / Non-Stock" per W38.3a) from one-time customer orders; to prevent item master bloat — (a) monthly: Merchandise Planner generates non-stock SKU aging report listing all non-stock SKUs with no sales activity in the past 12 months; (b) Merchandise Planner reviews each stale non-stock SKU and sets status to "Non-Stock — Archived" — item remains searchable in system for transaction history but is hidden from new Sales Order creation and Sales Associate lookup; (c) archived non-stock SKUs excluded from item count in reporting and system performance metrics; (d) if a customer subsequently requests the same item, Merchandise Planner reactivates the archived SKU (updates status to active) rather than creating a duplicate; system checks for archived SKUs matching the item description before allowing new non-stock SKU creation; (e) annually: Merchandise Planner reviews all archived non-stock SKUs older than 3 years with zero transaction history and proposes permanent deletion per BIR 7-year retention compliance (items with any transaction history retained for full 7 years regardless of archival status)
- Unclaimed deposit aging: system tracks deposit age from goods-receipt date; automated reminder at 30 days; escalation flag at 90 days; abandonment recognition with approval workflow; goods disposition tracking (W38.15)

### Staffing Implication
- **CSR**: ~2–5 special orders/store/month × ~20 min each (intake + communication + handoff) = ~1–1.5 hours/store/month. Absorbed.
- **Buyer**: 500–1,000 special orders/month ÷ 10–12 buyers = ~50–80/buyer/month × ~30 min each = ~30 hours/buyer/month. This is significant. Special orders should be handled by a dedicated 1–2 Buyers who specialize in trade/special orders, with remaining buyers focused on replenishment.
- **Merchandise Planner**: 500–1,000 non-stock SKU creations/year = ~2–4 hours/week. Absorbed within existing team.

---



---

## W44. Vendor Performance Review

| Field | Detail |
|---|---|
| **Trigger** | Quarterly review calendar; or ad-hoc triggered by persistent quality/delivery issues |
| **Frequency** | Quarterly for top 50 vendors (by spend); annually for remaining active vendors |
| **Volume** | ~800–1,000 active vendors; top 50 = 45% of COGS |
| **Owner** | Buyer |
| **Participants** | Buyer, Category Manager, VP Merchandising, Receiving Supervisor (quality input), AP Supervisor (invoice accuracy input) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System auto-generates vendor scorecard per vendor for the review period with the following metrics: | System | — | Automated |
| | • **On-time delivery %**: PO lines delivered on or before promised date ÷ total PO lines | | | |
| | • **Fill rate %**: PO lines delivered at full ordered quantity ÷ total PO lines | | | |
| | • **Quality reject rate %**: GR lines rejected for quality ÷ total GR lines | | | |
| | • **Invoice accuracy %**: Invoices matching PO within tolerance on first submission ÷ total invoices | | | |
| | • **Lead time variance**: avg actual lead time vs. agreed lead time (days) | | | |
| | • **Return rate %**: RTV lines ÷ total receipt lines | | | |
| 2 | Buyer reviews scorecard; adds qualitative notes: vendor responsiveness, market reputation, new product pipeline, relationship quality | Buyer | Category Manager | 15–30 min/vendor |
| 3 | Buyer assigns overall rating: A (Preferred), B (Acceptable), C (Watch), D (Probation), F (Exit) | Buyer | Category Manager | 5 min/vendor |
| 4 | For C-rated vendors: Buyer drafts improvement plan with specific targets and timeline; communicates to vendor | Buyer | Category Manager | 30 min/vendor |
| 5 | For D/F-rated vendors: Buyer escalates to Category Manager for decision: (a) put on probation with 90-day improvement deadline, (b) initiate vendor exit process (transition to alternative vendor, settle outstanding obligations) | Buyer | VP Merchandising | 1 hour/vendor |
| 6 | Quarterly: Category Manager and VP Merchandising review top 50 vendor scorecards in portfolio review meeting; discuss strategic vendor relationships, negotiate improved terms for A-rated vendors | Category Manager | VP Merchandising | 2 hours/quarter |
| 7 | Annually: VP Merchandising and CFO review total vendor portfolio performance; approve vendor list for next year; authorize new vendor onboarding (W36) and vendor exits | VP Merchandising + CFO | CEO | 4 hours/year |
| 8 | System maintains vendor scorecard history for trend analysis; supports vendor selection decisions in W2 and W36 | System | — | Automated |
| 9 | **Corrective action execution — Warning**: Buyer communicates performance gaps to vendor in writing (email or letter) with specific metrics from scorecard; establishes 30-day improvement period with clear targets (e.g., on-time delivery must improve from 75% to 90%); Buyer monitors PO performance during improvement period via weekly scorecard snapshot | Buyer | Category Manager | 30 min/vendor |
| 10 | **Corrective action execution — Probation**: if no improvement after Warning, Buyer initiates probation — (a) Category Manager sends formal probation notice to vendor with 90-day review period and specific improvement requirements; (b) system changes vendor master status to "Probation"; (c) system blocks creation of new POs for this vendor (existing committed POs unaffected); (d) Buyer identifies alternative vendor for affected SKUs per W36; (e) Buyer monitors vendor performance weekly during probation; (f) at 90-day mark: Buyer recommends to Category Manager either reinstatement (if targets met) or termination | Buyer / Category Manager | VP Merchandising | 1 hour/vendor (initial) + 30 min/week monitoring |
| 11 | **Corrective action execution — Termination**: VP Merchandising approves termination; (a) Category Manager sends formal termination notice to vendor per contract terms (typically 30–60 day notice); (b) Buyer reviews all open POs — decides per PO: cancel, allow to complete, or expedite; (c) AP Supervisor reviews outstanding invoices and credit memos — resolves all financial obligations; (d) system changes vendor master status to "Inactive"; (e) system blocks all transactions (POs, GRs, invoices); (f) Merchandise Planner reassigns affected SKUs to alternative vendors per W36; (g) termination date, reason, and all supporting documentation recorded in vendor master audit trail | Category Manager / Buyer / AP Supervisor | VP Merchandising | 2–4 hours/vendor |
| 12 | **Corrective action execution — Reactivation**: if Buyer requests reactivation of a previously terminated vendor — (a) Buyer provides evidence of improved capability (new ownership, new processes, reference customers, corrected quality issues); (b) Category Manager reviews evidence and approves or denies; (c) if approved, vendor re-enters abbreviated onboarding per W36 (skip trial PO if recent performance history exists within 12 months); (d) system changes vendor master status back to "Active"; (e) full audit trail of termination and reactivation retained | Buyer / Category Manager | VP Merchandising | 1 hour/vendor |

| Tier | Trigger | Action | System Impact |
|---|---|---|---|
| **Warning** | Scorecard rating drops to C, or single significant incident (major quality failure, delivery causing stockout) | Buyer communicates performance gaps to vendor in writing with specific metrics; establishes 30-day improvement period with clear targets | Vendor master status remains Active; Buyer monitors PO performance during improvement period |
| **Probation** | No improvement after Warning, or scorecard rating drops to D | Vendor suspended from receiving new POs; existing committed POs are fulfilled; 90-day formal review period; Category Manager notifies vendor in writing of probation status and improvement requirements | Vendor master status changed to Probation; system blocks creation of new POs for this vendor; existing POs unaffected |
| **Termination** | No improvement after Probation, or scorecard rating F, or vendor commits fraud/breach | VP Merchandising approves termination; Category Manager notifies vendor; all open POs cancelled or allowed to complete per agreement; vendor master deactivated | Vendor master status changed to Inactive; system blocks all transactions; termination date and reason recorded in audit trail; vendor record retained for regulatory and historical purposes |
| **Reactivation** | Buyer requests reactivation with evidence of improved capability (new ownership, new processes, reference customers) | Category Manager reviews evidence; if approved, vendor re-enters onboarding process per W36 (abbreviated: skip trial PO if recent history exists) | Vendor master status changed back to Active; full audit trail of termination and reactivation retained |

### System Touchpoints
- Automated vendor scorecard generation from operational data (W44.1)
- Multi-metric scoring: on-time delivery, fill rate, quality, invoice accuracy, lead time, return rate (W44.1)
- Vendor rating system with configurable thresholds (W44.3)
- Improvement plan tracking (W44.4)
- Vendor lifecycle status: Active → Warning → Probation → Inactive (terminated) → Active (reactivated); each status change logged with reason, approver, date, and supporting documentation; system enforces PO blocking for Probation and Inactive vendors (W44.5, corrective action tiers)
- Scorecard history and trend analysis (W44.8)
- Integration with W2 (PO performance), W3 (receiving quality), W7 (invoice matching), W36 (vendor onboarding)

### Staffing Implication
- **Buyers**: Top 50 vendors reviewed quarterly × 30 min = 25 hours/quarter. Remaining ~750 vendors reviewed annually × 15 min = ~190 hours/year. Total ~290 hours/year ÷ 10 buyers = ~29 hours/buyer/year. Absorbed within existing buyer duties.
- **Category Managers**: 2 hours/quarter for portfolio review + 1 hour/quarter for escalations = ~12 hours/year. Absorbed.
- **VP Merchandising**: 2 hours/quarter for top vendor review + 4 hours/year for annual portfolio review = ~12 hours/year. Absorbed.

---



---

## W60. Emergency Procurement

| Field | Detail |
|---|---|
| **Trigger** | Urgent operational need that cannot wait for standard PO cycle (W2) and exceeds petty cash threshold (W25): critical equipment breakdown, emergency facility repair, urgent compliance requirement, sudden supply shortage threatening store operations |
| **Frequency** | ~20–30 emergency procurement events/month across all locations |
| **Volume** | PHP 50,000–500,000 per event; typically for emergency equipment, parts, or services |
| **Owner** | Requestor (Store Manager or Department Head) |
| **Participants** | Store Manager / Dept. Head, Procurement (Buyer), Finance (Controller), Vendor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Requestor identifies emergency need and justifies urgency: equipment failure impacting store operations (e.g., POS server failure, HVAC breakdown in peak summer, forklift failure at DC), compliance deadline (regulatory order), or supply emergency (critical stockout on A-item with no PO coverage) | Store Manager / Dept. Head | — | 10 min |
| 2 | Requestor submits emergency procurement request in system: item/service description, estimated cost, urgency justification, required delivery date (typically same day or next day), preferred vendor (if known) | Requestor | — | 10 min |
| 3 | System routes for expedited approval: (a) ≤ PHP 100,000: Store Manager (for stores) or Dept. Head (for HQ/DC) + Controller verbal approval, (b) PHP 100,001–500,000: CFO verbal approval required within 2 hours, (c) > PHP 500,000: CEO verbal approval required within 4 hours; system logs verbal approval with timestamp and approver ID | System | Controller / CFO / CEO | 15 min – 4 hours |
| 4 | Buyer (or Requestor for store-level purchases) contacts vendor immediately — phone call or direct purchase authorized; system allows "confirm vendor later" mode where PO is created with vendor TBD and updated after the fact | Buyer / Requestor | Category Manager | 15–30 min |
| 5 | Goods or services received immediately; standard Goods Receipt (W3) or service confirmation documented | Receiving Clerk / Requestor | Dept. Head | Per W3 |
| 6 | Within 5 business days: Buyer or AP Clerk completes documentation — formalize PO in system (if created informally), obtain vendor invoice, process 3-way match (W7) or 2-way match for services; system enforces that all emergency procurements are regularized within 5 days or escalates to Controller | Buyer / AP Clerk | Controller | 15–30 min |
| 7 | Monthly: Controller reviews emergency procurement report: total spend, frequency by location, category, and requester; flags locations or categories with excessive emergency procurement frequency for root cause analysis (supplier reliability issues, planning gaps, or maintenance neglect) | Controller | CFO | 1 hour/month |

### System Touchpoints
- Emergency procurement request form with urgency justification field (W60.2)
- Expedited approval workflow with verbal approval logging and configurable SLA timers (W60.3)
- "Vendor TBD" PO creation mode for immediate procurement with post-hoc vendor assignment (W60.4)
- Regularization enforcement: system tracks emergency procurements not yet formalized; auto-escalates at day 5 (W60.6)
- Emergency procurement analytics: spend, frequency, category, location, root cause (W60.7)
- Integration with W2 (standard PO — this is the expedited alternative), W3 (goods receipt), W7 (AP matching), W21 (capex — if emergency need is actually capex, route to W21 expedited path), W25 (petty cash — for amounts ≤ PHP 50K), W47 (facility emergency repair), W48 (IT emergency equipment)

### Staffing Implication
- No incremental headcount. Emergency procurement is absorbed by existing Buyers, Store Managers, and AP Clerks.
- The monthly review by Controller adds ~1 hour/month — absorbed.

---



---

## W62. Vendor Contract Lifecycle (Non-PO Contracts)

| Field | Detail |
|---|---|
| **Trigger** | New service vendor engagement, contract renewal, or contract modification |
| **Frequency** | ~100–200 active service contracts at any time (IT services, cleaning, security, pest control, elevator maintenance, waste disposal, equipment leases, carrier contracts, banking services, professional services) |
| **Volume** | Peaks during annual budget cycle (W26) when contracts are reviewed and renewed |
| **Owner** | Requesting Department Head |
| **Participants** | Dept. Head, Procurement/Buyer, Finance, Legal, Vendor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Department Head identifies need for vendor service contract (new vendor, renewal, or replacement); defines scope of work, service level requirements, and budget | Dept. Head | VP / C-Suite | 1–2 hours |
| 2 | Buyer or Dept. Head solicits quotations from 3 vendors (or 2 for specialized services); evaluates on: price, capability, references, compliance (business permits, tax compliance, insurance coverage) | Buyer / Dept. Head | Dept. Head | 2–4 hours |
| 3 | Legal reviews contract terms: liability, termination clause, data privacy (RA 10173 compliance for vendors handling personal data), intellectual property, dispute resolution | Legal | Legal Head | 1–2 hours/contract |
| 4 | Approval per tiered matrix: (a) annual value ≤ PHP 500K: Dept. Head + Finance Manager, (b) PHP 500K–2M: VP + CFO, (c) > PHP 2M: CEO | Approver | Approver | 15–30 min |
| 5 | System creates vendor contract record: vendor, contract type, scope, start/end dates, value, payment terms, SLA terms, auto-renewal flag, document attachments (signed contract, vendor permits, insurance certificates) | Buyer / Dept. Head | Dept. Head | 15–30 min |
| 6 | System alerts Dept. Head 90 days before contract expiry for renewal decision; alerts 30 days before vendor insurance or permit expiry within contract period | System | — | Automated |
| 7 | Monthly: Dept. Head reviews vendor service performance against SLA terms; documents issues; escalates to Buyer or Legal for resolution | Dept. Head | VP / C-Suite | 30 min/vendor/month |
| 8 | Contract renewal: Dept. Head decides to (a) renew at existing terms, (b) renegotiate (repeat steps 2–4), or (c) terminate and re-bid; system blocks vendor invoices after contract expiry if not renewed | Dept. Head | VP / C-Suite | Per contract |
| 9 | Contract termination: Dept. Head provides notice per contract terms; coordinates vendor exit (return of company property, data deletion per RA 10173, final payment); system closes contract record and blocks future invoices | Dept. Head / Legal | VP / C-Suite | 1–2 hours |

### System Touchpoints
- Vendor contract register with full lifecycle: Draft → Active → Renewal Pending → Renewed / Terminated (W62.5, 8–9)
- Contract document storage with expiry alerting for contract, vendor permits, and insurance certificates (W62.6)
- SLA tracking with performance documentation per review period (W62.7)
- Auto-renewal management: system flags auto-renewal contracts 90 days before renewal for Dept. Head decision (W62.6)
- Invoice blocking after contract expiry (W62.8)
- Integration with W2c (blanket/contract POs for merchandise vendors), W7c (non-PO invoice processing), W36 (vendor onboarding), W44 (vendor performance review — service vendors included in annual review), W59 (insurance tracking for vendor insurance certificates)

### Staffing Implication
- No incremental headcount. Contract management is distributed across Department Heads as part of their operational responsibility. Legal reviews add ~1–2 hours/contract — absorbed within Legal team.

### W62b. 3PL / Delivery Partner Onboarding & Offboarding

| Field | Detail |
|---|---|
| **Trigger** | New delivery partner identified (new service area, capacity expansion, carrier diversification); or existing partner termination (performance failure, contract expiry, business exit) |
| **Frequency** | ~5–10 new partner evaluations/year; ~2–3 offboardings/year |
| **Volume** | Active partners: ~5–10 delivery partners (Lalamove, Transportify, own fleet surrogates, regional carriers, inter-island shipping lines) |
| **Owner** | Fleet Manager / DC Dispatch Supervisor |
| **Participants** | Fleet Manager, DC Dispatch, IT (API integration), Finance, Legal |

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Fleet Manager or DC Dispatch identifies need for new delivery partner: coverage gap, capacity constraint, cost benchmarking, or service quality issue with existing partner | Fleet Manager | Supply Chain Manager | 30 min |
| 2 | Fleet Manager solicits proposals from 2–3 candidate partners; evaluates on: delivery coverage (zones, islands), rate card per zone/weight/tier, SLA terms (on-time %, damage rate), API integration capability (order creation, tracking, proof of delivery), insurance coverage, business permits, tax compliance | Fleet Manager | Supply Chain Manager | 4–8 hours |
| 3 | IT evaluates API integration feasibility: order creation, real-time tracking, proof of delivery capture, webhook/callback for status updates; estimates integration timeline and cost | IT Team | CIO | 4 hours |
| 4 | Legal reviews contract terms: liability for lost/damaged goods, data privacy (RA 10173 — delivery partner may access customer name, phone, address), insurance requirements, termination clause | Legal | Legal Head | 1–2 hours |
| 5 | Approval per W62 tiered matrix (carrier contracts typically annual value ≤ PHP 2M → VP + CFO; > PHP 2M → CEO) | Approver | Approver | 15–30 min |
| 6 | IT configures API integration in staging environment; conducts integration testing with carrier test environment; validates order creation, status callbacks, and proof of delivery flow; Fleet Manager and DC Dispatch conduct pilot with limited order volume for 1–2 weeks | IT Team / Fleet Manager | CIO | 1–2 weeks |
| 7 | Go-live: IT activates API integration in production; DC Dispatch adds partner to carrier selection logic; system routes orders to new partner per configured zones and rates | IT Team / Fleet Manager | Supply Chain Manager | 1 day |
| 8 | Monthly: Fleet Manager monitors new partner performance per W19.7 3PL management dashboard (on-time %, damage rate, cost per delivery, customer complaint rate); underperformance escalated per W44 vendor scorecard methodology | Fleet Manager | Supply Chain Manager | 30 min/month |
| 9 | **Offboarding**: if partner termination required (performance, contract expiry, or business decision) — Fleet Manager coordinates with DC Dispatch to redirect order volume to alternative partners; IT deactivates API integration; system removes partner from carrier selection; Finance settles outstanding carrier invoices; Legal confirms data deletion per RA 10173 (partner must delete customer data collected during service); system archives partner record with termination date, reason, and performance history | Fleet Manager / IT / Finance / Legal | Supply Chain Manager | 1–2 weeks |

### System Touchpoints (3PL Partners)
- Carrier master record with rate cards per zone/weight/tier, SLA terms, API credentials, insurance details, and integration status (W62b.2, W62b.7)
- API integration: order creation, real-time tracking, status callbacks, proof of delivery capture (W62b.3, W62b.6)
- Carrier selection logic: automated carrier assignment by delivery zone, package weight, and cost (W62b.7)
- Pilot order routing and monitoring dashboard (W62b.6)
- Performance monitoring integrated into W19 3PL management dashboard and W44 vendor scorecard (W62b.8)
- Partner deactivation: API disconnect, carrier removal, data deletion confirmation (W62b.9)
- Carrier rate card maintenance: Fleet Manager receives rate change notification from carrier (quarterly or annual update); enters updated rate card per zone/weight/tier in carrier master record; Finance Manager approves rate card changes before activation (validates against contracted rates and budget impact); system stores rate card history with effective dates for audit trail; auto-calculated delivery fees in W5d and W19 use the currently active rate card; rate card changes effective on configured date — orders already in transit use the rate card active at time of order creation (W62b)
- Integration with W19 (home delivery), W52 (fleet), W44 (vendor scorecard), W62 (non-PO contracts)

### Staffing Implication (3PL Partners)
- **Fleet Manager**: absorbs 3PL partner management within existing role; ~5–10 evaluations/year × 4–8 hours = ~20–80 hours/year; ~30 min/month ongoing monitoring per partner.
- **IT**: API integration setup ~1–2 weeks per new partner; absorbed within existing IT team.
- No incremental headcount.

---



## W88. Return to Vendor (RTV) Processing

| Field | Detail |
|---|---|
| **Trigger** | Defective goods identified at DC or store; wrong items received; overage discovered; vendor-authorized return; or quality hold escalation (W3 AQL inspection) |
| **Frequency** | ~200–300 RTV shipments/month (~2–3% of inbound volume) |
| **Volume** | Avg 5–15 lines per RTV shipment; consolidated by vendor at DC |
| **Owner** | Buyer |
| **Participants** | Buyer, DC Receiving Clerk, Store Receiving Clerk, AP Clerk, AP Supervisor, Category Manager |

### Background

PUR-012 (Return to Vendor) is a Must Have requirement. RTV is currently mentioned as sub-steps W3.6a–b within warehouse receiving, but RTV is a cross-functional process spanning procurement, warehouse, store operations, and finance. Defective, wrong, or overage items must be identified, documented, authorized, physically returned to the vendor (or vendor-authorized disposal), and financially settled (credit memo or replacement). Without a dedicated workflow, RTV decisions are ad-hoc, leading to delayed vendor credits, unresolved inventory, and write-offs.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Identification**: (a) DC Receiving Clerk identifies defective/wrong items during goods receipt inspection (W3 AQL); (b) Store Receiving Clerk identifies issues during DSD receiving (W18) or DC delivery receipt; (c) Store Associate or Stock Associate discovers damaged/defective stock on shelf or in backroom; (d) AP Clerk identifies overage during 3-way match (W7 — vendor invoice quantity exceeds PO + GR); (e) Quality hold escalation from W3 AQL inspection (system blocks inventory and flags for RTV evaluation) | Receiving Clerk / Store Associate / AP Clerk | Buyer | 10 min/case |
| 2 | **Root cause classification**: Initiator classifies the issue: (a) defective/quality failure (vendor manufacturing defect, packaging damage in transit from vendor), (b) wrong item shipped (SKU mismatch vs. PO), (c) overage (vendor shipped more than PO quantity), (d) damaged in transit to DC (carrier damage — see W19.12b for carrier vs. vendor liability), (e) recall-related return (W29), (f) consignment return (W23.10), (g) warranty return (W33.6) | Initiator / Buyer | Buyer | 5 min/case |
| 3 | **Quarantine**: System moves identified items to "RTV Quarantine" inventory status (not available for sale, not available for allocation); physical items moved to designated quarantine area at DC or store backroom | Receiving Clerk / Stock Associate | DC Supervisor / Store Manager | 10 min/case |
| 4 | **Buyer review and authorization**: Buyer reviews RTV request with supporting evidence (photos, inspection report, PO vs. GR discrepancy); determines return action: (a) **Return to vendor** — vendor must physically take back goods and issue credit or replacement, (b) **Vendor-authorized disposal** — vendor authorizes BuildRight to dispose/destroy goods and issues credit memo (saves return freight cost for low-value items), (c) **Vendor-authorized markdown** — vendor agrees to partial credit; BuildRight sells at reduced price per W93 markdown process, (d) **No vendor liability** — damage caused by BuildRight handling (in-transit between DC and store, or in-store damage); disposition per W91 damaged goods process; no vendor credit sought | Buyer | Category Manager | 15 min/case |
| 5 | **Vendor notification**: Buyer contacts vendor (email or vendor portal W36.9) with RTV request: original PO reference, GR reference, item details, quantity, defect description, photos, and requested resolution (credit memo, replacement, or disposal authorization); for blanket/contract PO vendors (W2c), checks contract terms for RTV provisions and return shipping responsibility | Buyer | — | 15 min/case |
| 6 | **Vendor credit memo or replacement**: (a) If vendor agrees to credit: Buyer obtains vendor credit memo reference; (b) If vendor agrees to replacement: Buyer creates replacement PO with reference to original PO and RTV; (c) If vendor disputes: Buyer escalates to Category Manager for negotiation; unresolved disputes > 30 days escalated to VP Merchandising | Buyer / Category Manager | VP Merchandising | 30 min/dispute |
| 7 | **Physical return logistics** (if vendor requires physical return): (a) **DC-initiated**: DC consolidates RTV items by vendor; DC creates outbound shipment; ships via own fleet (W52) or 3PL carrier; (b) **Store-initiated**: Store sends RTV items to assigned DC via next scheduled DC→Store truck backhaul (W22); DC consolidates with other RTV items for same vendor before shipping; (c) **Vendor pickup**: Some vendors (especially local DSD vendors) pick up RTV items directly from store or DC by arrangement | DC Receiving Clerk / Store Receiving Clerk | DC Supervisor / Store Manager | 30 min/consolidated shipment |
| 8 | **Financial settlement**: (a) AP Clerk receives vendor credit memo (from Buyer); posts credit memo against original PO/invoice; system reduces vendor payable and posts GL entry (Dr. AP / Cr. COGS or Inventory); (b) If replacement PO: AP matches replacement invoice against replacement PO and GR per standard W7 3-way match; (c) If vendor-authorized disposal: AP posts credit memo and inventory write-off simultaneously; system removes items from RTV quarantine and posts disposal (Dr. AP / Cr. Inventory — at WAC value) | AP Clerk | AP Supervisor | 10 min/credit memo |
| 9 | **Aging and escalation**: System tracks RTV items in quarantine with aging buckets (0–15, 16–30, 31–60, 60+ days); weekly: Buyer reviews RTV aging report; items > 15 days without vendor response: follow-up call/email; items > 30 days: escalated to Category Manager; items > 60 days: escalated to VP Merchandising with recommendation to auto-dispose and write-off; items > 90 days: auto-write-off per W92 with Category Manager approval | Buyer / Category Manager | VP Merchandising | 30 min/week |
| 10 | **RTV analytics**: Monthly: Category Manager and Buyer review RTV report by vendor — RTV count, RTV value, average resolution time, root cause distribution (defective vs. wrong item vs. overage vs. carrier damage); feeds into W44 vendor performance scorecard as quality and accuracy metric; vendors with RTV rate > 5% of total PO lines flagged for vendor improvement plan or vendor exit per W68 | Category Manager / Buyer | VP Merchandising | 1 hour/month |

### System Touchpoints
- RTV quarantine inventory status: items blocked from sale and allocation while in quarantine (W88.3)
- RTV request creation linked to original PO and GR with defect evidence (photos, inspection report) (W88.4)
- Vendor portal RTV notification: vendor receives return request with documentation and can approve/reject/authorize disposal (W88.5)
- Vendor credit memo matching to original PO/invoice with GL posting (W88.8)
- Replacement PO creation linked to original PO with RTV reference (W88.6)
- RTV aging report with vendor-level drill-down and escalation triggers (W88.9)
- RTV analytics dashboard: RTV rate by vendor, root cause distribution, resolution time, value impact (W88.10)
- Integration with W3 (DC receiving — AQL inspection triggers RTV), W7 (AP — credit memo processing), W12 (returns — customer-returned defective items may be RTV'd), W18 (DSD — receiving discrepancies), W22 (store-to-DC backhaul for RTV consolidation), W23 (consignment returns), W29 (recall-related RTV), W33 (warranty RTV), W44 (vendor scorecard — RTV rate as quality metric), W52 (fleet — physical return logistics), W62 (vendor contract — RTV provisions), W91 (damaged goods disposition — no-vendor-liability cases), W92 (inventory adjustment — write-off for unresolved RTV)

### Staffing Implication
- **Buyers**: ~200–300 RTV cases/month ÷ 10–12 buyers = ~20–25 cases/buyer/month × ~45 min each = ~15–19 hours/buyer/month. Absorbed within existing buying workload.
- **DC Receiving Clerks**: RTV consolidation adds ~1–2 hours/week for staging and shipping returns. Absorbed.
- **AP Clerks**: ~200–300 credit memos/month adds ~1–2 hours/week. Absorbed within existing AP team.
- **No incremental headcount.**

---



---


## W110. Supplier Quality & CAPA (Corrective and Preventive Action)

| Field | Detail |
|---|---|
| **Trigger** | Quality failure at DC receiving (W3 AQL inspection failure); customer complaint about product quality (W41); product recall (W29); warranty claim spike (W33); or periodic quality trend review |
| **Frequency** | ~20–30 CAPA cases/month (from AQL rejects, customer complaints, and warranty analysis); quarterly quality trend review |
| **Volume** | ~200–300 quality failures/month from DC AQL inspection (W3); ~600–900 customer quality complaints/month (30% of W41 complaint volume); ~50–100 warranty claims/month potentially quality-related (W33) |
| **Owner** | Buyer (vendor communication); Category Manager (escalation); Quality Coordinator (if dedicated role) |
| **Participants** | Buyer, Category Manager, DC Receiving Supervisor, Quality Checker, VP Merchandising, Customer Service Manager |

### Background

W3 covers quality inspection at DC receiving with AQL sampling. W44 covers vendor scorecards with quality reject rate as a metric. W88 handles RTV processing for defective items. However, there is no systematic workflow for investigating the root cause of quality failures, implementing corrective and preventive actions (CAPA) with the vendor, tracking CAPA effectiveness, and feeding quality trends back into vendor management and assortment decisions. Without CAPA, quality failures recur, vendor scorecards penalize but don't improve performance, and the same defective products reach customers repeatedly.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **CAPA case creation**: System auto-generates CAPA case when: (a) AQL inspection fails at DC receiving (W3 — entire lot rejected or defect rate exceeds AQL), (b) customer quality complaint categorized as product defect (W41), (c) product recall initiated (W29 — systemic quality failure), (d) warranty claim rate for a SKU exceeds threshold (> 2% of units sold), (e) RTV rate for a vendor exceeds threshold (> 5% of PO lines per W88.10); alternatively, Buyer or Category Manager manually creates CAPA case for observed quality trends | System / Buyer / Category Manager | Category Manager | 5 min/case |
| 2 | **Case classification and severity**: Buyer classifies CAPA case: (a) **Critical** — safety hazard (electrical defect, structural failure, chemical hazard), regulatory non-compliance, or widespread customer impact; requires immediate response; (b) **Major** — functional defect affecting usability, high return/complaint rate (> 5%), or significant financial impact (> PHP 100,000); requires vendor corrective action; (c) **Minor** — cosmetic defect, packaging quality, labeling errors; monitored for trend but may not require formal vendor CAPA | Buyer | Category Manager | 10 min/case |
| 3 | **Immediate containment**: (a) For Critical/Major: system places quality hold on all on-hand inventory of affected SKU across all locations (blocked from sale and allocation pending investigation); (b) system blocks pending POs for the SKU from being confirmed (Buyer reviews); (c) if product already sold: Buyer coordinates with W29 recall process for consumer notification (Critical only); (d) DC Supervisor quarantines affected inventory in QC hold area per W3 quality hold process | Buyer / DC Supervisor | Category Manager | 1 hour/case (Critical); 30 min (Major) |
| 4 | **Root cause investigation**: (a) Buyer collects evidence: AQL inspection report, defect photos, customer complaint details, warranty claim photos, lot/batch numbers, manufacturing dates; (b) Buyer contacts vendor with detailed quality failure report: defect description, affected lot/batch, quantity impacted, severity, and request for root cause analysis; (c) vendor conducts root cause investigation (typically 5–15 business days); (d) for Critical cases: Buyer may request on-site vendor factory visit or independent third-party inspection | Buyer | Category Manager | 2–4 hours/case |
| 5 | **Corrective action plan**: Based on root cause findings, Buyer and vendor agree on corrective action: (a) **Process change** — vendor modifies manufacturing process, adds quality checkpoint, changes raw material supplier; (b) **Design change** — product specification modified to eliminate defect mode; (c) **Packaging change** — improved packaging to prevent transit damage; (d) **Batch replacement** — vendor replaces entire affected batch at vendor cost; (e) **Training** — vendor trains production staff on identified gap; Buyer documents agreed corrective actions with specific deliverables, responsible party, and completion deadline in CAPA case | Buyer / Vendor | Category Manager | 1–2 hours/case |
| 6 | **Preventive action**: Buyer identifies systemic preventive measures to avoid recurrence across similar products or vendors: (a) update AQL inspection checklist for the category to catch similar defects (W3); (b) revise vendor onboarding quality requirements for new vendors in the category (W36); (c) update item specification or acceptance criteria in item master (MDM-002); (d) communicate learnings to other Buyers handling similar categories | Buyer | Category Manager | 30 min/case |
| 7 | **Verification and closure**: (a) After corrective action deadline: Buyer verifies vendor implementation — request evidence (photos, updated process documents, test results); (b) for process/design changes: next 3 shipments inspected at tightened AQL level (Level III per ANSI Z1.4) to verify improvement; (c) if quality improvement confirmed: Buyer closes CAPA case with effectiveness verification notes; (d) if quality not improved: Buyer escalates to Category Manager for vendor improvement plan per W44 Warning/Probation/Termination tiers | Buyer | Category Manager | 30 min/case |
| 8 | **Monthly CAPA dashboard**: Buyer generates monthly CAPA dashboard: (a) open CAPA cases by vendor, category, and severity; (b) average time to resolution by severity; (c) corrective action effectiveness rate (cases closed without recurrence ÷ total closed); (d) recurring quality issues (same defect mode from same vendor); (e) vendors with most open/past-due CAPA cases; dashboard shared with Category Managers and VP Merchandising | Buyer | VP Merchandising | 1 hour/month |
| 9 | **Quarterly quality trend review**: Category Manager and VP Merchandising review quality trends quarterly: (a) quality reject rate trend by vendor and category, (b) customer complaint rate related to product quality, (c) CAPA case volume trend, (d) vendors with chronic quality issues (3+ CAPA cases in 12 months), (e) quality-driven assortment decisions — should BuildRight exit vendors with persistent quality failures?; feeds into W44 vendor scorecard and W1 assortment review | Category Manager | VP Merchandising | 2 hours/quarter |

### System Touchpoints
- CAPA case auto-generation from AQL failures, customer complaints, warranty claims, and RTV rate thresholds (W110.1)
- Case classification with severity levels triggering appropriate containment actions (W110.2–3)
- Quality hold on affected inventory across all locations with sales blocking (W110.3)
- Root cause documentation with evidence attachment (photos, inspection reports, vendor communications) (W110.4)
- Corrective action plan with deliverables, responsible party, and deadline tracking (W110.5)
- Verification workflow with tightened inspection for post-CAPA shipments (W110.7)
- Monthly CAPA dashboard with case aging, effectiveness rate, and vendor ranking (W110.8)
- Integration with W1 (assortment — quality-driven vendor exit), W3 (AQL inspection — source of CAPA triggers and tightened inspection post-CAPA), W29 (product recall — Critical CAPA escalation), W33 (warranty — quality-related claims), W36 (vendor onboarding — quality requirements from CAPA learnings), W41 (customer complaints — product quality complaints feed CAPA), W44 (vendor scorecard — CAPA history as quality metric), W88 (RTV — CAPA from high RTV rate), W91 (damaged goods — disposition during containment)

### Staffing Implication
- **Buyers**: ~20–30 CAPA cases/month ÷ 10–12 buyers = ~2–3 cases/buyer/month × ~3 hours each = ~6–9 hours/buyer/month. This is a core part of vendor management. Absorbed.
- **Category Managers**: 2 hours/quarter for trend review + 30 min/escalation case. Absorbed.
- **No incremental headcount.**

---

## W115. Supplier Diversity & MSME Development Program

| Field | Detail |
|---|---|
| **Trigger** | Annual supplier diversity review; or ad-hoc triggered by corporate social responsibility (CSR) initiative, LGU requirement, or MSME vendor opportunity identification |
| **Frequency** | Annual program review and target setting; quarterly progress tracking; continuous MSME vendor identification |
| **Volume** | ~800–1,000 active vendors; target: ≥ 20% MSME (Micro, Small, Medium Enterprise) vendor participation by spend or count within 3 years |
| **Owner** | Buyer (MSME identification and onboarding); VP Merchandising (program governance) |
| **Participants** | Buyer, Category Manager, VP Merchandising, Finance, Legal, CSR Coordinator |

### Background

The Philippine government actively promotes MSME development through the Magna Carta for MSMEs (RA 9501) and the Go Negosyo Act (RA 10644). Large enterprises are encouraged to source from MSMEs, and government procurement (W78) has MSME participation requirements. BuildRight sources 60% of goods from local Philippine vendors — many of which may qualify as MSMEs. However, there is no formal program to track MSME vendor participation, identify opportunities to onboard MSME suppliers, or provide development support to help MSMEs meet BuildRight's quality and scale requirements. This workflow creates that governance framework, supporting PUR-003 (vendor management) and contributing to corporate social responsibility objectives.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **MSME vendor classification**: System classifies existing vendors as MSME or non-MSME based on DTI/SEC registration and annual revenue: (a) Micro: < PHP 3M annual revenue, (b) Small: PHP 3M–15M, (c) Medium: PHP 15M–100M, (d) Large: > PHP 100M; classification captured in vendor master during onboarding (W36) or updated annually from BIR tax filing data; system generates MSME vendor register with: vendor name, category, MSME size classification, annual spend, and year-first-onboarded | System / Buyer | VP Merchandising | Automated (classification) + 2 hours/year (verification) |
| 2 | **Annual diversity target setting**: VP Merchandising and Category Managers set annual MSME sourcing targets by category: (a) overall target: ≥ 20% of active vendor count classified as MSME within 3 years, (b) category-specific targets based on MSME availability in the category (e.g., higher MSME % in home décor, garden, hardware where local artisans and manufacturers are prevalent; lower in power tools, appliances where scale requirements favor large manufacturers), (c) geographic diversity target: ensure MSME vendors are distributed across regions (Mindanao, Visayas, Luzon) not concentrated in one region | VP Merchandising | CEO | Annual (4 hours) |
| 3 | **MSME vendor identification**: Buyer actively identifies potential MSME vendors through: (a) trade shows and MSME fairs (DTI-organized events, regional trade fairs), (b) LGU and DTI referrals (DTI has MSME directories per region), (c) industry associations (Chamber of Commerce, sector-specific associations), (d) existing vendor referrals (current vendors may know MSME sub-suppliers), (e) competitor and market scanning for local manufacturers not yet in BuildRight's vendor base | Buyer | Category Manager | Ongoing (~2 hours/week across all buyers) |
| 4 | **MSME vendor evaluation**: Buyer evaluates MSME vendor candidates with modified criteria vs. large vendor onboarding (W36): (a) product quality — sample review (standard W36.4), (b) pricing competitiveness — may be slightly higher than large vendors but justified by uniqueness or local sourcing value, (c) production capacity — must meet minimum order quantity for BuildRight's needs (may be lower than standard MOQ to accommodate MSME scale), (d) delivery capability — must deliver to assigned DC or store within agreed lead time, (e) financial stability — review BIR registration and business permit (standard W36.2–3), (f) scalability potential — can the MSME grow with BuildRight's increasing demand? | Buyer | Category Manager | Per W36 (~4–6 hours/vendor) |
| 5 | **MSME onboarding support**: For MSME vendors that meet quality and capacity requirements but need operational support: (a) Buyer provides guidance on BuildRight's packaging, labeling, and barcode requirements; (b) Category Manager may approve a trial period with smaller initial orders and more frequent quality checks (W3 tightened AQL); (c) Finance may offer shorter payment terms (Net 15 instead of Net 30) to support MSME cash flow — requires Finance Manager approval; (d) IT provides vendor portal access and training for order management (W36.9) | Buyer / Category Manager / Finance | VP Merchandising | 2–4 hours/vendor |
| 6 | **Quarterly progress tracking**: Buyer generates quarterly MSME sourcing report: (a) total MSME vendor count and % of active vendors, (b) total MSME spend and % of total COGS, (c) new MSME vendors onboarded during quarter, (d) MSME vendor geographic distribution, (e) MSME vendor performance summary (quality, delivery, pricing vs. non-MSME benchmarks), (f) progress against annual targets | Buyer | VP Merchandising | 1 hour/quarter |
| 7 | **Annual program review**: VP Merchandising and CEO review annual MSME program performance: (a) year-over-year MSME vendor count and spend trend, (b) MSME vendor retention rate (how many MSME vendors remain active after first year?), (c) MSME vendor success stories and challenges, (d) set next year's targets, (e) evaluate program's contribution to BuildRight's CSR objectives and community impact (especially in Mindanao and Visayas regions) | VP Merchandising | CEO | 2 hours/year |
| 8 | **Government reporting**: If required for government procurement eligibility (W78) or LGU permit compliance (W54): Finance compiles MSME sourcing data for regulatory submissions; CSR Coordinator prepares MSME development program summary for annual CSR report | Finance / CSR Coordinator | VP Legal & Compliance | Annual (4 hours) |

### System Touchpoints
- MSME classification field in vendor master with size category (Micro, Small, Medium, Large) and annual revenue band (W115.1)
- MSME vendor register with spend, category, region, and year-onboarded (W115.1)
- Annual MSME sourcing target configuration by category and region (W115.2)
- Quarterly MSME sourcing report with count, spend, geographic, and performance metrics (W115.6)
- Integration with W36 (vendor onboarding — MSME classification at onboarding), W44 (vendor scorecard — MSME vs. non-MSME performance comparison), W62 (vendor contracts — MSME-specific payment terms), W78 (government procurement — MSME participation reporting), W26 (annual budget — MSME spend target)

### Staffing Implication
- **Buyers**: MSME identification adds ~2 hours/week total across all buyers.
- **No incremental headcount.**

---

## W136. Indirect / Non-Merchandise Procurement

| Field | Detail |
|---|---|
| **Trigger** | Requisition for supplies, services, or equipment not for resale |
| **Frequency** | Ongoing |
| **Volume** | ~300–400 indirect POs/month (supplies, fixtures, marketing materials) |
| **Owner** | Indirect Procurement Manager |
| **Participants** | Requesting Dept, Buyer, Vendor, Finance (AP) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Requisition: Dept user creates purchase request (PR) in ERP | Requestor | Dept Head | 15 min |
| 2 | Sourcing / Bidding: Buyer obtains 3 quotes for non-contract items | Buyer | Procurement Mgr | 3–5 days |
| 3 | Vendor Selection: Evaluate quotes based on TCO (Total Cost of Ownership) | Buyer | Procurement Mgr | 1 day |
| 4 | PO Creation: Convert approved PR to PO and transmit to vendor | Buyer | Procurement Mgr | 15 min |
| 5 | Receipt & Verification: Requestor confirms receipt of goods or service completion | Requestor | Dept Head | 30 min |
| 6 | Invoice Processing: Finance matches Invoice to PO and Receipt (3-way match) | AP Specialist | AP Supervisor | 15 min |

---

## W150. Product Quality Testing & Certification

| Field | Detail |
|---|---|
| **Trigger** | New product onboarding (W1); new vendor onboarding (W36); or scheduled periodic audit |
| **Frequency** | Ad-hoc (new items); Annual (periodic) |
| **Volume** | ~500–1,000 items tested/year (primarily private label and structural materials) |
| **Owner** | Quality Manager |
| **Participants** | Category Manager, Vendor, external testing lab (e.g., TUV, SGS), DC Receiving |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Sample Submission**: Vendor provides physical samples of the product for testing | Vendor | Category Mgr | 1 day |
| 2 | **Documentation Review**: Quality Manager verifies mandatory Philippine certifications (PS Mark for local, ICC for imported regulated items) | Quality Mgr | Quality Mgr | 1 hour |
| 3 | **Internal Testing**: Basic "Fit & Finish" testing at HQ or DC lab (e.g., measuring tile thickness, weighing cement bags) | Quality Mgr | Category Mgr | 2 hours |
| 4 | **External Lab Testing**: Send samples to accredited 3rd-party lab for structural/chemical testing (e.g., steel tensile strength, paint lead content) | Quality Mgr | — | 1–2 weeks |
| 5 | **Decision**: (a) Pass: System flags SKU as "QC Approved"; (b) Fail: Item rejected; Vendor must remediate or SKU is blocked from sale | Quality Mgr | VP Merch | 30 min |
| 6 | **Periodic Audit**: Random samples pulled from DC stock (W3) and sent for re-testing to ensure consistent quality | Quality Mgr | Quality Mgr | Ongoing |

### System Touchpoints
- "QC Approved" status flag in Item Master
- Storage of digital certificates and lab reports linked to the SKU
- Automated block on PO creation (W2) for items with expired or failed QC status
- Integration with W3 (Receiving) for sample pulling during DC arrival

---

### System Touchpoints (Procurement Extensions)
- Requisition portal for all employees
- Automated "3-quote" enforcement for indirect spend > threshold
- Service Entry Sheet (SES) for non-physical services (consulting, cleaning)
- Integration with Fixed Assets for equipment procurement (W21/W39)
- Budget check (Commitment accounting) at Requisition stage

---

---

## W155. Vendor Strategic Collaboration & Joint Business Planning (JBP)

| Field | Detail |
|---|---|
| **Trigger** | Annual planning cycle with "Top 20" strategic vendors |
| **Frequency** | Annual (with quarterly progress reviews) |
| **Volume** | Covers 20 key vendors (~45% of COGS) |
| **Owner** | VP for Merchandising |
| **Participants** | Category Managers, Buyers, Vendor Executives, Supply Chain Planners |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Performance Review**: Jointly review prior year: fill rates (W44), margin, growth, and rebate achievement (W27) | Buyer / Vendor | Category Mgr | 4 hours |
| 2 | **Growth Targets**: Set consensus growth targets and market share goals for the next 12 months | Category Mgr | VP Merch | 2 hours |
| 3 | **Supply Chain Alignment**: Share long-term demand forecasts (W31) to help vendor plan production capacity | Demand Planner | — | 1 hour |
| 4 | **JBP Document**: Sign joint plan covering exclusive SKUs, marketing co-op (W153), and logistics efficiency | VP Merch | CEO | 1 week |

---

## W160. Private Label Factory Audit & Social Compliance

| Field | Detail |
|---|---|
| **Trigger** | Onboarding new private label vendor (W129); or annual compliance cycle |
| **Frequency** | Annual per factory |
| **Volume** | ~30–50 factories audited annually |
| **Owner** | Quality & Compliance Manager |
| **Participants** | Buyer, Legal, External Auditor, Vendor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Self-Assessment**: Vendor submits social compliance questionnaire (labor practices, safety, environmental) | Vendor | Quality Mgr | 1 week |
| 2 | **On-site Audit**: Internal or 3rd-party audit (SGS/TUV) of factory floor, dormitories, and payroll records | External Auditor | Quality Mgr | 1–2 days |
| 3 | **CAPA**: If violations found, vendor must submit and execute Corrective Action Plan (W110) | Vendor | Quality Mgr | 30 days |
| 4 | **Certification**: Issue "BuildRight Approved Factory" status in ERP; linked to W2 PO creation | Quality Mgr | VP Merch | 1 day |

---

## W161. Vendor Price Protection & Market Markdown Claims

| Field | Detail |
|---|---|
| **Trigger** | Retail price reduction (W40, W93) or competitive price match (W61) impacting stocking items |
| **Frequency** | Monthly or per major price event |
| **Volume** | Covers all SKU categories with price protection agreements |
| **Owner** | Pricing Analyst |
| **Participants** | Buyer, Category Manager, Vendor, Finance (AR/AP) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Eligibility Review**: Identify SKUs with active price protection clauses in vendor contracts (W62) upon retail price change | Pricing Analyst | Category Manager | 1 hour |
| 2 | **Stock-on-Hand Capture**: System takes a snapshot of group-wide inventory (stores + DCs) at the moment of price change | System | — | Real-time |
| 3 | **Claim Calculation**: Calculate claim amount = (Old Retail - New Retail) × Inventory Count; or (Old Cost - New Cost) × Inventory Count, depending on contract | Pricing Analyst | Category Manager | 30 min |
| 4 | **Vendor Validation**: Transmit claim report to vendor for verification and approval; negotiate discrepancies | Buyer | Category Manager | 3-5 days |
| 5 | **Credit Note Issuance**: Vendor issues Credit Memo to offset future payables; or system auto-deducts from next PO payment if pre-authorized | Vendor / Finance | Buyer | 5-10 days |
| 6 | **Margin Recovery**: Update product costing (W85) to reflect the recovered margin; update P&L for category (W102) | Finance | Category Manager | 1 hour |

---

## W244. Vendor Invoice Dispute & Discrepancy Resolution

| Field | Detail |
|---|---|
| **Trigger** | 3-Way Match fails (discrepancy between PO, GR, or Vendor Invoice in price or quantity) in W7 |
| **Frequency** | Weekly |
| **Volume** | ~50–100 invoice disputes per month |
| **Owner** | AP Supervisor |
| **Participants** | AP Clerk, Buyer (Merchandising), Vendor Account Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Discrepancy Identification**: System flags 3-way match failure (W7 step 3). AP Clerk isolates invoice in "Disputed" status. | AP Clerk | — | 15 min |
| 2 | **Categorization**: System classifies discrepancy: (a) Price variance (invoice price > PO price), or (b) Quantity variance (invoice quantity > GR quantity). | System | — | Automated |
| 3 | **Internal Review**: AP Clerk routes price variance to the Buyer for review. Buyer either: (a) Approves invoice (PO was outdated, updates contract price books), or (b) Rejects price, generating a Debit Note request in ERP. | AP Clerk / Buyer | Category Manager | 1 day |
| 4 | **Quantity Reconciliation**: For quantity variance, AP Clerk cross-references GR slip and DC warehouse log. If short-shipped, routes to Vendor for confirmation. | AP Clerk | AP Supervisor | 2 hours |
| 5 | **Dispute Communication**: Buyer/AP Supervisor sends automated Dispute Notice with supporting system logs to the vendor via the Vendor Portal (W36). | AP Supervisor | — | 10 min |
| 6 | **Settlement**: Vendor accepts debit note or issues corrected invoice/Credit Note. AP Clerk posts Credit/Debit Note in ERP to match the variance and approves invoice for payment run. | AP Clerk / Vendor | AP Supervisor | 2–5 days |

### System Touchpoints
- Automated 3-way match variance flags (price/qty)
- Dispute workflow router (AP ↔ Buyer ↔ Vendor)
- Debit/Credit Note generation and automated GL posting
- Integration with W7 (AP processing) and W36 (Vendor Portal)

---

## W245. Vendor Performance Chargebacks & Penalties Management

| Field | Detail |
|---|---|
| **Trigger** | Incomplete shipment, late delivery, or poor product quality at GR (W3/W18) resulting in scorecard failure (W44) |
| **Frequency** | Ongoing |
| **Volume** | ~100–150 chargeback events/month across all DCs |
| **Owner** | Supplier Compliance Manager |
| **Participants** | DC Receiving Supervisor, Category Manager, Vendor Compliance, AP Specialist |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Log Discrepancy**: DC Receiving Supervisor logs delivery failure at GR (shortage, damage, packaging non-compliance) or late arrival (> 2 hours past SLA). | DC Supervisor | DC Manager | 15 min |
| 2 | **Fines Engine Execution**: System references Supplier Compliance Agreement (W62) and auto-calculates fee/penalty: (a) Fill rate failure: 2% of unfulfilled value; (b) Late delivery: PHP 5,000 flat penalty; (c) Packaging non-compliance: PHP 2,500 penalty. | System | — | Automated |
| 3 | **Notification**: System triggers a "Compliance Infraction Report" with photographs and receiving logs, sending it to the vendor via the Vendor Portal (W36) with copy to the Category Manager. | Supplier Compliance | — | 10 min |
| 4 | **Dispute Window**: Vendor has 5 business days to dispute infraction by uploading carrier proof or force majeure evidence; compliance manager reviews and makes final ruling. | Vendor / Compliance Mgr | Supplier Compliance Mgr | 5 days |
| 5 | **Chargeback Posting**: If infraction upheld, system automatically generates an AR invoice / AP Debit Note (Dr. Vendor Chargeback Receivable / Cr. Procurement Penalty Income) in the vendor's ledger. | System | — | Automated |
| 6 | **Deduction Reconciliation**: At next AP payment cycle (W7), matching engine auto-applies debit note as deduction against vendor's invoice payment, netting the settlement. | AP Specialist | AP Supervisor | 10 min |

### System Touchpoints
- Supplier compliance fine/penalty calculation engine linked to receiving logs and contracts
- Infraction workflow management dashboard with vendor portal linkage
- Automated Debit Note / AR invoice posting in General Ledger
- Auto-application of debit notes at payment cycle (W7)


