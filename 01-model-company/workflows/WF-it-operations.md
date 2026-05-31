# IT Operations Workflows

> Helpdesk, data privacy breach response, disaster recovery, and data migration/parallel-run testing.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W48. IT Operations & Helpdesk Support](#it-operations-helpdesk-support)
- [W53. Data Privacy Breach Response](#data-privacy-breach-response)
- [W55. IT Disaster Recovery & System Failover](#it-disaster-recovery-system-failover)
- [W73. Data Migration Validation & Parallel-Run Testing](#data-migration-validation-parallel-run-testing)
- [W113. Business Intelligence & Data Governance](#business-intelligence-data-governance)
- [W131. IT Asset Lifecycle Management](#it-asset-lifecycle-management)
- [W132. Software Development & Change Management](#software-development--change-management)
- [W152. Employee IT Provisioning & Access Lifecycle Management](#employee-it-provisioning--access-lifecycle-management)

---

## W48. IT Operations & Helpdesk Support

| Field | Detail |
|---|---|
| **Trigger** | User reports issue (phone, email, self-service portal); system generates automated alert; scheduled change window |
| **Frequency** | Continuous; ~800–1,200 support tickets/month across all locations |
| **Volume** | ~8,050 users; 1,000 POS terminals; 5 WMS systems; ~500 RF devices; 200+ network locations |
| **Owner** | IT Helpdesk Lead |
| **Participants** | IT Helpdesk, IT Infrastructure, IT Applications, end users, external vendors |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | User contacts IT Helpdesk via phone, email, or self-service portal; describes issue with system, hardware, network, or access | End User | — | 2 min |
| 2 | Helpdesk Agent creates support ticket: user, location, device, issue category, severity (see matrix below), description | Helpdesk Agent | IT Helpdesk Lead | 3 min |
| 3 | System auto-routes ticket based on category: (a) POS/retail → Retail IT support queue, (b) network/connectivity → Infrastructure queue, (c) ERP/application → Applications queue, (d) hardware → Hardware support queue, (e) access/permissions → Security queue | System | — | Automated |
| 4 | **Tier 1 — Remote resolution**: Helpdesk Agent attempts to resolve remotely (password reset, configuration fix, user guidance, system restart) | Helpdesk Agent | IT Helpdesk Lead | 5–15 min |
| 5 | If Tier 1 resolves: ticket closed with resolution code; user confirms | Helpdesk Agent | — | 2 min |
| 6 | If Tier 1 unresolved: ticket escalated to Tier 2 (specialist) with diagnostic notes; SLA timer restarts per severity | Helpdesk Agent | IT Helpdesk Lead | 2 min |
| 7 | **Tier 2 — Specialist resolution**: IT specialist investigates; may require remote session, configuration change, or system-level fix | IT Specialist | IT Helpdesk Lead | 15–60 min |
| 8 | If Tier 2 requires on-site presence (hardware failure, network cabling, POS terminal replacement): ticket assigned to IT Field Support with scheduled site visit | IT Specialist | CIO | Scheduling: 5 min |
| 9 | **Tier 3 — Vendor / escalation**: if issue requires vendor support (POS software bug, ERP vendor support, hardware warranty claim), IT engages vendor; tracks vendor response SLA | IT Specialist / CIO | CIO | Vendor-dependent |
| 10 | Resolution confirmed by user; ticket closed; system logs resolution time, root cause category, and recurring issue flag | Helpdesk Agent | IT Helpdesk Lead | 2 min |
| 11 | Monthly: IT Helpdesk Lead reviews ticket analytics: volume by category, resolution rate by tier, SLA compliance, mean time to resolution, top recurring issues per location | IT Helpdesk Lead | CIO | 2 hours/month |

### Severity & SLA Matrix

| Severity | Definition | Examples | Response SLA | Resolution SLA |
|---|---|---|---|---|
| **P1 — Critical** | System down affecting revenue or multiple users | All POS terminals down at a store, ERP system inaccessible, DC WMS failure | 15 min | 4 hours |
| **P2 — High** | Major function impaired but workaround exists | Single POS terminal down, ecommerce integration failure, reporting module error | 30 min | 8 hours |
| **P3 — Medium** | Non-critical issue affecting productivity | Printer malfunction, slow report generation, single user access issue | 2 hours | 24 hours |
| **P4 — Low** | Minor issue or enhancement request | Cosmetics, feature requests, non-urgent how-to questions | 8 hours | 72 hours |

### Change Management

| # | Activity | Role (R) | Role (A) | Frequency |
|---|---|---|---|---|
| 1 | IT team member submits change request: description, affected systems, risk assessment, rollback plan, planned window | IT Team Member | IT Helpdesk Lead | As needed (~20–30 changes/month) |
| 2 | IT Helpdesk Lead reviews and classifies: (a) standard change (pre-approved, low risk — e.g., password policy update), (b) normal change (requires review and approval — e.g., POS software patch), (c) emergency change (unplanned, critical fix — e.g., security vulnerability patch) | IT Helpdesk Lead | CIO | 10 min/change |
| 3 | Normal changes: CIO approves; emergency changes: CIO verbal approval with post-hoc documentation; standard changes: auto-approved per catalog | CIO | — | 5–15 min/change |
| 4 | Change executed during maintenance window (typically Tuesday/Thursday 22:00–02:00 or Sunday 00:00–04:00 to avoid peak hours) | IT Infrastructure | CIO | Per change |
| 5 | Post-change verification: IT confirms system health; Helpdesk monitors for related ticket spikes in next 24 hours | IT Team | IT Helpdesk Lead | 15 min/change |

### System Touchpoints
- IT ticket management: create, route, escalate, resolve, close with full audit trail (W48.2–10)
- Auto-routing by issue category to specialist queues (W48.3)
- SLA timer per severity level with auto-escalation at 75% of SLA threshold (W48.4–9)
- Remote desktop / diagnostic tool integration (W48.4, 7)
- Knowledge base / self-service portal for common issues (W48.1)
- Change request workflow with classification and approval (W48 change management)
- Maintenance window scheduling (W48 change 4)
- Ticket analytics dashboard: volume, SLA compliance, MTTR, top issues by location (W48.11)
- SLA breach escalation protocol: (a) single P1 SLA miss (resolution > 4 hours): IT Helpdesk Lead conducts immediate root cause analysis and documents corrective action; (b) 2 consecutive P1 SLA misses on same issue category: Helpdesk Lead escalates to CIO with remediation plan within 24 hours; CIO reviews staffing, tooling, or vendor support adequacy; (c) 3 or more P1 SLA misses within 30 days (any category): CIO presents incident review to CEO with systemic improvement plan (may include additional headcount, vendor escalation, or infrastructure investment); (d) P2/P3 SLA misses trending > 20% breach rate for 2 consecutive months: Helpdesk Lead initiates category-specific improvement (process change, training, or automation); (e) all SLA breaches tracked in monthly ticket analytics dashboard with trend analysis and root cause classification; SLA performance included in IT team's quarterly performance review (W48)
- IT asset tracking: system maintains asset register for all IT equipment (POS terminals, RF devices, servers, networking equipment, laptops, tablets) with location assignment, warranty status, maintenance history, and lifecycle status; supports IT asset planning and budgeting (cross-reference W21 for capex, W39 for disposal)
- Integration with W5g (offline POS recovery), W16 (new store IT setup), W43 (employee separation — account deactivation)

### Staffing Implication
- **4–5 Helpdesk Agents (Tier 1)**: handle ~800–1,200 tickets/month ÷ 20 working days = ~40–60/day. At ~10 min average per ticket = ~7–10 hours/day. With shifts and coverage, 4–5 agents needed.
- **3–4 IT Specialists (Tier 2)**: Application support, infrastructure, retail IT, security. Specialists handle ~30% of tickets that Tier 1 cannot resolve = ~240–360/month.
- **1–2 IT Field Support**: physical site visits for hardware issues across 200 stores + 5 DCs. Estimated 50–80 on-site visits/month across the Philippines. With travel time, 1–2 dedicated field staff with regional coverage.
- **1 IT Helpdesk Lead**: manages helpdesk operations, SLA compliance, change management.
- **Total IT**: recommend expanding IT team from ~25 to ~28–30 to accommodate dedicated helpdesk function. Current ~25 includes infrastructure, applications, data, security, and BI but does not explicitly allocate helpdesk headcount.

---



---

## W53. Data Privacy Breach Response

| Field | Detail |
|---|---|
| **Trigger** | Suspected or confirmed breach of personal data (customer, employee, or vendor data) as defined by RA 10173 (Data Privacy Act of 2012) |
| **Frequency** | Rare; estimated 0–2 incidents/year requiring formal breach response |
| **Volume** | Variable — from a single record exposed to bulk data extraction |
| **Owner** | Data Protection Officer (DPO) |
| **Participants** | DPO, CIO, IT Security, Legal, affected department head, NPC (National Privacy Commission), affected data subjects |

### Background

Under RA 10173 and its Implementing Rules and Regulations (IRR), BuildRight Depot (as a PIC — Personal Information Controller) must: (a) notify the National Privacy Commission within 72 hours of discovering a breach involving sensitive personal information affecting 100+ data subjects, (b) notify affected data subjects within a reasonable time, (c) document all breaches regardless of size. BuildRight holds personal data for ~600,000 loyalty members, ~5,200 trade accounts, ~200 corporate accounts, ~8,050 employees, and ~1,000 vendors.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Breach discovered or suspected: IT Security alerts (automated monitoring), employee report, third-party notification, or customer complaint about unauthorized access | IT Security / Any employee | CIO | Immediate |
| 2 | CIO and DPO assess breach severity: (a) scope — how many records, what data types (name, contact, financial, government ID), (b) vector — how the breach occurred (external attack, insider, misconfiguration, lost device, vendor breach), (c) containment status — is the breach ongoing or contained | CIO + DPO | CEO | 1–2 hours |
| 3 | **Containment**: IT Security takes immediate action to stop the breach: isolate affected systems, revoke compromised credentials, block unauthorized access, preserve forensic evidence | IT Security | CIO | As needed |
| 4 | DPO classifies the breach per NPC guidelines: (a) **Notifiable breach** — involves sensitive personal info, affects 100+ data subjects, or involves significant harm; (b) **Non-notifiable breach** — limited scope, no sensitive data, quickly contained | DPO | CEO | 30 min |
| 5 | If notifiable: DPO prepares NPC notification within 72 hours: nature of breach, data subjects affected, data types exposed, measures taken, remedial actions planned; submits via NPC online portal or prescribed form | DPO | CEO | 2–4 hours |
| 6 | DPO prepares data subject notification: clear description of breach in plain language, data exposed, potential harm, mitigation steps data subjects should take, BuildRight contact for inquiries; notification via email, SMS, or website notice depending on breach scope | DPO + Legal | CMO | 2–4 hours |
| 7 | CIO directs forensic investigation: determine root cause, full scope, and whether any data was exfiltrated; engage external forensic firm if needed; preserve all logs and evidence | CIO | CEO | 1–5 days |
| 8 | Legal assesses regulatory and litigation risk: review NPC requirements, evaluate liability exposure, prepare responses to potential regulatory inquiry or customer claims | Legal | CEO | As needed |
| 9 | Affected department head implements immediate operational safeguards: e.g., if payment data breached — reset payment credentials, work with payment gateways; if employee data breached — offer credit monitoring | Dept. Head | CEO | As needed |
| 10 | DPO documents full incident in breach register: timeline, root cause, scope, notifications sent, remedial actions, resolution date; breach register retained for 5 years per NPC requirements | DPO | CEO | 2 hours |
| 11 | Post-incident: CIO and DPO conduct lessons-learned review; update security controls, access policies, and data handling procedures; implement preventive measures; schedule follow-up assessment in 30 days | CIO + DPO | CEO | 2 hours |
| 12 | Quarterly: DPO reviews breach register with CEO and Internal Audit; analyzes trends; reports aggregate breach statistics in annual privacy impact assessment | DPO | CEO | 30 min/quarter |

### System Touchpoints
- Breach register in system: incident ID, discovery date/time, classification, scope, root cause, notifications, resolution status (W53.10)
- Data access audit trail: system maintains immutable log of all access to personal data (customer records, employee records) with user ID, timestamp, and action; forensic extraction capability for breach investigation (W53.7)
- Data subject notification workflow: system generates notification list of affected data subjects from breach scope analysis; bulk email/SMS capability for notification delivery (W53.6)
- Role-based access enforcement: system enforces minimum-necessary access to personal data; access revocation capability for containment (W53.3)
- Data encryption at rest and in transit: customer and employee data encrypted in database and during transmission; encryption key management with emergency rotation capability (W53.3)
- Data Subject Access Request (DSAR) full lifecycle per RA 10173: (a) **access**: DPO acknowledges DSAR within 72 hours; system generates data package containing all personal data held for the requesting data subject (loyalty profile, transaction history, AR account data, complaint history) in machine-readable format (JSON or CSV) within 30 days; DPO reviews package for third-party data exclusion before release; (b) **rectification**: data subject requests correction of inaccurate personal data; DPO or AR Clerk updates record in system with change log; (c) **erasure / right to be forgotten**: upon verified request, DPO initiates erasure workflow — system anonymizes personal data in active records (replace name, email, phone with "ANONYMIZED-[hash]") while preserving transaction records for BIR 7-year retention requirement (transaction amounts, dates, VAT, and payment methods retained; personal identifiers removed); system flags anonymized records to prevent re-identification; for loyalty accounts with unredeemed points, DPO offers final redemption before erasure; erasure logged with request date, data subject verification method, scope of erasure, and DPO approval; (d) **data portability**: system exports data subject's personal data in structured, machine-readable format (JSON) via DPO-approved download link with 72-hour expiry; (e) **consent withdrawal**: data subject withdraws consent for marketing communications; system updates consent flag in customer master; suppresses customer from all marketing lists, email campaigns, and SMS notifications within 24 hours; transactional communications (order confirmations, warranty notifications) continue as service necessity; (f) DPO reports DSAR metrics quarterly: volume by type, average resolution time, backlog
- Integration with W41 (complaint intake as DSAR channel), W17 (loyalty data — loyalty account erasure), W24 (customer accounts — account closure with erasure), W8 (AR account closure — W8 step 12 references PII anonymization), W15/W43 (employee lifecycle — employee data erasure after 7-year retention)

### Staffing Implication
- **1 Data Protection Officer (DPO)**: required by RA 10173 for organizations processing personal data of 1,000+ individuals. BuildRight holds data for 600K+ customers and 8,000+ employees. The DPO role may be combined with Legal or Compliance but must have direct reporting to management. This is a new role recommendation (absorbed within Legal & Compliance team of ~5, expanding to ~6).
- No other incremental headcount. Breach response is a cross-functional effort by existing IT, Legal, and management.

---



---

## W55. IT Disaster Recovery & System Failover

| Field | Detail |
|---|---|
| **Trigger** | Core ERP system failure exceeding RTO (4 hours per NFR-013), data center outage, cloud service disruption, or cyber attack causing system unavailability |
| **Frequency** | Rare; estimated 0–2 DR events/year requiring failover |
| **Volume** | Affects all 8,050 users; 1,000 POS terminals; 200 stores; 5 DCs |
| **Owner** | CIO |
| **Participants** | CIO, IT Infrastructure team, IT Helpdesk, Store Ops Director, CFO, external DR service provider |

### Background

This workflow covers the IT system recovery process, distinct from W49 (typhoon/facility business continuity) which covers physical location response. NFR-013 defines: RPO ≤ 1 hour (max 1 hour of data loss), RTO ≤ 4 hours (max 4 hours of core system unavailability). POS terminals operate offline for 8+ hours per W5g.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | IT Infrastructure monitoring detects or is alerted to system failure: error rates, service health checks, connectivity loss, or user reports of system unavailability | IT Infrastructure / System | CIO | Immediate (automated detection) |
| 2 | IT Infrastructure assesses scope and severity: (a) single module failure (e.g., POS integration down), (b) full ERP outage, (c) data center / cloud region outage, (d) suspected cyber attack (ransomware, DDoS) | IT Infrastructure Lead | CIO | 15–30 min |
| 3 | CIO declares DR event if severity exceeds RTO: notifies CEO, COO, CFO; communicates estimated recovery time; Store Ops Director notifies Regional Managers and Store Managers | CIO | CEO | 15 min |
| 4 | **Stores**: continue selling in offline mode per W5g; POS transactions queue locally for upload upon recovery | Store Manager | Store Ops Director | Automated (W5g) |
| 5 | **DCs**: DC operations shift to manual processing — Receiving Clerks record goods receipts on paper/spreadsheet for batch entry upon recovery; picking and shipping suspended for non-critical orders | DC Manager | Supply Chain Manager | Manual fallback |
| 6 | **Ecommerce**: Digital Commerce platform displays maintenance notification; new orders suspended; in-progress orders held for fulfillment upon recovery | Ecom Team | CMO | 15 min |
| 7 | **Recovery execution**: IT Infrastructure initiates failover to DR site or secondary cloud region: (a) verify DR environment is current (data replication lag ≤ RPO), (b) switch DNS and network routing to DR environment, (c) validate core services: authentication, POS sync, inventory, financial posting, (d) incremental data replay from primary if replication lag exists | IT Infrastructure | CIO | 1–3 hours |
| 8 | If primary system restore (instead of failover): (a) identify root cause, (b) repair or restore from backup, (c) verify data integrity against last known good checkpoint, (d) bring services online sequentially (core first, then ancillary), (e) validate system health | IT Infrastructure | CIO | 2–4 hours |
| 9 | System restored: CIO communicates "all clear" to business; stores begin uploading offline transactions per W5g; DCs batch-enter manual receipts; ecommerce resumes order processing | CIO | CEO | 15 min |
| 10 | **Data integrity verification**: IT runs reconciliation checks: (a) offline POS transactions vs. central inventory, (b) any manual DC entries vs. expected receipts, (c) database transaction logs for completeness, (d) financial posting integrity (no partial journal entries) | IT Infrastructure + Finance | Controller | 1–2 hours |
| 11 | Post-recovery: CIO conducts root cause analysis within 5 business days; documents incident, root cause, recovery actions, data loss (if any), and preventive measures | CIO | CEO | 4 hours |
| 12 | Quarterly: IT Infrastructure conducts scheduled DR failover test during maintenance window; validates RTO and RPO targets; documents test results; updates DR runbook based on findings | IT Infrastructure | CIO | 4 hours/quarter |

### System Touchpoints
- Automated system health monitoring with configurable alerting thresholds (W55.1)
- DR environment: real-time data replication with RPO ≤ 1 hour (synchronous or near-synchronous); automated or one-click failover capability (W55.7)
- Backup integrity verification: automated checksum validation on backup files; periodic restore testing (W55.8)
- Offline POS transaction upload and reconciliation per W5g (W55.4, 10)
- Incident logging and root cause documentation (W55.11)
- DR test scheduling and results tracking (W55.12)
- DR test failure remediation: if quarterly DR test fails to meet RTO (4 hours) or RPO (1 hour) targets — (a) IT Infrastructure Lead documents the specific failure (failover latency, data replication lag, service recovery sequence, single point of failure); (b) CIO convenes emergency remediation meeting with IT Infrastructure within 5 business days; (c) remediation plan created with specific actions, responsible owners, and target completion date; (d) retest scheduled within 30 days of remediation completion; (e) if retest also fails: CIO escalates to CEO with capital investment request for infrastructure upgrade; (f) all test results (pass and fail) retained in DR test log for audit evidence; (g) External auditor may request DR test results as part of annual audit (W42.19, W55.12)
- Integration with W5g (offline POS), W48 (helpdesk incident management), W49 (physical disaster response — this workflow is system-level, W49 is facility-level)

### Staffing Implication
- No incremental headcount. DR response is executed by existing IT Infrastructure team (part of the recommended ~28–30 IT staff in W48).
- External DR service provider: if BuildRight uses a managed DR service or colocation DR site, the provider's SLA must align with BuildRight's RTO/RPO targets.

---



---

## W73. Data Migration Validation & Parallel-Run Testing

> This workflow describes the operational participation of business users in data migration validation and parallel-run testing during ERP implementation. It is an implementation-phase workflow, not a steady-state operational process.

| Field | Detail |
|---|---|
| **Trigger** | Implementation roadmap Phase 2 (data migration) and Phase 3 (pilot go-live with parallel run) per Implementation Roadmap |
| **Frequency** | Once per implementation; validation cycles repeated per migration iteration |
| **Volume** | All master data (55,000 SKUs, 1,000 vendors, 600,000+ customers, 8,050 employees, 205 locations) + open transaction data (open POs, open AR/AP, inventory balances, fixed assets) |
| **Owner** | Implementation Project Manager (overall); Department Heads (validation per domain) |
| **Participants** | Store Managers, Cashiers, AP/AR Clerks, Category Managers, Buyers, Cost Accountant, IT, external implementation partner |

### Data Migration Validation

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Item master validation**: Merchandise Planners verify migrated SKU data — sample 500–1,000 SKUs across categories; confirm item description, unit of measure, cost, SRP, category assignment, and attributes (catch-weight flags, shelf-life flags, consignment/VMI flags) match source system; report discrepancies to implementation partner for correction | Merchandise Planner | Category Manager | 8 hours/iteration |
| 2 | **Customer master validation**: AR Clerks verify sample of 500 trade/corporate accounts — confirm credit limits, payment terms, VAT treatment classification, and contact details; Loyalty Manager verifies sample of 1,000 loyalty accounts — points balance, tier status, contact information | AR Clerk / Loyalty Manager | AR Supervisor | 8 hours/iteration |
| 3 | **Vendor master validation**: Buyers verify sample of 200 vendors — confirm payment terms, lead times, bank details, tax classification (ATC codes), and pricing tolerance | Buyer | Category Manager | 4 hours/iteration |
| 4 | **Inventory balance validation**: Cost Accountant and DC Supervisors verify opening inventory balances per location (200 stores + 5 DCs) — reconcile migrated quantities and values (WAC) to legacy system closing balances; identify discrepancies > 1% by value | Cost Accountant / DC Supervisor | Controller | 8 hours/location group |
| 5 | **Financial opening balance validation**: Controller and Chief Accountant verify migrated opening trial balance per entity (5 entities) — GL account balances, open AP invoices, open AR invoices, fixed asset register, bank balances; reconcile to legacy closing trial balance | Controller / Chief Accountant | CFO | 16 hours/iteration |
| 6 | **Employee master validation**: HR Head verifies sample of 200 employees across entities — confirm salary, tax status, statutory deduction registration, leave balances, and organizational assignment | HR Head | CHRO | 4 hours/iteration |
| 7 | All validation exceptions logged in implementation issue tracker; corrected in next migration iteration; re-validated until zero material discrepancies | All validators | Project Manager | Ongoing |

### Parallel-Run Testing (Pilot Phase)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 8 | **Payroll parallel run**: for 1 payroll cycle (semi-monthly), Payroll Officer processes payroll in both legacy and new ERP simultaneously; compares output per employee — gross pay, deductions, net pay, employer contributions; discrepancies > PHP 100 per employee flagged for investigation; Finance validates GL postings match between systems | Payroll Officer / Finance | CFO | 1 payroll cycle |
| 9 | **Month-end close parallel run**: for 1 month-end period, Chief Accountant performs close steps (W9a) in both systems; compares trial balance, financial statements, and key reconciliation outputs (bank rec, GRNI, AR aging, AP aging) | Chief Accountant | Controller | 1 close cycle |
| 10 | **POS parallel run** (pilot stores only): during pilot go-live (Implementation Roadmap Phase 3), pilot store Cashiers process live transactions in new POS while legacy POS runs in shadow mode; Store Manager compares daily Z-reports (transaction count, revenue by tender, cash total) between systems; discrepancies > 1% by revenue flagged for investigation | Cashier / Store Manager | Store Ops Director | 2–4 weeks |
| 11 | **Inventory transaction parallel run**: for pilot stores and serving DC, Receiving Clerks and Stock Associates process key inventory transactions (goods receipt, transfer receipt, cycle count, POS sales deduction) in both systems; Cost Accountant compares ending inventory balances | Receiving Clerk / Cost Accountant | Controller | 2–4 weeks |
| 12 | **User acceptance testing (UAT)**: before each go-live wave, designated power users from each department execute scripted UAT test cases covering their critical workflows (AP clerk tests W7, Buyer tests W2, Cashier tests W5b, etc.); all test cases must pass with zero critical defects for wave go-live approval | Department power users | Project Manager | 1–2 weeks/wave |
| 13 | **Sign-off**: after successful parallel run and UAT, Department Heads sign off on their domain's readiness per go-live wave; Controller signs off on financial accuracy; CFO gives final go/no-go for each wave | Department Heads / CFO | CEO | 1 day/wave |

### System Touchpoints
- Data migration validation workbench: compare migrated data to source with side-by-side display and discrepancy flagging (W73.1–7)
- Parallel-run comparison reports: payroll output comparison, trial balance comparison, Z-report comparison, inventory balance comparison (W73.8–11)
- UAT test case management: scripted test cases with pass/fail tracking and defect logging (W73.12)
- Go-live readiness sign-off workflow with department-level approval (W73.13)
- Integration with all operational workflows (each workflow validated during UAT)

### Staffing Implication
- **Business user time**: data migration validation requires ~50–80 hours of business user effort per iteration (typically 2–3 iterations); parallel-run testing requires ~40–60 hours per cycle; UAT requires ~20–30 hours per wave; total business user effort across implementation: ~400–600 hours spread over 12–18 months
- **This is a one-time implementation cost**, not steady-state headcount. Business users participate alongside their normal duties during implementation. Implementation project plan should allocate dedicated validation windows.

---



---


## W113. Business Intelligence & Data Governance

| Field | Detail |
|---|---|
| **Trigger** | Monthly BI governance review; ad-hoc report request; dashboard lifecycle milestone; or data quality issue identified |
| **Frequency** | Monthly governance review; continuous report request management; quarterly dashboard lifecycle review |
| **Volume** | ~50–100 ad-hoc report requests/month from across the organization; ~20–30 active dashboards at any time; ~8,060 potential users across 14 requirement categories |
| **Owner** | BI Manager / Data Analyst |
| **Participants** | BI Manager, Data Analysts, IT Manager, Department Heads, Controller, CIO |

### Background

RPT-001 through RPT-010 define reporting requirements — executive dashboards, store P&L, sales analytics, inventory reports, ad-hoc reporting, and scheduled distribution. W35 defines the management reporting rhythm. However, there is no workflow governing the BI layer itself: how reports and dashboards are created, maintained, and retired; how data quality is monitored; how ad-hoc requests are prioritized; who owns which data domain; and how the data dictionary and business rules are maintained. Without BI governance, reports proliferate (creating "Excel hell"), data definitions diverge across departments, and the same metric shows different values in different reports — undermining trust in data-driven decisions at PHP 62.3B scale.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Ad-hoc report request intake**: Department Head or Manager submits report request via BI request portal: (a) request description (what data is needed, for what purpose), (b) desired format (dashboard, scheduled report, one-time extract), (c) urgency (standard 5-day SLA, expedited 2-day SLA with Department Head justification, immediate — routed to BI Manager for triage), (d) intended audience (who will consume the report); BI Manager triages daily: (e) check if an existing report already covers the need (duplicate detection), (f) classify as: reuse existing, modify existing, or create new, (g) assign to Data Analyst with priority and deadline | BI Manager | CIO | 15 min/request (triage) |
| 2 | **Report development and approval**: Data Analyst develops report per request: (a) uses approved data sources and definitions from data dictionary (step 5), (b) validates output against known data points (reconciliation with source system), (c) creates report with appropriate visualization and documentation (data source, calculation logic, filters, refresh frequency), (d) BI Manager reviews for accuracy, performance (query execution time < 30 seconds per NFR-004), and adherence to report design standards, (e) requestor reviews and confirms report meets need, (f) BI Manager publishes report to appropriate audience group with access controls | Data Analyst / BI Manager | CIO | 4–8 hours (new report); 1–2 hours (modify existing) |
| 3 | **Data quality monitoring**: System runs automated daily data quality checks across critical data domains: (a) **Completeness**: are all expected records present? (e.g., every store should have daily sales data), (b) **Accuracy**: do totals reconcile? (e.g., sum of store sales = consolidated total), (c) **Timeliness**: is data current? (e.g., POS data loaded within 30 minutes of transaction), (d) **Consistency**: do cross-system metrics agree? (e.g., ERP inventory = WMS inventory), (e) anomalies generate data quality alerts to BI Manager and IT; BI Manager investigates and coordinates with IT for resolution; monthly: BI Manager generates data quality scorecard by domain (target: ≥ 98% quality score) | System / BI Manager | CIO | 30 min/day (alert review) + 2 hours/month (scorecard) |
| 4 | **Dashboard lifecycle management**: Quarterly: BI Manager reviews all active dashboards: (a) **Usage analytics**: which dashboards are actively used (login frequency, view count)? — dashboards not accessed in 90 days flagged for retirement, (b) **Performance**: which dashboards have slow load times or query timeouts? — prioritize for optimization, (c) **Accuracy**: have underlying data sources changed (new GL accounts, new locations, new item categories) that require dashboard updates?, (d) **Retirement**: deprecated dashboards archived (not deleted) with retirement date and reason; users notified 30 days before retirement | BI Manager | CIO | 4 hours/quarter |
| 5 | **Data dictionary and business rules maintenance**: BI Manager maintains master data dictionary: (a) **Metric definitions**: every KPI used in reports has a single documented definition (e.g., "Gross Margin = (Revenue − COGS) ÷ Revenue × 100; Revenue = net of returns; COGS = weighted average cost"), (b) **Data domain ownership**: each data domain has a designated owner (e.g., Finance owns financial metrics, Merchandising owns sales metrics, Supply Chain owns inventory metrics), (c) **Calculation logic**: documented and version-controlled for every report metric, (d) **Source system mapping**: every metric traced to its source system field, (e) updates to data dictionary require BI Manager approval and are logged with effective date and reason | BI Manager | CIO | Ongoing (~4 hours/month) |
| 6 | **Monthly BI governance meeting**: BI Manager convenes monthly BI governance meeting with Department Head representatives: (a) review data quality scorecard, (b) review open report requests and backlog, (c) discuss upcoming reporting needs (new metrics, new data sources, organizational changes), (d) resolve data definition disputes (when departments disagree on metric calculation), (e) review report usage and identify opportunities to consolidate overlapping reports, (f) approve data dictionary changes | BI Manager / Department Heads | CIO | 1 hour/month |
| 7 | **Access control and security**: BI Manager manages report and dashboard access per NFR-007 security requirements: (a) reports containing financial data restricted to Finance and authorized roles, (b) store-level P&L visible to Store Manager (own store only), Regional Manager (stores in region), and VP Operations (all stores), (c) customer data in reports masked per RA 10173 data privacy requirements (W53), (d) access changes logged with approver and reason; quarterly: BI Manager reviews access control list for appropriateness | BI Manager | CIO | 30 min/month + 4 hours/quarter (review) |
| 8 | **Annual BI roadmap**: CIO and BI Manager prepare annual BI roadmap: (a) planned new reports and dashboards based on business priorities, (b) technology upgrades (BI tool versions, data warehouse performance), (c) self-service BI enablement — train power users in Department Heads to create own reports using governed data sets, (d) data integration roadmap — new data sources to onboard (3PL tracking data, ecommerce behavioral data, vendor portal data), (e) budget for BI tools, training, and external consulting | CIO / BI Manager | CEO | Annual (8 hours) |

### System Touchpoints
- BI report request portal with classification, priority, and SLA tracking (W113.1)
- Report development standards and publishing workflow with approval gates (W113.2)
- Automated daily data quality checks: completeness, accuracy, timeliness, consistency (W113.3)
- Data quality scorecard by domain with trend tracking (W113.3)
- Dashboard usage analytics with login frequency, view count, and load time metrics (W113.4)
- Dashboard retirement workflow with 30-day user notification and archiving (W113.4)
- Master data dictionary with metric definitions, domain ownership, calculation logic, and source mapping (W113.5)
- Role-based access control for reports and dashboards per NFR-007 (W113.7)
- Integration with W35 (management reporting — reports consumed in reporting rhythm), W48 (IT helpdesk — BI tool support), W53 (data privacy — customer data in reports), W55 (DR — BI system failover), W73 (data migration — BI data source validation post-migration)

### Staffing Implication
- **1 BI Manager** (within IT team of ~28): manages BI platform, governance, and team. This role is implied by RPT requirements but not formalized.
- **2–3 Data Analysts** (within IT team): develop reports, manage data quality, maintain data dictionary. At ~50–100 requests/month × 4–8 hours each for new reports, plus ongoing maintenance = ~2–3 full-time equivalents. Redeployed from existing IT team or new hires within planned IT headcount.
- **No incremental headcount beyond planned IT team.**

---

## W131. IT Asset Lifecycle Management

| Field | Detail |
|---|---|
| **Trigger** | New hire (W15), hardware failure, or refresh cycle (every 3–4 years) |
| **Frequency** | Ongoing |
| **Volume** | Managing ~1,500 laptops/desktops, ~1,000 POS terminals, servers, and networking gear |
| **Owner** | IT Asset Manager |
| **Participants** | IT Helpdesk, Procurement (W2), Finance (Fixed Assets W39) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Sourcing: Procurement of IT hardware based on standard specs | IT Asset Mgr | CIO | 2 weeks |
| 2 | Tagging & Registration: Assign Asset Tag and record in ITAM database and ERP Fixed Assets | IT Helpdesk | IT Asset Mgr | 30 min/unit |
| 3 | Provisioning: Install OS, security software, and user-specific apps | IT Helpdesk | IT Asset Mgr | 2 hours/unit |
| 4 | Assignment: Handover to employee and sign acknowledgment form | IT Helpdesk | Employee | 15 min |
| 5 | Maintenance: Periodic updates and physical health checks | IT Helpdesk | IT Asset Mgr | Ongoing |
| 6 | Retirement: Data wipe, asset decommissioning, and disposal (W39) | IT Helpdesk | IT Asset Mgr | 1 hour/unit |

---

## W132. Software Development & Change Management

| Field | Detail |
|---|---|
| **Trigger** | Business request for new feature, bug fix, or system update |
| **Frequency** | Weekly release cycle |
| **Volume** | ~5–10 changes per week |
| **Owner** | Application Manager |
| **Participants** | Developers, QA Team, Business Users (UAT), Change Advisory Board (CAB) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Requirement Analysis: Document functional and technical specs | Business Analyst | App Manager | 3–5 days |
| 2 | Development: Code changes in sandbox/dev environment | Developer | App Manager | 1–2 weeks |
| 3 | Unit & Integration Testing: Verify code in QA environment | QA Team | App Manager | 2–3 days |
| 4 | User Acceptance Testing (UAT): Business users sign off on change | Dept Users | Dept Head | 2–5 days |
| 5 | CAB Review: Evaluate risk and impact of the change | CAB | CIO | 1 hour |
| 6 | Deployment: Release to Production environment during maintenance window | DevOps / IT Ops | App Manager | 2 hours |

---

### System Touchpoints (IT Extensions)
- IT Asset Management (ITAM) database integrated with ERP Fixed Assets
- Change Management / Jira tracking for software lifecycle
- Automated deployment / CI/CD pipeline logs
- Acknowledgment form digital signature capture
- Hardware refresh schedule alerts

---

---

## W152. Employee IT Provisioning & Access Lifecycle Management

| Field | Detail |
|---|---|
| **Trigger** | New hire notification (W15); employee transfer (W43.15); or separation (W43) |
| **Frequency** | 100–150 provisioning events/month |
| **Volume** | Covers ~8,000 employees and ~1,500 ERP users |
| **Owner** | IT Infrastructure Manager |
| **Participants** | HR, IT Helpdesk, Hiring Manager, Security |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Request**: HR system triggers provisioning request upon completion of W15 onboarding | System / HR | — | Automated |
| 2 | **Identity Creation**: System auto-generates AD/Azure account, company email, and employee ID link | IT Helpdesk | Infrastructure Mgr | 15 min |
| 3 | **Access Role Mapping**: Assign ERP roles (W37), folder permissions, and application access based on Job Code | IT Helpdesk | Infrastructure Mgr | 30 min |
| 4 | **Hardware Prep**: Image laptop/workstation; configure POS login for store staff | IT Helpdesk | — | 1 hour |
| 5 | **Transfer / Change**: Upon employee transfer, review and revoke old permissions; add new ones within 24 hours | IT Helpdesk | Dept Head | 30 min |
| 6 | **De-provisioning**: Upon separation (W43), immediate block on all accounts (T-minus 0); hardware retrieval | IT Helpdesk | CIO | 15 min |
| 7 | **Audit**: Monthly reconciliation of Active Directory vs. HR Master to identify "ghost accounts" | Security Admin | CIO | 4 hours |

---

## W257. Enterprise API & Systems Integration Lifecycle Management

| Field | Detail |
|---|---|
| **Trigger** | Business requirement for a new software integration (e.g., 3PL carrier API, Ecommerce platform, new CRM tool) or update to existing API |
| **Frequency** | 2-3 new integrations per quarter; ongoing maintenance |
| **Volume** | Over 50 active integrations across the enterprise |
| **Owner** | Integration Architect |
| **Participants** | Business Owner, IT Developers, External Vendor, Security Admin |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Requirements Gathering**: Define data payload, frequency (real-time vs batch), mapping rules, and security requirements (OAuth, TLS) | Integration Arch | Business Owner | 1-2 weeks |
| 2 | **Design & Security Review**: Security team reviews API endpoints, data privacy (RA 10173) implications, and rate limiting policies | Security Admin | CIO | 2 days |
| 3 | **Development & Middleware Config**: Configure API Gateway / Enterprise Service Bus (ESB) for routing, transformation, and error handling | IT Developer | Integration Arch | 2-4 weeks |
| 4 | **Testing**: Conduct unit testing, end-to-end integration testing in sandbox, and load testing for peak volumes | QA Team | Integration Arch | 1-2 weeks |
| 5 | **Deployment & Monitoring**: Deploy to production; configure automated alerts for integration failures or latency spikes | DevOps | Integration Arch | 1 day |
| 6 | **Maintenance & Versioning**: Monitor API performance; manage API version upgrades to avoid breaking downstream systems | Integration Arch | CIO | Ongoing |
