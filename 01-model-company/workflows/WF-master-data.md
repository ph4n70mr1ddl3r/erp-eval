# Master Data Management (MDM) Workflows

> Centralized item master creation & governance, customer master data governance & deduplication, and location master lifecycle & hierarchy management.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W252. Centralized Item Master Creation & Governance](#centralized-item-master-creation--governance)
- [W253. Customer Master Data Governance & Deduplication](#customer-master-data-governance--deduplication)
- [W254. Location Master Lifecycle & Hierarchy Management](#location-master-lifecycle--hierarchy-management)

---

## W252. Centralized Item Master Creation & Governance

| Field | Detail |
|---|---|
| **Trigger** | Merchandising department requests a new SKU/Item to be added to the assortment |
| **Frequency** | Daily (approx. 50–100 new SKUs/week across all categories) |
| **Owner** | Master Data Manager |
| **Participants** | Category Manager, Pricing Analyst, Supply Chain Planner, Master Data Analyst |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Request Initiation**: Category Manager submits a New Item Request via the ERP MDM portal, filling in mandatory commercial attributes (supplier, brand, hierarchy category, unit of measure, standard cost) | Category Manager | — | 10 min |
| 2 | **Attribute Enrichment — Supply Chain**: Supply Chain Planner adds logistical attributes (dimensions, weight, pallet tie/high, default supply DC, lead time, minimum order quantity) | Supply Chain Planner | — | 10 min |
| 3 | **Attribute Enrichment — Pricing**: Pricing Analyst adds retail pricing parameters (base retail price, price family grouping, initial margin) | Pricing Analyst | — | 5 min |
| 4 | **Validation & Quality Check**: Master Data Analyst reviews the completed request, ensuring no duplicates exist (checking GTIN/UPC/EAN) and all naming conventions are strictly followed | Master Data Analyst | Master Data Manager | 10 min |
| 5 | **Approval & Activation**: Master Data Manager approves the item. System assigns internal SKU number, activates the item across the relevant location matrix (store assortments), and syncs to POS and Ecommerce platforms | Master Data Manager | Master Data Manager | 5 min |

**System Touchpoints**:
- ERP Item Master Module (centralized creation, attribute fields)
- ERP Approval Workflow Engine
- POS / Ecom Integration (downstream sync)

**Pain Points / Risks**:
- Incomplete dimensional data causing warehouse slotting failures.
- Duplicate SKU creation leading to fragmented sales history and over-purchasing.

---

## W253. Customer Master Data Governance & Deduplication

| Field | Detail |
|---|---|
| **Trigger** | Ongoing customer data ingestion from POS loyalty sign-ups, Ecommerce registrations, and B2B Trade Account creations |
| **Frequency** | Continuous automated ingestion; Monthly manual deduplication review |
| **Owner** | CRM Data Steward |
| **Participants** | Store Cashier, B2B Sales Rep, Customer Service Rep, CRM Data Steward |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Data Ingestion**: Customer data is captured at POS (phone number lookup/creation), Ecommerce (email registration), or B2B Portal. System performs real-time validation (e.g., regex checks for PH mobile numbers +639XX) | Store Cashier / System | — | 2 min |
| 2 | **Automated Matching**: ERP/CDP runs daily batch matching algorithms (Levenshtein distance on names, exact match on email/mobile) to flag potential duplicate profiles | System | — | Automated |
| 3 | **Exception Management**: CRM Data Steward reviews the "Potential Duplicates" queue | CRM Data Steward | — | 15 min/batch |
| 4 | **Merge & Consolidate**: Steward executes a merge. System consolidates loyalty points, purchase history, and contact details into the surviving "Golden Record", and leaves a tombstone on the deprecated record | CRM Data Steward | CRM Data Steward | 10 min/merge |
| 5 | **Downstream Sync**: The Golden Record updates are pushed to Ecommerce, POS offline databases, and Marketing Automation tools | System | — | Automated |

**System Touchpoints**:
- ERP Customer Master / CRM Module
- Customer Data Platform (CDP) deduplication engine
- POS and Ecommerce APIs

**Pain Points / Risks**:
- Cashiers creating "dummy" accounts to bypass mandatory fields, polluting the database.
- Merging two distinct customers (e.g., family members sharing a phone number) causing privacy issues.

---

## W254. Location Master Lifecycle & Hierarchy Management

| Field | Detail |
|---|---|
| **Trigger** | Real estate team confirms a new store/DC opening, relocation, or closure |
| **Frequency** | 5–10 times per year |
| **Owner** | IT ERP Administrator |
| **Participants** | Real Estate Manager, Operations Director, Finance Controller, Master Data Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Location Request**: Operations submits a Location Master request specifying store type, region, GL company code, and tax registration details (TIN/Branch Code) | Operations Director | — | 15 min |
| 2 | **Financial Setup**: Finance Controller defines the cost center, profit center, and fixed asset location mappings for the new entity | Finance Controller | — | 20 min |
| 3 | **Logistical Setup**: Supply Chain assigns the supplying DC, default transit times, and delivery schedules to the location profile | Supply Chain Planner | — | 15 min |
| 4 | **Hierarchy Assignment**: Master Data Manager places the location in the enterprise hierarchy (e.g., Region: Visayas → Area: Cebu → Store: Mandaue City) | Master Data Manager | — | 10 min |
| 5 | **System Activation**: ERP Administrator activates the location. This triggers automated setup in POS polling routines, replenishment MRP runs, and financial reporting roll-ups | IT ERP Administrator | IT ERP Administrator | 30 min |

**System Touchpoints**:
- ERP Location/Site Master
- Finance GL Mapping
- Supply Chain Network configuration

**Pain Points / Risks**:
- Misaligned tax branch codes leading to BIR filing errors.
- Failure to update the hierarchy resulting in missing stores in regional sales reports.
