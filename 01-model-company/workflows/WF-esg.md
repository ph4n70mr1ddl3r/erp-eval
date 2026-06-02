# ESG & Sustainability Reporting Workflows

> Management of carbon footprint tracking, waste reduction, circular economy initiatives, and social impact reporting.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W192. Greenhouse Gas (GHG) Emissions Tracking](#ghg-emissions-tracking)
- [W193. Waste Management & Circular Economy](#waste-management--circular-economy)
- [W194. Social Impact & Community Development (CSR)](#social-impact--community-development)
- [W195. Sustainable Sourcing & Ethical Vendor Audit](#sustainable-sourcing--ethical-vendor-audit)

---

## W192. Greenhouse Gas (GHG) Emissions Tracking

| Field | Detail |
|---|---|
| **Trigger** | Monthly utility billing; or fuel consumption report |
| **Frequency** | Monthly |
| **Volume** | Covers 200 stores, 5 DCs, HQ, and Fleet |
| **Owner** | Sustainability Lead |
| **Participants** | Finance (Utility payments), Fleet Manager (Fuel), Maintenance, Sustainability Lead |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Data Collection (Scope 1 - Direct)**: System pulls fuel consumption data from fleet management (W196) and backup generators | Fleet Manager | Sustainability Lead | 1 hour |
| 2 | **Data Collection (Scope 2 - Indirect)**: System pulls electricity (kWh) consumption from utility invoices (W7) and solar generation data (W173) | AP Clerk | Finance Manager | 1 hour |
| 3 | **Emission Calculation**: Sustainability Lead applies Philippine-specific emission factors (from DOE/DENR) to convert fuel and electricity data into CO2e (CO2 equivalent) | Sustainability Lead | — | 2 hours |
| 4 | **Scope 3 (Supply Chain)**: (Optional) Estimate emissions from 3PL logistics (W62B) and employee travel (W74) | Sustainability Lead | — | 4 hours |
| 5 | **Validation**: Internal Audit or external consultant verifies the calculations for accuracy | Internal Audit | — | Annual |
| 6 | **Dashboard**: System updates "Environmental Scorecard" showing emissions intensity (CO2e per PHP 1M revenue) | System | Sustainability Lead | Automated |

---

## W193. Waste Management & Circular Economy

| Field | Detail |
|---|---|
| **Trigger** | Generation of scrap (W169), damaged goods (W91), or office waste |
| **Frequency** | Weekly collections |
| **Volume** | Significant wood, plastic, and metal scrap from 200 locations |
| **Owner** | Environmental Compliance Officer |
| **Participants** | Store/DC Manager, Scrap Vendor, Sustainability Lead |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Sorting**: Store/DC staff sort waste at source: (a) Recyclables (Cardboard, Wood off-cuts, Plastic wrap); (b) Hazardous (W82); (c) General Waste | Store/DC Staff | Manager | Ongoing |
| 2 | **Recovery**: Wood off-cuts from cutting services (W169) are moved to "Remnant Sale" or donated for community building | Cutter | Store Manager | 15 min |
| 3 | **Vendor Collection**: Accredited recycling vendors collect sorted waste; record weights in the system | Vendor / Manager | — | 30 min |
| 4 | **Waste Diversion Tracking**: System logs weight diverted from landfill vs. total waste generated | Environmental Officer | Sustainability Lead | Monthly |
| 5 | **Impact Reporting**: Calculate "Trees Saved" or "Plastic Prevented" for use in annual ESG report | Sustainability Lead | CMO | Quarterly |

---

## W194. Social Impact & Community Development (CSR)

| Field | Detail |
|---|---|
| **Trigger** | Approved CSR initiative (e.g., "BuildRight Homes for Mindanao") |
| **Frequency** | Quarterly projects |
| **Owner** | CSR Coordinator (within Marketing) |
| **Participants** | HR (Volunteers), Finance (Donations), Partner NGOs |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Project Selection**: Align CSR activity with company mission (Building supplies → Habitat for Humanity, etc.) | CSR Coordinator | CEO | 1 week |
| 2 | **Resource Allocation**: (a) Materials: Donate near-expiry or slow-moving stock (W93); (b) Cash: Direct donation per board-approved budget; (c) Time: Employee volunteer hours | CSR Coordinator | CFO / CHRO | 3 days |
| 3 | **Execution**: Distribute materials or conduct volunteer activity; capture impact metrics (houses built, families helped) | Project Team | — | Varies |
| 4 | **Communication**: PR & Social Media coverage of the initiative (W142) | Social Mgr | CMO | 1 day |
| 5 | **Reporting**: Document in ESG Report: PHP value donated, volunteer hours, and community impact | CSR Coordinator | Sustainability Lead | Quarterly |

---

## W195. Sustainable Sourcing & Ethical Vendor Audit

| Field | Detail |
|---|---|
| **Trigger** | New vendor onboarding (W36); or annual high-risk vendor review |
| **Frequency** | Annual for top 20 vendors |
| **Owner** | Sustainability Lead |
| **Participants** | Procurement (Buyer), Sustainability Lead, Internal Audit |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Self-Assessment**: Vendor completes "BuildRight Ethical Sourcing Questionnaire" covering child labor, safety, and environmental permits | Vendor | Buyer | 2 hours |
| 2 | **Risk Screening**: Sustainability Lead flags vendors based on category (e.g., lumber/quarry = high risk) or geography | Sustainability Lead | — | 30 min |
| 3 | **Audit**: Sustainability Lead or 3rd party conducts on-site or desktop audit of high-risk vendors | Sustainability Lead | VP Merch | 1–3 days |
| 4 | **Corrective Action**: If non-compliance found, vendor must execute CAPA (Corrective Action Plan) or face de-listing (W36.12) | Vendor | Sustainability Lead | 30 days |
| 5 | **Scoring**: Vendor's "Sustainability Score" integrated into the Master Vendor Scorecard (W44) | Sustainability Lead | — | 15 min |

### System Touchpoints (ESG)
- Utility consumption module (Scope 2 tracking)
- Fleet fuel integration (Scope 1 tracking)
- Waste weight logging system
- Vendor Sustainability Score in Vendor Master data
- ESG Dashboard with GRI/SASB-aligned metrics
- CSR material donation tracking (Inventory deduction with zero-price SO)
