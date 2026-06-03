# ERP Implementation — High-Level Roadmap

> This document outlines the phased implementation plan for the selected ERP platform
> at BuildRight Depot Corp. The approach is phased rollout starting with a pilot group
> of stores before nationwide deployment.

---

## 1. Implementation Strategy

| Parameter | Decision |
|---|---|
| **Approach** | Phased rollout (not big-bang) |
| **Pilot Scope** | 5 stores + 1 DC + HQ finance |
| **Pilot Location** | Mindanao region (near HQ; Davao City stores) |
| **Wave Size** | 20–30 stores per wave after pilot |
| **Total Waves** | ~8–10 waves over 12–18 months |
| **Go-Live Strategy** | Module-by-module within pilot, then full-stack per wave |

### Why Phased Rollout?
- **De-risk POS**: 2.8M monthly transactions cannot be cut over in one event
- **Learn and adjust**: Pilot stores reveal process gaps before scale
- **Resource management**: Training 6,000 store staff requires sequencing
- **Supply chain stability**: DC operations must be stable before loading all stores

---

## 2. Implementation Phases

### Phase 0: Project Setup (Months 1–2)

| Activity | Duration | Owner |
|---|---|---|
| ERP vendor contract & SOW | 4 weeks | CFO + CIO |
| Implementation partner selection | 4 weeks | CIO + Procurement |
| Project governance setup (steerco, PMO) | 2 weeks | CIO |
| Project team formation (core + extended) | 2 weeks | CIO + Department Heads |
| Project kickoff | 1 day | All |
| Detailed project plan refinement | 2 weeks | PMO + Implementation Partner |

**Deliverables**: Signed SOW, project charter, governance framework, resource plan

### Phase 1: Design & Configure (Months 3–6)

