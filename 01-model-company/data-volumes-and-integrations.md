# Model Company — Data Volumes & Integration Map

> Supplementary reference for ERP planning. Contains detailed volume calculations,
> integration touchpoints, and data flow architecture.

---

## 1. Transaction Volume Summary

### 1.1 Daily Volumes (assuming 30 operating days/month)

| Transaction Type | Daily Volume | Peak Factor | Peak Daily |
|---|---|---|---|
| POS Transactions | 66,667 | 2.0x (weekends/sales) | 133,334 |
| POS Line Items | 266,667 | 2.0x | 533,334 |
| Store Replenishment Orders | 117 | 1.5x | 176 |
| Goods Receipts | 150 | 1.5x | 225 |
| Purchase Orders Created | 33 | 2.0x (batch days) | 66 |
| AP Invoices Processed | 183 | 2.0x (month-end) | 366 |
| Ecommerce Orders | 167 | 3.0x (sale events) | 500 |
| Customer Registrations | ~100 | — | ~300 |

### 1.2 Data Storage Estimates (Annual Growth)

| Data Type | Annual Records | Est. Size |
|---|---|---|
| POS Transaction Headers | 24,000,000 | ~12 GB |
| POS Transaction Lines | 96,000,000 | ~48 GB |
| Inventory Movements | ~2,000,000 | ~4 GB |
| Journal Entries + Lines | ~1,000,000 | ~2 GB |
| Purchase Orders + Lines | ~192,000 | ~0.5 GB |
| AP/AR Documents | ~1,200,000 | ~3 GB |
| Master Data (all types) | ~600,000 | ~0.5 GB |
| **Total Annual Increment** | | **~70 GB** |
| **7-Year Retention** | | **~500 GB** (with compression) |

---

## 2. Integration Architecture Map

```
┌─────────────────────────────────────────────────────────────────────┐
│                        BUILDRIGHT DEPOT CORP                        │
│                      INTEGRATION ARCHITECTURE                       │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │
│  │ 200 POS  │  │ 4 WMS    │  │ Ecommerce │  │ Loyalty Engine   │   │
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

| Source | Target | Data | Direction | Frequency | Protocol |
|---|---|---|---|---|---|
| POS | ERP | Sales transactions | POS → ERP | Real-time (or batch every 15 min) | API |
| ERP | POS | Price file, item master, promos | ERP → POS | Hourly sync | API |
| ERP | POS | Customer lookup | ERP → POS | Real-time | API |
| Ecommerce | ERP | Orders, customer registrations | ECOM → ERP | Real-time | REST API |
| ERP | Ecommerce | Inventory levels, prices, catalog | ERP → ECOM | Near real-time (5 min) | REST API |
| ERP | Ecommerce | Order fulfillment status | ERP → ECOM | Real-time | Webhook |
| ERP | WMS | Transfer orders, PO receipts | ERP → WMS | Real-time | API |
| WMS | ERP | Pick confirmation, ship confirm, inventory | WMS → ERP | Real-time | API |
| ERP | Loyalty/CRM | Points earning triggers | ERP → CRM | Real-time | API |
| CRM/POS | ERP | Points redemption | CRM → ERP | Real-time | API |
| ERP | Banks | Payment files (AP) | ERP → Bank | Batch (daily) | File (CSV/XML) |
| Banks | ERP | Bank statements | Bank → ERP | Batch (daily) | File / API |
| ERP | BIR eFPS | Tax returns | ERP → BIR | Monthly/Quarterly | File |
| ERP | SSS/PH/PagIBIG | Contribution files | ERP → Statutory | Monthly | File |
| ERP | Delivery Partners | Delivery orders | ERP → 3PL | Real-time | API |
| Delivery Partners | ERP | Delivery status | 3PL → ERP | Real-time | Webhook |
| Payment GW | ERP | Payment confirmation | GW → ERP | Real-time | Webhook |
| ERP | Supplier Portal | POs, schedules | ERP → Portal | Real-time | Web portal |
| Supplier Portal | ERP | ASN, invoices | Portal → ERP | As submitted | Web portal |

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

---

*Document Version: 1.0 | Date: 2026-05-29*
