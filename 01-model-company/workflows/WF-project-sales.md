# Project-Based B2B & Trade Sales Workflows

> Quotations, bid management, contract pricing, staged deliveries, and project-specific logistics for construction and corporate clients.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W162. Project Quotation & Bid Management](#project-quotation--bid-management)
- [W163. Contract Pricing & Project Price Books](#contract-pricing--project-price-books)
- [W164. Staged Project Delivery & Call-Off Orders](#staged-project-delivery--call-off-orders)
- [W165. Project Retention & Milestone Billing](#project-retention--milestone-billing)
- [W166. Corporate / Institutional Tendering](#corporate--institutional-tendering)

---

## W162. Project Quotation & Bid Management

| Field | Detail |
|---|---|
| **Trigger** | Customer requests a quote for a specific construction project or bulk purchase |
| **Frequency** | ~300–500 quotes/month |
| **Volume** | Quote value: PHP 100K to PHP 10M+ |
| **Owner** | Sales Rep (B2B) |
| **Participants** | Sales Rep, Category Manager (for deep discounts), Project Manager (Client) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Sales Rep receives Bill of Quantities (BOQ) or item list from client project | Sales Rep | — | 1 hour |
| 2 | Sales Rep creates Quote in system: selects items, specifies quantities, sets validity period (typically 15–30 days) | Sales Rep | — | 30 min |
| 3 | System checks current stock (ATP) across all DCs/Stores; flags items with insufficient stock for the project timeline | System | — | Automated |
| 4 | **Pricing Strategy**: (a) If standard B2B price list used: auto-approved; (b) If additional discount requested (> 5% off B2B list): route to Category Manager for approval; (c) If "Loss Leader" pricing for strategic bid: route to VP Merchandising | Sales Rep / Cat. Manager | VP Merchandising | 1–4 hours |
| 5 | System generates Quotation PDF with terms (payment, delivery, lead times, force majeure) | System | — | Automated |
| 6 | Sales Rep presents quote to client; negotiates terms | Sales Rep | Sales Manager | 1–5 days |
| 7 | Client accepts: Sales Rep converts Quote to **Project Contract / Master Sales Order** in system | Sales Rep | — | 15 min |
| 8 | If Quote expires: system auto-cancels; Sales Rep can "re-quote" with updated pricing | System | Sales Rep | Automated |

---

## W163. Contract Pricing & Project Price Books

| Field | Detail |
|---|---|
| **Trigger** | Project Contract signed; requires locked-in pricing for duration of project (6–18 months) |
| **Owner** | Pricing Analyst |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Pricing Analyst creates a **Project Price Book** linked to the specific Customer + Project ID | Pricing Analyst | Category Manager | 30 min |
| 2 | Enters locked-in prices for the agreed BOQ items; sets price validity end date | Pricing Analyst | Category Manager | 30 min |
| 3 | System ensures that when this Customer orders for this Project, the Project Price Book takes precedence over standard B2B or Promo price lists | System | — | Automated |
| 4 | **Price Escalation Clause**: If contract allows for price adjustment (e.g., fuel/commodity surcharge), Pricing Analyst updates Price Book based on formula; triggers notification to client | Pricing Analyst | Sales Rep | 30 min |

---

## W164. Staged Project Delivery & Call-Off Orders

| Field | Detail |
|---|---|
| **Trigger** | Project site requests a partial delivery (Call-Off) against the Master Sales Order |
| **Frequency** | Weekly/Bi-weekly per project |
| **Volume** | Total project may have 10–50 partial deliveries |
| **Owner** | Sales Coordinator |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Client Project Site sends "Call-Off" request (Item, Quantity, Site Location, Date) | Client / Sales Rep | — | 10 min |
| 2 | Sales Coordinator creates **Release Order (Delivery Order)** against the Master Sales Order | Sales Coordinator | — | 15 min |
| 3 | System validates: (a) Quantity is within Master Order balance, (b) Customer has available credit limit, (c) Customer has no overdue invoices | System | — | Automated |
| 4 | System reserves stock at the designated DC or Store for this release | System | — | Automated |
| 5 | Logistics processes the delivery per W19 (Dispatch) | Logistics Team | — | Per W19 |
| 6 | Upon delivery: System updates Master Order "Remaining Quantity"; posts to AR (W8) if on-account | System | — | Automated |

---

## W165. Project Retention & Milestone Billing

| Field | Detail |
|---|---|
| **Trigger** | Project milestone achieved; or final billing with retention |
| **Owner** | AR Clerk |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Sales Rep confirms milestone achievement with client (e.g., "Structural Phase Complete") | Sales Rep | — | — |
| 2 | AR Clerk generates Milestone Invoice per contract terms (e.g., 20% of total project value) | AR Clerk | — | 15 min |
| 3 | **Retention Management**: If contract specifies retention (typically 5–10% held until final acceptance), system automatically deducts retention from each milestone invoice and posts to "Retention Receivable" account | System / AR Clerk | — | Automated |
| 4 | Final Acceptance: Client signs off; AR Clerk invoices for the total accumulated Retention balance | AR Clerk | Sales Manager | 30 min |

---

## W166. Corporate / Institutional Tendering

| Field | Detail |
|---|---|
| **Trigger** | Government (PhilGEPS) or Private Institutional RFP/RFQ issued |
| **Owner** | Bid & Tender Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Bid Manager monitors PhilGEPS/Tender boards; downloads RFP | Bid Manager | — | Daily |
| 2 | Initial Go/No-Go: Evaluate capability, capacity, and margin potential | Bid Manager | Sales Director | 1 day |
| 3 | Coordinate with Legal (Tender Bonds, JV agreements) and Finance (Performance Bonds, Cash Flow) | Bid Manager | Legal / CFO | 3–5 days |
| 4 | Compile Bid Package: Pricing (W162), Technical Specs (W50), Corporate Docs | Bid Manager | — | 1–2 weeks |
| 5 | Submit Bid (Electronic or Physical); track bid opening results | Bid Manager | — | Per RFP |
| 6 | If won: Transition to W163 (Contract Pricing) and W164 (Fulfillment) | Bid Manager | — | — |

---

### System Touchpoints (Project Sales)
- Quote-to-Contract (Master Sales Order) conversion
- Project-specific Price Books with locked-in pricing
- ATP (Available-to-Promise) check across multi-location inventory
- Credit limit check including "In-Flight" project commitments
- Staged delivery (Call-Off) management with balance tracking
- Retention Receivable accounting
- Integration with W19 (Logistics) and W8 (AR)

---

### System Touchpoints (Project Sales)
- Quote-to-Contract (Master Sales Order) conversion
- Project-specific Price Books with locked-in pricing
- ATP (Available-to-Promise) check across multi-location inventory
- Credit limit check including "In-Flight" project commitments
- Staged delivery (Call-Off) management with balance tracking
- Retention Receivable accounting
- Integration with W19 (Logistics) and W8 (AR)
