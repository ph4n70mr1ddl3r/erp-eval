# Compliance & Governance Workflows

> Loss prevention, business continuity, LGU permits, BIR audit, government procurement, grievance/whistleblower, and hazardous waste disposal.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W37. Loss Prevention & Exception Reporting](#loss-prevention-exception-reporting)
- [W49. Natural Disaster / Typhoon Business Continuity](#natural-disaster-typhoon-business-continuity)
- [W54. LGU Business Permit Renewal per Location](#lgu-business-permit-renewal-per-location)
- [W77. BIR Tax Audit Response](#bir-tax-audit-response)
- [W78. Government / Institutional Procurement Participation](#government-institutional-procurement-participation)
- [W79. Employee Grievance & Whistleblower Process](#employee-grievance-whistleblower-process)
- [W82. Hazardous Waste Disposal Tracking & DENR Compliance](#hazardous-waste-disposal-tracking-denr-compliance)
- [W95. External Audit Coordination & Support](#external-audit-coordination-support)
- [W114. Sustainability & Environmental Compliance Reporting](#sustainability--environmental-compliance-reporting)
- [W157. E-waste Collection & Circular Economy Operations](#e-waste-collection--circular-economy-operations)
- [W158. Business Continuity Drill & Disaster Recovery Testing](#business-continuity-drill--disaster-recovery-testing)
- [W167. Store & DC Recycling Program (Circular Economy)](#store--dc-recycling-program-circular-economy)
- [W185. Product Liability & Consumer Safety Incident Management](#product-liability--consumer-safety-incident-management)
- [W207. Store-Level Security Camera (CCTV) Audit & LP Integration](#store-level-security-camera-cctv-audit--lp-integration)
- [W209. Barangay & Local Community Relationship Management](#barangay--local-community-relationship-management)

---

## W37. Loss Prevention & Exception Reporting

| Field | Detail |
|---|---|
| **Trigger** | Daily exception report generation; or real-time alert triggered by POS exception |
| **Frequency** | Daily review; real-time alerts for high-severity exceptions |
| **Volume** | ~500–1,000 exception events/day chain-wide across all 200 stores |
| **Owner** | Loss Prevention Officer (LPO) |
| **Participants** | LPO, Store Manager, Regional Manager, Internal Audit, Cashier, Department Supervisor |

### Background

Shrinkage target: < 1.5% of sales (~PHP 75M/month at risk). Exception-based reporting identifies suspicious transaction patterns at POS and receiving dock that may indicate theft, fraud, or process errors.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System automatically monitors POS transactions in real-time and generates exception alerts for: (a) excessive voids/cancels per cashier, (b) high-value refunds without manager override, (c) manual price overrides, (d) sweet-hearting (repeated transactions with loyalty card of same employee or family), (e) excessive no-sale drawer opens, (f) post-void patterns, (g) high ratio of discount transactions | System | — | Real-time |
| 2 | System generates daily exception summary report per store: top exception categories, top cashiers by exception count, transaction drill-down capability | System | — | Automated (daily) |
| 3 | LPO reviews daily exception report; prioritizes investigation of high-risk patterns (e.g., one cashier with 5× average void rate) | LPO | Internal Audit | 1–2 hours/day |
| 4 | For flagged exceptions: LPO pulls transaction details, CCTV timestamps (cross-reference with security footage), and employee history | LPO | Internal Audit | 30 min/case |
| 5 | If investigation confirms irregularity: LPO documents findings; escalates to Regional Manager and Internal Audit for disciplinary action | LPO | Internal Audit | 1 hour/case |
| 6 | For receiving dock exceptions: system monitors GR short shipments, frequent damage claims from same vendor, and receiving patterns outside scheduled appointments | System | DC Manager | Automated |
| 7 | Monthly: LPO generates shrinkage report per store (inventory adjustment value ÷ sales); flags stores exceeding 1.5% threshold | LPO | Internal Audit | 2 hours/month |
| 8 | Monthly: LPO and Regional Manager review top shrinkage stores; develop action plans (additional training, CCTV repositioning, staffing adjustments) | LPO + Regional Manager | Internal Audit | 1 hour/month per high-shrinkage store |
| 9 | Quarterly: Internal Audit includes POS exception trends in audit findings; recommends system configuration changes (e.g., tighten void approval rules) | Internal Audit | CFO | Quarterly report |
| 10 | System tracks all investigation cases: status (open/investigating/closed), resolution, recovery amount, disciplinary action taken | System | — | Automated |

### System Touchpoints
- Real-time POS exception monitoring with configurable thresholds per exception type (W37.1)
- Daily exception summary report with drill-down to transaction level (W37.2)
- Transaction detail with CCTV timestamp cross-reference capability (W37.4)
- Receiving dock exception monitoring (W37.6)
- Shrinkage report per store with threshold alerting (W37.7)
- Investigation case management with status tracking (W37.10)
- Confirmed theft / inventory write-off process: documentation with supporting evidence, police report filing for theft, tiered approval per loss value, GL write-off posting, insurance claim integration, quarterly shrinkage reporting integration (W37.11–16)
- Exception threshold configuration and tuning (W37.9)
- CCTV integration specification: (a) system captures POS transaction timestamp and terminal ID; (b) POS integration layer sends transaction event to CCTV system via API or middleware; (c) CCTV system bookmarks associated video clip (configurable: ± 2 minutes around transaction event); (d) LPO retrieves correlated video from LP investigation dashboard by clicking transaction exception — system deep-links to CCTV playback at the transaction timestamp; (e) CCTV recording retention: minimum 30 days online storage, 90 days archived; (f) CCTV access restricted to LPO, Store Manager, Regional Manager, and Internal Audit via role-based access control; (g) for new store openings (W16), IT configures POS-to-CCTV integration as part of go-live readiness checklist (W16.9a); (h) system does not store video — only stores timestamp reference and CCTV clip ID for retrieval from the CCTV system's own storage
- Loyalty program fraud detection: system monitors for loyalty abuse patterns in addition to POS transaction exceptions; detection rules include: (a) cashier scanning the same loyalty card across > 20% of their transactions (self-scanning or family/friend farming), (b) loyalty points earned on subsequently voided transactions (points earned but not reversed), (c) unusually high points earning on single transaction (points-to-revenue ratio exceeding 3× normal), (d) multiple loyalty accounts with > 85% match on name, phone, or address (farming multiple accounts), (e) redemption velocity spike on dormant accounts; flagged patterns appear on LPO daily exception dashboard alongside POS exceptions; LPO investigates and escalates to Loyalty Manager for account action (W17 manual points adjustment); confirmed fraud cases result in account suspension per W17 manual adjustment approval tiers
- Gift card / store credit fraud detection: system monitors gift card and store credit transactions for fraud patterns: (a) multiple gift card balance inquiries from same terminal within short time window (potential brute-force balance checking), (b) gift card redemption at a different store within 24 hours of activation (potential barcode photocopying or stolen card), (c) return-to-store-credit followed by immediate cash-out attempt (return fraud), (d) employee-associated gift card transactions (employee purchasing or reloading their own gift card with subsequent return manipulation), (e) high-value gift card purchases paid in cash (potential money laundering); flagged patterns appear on LPO daily exception dashboard; LPO investigates and escalates to Store Manager for card suspension and customer verification; confirmed fraud results in gift card deactivation and loss reporting; monthly: LPO includes gift card fraud metrics in shrinkage report (W37.7); any manual gift card balance adjustment requires dual approval (Store Manager + AP Supervisor) with full audit trail

### Staffing Implication
- **2–3 Loss Prevention Officers** (reporting to Internal Audit or a dedicated LP function): Daily review (1–2 hours) + case investigation (5–10 active cases at any time) + monthly shrinkage reporting + quarterly reviews. This is a specialized role that may not exist in the current org chart. Recommend adding 2 LPOs to cover 200 stores (each covering ~70 stores, rotating through physical store visits).
- **Store Managers**: Review their store's exception report daily (~15 min). Absorbed into opening routine.
- **Internal Audit**: Incorporates LP findings into quarterly audit cycle. No incremental headcount.

### Confirmed Theft / Inventory Write-Off Process

When an LPO investigation confirms theft or irrecoverable loss:

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| W37.11 | LPO documents confirmed loss: investigation findings, supporting evidence (CCTV footage, transaction records, witness statements); for theft, files police report with local PNP station | LPO | Internal Audit | 1 hour/case |
| W37.12 | LPO submits inventory write-off request: SKU, quantity, value at WAC, root cause classification (internal theft, external shoplifting, vendor fraud, unexplained loss) | LPO | Internal Audit | 15 min/case |
| W37.13 | Approval per tier: (a) total loss ≤ PHP 10,000: Store Manager, (b) PHP 10,001–50,000: Regional Manager + Internal Audit, (c) PHP 50,001–500,000: Controller + Internal Audit, (d) > PHP 500,000: CFO + CEO | Approver | Approver | 15 min/case |
| W37.14 | System posts write-off: Dr. Inventory Loss / Cr. Inventory; removes items from inventory register; records loss in shrinkage tracking for store KPI | System | — | Automated |
| W37.15 | If loss is insured (e.g., large robbery, transit theft): LPO files insurance claim per W3.6a insurance claim process; Finance posts recovery upon settlement | LPO / Finance | Controller | Per W3.6a |
| W37.16 | Quarterly: LPO includes confirmed theft and write-off totals in shrinkage report (W37.7); feeds into store KPI scoring and loss prevention action plans | LPO | Internal Audit | Part of existing reporting |

---



---

## W49. Natural Disaster / Typhoon Business Continuity

| Field | Detail |
|---|---|
| **Trigger** | PAGASA raises tropical cyclone warning signal over a store/DC location; or earthquake, flooding, or volcanic activity alert |
| **Frequency** | ~10–20 typhoon-related events/year requiring action across Philippine store network; 2–4 significant events/year with store closures |
| **Volume** | Variable — from 1–2 stores affected (localized flooding) to 50+ stores (major typhoon crossing multiple regions) |
| **Owner** | COO (overall response); Store Manager (store-level execution) |
| **Participants** | COO, Store Ops Director, Regional Managers, Store Managers, DC Managers, IT, HR, Finance, Supply Chain, Marketing, Logistics |

### Background

The Philippines experiences an average of 20 tropical cyclones per year, of which 5–7 make landfall as typhoons (Signal 3 or higher). BuildRight's 200 stores span Luzon, Visayas, and Mindanao, meaning multiple regions can be affected simultaneously or sequentially. The primary risks are: (a) staff safety, (b) inventory damage (especially outdoor lumber yards and building materials), (c) facility structural damage, (d) supply chain disruption, and (e) revenue loss from store closures.

### Phase 1: Pre-Disaster Preparation (48–72 hours before projected landfall)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | COO monitors PAGASA bulletins and NDRRMC advisories; activates disaster monitoring protocol when Signal 1 is raised over any operating region | COO | CEO | Ongoing during typhoon season |
| 2 | Regional Managers notify Store Managers in affected regions to begin preparations; Store Managers brief all staff | Regional Manager | Store Ops Director | 1 hour |
| 3 | **Store preparations**: Store Manager directs staff to: (a) secure outdoor yard inventory — move lumber, cement, and building materials under cover or to higher ground; (b) protect floor-level merchandise from potential flooding (move to higher shelves or backroom); (c) secure display fixtures, signage, and loose items; (d) verify backup power (generator fuel level, battery backup for POS); (e) verify emergency supplies (flashlights, first aid kits, drinking water) | Store Manager | Regional Manager | 4–8 hours |
| 4 | **DC preparations**: DC Manager directs staff to: (a) prioritize outbound shipments to stores in safe zones before transport disruption; (b) secure outdoor inventory and yard areas; (c) verify backup power systems; (d) coordinate with carriers to suspend inbound shipments to affected areas | DC Manager | Supply Chain Manager | 4–8 hours |
| 5 | IT sends system advisory to all locations: reminder of offline POS procedures (W5g), system backup schedule accelerated | IT Team | CIO | 30 min |
| 6 | HR verifies emergency contact information for all employees in affected regions; prepares welfare check plan | HR Head | CHRO | 1 hour |
| 7 | Supply Planner reviews inventory levels at stores and DCs in projected path; identifies potential stockout risks for essential items (tarps, waterproofing, cement, plywood, flashlights, batteries, generators) | Supply Planner | Supply Chain Manager | 1 hour |

### Phase 2: Closure Decision & Execution (24–0 hours before projected landfall)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 8 | COO makes store closure decision based on: PAGASA signal level (Signal 2+ triggers automatic closure), LGU advisory, road conditions, staff safety assessment; decisions made by region, not chain-wide | COO | CEO | 30 min |
| 9 | Marketing communicates closure to customers: update website, social media, Google Business listings; send SMS/email to loyalty members in affected areas | Marketing | CMO | 1 hour |
| 10 | Ecommerce platform: Digital Commerce Inc. suspends BOPIS and delivery orders for closed stores/DCs; displays closure notice | Ecom Team | CMO | 30 min |
| 11 | Store Manager executes early closing procedure (abbreviated W5f): expedited Z-report, cash secured in safe (do NOT send with armored car during typhoon — hold in safe), POS shut down, building secured | Store Manager | Regional Manager | 30 min |
| 12 | Store Manager sends staff home with safety instructions; confirms all staff have departed safely | Store Manager | Regional Manager | 15 min |

### Phase 3: Post-Disaster Assessment & Recovery (0–72 hours after event)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 13 | Store Manager or designated contact conducts visual assessment of store exterior (drive-by or walk-by) as soon as safely possible after event passes; reports to Regional Manager: structural damage, flooding, power status, yard inventory status | Store Manager | Regional Manager | 30 min |
| 14 | Regional Manager compiles damage assessment across affected stores; reports to COO and Store Ops Director | Regional Manager | COO | 2 hours |
| 15 | COO makes reopening decision per store: (a) open immediately if no damage and power/connectivity restored, (b) delayed opening for minor cleanup and repair, (c) remain closed for significant damage requiring repair or insurance assessment | COO | CEO | 1 hour |
| 16 | **If inventory damaged**: Store Manager conducts damage inventory with photos; system creates damage report; disposition per W6.8a (scrap, markdown, RTV, insurance claim) | Store Manager / Maintenance | Regional Manager | 2–4 hours |
| 17 | **If facility damaged**: Facilities Coordinator engages contractors for emergency repair; Store Manager initiates insurance claim per W3.6a process (photos, documentation, claim filing) | Facilities Coordinator / Store Manager | Store Ops Director | Varies |
| 18 | Supply Planner triggers emergency replenishment for disaster-response items (tarps, plywood, cement, paint, waterproofing, tools, generators) to reopened stores; coordinates with DC for expedited shipment | Supply Planner | Supply Chain Manager | 2–4 hours |
| 19 | HR conducts welfare check on all employees in affected regions within 24 hours; provides assistance (advance salary, emergency loan, temporary shelter) per company policy | HR Head | CHRO | 4–8 hours |
| 20 | Marketing communicates reopening to customers; update website and social media; potential "rebuilding supplies" promotion to serve community needs | Marketing | CMO | 1 hour |
| 21 | System reconciles: process any offline POS transactions from pre-closure; reverse pending ecommerce orders for closed stores; update inventory for damaged/scrapped items | IT / Finance | Controller | 2–4 hours |

### Phase 4: Post-Event Review (1–2 weeks after)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 22 | COO conducts after-action review: preparation adequacy, response time, damage extent, recovery speed, staff safety outcomes | COO | CEO | 2 hours |
| 23 | Finance quantifies total loss: inventory damage, facility repair costs, revenue loss from closure days, insurance recovery | Controller | CFO | 1 day |
| 24 | Insurance claims finalized for major events; Finance tracks claim status and settlement | Treasury Analyst | CFO | Varies |
| 25 | Store Ops Director updates disaster response procedures based on lessons learned | Store Ops Director | COO | 2 hours |

### System Touchpoints
- Emergency communication channel integration (SMS blast to store managers, regional managers, employees) (W49.2, 6, 9)
- Store closure/reopening status tracking per location with real-time dashboard (W49.8, 15)
- Ecommerce platform store availability toggle for BOPIS/delivery (W49.10)
- Damage inventory recording with photo attachment and disposition workflow (W49.16)
- Emergency replenishment order generation with priority flag (W49.18)
- Insurance claim tracking per W3.6a process (W49.17, 24)
- Post-disaster inventory and financial reconciliation (W49.21, 23)
- Employee welfare check tracking with HR case management (W49.19)
- Integration with W5g (offline POS recovery), W3.6a (insurance claims), W22 (emergency transfers), W25 (emergency petty cash for cleanup supplies), W47 (facility emergency repair)

### Staffing Implication
- No dedicated disaster response team. Response is a cross-functional effort managed by existing roles (COO leads, Regional Managers execute, Store Managers act).
- **Facilities Coordinator** (recommended in W47) becomes critical during post-disaster recovery for coordinating emergency repairs across multiple affected stores.
- **IT Field Support** (recommended in W48) may need to deploy to affected stores for POS/network restoration.
- Post-disaster emergency replenishment adds temporary surge to Supply Planner and DC workload — absorbed with overtime during recovery period.

---



---

## W54. LGU Business Permit Renewal per Location

| Field | Detail |
|---|---|
| **Trigger** | LGU business permit renewal calendar (typically annual, per LGU) |
| **Frequency** | Annual per location; 200 stores + 5 DCs + HQ = ~206 renewals/year, staggered across LGU calendars |
| **Volume** | ~206 locations across ~150 different LGUs (some LGUs have multiple stores); most LGUs require renewal in January–March |
| **Owner** | Legal & Compliance — Regulatory Officer |
| **Participants** | Regulatory Officer, Store Manager, DC Manager, Finance, Facilities Coordinator |

### Background

Each BuildRight Depot store and DC operates within a specific Local Government Unit (LGU — city or municipality). Each LGU requires an annual business permit (Mayor's Permit) to operate, with requirements, fees, and renewal calendars varying by LGU. Failure to maintain current permits risks closure orders, fines, and reputational damage. BuildRight's 200 stores span ~150 distinct LGUs across Luzon, Visayas, and Mindanao.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System maintains LGU permit calendar per location: renewal deadline, LGU name, LGU-specific requirements, required documents, fee schedule (based on LGU rate × estimated gross receipts), prior year permit reference | Regulatory Officer | Legal Head | 4 hours/year (setup) |
| 2 | System alerts Regulatory Officer 60 days before each location's permit renewal deadline | System | — | Automated |
| 3 | Regulatory Officer prepares renewal package per LGU requirements: (a) current year business permit, (b) SEC/DTI registration, (c) BIR registration, (d) lease contract or proof of occupancy, (e) barangay clearance, (f) fire safety inspection certificate (BFP), (g) sanitary/health permit (if applicable), (h) local business tax payment receipt, (i) authorized representative letter if not store manager filing | Regulatory Officer | Legal Head | 1–2 hours/location |
| 4 | Regulatory Officer coordinates with Store Manager: Store Manager obtains barangay clearance (requires physical visit to barangay hall), confirms fire safety inspection is current (W47 preventive maintenance — BFP annual inspection), and verifies physical signage matches registered business name | Store Manager | Regulatory Officer | 1–2 hours/location |
| 5 | Finance processes local business tax payment per LGU schedule (separate from W9a.16c LBT payment — the permit renewal requires payment first or concurrently) | Treasury Analyst | Controller | 30 min/location |
| 6 | Regulatory Officer (or designated Store Manager) submits renewal application to LGU Business Permit and Licensing Office (BPLO); many LGUs now accept online renewal via Business One-Stop Shop (BOSS) portals | Regulatory Officer / Store Manager | Legal Head | 1–4 hours/location |
| 7 | LGU processes renewal; may require inspection or hearing; issues new business permit | LGU | — | External (1–30 days) |
| 8 | Store Manager receives new permit; displays original in store (BIR and LGU requirement); sends copy to Regulatory Officer for system upload | Store Manager | Regulatory Officer | 15 min |
| 9 | Regulatory Officer uploads permit copy to system; updates location master with new permit number, issue date, and expiry date | Regulatory Officer | Legal Head | 5 min/location |
| 10 | System alerts Regulatory Officer if permit not received within 30 days of renewal deadline; escalates to Legal Head | System | — | Automated |
| 11 | Monthly: Regulatory Officer generates permit status dashboard: active, pending renewal, expired, at-risk locations; Legal Head reviews expired permits as priority escalation | Regulatory Officer | Legal Head | 1 hour/month |

### System Touchpoints
- LGU permit calendar per location with renewal deadlines, LGU-specific requirements, and document checklists (W54.1)
- Automated renewal alerts at 60, 30, and 7 days before expiry (W54.2)
- Location master integration: permit number, issue date, expiry date stored per location; active permit required for location to remain in "Operating" status (W54.9)
- Document storage: permit copies attached to location record per DOC-001 (W54.8–9)
- Permit status dashboard with expiry alerting and escalation (W54.11)
- Integration with W9a.16c (LBT payment), W47 (fire safety inspection scheduling), W16 (new store — initial permit acquisition)

### Staffing Implication
- **1 Regulatory Officer** (within Legal & Compliance): ~206 renewals/year × ~3 hours each = ~620 hours/year = ~4 days/month. Concentrated in Q1 when most LGUs require renewal. This role also manages BIR CAS registration (W54a) and regulatory inspection handling. Absorbed within Legal & Compliance team (recommend expanding from ~5 to ~6 with the DPO role in W53).
- **Store Managers**: ~2 hours/year for their location's permit renewal coordination. Absorbed.

### W54a. BIR Computerized Accounting System (CAS) Registration

| Field | Detail |
|---|---|
| **Trigger** | New entity incorporation, new ERP system deployment, major system upgrade requiring re-registration, or annual permit renewal |
| **Frequency** | Initial registration per entity (5 entities); annual renewal per BIR requirements; re-registration if system undergoes major changes |
| **Volume** | 5 entity registrations initially; 5 annual renewals thereafter |
| **Owner** | Regulatory Officer |
| **Participants** | Regulatory Officer, CIO, Controller, CFO, external ERP vendor, BIR Regional Office |

### Background

Under BIR Revenue Regulations No. 11-2018 and Revenue Memorandum Order (RMO) No. 29-2002, any business using a computerized accounting system (including ERP systems) must register the system with the BIR and obtain a CAS Permit before the system can legally generate BIR-registered receipts, invoices, and accounting records. Each of BuildRight's 5 legal entities must obtain its own CAS permit. The system must be able to produce books of accounts (general journal, general ledger, cash receipts journal, cash disbursements journal, sales journal, purchases journal) in the format prescribed by BIR.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Regulatory Officer obtains BIR CAS registration forms: BIR Form 1907 (Application for Registration of Books of Accounts), together with system documentation package | Regulatory Officer | Legal Head | 4 hours/entity |
| 2 | IT and ERP vendor prepare system documentation package per BIR requirements: (a) system overview and architecture diagram, (b) data flow diagram showing transaction processing from source to GL, (c) security and access control documentation, (d) sample outputs: BIR-registered receipt format, sales invoice, purchase invoice, journal voucher, official receipt, books of accounts (general journal, general ledger, cash receipts/disbursements journals, sales/purchases journals), (e) data retention and backup procedures, (f) audit trail documentation, (g) BIR permit application letter signed by entity's authorized representative | IT Team / ERP Vendor | CIO | 2–3 weeks/entity |
| 3 | Controller reviews and validates sample outputs for accounting accuracy: GL account mapping, journal entry formatting, books of accounts layout compliance with BIR-prescribed format | Controller | CFO | 4 hours/entity |
| 4 | Regulatory Officer submits CAS registration application to BIR Regional Office (or Revenue District Office) where the entity is registered; pays registration fee per BIR schedule | Regulatory Officer | Legal Head | 1 day/entity |
| 5 | BIR evaluates application; may conduct system demonstration or on-site inspection at BuildRight office; IT and Finance present system capabilities to BIR evaluators | BIR / IT / Finance | CFO | 1–2 days/entity (if inspection required) |
| 6 | BIR issues CAS Permit (Authority to Use Computerized Accounting System) per entity; permit includes registered system name, entity TIN, permit number, and conditions of use | BIR | — | External (2–6 months from submission) |
| 7 | Regulatory Officer records CAS permit in system: permit number, issue date, expiry date (if applicable — some permits are perpetual unless system changes), entity TIN, authorized system name; uploads permit document to entity master | Regulatory Officer | Legal Head | 15 min/entity |
| 8 | IT configures ERP to print BIR-registered receipt/invoice numbers per CAS permit: system generates sequential, non-skippable invoice/receipt numbers per BIR requirements; TIN, registered business name, and CAS permit number printed on all receipts per BIR format | IT Team | CIO | 2–3 days/entity |
| 9 | **Annual renewal** (if required per BIR ruling): Regulatory Officer submits renewal documentation before expiry; confirms no material system changes since last registration | Regulatory Officer | Legal Head | 2 hours/entity/year |
| 10 | **Re-registration triggers**: if ERP system undergoes major version upgrade, change of ERP platform, or change of entity legal name, Regulatory Officer files amended CAS registration with updated system documentation | Regulatory Officer / IT | CFO | Per initial process |

### System Touchpoints (BIR CAS)
- CAS permit tracking in entity master: permit number, issue date, expiry date, authorized system name (W54a.7)
- BIR-compliant sequential invoice/receipt numbering: system enforces non-skippable, sequential numbering per CAS permit per entity; voided transactions retain number with void indicator per BIR requirements; system prints or records a BIR-compliant void receipt referencing the original transaction number, void reason code, and authorizing manager ID per CAS permit conditions (W54a.8)
- BIR books of accounts generation: system produces general journal, general ledger, cash receipts journal, cash disbursements journal, sales journal, and purchases journal in BIR-prescribed format (per CAS registration commitment) (W54a.2)
- Entity-level CAS permit number printed on all receipts, invoices, and official receipts alongside entity TIN (W54a.8)
- Integration with W5b (BIR-registered receipt printing), W9a (books of accounts generation for close), W16 (new entity setup — CAS registration required before entity can transact), W54 (LGU permits — Regulatory Officer manages both)

### Staffing Implication
- **Regulatory Officer**: initial registration adds ~40–60 hours across 5 entities (concentrated during ERP implementation Phase 2); annual renewals add ~10 hours/year. Absorbed within existing role.
- **IT**: system documentation preparation adds ~2–3 weeks/entity during implementation; absorbed within implementation project.
- **Controller**: sample output validation adds ~4 hours/entity during implementation; absorbed.

---



---

## W77. BIR Tax Audit Response

| Field | Detail |
|---|---|
| **Trigger** | BIR issues Letter of Authority (LOA) or audit notification to any BuildRight entity |
| **Frequency** | Occasional; estimated 1–2 BIR audits/year across 5 entities; higher probability for entities with large revenue or import activity |
| **Volume** | Audit scope varies — from specific tax type (VAT only) to comprehensive (income tax, VAT, withholding tax) for 1–3 taxable years |
| **Owner** | Tax Accountant (operational); Controller (oversight); CFO (escalation) |
| **Participants** | Tax Accountant, Controller, CFO, Chief Accountant, AP Clerk, AR Clerk, IT, Legal, external tax advisor, BIR Revenue Officers |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | BIR Revenue Officer presents Letter of Authority (LOA) at entity's registered office or BIR Regional Office; Tax Accountant receives and logs LOA in system: LOA number, audit period, tax types under audit, assigned Revenue Officers, deadline for submission | Tax Accountant | Controller | 30 min |
| 2 | Controller and CFO assess audit scope and risk; engage external tax advisor (CPA firm) for audit representation if assessment is complex or potential exposure is material (> PHP 1M) | Controller / CFO | CEO | 1 hour |
| 3 | Tax Accountant gathers documents per BIR requirements — system generates: (a) books of accounts (general journal, general ledger, cash receipts/disbursements journals, sales/purchases journals) per BIR format and CAS permit (W54a), (b) VAT returns and supporting schedules for audit period, (c) withholding tax returns (1601-E, 1601-C) and alphalist of payees, (d) income tax returns and supporting financial statements, (e) summary of credit/debit notes, (f) list of related-party transactions and IC pricing documentation per W14, (g) fixed asset register and depreciation schedules, (h) inventory records and physical count reports (W42) | Tax Accountant / Chief Accountant | Controller | 2–5 days |
| 4 | Tax Accountant prepares working papers reconciling tax returns to books of accounts; identifies and documents any discrepancies or areas of exposure before submission to BIR | Tax Accountant | Controller | 3–5 days |
| 5 | Tax Accountant or external tax advisor submits documents to BIR Revenue Officers per LOA deadline; logs submission date and receipt confirmation in system | Tax Accountant | Controller | 1 day |
| 6 | BIR conducts examination: Revenue Officers may request additional documents, clarifications, or schedule meetings/walkthroughs; Tax Accountant coordinates responses within 5 business days per BIR practice | Tax Accountant / Controller | CFO | Varies (weeks to months) |
| 7 | BIR issues Preliminary Assessment Notice (PAN) if deficiencies found; Tax Accountant and external tax advisor review PAN; prepare protest or rebuttal within 15 days of receipt if assessment is disputed | Tax Accountant / External Advisor | CFO | 3–5 days |
| 8 | If protest accepted by BIR: case closed; Tax Accountant documents final resolution. If BIR issues Final Assessment Notice (FAN): Tax Accountant evaluates options — (a) accept assessment and pay deficiency tax + surcharge + interest; (b) escalate to Court of Tax Appeals or file motion for reconsideration within 30 days | Tax Accountant / CFO / Legal | CEO | 3–10 days |
| 9 | If payment required: Treasury processes payment per W30; system posts payment (Dr. Tax Payable / Dr. Tax Penalty Expense / Cr. Cash); Tax Accountant files amended returns if applicable | Treasury Analyst / Tax Accountant | CFO | Per W30 |
| 10 | Post-audit: Controller and Tax Accountant conduct lessons-learned review; document findings and corrective actions to prevent recurrence; update internal tax compliance procedures (W9a) if needed; include audit outcomes in next quarterly management committee meeting (W35.14) | Controller / Tax Accountant | CFO | 2 hours/audit |
| 11 | Quarterly: Tax Accountant maintains BIR audit readiness checklist: confirm books of accounts are current and BIR-compliant, withholding tax alphalists reconcile to returns, IC transfer pricing documentation is complete per W14, CAS permit is current per W54a, all tax returns filed on time | Tax Accountant | Controller | 2 hours/quarter |

### System Touchpoints
- BIR audit register: LOA number, audit period, tax types, Revenue Officers, submission deadlines, assessment amounts, protest status, resolution date (W77.1)
- Books of accounts generation in BIR-prescribed format per CAS permit (W77.3, cross-reference W54a)
- Tax return and supporting schedule retrieval for audit periods (W77.3)
- Document submission tracking with deadline alerting (W77.5)
- Assessment tracking with protest deadline management (W77.7–8)
- Integration with W9a (month-end close — source of audit documents), W14 (IC transfer pricing documentation), W30 (payment of deficiencies), W35 (management reporting), W54a (CAS permit compliance)

### Staffing Implication
- **Tax Accountant**: audit response adds ~40–80 hours per audit over 2–4 months. Absorbed within existing role with priority reallocation during active audits.
- **External tax advisor**: engaged for complex audits; budgeted within Finance operations.
- **No incremental headcount.**

---



---

## W78. Government / Institutional Procurement Participation

| Field | Detail |
|---|---|
| **Trigger** | Government agency, LGU, or state-owned enterprise issues Invitation to Bid or Request for Quotation (RFQ) for construction materials, hardware, or related supplies |
| **Frequency** | ~20–40 government procurement opportunities/year; primarily infrastructure agencies (DPWH), LGUs, DepEd, DOH, and state universities |
| **Volume** | Individual contract values PHP 500K–20M; represents ~5–8% of total revenue |
| **Owner** | Sales Rep (Trade & Corporate) — dedicated government accounts representative |
| **Participants** | Sales Rep, Category Manager, Pricing Analyst, Legal, Finance, Supply Planner |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Sales Rep monitors government procurement opportunities: PHILGEPS (Philippine Government Electronic Procurement System) portal, agency websites, and newspaper postings per RA 9184 (Government Procurement Reform Act); identifies opportunities matching BuildRight's product range | Sales Rep | VP Merchandising | 2 hours/week |
| 2 | Sales Rep evaluates opportunity viability: (a) product match — does BuildRight carry the specified items or equivalents, (b) delivery capability — can BuildRight deliver to the agency's required locations within the specified timeline, (c) pricing competitiveness — can BuildRight meet the Approved Budget for the Contract (ABC), (d) eligibility — does BuildRight meet PHILGEPS registration, BIR tax compliance, and other bidder eligibility requirements | Sales Rep | Category Manager | 1–2 hours/opportunity |
| 3 | Sales Rep prepares bid/quote documents per agency requirements: (a) PHILGEPS registration certificate, (b) BIR tax compliance certificate, (c) business permits per W54, (d) audited financial statements (most recent year from W9b), (e) similar completed projects or supply contracts, (f) product specifications and pricing, (g) delivery schedule and terms, (h) bid security (if required) | Sales Rep / Legal | VP Merchandising | 4–8 hours/bid |
| 4 | Category Manager and Pricing Analyst review proposed pricing: ensure margin is adequate (minimum gross margin target for government contracts, typically 10–15%); verify that pricing does not violate any existing contract pricing or trade agreements | Category Manager / Pricing Analyst | VP Merchandising | 1–2 hours/bid |
| 5 | Sales Rep submits bid/quote per agency deadline (sealed bid, electronic submission, or direct quotation depending on procurement method per RA 9184) | Sales Rep | VP Merchandising | Per deadline |
| 6 | **If awarded**: Sales Rep creates Sales Order in system linked to government Purchase Order; applies government-specific pricing and delivery schedule; system creates delivery plan per W19 or in-store pickup per W11 (BOPIS); revenue recognized at delivery per standard process | Sales Rep | Finance Manager | Per W58 |
| 7 | **Billing**: Sales Rep generates billing documents per government agency requirements — (a) standard sales invoice with BIR-registered format, (b) delivery receipt signed by agency receiving officer, (c) collection receipt per agency's accounting procedures; government accounts typically on Net 30–60 terms; collection requires submission of complete billing documents per agency-specific procedures (some agencies require liquidation documents or progress reports) | Sales Rep / AR Clerk | AR Supervisor | Per W8 |
| 8 | **Collection**: AR Clerk follows up on government receivables per W8 collection tiers; government payments may be delayed due to budget processing — Sales Rep coordinates with agency procurement officer and accounting division; system tracks government receivable aging separately from trade accounts for reporting | AR Clerk / Sales Rep | AR Supervisor | Per W8 |
| 9 | Quarterly: Sales Rep and Category Manager review government account portfolio: win rate, revenue, margin, collection timeliness, and bid pipeline; VP Merchandising reviews as part of corporate account portfolio (W58.10) | Sales Rep / Category Manager | VP Merchandising | 2 hours/quarter |

### System Touchpoints
- PHILGEPS registration tracking in vendor/customer master with renewal alerting (W78.1)
- Government customer account with specialized billing requirements, delivery terms, and collection procedures (W78.6–8)
- Government-specific pricing and margin validation per W40 approval workflow (W78.4)
- Government receivable aging separate from trade accounts for reporting and collection management (W78.8)
- Integration with W8 (AR and collections), W19 (delivery), W24 (credit application — government accounts may use purchase orders instead of credit), W40 (pricing), W54 (LGU permits — build compliance documentation), W58 (corporate account management)

### Staffing Implication
- **1 Sales Rep (dedicated government accounts)**: within the existing 3–4 Sales Reps (Trade & Corporate) per W58, one rep should specialize in government accounts given the unique procurement regulations and document requirements; PHILGEPS monitoring and bid preparation add ~8–12 hours/week during active bidding periods.
- **No incremental headcount.** Absorbed within existing B2B sales team.

---



---

## W79. Employee Grievance & Whistleblower Process

| Field | Detail |
|---|---|
| **Trigger** | Employee files a grievance regarding workplace conditions, policy violations, harassment, discrimination, or unethical conduct; or whistleblower report of fraud, corruption, or legal non-compliance |
| **Frequency** | Estimated 20–50 grievance/whistleblower reports/year across all locations |
| **Volume** | Grievance categories: workplace conflict (30%), policy/procedure concern (25%), compensation/benefits dispute (20%), harassment/discrimination (15%), safety concern (10%) |
| **Owner** | HR Head (grievance); Internal Audit (whistleblower reports involving management) |
| **Participants** | Employee, HR Head, Internal Audit, Legal, Department Head / Store Manager, CHRO |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Employee submits grievance or whistleblower report; or incident reported (theft, misconduct, policy violation) | Employee / Manager | — | 15 min |
| 2 | HR Head (grievance) or Internal Audit (whistleblower) acknowledges receipt within 24 hours; assigns case number; classifies severity (Minor, Serious, Grave, Critical) | HR Head / Internal Audit | CHRO | 15 min/case |
| 3 | **Due Process: Notice to Explain (NTE)**: For disciplinary cases, HR issues NTE to employee; provides 120 hours (5 business days) to submit written response per Philippine Labor Code | HR ER Officer | — | 30 min |
| 4 | Employee submits written explanation; system records date/time received; HR reviews explanation | Employee | — | — |
| 5 | **Administrative Hearing**: For Serious/Grave offenses, HR conducts hearing; documents proceedings in system; respondent allowed counsel or union representative | HR ER Officer | Dept Head | 1–2 hours |
| 6 | **Decision / Notice of Decision (NOD)**: HR and Dept Head determine outcome (Exoneration, Warning, Suspension, or Termination) per company table of offenses | HR Head | Dept Head | 1 hour |
| 7 | System generates NOD; issued to employee; system updates employee record with disciplinary status; if Suspension: System auto-blocks timekeeping for suspension dates | HR ER Officer | — | 15 min |
| 8 | **Whistleblower / High Severity Investigation**: For harassment, fraud, or corruption — HR Head and Legal/Audit jointly investigate; whistleblower identity protected; retaliation protection flagged (W79.7) | HR Head / Legal / Internal Audit | CHRO / CEO | 8–20 hours/case |
| 9 | Monthly: HR Head generates grievance/whistleblower summary; reports to CHRO and CEO | HR Head | CHRO | 2 hours/month |

### System Touchpoints
- Grievance submission form in self-service portal with category, severity, and desired resolution fields (W79.1)
- Anonymous whistleblower channel (email or third-party hotline) integration with case management (W79.1)
- Case management with severity classification, investigation tracking, evidence attachment, and resolution documentation (W79.2–6)
- Retaliation protection: system flags adverse actions against grievance filers within 90-day lookback (W79.7)
- Grievance/whistleblower analytics: volume, category, severity, location, resolution time (W79.8)
- Integration with W10 (payroll — preventive suspension with pay), W43 (separation — pending grievance resolved before clearance), W47 (safety concerns), W51 (self-service portal, training improvements), W72 (corrective action and progressive discipline)
- Whistleblower anonymity technical controls: the anonymous whistleblower channel (dedicated email or third-party hotline) is configured with the following technical safeguards: (a) no IP address logging on the whistleblower submission form; (b) no employee ID or session token capture on anonymous submissions; (c) if third-party hotline is used, the provider contractually commits to not disclosing reporter identity to BuildRight management; (d) system stores whistleblower case records with a pseudonymous case ID — the real identity is accessible only to the DPO and Internal Audit lead (dual-access control); (e) retaliation protection (W79.7) is extended to anonymous reporters where identity is later inferred or disclosed; (f) annual: DPO reviews whistleblower channel anonymity safeguards as part of privacy impact assessment (W53)

### Staffing Implication
- **HR Head**: grievance investigation adds ~20–40 hours/year. Absorbed within existing role.
- **Internal Audit**: whistleblower investigation adds ~10–20 hours/year. Absorbed.
- **No incremental headcount.** Grievance handling is a core HR function distributed across existing management.

---

### HQ Departments

| Department | Roles | Count | Key Workflows | Validation |
|---|---|---|---|---|
| **Merchandising & Buying** | VP, Category Managers, Buyers, Pricing Analysts, Merch Planners | ~40 | W1, W2, W13, W20, W23, W27, W29, W32, W36, W40, W44, W68 | ✅ Adequate for daily PO review + quarterly assortment cycles + VMI/consignment oversight + rebate management + seasonal planning + vendor onboarding + price maintenance + product discontinuation lifecycle; includes 1–2 dedicated Buyers for trade/special orders (W38) within the ~40 team |
| **Finance & Accounting** | Controller, Chief Accountant, AP/AR Clerks, Treasury, Tax | ~35 | W7, W7d, W8, W9, W14, W21, W24, W25, W26, W27, W28, W30, W39, W42, W54a (CAS permit validation), W59, W60, W70, W74 | ✅ Stretched during close week; capex/credit/petty cash absorbed; treasury daily cycle manageable with 2–3 analysts; asset disposal and annual physical inventory absorbed; insurance lifecycle and emergency procurement review absorbed; credit/debit note reconciliation absorbed into month-end close and weekly AP/AR review; AP staffing recalculated on business-day basis: ~305–370 invoices/business-day (6,500 merchandise + 2,000–3,000 non-PO per month ÷ 22 business days) requiring 10 clerks at ~5–6 hrs each/day; month-end peak (+50%) requires overtime or Finance staff redeployment; vendor statement reconciliation (W7d) absorbed into monthly AP cycle; employee expense reimbursement (W74) adds ~25–42 hours/month absorbed across AP team |
| **Supply Chain & Logistics** | Supply Planners, Demand Planners, Import Coordinator, Fleet Manager, DC Ops managers | ~31 | W3, W3c, W4, W4b, W19, W19b, W22, W22b, W31, W52, W56, W57, W62b, W66 | ✅ 2–3 planners handle replenishment + store-initiated requests + transfers + backorder fulfillment + promo allocation; home delivery and ship-from-store picked by DC/store staff; 1–2 dedicated demand planners handle forecasting; 1 Fleet Manager manages owned vehicles and 3PL relationships; Import Coordinator absorbs inter-island logistics; DC inbound scheduling (W3c) absorbed by DC Receiving Supervisor; 3PL partner onboarding (W62b) absorbed by Fleet Manager; allocation rule governance reviewed quarterly as part of W31.8 parameter cycle |
| **HR & Payroll** | HR Head, Recruitment, Payroll, Training Officer, HR Assistants | ~16 | W10, W15, W51, W72 | ✅ 2–3 payroll officers + 2 recruiters + 1 Training Officer handle the volume; employee performance management absorbed by ~230 managers |
| **Marketing** | Brand, Promo, Loyalty, Ecommerce, Digital, Content, CS Manager | ~24 | W13, W17, W50, W61, W65 | ✅ Loyalty is largely automated; promo work is cyclical; dedicated Content Manager + 2–3 Content Specialists for ecommerce product content; CS Manager owns customer satisfaction measurement; price match review absorbed by Pricing Analysts |
| **Store Operations** | Director, Regional Managers, CS Manager, Ops Standards, Facilities Coordinator | ~23 | W5, W5d (in-store delivery), W5e (opening delay), W16, W29, W5g (offline recovery), W34, W37, W41, W47, W49, W54a, W67, W69, W71 | ✅ 4 Regional Managers × 50 stores each; oversee new openings and monthly store performance reviews; in-store delivery uses existing 3PL carrier infrastructure; opening delay procedure is Store Mgr responsibility; offline recovery is Store Mgr responsibility; shift scheduling and complaint handling absorbed; 2–3 LPOs recommended for loss prevention; 1 Facilities Coordinator manages store maintenance, disaster response, and physical security oversight; weekly price compliance audits absorbed by Dept. Supervisors and Stock Associates |
| **IT** | Infrastructure, Apps, Data, Security, BI Analyst, Helpdesk | ~28–30 | W16 (store setups), W35 (reporting), W48 (helpdesk & IT ops) | ✅ 4–5 helpdesk agents + 3–4 specialists handle ~800–1,200 tickets/month; 2–3 per store setup + BAU support; 1 BI Analyst supports management reporting; note: for physical IT support across the Philippine archipelago (200 stores + 5 DCs across Mindanao, Visayas, Luzon), 1–2 dedicated field staff may not provide adequate same-day response for P1 incidents in remote locations — recommend (a) training designated Store Managers as first-level hardware troubleshooters (certified on basic POS terminal swap, cable reseat, network restart), (b) contracting regional IT service providers in each major region (Davao, Cebu, Manila, Clark) for emergency on-site support, and (c) maintaining a spare POS terminal and network equipment swap stock at each DC for rapid dispatch |
| **Other** | Legal, Internal Audit, DPO, Regulatory Officer, Customer Service (call center), Executive | ~52 | W41 (complaints), W42 (audit observation), W53 (data privacy breach, DSAR lifecycle, data portability/erasure), W54 (LGU permits), W54a (BIR CAS registration), W62 (vendor contracts) | ✅ Support functions; call center handles multi-channel complaint intake; Legal expanded to include DPO (W53 with full DSAR lifecycle) and Regulatory Officer (W54 LGU + W54a BIR CAS); total Legal & Compliance expands from ~5 to ~7 |

### Per-Store Staffing (35 people)

| Role | Count | Key Workflows | Workload Validation |
|---|---|---|---|
| Store Manager | 1 | W5 (open/close), W5d (in-store delivery coordination), W5e (opening delay handling), W6 (approvals), W12 (returns), W16 (opening), W22b (store-to-DC returns), W54 (LGU permit coordination), W67 (monthly performance review), W69 (price audit review) | Manageable; delegates floor ops to supervisors |
| Asst. Store Manager | 1 | W5 (open/close backup), W6, W12 | Shares management load; covers days off |
| Dept. Supervisors | 4 | W5b (floor selling), W6 (cycle count review), W12 (restock), W69 (price compliance audit execution and review) | 4 depts × 1 supervisor; handles floor + counts + weekly price audits |
| Sales Associates | 16 | W5b (selling, paint mixing, lumber cutting), W5d (in-store delivery staging), W11 (BOPIS pick), W56 (backorder intake), W61 (price match verification) | 4/dept × 2 shifts = adequate for floor coverage |
| Cashiers | 6 | W5b (checkout), W17 (loyalty scan), W28 (gift card sell/reload) | 5 terminals + 1 float; 2 shifts of 3; tight on coverage |
| Receiving Clerks | 2 | W4 (store receiving from DC), W18 (DSD receiving), W22 (transfer receiving), W22b (store-to-DC return staging) | 2–3 DC trucks/week + 2–3 DSD/week + transfers + return staging; 2 clerks in shifts handle it |
| Stock Associates | 3 | W4 (shelf stocking), W4b (store replenishment request), W6 (cycle counting), W11 (BOPIS pick), W18 (DSD shelving), W19b (ship-from-store picking), W22 (transfer pick/receive), W22b (store-to-DC return packing), W34 (shift adherence), W42 (annual count), W57 (promo stock staging), W63 (shelf label application), W69 (price audit scanning) | 700 SKUs/day counting + stocking + DSD + transfers + label updates + weekly price audit; adequate but minimal slack |
| Customer Service Rep | 1 | W11 (BOPIS handoff), W12 (returns), W24 (credit application assistance), W28 (store credit), W29 (recall returns), W33 (warranty claims), W38 (special order intake), W41 (complaints) | ~4 BOPIS + ~2 returns + ~0.5 gift cards + ~2 warranty claims + ~0.5 special orders + ~10 complaints/day = moderate; also handles special orders |
| Maintenance | 1 | W5f (closing checklist), W47 (facility maintenance & work orders), general upkeep | Standard for big-box format; handles ~10–15 maintenance work orders/month including preventive tasks; external contractors engaged for specialized repairs |
| **Total** | **35** | | **Validated — headcount is lean but supportable** |

### Per-DC Staffing (~150 people)

| Function | Count | Key Workflows | Workload Validation |
|---|---|---|---|
| DC Manager + Supervisors | 5 | W3, W4 (oversight) | 1 manager + 4 shift/area supervisors |
| Receiving | 10–13 | W3 (receiving & putaway), W20 (VMI receipt) | ~40 receipts/day × 1.5–3 hrs; 3–4 clerks + 4–6 putaway + 1–2 QC |
| Picking & Packing | 25–30 | W4 (pick/pack/ship), W19 (home delivery pick/pack) | ~33 store orders + ~115 home delivery orders/day; 15–20 pickers + 8–10 packers; 3–4 dedicated to home delivery; peak ecommerce periods may require surge staffing |
| Loading & Dispatch | 6–8 | W4 (loading) | Multi-drop truck loading; 4–6 crew + dispatch |
| Inventory Control | 2–3 | W6 (DC cycle counts) | DC-level accuracy monitoring |
| Admin & Support | 5–8 | Admin, safety, maintenance | Office, security, equipment maintenance |
| Special Handling (lumber, tiles, paint) | 8–10 | W3, W4 (special areas) | Dedicated teams for heavy/hazardous goods |
| **Total** | **~150** | | **Validated** |

---



---

## W82. Hazardous Waste Disposal Tracking & DENR Compliance

| Field | Detail |
|---|---|
| **Trigger** | Hazardous waste accumulation at location reaches disposal threshold; or quarterly disposal schedule; or DENR reporting deadline |
| **Frequency** | Disposal: quarterly per location (minimum); DENR reporting: quarterly; Permit renewal: annual per location |
| **Volume** | Hazardous waste categories: paint/chemical waste (sludge, expired products, solvent rags), used oils and lubricants (from fleet maintenance W52, forklift maintenance), broken fluorescent lamps and LED tubes (mercury content), used batteries (lead-acid from forklifts, UPS systems), aerosol cans (residual propellant); ~200 stores + 5 DCs each generating small but regulated quantities |
| **Owner** | Regulatory Officer (HQ); Store Manager / DC Manager (location-level execution) |
| **Participants** | Regulatory Officer, Store Manager, DC Manager, Maintenance Staff, accredited transporter, DENR-accredited treatment/disposal facility, Finance (disposal cost), Legal |

### Background

BuildRight Depot operations generate hazardous waste across several categories regulated by the Philippine Department of Environment and Natural Resources (DENR) under Republic Act 6969 (Toxic Substances and Hazardous and Nuclear Wastes Control Act) and its implementing rules (DAO 29, DENR Administrative Order). Each location (store or DC) that generates hazardous waste is classified as a waste generator and must hold a DENR Hazardous Waste Generator Registration (HWGR). Compliance requires: proper storage and labeling, use of DENR-accredited transporters and treaters, manifest tracking, and quarterly disposal reports.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Location registration**: for each new store (W16) or DC, Regulatory Officer applies for DENR Hazardous Waste Generator Registration (HWGR) — submits required documents (business permit, location map, waste management plan, emergency response plan) to DENR-EMB regional office; receives HWGR certificate with generator ID number; system records HWGR number, registration date, and expiry date per location | Regulatory Officer | Legal Head | 2–4 hours/location (initial) |
| 2 | **Annual renewal**: system alerts Regulatory Officer 90 days before HWGR expiry per location; Regulatory Officer submits renewal documents to DENR-EMB; renewed certificate uploaded to location document management (W54-style permit tracking) | Regulatory Officer | Legal Head | 1 hour/location/year |
| 3 | **Ongoing accumulation at location**: Maintenance Staff (or designated Stock Associate at stores) segregates hazardous waste by category in designated, properly labeled storage containers — (a) **paint/chemical waste**: expired paint, adhesives, solvents, contaminated rags — stored in sealed drums in ventilated area away from ignition sources, (b) **used oils**: from forklift maintenance at DCs and vehicle maintenance per W52 — stored in sealed containers in bunded area, (c) **fluorescent lamps**: broken or expired tubes — stored in original packaging or dedicated collection boxes, (d) **used batteries**: lead-acid batteries from forklifts and UPS systems — stored upright on spill containment pallets, (e) **aerosol cans**: residual product cans — stored in vented containers | Maintenance Staff / Stock Associate | Store Manager / DC Manager | Ongoing |
| 4 | **Accumulation monitoring**: system tracks hazardous waste accumulation per location per waste category — Maintenance Staff logs waste additions (category, estimated quantity, date) in system via handheld or terminal; system flags location when accumulated quantity approaches disposal threshold (configurable per category based on DENR storage limits — typically 90 days maximum storage) | Maintenance Staff | Store Manager / DC Manager | 5 min/entry |
| 5 | **Disposal scheduling**: when location reaches disposal threshold or quarterly schedule triggers — Regulatory Officer coordinates disposal with DENR-accredited transporter and DENR-accredited treatment/storage/disposal (TSD) facility; obtains quotations from accredited providers; selects based on: DENR accreditation status, cost, proximity, service reliability | Regulatory Officer | Legal Head | 1–2 hours/disposal event |
| 6 | **Transporter accreditation verification**: before each shipment, Regulatory Officer verifies transporter's DENR accreditation (PCO license, transport permit, vehicle registration with DENR) is current and valid; system maintains accredited transporter registry with accreditation expiry tracking and auto-alerting | Regulatory Officer | Legal Head | 15 min/verification |
| 7 | **Hazardous waste manifest (DENR Form)**: Regulatory Officer prepares DENR-compliant hazardous waste manifest per shipment — (a) generator information (BuildRight location name, address, HWGR number), (b) waste description (category, quantity, physical state, hazard characteristics), (c) transporter information (company name, DENR transport permit number, vehicle plate, driver name), (d) TSD facility information (company name, DENR permit number, facility address), (e) six-copy manifest per DENR format — signed by generator, transporter, and TSD facility | Regulatory Officer | Store Manager / DC Manager | 30 min/manifest |
| 8 | **Physical pickup**: accredited transporter arrives at location; Maintenance Staff and transporter representative jointly verify waste quantity and category against manifest; both sign manifest copies; transporter loads waste | Maintenance Staff / Transporter | Store Manager / DC Manager | 30–60 min/pickup |
| 9 | **Manifest tracking**: system tracks manifest lifecycle — (a) **Generated**: manifest created and signed by generator, (b) **In Transit**: transporter departs with waste, (c) **Received by TSD**: TSD facility signs manifest confirming receipt and treatment/disposal, (d) **Closed**: TSD returns signed manifest copy (generator copy) to Regulatory Officer within 30 days; if manifest not returned within 30 days, system alerts Regulatory Officer for follow-up with transporter and TSD | Regulatory Officer / System | Legal Head | 15 min/manifest tracking |
| 10 | **Disposal cost processing**: Finance processes disposal invoice from transporter/TSD — (a) invoice matched to manifest number and location, (b) cost allocated to location's operating expense (Dr. Waste Disposal Expense / Cr. Cash), (c) system tracks disposal cost per location per quarter for budgeting (W26) | AP Clerk / Finance | Controller | Per W7 |
| 11 | **Quarterly reporting**: Regulatory Officer prepares DENR quarterly disposal report (due within 30 days after end of quarter) — (a) total waste generated by category per location, (b) total waste disposed by category per location with manifest references, (c) transporter and TSD facility details, (d) current on-site waste inventory per location; report submitted to DENR-EMB regional office per location jurisdiction | Regulatory Officer | Legal Head | 4 hours/quarter |
| 12 | **Annual waste management plan update**: Regulatory Officer reviews and updates the waste management plan per location — (a) projected waste generation by category, (b) disposal schedule and budget, (c) transporter and TSD facility list, (d) emergency response procedures for spills or accidents; updated plan submitted to DENR as part of HWGR renewal | Regulatory Officer | Legal Head | 8 hours/year |
| 13 | **Spill / accidental release response**: if hazardous material spills or is accidentally released at a location — (a) Maintenance Staff contains spill using location's spill kit (positioned at paint area, chemical storage, and battery storage areas), (b) reports spill to Store Manager / DC Manager and Regulatory Officer, (c) Regulatory Officer assesses severity — minor spill (contained on-site, cleaned with standard PPE): location staff handles cleanup with proper disposal of contaminated materials per W82; major spill (spreading, off-site risk, or personnel exposure): Regulatory Officer engages DENR-accredited emergency response contractor and notifies DENR-EMB within 24 hours, (d) system logs spill event with date, location, material, quantity, response actions, and disposal of contaminated cleanup materials | Maintenance Staff / Regulatory Officer | Legal Head | Varies |

### System Touchpoints
- Hazardous waste generator registration (HWGR) tracking per location with expiry alerting (W82.1–2)
- Hazardous waste accumulation log per location per category with disposal threshold alerting (W82.3–4)
- DENR hazardous waste manifest lifecycle tracking: Generated → In Transit → Received by TSD → Closed; auto-alert if manifest not returned within 30 days (W82.7–9)
- Accredited transporter registry with DENR accreditation expiry tracking (W82.6)
- Quarterly disposal reporting: waste generation, disposal, and inventory by location and category (W82.11)
- Disposal cost tracking per location per quarter integrated with AP (W82.10)
- Spill / accidental release event logging with response documentation (W82.13)
- Integration with W16 (new store opening — HWGR registration as part of pre-opening permits), W25 (petty cash — small disposal costs may be paid from petty cash), W26 (budget — annual disposal budget per location), W47 (facility maintenance — spill kit maintenance and replenishment), W48 (IT helpdesk — hazardous waste system support), W52 (fleet — used oil and battery disposal), W54 (LGU permits — HWGR tracked alongside LGU business permits in location compliance dashboard), W62 (vendor contracts — transporter and TSD facility contracts), W68 (product discontinuation — hazardous waste disposal for discontinued chemicals/paint)

### Staffing Implication
- **Regulatory Officer** (1 person in Legal & Compliance team): manages HWGR registrations, disposal scheduling, manifest tracking, DENR reporting, and transporter accreditation for 200 stores + 5 DCs. Quarterly reporting adds ~4 hours; annual plan update adds ~8 hours; ongoing coordination adds ~4–6 hours/month. This role is justified by the regulatory compliance requirement and aligns with the Regulatory Officer position mentioned in the model company profile.
- **Maintenance Staff** (1 per store, part of existing headcount): hazardous waste segregation and logging adds ~15 min/week. Absorbed.
- **DC Safety/Environmental Officer** (1 per DC, within existing support staff): hazardous waste management at DCs adds ~2 hours/month. Absorbed.
- No incremental headcount beyond the Regulatory Officer role already planned in the model company profile.

---



## W95. External Audit Coordination & Support

| Field | Detail |
|---|---|
| **Trigger** | Annual external audit engagement per SEC requirement; quarterly review (if required by lenders or board); or special audit (M&A due diligence, regulatory investigation) |
| **Frequency** | Annual statutory audit (Q1 following fiscal year-end); quarterly interim review (if applicable) |
| **Volume** | 1 annual audit covering 5 entities + consolidated; quarterly reviews if required |
| **Owner** | Controller |
| **Participants** | Controller, CFO, Cost Accountant, AP Supervisor, AR Accountant, Treasury Analyst, Tax Accountant, Internal Audit, IT Manager, external auditors (CPA firm) |

### Background

As a Philippine corporation with 5 legal entities requiring consolidated financial statements, BuildRight must undergo an annual external audit by a SEC-accredited CPA firm per the Philippine Securities and Exchange Commission (SEC) requirements and the Philippine Financial Reporting Standards (PFRS). W77 (BIR Tax Audit Response) covers tax-specific audits by the Bureau of Internal Revenue. This workflow covers the broader external financial statement audit, which is a significant annual undertaking involving 5 entities, 200+ locations, and complex intercompany transactions. The external audit validates the financial statements that investors, lenders, regulators, and management rely upon.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Audit planning — engagement letter**: (a) CFO and Controller review and sign annual audit engagement letter from external auditors (typically signed Q4 for the following year's audit); (b) agree on audit scope (5 entities + consolidated), timeline (fieldwork in February, report by March–April), materiality thresholds, and audit fee; (c) Controller coordinates audit planning meeting with external audit partner and manager | CFO / Controller | CEO | 2 hours |
| 2 | **Pre-audit preparation** (January — after W9b year-end close): Controller assigns preparation tasks across Finance team: (a) **AP Supervisor**: finalize AP aging reconciliation, open GRNI analysis, vendor confirmation letters (send to top 50 vendors requesting confirmation of balances); (b) **AR Accountant**: finalize AR aging, send customer confirmation letters (top 50 trade/corporate accounts), prepare bad debt provision analysis (W81); (c) **Treasury Analyst**: complete all bank reconciliations (W89) through December 31, prepare bank confirmation requests (send to all 4 banks for all 25 accounts); (d) **Tax Accountant**: prepare annual tax reconciliation (W90), reconcile tax liability accounts, compile all BIR filings for the year; (e) **Cost Accountant**: prepare inventory valuation report (W9a.6), inventory reserve analysis (obsolescence, NRV), fixed asset register with depreciation schedule (W39); (f) **IT Manager**: prepare IT general controls documentation (access controls, change management, backup procedures per W48/W55) | Controller | CFO | 8 hours |
| 3 | **PBC (Prepared by Client) list fulfillment**: External auditors provide a PBC list of documents and schedules required for the audit; Controller assigns each item with deadline (typically 1–2 weeks before fieldwork start): (a) trial balance per entity, (b) consolidated elimination entries (W14), (c) intercompany reconciliation (W14.4–5), (d) revenue and expense analysis by category, (e) journal entry listing with supporting documentation for all manual JEs > materiality, (f) bank reconciliation reports (W89), (g) inventory count documentation from W42 annual physical inventory, (h) capex additions and disposals (W21, W39), (i) insurance schedule (W59), (j) related party transactions schedule, (k) contingent liabilities (pending litigation, tax assessments from W77), (l) subsequent events review (transactions after year-end through audit report date) | Finance Team | Controller | 20–30 hours total |
| 4 | **External audit fieldwork** (February — typically 2–3 weeks on-site at HQ): (a) **Opening meeting**: Controller, CFO, and external audit team agree on fieldwork schedule, key contact persons per area, and logistics; (b) **Substantive testing**: auditors test revenue (POS transaction sampling — W5b), purchases (PO and invoice sampling — W2/W7), inventory (observe physical count — W42, or rely on count documentation), bank balances (confirmations from W89), fixed assets (physical verification of additions), intercompany (W14 reconciliation), payroll (W10 sampling); (c) **Internal controls testing**: auditors test key controls — PO approval (W2.5–6), 3-way match (W7.2–3), credit approval (W24), physical security (W71), IT access controls (W48); (d) **Entity walkthroughs**: auditors may visit 1–2 stores and 1 DC for physical observation; Controller coordinates visits with Store Managers and DC Supervisors | External Auditors / Controller | CFO | 2–3 weeks |
| 5 | **Audit queries and information requests** (throughout fieldwork): (a) External auditors issue queries and additional information requests as testing proceeds; Controller triages and routes to appropriate Finance team member; (b) target response time: 2 business days for standard queries, 5 business days for complex analysis; (c) weekly status meetings between Controller and audit manager to track open queries and issues | Controller / Finance Team | CFO | Ongoing during fieldwork |
| 6 | **Draft financial statements review**: (a) External auditors present draft audited financial statements (per entity and consolidated) to Controller and CFO; (b) Controller reviews for accuracy vs. internal records, proper PFRS/IFRS presentation, and adequate disclosure; (c) Controller provides comments and corrections within 1 week | Controller / CFO | CEO | 4–6 hours |
| 7 | **Audit adjustments and passed adjustments**: (a) **Proposed audit adjustments**: external auditors propose correcting entries for any misstatements found during testing; Controller reviews and posts agreed adjustments per W9b year-end close; (b) **Passed adjustments (unadjusted differences)**: misstatements below materiality that auditors note but do not require correction; Controller logs passed adjustments in audit summary for future reference and potential cumulative materiality assessment | Controller | CFO | 2–4 hours |
| 8 | **Exit meeting and management letter**: (a) External auditors conduct exit meeting with Controller, CFO, and CEO to present audit findings, significant observations, and recommendations; (b) external auditors issue management letter with internal control recommendations (e.g., segregation of duties improvements, system access issues, process inefficiencies); (c) Controller prepares management response and action plan for each recommendation with deadlines and responsible persons; (d) management response reviewed and approved by CFO | Controller / CFO / CEO | CEO | 2 hours |
| 9 | **Audit report issuance**: External auditors issue audit opinion and audited financial statements; Controller files with SEC per regulatory deadline (typically within 120 days of fiscal year-end for corporations); files with BIR as part of 1702RT annual return (W90) | Controller / External Auditors | CFO | 2 hours |
| 10 | **Management letter follow-up**: Controller tracks implementation of management letter recommendations: (a) assigns each recommendation to responsible person, (b) tracks implementation progress quarterly, (c) reports status to CFO and Audit Committee, (d) unresolved items > 6 months escalated to CEO; external auditors review prior year recommendations in next year's audit | Controller | CFO | Ongoing |

### System Touchpoints
- Audit document management: engagement letter, PBC list, management letter, audit report stored per entity with DOC-001 document management (W95.1, 3, 8–9)
- Financial data extraction for PBC: trial balance, journal entries, aging reports, elimination entries per entity (W95.3)
- Audit trail: all transactions, approvals, and changes accessible for auditor review with full audit trail per NFR-007 (W95.4)
- Fixed asset register with depreciation schedule for auditor verification (W95.3e)
- Inventory valuation and reserve analysis for auditor review (W95.3e)
- Intercompany reconciliation and elimination documentation (W95.3c)
- Bank reconciliation reports and bank confirmation coordination (W95.3c)
- Management letter recommendation tracker with status and deadlines (W95.10)
- Integration with W7 (AP — vendor confirmations, 3-way match testing), W8 (AR — customer confirmations, bad debt analysis), W9 (financial close — audited financial statements source), W10 (payroll — compensation testing), W14 (IC — intercompany reconciliation and elimination testing), W21 (capex — addition verification), W30 (treasury — bank balance confirmation), W39 (fixed assets — physical verification), W42 (physical inventory — count documentation), W48 (IT — IT general controls), W55 (DR — business continuity documentation), W77 (BIR audit — separate from external audit but may share data), W89 (bank reconciliation — primary audit evidence for cash), W90 (tax — tax reconciliation and filing verification), W92 (inventory adjustments — control testing)

### Staffing Implication
- **Controller**: primary audit liaison; adds ~40–60 hours during Jan–March for audit preparation and coordination. This is the Controller's busiest period; other duties deprioritized during fieldwork.
- **Finance Team** (AP Supervisor, AR Accountant, Treasury Analyst, Tax Accountant, Cost Accountant): each adds ~10–20 hours for PBC preparation and query response during fieldwork. Managed through workload planning during Jan–Feb.
- **Internal Audit**: provides coordination support and observes external audit process; adds ~8–10 hours. Absorbed.
- **Store Managers / DC Supervisors**: 1–2 store/DC visits per year for physical observation; minimal time impact. Absorbed.
- **No incremental headcount.** External audit fee budgeted as professional fees in W26 annual budget.

---


## W114. Sustainability & Environmental Compliance Reporting

| Field | Detail |
|---|---|
| **Trigger** | Annual sustainability reporting cycle; quarterly environmental compliance review; DENR reporting deadline; or ad-hoc triggered by environmental incident or regulatory inquiry |
| **Frequency** | Annual sustainability report; quarterly environmental metrics review; monthly waste and emissions tracking |
| **Volume** | 200 stores + 5 DCs + HQ; environmental data collected per location across waste, energy, water, and emissions categories |
| **Owner** | Facilities Manager (data collection); VP Legal & Compliance (regulatory reporting) |
| **Participants** | Facilities Manager, VP Legal & Compliance, Regulatory Officer, Store Managers, DC Managers, Finance Manager, CSR Coordinator |

### Background

BuildRight operates 200 stores and 5 DCs across the Philippine archipelago. Environmental compliance is governed by the Philippine Clean Air Act (RA 8749), Clean Water Act (RA 9275), Ecological Solid Waste Management Act (RA 9003), Toxic Substances and Hazardous and Nuclear Wastes Control Act (RA 6969), and the Philippine Strategy for Sustainable Development. W82 covers hazardous waste disposal tracking and DENR compliance specifically. W111 covers energy and utility consumption management. However, there is no unified workflow for: (a) tracking environmental metrics beyond hazardous waste (solid waste diversion rate, water consumption, carbon emissions), (b) compiling sustainability data into regulatory reports and voluntary disclosures, (c) setting and monitoring environmental reduction targets, and (d) coordinating environmental compliance across 200+ locations. This workflow creates that comprehensive sustainability governance layer.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Monthly environmental data collection**: System aggregates environmental data per location from multiple sources: (a) **Waste**: hazardous waste manifests (W82), general solid waste collection volumes (from waste hauler invoices per W7c), recyclable materials recovered (cardboard bales, plastic, metal — from recycling vendor records); (b) **Energy**: electricity consumption (W111 utility data), diesel consumption (fleet per W52, generators per W47); (c) **Water**: water consumption per location (W111 utility data); (d) **Emissions**: estimated CO₂ from electricity (using DU emission factor) and diesel (using DEF emission factor) — system calculates carbon footprint estimate per location | System / Facilities Manager | VP Legal & Compliance | Automated (aggregation) + 2 hours/month (verification) |
| 2 | **Quarterly environmental metrics review**: Facilities Manager reviews quarterly environmental dashboard: (a) **Solid waste diversion rate**: recycled waste ÷ total waste — target: ≥ 30%, (b) **Energy intensity**: kWh per sqm per month — target: reduce 2% year-over-year, (c) **Water intensity**: cubic meters per sqm per month — target: reduce 2% year-over-year, (d) **Carbon intensity**: tonnes CO₂ per PHP million revenue — target: reduce 3% year-over-year, (e) **Hazardous waste compliance**: 100% of hazardous waste disposed via DENR-accredited transporters with manifest tracking (W82), (f) per-location outliers flagged for investigation and corrective action | Facilities Manager | VP Legal & Compliance | 2 hours/quarter |
| 3 | **Environmental compliance calendar**: Regulatory Officer maintains environmental compliance calendar per location: (a) **DENR hazardous waste generator registration** renewal per location (W82), (b) **DENR quarterly hazardous waste disposal report** per location, (c) **LGU environmental compliance certificate** renewal (for stores with Environmental Compliance Certificate requirement), (d) **Wastewater discharge permit** (for locations with discharge to waterways — paint/chemical areas), (e) **Air emissions permit** (for DCs with backup generators above threshold); system alerts Regulatory Officer 60 days before each deadline; expired permits escalated to VP Legal & Compliance | Regulatory Officer | VP Legal & Compliance | 2 hours/quarter (calendar maintenance) |
| 4 | **Annual environmental reduction targets**: Facilities Manager and VP Legal & Compliance set annual environmental targets aligned with corporate sustainability strategy: (a) carbon emission reduction target (% year-over-year), (b) energy efficiency improvement target (% reduction in kWh/sqm), (c) water consumption reduction target, (d) solid waste diversion rate improvement, (e) hazardous waste volume reduction; targets approved by CEO; integrated into W26 annual budget as operational KPIs | Facilities Manager / VP Legal & Compliance | CEO | Annual (4 hours) |
| 5 | **Annual sustainability report compilation**: CSR Coordinator compiles annual sustainability data for: (a) voluntary sustainability disclosure (if BuildRight pursues GRI or SASB reporting framework), (b) DENR annual environmental performance report (if required), (c) SEC sustainability reporting requirements (SEC Memorandum Circular No. 4, Series of 2019 requires publicly listed companies to submit sustainability reports — BuildRight is theoretical but prepares as if applicable), (d) internal stakeholder communication (sustainability section of annual report); Facilities Manager provides environmental metrics; Finance Manager provides utility spend data; VP Legal & Compliance reviews regulatory compliance status | CSR Coordinator / Facilities Manager | VP Legal & Compliance | Annual (20 hours) |
| 6 | **Environmental incident response**: If environmental incident occurs (chemical spill at paint mixing station, hazardous waste container breach, wastewater discharge violation): (a) Store Manager / DC Supervisor initiates immediate containment per W82 emergency procedures; (b) Regulatory Officer notified within 24 hours; (c) Regulatory Officer assesses reporting requirement — incidents exceeding threshold require DENR notification within 24–72 hours per RA 6969; (d) Facilities Manager coordinates remediation; (e) system logs incident with location, date, type, quantity, response actions, and remediation cost; (f) incident included in quarterly metrics review and annual sustainability report | Store Manager / DC Supervisor / Regulatory Officer | VP Legal & Compliance | Per incident |
| 7 | **Vendor environmental compliance**: Buyer evaluates vendor environmental practices for high-risk categories (paint, chemicals, treated lumber, cement): (a) during vendor onboarding (W36), check for environmental compliance certifications (ISO 14001, DENR compliance for Philippine manufacturers); (b) for import vendors: check compliance with applicable environmental standards in country of manufacture; (c) annual review of vendor environmental compliance as part of W44 vendor scorecard; (d) vendors with environmental violations flagged for CAPA per W110 or vendor exit per W44 termination | Buyer / Regulatory Officer | VP Merchandising | Absorbed within W36/W44 |

### System Touchpoints
- Monthly environmental data aggregation from utility bills (W111), waste manifests (W82), fleet records (W52), and generator maintenance records (W47) (W114.1)
- Carbon footprint estimation calculator using DU emission factors for electricity and DEF factors for diesel (W114.1)
- Quarterly environmental dashboard: waste diversion, energy intensity, water intensity, carbon intensity, hazardous waste compliance (W114.2)
- Environmental compliance calendar per location with permit tracking and renewal alerting (W114.3)
- Annual environmental reduction target configuration with year-over-year tracking (W114.4)
- Environmental incident logging with DENR reporting workflow (W114.6)
- Integration with W47 (facility maintenance — generator emissions, HVAC efficiency), W52 (fleet — fuel consumption and emissions), W60 (emergency procurement — environmental incident supplies), W82 (hazardous waste — manifests and DENR compliance), W111 (energy and utility — consumption data), W26 (annual budget — environmental targets as KPIs)

### Staffing Implication
- **Facilities Manager**: adds ~2 hours/month for data verification + ~2 hours/quarter for metrics review + ~4 hours/year for target setting = ~40 hours/year. Absorbed within existing Facilities Manager role (formalized in W111).
- **Regulatory Officer**: adds ~2 hours/quarter for environmental compliance calendar maintenance. Absorbed within existing Regulatory Officer role (formalized in W54).
- **CSR Coordinator** (within Marketing team): adds ~20 hours/year for annual sustainability report compilation. Absorbed.
- **No incremental headcount.**

---

---

## W157. E-waste Collection & Circular Economy Operations

| Field | Detail |
|---|---|
| **Trigger** | Customer brings end-of-life products (batteries, old tools, appliances) to store collection points |
| **Frequency** | Ongoing |
| **Volume** | Covers all 200 stores |
| **Owner** | Sustainability Manager |
| **Participants** | Store Staff, Logistics, Accredited Recyclers, DENR |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Collection**: Customer drops off items at designated in-store bins; Store Staff record weight/type in system | Store Staff | Store Manager | Ongoing |
| 2 | **Incentive**: System issues "Green Points" to customer loyalty account (W17) for participating | System | — | Real-time |
| 3 | **Consolidation**: DC delivery trucks backhaul e-waste to the nearest Hub (W4) | Logistics | — | Weekly |
| 4 | **Certified Disposal**: Accredited 3rd-party recycler collects waste from DC; provide Certificate of Treatment | Recycler | Sustainability Mgr | Monthly |
| 5 | **Impact Reporting**: Track total tonnage diverted from landfills for ESG report (W114) | Sustainability Mgr | CMO | Monthly |

---

## W158. Business Continuity Drill & Disaster Recovery Testing

| Field | Detail |
|---|---|
| **Trigger** | Annual BC/DR schedule or major system change |
| **Frequency** | Semi-annual for IT DR; Annual for full BC drill |
| **Volume** | Covers all 5 legal entities and critical sites (HQ, DCs, 200 stores) |
| **Owner** | VP Legal & Compliance |
| **Participants** | IT Infrastructure Team, DC Managers, Store Managers, HR, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Scenario Planning**: Define the drill scenario (e.g., total network outage, major typhoon landfall in Visayas, fire at DC3) | Compliance Officer | VP Legal & Compliance | 4 hours |
| 2 | **IT Disaster Recovery Test**: Execute "failover" to backup data center; verify data integrity and POS transaction synchronization (W55) | IT Manager | CIO | 8-12 hours |
| 3 | **Communication Drill**: Activate emergency notification tree; verify response times from Store Managers and DC Supervisors | HR Manager | CHRO | 2 hours |
| 4 | **Operational Workarounds**: Stores practice manual sales recording (W5g) and manual inventory logging for 4 hours; DCs practice manual load manifest creation | Store Manager / DC Supervisor | COO | 4 hours |
| 5 | **Post-Drill Review**: Document gaps, system performance issues, and communication bottlenecks; update Business Continuity Plan (BCP) | Compliance Officer | VP Legal & Compliance | 1 day |
| 6 | **Board Reporting**: Present DR/BC readiness status and improvement plan to the Board of Directors | VP Legal & Compliance | CEO | Quarterly |

---

## W167. Store & DC Recycling Program (Circular Economy)

| Field | Detail |
|---|---|
| **Trigger** | Accumulation of secondary packaging (cartons, plastics, broken pallets) |
| **Frequency** | Weekly |
| **Owner** | DC Supervisor / Store Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Store/DC Associates segregate waste: Carton, Stretch Film (Plastic), Wood (Pallets), Scrap Metal | Associates | — | Ongoing |
| 2 | Materials baled (for carton/plastic) or stacked (for pallets) at DC/Store dock | Stock Associate | — | 30 min/day |
| 3 | Logistics collects recyclables from Stores via **Reverse Logistics** trucks returning to DC | Logistics Team | — | Weekly |
| 4 | DC consolidates recyclables; sells to accredited recycling partners | DC Supervisor | Supply Chain Mgr | Monthly |
| 5 | System records "Recycling Revenue" and weight diverted from landfill; feeds into W114 Sustainability Report | DC Supervisor | — | 15 min |

## W185. Product Liability & Consumer Safety Incident Management

| Field | Detail |
|---|---|
| **Trigger** | Report of property damage, personal injury, or safety hazard related to a sold product |
| **Frequency** | As occurred |
| **Volume** | < 10 incidents/month |
| **Owner** | Legal & Compliance Manager |
| **Participants** | Customer Service Manager, Risk Manager, Store Manager, Vendor (Supplier) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer Service Rep receives report; records incident details, product SKU, batch/lot (if available), and photos in ERP | CS Rep | CS Manager | 30 min |
| 2 | System flags product; if multiple reports occur for same SKU, alerts Merchandising for potential stop-sell | System | Merchandising Mgr | Real-time |
| 3 | Store Manager/Risk Manager conducts physical inspection of incident site or product remains | Risk Manager | Legal Manager | 4 hours |
| 4 | Legal Manager reviews documentation; determines liability and coordinates with insurance (W59) | Legal Manager | CFO | 2 hours |
| 5 | Formal notice sent to Vendor; request for investigation and indemnity | Legal Manager | — | 1 hour |
| 6 | Coordinate with DTI (Dept of Trade and Industry) if mandatory product recall is triggered (W29) | Legal Manager | — | 2 hours |
| 7 | Resolve claim: settlement, replacement, or legal defense | Legal Manager | CFO | Ongoing |
| 8 | Document "Lessons Learned"; feed into Vendor Performance Review (W44) | Risk Manager | — | 1 hour |

### System Touchpoints
- Incident Management Portal with photo/document upload (W185.1)
- Automated alert for "Product Hazard Threshold" (W185.2)
- Integration with SKU Master (Stop-Sell flag) (W185.2)
- Link to Insurance Claims workflow (W59) (W185.4)
- Link to Product Recall (W29) and Vendor Performance (W44) (W185.6, W185.8)

---

## W207. Store-Level Security Camera (CCTV) Audit & LP Integration

| Field | Detail |
|---|---|
| **Trigger** | Scheduled audit or suspected internal/external theft incident |
| **Frequency** | Weekly audits of high-risk transactions |
| **Volume** | Covers all 200 stores and 5 DCs |
| **Owner** | Loss Prevention (LP) Manager |
| **Participants** | LP Analyst, Store Manager, IT (for system access) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Exception Identification**: System identifies high-risk POS transactions (e.g., voids, high-value returns, employee discounts) via automated exception reports (W37) | System | LP Analyst | Automated |
| 2 | **CCTV Reconciliation**: LP Analyst retrieves CCTV footage synced with POS transaction timestamps; verifies physical action matches system record | LP Analyst | LP Manager | 30 min/event |
| 3 | **Discrepancy Logging**: If "phantom return" or unrecorded sale discovered, log as a "Confirmed Incident" in LP module | LP Analyst | LP Manager | 15 min |
| 4 | **Investigation**: Confront staff or review external footage for identification; coordinate with HR for disciplinary action (W79) | LP Manager | CHRO | 2-4 hours |
| 5 | **System Update**: Write off confirmed theft inventory (W37.6); update shrinkage metrics in P&L (W102) | Finance | LP Manager | 10 min |
| 6 | **Security Hardening**: Adjust camera angles or POS procedures based on audit findings | IT / Store Manager | LP Manager | 1 hour |

---

## W209. Barangay & Local Community Relationship Management

| Field | Detail |
|---|---|
| **Trigger** | Store opening (W16); annual local permit cycle (W54); or community grievance |
| **Frequency** | Quarterly check-ins; or as needed |
| **Volume** | One relationship per store/DC location (205+ barangays) |
| **Owner** | Store Manager / DC Manager |
| **Participants** | Barangay Captain, LGU Officials, Legal Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Stakeholder Mapping**: Identify key local officials (Barangay Captain, LGU licensing office, local police) | Store Manager | Legal Manager | 2 hours |
| 2 | **Permit Coordination**: Liaise with Barangay for "Barangay Clearance" required for LGU Business Permit renewal (W54) | Store Manager | Regulatory Officer | 4 hours/year |
| 3 | **Local Employment**: Coordinate with Barangay for local hiring requirements/quotas as part of social responsibility and LGU agreements | HR / Store Manager | — | Monthly |
| 4 | **Community Support**: Manage local CSR requests (e.g., school repair donations, neighborhood cleaning) via CSR Program Execution (W135) | Store Manager | CSR Coordinator | 1 hour |
| 5 | **Dispute Resolution**: Address community complaints (e.g., truck noise, parking congestion) via direct dialogue; document resolution in Legal Case Management (W125) | Store Manager | Legal Manager | Varies |
| 6 | **Annual Appreciation**: Conduct "Community Day" or stakeholder briefing on store performance and local impact | Store Manager | — | 4 hours/year |

---

## W216. BIR CAS (Computerized Accounting System) Compliance Audit

| Field | Detail |
|---|---|
| **Trigger** | Periodic compliance review; or BIR post-evaluation/inspection of the ERP system |
| **Frequency** | Annual internal review; or as scheduled by BIR |
| **Volume** | Covers all 5 legal entities and centralized accounting |
| **Owner** | VP Legal & Compliance / CIO |
| **Participants** | Tax Manager, IT Manager, External Audit, BIR Officers |

### Background

Philippine regulations require companies using a Computerized Accounting System (CAS) to maintain a Permit to Use (PTU) and adhere to strict audit trail, reporting, and e-invoicing standards.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **System Documentation Update**: Maintain up-to-date system architecture, data flow diagrams, and functional descriptions for BIR submission | IT Manager | CIO | 4 hours |
| 2 | **Audit Trail Verification**: Verify that all transactions (GL, AP, AR, Inventory) have immutable audit trails (who, when, what, previous value) | IT Manager | Internal Audit | 2 hours |
| 3 | **Standard Report Generation**: Generate and validate "Books of Accounts" in BIR-required formats (General Journal, Sales Journal, Purchase Journal, etc.) | Tax Manager | Controller | 4 hours |
| 4 | **E-Invoicing Compliance**: Verify that system-generated Invoices and Official Receipts (OR) comply with BIR serial numbering and mandatory field requirements | Tax Manager | VP Compliance | 2 hours |
| 5 | **CAS Permit Review**: Verify that any significant system changes (W132) have been reported to the BIR as "System Enhancements" per regulation | VP Compliance | — | 1 hour |
| 6 | **Mock Inspection**: Conduct mock BIR walk-through: demonstrate system navigation, report generation, and data archival for BIR officers | Tax Manager | CIO | 1 day |
| 7 | **Archival & Retention**: Verify 7-year data retention and accessibility of archived accounting data (W15.3) | IT Manager | — | 1 hour |

### System Touchpoints
- BIR-compliant reporting module (Books of Accounts)
- Immutable audit trail logs
- Sequential and controlled serial numbering for invoices/receipts
- Data retention and archival system (IT infrastructure)



