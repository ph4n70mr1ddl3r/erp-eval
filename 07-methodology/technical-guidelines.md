# Technical Implementation Guidelines

> This document provides technical guidance for ERP implementors and evaluators. These are
> **suggestions and reference specs**, not mandates. Each ERP evaluation folder should propose
> its own technical architecture that meets the business requirements defined in
> [01-model-company/](../01-model-company/).

---

## 1. POS Hardware Reference Specification

The following is a reference POS hardware specification that meets the business requirements
(offline capability, barcode scanning, multi-tender, receipt printing). ERP evaluators should
confirm their POS solution supports equivalent or better specifications.

| Component | Reference Spec |
|---|---|
| **Terminal Type** | All-in-one POS terminal (touchscreen) |
| **Screen Size** | 15" touchscreen (cashier) + customer-facing display |
| **Barcode Scanner** | Integrated 2D imager (1D + 2D: QR, DataMatrix) + handheld scanner |
| **Receipt Printer** | 80mm thermal printer (BIR-registered format) |
| **Cash Drawer** | Triggered by POS; 4-bill / 8-coin compartments |
| **Payment Device** | PIN pad for card (EMV/chip & contactless); e-wallet QR support |
| **Offline Storage** | Must store ≥ 8 hours of transactions locally (~4,700 txns per store per day) |
| **Connectivity** | Primary link + failover connectivity |
| **Central Management** | Centrally managed (MDM or equivalent); OTA updates across 1,000 terminals |

### POS Cost Estimate (Reference)

| Item | Unit Cost (PHP) | Qty | Total (PHP) |
|---|---|---|---|
| POS Terminal (all-in-one) | ~20,000 | 1,000 | 20,000,000 |
| Barcode Scanner (handheld) | ~5,000 | 1,000 | 5,000,000 |
| Receipt Printer | ~8,000 | 1,000 | 8,000,000 |
| Cash Drawer | ~5,000 | 1,000 | 5,000,000 |
| Payment PIN Pad | ~15,000 | 1,000 | 15,000,000 |
| **Per-Store Total (5 terminals)** | | | **~PHP 265,000** |
| **All 200 Stores** | | | **~PHP 53,000,000** |

> Note: Actual costs depend on ERP vendor's certified POS hardware and Philippine sourcing.

---

## 2. Infrastructure & Deployment Reference

The following is a reference infrastructure topology. ERP evaluators should propose their
own architecture that satisfies the NFRs in [erp-requirements.md](../01-model-company/erp-requirements.md).

### 2.1 Deployment Model Considerations

| Consideration | Notes |
|---|---|
| 200 store locations with POS | Requires reliable connectivity or robust offline mode |
| 5 DCs with WMS/RF guns | Low-latency connection needed for real-time pick/ship |
| 1,000 POS terminals | Centralized management is essential |
| 8,050 employees | HR/payroll can be cloud-hosted |
| Philippine regulatory filing | BIR, SSS, PhilHealth, Pag-IBIG file generation |
| Data residency | No strict PH data residency requirement, but Asia-Pacific hosting recommended for latency |

### 2.2 Network Bandwidth Reference Estimates

These are estimates based on transaction volumes. Actual bandwidth depends on the chosen
ERP's data sync requirements.

| Site Type | Count | Reference Bandwidth | Rationale |
|---|---|---|---|
| Store | 200 | ≥ 2 Mbps stable + failover link | POS sync, price updates, inventory updates |
| DC | 5 | ≥ 10 Mbps stable, redundant | WMS real-time operations, 150 RF guns per DC |
| HQ | 1 | ≥ 100 Mbps | 300 users, reporting, batch processing |
| **Total WAN** | **206** | **~550 Mbps aggregate** | |

### 2.3 DR & Business Continuity Reference

| Parameter | Target | Notes |
|---|---|---|
| RPO (back-office) | ≤ 1 hour | Financial data, inventory |
| RTO (back-office) | ≤ 4 hours | Core ERP functions |
| POS offline endurance | ≥ 8 hours | Must continue selling without connectivity |
| POS sync on reconnection | Automatic | No manual intervention; reconcile all offline transactions |
| Data backup | Daily | 30-day rolling + 7-year archive |
| Data retention | 7 years | BIR requirement |

---

## 3. Integration Architecture Reference

### 3.1 Integration Methods by Touchpoint

The model company's [integration touchpoints](../01-model-company/model-company-profile.md#143-integration-touchpoints)
define *what* must connect. The table below suggests *how* — each ERP evaluator should
propose their own integration approach.

| Touchpoint | Suggested Method | Notes |
|---|---|---|
| POS ↔ ERP | API (real-time or near-real-time) | Batch fallback every 15 min if real-time unavailable |
| Ecommerce ↔ ERP | REST API | Real-time for orders; near-real-time for inventory |
| Payment Gateway → ERP | Webhook / API | Real-time payment confirmation |
| Bank ↔ ERP | File-based (CSV/XML) or API | Bank-specific formats (BDO, BPI, Metrobank) |
| BIR eFPS ← ERP | File export | BIR-formatted tax return files |
| SSS / PhilHealth / Pag-IBIG ← ERP | File export | Monthly contribution files with PRN |
| Delivery Partners ↔ ERP | API | Real-time order dispatch and status tracking |
| Loyalty Engine ↔ ERP | API | Real-time points earn/redeem |
| WMS ↔ ERP | API or middleware | Real-time for pick/ship confirmations |
| Supplier Portal ↔ ERP | Web portal / EDI | PO viewing, ASN, invoice submission |

### 3.2 Integration Architecture Diagram (Reference)

```
┌─────────────────────────────────────────────────────────────────────┐
│                        BUILDRIGHT DEPOT CORP                        │
│                      INTEGRATION TOUCHPOINTS                        │
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

## 4. Security Reference Requirements

These are baseline security expectations. ERP evaluators should detail their platform's
security capabilities in their architecture documents.

| Area | Expectation |
|---|---|
| **Access Control** | Role-based access control (RBAC) with per-entity, per-location, per-function permissions |
| **Audit Trail** | All financial and inventory transactions must have immutable audit logs |
| **Data Encryption** | Encryption at rest and in transit for all sensitive data |
| **POS Security** | Endpoint protection on all POS devices; tamper-resistant payment processing |
| **Customer Data** | RA 10173 (Data Privacy Act) compliance; consent management; data subject access requests |
| **Vulnerability Management** | Regular patching; annual penetration testing |
| **Compliance** | SOC 2 Type II or ISO 27001 certification target for ERP provider |

---

*Document Version: 1.0 | Date: 2026-05-30 | Initial version — reference specs moved from model company docs*
