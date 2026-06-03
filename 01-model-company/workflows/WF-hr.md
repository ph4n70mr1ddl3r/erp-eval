# HR & Payroll Workflows

> Payroll, recruitment, shift scheduling, onboarding/offboarding, training, performance, expenses, employee loans, PPE & uniform, succession & internal mobility, management trainee program, and statutory benefits & claims administration.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W10. Payroll Processing](#payroll-processing)
- [W15. Recruitment & Employee Onboarding](#recruitment-employee-onboarding)
- [W34. Store Shift Scheduling](#store-shift-scheduling)
- [W43. Employee Separation & Offboarding](#employee-separation-offboarding)
- [W51. Employee Training & Skills Development](#employee-training-skills-development)
- [W72. Employee Performance Management](#employee-performance-management)
- [W74. Employee Expense Reimbursement](#employee-expense-reimbursement)
- [W76. Employee Loans & Advances](#employee-loans-advances)
- [W172. Employee PPE & Uniform Lifecycle](#employee-ppe--uniform-lifecycle)
- [W178. Employee Succession & Internal Mobility](#employee-succession--internal-mobility)
- [W179. Management Trainee (Cadetship) Program](#management-trainee-cadetship-program)
- [W251. Philippine Statutory Benefits & Claims Administration (SSS, PhilHealth, Pag-IBIG)](#philippine-statutory-benefits--claims-administration-sss-philhealth-pag-ibig)

---

## W10. Payroll Processing

| Field | Detail |
|---|---|
| **Trigger** | Semi-monthly payroll calendar (14th and 28th/30th) |
| **Frequency** | 10 payroll runs/month (5 entities × 2) |
| **Volume** | ~7,050 employees total |
| **Owner** | Payroll Manager |
| **Participants** | Payroll Officer, HR Assistant, Department Heads (OT/leave approval), Finance (bank file) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Payroll Officer pulls time & attendance data from biometric/RFID system | Payroll Officer | Payroll Manager | 30 min/run |
| 2 | HR Assistant verifies approved leaves, overtime, and schedule adjustments are posted | HR Assistant | Payroll Manager | 2 hours/run |
| 3 | Payroll Officer validates: basic salary + OT + night differential + holiday pay + allowances | Payroll Officer | Payroll Manager | 1 hour/run |
| 4 | System calculates deductions: SSS, PhilHealth, Pag-IBIG, withholding tax (TRAIN law), loans, advances | System | — | Automated |
| 5 | Payroll Officer reviews computed payroll for anomalies (negative net pay, unusually high OT) | Payroll Officer | Payroll Manager | 1 hour/run |
| 6 | Payroll Manager reviews and approves payroll register | Payroll Manager | CHRO | 30 min/run |
| 7 | System generates bank file for payroll crediting (BDO, BPI, etc.) | System | — | Automated |
| 8 | Finance/Treasury reviews bank file; transmits to bank | Treasury Analyst | CFO | 30 min/run |
| 9 | System posts payroll journal entries to GL (salary expense, payable, deductions) | System | — | Automated |
| 10 | Payslips generated; distributed via email or employee self-service portal | System | — | Automated |
| 11 | Monthly: generate SSS PRN, PhilHealth contribution, Pag-IBIG contribution files for remittance | Payroll Officer | Payroll Manager | 1 hour/month |
| 11a | Payroll Officer reconciles statutory contribution schedule (per-employee breakdown) to generated remittance file and bank payment confirmation; investigates and resolves discrepancies before remittance deadline; system flags employees with missing or incomplete statutory data | Payroll Officer | Payroll Manager | 30 min/month |
| 11b | Contractual / fixed-term workers: system tracks contract start/end dates and auto-alerts HR Assistant 30 days before expiry; payroll computes pro-rated 13th month pay and statutory benefits per contract duration; end-of-contract settlement computed similar to final pay (W10 step 12) but with different legal basis; if employee converts to regular status, HR Assistant updates employee type in system and payroll adjusts benefit computation accordingly | HR Assistant / Payroll Officer | Payroll Manager | 15 min/employee |
| 12 | Final pay computation (upon employee separation): system calculates pro-rated 13th month pay, converted unused leave credits, less outstanding loans/advances and clearance deductions | Payroll Officer | Payroll Manager | 30 min/employee |
| 13 | System posts final pay as separate payroll run or adjustment; generates final payslip | System | — | Automated |

**Total payroll processing time**: ~6 hours per run per entity. With 5 entities, can be parallelized across 2–3 payroll officers.

### System Touchpoints
- Time & attendance import from biometric system (W10.1)
- Leave and overtime approval workflow (W10.2)
- Philippine payroll computation engine (TRAIN law, SSS, PhilHealth, Pag-IBIG tables) (W10.3–4)
- Payroll anomaly detection (W10.5)
- Bank file generation in Philippine bank formats (W10.7)
- GL posting from payroll (W10.9)
- Payslip distribution (W10.10)
- Statutory contribution file generation with PRN (W10.11)
- Statutory remittance reconciliation: per-employee contribution schedule vs. remittance file vs. bank confirmation; discrepancy flagging (W10.11a)
- Contractual/fixed-term worker management: contract date tracking, pro-rated benefit computation, end-of-contract settlement, regularization conversion (W10.11b)
- Agency / manpower contractor worker management: for seasonal and peak-period staffing (Christmas season, bi-monthly sale events, new store openings), BuildRight engages licensed manpower agencies per DOLE Department Order No. 174 (Labor-Only Contracting rules); agency workers are NOT employees of BuildRight entities — they appear in the agency's payroll, not in BuildRight's W10 payroll run; system tracks agency worker headcount separately from regular headcount for workforce planning; Store Manager submits agency staffing request to HR with headcount, duration, and skill requirements; HR coordinates with approved agency partners; agency invoices are processed as non-PO service invoices per W7C with DOLE-compliant documentation (agency service agreement, worker deployment list, attendance records); agency workers are issued temporary POS and access badges with limited system permissions and defined expiry dates; system distinguishes agency hours from regular employee hours for labor cost reporting (agency cost is a contract service expense, not payroll); typical agency worker deployment: 2–5 per store during November–December peak, and 10–15 per new store opening (W16) for the first 2 weeks of operations
- Agency worker access provisioning: Store Manager submits agency worker access request to IT via W48 helpdesk ticket, specifying worker name, agency, assignment duration, and required access level; IT creates temporary system account with predefined "Agency Worker" permission template (POS transaction processing only — no voids, no price overrides, no manager functions, no reports); access badge created with defined expiry date matching deployment end date; system auto-revokes access on expiry date; at end of deployment, Store Manager verifies badge return and IT confirms system deactivation; if deployment extended, Store Manager submits extension request before expiry; system logs all agency worker access with agency name, worker name, store, start/end dates, and permission level; monthly: IT generates agency worker access report showing active, expired, and unreturned badges; unreturned badges flagged for Store Manager follow-up (W10, cross-reference W71 access badge management)

### Statutory Compliance Calendar

The following table shows all recurring statutory remittance deadlines per entity. System generates alerts 5 business days before each deadline.

| Statutory Obligation | Frequency | Deadline | Remittance Method | Responsible | Cross-Reference |
|---|---|---|---|---|---|
| SSS employee + employer contributions | Monthly | Last day of following month (or 10th of second month per SSS schedule) | PRN via SSS online portal or bank | Payroll Officer | W10.11 |
| PhilHealth contributions | Monthly | Every 10th of the following month | Electronic remittance via PhilHealth portal | Payroll Officer | W10.11 |
| Pag-IBIG contributions | Monthly | Every 10th of the following month | Online remittance via Pag-IBIG portal | Payroll Officer | W10.11 |
| BIR Withholding Tax on Compensation (1601-C) | Monthly | 10th of following month | eFPS / eBIRForms | Tax Accountant | W9A.16 |
| BIR Expanded Withholding Tax (1601-E) | Monthly | 10th of following month | eFPS / eBIRForms | Tax Accountant | W9A.16a |
| BIR VAT Return (2550M) | Monthly | 20th or 25th of following month (per BIR filing threshold) | eFPS / eBIRForms | Tax Accountant | W9A.16 |
| BIR Quarterly VAT / Income Tax (2550Q / 1702Q) | Quarterly | 25th of month following quarter end | eFPS / eBIRForms | Tax Accountant | W9A.16 |
| Local Business Tax per LGU | Per LGU calendar (annual or quarterly) | Per LGU deadline | Per LGU (online, OTC, or LGU office) | Tax Accountant | W9A.16c |
| 13th Month Pay distribution | Annual | On or before December 24 | Via payroll run | Payroll Officer | W10, W9B.18 |
| BIR Annual Income Tax Return (1702RT) | Annual | April 15 (or as extended) | eFPS / eBIRForms | Tax Accountant | W9B.21 |

> **Note**: Deadlines are based on current BIR and statutory agency guidelines; Payroll Manager reviews for regulatory changes quarterly. The 5-entity structure means each obligation is filed per-entity TIN; Payroll Officer and Tax Accountant process 5 submissions per deadline.

### Staffing Implication
- **2–3 Payroll Officers**: 5 entities × 2 runs = 10 runs/month. Each run takes ~6 hours. Total ~60 hours/month of payroll processing. 2 officers can handle this with time for reconciliation and inquiries.
- **1 Payroll Manager**: Approval, oversight, statutory compliance.
- **1–2 HR Assistants**: Leave and OT verification (data entry-heavy during payroll week).
- Fits within the ~16-person HR team.

---



---

## W15. Recruitment & Employee Onboarding

| Field | Detail |
|---|---|
| **Trigger** | Vacancy created (resignation, new position, new store opening) |
| **Frequency** | ~100–130 hires/month (1,200–1,600/year including turnover + growth) |
| **Volume** | Peaks during new store openings (35 hires per new store) |
| **Owner** | HR Recruitment Officer |
| **Participants** | Recruitment Officer, HR Assistant, Hiring Manager, HR Head |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Hiring Manager submits staffing request with role, department, justification | Hiring Manager | Dept. Head | 15 min |
| 2 | HR Recruitment Officer posts job on job boards, social media, walk-in postings | Recruitment Officer | HR Head | 30 min/role |
| 3 | Screen applications; shortlist candidates | Recruitment Officer | HR Head | 2–4 hours/role |
| 3a | **Applicant tracking detail**: system tracks all applicants through a structured pipeline — Applied → Phone Screen → Interview (1st) → Interview (2nd) → Offer → Hired / Rejected; each pipeline stage records date, recruiter notes, interviewer feedback (rating 1–5), and outcome; system auto-sends rejection email to unsuccessful candidates at each stage with configurable template; for high-volume store roles (Sales Associates, Cashiers, Stock Associates), Recruitment Officer may use a walk-in hiring event model with batch applicant entry and bulk status updates; system generates recruitment analytics: time-to-fill by role, sourcing channel effectiveness (job boards, walk-in, referral, social media), offer acceptance rate, interviewer assessment scores; applicant data retained for 1 year per RA 10173 (with candidate consent) for potential future openings | Recruitment Officer | HR Head | Ongoing |
| 4 | Conduct interviews (1st: HR; 2nd: Hiring Manager) | Recruitment Officer + Hiring Manager | Dept. Head | 1 hour/candidate |
| 5 | Select candidate; extend offer | Recruitment Officer | HR Head | 30 min |
| 6 | New hire completes pre-employment requirements (SSS, PhilHealth, Pag-IBIG, TIN, medical, NBI clearance) | New Hire | Recruitment Officer | — |
| 7 | HR Assistant creates employee record in system (personal info, position, salary, entity, tax status); employee type classified as regular, probationary, fixed-term, or project-based with contract start/end dates for non-regular employees | HR Assistant | HR Head | 30 min |
| 8 | System generates employee ID; enrolls in payroll with correct statutory deductions | System | — | Automated |
| 9 | Assign biometric/RFID credentials for time & attendance | HR Assistant | — | 10 min |
| 10 | Onboarding: safety orientation, company policies, POS/system training | Dept. Supervisor + HR | Hiring Manager | 2–3 days |
| 11 | First payroll: system computes pro-rated salary for partial month | System | — | Automated |

### Staffing Implication
- **1–2 Recruitment Officers**: 100–130 hires/month. Each hire takes ~4–6 hours of HR time (screening + interview + paperwork). With 2 recruiters: ~60 hires each/month × 5 hours = 300 hours ÷ 160 working hours/month = ~2 recruiters at near-full capacity. 2 is appropriate.
- **2 HR Assistants**: Employee record creation, credentials, onboarding logistics. 130 hires × 1 hour admin each = 130 hours/month. 2 assistants can handle alongside other HR admin.

---



---

## W34. Store Shift Scheduling

| Field | Detail |
|---|---|
| **Trigger** | Weekly schedule creation cycle |
| **Frequency** | Weekly per store; published 1 week in advance |
| **Volume** | 30 staff × 200 stores = 6,000 weekly shift assignments; 2–3 shifts per day (opening: 7 AM–2 PM, mid: 10 AM–6 PM, closing: 2 PM–10 PM) |
| **Owner** | Store Manager |
| **Participants** | Store Manager, Assistant Store Manager, Department Supervisors, HR Assistant |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates draft schedule based on: (a) store operating hours, (b) staffing model per shift (min cashiers, floor associates, receiving), (c) historical sales volume by day and hour, (d) approved leave requests, (e) labor budget (max hours per employee per week) | System | — | Automated |
| 2 | Store Manager reviews draft schedule; adjusts for: expected delivery days (DSD receiving), upcoming promotions, special events, employee skill mix per shift | Store Manager | Store Ops Director | 1 hour/week |
| 3 | Department Supervisors review shift assignments for their departments; flag conflicts or coverage gaps | Dept. Supervisor | Store Manager | 30 min/week |
| 4 | Store Manager finalizes and publishes schedule in system; employees receive notification (mobile app, SMS, or bulletin board) | Store Manager | — | 15 min |
| 5 | Employee views schedule; submits swap requests to Store Manager if needed | Employee | — | Self-service |
| 6 | Store Manager approves or denies shift swap requests; updates schedule | Store Manager | — | 15 min/week |
| 7 | During the week: if unplanned absence (sick leave, emergency): Store Manager activates contingency (call in off-duty employee, redistribute floor staff, cover cashier shift personally) | Store Manager | — | Ad hoc |
| 8 | System tracks actual hours worked (biometric/RFID clock-in/out) vs. scheduled hours; flags overtime and undertime | System | — | Automated |
| 9 | Weekly: Store Manager reviews schedule adherence report; adjusts next week's plan based on actuals | Store Manager | Regional Manager | 15 min/week |
| 10 | Monthly: Regional Manager reviews overtime hours per store vs. labor budget; flags stores consistently exceeding targets | Regional Manager | Store Ops Director | 2 hours/month (across 50 stores) |

### System Touchpoints
- Automated schedule generation based on rules engine (W34.1)
- Leave request integration (W34.1d)
- Shift swap request and approval workflow (W34.5–6)
- Schedule publishing with employee notification (W34.4)
- Time & attendance integration: actual vs. scheduled hours comparison (W34.8)
- Overtime alerting (W34.8)
- Attendance exception handling: system detects clock-in/out anomalies — (a) **missed punch**: employee forgot to clock in or out; system generates missed punch alert; employee submits missed punch request via self-service portal (W51) within 24 hours with estimated in/out time; Department Supervisor approves or adjusts; system retroactively calculates hours; (b) **biometric reader failure**: if biometric device malfunctions, Store Manager records attendance manually in system with reason code; IT Helpdesk (W48) notified as P2 incident for device repair; manual records reconciled upon device restoration; (c) **late arrival / early departure**: system flags employees clocking in > 15 minutes after shift start or clocking out > 15 minutes before shift end; Store Manager reviews daily exception list; habitual lateness (> 3 occurrences/month) triggers HR counseling; (d) **unmatched punch**: employee clocks in at one terminal and out at another, or forgets to clock out and clocks in next day; system generates unmatched punch alert; employee submits correction via self-service; supervisor approves; system resolves unmatched pair; all attendance exceptions logged per employee with timestamp, type, resolution, and approver; monthly: HR Assistant generates attendance exception summary per store for Regional Manager review (W34)
- Schedule adherence and labor budget reporting (W34.9–10)
- Integration with payroll (W10) for hour calculation

### Staffing Implication
- **Store Manager**: ~2 hours/week on scheduling. Absorbed into existing duties.
- **Department Supervisors**: ~30 min/week reviewing their section schedules. Absorbed.
- **Regional Managers**: ~2 hours/month reviewing overtime reports across their 50 stores. Absorbed.
- No incremental headcount. The system's automated draft generation significantly reduces manual scheduling effort.

---



---

## W43. Employee Separation & Offboarding

| Field | Detail |
|---|---|
| **Trigger** | Employee submits resignation, or management initiates termination, or employee retires |
| **Frequency** | ~100–130 separations/month (1,200–1,600/year at 15–20% annual turnover) |
| **Volume** | Peaks in January (post-13th month pay resignations) and during store opening months (transfer to new store vs. separation) |
| **Owner** | HR Assistant |
| **Participants** | HR Assistant, HR Head, Department Head, Payroll Officer, IT, Employee |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Employee submits resignation letter (or management issues termination notice) | Employee / Dept. Head | Dept. Head | — |
| 2 | HR Assistant creates separation record in system: resignation date, last working day (30-day notice per Labor Code or garden leave), separation type (resignation, termination, retirement, end of contract) | HR Assistant | HR Head | 10 min |
| 3 | Department Head conducts exit interview; documents feedback (work conditions, compensation, management, reason for leaving) | Dept. Head | HR Head | 30 min |
| 4 | HR Assistant initiates clearance process: system generates clearance form routed to all relevant departments | System | HR Assistant | Automated |
| 5 | **IT clearance**: IT confirms return of laptop/tablet/phone (if issued); deactivates system accounts (ERP, POS, email, VPN); revokes access badges | IT Team | CIO | 15 min/employee |
| 6 | **Department clearance**: Dept. Head confirms return of company property (uniforms, tools, keys); approves final leave usage | Dept. Head | Dept. Head | 10 min/employee |
| 7 | **Finance clearance**: AP Clerk confirms no outstanding cash advances or loans; AR confirms no corporate account exposure | AP / AR Clerk | AP/AR Supervisor | 10 min/employee |
| 8 | **Store Operations clearance** (if store employee): Store Manager confirms no pending inventory accountability issues, cash drawer reconciled | Store Manager | Store Ops Director | 10 min/employee |
| 9 | HR Assistant collects all signed clearances; marks clearance as complete in system | HR Assistant | HR Head | 10 min/employee |
| 10 | Payroll Officer computes final pay per W10 step 12: pro-rated salary for final pay period, pro-rated 13th month pay (1/12 of annual basic salary × months worked ÷ 12), converted unused leave credits (VL to cash per company policy), less outstanding loans/advances and clearance deductions; final pay computation varies by separation type — resignation: pro-rated salary + 13th month + VL conversion; termination for cause: pro-rated salary + 13th month (VL conversion per company discretion); retirement: pro-rated salary + 13th month + VL conversion + retirement pay per Labor Code or company plan (whichever is higher); end of contract: pro-rated salary + 13th month + VL conversion + separation pay if applicable per DOLE; system auto-calculates final pay based on separation type classification from W43.2 with Payroll Officer review and validation | Payroll Officer | Payroll Manager | Per W10 |
| 11 | System generates final pay as separate payroll run or adjustment; final payslip issued (W10 step 13) | System | — | Automated |
| 12 | System updates employee status to "Separated"; deactivates payroll processing; retains record for regulatory retention (7 years) | System | — | Automated |
| 13 | System generates COE (Certificate of Employment) on request: dates of employment, position, compensation range (optional) | System / HR Assistant | HR Head | 5 min/request |
| 14 | HR Head includes separation data in monthly turnover report: rate by department, store, and separation type; exit interview themes | HR Head | CHRO | 1 hour/month |
| 15 | Cross-entity employee transfer (between legal entities, e.g., Depot Inc. → Logistics Inc.): HR Assistant initiates transfer with effective date, destination entity, and new position; system processes as simultaneous separation from source entity and onboarding in destination entity with continuity of service — accumulated leave credits, 13th month pay pro-ration, and seniority carry forward; system deactivates employee in source entity payroll, creates employee record in destination entity with transferred balances, reassigns SSS/PhilHealth/Pag-IBIG to new entity's remittance, and switches BIR withholding tax to new entity's TIN registration; final pay computed at source entity (pro-rated) and first pay at destination entity for the same period; no break in employment continuity | HR Assistant / Payroll Officer | HR Head | 30 min/transfer |

**Total cycle time**: 30 days (notice period) + 5 business days after last day for final pay release

### System Touchpoints
- Separation record creation with type classification (W43.2)
- Automated clearance form generation and routing (W43.4)
- Clearance status tracking per department (W43.5–9)
- System account deactivation trigger (W43.5)
- Final pay computation by separation type: system auto-calculates final pay based on separation type (resignation, termination, retirement, end of contract) including pro-rated salary, pro-rated 13th month pay per BIR rules (1/12 of basic salary × months worked), unused VL monetization, applicable separation/retirement pay per Labor Code, less outstanding loans and deductions; final tax withholding per BIR rules (different treatment for retirement pay vs. resignation); final statutory contribution period computed per SSS/PhilHealth/Pag-IBIG rules; Payroll Officer reviews system calculation before processing (W43.10)
- Employee status lifecycle: Active → On Notice → Separated (W43.12)
- Certificate of Employment generation (W43.13)
- Cross-entity employee transfer: simultaneous separation and onboarding across legal entities with continuity of service; automatic payroll entity switch with transferred leave balances, 13th month pro-ration, and statutory reassignment; SSS/PhilHealth/Pag-IBIG reassigned to new entity; BIR withholding tax switched to new entity's TIN; GL postings to both entity payrolls for the transfer period (W43.15)
- Turnover analytics (W43.14)
- Integration with W10 (payroll) and W15 (onboarding — reverse process)

### Staffing Implication
- **HR Assistants (2)**: 100–130 separations/month × ~45 min admin each (clearance coordination + documentation) = ~90 hours/month. With 2 assistants that's ~45 hours each. Manageable alongside other HR admin duties.
- **IT**: 100–130 deactivations/month × 15 min each = ~30 hours/month. Absorbed by IT helpdesk.
- **Department Heads / Store Managers**: ~20 min per separating employee for clearance. With ~100/month spread across 200 stores, most managers handle < 1 separation/month. Negligible impact.

---



---

## W51. Employee Training & Skills Development

| Field | Detail |
|---|---|
| **Trigger** | New hire onboarding (W15), new system rollout, compliance requirement, periodic schedule, performance review finding |
| **Frequency** | Continuous; formal training sessions monthly per store; compliance training quarterly |
| **Volume** | ~7,050 employees; ~1,200–1,600 new hires/year requiring onboarding training; all employees require periodic refresher |
| **Owner** | HR — Training Officer |
| **Participants** | Training Officer, Department Supervisors, Store Managers, Category Managers (product knowledge), IT (system training), external trainers |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Training Officer maintains annual training calendar: (a) new hire onboarding (W15 step 10 — continuous), (b) quarterly compliance refreshers (safety, BIR procedures, data privacy), (c) semi-annual product knowledge updates (aligned with W1 assortment review and W32 seasonal planning), (d) annual system refresher (POS, ERP updates), (e) leadership development for supervisors and managers | Training Officer | HR Head | 4 hours/quarter (planning) |
| 2 | Training Officer develops or sources training materials per category: (a) creates in-house materials for company-specific processes (POS operations, returns handling, safety procedures, customer service standards), (b) sources external content for compliance topics (fire safety, first aid, hazmat handling for paint/chemicals), (c) coordinates with Category Managers for product knowledge content (new product features, seasonal items) | Training Officer | HR Head | Ongoing |
| 3 | Training delivery methods by audience: (a) **Store staff (6,000)**: monthly 30-minute department huddles led by Department Supervisors using provided materials; quarterly 2-hour group sessions at store level; (b) **DC staff (~750)**: quarterly safety and equipment training at DC; (c) **HQ staff (~300)**: quarterly system and process training at HQ; (d) **New hires**: W15 onboarding program (2–3 days); (e) **Managers and supervisors**: semi-annual leadership and management skills workshops | Training Officer / Dept. Supervisors / External Trainers | HR Head | Per schedule |
| 4 | System tracks training completion per employee: attendance recording, quiz/assessment scores (where applicable), certification status and expiry dates | System / HR Assistant | Training Officer | Automated + 15 min/session |
| 5 | Training Officer generates compliance dashboard: completion rates by training type, overdue trainings by location, certification expiries (e.g., forklift license, fire safety) | Training Officer | HR Head | 1 hour/month |
| 6 | Department Supervisors and Store Managers identify training needs from performance observations (W34 schedule adherence, W37 exception patterns, W41 complaint root causes) and submit training requests to Training Officer | Dept. Supervisor / Store Manager | HR Head | As needed |
| 7 | Annual: HR Head reviews training program effectiveness: training hours per employee, correlation between training completion and key metrics (POS accuracy, shrinkage rate, customer satisfaction), budget utilization | HR Head | CHRO | 4 hours/year |

### Training Categories

| Category | Frequency | Audience | Delivery Method | Assessment |
|---|---|---|---|---|
| **New hire onboarding** | Per W15 | New employees | In-person at store/DC + e-learning modules | POS competency test, safety quiz |
| **POS operations** | Annual refresher; ad-hoc for system updates | Cashiers, CSRs | Hands-on at POS terminal | Speed and accuracy test |
| **Product knowledge** | Quarterly (aligned with W1 assortment review) | Sales Associates, Dept. Supervisors | Department huddle with Category Manager materials | Informal — supervisor observation |
| **Safety & compliance** | Quarterly | All employees | E-learning (LMS) + annual practical drill | Mandatory quiz (pass/fail) |
| **Hazmat handling** | Annual (for paint/chemical departments) | Paint dept. staff, receiving clerks | In-person with certified trainer | Written test + practical demo |
| **Loss prevention awareness** | Semi-annual | All store staff | E-learning + LP officer presentation (W37) | Awareness quiz |
| **Leadership development** | Semi-annual | Store Managers, Dept. Supervisors, Asst. Managers | Workshop (2 days) | 360 feedback |
| **IT system updates** | Per system change (W48 change management) | Affected users | E-learning + release notes | N/A |

### System Touchpoints
- Training calendar management with automated scheduling (W51.1)
- Training material repository (document storage per category) (W51.2)
- Training attendance tracking with digital sign-in or manager confirmation (W51.4)
- Assessment and certification tracking with expiry alerts (W51.4–5)
- Compliance dashboard: completion rates, overdue trainings, certification status by location and employee (W51.5)
- Learning Management System (LMS) integration for e-learning modules and assessments (W51.3)
- Integration with W15 (onboarding), W34 (shift scheduling — training time scheduled), W37 (LP awareness), W43 (separation — training history retained), W48 (system change training)
- Employee self-service portal: system provides a web-based or mobile-accessible self-service portal for employees with the following capabilities — (a) **payslip viewing**: employees view and download current and historical payslips (secure, accessible only by the employee); (b) **leave management**: employees submit leave requests (VL, SL, maternity, paternity, etc.) with automatic routing to Department Supervisor / Store Manager for approval; view leave balance and approval status; (c) **personal information update**: employees update contact information (address, phone, emergency contact), bank account details for payroll crediting, and dependent information; changes require HR Assistant verification before updating the payroll master; (d) **tax document access**: employees view and download BIR Form 2316 (Certificate of Compensation Payment/Tax Withheld) annually; (e) **benefits inquiry**: view SSS, PhilHealth, Pag-IBIG contribution history and loan balances (linked to agency portals or displayed from payroll data); (f) **training enrollment**: browse and enroll in available training sessions from the W51 training calendar; view training history and certification status; (g) **announcement board**: HR and management post company announcements, policy updates, and employee engagement content; portal access is role-based (employees see their own data only; managers see additional team-level information such as team leave calendar); mobile-responsive design for access from smartphones; requirement priority: Should Have (not all features needed at go-live — payslips and leave management are highest priority)

### Staffing Implication
- **1 Training Officer** (within HR team): manages training calendar, develops materials, coordinates external trainers, and monitors compliance. With 7,050 employees across 200+ locations, this is a full-time role.
- **Department Supervisors (per store)**: deliver monthly department huddles (30 min/month) — absorbed into existing duties.
- **HR Assistants (2)**: support attendance recording and logistics — absorbed into existing duties.
- **External trainers**: engaged for specialized topics (fire safety, hazmat, first aid, forklift certification, leadership) on a per-event basis.

---



---

## W72. Employee Performance Management

| Field | Detail |
|---|---|
| **Trigger** | Annual performance review cycle; or periodic performance improvement need |
| **Frequency** | Annual formal review; quarterly check-in; ongoing performance coaching |
| **Volume** | ~7,050 employees; all employees reviewed annually |
| **Owner** | Department Head (for direct reports); Store Manager (for store staff) |
| **Participants** | Store Manager, Department Supervisors, Department Heads, HR Head, employees |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Annual goal-setting** (January): Department Heads and Store Managers set performance goals for each direct report aligned with department/store KPIs — (a) quantitative goals (sales targets, accuracy rates, shrinkage targets for Dept. Supervisors; transaction speed, cash variance for Cashiers; receiving accuracy for Receiving Clerks; cycle count accuracy for Stock Associates), (b) qualitative goals (customer service standards, teamwork, adherence to company policies), (c) development goals (training completion per W51, skill acquisition, cross-training); goals entered in system with measurable targets and timeline | Dept. Head / Store Manager | VP / Store Ops Director | 30 min/employee |
| 2 | **Quarterly check-in**: Store Manager or Department Supervisor conducts 15-minute check-in with each direct report — review progress against goals, identify obstacles, adjust goals if business conditions changed; system sends quarterly reminder to managers; check-in notes documented in system | Store Manager / Dept. Supervisor | Dept. Head | 15 min/employee/quarter |
| 3 | **Mid-year calibration** (June): Store Ops Director conducts calibration session with Regional Managers to ensure consistent performance standards across stores; HR Head provides aggregate performance data by department and region; significant rating adjustments documented | Store Ops Director / HR Head | COO | 4 hours/year |
| 4 | **Annual performance review** (December): manager completes formal assessment per employee — (a) rates performance against each goal (Exceeds Expectations, Meets Expectations, Needs Improvement, Does Not Meet Expectations), (b) documents key achievements and areas for development, (c) proposes overall rating, (d) submits to next-level manager for review and approval | Store Manager / Dept. Supervisor | Dept. Head / Store Ops Director | 45 min/employee |
| 5 | **Employee acknowledgment**: employee reviews assessment in system; provides written comments (optional); signs acknowledgment (digital signature); if employee disagrees, may submit written rebuttal retained in system alongside the assessment | Employee | — | 15 min |
| 6 | **Rating confirmation and compensation action**: Dept. Head or Store Ops Director confirms final rating; HR Head approves ratings distribution (ensures no grade inflation); ratings linked to: (a) merit increase (if budgeted — typically 3–5% for Meets Expectations, 5–8% for Exceeds), (b) 13th month pay is statutory and not performance-linked, (c) promotional readiness identification, (d) performance improvement plan trigger for Needs Improvement/Does Not Meet | HR Head / CFO | CEO | 1 week/year |
| 7 | **Performance Improvement Plan (PIP)**: for employees rated Needs Improvement or Does Not Meet — (a) manager creates PIP in system with specific improvement targets, timeline (typically 30–60 days), and support resources (training per W51, closer supervision, mentoring), (b) employee acknowledges PIP, (c) manager conducts weekly check-ins during PIP period, (d) at PIP conclusion: manager assesses outcome — improved (close PIP, continue standard monitoring), insufficient improvement (extend PIP 30 days or initiate separation per W43 with HR Head approval), (e) system tracks PIP status and outcomes for HR reporting | Store Manager / Dept. Head | HR Head | 2 hours/PIP |
| 8 | **Promotion and transfer identification**: during annual review cycle, managers identify employees meeting promotion criteria — (a) consistent Exceeds Expectations ratings for 2+ years, (b) demonstrated readiness for next-level responsibilities, (c) completed required training per W51; promotion recommendations submitted to HR Head for review and inclusion in annual headcount plan; inter-store or inter-entity transfers processed per W43.15 (cross-entity transfer) or simplified location transfer within same entity | Store Manager / Dept. Head | HR Head | Part of annual review |
| 9 | **Analytics**: HR Head generates annual performance dashboard — rating distribution by department, store, region, and entity; year-over-year rating trend; correlation between training completion (W51) and performance ratings; PIP completion rate and outcomes; promotion rate; turnover rate by performance tier | HR Head | CHRO | 4 hours/year |

### System Touchpoints
- Performance goal entry with measurable targets and timeline (W72.1)
- Quarterly check-in reminder and documentation (W72.2)
- Annual assessment form with goal-by-goal rating, comments, and digital signature (W72.4–5)
- Rating workflow: manager proposes → next-level manager reviews → HR Head approves distribution (W72.6)
- PIP creation with improvement targets, timeline, weekly check-in logging, and outcome tracking (W72.7)
- Promotion/transfer identification linked to performance history (W72.8)
- Performance analytics dashboard: rating distribution, trends, training correlation, PIP outcomes (W72.9)
- Integration with W10 (merit increase in payroll), W15 (onboarding — initial goal-setting during first 90 days), W43 (PIP failure may lead to separation), W51 (training completion feeds into performance assessment), W67 (store performance KPIs inform goal-setting for store staff)

### Staffing Implication
- **No incremental headcount.** Performance reviews are distributed across ~230 managers (Store Managers, Dept. Supervisors, Dept. Heads). Annual cycle adds ~45 min/employee/year for ~7,050 employees = ~5,300 hours total effort, distributed across the management team.
- **HR Head**: adds ~8 hours/year for calibration and rating distribution approval. Absorbed.

---



---

## W74. Employee Expense Reimbursement

| Field | Detail |
|---|---|
| **Trigger** | Employee incurs business expense not covered by petty cash (W25), purchase order (W2), or corporate card |
| **Frequency** | ~300–500 expense claims/month across all locations; peaks at month-end and during travel periods |
| **Volume** | Average claim value PHP 1,000–5,000; primarily travel, meals, training materials, field supplies, client entertainment |
| **Owner** | Employee (claimant); Department Head (approval) |
| **Participants** | Employee, Department Head / Store Manager, AP Clerk, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Employee submits expense claim in system (self-service portal or mobile app): expense date, category (travel, meals, supplies, training, entertainment, other), amount, business purpose, cost center, and receipt attachment (photo or PDF) | Employee | — | 10 min/claim |
| 2 | System validates claim: (a) receipt amount matches claimed amount, (b) expense date within allowable claim window (typically 30 days from expense date), (c) expense category is valid for employee's role, (d) total monthly claims for employee do not exceed department expense budget allocation | System | — | Automated |
| 3 | System routes claim for approval per tier: (a) ≤ PHP 5,000: immediate supervisor, (b) PHP 5,001–20,000: Department Head / Store Manager, (c) > PHP 20,000: VP / C-Suite; entertainment expenses always require Department Head approval regardless of amount | System | — | Automated routing |
| 4 | Approver reviews claim: validates business purpose, checks receipt authenticity, confirms expense is within policy (meal per diem limits, travel class restrictions, entertainment pre-approval); approves, returns for correction, or rejects with reason | Approver | Finance Manager | 5 min/claim |
| 5 | Approved claim routed to AP Clerk for processing; AP Clerk validates GL coding and cost center; posts expense to GL (Dr. Department Expense / Cr. Employee Payable) | AP Clerk | AP Supervisor | 5 min/claim |
| 6 | Reimbursement: system includes approved expense reimbursement in the next semi-monthly payroll run (W10) as a separate line item on the payslip — not taxed as compensation if supported by receipts per BIR rules; alternatively, for large reimbursements (> PHP 20,000), AP Clerk processes via separate bank transfer per W7 payment run | Payroll Officer / AP Clerk | AP Supervisor | Per W10 / W7 |
| 7 | Monthly: AP Supervisor generates expense report by department, category, and employee; Finance Manager reviews for policy compliance and unusual patterns; includes in department budget variance report per W26 | AP Supervisor | Finance Manager | 1 hour/month |

### Expense Policy Parameters (Configurable in System)

| Category | Limit | Notes |
|---|---|---|
| **Meal per diem** | PHP 500/day (local); PHP 1,000/day (provincial travel) | Receipt required for amounts exceeding per diem; per diem is non-taxable per BIR rules with supporting travel order |
| **Travel — airfare** | Economy class for domestic; requires pre-approved travel order | Receipt required; booked through admin or approved booking platform |
| **Travel — lodging** | PHP 2,000/night maximum (provincial); requires hotel receipt | Exceptions require VP approval |
| **Transportation** | Taxi, grab, or shuttle receipts | Fuel claims only for authorized vehicle users per W52 |
| **Client entertainment** | PHP 3,000/event maximum; requires pre-approval from Dept. Head | Must specify client name, attendees, and business purpose |
| **Training materials** | Per approved training plan per W51 | Requires training enrollment confirmation |
| **Claim window** | 30 days from expense date | Claims > 30 days require Finance Manager approval |
| **Monthly claim limit** | PHP 20,000 per employee (standard) | Exceptions require VP approval |

### System Touchpoints
- Employee expense claim form in self-service portal (W74.1) with receipt photo upload, category selection, and business justification (W51 employee self-service portal)
- Automated validation rules: receipt matching, claim window enforcement, monthly limit check (W74.2)
- Tiered approval workflow with routing by amount and category (W74.3–4)
- GL posting with cost center allocation (W74.5)
- Payroll integration: approved reimbursements included in semi-monthly payroll as non-taxable line items (per BIR rules — reimbursement of substantiated business expenses is not compensation); alternatively processed via AP payment run for large amounts (W74.6)
- Expense policy parameter configuration by category with limits and approval rules (W74 policy table)
- Monthly expense reporting by department, category, and employee with budget variance integration (W74.7)
- Integration with W7 (AP processing), W10 (payroll — reimbursement payment), W25 (petty cash — boundary: petty cash is for small operational expenses at location; employee expense claims are for individual employee-incurred business expenses), W26 (budget — expense tracking against department budgets), W51 (self-service portal)

### Staffing Implication
- **AP Clerk**: ~300–500 claims/month × 5 min each = ~25–42 hours/month. Absorbed within existing AP team (~8–10 clerks); ~3–5 hours/clerk/month.
- **Department Heads / Store Managers**: ~5 min per claim × average 2–5 claims/approver/month = ~10–25 min/month. Absorbed.
- No incremental headcount.

---



---

## W76. Employee Loans & Advances

| Field | Detail |
|---|---|
| **Trigger** | Employee requests salary advance, calamity loan, or company-internal loan |
| **Frequency** | ~100–200 loan/advance requests/month chain-wide; spikes after typhoons (W49) and during enrollment season (May–August) |
| **Volume** | Salary advances: PHP 5,000–20,000; Calamity loans: PHP 10,000–50,000; Company loans: PHP 10,000–100,000 |
| **Owner** | HR Assistant (intake); Payroll Officer (processing) |
| **Participants** | Employee, Department Head / Store Manager, HR Assistant, Payroll Officer, Finance Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Employee submits loan/advance request in self-service portal (W51) or paper form to HR Assistant: type (salary advance, calamity loan, company loan), amount, reason, proposed repayment period | Employee | — | 10 min |
| 2 | HR Assistant verifies eligibility: (a) salary advance — employee must be regular status, employed ≥ 6 months, no outstanding salary advance; limit = 1× basic monthly salary; (b) calamity loan — triggered by declared natural disaster (W49) affecting employee's residence; limit = 2× basic monthly salary; requires disaster declaration or barangay certification; (c) company loan — employee must be regular status, employed ≥ 1 year, no outstanding loan delinquency; limit = 3× basic monthly salary; requires documented purpose (medical, education, housing repair) | HR Assistant | HR Head | 15 min/request |
| 3 | Approval per tier: (a) salary advance ≤ PHP 20,000: Store Manager / Dept. Head; (b) calamity loan ≤ PHP 50,000: HR Head + Finance Manager; (c) company loan ≤ PHP 100,000: HR Head + CFO; (d) > PHP 100,000: CEO | Approver | Approver | 10 min/request |
| 4 | Payroll Officer creates loan record in system: principal amount, disbursement date, repayment schedule (typically 3–6 monthly installments for salary advance; 6–12 months for calamity/company loan), interest rate (salary advance: 0% per company policy; calamity loan: 0% per DOLE guidance; company loan: 6% per annum or BIR-prescribed minimum per arm's-length rules if officer/owner), monthly deduction amount | Payroll Officer | Payroll Manager | 10 min/loan |
| 5 | System disburses loan: salary advance included in next semi-monthly payroll run as a separate non-taxable line item (Dr. Employee Loans Receivable / Cr. Cash); calamity and company loans processed via separate bank transfer (Dr. Employee Loans Receivable / Cr. Cash) within 3 business days of approval | System / Treasury Analyst | Payroll Manager | Automated + 15 min |
| 6 | System automatically deducts monthly loan repayment from employee's payroll per schedule (Dr. Cash / Cr. Employee Loans Receivable); deduction appears as separate line on payslip; if employee's net pay would fall below minimum wage after deduction, system reduces deduction amount and extends repayment period | System | — | Automated |
| 7 | Monthly: Payroll Officer generates loan portfolio report — total outstanding loans by type, aging (current vs. overdue), delinquency rate, new disbursements, collections; Finance Manager reviews for provisioning adequacy | Payroll Officer | Finance Manager | 1 hour/month |
| 8 | **Employee separation with outstanding loan**: at separation (W43), Payroll Officer settles outstanding loan balance from final pay (W10 step 12) — system deducts remaining principal and accrued interest from final pay before other deductions; if final pay insufficient to cover full loan balance, employee signs promissory note for remaining balance and Payroll Officer tracks post-employment collection; write-off per Controller approval if uncollectible | Payroll Officer / Controller | Finance Manager | Per W43 |

### System Touchpoints
- Loan/advance request form in self-service portal with eligibility validation (employment status, tenure, outstanding loans) (W76.1–2)
- Loan record creation with amortization schedule and automatic payroll deduction (W76.4, W76.6)
- Loan disbursement via payroll or bank transfer with GL posting (W76.5)
- Loan portfolio reporting: outstanding, aging, delinquency, disbursements, collections (W76.7)
- Final pay settlement of outstanding loans at separation (W76.8)
- Minimum wage protection: system ensures net pay does not fall below minimum wage after loan deduction (W76.6)
- Integration with W10 (payroll deduction), W43 (separation — final pay settlement), W49 (calamity loan trigger), W51 (self-service portal)

---

### Staffing Implication
- **HR Assistant**: ~100–200 requests/month × 15 min = ~25–50 hours/month. Absorbed within existing 2 HR Assistants.
- **Payroll Officer**: loan creation + portfolio reporting adds ~15 hours/month. Absorbed within existing payroll team.
- **No incremental headcount.**

---

## W172. Employee PPE & Uniform Lifecycle

| Field | Detail |
|---|---|
| **Trigger** | New hire onboarding; or periodic replacement schedule; or damage/loss report |
| **Frequency** | Annual mass distribution; semi-annual replenishment; ad-hoc for new hires |
| **Volume** | ~8,000 employees; ~24,000 sets of uniforms (3 per employee) + safety gear |
| **Owner** | HR Operations Manager |
| **Participants** | HR Assistant, Store/DC Manager, Procurement, Vendor, Employee |

### Background

With over 8,000 employees in retail and distribution, maintaining a consistent professional image and ensuring safety compliance (PPE) is a significant logistical task. BuildRight provides uniforms and mandatory safety gear (safety shoes, helmets, vests) to all store and DC personnel.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Sizing & Allocation**: During onboarding (W15), HR Assistant captures employee sizes (shirt, pants, shoes); system assigns standard entitlement (e.g., 3 shirts, 2 pants, 1 pair of safety shoes, 1 helmet) | HR Assistant | — | 10 min |
| 2 | **Issuance**: HR Assistant issues gear from store/DC stock; employee signs "Property Acknowledgment" in the system/portal; system links items to employee ID for accountability | HR Assistant | Store/DC Mgr | 15 min |
| 3 | **Inventory Tracking**: System tracks PPE/Uniform stock as "Internal Use Inventory"; replenishment triggered via W4 when stock falls below reorder point | HR Assistant | Procurement | Automated |
| 4 | **Replacement**: (a) **Periodic**: Every 12 months, employees are eligible for a new set; (b) **Damage**: If gear is damaged in the line of duty, employee returns old item for a free replacement; (c) **Loss**: If lost, employee pays a replacement fee via payroll deduction (W10) | HR Assistant | Store/DC Mgr | 10 min |
| 5 | **Return at Separation**: Upon separation (W43), employee must return all non-consumable gear (helmets, vests, badges); HR Assistant verifies return before final clearance approval | HR Assistant | Dept Head | 15 min |
| 6 | **Audit**: Quarterly: HR Ops Manager audits PPE compliance on the floor (ensuring correct shoes/helmets worn); feeds into W72 Performance Review | HR Ops Mgr | Store/DC Mgr | 2 hours/site |

### System Touchpoints
- Employee entitlement module (linking roles to specific PPE requirements)
- Property acknowledgment log with digital signature
- Payroll deduction integration for lost items (W10)
- Internal-use inventory replenishment (W4)
- PPE compliance flag in Performance Management (W72)



---


---

## W178. Employee Succession & Internal Mobility

| Field | Detail |
|---|---|
| **Trigger** | Retirement of key leader; store expansion; or high-potential (HiPo) identification |
| **Owner** | CHRO |
| **Participants** | CEO, Department Heads, HR Manager, High-Potential Employees |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **HiPo Identification**: Annual review of performance (W72) and potential; tag employees for "Internal Mobility" in ERP | HR Manager | CHRO | 2 weeks |
| 2 | **Succession Mapping**: Identify "Ready Now" and "Ready in 1–2 Years" successors for all Store Manager and HQ Director roles | Department Head | CEO | 1 week |
| 3 | **Individual Development Plan (IDP)**: Successors assigned to specific training (W51) and cross-functional rotations | HR Manager | — | 1 year |
| 4 | **Internal Posting**: Vacancies posted internally for 5 days before external search; system alerts eligible internal candidates | System | HR Manager | Automated |
| 5 | **Transfer/Promotion**: Selected candidate's contract and payroll (W10) updated; system auto-triggers offboarding from old role and onboarding to new | System / HR | — | 30 min |

### System Touchpoints
- Talent pool tagging in HRIS
- Career path visualization and tracking
- Automatic internal job alerts based on profile

---

## W179. Management Trainee (Cadetship) Program

| Field | Detail |
|---|---|
| **Trigger** | Annual corporate strategy (10–15 new stores/year growth) |
| **Frequency** | Annual intake (Cohort-based) |
| **Volume** | ~30–50 trainees per year |
| **Owner** | CHRO |
| **Participants** | Store Managers (Mentors), Trainees, Learning & Development Team |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Recruitment**: Campus hiring and assessment centers targeting fresh graduates | HR Manager | — | 2 months |
| 2 | **Orientation**: 1-week corporate orientation at HQ | L&D Team | CHRO | 1 week |
| 3 | **Rotational Training**: 6-month rotation through all store departments (Receiving, Sales, Cashier, Operations) | Trainee | Store Manager | 6 months |
| 4 | **Project Assignment**: Trainees assigned a "Process Improvement" project in a specific store | Trainee | Dept Head | 2 months |
| 5 | **Graduation & Deployment**: Successful trainees deployed as "Assistant Store Managers" or "Department Supervisors" in new stores | CHRO | CEO | — |

### System Touchpoints
- Training progress tracking (W51)
- Rotation schedule management (W34)
- Trainee-to-Mentor mapping and feedback loop

---

## W251. Philippine Statutory Benefits & Claims Administration (SSS, PhilHealth, Pag-IBIG)

| Field | Detail |
|---|---|
| **Trigger** | Employee sickness event, maternity event, or application for SSS/Pag-IBIG statutory loan |
| **Frequency** | Continuous; daily processing of claims and semi-monthly reconciliation |
| **Volume** | ~7,060 employee base; average ~120–180 sickness claims/month, ~40–60 maternity leaves/month, and ~250–350 loan applications/month |
| **Owner** | HR Benefits Specialist |
| **Participants** | Employee, HR Benefits Specialist, Payroll Specialist, Finance (Treasury) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Claim Submission**: Employee uploads medical certificate, SSS Maternity Notification, or loan request documents to the HRIS/ERP system via Employee Self-Service (ESS) portal (W251.1) | Employee | — | 15 min |
| 2 | **Eligibility Verification**: HR Benefits Specialist reviews the uploaded documents; system auto-checks employee contribution history against SSS/PhilHealth criteria to verify eligibility (W251.2) | HR Benefits | CHRO | 30 min |
| 3 | **Agency Portal Certification**: HR Benefits Specialist logs into the government agency's online portal (SSS Sickness/Maternity portal, Pag-IBIG Virtual Employer portal) to certify the employee's leave or confirm the employer endorsement for a salary/calamity loan (W251.3) | HR Benefits | — | 20 min |
| 4 | **Benefit Advance Computation**: For SSS Sickness/Maternity, under Philippine law, the employer must advance the SSS benefit. System automatically computes the daily SSS benefit rate based on the employee's average daily salary credit and schedules the advance payment (W251.4) | System | Payroll Mgr | Automated |
| 5 | **Payroll Disbursal**: Payroll Specialist reviews the computed statutory advance and approves it for inclusion in the next semi-monthly payroll run (W10) (W251.5) | Payroll Spec | Payroll Mgr | 10 min |
| 6 | **Reimbursement Claim Submission**: After the employee returns or the leave completes, HR Benefits Specialist submits a digitized SSS Reimbursement Claim via the online portal to recover the advanced amount from the government (W251.6) | HR Benefits | — | 15 min |
| 7 | **Reconciliation & Settlement**: SSS releases the reimbursement via direct deposit to the company's bank account. Finance reconciles the incoming bank settlement against the SSS Receivable ledger to close the transaction loop (W251.7) | Treasury / Accountant | Controller | 30 min |
| 8 | **Loan Deduction Scheduling**: For SSS/Pag-IBIG loans, once approved, the system imports the monthly electronic billing files from SSS/Pag-IBIG, matches loan accounts with active employee profiles, and schedules the statutory semi-monthly deductions in the payroll system, ensuring compliance with minimum wage take-home pay rules (W251.8) | System | Payroll Mgr | Automated |

### System Touchpoints
- Employee Self-Service (ESS) portal for digital document upload and notification tracking
- HRIS Integration with Payroll (W10) for automated advanced benefit calculation and statutory loan deductions
- General Ledger integration: SSS Receivable reconciliation and bank settlement auto-matching (W89)
- Government billing file import interface (semi-monthly SSS and Pag-IBIG billing formats)


