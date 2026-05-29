# Model Company — Data Volumes & Integration Map

> Supplementary reference for ERP planning. Contains detailed volume calculations,
> integration touchpoints, and data flow architecture.

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

*Document Version: 2.0 | Date: 2026-05-29 | Status: Revised — updated volumes per realism review*