| Activity | Duration | Notes |
|---|---|---|
| Business process workshops (BPML) | 4 weeks | All modules; document current vs. future state |
| Solution design document | 3 weeks | Fit-gap confirmation; identify customizations |
| System configuration (core modules) | 6 weeks | Finance, inventory, procurement, HR |
| POS configuration & integration design | 4 weeks | Offline mode, payment devices, receipt format |
| Ecommerce integration design | 2 weeks | API mapping, inventory sync, BOPIS flow |
| Data migration strategy & mapping | 3 weeks | Legacy data extraction, transformation, load plan |
| Integration architecture finalized | 2 weeks | All touchpoints in [Data Volumes §3](../01-model-company/data-volumes-and-integrations.md#3-integration-detail-matrix) |

**Deliverables**: Solution design document, configured sandbox, data migration plan

### Phase 2: Build & Test (Months 7–9)

| Activity | Duration | Notes |
|---|---|---|
| Customization / extension development | 6 weeks | Minimize custom code; prefer configuration |
| Integration development | 4 weeks | POS, ecommerce, banks, BIR, statutory |
| Data migration scripts & test loads | 3 weeks | Run at least 3 test migrations |
| POS hardware staging & imaging | 3 weeks | 25 terminals for pilot (5 stores × 5) |
| WMS configuration & RF gun setup | 3 weeks | DC1 (Davao) only for pilot |
| **SIT (System Integration Testing)** | 3 weeks | End-to-end process testing |
| **UAT (User Acceptance Testing)** | 3 weeks | Business users validate scenarios |
| Performance / load testing | 2 weeks | Simulate peak POS volumes |
| Security & penetration testing | 1 week | External security review |
| Cutover rehearsal | 1 week | Dry run of go-live weekend |

**Deliverables**: Tested system, signed-off UAT, performance test report

### Phase 3: Pilot Go-Live (Months 10–11)

| Activity | Duration | Notes |
|---|---|---|
| Pilot scope: 5 Davao stores + DC1 + HQ Finance | | |
| Data migration (final load) | Weekend | Legacy → ERP cut-over |
| POS hardware deployment (5 stores) | 1 week | Install, test, train |
| Hypercare / floor support | 4 weeks | On-site support team at each pilot store |
| Daily issue triage & resolution | Ongoing | PMO-led |
| Pilot lessons learned | 1 week | Document adjustments for Wave 1 |

**Pilot Success Criteria**:
- All 5 stores processing transactions on new POS
- DC1 receiving, picking, and shipping on new WMS
- HQ finance posting entries and generating reports
- Inventory accuracy ≥ 95% at pilot stores
- POS transaction success rate ≥ 99.5%
- Zero critical (P1) open defects after Week 2

### Phase 4: Wave Rollout (Months 12–22)

| Wave | Stores | Region | DC | Timeline |
|---|---|---|---|---|
| **Wave 1** | 20 | Mindanao (remaining) | — | Month 12 |
| **Wave 2** | 25 | Visayas | DC2 (Cebu) | Month 14 |
| **Wave 3** | 25 | Visayas (remaining) | — | Month 15 |
| **Wave 4** | 30 | South Luzon + NCR | DC3 (Laguna) + DC5 (Valenzuela) | Month 17 |
| **Wave 5** | 30 | NCR + South Luzon | — | Month 18 |
| **Wave 6** | 25 | North/Central Luzon | DC4 (Clark) | Month 20 |
| **Wave 7** | 40 | Remaining stores | — | Month 22 |

> **Note**: Wave sizes may be adjusted based on pilot learnings. Each wave follows:
> 1. Pre-wave training (2 weeks) → 2. Hardware deploy (1 week) → 3. Go-live weekend → 4. Hypercare (2 weeks)

### Phase 5: Optimization & BAU (Months 23–26)

| Activity | Duration | Notes |
|---|---|---|
| Ecommerce full integration go-live | — | May launch earlier in pilot region |
| Demand planning / forecasting activation | 4 weeks | Requires 3–6 months of historical data in system |
| Advanced analytics / BI dashboards | 4 weeks | Executive and operational dashboards |
| Loyalty program integration | 3 weeks | Full points earn/redeem at POS and online |
| Process optimization | Ongoing | Continuous improvement based on user feedback |
| Knowledge transfer & BAU support model | 4 weeks | Transition from implementation partner to internal IT |

---

## 3. Data Migration Plan

### Legacy Systems to Migrate

| Source System | Data to Migrate | Strategy |
|---|---|---|
| Legacy accounting | GL balances, open AP/AR, fixed assets | Balances as of go-live date; open items migrated individually |
| Standalone POS | Historical sales (12 months) | Summarized daily sales by store; detailed last 3 months only |
| Spreadsheet purchasing | Open POs, vendor master | Active POs migrated; vendor master cleansed |
| Payroll software | Employee master, YTD earnings | Full employee master + year-to-date for BIR reconciliation |
| Custom ecommerce | Customer accounts, order history | Loyalty members migrated; order history last 6 months |
| Manual inventory | On-hand quantities per store/DC | Full wall-to-wall physical count at go-live; counts loaded as opening balances |

### Data Migration Principles
1. **Cleanse before migrating**: De-duplicate vendors, customers, and items before load
2. **Historical data**: Minimum 12 months summarized; 3 years for financial reporting
3. **Parallel run**: Run legacy and new system simultaneously for 1 payroll cycle and 1 month-end close during pilot
4. **Archived access**: Legacy systems placed in read-only mode for 7 years (BIR retention)

---

## 4. Change Management & Training

### Training Approach

| Audience | Training Method | Duration | Timing |
|---|---|---|---|
| Core project team (20) | Vendor-led deep training | 2 weeks | Phase 1 |
| Department super-users (50) | Train-the-trainer | 1 week per module | Phase 2 |
| HQ staff (300) | Classroom + e-learning | 2–3 days per role | Pre-pilot |
| Store managers (200) | Classroom + hands-on POS | 2 days | Pre-wave |
| Store staff (6,800) | On-site training by super-users | 1 day | Pre-wave (1 week before go-live) |
| DC staff (750) | Hands-on WMS + RF gun training | 2 days | Pre-DC go-live |
| Executives (10) | Dashboard & report orientation | Half day | Post-pilot |

### Change Management Activities
- Executive sponsor communications (bi-weekly)
- Store manager town halls (pre-wave)
- "ERP Champions" program (1 per store; 200 total)
- Quick-reference cards at every POS and workstation
- Post-go-live help desk (first 30 days per wave)

---

## 5. Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| POS offline failure during go-live | Medium | Critical | Pilot validates offline mode; fallback to manual selling procedures |
| Data migration errors (inventory) | High | High | Pre-migration physical count; reconciliation reports before go-live |
| User resistance / low adoption | Medium | High | Change management program; ERP champions; management KPI alignment |
| Integration failure (POS ↔ ERP) | Medium | Critical | SIT stress testing; fallback batch mode; monitoring alerts |
| Philippine localization gaps | Medium | High | Early validation of BIR/SSS compliance in Phase 1; partner assessment |
| Scope creep | High | Medium | Fixed scope per phase; change control board |
| Implementation partner underperformance | Medium | High | Milestone-based payments; contractual SLA; backup partner identified |

---

## 6. Project Governance

```
Steering Committee (meets monthly)
├── Sponsor: CEO
├── Members: CFO, COO, CIO, CMO, CHRO
└── Decision authority: scope changes, budget, timeline

Project Management Office (PMO)
├── Project Director (internal)
├── Project Manager (implementation partner)
├── Weekly status reports → Steerco monthly
└── Risk/issue escalation within 24 hours

Workstreams
├── Finance & Accounting
├── Supply Chain & Inventory
├── POS & Retail Operations
├── Ecommerce & Digital
├── HR & Payroll
├── Data Migration
├── Infrastructure & Security
└── Training & Change Management
```

---

## 7. Timeline Summary

```
Month:  1   2   3   4   5   6   7   8   9   10  11  12  ... 22  23  24  25  26
        ├───────┤                                                   ├───────────┤
Phase:  0:Setup     Phase 1:Design        Phase 5:Optimization & BAU
              ├───────────────────┤
              Phase 2:Build & Test
                            ├───────────┤
                            Phase 3:Pilot
                                    ├───────────────────────────────┤
                                    Phase 4:Wave Rollout (stores)
```

**Total Project Duration**: ~26 months (Phase 0 through Phase 5)

---

*Document Version: 1.0 | Date: 2026-05-30*
