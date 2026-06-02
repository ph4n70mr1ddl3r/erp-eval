# Wholesale & Reseller Operations Workflows

> Management of sales to 3rd-party hardware stores, resellers, and institutional bulk buyers.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W145. Wholesale Reseller Onboarding & Credit Management](#wholesale-reseller-onboarding--credit-management)
- [W146. Bulk Fulfillment & Cross-Docking for Wholesale](#bulk-fulfillment--cross-docking-for-wholesale)

---

## W145. Wholesale Reseller Onboarding & Credit Management

| Field | Detail |
|---|---|
| **Trigger** | 3rd-party hardware store or construction supply company requests reseller partnership |
| **Frequency** | 2–5 new resellers/month |
| **Volume** | ~100–150 active resellers |
| **Owner** | B2B Sales Manager |
| **Participants** | Sales Rep, Credit Analyst, Legal, Finance |

### Background

While BuildRight is primarily retail, it acts as a regional distributor for certain brands and high-volume commodities (cement, steel) for smaller hardware stores. Resellers require different tax handling (withholding tax on sales) and volume-based pricing.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Application**: Reseller submits business permits, SEC/DTI registration, and BIR 2303 (Certificate of Registration) | Reseller / Sales Rep | B2B Sales Mgr | 1 hour |
| 2 | **Credit Review**: Credit Analyst performs deep-dive on financial statements and trade references per W24; sets "Wholesale Credit Limit" | Credit Analyst | Finance Mgr | 1–3 days |
| 3 | **Tax Configuration**: System flags account as "Reseller"; configures automatic handling of Expanded Withholding Tax (EWT) certificates (BIR 2307) | Finance (AR) | Controller | 30 min |
| 4 | **Price List Assignment**: Assign "Wholesale Tier" price list (W40.15–19) based on projected annual volume | B2B Sales Mgr | VP Merch | 15 min |
| 5 | **Onboarding**: Create account in ERP with "Reseller" category; provide login to B2B ordering portal | Sales Rep | — | 30 min |

---

## W146. Bulk Fulfillment & Cross-Docking for Wholesale

| Field | Detail |
|---|---|
| **Trigger** | Wholesale Sales Order (SO) exceeding 10 pallets or full truckload |
| **Frequency** | Weekly; ~10–20 bulk shipments/DC |
| **Volume** | Primary commodities: Cement, Plywood, Steel Bars, Tiles |
| **Owner** | DC Manager |
| **Participants** | Logistics, Warehouse, 3PL Carrier, Reseller |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **SO Entry**: Sales Rep enters wholesale order; system checks DC inventory (skipping store-level pools) | Sales Rep | B2B Sales Mgr | 15 min |
| 2 | **Fulfillment Strategy**: (a) If stock in DC: Pick from bulk zone; (b) If stock coming from vendor: Flag for "Cross-Dock" (no putaway) | DC Manager | — | 30 min |
| 3 | **Transportation Booking**: Book 10-wheeler or tractor head via 3PL (W62B); specify "Wholesale Delivery" SLA | Logistics | Fleet Manager | 1 hour |
| 4 | **Loading & Tally**: Physical tally during loading; driver signs "Wholesale Tally Sheet" and B/L | DC Team / Driver | DC Manager | 2 hours |
| 5 | **Direct Shipment**: Delivery from DC or Vendor direct to Reseller site (bypassing BuildRight stores) | Driver | — | Varies |
| 6 | **Proof of Delivery (POD)**: Reseller signs POD and provides BIR 2307 (if applicable); driver uploads via mobile app | Driver | AR Clerk | 10 min |
| 7 | **Billing**: System generates Wholesale Invoice; adjusts inventory; initiates collection cycle (W8) | System | — | Automated |
