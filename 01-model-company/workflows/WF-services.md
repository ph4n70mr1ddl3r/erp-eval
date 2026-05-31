# Installation & Value-Added Services Workflows

> Management of home installation services (tiles, appliances, plumbing, AC) and tool/equipment rental.
> 
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W138. Home Installation Services Management](#home-installation-services-management)
- [W139. Tool & Equipment Rental Operations](#tool-equipment-rental-operations)
- [W147. DIY Workshop & In-Store Event Management](#diy-workshop--in-store-event-management)
- [W148. Home Design & Consultancy Services](#home-design--consultancy-services)
- [W168. Custom Paint Mixing & Tinting Operations](#custom-paint-mixing--tinting-operations)
- [W169. Lumber & Board Cutting Services](#lumber--board-cutting-services)
- [W211. In-Store 3D Kitchen/Bathroom Design Rendering](#in-store-3d-kitchenbathroom-design-rendering)

---

## W138. Home Installation Services Management

| Field | Detail |
|---|---|
| **Trigger** | Customer purchases installation-eligible product (e.g., split-type AC, water heater, floor tiles) and requests service |
| **Frequency** | Daily across 200 stores |
| **Volume** | ~500–800 service orders/week chain-wide |
| **Owner** | Services Manager (HQ); Customer Service Rep (Store) |
| **Participants** | CSR, Installation Contractor (3rd party), Warehouse/Logistics, Finance, Customer |

### Background

As a "Home Building Partner," BuildRight Depot provides professional installation services through a network of accredited 3rd-party contractors. This workflow manages the end-to-end lifecycle from service sale to contractor payout, ensuring quality control and financial reconciliation.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Service Sale**: Customer purchases item + Service SKU at POS; CSR captures site details (address, contact, preferred date) and attaches to Service Order (SO) | CSR | Store Manager | 10 min |
| 2 | **Contractor Assignment**: System auto-assigns SO to nearest accredited contractor based on category (HVAC, Plumbing, Flooring) and current workload; contractor notified via mobile app | System / Services Mgr | Services Mgr | Automated |
| 3 | **Site Inspection (if complex)**: For large flooring or roofing jobs, contractor performs site inspection; updates SO with actual material requirements; system adjusts SO price if needed | Contractor | Services Mgr | 1 day |
| 4 | **Scheduling**: Contractor confirms installation date/time with customer via system; system sends SMS confirmation to customer | Contractor | — | 5 min |
| 5 | **Material Release**: Store/DC releases materials for delivery (W19) or customer pickup (W11); system links material delivery status to SO status | Warehouse / CSR | Store Manager | Per W19 |
| 6 | **Execution**: Contractor performs installation; captures "Before" and "After" photos via mobile app; records any additional materials used from customer's stock | Contractor | — | 2–6 hours |
| 7 | **Completion & Sign-off**: Customer reviews work; signs digital completion certificate on contractor's app; rate service (1–5 stars) | Customer / Contractor | — | 10 min |
| 8 | **Quality Audit**: Services Manager reviews a sample of completed SOs (10%) and all low-rated services; triggers corrective action if needed | Services Mgr | VP Store Ops | 1 hour/day |
| 9 | **Billing & Payout**: System moves SO to "Completed/Ready for Payout"; Finance runs weekly payout batch: Contractor Fee − Commission % = Net Payout | Finance (AP) | Controller | Weekly |
| 10 | **Warranty Tracking**: System records installation date as start of labor warranty; links to product warranty (W33) | System | — | Automated |

### System Touchpoints
- Service SKU integration with material SKUs (prompting for service at POS)
- Contractor Portal/App for assignment, scheduling, photo upload, and sign-off
- Automated customer SMS/Email notifications
- Integration with AP for contractor payouts (W7)
- Service warranty tracking linked to customer profile (W17)

---

## W139. Tool & Equipment Rental Operations

| Field | Detail |
|---|---|
| **Trigger** | Customer requests rental of professional tools (jackhammers, tile cutters, generators) |
| **Frequency** | Daily; ~5–10 rentals per store/day |
| **Volume** | ~1,500 active rental units chain-wide |
| **Owner** | Store Manager |
| **Participants** | CSR, Warehouse/Stock Associate, Finance, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Rental Request**: CSR checks real-time availability of tool in store; verifies customer ID and loyalty status | CSR | Store Manager | 5 min |
| 2 | **Contract & Deposit**: System generates Rental Agreement; Customer pays Rental Fee + Refundable Security Deposit at POS | CSR / Cashier | — | 5 min |
| 3 | **Tool Release**: Stock Associate performs "Outbound Inspection" with customer: verify tool condition, fuel level, and safety features; Customer signs release form | Stock Associate | Store Manager | 10 min |
| 4 | **In-Use Tracking**: System tracks rental duration; sends SMS reminder 2 hours before scheduled return | System | — | Automated |
| 5 | **Return & Inspection**: Customer returns tool; Stock Associate performs "Inbound Inspection": check for damage, cleanliness, and functionality | Stock Associate | Store Manager | 10 min |
| 6 | **Closing & Refund**: (a) If tool OK: System processes deposit refund; (b) If tool damaged/dirty: CSR applies cleaning/repair fee from deposit; (c) If late: System calculates late fee | CSR / Cashier | Store Manager | 5 min |
| 7 | **Maintenance**: Tool moved to "Maintenance" status; Stock Associate performs standard cleaning/servicing before making "Available" again | Stock Associate | Maintenance | 20 min |
| 8 | **Asset Lifecycle**: System tracks total hours used/rentals per unit; triggers major preventive maintenance (PM) or retirement based on usage thresholds | System | Maintenance | Automated |

---

## W147. DIY Workshop & In-Store Event Management

| Field | Detail |
|---|---|
| **Trigger** | Monthly marketing calendar; or new product launch requiring education |
| **Frequency** | Weekly (weekends) at selected flagship stores |
| **Volume** | ~20–40 participants per session |
| **Owner** | Store Marketing Coordinator |
| **Participants** | Store Manager, Category Manager, Vendor Rep (Trainer), Customers |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Theme Selection**: Choose DIY topic (e.g., "Basic Plumbing", "Tile Laying") based on seasonal demand | Category Mgr | CMO | 1 hour |
| 2 | **Vendor Coordination**: Invite vendor to provide expert trainer and free sample materials | Category Mgr | — | 2 hours |
| 3 | **Promotion & Registration**: Advertise via social media (W142); manage registrations via Loyalty App | Marketing | Social Mgr | Ongoing |
| 4 | **Set-up**: Prepare demo area in-store; arrange tools, materials, and safety gear | Stock Assoc | Store Mgr | 2 hours |
| 5 | **Execution**: Conduct workshop; capture attendee leads; offer "Same Day" discount on featured tools | Vendor / Marketing | Store Mgr | 2–3 hours |
| 6 | **Feedback & Leads**: Collect survey (W65); update CRM with attendee interests for targeted follow-up | Marketing | — | 30 min |

---

## W148. Home Design & Consultancy Services

| Field | Detail |
|---|---|
| **Trigger** | Customer requests renovation planning for Kitchen, Bathroom, or Wardrobe |
| **Frequency** | Daily; ~5–10 requests per store/month |
| **Volume** | High-value sales potential (PHP 50,000–500,000 per lead) |
| **Owner** | Design Consultant |
| **Participants** | Customer, Sales Rep, Category Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Discovery**: Interview customer on needs, style, and budget; schedule site measurement if needed | Design Consultant | — | 1 hour |
| 2 | **3D Modeling**: Create kitchen/bath layout using design software; select SKUs from active assortment | Design Consultant | — | 2–4 hours |
| 3 | **Presentation**: Present 3D render and detailed BOM (Bill of Materials) to customer | Design Consultant | Sales Rep | 1 hour |
| 4 | **Quotation**: Generate project quotation (W58.1a) with bundled discount if applicable | Sales Rep | Category Mgr | 30 min |
| 5 | **Order Conversion**: Customer accepts; convert to Sales Order; coordinate delivery and installation (W138) | Sales Rep | Store Mgr | 15 min |

---

## W211. In-Store 3D Kitchen/Bathroom Design Rendering

| Field | Detail |
|---|---|
| **Trigger** | Customer request for customized kitchen, bathroom, or closet layout |
| **Frequency** | ~20–30 designs per store/month |
| **Volume** | High-value project leads |
| **Owner** | Design Consultant |
| **Participants** | Customer, Sales Rep, Category Manager (for custom SKU approval) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Space Survey**: Consultant captures floor plan dimensions (manual or via laser scanner app) | Consultant | — | 30 min |
| 2 | **Assortment Mapping**: System filters 3D assets library for SKUs currently in stock or available for order (W1) | System | — | Automated |
| 3 | **Interactive Design**: Consultant builds 3D model with customer; applies finishes (tiles, paint), fixtures, and cabinets | Consultant | — | 1–2 hours |
| 4 | **ERP BOM Linkage**: System automatically generates a Bill of Materials (BOM) linked to ERP SKU IDs and real-time prices | System | — | Real-time |
| 5 | **Margin Validation**: System checks total project margin; flags if bundled price falls below threshold (W102) | System | Category Mgr | Automated |
| 6 | **Rendering & Export**: Generate high-quality render; email to customer with link to "Click-to-Purchase" in Web Portal | Consultant | — | 15 min |
| 7 | **Quote Conversion**: Convert design BOM into a Formal Quotation in ERP (W58); reserve stock for 48 hours | Consultant | Sales Rep | 5 min |

### System Touchpoints
- 3D Design software integration with ERP Item Master and Pricing
- Automated BOM generation from design assets
- Margin-check workflow for project-based pricing
- Web portal integration for customer design viewing

---

## W168. Custom Paint Mixing & Tinting Operations

| Field | Detail |
|---|---|
| **Trigger** | Customer selects a base paint and a specific color from the swatch/fan deck |
| **Frequency** | High volume; ~15–30 tinting requests per store/day |
| **Volume** | ~100,000+ liters mixed annually chain-wide |
| **Owner** | Paint Department Supervisor |
| **Participants** | Paint Technician (Sales Associate), Customer, Cashier |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Color Selection**: Customer chooses color code from brand swatch; Technician identifies required Base Paint (A, B, C, or Deep) | Paint Technician | — | 3 min |
| 2 | **System Entry**: Technician enters Color Code and Can Size in the tinting machine software; system calculates required colorant dosage | Paint Technician | — | 2 min |
| 3 | **Tinting**: Technician places base can under dispenser; machine injects colorants; system logs colorant consumption per canister | Paint Technician | — | 2 min |
| 4 | **Mixing**: Can is sealed and placed in the Gyroscopic Mixer for 2–3 minutes to ensure uniform color distribution | Paint Technician | — | 3 min |
| 5 | **Quality Check**: Technician performs a "dot test" on the can lid; dries with heat gun; verifies match against physical swatch | Paint Technician | Dept Supervisor | 2 min |
| 6 | **Labeling & POS**: Technician generates a "Custom Tint" barcode label from the system; labels can; customer takes to Cashier | Paint Technician | — | 1 min |
| 7 | **Checkout**: Cashier scans Custom SKU; system deducts Base Paint and Colorants from inventory in real-time | Cashier | — | 30 sec |
| 8 | **Machine Maintenance**: Daily nozzle cleaning and weekly calibration to ensure color accuracy | Paint Technician | Dept Supervisor | 15 min |

### System Touchpoints
- Tinting software integration with ERP Item Master (Base + Colorants)
- Real-time consumption tracking of colorants (milliliters)
- Custom SKU generation at POS linked to original Base SKU for traceability
- Machine maintenance log tracking in W47 (Facility Maintenance)

---

## W169. Lumber & Board Cutting Services

| Field | Detail |
|---|---|
| **Trigger** | Customer purchases whole lumber/plywood and requests specific sizes |
| **Frequency** | Moderate; ~10–20 requests per store/day |
| **Volume** | Primary items: Plywood, Marine Board, 2x4 Lumber |
| **Owner** | Lumber Department Supervisor |
| **Participants** | Cutter (Stock Associate), Customer, Cashier |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Intake**: Customer presents purchased board/lumber or selects from floor; provides cutting list/dimensions | Cutter | — | 5 min |
| 2 | **Calculation**: Cutter calculates number of cuts; system determines "Cutting Fee" (e.g., first 2 cuts free, PHP 10 per subsequent cut) | Cutter | — | 2 min |
| 3 | **Payment**: Customer pays Cutting Fee at POS; receives "Cutting Authorization" slip | Cashier | — | 2 min |
| 4 | **Execution**: Cutter performs cuts using Table Saw or Panel Saw; adheres to safety protocols (PPE, machine guards) | Cutter | Dept Supervisor | 5–15 min |
| 5 | **Scrap Management**: (a) Off-cuts > 1ft offered to customer; (b) if declined, off-cuts moved to "Scrap Bin" for discounted sale or internal use | Cutter | — | 2 min |
| 6 | **Safety Log**: Cutter logs machine hours and blade condition; reports dull blades for sharpening/replacement (W47) | Cutter | Dept Supervisor | 5 min |

### System Touchpoints
- Service SKU for "Cutting Fee" at POS
- Scrap inventory tracking (Optional: creating "Remnant" SKUs for large off-cuts)
- Safety incident logging in W52 (Health & Safety)

---

## W213. Installation Service Partner Quality Audit

| Field | Detail |
|---|---|
| **Trigger** | Scheduled quarterly audit; or high complaint rate for a specific contractor (W138.8) |
| **Frequency** | Quarterly per contractor; or ad-hoc |
| **Owner** | Services Quality Manager |
| **Participants** | Services Quality Mgr, Contractor, Customer (for site visit) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Audit Scoping**: System identifies contractors with high volume or low CSAT (W65) in the past quarter | System | Services Qual Mgr | 30 min |
| 2 | **Site Visit**: Auditor visits 3–5 active/completed sites with the contractor; inspects workmanship against "BuildRight Standard" | Services Qual Mgr | — | 1 day |
| 3 | **Compliance Check**: Verify contractor's team has valid IDs, PPE, and appropriate tools (as required in W138 contract) | Services Qual Mgr | — | 1 hour |
| 4 | **Audit Report**: Auditor logs findings in system: workmanship score, safety score, compliance score | Services Qual Mgr | Services Mgr | 1 hour |
| 5 | **Scorecard Update**: Audit score feeds into the "Contractor Master Scorecard" (linked to W44) | System | — | Automated |
| 6 | **Corrective Action**: If score < 70%, contractor put on "Probation"; requires remedial training or face de-listing | Services Mgr | VP Store Ops | 1 hour |

### System Touchpoints
- Contractor quality audit module with photo upload capability
- CSAT and Complaint data integration for audit triggering
- Integration with Contractor Master Scorecard


