# Health, Safety & Environment (HSE) Workflows

> Management of occupational health and safety (OHS), incident reporting, and safety compliance.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W140. Occupational Health & Safety (OHS) Incident Management](#ohs-incident-management)
- [W141. Workplace Safety Inspection & Audit](#workplace-safety-inspection--audit)
- [W187. Contractor & Third-Party On-site Safety Orientation](#contractor--third-party-on-site-safety-orientation)

---

## W140. Occupational Health & Safety (OHS) Incident Management

| Field | Detail |
|---|---|
| **Trigger** | Workplace accident, "near miss," or safety hazard reported (involving employee, customer, or contractor) |
| **Frequency** | Ad-hoc; ~50–100 reportable incidents/year chain-wide |
| **Volume** | Covers all 200 stores, 4 DCs, and HQ |
| **Owner** | Safety Officer (HQ/DC); Store Manager (Store) |
| **Participants** | Affected Individual, First Aider, Store/DC Manager, HR, Legal, Insurance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Emergency Response**: Immediate first aid or medical evacuation; secure the scene to prevent further injury | First Aider / Manager | Store Manager | Immediate |
| 2 | **Incident Reporting**: Manager creates Incident Report in system within 2 hours: date/time, location, individuals involved, description of event, and immediate actions taken | Store/DC Manager | Safety Officer | 20 min |
| 3 | **Evidence Capture**: Upload photos of the scene, witness statements, and CCTV footage to the incident record | Store/DC Manager | — | 30 min |
| 4 | **Investigation**: Safety Officer conducts root cause analysis (e.g., "5 Whys"); classifies incident (Minor, Medical Treatment, Lost Time Injury, Fatality) | Safety Officer | VP HR | 1–3 days |
| 5 | **Corrective Action (CAPA)**: System generates CAPA tasks (e.g., repair floor, replace PPE, retraining); tracks completion | Safety Officer | Dept Head | Varies |
| 6 | **Regulatory Notification**: If required (e.g., serious injury), DPO/Safety Officer notifies DOLE (Department of Labor and Employment) within prescribed timelines | Safety Officer | Legal Head | 4 hours |
| 7 | **Insurance/Claims**: If involving customer injury or significant property damage, initiate insurance claim per W3.6a | Store Manager / Finance | CFO | Per W3.6a |
| 8 | **Closure**: Review all actions completed; Safety Officer closes the case; system archives for 10 years | Safety Officer | VP HR | 15 min |
| 9 | **Monthly Review**: Monthly Safety Committee meeting reviews incident trends, "near miss" patterns, and CAPA completion rates | Safety Committee | CEO | 2 hours/month |

---

## W141. Workplace Safety Inspection & Audit

| Field | Detail |
|---|---|
| **Trigger** | Scheduled monthly inspection; or pre-opening checklist for new store |
| **Frequency** | Monthly per location |
| **Volume** | ~205 inspections/month |
| **Owner** | Safety Officer |
| **Participants** | Store/DC Manager, Maintenance, external fire/safety inspectors |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Inspection Prep**: System generates monthly inspection checklist for the location (tailored for Store vs. DC) | System | Safety Officer | Automated |
| 2 | **Walkthrough**: Manager/Safety Officer conducts physical inspection: fire exits clear, fire extinguishers charged, racking integrity (DC), spill kits stocked, PPE usage, electrical safety | Store/DC Manager | Safety Officer | 1–2 hours |
| 3 | **Findings Logging**: Record "Pass/Fail" for each item; capture photos of any non-compliance | Store/DC Manager | — | 30 min |
| 4 | **Immediate Fixes**: Resolve low-risk items immediately (e.g., move a box blocking an exit); log as "Corrected on Site" | Store/DC Manager | — | Ongoing |
| 5 | **Maintenance Request**: For structural/equipment issues, auto-generate Work Order in Facilities Mgmt system (W47) | System | Maintenance | Automated |
| 6 | **Certification Tracking**: System tracks expiry of mandatory certifications: Fire Safety Inspection Certificate (FSIC), Elevator/Escalator permits, Forklift operator licenses | Safety Officer | Regulatory Officer | 15 min/month |
| 7 | **Dashboard**: Safety Officer reviews "Safety Compliance Score" per region/location; flags high-risk locations for unannounced audit | Safety Officer | VP Store Ops | 1 hour/month |

### System Touchpoints
- Mobile-friendly Safety Inspection App with photo/GPS capture
- Automated integration with Facilities Maintenance (W47) for repairs
- Compliance calendar with automated alerts for permit/license expiries
- Incident analytics dashboard for trend reporting

---

## W187. Contractor & Third-Party On-site Safety Orientation

| Field | Detail |
|---|---|
| **Trigger** | Contractor or 3rd party arriving to perform work (maintenance, construction, cleaning) |
| **Frequency** | As occurred |
| **Volume** | ~500–1,000 orientations/month chain-wide |
| **Owner** | Store Manager / DC Manager |
| **Participants** | Contractor Supervisor, Safety Officer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Contractor signs in at Security/Receiving; presents work order and valid ID | Security | — | 10 min |
| 2 | Manager/Safety Officer verifies Contractor Insurance & Accreditation (W62) | Manager | — | 5 min |
| 3 | Contractor undergoes "Safety Briefing": fire exits, PPE requirements, hazardous areas, emergency contacts | Manager | Safety Officer | 20 min |
| 4 | Contractor signs digital "Safety Acknowledgement" and "Permit to Work" (for hot work, height work, or confined space) | Contractor | Manager | 10 min |
| 5 | Security issues "Contractor Badge"; logs entry time in ERP | Security | — | 5 min |
| 6 | Periodic monitoring: Safety Officer checks contractor compliance during the shift | Safety Officer | — | Ongoing |
| 7 | Completion: Contractor signs out; Security logs exit time; Badge returned | Security | — | 5 min |

### System Touchpoints
- Contractor Management Module with Accreditation status (W187.2)
- Digital Safety Induction & Permit-to-Work Portal (W187.4)
- Visitor/Contractor Log integrated with ERP Access Control (W187.5)

