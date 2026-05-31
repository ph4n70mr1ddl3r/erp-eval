# Hazardous Materials (Hazmat) & Compliance Workflows

> Storage, handling, and transportation of hazardous products (Paint, Chemicals, Adhesives, Batteries).
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W236. Hazmat Storage & Segregation Compliance (DC)](#hazmat-storage--segregation-compliance-dc)
- [W237. Hazmat Handling & Safety Training (Store)](#hazmat-handling--safety-training-store)
- [W238. Hazmat Spill Response & Incident Management](#hazmat-spill-response--incident-management)
- [W239. Customs Duty & Tax Reconciliation (BOC)](#customs-duty--tax-reconciliation-boc)

---

## W236. Hazmat Storage & Segregation Compliance (DC)

| Field | Detail |
|---|---|
| **Trigger** | Receiving of Hazmat SKUs (W3) |
| **Frequency** | Daily |
| **Volume** | ~15% of SKUs (Paint, Thinners, Adhesives, Batteries) |
| **Owner** | DC Safety Officer |
| **Participants** | DC Receiving Clerk, Putaway Staff |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Identification**: System flags incoming SKU as "Hazmat" based on SDS (Safety Data Sheet) in Item Master | System | Receiving Clerk | Automated |
| 2 | **Segregation Check**: System suggests putaway in dedicated "Hazmat Zone" (Fire-rated area) | System | — | Automated |
| 3 | **Compatibility Review**: Verify SKU is not stored adjacent to incompatible chemicals (e.g., Flammables away from Oxidizers) | DC Safety Officer | — | 10 min |
| 4 | **Containment**: Ensure secondary containment (spill pallets) is used for bulk liquid storage | Putaway Staff | DC Safety Officer | 5 min |
| 5 | **Signage**: Verify appropriate hazard placards (NFPA/GHS) are visible at the bin location | DC Safety Officer | — | 2 min |

---

## W237. Hazmat Handling & Safety Training (Store)

| Field | Detail |
|---|---|
| **Trigger** | New employee hire (W15); or annual refresher |
| **Frequency** | Annual |
| **Owner** | Store Safety Officer |
| **Participants** | Store Staff, HR |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Training Module**: Staff complete "Hazmat Handling 101" (PPE use, SDS reading, lifting techniques) | HR / Safety Officer | — | 2 hours |
| 2 | **PPE Inspection**: Daily check of available PPE (Gloves, Eye protection, Aprons) in Paint/Tile departments | Safety Officer | — | 10 min |
| 3 | **Display Safety**: Ensure chemicals on shelves are not stacked > 1.5m and are secured from falling | Dept Supervisor | — | Daily |

---

## W238. Hazmat Spill Response & Incident Management

| Field | Detail |
|---|---|
| **Trigger** | Discovery of a spill or leak (Paint, Chemical, Battery acid) |
| **Frequency** | Ad-hoc (Rare) |
| **Owner** | Safety Officer |
| **Participants** | Response Team, Store/DC Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Containment**: Evacuate immediate area; deploy spill kit (absorbent pads, socks) | Response Team | Safety Officer | 5 min |
| 2 | **Reporting**: Create Incident Report in system (W140) with photos and SDS reference | Safety Officer | Store Mgr | 15 min |
| 3 | **Cleanup**: Dispose of contaminated materials as "Hazardous Waste" per W82 | Safety Officer | — | 1 hour |
| 4 | **Inventory Adjustment**: Record loss in system via W92 (Damage) | Store Mgr | — | 5 min |

---

## W239. Customs Duty & Tax Reconciliation (BOC)

| Field | Detail |
|---|---|
| **Trigger** | Release of import shipment from Bureau of Customs (BOC) |
| **Frequency** | Per import shipment (~20–30/month) |
| **Volume** | Significant tax payments (VAT, Duties, Excise) |
| **Owner** | Import Coordinator |
| **Participants** | Finance (Tax), Customs Broker |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Payment**: Pay duties and taxes via bank (IPAY/Pass5 system) based on BOC assessment | Finance | — | 1 day |
| 2 | **Receipt Aggregation**: Collect Official Receipts (BCOR) and Statement of Settlement of Duties and Taxes (SSDT) | Import Coord | — | 2 days |
| 3 | **Reconciliation**: Compare BOC assessed values vs. ERP estimated landed cost (W2b.12) | Finance | Controller | 1 day |
| 4 | **VAT Input Capture**: Ensure 12% Import VAT is correctly recorded for BIR credit (W90) | Tax Manager | — | 30 min |
| 5 | **Variance Analysis**: Investigate significant variances in tariff classification or valuation | Import Coord | Tax Manager | 2 hours |

### System Touchpoints
- SDS (Safety Data Sheet) storage in Item Master
- Hazmat zone location management in WMS
- Incident management module (W140)
- Landed cost calculation engine (W2b)
- VAT Input/Output reconciliation (W90)
