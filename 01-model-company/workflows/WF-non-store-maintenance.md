# Facility & Asset Maintenance (HQ & DC) Workflows

> Maintenance of non-store facilities: Distribution Centers (DCs), Head Office (HQ), and specialized DC equipment.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W240. DC Facility & Warehouse Equipment Maintenance](#dc-facility--warehouse-equipment-maintenance)
- [W241. HQ Office Facility & Executive Asset Maintenance](#hq-office-facility--executive-asset-maintenance)
- [W242. 3PL & Logistics Partner Performance Review](#3pl--logistics-partner-performance-review)
- [W243. Power of Attorney (POA) & Board Resolution Lifecycle](#power-of-attorney-poa--board-resolution-lifecycle)

---

## W240. DC Facility & Warehouse Equipment Maintenance

| Field | Detail |
|---|---|
| **Trigger** | Odometer/Hour-meter reading (Forklifts); or scheduled facility audit |
| **Frequency** | Weekly/Monthly/Quarterly |
| **Owner** | DC Maintenance Supervisor |
| **Participants** | DC Staff, External Technicians |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Inspection**: Weekly walk-through of DC (Racking, Lighting, Flooring, Fire Sprinklers) | Maint Supervisor | — | 2 hours |
| 2 | **Equipment PM**: Preventive Maintenance (PM) for Forklifts, Conveyors, and Dock Levelers | Technician | Maint Supervisor | 4 hours |
| 3 | **Racking Audit**: Annual structural audit of pallet racking (Philippine Seismic Code compliance) | Ext Auditor | DC Manager | 2 days |
| 4 | **Work Order**: Create repairs in W47 system for any failures | Maint Supervisor | — | 10 min |

---

## W241. HQ Office Facility & Executive Asset Maintenance

| Field | Detail |
|---|---|
| **Trigger** | Employee request; or scheduled lease/utility review |
| **Frequency** | Ongoing |
| **Owner** | HQ Facilities Manager |
| **Participants** | Office Admin, IT, Vendors |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Request Intake**: Employee submits HQ facility request (AC cooling, lighting, furniture) | Employee | — | 5 min |
| 2 | **Asset Tracking**: Maintain register of HQ-specific assets (Boardroom AV, Gym equipment, Executive vehicles) | Office Admin | Facilities Mgr | Ongoing |
| 3 | **Vendor Management**: Manage contracts for Cleaning, Security, and Canteen services (W62) | Facilities Mgr | — | Monthly |

---

## W242. 3PL & Logistics Partner Performance Review

| Field | Detail |
|---|---|
| **Trigger** | Quarterly review calendar |
| **Frequency** | Quarterly |
| **Volume** | ~5–10 key logistics partners |
| **Owner** | Fleet Manager |
| **Participants** | DC Dispatch, Customer Experience, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **KPI Aggregation**: Compile On-Time Delivery (OTD), Damage Rate, and Billing Accuracy for the 3PL | System | Fleet Manager | 2 hours |
| 2 | **CX Feedback**: Review customer complaints/satisfaction related to 3PL deliveries (W41) | CX Manager | — | 1 hour |
| 3 | **Review Meeting**: Present findings to 3PL executives; identify improvement areas | Fleet Manager | Supply Chain Mgr | 2 hours |
| 4 | **Rate Review**: Compare 3PL performance vs. contract rates; initiate re-negotiation if needed | Fleet Manager | — | 1 day |

---

## W243. Power of Attorney (POA) & Board Resolution Lifecycle

| Field | Detail |
|---|---|
| **Trigger** | Need for specific authorization (Bank, Government, Contracts) |
| **Frequency** | Ad-hoc; ~10–20 per month |
| **Owner** | Corporate Secretary |
| **Participants** | Board of Directors, Legal, Authorized Signatories |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Request**: Dept Head requests specific authority (e.g., to sign LTO documents or open bank account) | Dept Head | Legal Counsel | 15 min |
| 2 | **Drafting**: Corp Sec drafts Board Resolution or Secretary's Certificate | Corp Sec | — | 1 hour |
| 3 | **Approval**: Circulate to Board for signature (Digital or Physical) | Corp Sec | Chairman | 2 days |
| 4 | **Notarization**: Obtain notarization (Mandatory for PH legal documents) | Legal Assistant | — | 4 hours |
| 5 | **Register**: Upload scanned copy to "Authority Matrix" / POA Register; issue to requestor | Legal Assistant | — | 10 min |
| 6 | **Expiry Tracking**: Monitor expiry of specific POAs; trigger renewal 30 days before | Legal Assistant | — | Monthly |

### System Touchpoints
- WMS maintenance module
- Contract Management (W62) for 3PLs
- Digital Asset Register for HQ/DC equipment
- Legal Document Management (DMS) for POAs/Resolutions
- Integration with W140 (Incidents), W52 (Fleet), W124 (Corp Sec)
