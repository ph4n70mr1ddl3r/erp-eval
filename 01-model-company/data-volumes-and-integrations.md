# Model Company — Data Volumes & Integration Map

> Supplementary reference for ERP planning. Contains detailed volume calculations,
> integration touchpoints, and data flow architecture. Cross-references:
> - Company profile & POS details: [model-company-profile.md](model-company-profile.md)
> - Full requirements list: [erp-requirements.md](erp-requirements.md)
> - Scoring methodology: [scoring-methodology.md](../07-methodology/scoring-methodology.md)

---

## 1. Transaction Volume Summary

### 1.1 Daily Volumes (assuming 30 operating days/month)

| Transaction Type | Daily Volume | Peak Factor | Peak Daily |
|---|---|---|---|
| POS Transactions | 93,333 | 2.0x (weekends/sales) | 186,666 |
| POS Line Items | 373,333 | 2.0x | 746,666 |
| Store Replenishment Orders | 167 | 1.5x | 250 |
| Goods Receipts | 200 | 1.5x | 300 |
| Purchase Orders Created | 40 | 2.0x (batch days) | 80 |
| AP Invoices Processed | 217 | 2.0x (month-end) | 433 |
| Ecommerce Orders | 1,500 | 3.0x (sale events) | 4,500 |
| Customer Registrations | ~150 | — | ~450 |

### 1.2 Data Storage Estimates (Annual Growth)

| Data Type | Annual Records | Est. Size |
|---|---|---|
| POS Transaction Headers | 33,600,000 | ~17 GB |
| POS Transaction Lines | 134,400,000 | ~67 GB |
| Inventory Movements | ~3,000,000 | ~6 GB |
| Journal Entries + Lines | ~1,500,000 | ~3 GB |
| Purchase Orders + Lines | ~233,000 | ~0.6 GB |
| AP/AR Documents | ~1,440,000 | ~4 GB |
| Ecommerce Orders + Lines | ~540,000 | ~1.5 GB |
| Master Data (all types) | ~700,000 | ~0.7 GB |
| **Total Annual Increment** | | **~100 GB** |
| **7-Year Retention** | | **~700 GB** (with compression) |

---

## 2. Integration Architecture Map

