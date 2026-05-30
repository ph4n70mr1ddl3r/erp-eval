# BuildRight Depot Corp. — Mobile App Strategy

> Defines the mobile application strategy for BuildRight Depot's customers and employees.
> This document informs the ERP evaluation by specifying mobile integration requirements.

---

## 1. Customer-Facing Mobile App

### 1.1 Platform & Technology

| Parameter | Decision |
|---|---|
| **App Type** | Native mobile app (iOS + Android) |
| **Architecture** | Mobile app → API gateway → ERP backend + ecommerce platform |
| **Authentication** | Email/phone registration; optional social login (Google, Facebook); biometric login (fingerprint/face) |
| **Minimum OS** | iOS 15+; Android 10+ |
| **Distribution** | Apple App Store + Google Play Store |

### 1.2 Customer App Features

| Feature | Priority | ERP Integration | Notes |
|---|---|---|---|
| **Product browsing & search** | Must Have | ECOM-009 (catalog sync), MDM-002 (attributes) | Full 35K SKU catalog with category navigation, keyword search, filters |
| **Real-time inventory check** | Must Have | ECOM-001 (inventory sync) | Per-store availability; "Select your store" selector |
| **BOPIS ordering** | Must Have | ECOM-003 (BOPIS flow) | Select store → add to cart → pay online → receive pickup notification |
| **Home delivery ordering** | Must Have | ECOM-004 (delivery flow) | Enter address → select items → choose delivery slot → pay online |
| **Order tracking** | Must Have | ECOM-005 (order status) | Real-time tracking for home delivery; pickup status for BOPIS |
| **Loyalty account management** | Must Have | CRM-001, CRM-005 | Points balance, tier status, transaction history, digital loyalty card |
| **Payment integration** | Must Have | ECOM-006 (payment gateway) | GCash, Maya, credit/debit card, bank transfer, COD |
| **Returns initiation** | Must Have | ECOM-007 (online return) | Submit return request with photos; QR code authorization for in-store drop-off |
| **Personalized promotions** | Should Have | RPT-003, CRM-007 | Push notifications for deals based on purchase history and tier |
| **Digital receipts** | Should Have | POS-012 | Access historical transaction receipts |
| **Store locator** | Must Have | MDM-006 (location master) | Map view with store hours, contact, directions, real-time stock check |
| **Wishlist / save for later** | Nice to Have | — | Local storage + server sync |
| **Barcode scanner** | Should Have | ECOM-001, MDM-001 | Scan item in-store to view product details, specs, reviews, and stock |
| **Project lists** | Nice to Have | — | Create material lists for home projects; share with trade account |
| **Push notifications** | Should Have | — | Order updates, promo alerts, BOPIS ready-for-pickup, points expiry |

### 1.3 Customer App Integration Architecture

```
┌─────────────────────┐
│  Customer Mobile App │
│  (iOS / Android)     │
└──────────┬──────────┘
           │ REST API (HTTPS)
           ▼
┌─────────────────────┐     ┌─────────────────┐
│   API Gateway        │────→│  Ecommerce       │
│   (rate limiting,    │     │  Platform        │
│    auth, routing)    │     │  (catalog, cart,  │
└──────────┬──────────┘     │   checkout)       │
           │                 └────────┬──────────┘
           │                          │
           ▼                          ▼
┌─────────────────────┐     ┌─────────────────┐
│   ERP System         │←───→│  Loyalty Engine   │
│   (inventory, orders, │     │  (points, tiers)  │
│    customers, AR)     │     └─────────────────┘
└─────────────────────┘
```

---

## 2. Employee-Facing Mobile Capabilities

### 2.1 Store Manager App

