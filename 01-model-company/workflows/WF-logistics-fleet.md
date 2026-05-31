# Fleet Operations & Driver Management Workflows

> Management of company-owned delivery fleet, driver performance, route optimization, and fuel efficiency.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W196. Route Planning & Dispatch Optimization](#route-planning--dispatch-optimization)
- [W197. Driver Performance & Safety Management](#driver-performance--safety-management)
- [W198. Fuel Management & Consumption Monitoring](#fuel-management--consumption-monitoring)
- [W199. Fleet Telematics & Real-Time Tracking](#fleet-telematics--real-time-tracking)

---

## W196. Route Planning & Dispatch Optimization

| Field | Detail |
|---|---|
| **Trigger** | Released Home Delivery orders (W19) or Store Replenishment orders (W4) |
| **Frequency** | Daily (Morning and Evening waves) |
| **Volume** | ~115 home deliveries/DC/day; ~33 store replenishments/DC/day |
| **Owner** | Logistics Planner |
| **Participants** | Logistics Planner, DC Dispatch, Drivers, 3PL Partners |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Batching**: System aggregates all pending deliveries by zone, weight, and volume (CBM) | System | Logistics Planner | Automated |
| 2 | **Vehicle Allocation**: System recommends vehicle type (10-wheeler vs. 6-wheeler vs. small van) based on load and delivery access restrictions (e.g., "Truck Ban" zones) | System | — | Automated |
| 3 | **Optimization**: Route optimization engine calculates most efficient sequence to minimize kilometers and fuel; accounts for traffic patterns and delivery windows | System | Logistics Planner | 5 min |
| 4 | **Manifest Generation**: Finalize route; system generates Trip Manifest and Load List; assigns to Driver/Vehicle | Logistics Planner | DC Manager | 10 min |
| 5 | **Driver Briefing**: Driver receives digital manifest on mobile app; verifies load; starts trip | Driver | DC Dispatch | 15 min |

---

## W197. Driver Performance & Safety Management

| Field | Detail |
|---|---|
| **Trigger** | New driver onboarding; or monthly performance review cycle |
| **Frequency** | Continuous monitoring; Monthly review |
| **Volume** | ~250–300 company drivers |
| **Owner** | Fleet Manager |
| **Participants** | Driver, Fleet Manager, Safety Officer, HR |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Licensing & Compliance**: System tracks Driver License expiries and professional certifications (e.g., Hazmat for paint) | System | Fleet Manager | Automated |
| 2 | **Safety Monitoring**: Telematics system logs events: Harsh braking, over-speeding, idling, and unauthorized stops | System | — | Real-time |
| 3 | **Incident Review**: Safety Officer reviews telematics alerts daily; conducts "Coaching Session" for frequent offenders | Safety Officer | — | 20 min |
| 4 | **Performance Scoring**: Monthly "Driver Scorecard" based on: On-time delivery %, fuel efficiency (km/L), and safety incidents | Fleet Manager | — | 30 min |
| 5 | **Rewards/Discipline**: High scorers eligible for "Safety Bonus"; low scorers trigger HR counseling (W72) | Fleet Manager | CHRO | Monthly |

---

## W198. Fuel Management & Consumption Monitoring

| Field | Detail |
|---|---|
| **Trigger** | Fueling event; or end of month |
| **Frequency** | Ongoing |
| **Volume** | ~PHP 10M–15M monthly fuel spend |
| **Owner** | Fleet Accountant |
| **Participants** | Driver, Gas Station (Vendor), Fleet Accountant, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Fueling**: Driver uses company Fuel Card; enters odometer reading at pump | Driver | — | 5 min |
| 2 | **Data Integration**: Fuel vendor (Shell/Petron) sends daily electronic file of all transactions | System | Fleet Accountant | Automated |
| 3 | **Reconciliation**: System matches fuel transaction to vehicle and compares odometer jump vs. fuel volume to calculate actual km/L | System | — | Automated |
| 4 | **Exception Alert**: System flags anomalies: (a) Fuel volume > Tank capacity; (b) Low km/L (potential fuel siphoning); (c) Fueling far from assigned route | System | Fleet Accountant | Real-time |
| 5 | **Investigation**: Fleet Manager investigates flagged transactions; if fraud confirmed, trigger W123 (Fraud Protocol) | Fleet Manager | — | 1 hour |
| 6 | **Payment**: Finance processes monthly fuel invoice; system allocates costs to specific vehicles and cost centers | Finance | Controller | Per W7 |

---

## W199. Fleet Telematics & Real-Time Tracking

| Field | Detail |
|---|---|
| **Trigger** | Vehicle starts trip |
| **Frequency** | Real-time |
| **Owner** | DC Dispatch |
| **Participants** | DC Dispatch, Customer Service, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **GPS Tracking**: System tracks vehicle location, speed, and status (moving/stopped/idle) | System | — | Real-time |
| 2 | **Dynamic ETA**: System recalculates Estimated Time of Arrival (ETA) based on live traffic; updates customer via SMS/App | System | — | Automated |
| 3 | **Geofencing**: System alerts DC Dispatch when vehicle arrives at or leaves a store/customer site; logs "Time on Site" | System | — | Automated |
| 4 | **Dispatch Dashboard**: DC Dispatch monitors all active vehicles on map; identifies delays or breakdowns | DC Dispatch | — | Continuous |
| 5 | **Maintenance Integration**: Odometer data from telematics auto-triggers "Preventive Maintenance" in W188 when thresholds reached | System | — | Automated |

### System Touchpoints (Fleet)
- Route Optimization Engine integration (W196.3)
- Telematics / GPS provider API integration (W199.1)
- Fuel Card provider data integration (W198.2)
- Driver Mobile App (Manifest, POD, Safety alerts)
- Fleet Dashboard (KPIs: Cost-per-km, Vehicle utilization, Driver safety)
- Integration with W188 (Maintenance), W10 (Driver payroll/bonus), W52 (Safety)