```
┌─────────────────────────────────────────────────────────────────────┐
│                        BUILDRIGHT DEPOT CORP                        │
│                      INTEGRATION ARCHITECTURE                       │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │
│  │1,000 POS │  │ 5 WMS    │  │ Ecommerce │  │ Loyalty Engine   │   │
│  │Terminals │  │Systems   │  │ Platform │  │ (CRM)            │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────────┬─────────┘   │
│       │              │              │                  │             │
│       └──────────────┴──────┬───────┴──────────────────┘             │
│                             │                                        │
│                    ┌────────▼────────┐                               │
│                    │   ERP SYSTEM    │                               │
│                    │   (Core Hub)    │                               │
│                    └────────┬────────┘                               │
│                             │                                        │
│       ┌─────────────┬──────┴──────┬──────────────┐                  │
│       │             │             │              │                   │
│  ┌────▼─────┐ ┌────▼─────┐ ┌────▼─────┐  ┌────▼──────┐            │
│  │   Banks   │ │ BIR/eFPS │ │ SSS/PH/  │  │ Delivery  │            │
│  │(BDO,BPI,  │ │ (Tax     │ │ Pag-IBIG │  │ Partners  │            │
│  │  MB)      │ │ filing)  │ │ (Stat.)  │  │(Lalamove, │            │
│  └──────────┘ └──────────┘ └──────────┘  │ Transp.)  │            │
│                                           └───────────┘            │
│       ┌─────────────┐         ┌─────────────────┐                  │
│       │  Payment     │         │   Supplier       │                 │
│       │  Gateways    │         │   Portal         │                 │
│       │(PayMongo,   │         │                   │                 │
│       │ Dragonpay)  │         └─────────────────┘                  │
│       └─────────────┘                                               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Integration Detail Matrix

| Source | Target | Data | Direction | Frequency |
|---|---|---|---|---|
| POS | ERP | Sales transactions | POS → ERP | Real-time (or batch every 15 min) |
| ERP | POS | Price file, item master, promos | ERP → POS | Hourly sync |
| ERP | POS | Customer lookup | ERP → POS | Real-time |
| Ecommerce | ERP | Orders, customer registrations | ECOM → ERP | Real-time |
| ERP | Ecommerce | Inventory levels, prices, catalog | ERP → ECOM | Near real-time (5 min) |
| ERP | Ecommerce | Order fulfillment status | ERP → ECOM | Real-time |
| ERP | WMS | Transfer orders, PO receipts | ERP → WMS | Real-time |
| WMS | ERP | Pick confirmation, ship confirm, inventory | WMS → ERP | Real-time |
| ERP | Loyalty/CRM | Points earning triggers | ERP → CRM | Real-time |
| CRM/POS | ERP | Points redemption | CRM → ERP | Real-time |
| ERP | Banks | Payment files (AP) | ERP → Bank | Batch (daily) |
| Banks | ERP | Bank statements | Bank → ERP | Batch (daily) |
| ERP | BIR eFPS | Tax returns | ERP → BIR | Monthly/Quarterly |
| ERP | SSS/PH/PagIBIG | Contribution files | ERP → Statutory | Monthly |
| ERP | Delivery Partners | Delivery orders | ERP → 3PL | Real-time |
| Delivery Partners | ERP | Delivery status | 3PL → ERP | Real-time |
| Payment GW | ERP | Payment confirmation | GW → ERP | Real-time |
| ERP | Supplier Portal | POs, schedules | ERP → Portal | Real-time |
| Supplier Portal | ERP | ASN, invoices | Portal → ERP | As submitted |

---

## 4. Critical Timings & SLAs

| Integration | Max Latency | Impact if Exceeded |
|---|---|---|
| POS → ERP (sales) | 15 minutes | Inventory inaccuracy, stockouts |
| ERP → POS (prices) | 1 hour | Wrong pricing at checkout |
| ERP → ECOM (inventory) | 5 minutes | Overselling online |
| ECOM → ERP (orders) | 1 minute | Delayed order processing |
| WMS ↔ ERP (inventory) | 1 minute | DC inventory inaccuracy |
| Payment confirmation | 30 seconds | Failed order completion |

## 5. Batch Processing Windows

| Process | Schedule | Estimated Duration | Window |
|---|---|---|---|
| POS transaction sync (batch mode fallback) | Every 15 minutes | 1–3 minutes | Ongoing |
| Nightly inventory snapshot | Daily at 01:00 | 15–30 minutes | 01:00–03:00 |
| Nightly price/promo sync to POS | Daily at 02:00 | 10–20 minutes | 02:00–04:00 |
| Day-end close per store | Daily at 23:30 local | 5–10 minutes per store | 23:30–00:30 |
| Week-on-week sales report generation | Weekly (Monday 06:00) | 10–20 minutes | 06:00–07:00 |
| Month-end close | Last day of month + 5 working days | 2–4 hours for heavy jobs | 22:00–03:00 (off-peak) |
| Payroll processing (5 entities) | Semi-monthly (14th & 28th) | 1–2 hours per entity | 20:00–23:00 |
| VAT / tax report generation | Monthly (by 10th) | 30–60 minutes | Evening batch |
| BIR eFPS tax filing file export | Monthly / Quarterly | < 30 minutes | On-demand |
| Full inventory reindex / valuation | Monthly (1st) | 30–60 minutes | 01:00–03:00 |
| Demand planning / forecast recalculation | Weekly (Sunday) | 1–3 hours | 00:00–04:00 |
| Database backup | Daily at 03:00 | 1–2 hours | 03:00–05:00 |

### Peak Load Calendar

| Period | Activity | Additional Load |
|---|---|---|
| Month-end (last 3 days) | Close, accruals, reconciliation | +30% AP/AR processing, heavy reporting |
| Bi-monthly sale events | Promotional pricing, traffic surge | +100% POS volume, +200% ecommerce |
| Payroll dates (14th & 28th) | Payroll runs, bank file generation | Heavy HR/payroll module usage |
| Q1 inventory count (Jan) | Annual wall-to-wall physical count | Heavy inventory module, RF gun usage |
| Christmas season (Nov–Dec) | Peak retail period | Sustained +50% volume across all channels |

---

*Document Version: 3.0 | Date: 2026-05-30 | Removed network bandwidth estimates and integration protocols (moved to technical guidelines); renumbered §6 to §5; kept business-level volumes, timings, and batch windows*