| Feature | Priority | ERP Integration | Notes |
|---|---|---|---|
| **Daily sales dashboard** | Must Have | RPT-001, RPT-002 | Real-time store revenue, transactions, ATV, vs. target |
| **Exception alerts** | Must Have | W37 (loss prevention) | Void alerts, price override alerts, high-value return alerts |
| **Approval inbox** | Must Have | PUR-010, POS-006 | Approve POs, price overrides, voids, returns above threshold |
| **Staff schedule view** | Should Have | HR-006 (shift scheduling) | View weekly schedule, approve swap requests |
| **Inventory alerts** | Should Have | INV-002 | Stockout alerts, negative inventory, low-stock warnings |
| **Store P&L summary** | Should Have | RPT-002 | Monthly store P&L with variance to budget |
| **BOPIS management** | Should Have | ECOM-003 | View pending BOPIS picks, monitor SLA compliance |
| **Receiving schedule** | Should Have | W4, W18 | View expected deliveries for the day/week |

### 2.2 Sales Associate / Floor Staff App (Handheld)

| Feature | Priority | ERP Integration | Notes |
|---|---|---|---|
| **Cross-store inventory lookup** | Must Have | INV-002 | Real-time stock check at nearby stores for customer requests |
| **Product information lookup** | Must Have | MDM-001, MDM-002 | Scan barcode → view specs, price, stock, alternatives |
| **Customer-initiated transfer request** | Should Have | W22 | Create inter-store transfer for customer |
| **Backorder creation** | Should Have | W56 | Create backorder for out-of-stock item |
| **Special order intake** | Should Have | W38 | Initiate special order for non-stock item |

### 2.3 Executive Dashboard App

| Feature | Priority | ERP Integration | Notes |
|---|---|---|---|
| **Chain-wide KPI dashboard** | Must Have | RPT-001 | Revenue, margin, transactions, same-store sales |
| **Store heat map** | Should Have | RPT-003 | Performance by region/store on map |
| **Cash position** | Should Have | FIN-010 | Real-time cash position per entity |
| **Alert inbox** | Should Have | — | Critical alerts (P1 incidents, store closures, major variances) |

### 2.4 Receiving / Warehouse Mobile (RF Devices)

| Feature | Priority | ERP Integration | Notes |
|---|---|---|---|
| **PO/TO lookup** | Must Have | PUR-011, WMS-004 | Pull up expected receipt on handheld |
| **Barcode scanning** | Must Have | WMS-001 | Scan items against PO |
| **Goods receipt posting** | Must Have | INV-001 | Post GR in real-time |
| **Putaway direction** | Must Have | WMS-004 | System-directed putaway location |
| **Cycle count entry** | Must Have | INV-006 | Enter count quantities on device |
| **Discrepancy flagging** | Must Have | PUR-011 | Flag variances at receiving |

---

## 3. Technical Requirements for ERP Evaluators

Each ERP evaluation should address:

| Question | Relevance |
|---|---|
| Does the ERP provide native mobile apps for store managers, or must they be custom-built? | Affects implementation cost and timeline |
| What is the mobile API strategy (REST, GraphQL, SDK)? | Determines mobile development flexibility |
| Can the POS system be extended to handheld devices for floor selling? | Enables line-busting during peak periods |
| Does the ERP vendor offer a customer-facing mobile commerce SDK? | Reduces custom development for the customer app |
| How do mobile devices authenticate (SSO, OAuth, biometric)? | Security and user experience |
| Is offline capability available on employee mobile apps? | Store connectivity during outages |
| What is the push notification architecture? | Real-time alerting for managers and customers |

---

## 4. Build vs. Buy Decision Framework

| Component | Recommendation | Rationale |
|---|---|---|
| **Customer mobile app** | Build (with ERP API backend) | Customer experience is a brand differentiator; native app provides best UX, push notifications, and biometric login; backend data from ERP via APIs |
| **Store manager app** | ERP-native or configure | Most ERPs offer manager dashboards; prefer configuring ERP-provided app to reduce custom development |
| **RF / warehouse mobile** | ERP-native (WMS module) | Must use ERP's WMS mobile client for real-time integration; RF device compatibility is a selection criterion |
| **Executive dashboard** | ERP-native or Power BI / embedded | Use ERP's built-in executive dashboards or BI tool integration (e.g., Power BI for D365, SAC for SAP) |
| **Sales associate handheld** | Build (lightweight) | Simple inventory lookup and transfer request; can be built as a responsive web app or native app using ERP APIs |

---

*Date: 2026-05-30*
