# Real Estate & Lease Management Workflows

> Site selection, lease administration, rent processing, and property tax management.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W116. Site Selection & Feasibility Analysis](#site-selection-feasibility-analysis)
- [W117. Lease Administration & Renewal](#lease-administration-renewal)
- [W118. Rent & CAM Payment Processing](#rent-cam-payment-processing)
- [W119. Real Property Tax (Amillaramento) Management](#real-property-tax-amillaramento-management)

---

## W116. Site Selection & Feasibility Analysis

| Field | Detail |
|---|---|
| **Trigger** | Strategic growth plan (10–15 new stores/year target) |
| **Frequency** | Ongoing; ~15–20 sites evaluated monthly |
| **Volume** | ~10–15 approved sites/year |
| **Owner** | VP for Property Management |
| **Participants** | Property Acquisition Manager, Finance (ROI analysis), CEO/Board (approval) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Identify potential site (greenfield or existing building) based on catchment analysis | Property Manager | VP Property | 1–2 weeks |
| 2 | Conduct site survey: size (8k–15k sqm), zoning, access, utilities, competitors | Property Manager | VP Property | 3–5 days |
| 3 | Financial Feasibility: Calculate projected store sales (W13) vs. build/lease cost | Finance Analyst | CFO | 2–3 days |
| 4 | Draft Letter of Intent (LOI) and initial lease terms | Property Manager | VP Property | 2 days |
| 5 | Present Site Selection Memo to Board/CEO for approval | VP Property | CEO | 1 hour |
| 6 | Execute Lease Agreement (W117) | Legal / VP Property | VP Property | 1–2 weeks |

---

## W117. Lease Administration & Renewal

| Field | Detail |
|---|---|
| **Trigger** | Signed lease or upcoming expiry (12–18 months prior) |
| **Frequency** | Managed per contract; ~200+ active leases |
| **Volume** | ~20–30 renewals/year |
| **Owner** | Lease Administrator |
| **Participants** | VP Property, Legal, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Input new lease into ERP: terms, escalations (e.g., 5% every 2 years), grace periods | Lease Admin | VP Property | 2 hours |
| 2 | System flags upcoming expiry (T-minus 18 months) | System | — | Automated |
| 3 | Evaluate store performance and strategic value of location | Store Ops / Finance | COO | 1 week |
| 4 | Negotiate renewal terms with lessor | VP Property | VP Property | 2–4 weeks |
| 5 | Legal review of renewal addendum | Legal Counsel | VP Legal | 3–5 days |
| 6 | Update ERP with new lease end date and revised escalation schedule | Lease Admin | VP Property | 1 hour |

---

## W118. Rent & CAM Payment Processing

| Field | Detail |
|---|---|
| **Trigger** | Monthly billing or lease schedule |
| **Frequency** | Monthly |
| **Volume** | ~250 payments/month (Stores, DCs, Offices, Parking) |
| **Owner** | AP Specialist (Lease) |
| **Participants** | Lease Administrator, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates payment schedule for base rent per lease master | System | — | Automated |
| 2 | Receive lessor invoice for Common Area Maintenance (CAM) and utility recharges | Lease Admin | — | Monthly |
| 3 | Validate CAM charges against lease caps/clauses | Lease Admin | VP Property | 30 min/inv |
| 4 | Create AP voucher in ERP (2-way match: Invoice to Lease Master) | AP Specialist | AP Supervisor | 15 min/inv |
| 5 | Route for approval per tiered matrix | AP Supervisor | Finance Manager | 10 min/inv |
| 6 | Release payment (Check or Bank Transfer) | Treasury | CFO | 1 day |

---

## W119. Real Property Tax (Amillaramento) Management

| Field | Detail |
|---|---|
| **Trigger** | Annual/Quarterly tax assessment from LGU |
| **Frequency** | Annual (with quarterly installment options) |
| **Volume** | ~50 owned sites (Land/Building) |
| **Owner** | Tax Manager |
| **Participants** | Lease Admin (for records), Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Consolidate list of owned properties and current tax declarations | Lease Admin | VP Property | 2 days |
| 2 | Receive Tax Bill from LGU (Provincial/City Treasurer) | Tax Manager | — | Annual |
| 3 | Validate assessment against previous year and improvements made | Tax Manager | CFO | 1 hour/site |
| 4 | Calculate prompt-payment discounts (if applicable) | Tax Manager | Tax Manager | 15 min/site |
| 5 | Process payment via manager's check or bank transfer to LGU | Treasury | CFO | 1–2 days |
| 6 | File receipt and update property records in ERP (Fixed Asset module) | Lease Admin | — | 30 min |

---

### System Touchpoints (Property)
- Lease master data: terms, escalations, renewals, security deposits
- Automated expiry alerts (W117)
- Integration with AP for recurring rent payments (W118)
- Fixed Asset integration for owned property tax tracking (W119)
- Document management for scanned lease agreements and tax receipts
