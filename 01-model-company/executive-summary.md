# BuildRight Depot Corp. — Executive Summary

> One-page overview of the model company and ERP evaluation program for C-suite stakeholders.

---

## The Company

**BuildRight Depot Corp.** is a theoretical big-box hardware/home improvement retail chain in the Philippines, designed as a rigorous test case for ERP platform evaluation.

| Parameter | Value |
|---|---|
| Format | Hardware / DIY / Home Improvement Big Box |
| Stores | 200 (nationwide: Luzon, Visayas, Mindanao) |
| Distribution Centers | 5 (Davao, Cebu, Laguna, Clark, Manila) |
| HQ | Davao City, Philippines |
| Legal Entities | 5 (Holdings, Depot, Logistics, Digital Commerce, Property Mgmt) |
| Annual Revenue | ~PHP 62.3 Billion |
| Employees | ~7,060 |
| Active SKUs | 35,000 |
| POS Terminals | 1,000 (5 per store) |
| Monthly Transactions | 2.8 million |
| Ecommerce | Yes — BOPIS + Home Delivery |
| Loyalty Members | ~600,000 |

---

## Why This Model?

Inspired by **Wilcon Depot** (PSE: WLCON), the Philippines' largest home improvement retailer (~100 stores, ~PHP 33–35B revenue). BuildRight is designed at **2× Wilcon's current scale** to stress-test ERP platforms for growth. Key differentiators vs. Wilcon: more stores, more DCs, multi-entity structure, Davao-based HQ.

---

## What We're Evaluating

Four ERP platforms for ability to run BuildRight end-to-end:

| Platform | Vendor | Status |
|---|---|---|
| SAP S/4HANA Cloud | SAP | Not Started |
| Oracle NetSuite | Oracle | Not Started |
| Microsoft Dynamics 365 | Microsoft | Not Started |
| Odoo Enterprise | Odoo | Not Started |

---

## Critical Requirements

The ERP must handle these non-negotiables:

1. **High-volume retail POS** — 2.8M transactions/month, 1,000 terminals, offline capability
2. **Multi-entity Philippine operations** — 5 legal entities with intercompany consolidation, BIR compliance (VAT, EWT, income tax), SSS/PhilHealth/Pag-IBIG payroll
3. **Complex supply chain** — 5 DCs, import management (LC, customs, landed cost), catch-weight items (lumber, wire), consignment, VMI
4. **Omnichannel** — BOPIS + home delivery with real-time inventory sync across 200 stores
5. **Scalability** — must grow to 300+ stores without architectural limits

---

## Evaluation Methodology

- **261 requirements** scored across 18 categories with weighted priorities
- **5 evaluation dimensions**: Functional Fit (40%), TCO (20%), Implementation Risk (15%), Scalability (15%), Local Support (10%)
- **Phased rollout plan**: 26 months, pilot 5 stores → 7 waves nationwide

---

## Repository Structure

```
erpplans/
├── 01-model-company/       ← Company profile, requirements, workflows (COMPLETE)
├── 02-wilcon-benchmark/    ← Real-world benchmark research (COMPLETE)
├── 03-sap/                 ← SAP evaluation (NOT STARTED)
├── 04-oracle-netsuite/     ← NetSuite evaluation (NOT STARTED)
├── 05-microsoft-d365/      ← D365 evaluation (NOT STARTED)
├── 06-odoo/                ← Odoo evaluation (NOT STARTED)
└── 07-methodology/         ← Scoring, roadmap, technical guidelines (COMPLETE)
```

---

## Key Metrics for Decision-Making

| Metric | Target | Why It Matters |
|---|---|---|
| POS uptime | 99.9% | Revenue stops if registers go down |
| POS offline endurance | ≥ 8 hours | Philippine internet reliability |
| Month-end close | ≤ 5 working days | Financial reporting agility |
| Inventory accuracy | ≥ 97% | Shrinkage control at PHP 62B scale |
| System implementation | ≤ 26 months | Time-to-value |
| 5-year TCO | TBD per ERP | Total cost of ownership |

---

## Next Steps

1. Complete fit-gap analysis for each ERP platform
2. Conduct vendor demos using BuildRight scenarios
3. Produce architecture designs and cost estimates
4. Score and shortlist top 2
5. Deep-dive / POC with shortlisted vendors
6. Final selection

---

*Date: 2026-06-02*
