# Complete Vendor Stack Evaluation — BuildRight Depot Corp.

> Full-suite solution mapping for **SAP**, **Microsoft**, and **Oracle** — showing how each vendor's
> entire product portfolio (not just core ERP) addresses every BuildRight Depot requirement.
> This is the companion to [ERP-Evaluation-Matrix.md](ERP-Evaluation-Matrix.md) which evaluated
> core ERP capabilities only.

---

## 1. Vendor Solution Stacks

### 1.1 SAP Complete Stack

| Layer | Product | Role in BuildRight |
|---|---|---|
| **Core ERP** | SAP S/4HANA Cloud (private edition) | GL, AP, AR, FA, MM, SD, CO, consolidation |
| **Warehouse** | SAP Extended Warehouse Management (EWM) | RF-directed putaway/pick, yard mgmt, catch-weight |
| **POS** | SAP Customer Checkout 11 (CCO) | 1,000 POS terminals, offline mode, multi-tender |
| **Ecommerce** | SAP Commerce Cloud (CCv2) | BOPIS, home delivery, catalog, order mgmt |
| **Supply Chain Planning** | SAP Integrated Business Planning (IBP) | Demand forecasting, replenishment, S&OP |
| **HR & Payroll** | SAP SuccessFactors (EC, Payroll, Time, Talent) | PH payroll, time & attendance, recruitment, ESS |
| **CRM & Loyalty** | SAP Sales Cloud + SAP Loyalty Management | Trade accounts, loyalty tiers, pipeline mgmt |
| **Customer Analytics** | SAP Customer Activity Repository (CAR) | Real-time customer insights, purchase history |
| **Supplier Collaboration** | SAP Ariba / Business Network | Vendor portal, procurement collaboration, JBP |
| **Expense Management** | SAP Concur | Employee expense reimbursement |
| **Marketing** | SAP Emarsys (Customer Engagement) | Campaign management, email, personalization |
| **Customer Data** | SAP Customer Data Cloud (Gigya) | Unified CDP, identity management |
| **Analytics & BI** | SAP Analytics Cloud (SAC) + SAP Datasphere | Executive dashboards, self-service BI, data warehouse |
| **Integration** | SAP BTP Integration Suite (CPI) | Middleware for all system-to-system integration |
| **Extension Platform** | SAP BTP (Cloud Foundry / ABAP Environment) | Custom apps, PH localization extensions |
| **Master Data** | SAP MDG (Master Data Governance) | Item, vendor, customer master governance |
| **Document Management** | SAP ArchiveLink + SAP ILM | Document storage, retention, BIR compliance |
| **Industry** | SAP Retail / CAR Retail Extension Pack | Retail-specific pricing, promotions, markdown |
| **AI** | SAP Business AI / SAP AI Core | Predictive analytics, intelligent automation |
| **IoT** | SAP IoT (on BTP) | Smart store, fleet telematics |

### 1.2 Microsoft Complete Stack

| Layer | Product | Role in BuildRight |
|---|---|---|
| **Core ERP** | Dynamics 365 Finance | GL, AP, AR, FA, consolidation, tax |
| **Supply Chain** | Dynamics 365 Supply Chain Management | Inventory, procurement, WMS, planning |
| **POS & Retail** | Dynamics 365 Commerce | 1,000 POS terminals, offline CSU, retail pricing |
| **Ecommerce** | Dynamics 365 Commerce (e-commerce module) | BOPIS, home delivery, catalog, storefront |
| **HR** | Dynamics 365 Human Resources | Leave, benefits, ESS, performance |
| **Payroll** | ISV Partner (e.g., Itsubmit, SL Payroll) | PH statutory payroll (SSS, PhilHealth, Pag-IBIG, BIR) |
| **CRM & Sales** | Dynamics 365 Sales + Customer Insights | Trade accounts, pipeline, territory mgmt |
| **Loyalty** | Dynamics 365 Commerce (native loyalty engine) | Points, tiers, earn/redeem at POS |
| **Customer Service** | Dynamics 365 Customer Service | Omnichannel ticketing, call center, SLA |
| **Marketing** | Dynamics 365 Customer Insights – Journeys | Campaigns, email, segmentation, personalization |
| **CDP** | Dynamics 365 Customer Insights | Unified customer profile, identity resolution |
| **Expense** | Dynamics 365 Expense Management / Concur | Employee expense reimbursement |
| **Field Service** | Dynamics 365 Field Service | Installation services, scheduling, dispatch |
| **Analytics & BI** | Power BI (Pro/Premium) + Azure Synapse | Dashboards, self-service BI, data warehouse |
| **Workflow & Automation** | Power Automate + Power Apps | Approval workflows, custom apps (LGU, CIT, etc.) |
| **Integration** | Azure API Management + Logic Apps / Service Bus | Middleware for all external integrations |
| **Cloud** | Azure (East Asia / Southeast Asia region) | Cloud infrastructure, DR, scalability |
| **AI** | Azure AI + Copilot + Copilot Studio | Predictive analytics, chatbots, AI automation |
| **IoT** | Azure IoT Hub + Azure Digital Twins | Smart store, fleet telematics, sensors |
| **Collaboration** | Microsoft 365 / Teams / SharePoint | Document management, collaboration, approvals |
| **Security** | Azure Active Directory + Microsoft Purview | Identity, RBAC, data governance, compliance |
| **Low-Code Apps** | Power Apps (Canvas + Model-driven) | Custom gap-fillers (hazmat, PPE, permits, etc.) |

### 1.3 Oracle Complete Stack

| Layer | Product | Role in BuildRight |
|---|---|---|
| **Core ERP** | Oracle Fusion Cloud ERP | GL, AP, AR, FA, project accounting |
| **Supply Chain** | Oracle Fusion Cloud SCM (Supply Chain Orchestration) | Inventory, procurement, order management |
| **Warehouse** | Oracle Warehouse Management Cloud (LogFire) | RF-directed operations, wave picking, cross-dock |
| **POS** | Oracle Retail Xstore Point-of-Service | 1,000 POS terminals, offline, multi-tender, catch-weight |
| **Retail Merchandising** | Oracle Retail Merchandising Foundation | Retail pricing, promotions, markdown, allocation |
| **Ecommerce** | Oracle Commerce Cloud | BOPIS, home delivery, catalog, storefront |
| **Order Management** | Oracle Fusion Cloud Order Management | Order capture, orchestration, fulfillment routing |
| **Supply Chain Planning** | Oracle Fusion Cloud Supply Planning | Demand forecasting, replenishment, S&OP |
| **HR & Payroll** | Oracle Fusion Cloud HCM (Global HR, Payroll, Time, Talent) | PH payroll, time & attendance, recruitment, ESS |
| **CRM & Sales** | Oracle Fusion Cloud CX (Sales) | Trade accounts, pipeline, territory mgmt |
| **Loyalty** | Oracle CrowdTwist (Loyalty & Engagement) | Points, tiers, earn/redeem, gamification |
| **Customer Service** | Oracle Fusion Cloud CX (Service) | Omnichannel ticketing, call center, SLA |
| **Marketing** | Oracle Fusion Cloud CX (Marketing / Maxymiser) | Campaigns, email, personalization, A/B testing |
| **CDP** | Oracle CX Unity | Unified customer profile, identity resolution |
| **Consolidation** | Oracle Enterprise Performance Management (EPM) Cloud | Financial consolidation, planning, budgeting |
| **Expense** | Oracle Expenses Cloud | Employee expense reimbursement |
| **Analytics & BI** | Oracle Analytics Cloud + Autonomous Data Warehouse | Dashboards, self-service BI, data warehouse |
| **Integration** | Oracle Integration Cloud (OIC) | Middleware for all system-to-system integration |
| **Extension** | Oracle Visual Builder Cloud Service (VBCS) | Custom apps, PH localization extensions |
| **Master Data** | Oracle Product Hub + Oracle Customer Data Management | Item, vendor, customer master governance |
| **Document Management** | Oracle Content and Experience Cloud + WebCenter | Document storage, retention, collaboration |
| **Industry** | Oracle Retail Suite (Xstore, RMS, RPM, RI) | Retail-specific pricing, promotions, planograms |
| **Construction** | Oracle Aconex / Oracle Construction Intelligence | New store construction project management |
| **AI** | Oracle AI Services (OCI AI) | Predictive analytics, NLP, computer vision |
| **IoT** | Oracle IoT Cloud | Smart store, fleet telematics, asset monitoring |
| **Cloud** | Oracle Cloud Infrastructure (OCI) | Cloud infrastructure, DR, scalability |

---

## 2. Gap Resolution Matrix — How the Full Stack Fills Gaps

The table below shows every requirement that was scored 🔧 (custom/3rd-party) or ❌ (not available)
in the [original matrix](ERP-Evaluation-Matrix.md), re-evaluated with the **complete vendor stack**.

### 2.1 Financial Management (FIN)

| Req ID | Requirement | Original Gap | SAP Stack Resolution | MS Stack Resolution | Oracle Stack Resolution |
|---|---|---|---|---|---|
| FIN-008 | BIR Tax Return Generation | 🔧 All 3 | 🔧 **Still needs PH ISV** — SAP PH localization partner (e.g., DXC,Accenture) builds BIR form templates on S/4 + BTP | 🔧 **Still needs PH ISV** — PH tax ISV builds BIR forms on D365 Finance + Power Automate for eFPS | 🔧 **Still needs PH partner** — Oracle PH partner builds BIR form templates on Fusion ERP + VBCS |
| FIN-021 | FX Hedging / Forward Contracts | 🔧 D365 | ✅ SAP Treasury covers this | 🔧 **Power App + D365 Finance** — custom FX hedging tracker using Power Apps canvas app + D365 currency revaluation | ✅ Oracle Treasury covers this |
| FIN-023 | Insurance Policy Lifecycle | 🔧 All 3 | ⚙️ **SAP BTP custom app** or SAP RE FX (Real Estate Flex) extended for insurance | ⚙️ **Power App** for insurance registry with Power Automate renewal alerts | ⚙️ **VBCS custom app** for insurance policy registry with OIC workflow |
| FIN-024 | Employee Gratuity (RA 7641) | 🔧 All 3 | ⚙️ **SuccessFactors Payroll** with PH localization — RA 7641 rules configured as custom payroll calculation | ⚙️ **ISV PH payroll partner** (Itsubmit/SL) — RA 7641 configured in payroll rules | ⚙️ **Oracle HCM Payroll** with PH localization — RA 7641 rules configured as custom payroll element |
| FIN-025 | Cash-in-Transit / Armored Car | 🔧 All 3 | ⚙️ **BTP custom app** — CIT scheduling with integration to SAP Treasury for bank reconciliation | ⚙️ **Power App** — CIT scheduling + tracking with Power Automate reconciliation to D365 bank transactions | ⚙️ **VBCS custom app** — CIT management with OIC integration to Fusion Cash Management |
| FIN-030 | Fixed Asset Physical Verification | 🔧 All 3 | ⚙️ **SAP Asset Intelligence Network** or custom BTP app for asset scanning via mobile | ⚙️ **Power App** with camera/barcode scanning for asset verification + D365 Fixed Assets | ⚙️ **VBCS mobile app** for asset tag scanning + Fusion Fixed Assets reconciliation |
| FIN-031 | BIR eFPS Filing & e-Payment | 🔧 All 3 | 🔧 **PH localization partner + BTP Integration** — SAP S/4 tax data → BTP integration → eFPS submission; **still requires PH ISV** | 🔧 **PH ISV + Power Automate** — D365 tax data → Power Automate RPA → eFPS submission; **still requires PH ISV** | 🔧 **PH partner + OIC** — Fusion tax data → OIC integration → eFPS submission; **still requires PH partner** |
| FIN-032 | E-Wallet Settlement Reconciliation | 🔧 All 3 | ⚙️ **BTP Integration Suite** — Build adapters for GCash/Maya settlement file import → auto-match in SAP AP | ⚙️ **Azure Logic Apps** — Import settlement files → auto-match in D365 bank reconciliation | ⚙️ **OIC adapters** — Import settlement files → auto-match in Fusion Cash Management |

### 2.2 Inventory Management (INV)

| Req ID | Requirement | Original Gap | SAP Stack Resolution | MS Stack Resolution | Oracle Stack Resolution |
|---|---|---|---|---|---|
| INV-010 | Catch-Weight / Variable Measure | ⚠️ All 3 | ⚙️ **SAP EWM + Retail for Catch-Weight** — SAP has catch-weight management in EWM with integration to SD pricing; board-feet/meter conversion units configured | ⚙️ **D365 SCM product variants** — Configure catch-weight with UOM conversions; dual-UOM tracking (inventory UOM vs. sales UOM) | ⚙️ **Oracle Retail Xstore + RMS** — Oracle Retail supports catch-weight natively in Xstore POS and RMS; dual-UOM for lumber/wire |
| INV-016 | Product Recall Tracking | 🔧 All 3 | ⚙️ **SAP QM + Batch Where-Used** — Lot traceability with recall workflow in QM; batch where-used list identifies affected customers | ⚙️ **Power App + D365 SCM** — Custom recall case management app with batch tracing via D365 inventory | ⚙️ **Oracle Supply Chain Traceability** — Lot/serial trace in Fusion SCM with recall workflow in VBCS |
| INV-017 | Consignment Tracking | 🔧 Oracle | ✅ SAP handles natively | ✅ D365 handles natively | ⚙️ **Oracle Retail RMS + Fusion SCM** — Oracle Retail Merchandising supports consignment; configure ownership transfer rules |
| INV-020 | Store Inventory Rebalancing | 🔧 D365/Oracle | ⚙️ **SAP IBP for Response & Supply** — Suggests rebalancing based on demand signals across locations | ⚙️ **D365 Planning Optimization** — Rebalancing suggestions via demand planning + distribution requirements | ⚙️ **Oracle Supply Planning** — Rebalancing suggestions via constrained supply planning |

### 2.3 Procurement & Purchasing (PUR)

| Req ID | Requirement | Original Gap | SAP Stack Resolution | MS Stack Resolution | Oracle Stack Resolution |
|---|---|---|---|---|---|
| PUR-007 | Vendor Portal | ⚙️ D365 | ✅ SAP Ariba Supplier Portal | ⚙️ **D365 Vendor Collaboration** workspace — vendors view POs, submit confirmations; full invoice submission via Power Pages portal | ✅ Oracle Supplier Portal |
| PUR-008 | Vendor Performance Scorecard | ⚙️ D365/Oracle | ✅ SAP MM Vendor Evaluation | ⚙️ **Power BI + D365** — Custom vendor scorecard dashboard with on-time delivery, quality, fill rate metrics from D365 data | ⚙️ **Oracle BI + Fusion Procurement** — Supplier performance analytics via OTBI dashboards |
| PUR-016 | AQL Sampling per SKU Category | 🔧 D365 | ⚙️ **SAP QM** — Quality inspection plans with AQL sampling per material type | ⚙️ **D365 Quality Management** — Inspection groups with sampling plans per item category | ⚙️ **Oracle Quality** — Quality inspection plans with AQL sampling |
| PUR-017 | Supplier Quality & CAPA | 🔧 D365 | ✅ **SAP QM + Ariba Supplier Management** — Full CAPA workflow, 8D reporting, supplier quality portal | ⚙️ **D365 Quality Management + Power App** — Quality issue logging with CAPA workflow in Power Automate | ⚙️ **Oracle Quality + Fusion Supplier qualification** — Quality holds, CAPA tracking |
| PUR-020 | Vendor Price Protection Claims | 🔧 All 3 | ⚙️ **SAP Settlement Management** — Price protection claims with credit memo generation | ⚙️ **D365 Trade Allowance Management** — Price protection claim filing and credit processing | ⚙️ **Oracle Trade Management** — Price protection claims and settlements |
| PUR-021 | Vendor Strategic Collaboration & JBP | 🔧 All 3 | ✅ **SAP Ariba — JBP workspace** — Joint business planning, shared scorecards, co-investment tracking | ⚙️ **Power Pages vendor portal + Power BI** — Shared JBP workspace with scorecards and calendar | ⚙️ **Oracle Supplier Collaboration** — JBP workspace in Fusion with shared analytics |
| PUR-022 | PL Factory Audit & Social Compliance | 🔧 All 3 | ✅ **SAP Ariba Supply Chain Risk** — Supplier risk assessment, audit management, compliance scoring | ⚙️ **Power App** — Factory audit checklist app with scoring, photo capture, corrective action tracking | ⚙️ **Oracle Supplier Qualification Management** — Audit questionnaires, scoring, corrective actions |
| PUR-023 | Supplier Diversity / MSME | 🔧 All 3 | ⚙️ **SAP Ariba + custom reporting** — Vendor classification fields for MSME; diversity spend reporting via SAC | ⚙️ **Power App + Power BI** — MSME vendor classification and diversity spend reporting | ⚙️ **Oracle Supplier classification + BI** — MSME vendor attributes with diversity analytics |
| PUR-024 | Product Quality Testing | 🔧 D365 | ✅ **SAP QM** — Test plans, result recording, CoC tracking, failed test disposition | ⚙️ **D365 Quality Management** — Inspection orders with test results and disposition | ⚙️ **Oracle Quality** — Test specifications, result recording, CoC tracking |

### 2.4 Warehouse Management (WMS)

| Req ID | Requirement | Original Gap | SAP Stack Resolution | MS Stack Resolution | Oracle Stack Resolution |
|---|---|---|---|---|---|
| WMS-006 | Yard Management (Lumber) | 🔧 D365/Oracle | ✅ **SAP EWM Yard Management** — Outdoor stock with yard movements, gate entry/exit, parking space management | ⚙️ **Power App** — Yard inventory tracking app with map-based location for outdoor lumber yard | ⚙️ **Oracle WMS Cloud yard mgmt** — Yard operations with location mapping for outdoor areas |
| WMS-008 | WMS-ERP Integration | ⚠️ Oracle (separate cloud) | ✅ EWM embedded in S/4HANA | ✅ WMS native in D365 SCM | ⚙️ **OIC prebuilt adapter** — Oracle WMS Cloud connects to Fusion SCM via Integration Cloud; real-time sync requires careful latency tuning |

### 2.5 Point-of-Sale (POS) & Retail — **THE CRITICAL GAPS**

| Req ID | Requirement | Original Gap | SAP Stack Resolution | MS Stack Resolution | Oracle Stack Resolution |
|---|---|---|---|---|---|
| POS-001 | 1,000 POS Terminals | 🔧 SAP, ❌ Oracle | ⚙️ **SAP Customer Checkout 11** — Redesigned for scale; supports multi-register, headless API architecture; **verify proven deployments at 1K+ terminals** | ✅ **D365 Commerce POS** — Proven at scale (Walmart, retail chains); Commerce Scale Unit (CSU) handles 1K+ terminals | ⚙️ **Oracle Retail Xstore** — Enterprise retail POS used by major retailers (Gap, American Eagle); proven at 1K+ terminals. **Must integrate with Fusion SCM via OIC** |
| POS-002 | Offline Mode | ⚠️ SAP, ❌ Oracle | ⚙️ **SAP CCO offline** — CCO v11 has offline transaction queue; syncs on reconnect. **Limitation: offline duration and data volume need validation** | ✅ **CSU offline mode** — Full offline capability; stores complete transaction locally; 8+ hours proven; auto-sync on reconnect | ⚙️ **Oracle Xstore offline** — Xstore has robust offline mode with local database; proven for extended offline in retail. **Integrates with Oracle Retail cloud** |
| POS-005 | Loyalty Integration | ⚙️ SAP | ⚙️ **SAP Loyalty Management → CCO** — Loyalty engine on SAP Cloud; CCO calls loyalty API for earn/redeem. Requires BTP integration | ✅ **Native** — D365 Commerce loyalty engine built-in | ⚙️ **Oracle CrowdTwist → Xstore** — Loyalty engine in Oracle CX; Xstore calls CrowdTwist API for earn/redeem |
| POS-010 | Quantity Break Pricing | ⚙️ SAP/Oracle | ⚙️ **SAP Retail Pricing** — Quantity-based pricing conditions in SD; applied at POS via pricing engine call to S/4 | ✅ **Native** — D365 Commerce quantity discounts built-in | ⚙️ **Oracle Retail Price Management (RPM)** — Quantity break pricing rules in RPM; pushed to Xstore |
| POS-012 | Receipt Printing (BIR format) | 🔧 All 3 | 🔧 **Custom receipt template** — BIR-compliant layout built in CCO receipt designer; TIN, business name, permit number | 🔧 **Custom receipt template** — BIR-compliant layout built in D365 Commerce receipt designer | 🔧 **Custom receipt template** — BIR-compliant layout in Xstore receipt designer |
| POS-014a | Senior/PWD Discount (PH Legal) | 🔧 All 3 | ⚙️ **Custom pricing rule in SAP** — SC/PWD 20% discount as pricing condition with ID-based validation; BIR logs via custom BTP app | ⚙️ **Custom pricing rule in D365 Commerce** — SC/PWD discount as retail discount with ID capture; BIR-compliant audit log via extension | ⚙️ **Custom pricing rule in Xstore** — SC/PWD discount as promotion rule with ID-based trigger; BIR logs via custom extension |
| POS-015 | Gift Card / Store Credit | ⚙️ SAP/Oracle | ⚙️ **SAP Gift Card** solution or BTP extension for gift card management with issuance, reload, redemption | ✅ **Native** — D365 Commerce gift card module | ⚙️ **Oracle Retail Gift Card** — Oracle Retail has gift card module; integrates with Xstore |
| POS-016 | Catch-Weight at POS | 🔧 All 3 | ⚙️ **SAP CCO + EWM catch-weight** — Variable weight entry at POS; price calculated per unit of measure; integrates with EWM stock | ⚙️ **D365 Commerce + SCM catch-weight** — Variable weight entry at POS; dual-UOM pricing | ⚙️ **Oracle Xstore native catch-weight** — Xstore supports variable weight/measure selling natively for retail; integrates with RMS |
| POS-017 | Paint Mixing / Custom SKU | 🔧 All 3 | ⚙️ **BTP extension** — Custom SKU generator app linked to CCO; base paint + colorant inventory deduction in S/4 | ⚙️ **D365 Commerce extension** — Custom SKU generator as POS extension; kit/bom explosion for base paint + colorant | ⚙️ **Oracle Xstore + RMS** — Custom item assembly in Xstore; bill of material for paint mixing in RMS |
| POS-018 | Age-Restricted Prompts | ⚙️ SAP, 🔧 Oracle | ⚙️ **SAP CCO configuration** — Age-restriction prompt on flagged items; cashier confirmation required | ✅ **Native** — Age restriction prompts in D365 Commerce | ⚙️ **Oracle Xstore configuration** — Age-restriction prompt on restricted items |
| POS-019 | Warranty Claim Registration | 🔧 All 3 | ⚙️ **SAP Service Cloud** — Warranty registration at POS with service ticket creation; vendor return tracking integration | ⚙️ **D365 Customer Service + Commerce** — Warranty claim created at POS; ticket routed to service team | ⚙️ **Oracle CX Service + Xstore** — Warranty claim at POS; service ticket in Oracle CX |
| POS-020 | Layaway / Installment Sales | 🔧 All 3 | ⚙️ **BTP custom app** — Layaway management with deposit collection, schedule, inventory reservation in S/4 | ⚙️ **D365 Commerce extension** — Layaway module as POS extension with order management integration | ⚙️ **Oracle Xstore extension** — Layaway/special order module in Xstore with Oracle Order Management |
| POS-022 | Employee Discount | ⚙️ SAP/Oracle | ⚙️ **SAP HR-SD integration** — Employee ID badge → SuccessFactors lookup → discount condition applied in CCO | ⚙️ **D365 Commerce + HR** — Employee badge scan → D365 HR lookup → discount applied at POS | ⚙️ **Oracle HCM-Xstore integration** — Employee ID → HCM lookup → discount applied in Xstore |
| POS-023 | Store-Level Delivery Scheduling | 🔧 All 3 | ⚙️ **SAP Commerce + S/4 Delivery** — Delivery scheduling in Commerce Cloud; fulfillment in S/4 LE | ⚙️ **D365 Commerce + Field Service** — Delivery scheduling with route optimization | ⚙️ **Oracle Xstore + Logistics** — Delivery scheduling at POS; fulfillment in Oracle Logistics Cloud |

### 2.6 Ecommerce (ECOM)

| Req ID | Requirement | Original Gap | SAP Stack Resolution | MS Stack Resolution | Oracle Stack Resolution |
|---|---|---|---|---|---|
| ECOM-006 | Payment Gateway (PH) | 🔧 All 3 | ⚙️ **SAP Commerce + BTP Integration** — Custom payment adapter for PayMongo/Dragonpay/GCash built on Commerce extension framework | ⚙️ **D365 Commerce payment connector** — Custom payment connector for PH gateways using Commerce extensibility | ⚙️ **Oracle Commerce + OIC** — Custom payment integration adapter for PH gateways |
| ECOM-012 | Delivery Partner (3PL) | 🔧 All 3 | ⚙️ **BTP Integration** — Build adapters for Lalamove/Transportify APIs via SAP CPI | ⚙️ **Azure Logic Apps** — Pre-built/custom connectors for Lalamove/Transportify APIs | ⚙️ **OIC adapters** — Build integration adapters for PH 3PL carriers |
| ECOM-013 | Marketplace (Lazada/Shopee) | 🔧 All 3 | ⚙️ **SAP Commerce + CPI** — Marketplace integration via SAP Commerce Marketplace extension or CPI adapters | ⚙️ **Azure Logic Apps + D365 Commerce** — Marketplace order pull, inventory sync via connectors | ⚙️ **Oracle Commerce + OIC** — Marketplace API integration via Oracle Integration Cloud |
| ECOM-014 | Ship-from-Store | ⚠️ Oracle | ⚙️ **SAP CAR + EWM** — Ship-from-store with real-time ATP check across stores | ⚙️ **D365 Commerce** — Native ship-from-store with store inventory ATP | ⚙️ **Oracle Xstore + Order Management** — Ship-from-store routing via Oracle Order Management with store ATP |
| ECOM-015 | Omni-channel Ticketing | ⚠️ All 3 | ✅ **SAP Service Cloud** — Omnichannel ticketing with CRM integration | ✅ **D365 Customer Service** — Omnichannel ticketing with unified queue | ✅ **Oracle CX Service** — Omnichannel ticketing with SLA management |

### 2.7 HR & Payroll (HR)

| Req ID | Requirement | Original Gap | SAP Stack Resolution | MS Stack Resolution | Oracle Stack Resolution |
|---|---|---|---|---|---|
| HR-002 | PH Statutory Deductions | ⚠️ SAP, 🔧 D365, ⚠️ Oracle | ⚙️ **SuccessFactors PH Payroll** — SAP has growing PH payroll localization; SSS, PhilHealth, Pag-IBIG configured in payroll rules. **Verify completeness with SAP PH partner** | 🔧 **ISV PH Payroll Partner** — D365 has no native PH payroll; must use ISV (e.g., Itsubmit, SL Global, or custom Power Platform payroll). **Highest risk** | ⚙️ **Oracle HCM Payroll PH** — Oracle has PH payroll localization; statutory deductions configured as payroll elements. **Verify completeness with Oracle PH partner** |
| HR-003 | BIR Withholding Tax (Comp) | ⚠️ SAP, 🔧 D365, ⚠️ Oracle | ⚙️ **SuccessFactors Payroll PH** — TRAIN law tax tables configured; verify auto-update mechanism | 🔧 **ISV PH Payroll** — BIR compensation withholding tax tables in ISV payroll | ⚙️ **Oracle HCM Payroll PH** — TRAIN law tax tables configured as payroll balance definitions |
| HR-013 | Employee Loan & Advance | 🔧 D365 | ⚙️ **SuccessFactors Payroll** — Loan deduction elements configured in payroll with amortization schedule | ⚙️ **ISV Payroll or Power App** — Loan management app with payroll deduction integration | ⚙️ **Oracle HCM Payroll** — Loan deduction elements configured in payroll |
| HR-014 | Grievance & Whistleblower | 🔧 All 3 | ⚙️ **SuccessFactors Case Management** or BTP custom app for anonymous submission | ⚙️ **Power App + D365 HR** — Anonymous grievance submission app with case routing | ⚙️ **Oracle HCM Journeys + VBCS** — Grievance workflow with anonymous submission option |
| HR-015 | PH Statutory Benefits & Claims | 🔧 D365 | ⚙️ **SuccessFactors Benefits** — PH statutory benefits configured; SSS salary loan, PhilHealth claims workflows | 🔧 **ISV Payroll + Power App** — PH statutory benefits managed in ISV payroll; claims via Power App | ⚙️ **Oracle HCM Benefits PH** — PH statutory benefits configured as benefit plans |

### 2.8 Non-Functional Requirements (NFR)

| Req ID | Requirement | Original Gap | SAP Stack Resolution | MS Stack Resolution | Oracle Stack Resolution |
|---|---|---|---|---|---|
| NFR-009 | PH Localization | ⚠️ All 3 | ⚠️ **SAP PH localization** — Growing; BIR, VAT basic; gaps in eFPS, BIR CAS, LGU permits. **Needs PH implementation partner with localization assets** | ⚠️ **D365 PH localization** — Limited; basic VAT/WHT; gaps in BIR forms, eFPS, CAS, LGU. **Needs PH ISV ecosystem** | ⚠️ **Oracle PH localization** — Limited; basic VAT/WHT; gaps in BIR forms, eFPS, CAS. **Needs PH partner with localization assets** |
| NFR-011 | Offline POS (≥ 8 hours) | ⚠️ SAP, ❌ Oracle | ⚙️ **SAP CCO v11 offline** — Transaction queuing with local DB; **needs load testing for 8-hour window** | ✅ **D365 CSU offline** — Proven extended offline; full transaction capability | ⚙️ **Oracle Xstore offline** — Robust offline with local Oracle DB; **proven in retail but needs validation with Fusion integration** |
| NFR-017 | LGU Business Permit Tracking | 🔧 All 3 | ⚙️ **BTP custom app** — LGU permit calendar per location with renewal alerts and document storage | ⚙️ **Power App** — LGU permit tracker with Dataverse; renewal alerts via Power Automate | ⚙️ **VBCS custom app** — LGU permit calendar with OIC workflow for renewal alerts |
| NFR-018 | ESG & Sustainability | 🔧 All 3 | ⚙️ **SAP Sustainability Control Tower** — Carbon footprint tracking, ESG reporting, waste diversion metrics | 🔧 **Power BI + Power App** — Custom ESG data collection and reporting dashboards | 🔧 **Oracle ESG reporting** — Sustainability analytics in Oracle Analytics Cloud + custom VBCS app |
| NFR-019 | Fleet Optimization | 🔧 All 3 | ⚙️ **SAP Transportation Management + BTP IoT** — Route optimization, telematics, fuel tracking | ⚙️ **Azure Maps + IoT + Power App** — Fleet tracking, route optimization, fuel monitoring | ⚙️ **Oracle Transportation Management + IoT Cloud** — Route planning, telematics, fleet analytics |
| NFR-021 | Smart Store Operations | 🔧 All 3 | ⚙️ **SAP IoT + BTP** — Mobile POS queue busting, smart safe integration, 3D rendering app | ⚙️ **Azure IoT + D365 Commerce + Power Apps** — Mobile POS, smart safe, smart locker integration | ⚙️ **Oracle IoT + Xstore** — Mobile POS, smart safe, custom 3D rendering app |
| NFR-022a | BIR CAS Registration | 🔧 All 3 | ⚙️ **BTP custom app** — CAS registration status per location, permit renewal tracking, compliance docs | ⚙️ **Power App** — CAS registration tracker with Dataverse, renewal alerts, compliance documents | ⚙️ **VBCS custom app** — CAS registration status dashboard with OIC workflow |
| NFR-024 | IT Asset Lifecycle | 🔧 All 3 | ⚙️ **SAP EAM / Asset Manager** — IT hardware asset tracking with maintenance scheduling | ⚙️ **Power App + Azure AD** — IT asset registry with Intune integration for device management | ⚙️ **Oracle Assets + VBCS** — IT asset tracking with custom lifecycle workflow |

### 2.9 Cross-Functional (GOV, SRV, WSL, MER, DOC)

| Req ID | Requirement | Original Gap | SAP Stack Resolution | MS Stack Resolution | Oracle Stack Resolution |
|---|---|---|---|---|---|
| GOV-001 | Corporate Governance & Legal | 🔧 All 3 | ⚙️ **SAP GRC** — Governance, risk, compliance; board resolutions in custom BTP app | ⚙️ **Power App + M365** — Legal case management, SOP governance in SharePoint + Power Automate | ⚙️ **Oracle GRC + VBCS** — Corporate governance, legal tracking in custom app |
| GOV-003 | Real Estate & Lease Management | 🔧 All 3 | ⚙️ **SAP RE FX (Flexible Real Estate)** — Lease administration, rent processing, property tax | ⚙️ **Power App + D365 Finance** — Lease tracking app with rent payment integration | ⚙️ **Oracle Real Estate Management** — Lease admin, rent processing, property tax |
| GOV-004 | Health, Safety & Environment | 🔧 All 3 | ⚙️ **SAP EHS (Environment, Health & Safety)** — Incident reporting, safety inspections, corrective actions | ⚙️ **Power App + D365** — OHS incident reporting app with inspection scheduling | ⚙️ **Oracle EHS** — Incident management, safety inspections, corrective actions |
| GOV-005 | Engineering & Construction | 🔧 All 3 | ⚙️ **SAP S/4HANA Project System (PS)** — Construction project management, bidding, supervision | ⚙️ **D365 Project Operations + Power App** — Construction project management | ⚙️ **Oracle Aconex + Construction Intelligence** — New store construction, bidding, supervision, commissioning |
| GOV-007 | Fleet Operations & Driver Mgmt | 🔧 All 3 | ⚙️ **SAP TM + BTP IoT** — Route planning, driver scoring, fuel monitoring, telematics | ⚙️ **Azure Maps + IoT + Power App** — Fleet tracking, driver scoring, fuel management | ⚙️ **Oracle Transportation Mgmt + IoT** — Route planning, telematics, fleet analytics |
| GOV-008 | Sustainability & Environmental | 🔧 All 3 | ⚙️ **SAP Sustainability Control Tower** — GHG tracking, waste reporting, social impact | ⚙️ **Power BI + Power App** — Custom sustainability metrics dashboard | ⚙️ **Oracle Sustainability** — Environmental compliance tracking |
| GOV-009 | Innovation & Digital Transformation | 🔧 All 3 | ⚙️ **SAP Business AI + BTP** — AI personalization, RPA, computer vision, predictive analytics | ⚙️ **Azure AI + Copilot + Power Automate** — AI personalization, RPA, computer vision | ⚙️ **Oracle AI Services** — Predictive analytics, NLP, computer vision |
| GOV-010 | Marketing Campaign Management | 🔧 All 3 | ✅ **SAP Emarsys** — Full marketing automation, loyalty governance, social, PR, crisis management | ✅ **D365 Customer Insights – Journeys** — Campaign planning, execution, measurement | ✅ **Oracle CX Marketing** — Campaign management, email, social, analytics |
| GOV-016 | Employee Training & Development | 🔧 All 3 | ✅ **SuccessFactors Learning** — LMS with training programs, skills certification, compliance tracking | ⚙️ **D365 HR + LinkedIn Learning** — Training management with LinkedIn Learning integration | ✅ **Oracle HCM Learning** — LMS with training programs, compliance tracking |
| GOV-017 | Employee Performance & Career | 🔧 All 3 | ✅ **SuccessFactors Performance & Goals + Succession** — Full talent management suite | ⚙️ **D365 HR + LinkedIn Talent** — Performance reviews, succession, career development | ✅ **Oracle HCM Talent** — Performance management, succession planning, career development |
| GOV-018 | Store Performance Management | 🔧 All 3 | ⚙️ **SAP CAR + SAC** — Store KPIs, scorecard, benchmarking, action plan tracking | ⚙️ **Power BI + D365** — Store scorecard dashboards with action plan tracking in Power App | ⚙️ **Oracle BI + Fusion** — Store performance dashboards with custom action plans |
| GOV-025 | Sales Commission Management | 🔧 All 3 | ⚙️ **SAP Sales Cloud + S/4** — Commission calculation with GL posting and payroll integration | ⚙️ **D365 Sales + Finance** — Commission plans with accrual and payroll posting | ⚙️ **Oracle Sales + Fusion** — Commission calculation with GL posting |
| SRV-001 | Installation & Services | 🔧 All 3 | ⚙️ **SAP S/4 Service Order** or **SAP Field Service Management** — Service order creation, scheduling, revenue recognition | ⚙️ **D365 Field Service** — Service scheduling, resource allocation, completion, revenue recognition | ⚙️ **Oracle Field Service** — Service scheduling, resource management, revenue recognition |
| DOC-007 | Hazardous Waste Disposal | 🔧 All 3 | ⚙️ **SAP EHS** — Hazmat tracking, waste manifest, transporter accreditation, disposal reporting | ⚙️ **Power App** — DENR-compliant hazmat tracking app with quarterly reporting | ⚙️ **Oracle EHS** — Hazmat tracking with regulatory reporting |
| DOC-008 | Enterprise Retention & Archiving | ⚙️ All 3 | ✅ **SAP ILM (Information Lifecycle Management)** — Configurable retention per doc type, legal hold, secure destruction | ⚙️ **SharePoint compliance + D365** — Retention policies per document type with legal hold | ⚙️ **Oracle Records Management** — Retention policies, legal hold, secure destruction |

---

## 3. Updated Fit Assessment — Core ERP vs. Full Stack

The table below shows how the fit score changes when the **complete vendor portfolio** is applied
instead of just the core ERP module.

| Category | Must Have Count | SAP Core Only | SAP Full Stack | MS Core Only | MS Full Stack | Oracle Core Only | Oracle Full Stack |
|---|---|---|---|---|---|---|---|
| R1. Financial Management | 22 | 15 ✅ · 5 ⚙️ · 2 🔧 | 15 ✅ · 6 ⚙️ · 1 🔧 | 13 ✅ · 6 ⚙️ · 3 🔧 | 14 ✅ · 6 ⚙️ · 2 🔧 | 14 ✅ · 5 ⚙️ · 3 🔧 | 15 ✅ · 5 ⚙️ · 2 🔧 |
| R2. Inventory | 12 | 10 ✅ · 1 ⚙️ · 1 🔧 | 10 ✅ · 2 ⚙️ | 9 ✅ · 2 ⚙️ · 1 🔧 | 10 ✅ · 2 ⚙️ | 8 ✅ · 3 ⚙️ · 1 🔧 | 10 ✅ · 2 ⚙️ |
| R3. Procurement | 12 | 10 ✅ · 2 ⚙️ | 11 ✅ · 1 ⚙️ | 8 ✅ · 2 ⚙️ · 2 🔧 | 10 ✅ · 2 ⚙️ | 8 ✅ · 3 ⚙️ · 1 🔧 | 10 ✅ · 2 ⚙️ |
| R4. Warehouse | 5 | 5 ✅ | 5 ✅ | 4 ✅ · 1 🔧 | 4 ✅ · 1 ⚙️ | 3 ✅ · 2 🔧 | 4 ✅ · 1 ⚙️ |
| R5. POS & Retail | 17 | 5 ✅ · 6 ⚙️ · 6 🔧 | 8 ✅ · 7 ⚙️ · 2 🔧 | 12 ✅ · 4 ⚙️ · 1 🔧 | 13 ✅ · 4 ⚙️ | 0 ✅ · 0 ⚙️ · 17 🔧 | 9 ✅ · 6 ⚙️ · 2 🔧 |
| R6. Ecommerce | 9 | 6 ✅ · 2 ⚙️ · 1 🔧 | 7 ✅ · 2 ⚙️ | 8 ✅ · 1 ⚙️ | 8 ✅ · 1 ⚙️ | 4 ✅ · 4 ⚙️ · 1 🔧 | 7 ✅ · 2 ⚙️ |
| R7. Supply Chain Planning | 3 | 3 ✅ | 3 ✅ | 2 ✅ · 1 ⚙️ | 3 ✅ | 2 ✅ · 1 ⚙️ | 3 ✅ |
| R8. HR & Payroll | 11 | 6 ✅ · 4 ⚙️ · 1 🔧 | 7 ✅ · 3 ⚙️ · 1 🔧 | 3 ✅ · 4 ⚙️ · 4 🔧 | 5 ✅ · 4 ⚙️ · 2 🔧 | 6 ✅ · 4 ⚙️ · 1 🔧 | 7 ✅ · 3 ⚙️ · 1 🔧 |
| R9. CRM & Loyalty | 5 | 4 ✅ · 1 ⚙️ | 5 ✅ | 4 ✅ · 1 ⚙️ | 5 ✅ | 3 ✅ · 2 ⚙️ | 4 ✅ · 1 ⚙️ |
| R10. Analytics | 5 | 4 ✅ · 1 🔧 | 5 ✅ | 4 ✅ · 1 🔧 | 5 ✅ | 3 ✅ · 2 🔧 | 4 ✅ · 1 🔧 |
| R11. Intercompany | 5 | 5 ✅ | 5 ✅ | 5 ✅ | 5 ✅ | 5 ✅ | 5 ✅ |
| R12. Document Mgmt | 5 | 3 ✅ · 2 ⚙️ | 4 ✅ · 1 ⚙️ | 3 ✅ · 2 ⚙️ | 3 ✅ · 2 ⚙️ | 3 ✅ · 2 ⚙️ | 3 ✅ · 2 ⚙️ |
| R13. Master Data | 5 | 5 ✅ | 5 ✅ | 4 ✅ · 1 ⚙️ | 4 ✅ · 1 ⚙️ | 3 ✅ · 2 ⚙️ | 4 ✅ · 1 ⚙️ |
| R14. Non-Functional | 14 | 8 ✅ · 4 ⚙️ · 2 🔧 | 9 ✅ · 4 ⚙️ · 1 🔧 | 9 ✅ · 4 ⚙️ · 1 🔧 | 10 ✅ · 3 ⚙️ · 1 🔧 | 7 ✅ · 5 ⚙️ · 2 🔧 | 9 ✅ · 4 ⚙️ · 1 🔧 |
| **Total Must Have Met (✅ + ⚙️)** | ~130 | **~99** | **~109** | **~93** | **~106** | **~84** | **~103** |
| **Remaining 🔧 Gaps** | | ~16 | ~8 | ~19 | ~7 | ~21 | ~10 |

### Key Insight

| Metric | SAP | Microsoft | Oracle |
|---|---|---|---|
| **Core ERP only — Must Have gaps (🔧+❌)** | ~16 | ~19 | ~21 |
| **Full stack — Must Have gaps (🔧+❌)** | ~8 | ~7 | ~10 |
| **Gaps resolved by full stack** | **+8 resolved** | **+12 resolved** | **+11 resolved** |
| **Remaining Must Have gaps** | 8 (mostly PH-localization) | 7 (mostly PH-payroll) | 10 (POS integration + PH-localization) |

> **The full vendor stack closes 8–12 gaps per vendor.** The remaining gaps are overwhelmingly
> **Philippine-specific regulatory requirements** (BIR forms, eFPS, PH payroll statutory, LGU permits,
> BIR CAS registration) that no global vendor handles natively — all need a Philippines-local
> implementation partner or ISV.

---

## 4. Remaining Gaps After Full Stack

These requirements remain 🔧 even with the complete vendor stack. They are the **true implementation risks**.

| Req ID | Requirement | Priority | Why All 3 Still Gap | Mitigation |
|---|---|---|---|---|
| FIN-008 | BIR Tax Return Generation | Must | No global ERP has native BIR 2550M/1601-E/1702 form generation | PH localization partner builds form templates; SAP BTP / Power Automate / OIC for eFPS submission |
| FIN-031 | BIR eFPS Filing | Must | eFPS is a PH government portal; no ERP has direct API | PH ISV/partner builds integration adapter; RPA-based submission via Power Automate/CPI/OIC |
| FIN-032 | E-Wallet Settlement | Must | GCash/Maya settlement file formats are PH-specific | Custom integration adapter on BTP/Azure Logic Apps/OIC |
| FIN-024 | Employee Gratuity (RA 7641) | Must | PH-specific retirement law; no global payroll handles natively | Configure in payroll rules (SuccessFactors/ISV/Oracle HCM) with PH legal counsel validation |
| POS-014a | Senior/PWD Discount (PH) | Must | RA 9994/10754 is PH-specific; no POS has this out-of-box | Custom pricing rule in POS (CCO/D365 Commerce/Xstore) with PH legal validation |
| POS-012 | BIR Receipt Format | Must | BIR registered sales invoice format is PH-specific | Custom receipt template in each POS with BIR compliance review |
| POS-017 | Paint Mixing / Custom SKU | Must | Retail-specific custom SKU generation; no ERP handles natively | Extension in POS (CCO/D365/Xstore) with base paint + colorant BOM |
| NFR-022a | BIR CAS Registration | Must | PH-specific regulatory tracking per location | Custom app (BTP/Power Apps/VBCS) for CAS registration status per store |

**Total remaining gaps: 8 Must Have requirements** — all are **Philippine regulatory/compliance** requirements. These are not product deficiencies; they are localization gaps that require a **Philippines-based implementation partner** regardless of which vendor is chosen.

---

## 5. Integration Architecture — Full Stack

### 5.1 SAP Stack Integration Map

```
┌─────────────────────────────────────────────────────────────┐
│                    SAP BTP (Integration Suite)                │
│           CPI / API Management / Event Mesh                  │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│          │          │          │          │                  │
│  ┌───────▼──┐  ┌────▼───┐  ┌──▼────┐  ┌──▼──────┐  ┌─────▼─────┐
│  │SAP CCO   │  │SAP CCv2│  │SAP    │  │Success- │  │SAP Ariba  │
│  │(1,000    │  │(Ecom)  │  │EWM    │  │Factors  │  │(Vendors)  │
│  │POS)      │  │        │  │(5 DCs)│  │(HR/Pay) │  │           │
│  └──────┬───┘  └───┬────┘  └──┬────┘  └──┬──────┘  └─────┬─────┘
│         │          │          │          │               │
│    ┌────▼──────────▼──────────▼──────────▼───────────────▼────┐
│    │              SAP S/4HANA Cloud                           │
│    │    GL · AP · AR · MM · SD · CO · PP · Treasury           │
│    └─────────────────────────────────────────────────────────┘
│                          │
│    ┌─────────────────────▼───────────────────────────────────┐
│    │  SAP Analytics Cloud · SAP CAR · SAP MDG · SAP ILM     │
│    └─────────────────────────────────────────────────────────┘
│
│    Integration Points:
│    • POS → S/4: CCO → CPI → S/4 (real-time sales + inventory)
│    • Ecom → S/4: CCv2 → CPI → S/4 (orders + inventory + price)
│    • WMS → S/4: EWM embedded (same system)
│    • HR → S/4: SuccessFactors → CPI → S/4 (payroll postings)
│    • Vendors → S/4: Ariba → CPI → S/4 (POs + invoices)
│    • Banks → S/4: Multi-Bank Connectivity
│    • PH ISV → S/4: BTP custom extensions (BIR, eFPS)
└─────────────────────────────────────────────────────────────┘
```

**Integration count: ~8 major integration flows.** SAP BTP CPI serves as the middleware hub.
SAP has the most integrated stack (EWM is embedded in S/4HANA; SuccessFactors has growing S/4 integration).

### 5.2 Microsoft Stack Integration Map

```
┌─────────────────────────────────────────────────────────────┐
│               Azure (API Mgmt + Logic Apps + Service Bus)    │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│          │          │          │          │                  │
│  ┌───────▼────┐ ┌───▼────┐ ┌──▼─────┐ ┌─▼────────┐ ┌──────▼─────┐
│  │D365 Commerce│ │D365 SCM│ │D365    │ │D365 HR + │ │Power       │
│  │POS + Ecom  │ │WMS     │ │Finance │ │ISV Payroll│ │Platform    │
│  │(1,000 POS) │ │(5 DCs) │ │        │ │          │ │(gap-fill)  │
│  └──────┬─────┘ └───┬────┘ └──┬─────┘ └──┬───────┘ └──────┬─────┘
│         │           │         │           │                │
│    ┌────▼───────────▼─────────▼───────────▼────────────────▼────┐
│    │         Dataverse (Common Data Platform)                   │
│    └───────────────────────────────────────────────────────────┘
│                          │
│    ┌─────────────────────▼────────────────────────────────────┐
│    │  Power BI · Azure Synapse · Azure AD · M365 / SharePoint │
│    └──────────────────────────────────────────────────────────┘
│
│    Integration Points:
│    • POS ↔ D365: Commerce POS ↔ Commerce HQ via CSU (native real-time)
│    • Ecom ↔ D365: Commerce e-commerce ↔ native (same platform)
│    • WMS ↔ D365: SCM WMS native (same app)
│    • HR ↔ D365 Finance: ISV payroll → Dataverse → D365 Finance (GL posting)
│    • Vendors: D365 vendor collaboration (native)
│    • Banks: Azure Logic Apps → bank file import
│    • PH ISV: Power Apps / Power Automate (BIR, eFPS)
└─────────────────────────────────────────────────────────────┘
```

**Integration count: ~4 major flows (tightest integration).** D365 Commerce, SCM, and Finance
share the Dataverse. POS ↔ Commerce is native. WMS is in SCM (native). **Microsoft has the fewest
integration points to manage**, which reduces implementation risk and ongoing maintenance.

### 5.3 Oracle Stack Integration Map

```
┌─────────────────────────────────────────────────────────────┐
│            Oracle Integration Cloud (OIC)                     │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│          │          │          │          │                  │
│  ┌───────▼──────┐┌──▼─────┐┌──▼──────┐┌──▼───────┐┌───────▼──────┐
│  │Oracle Retail ││Oracle  ││Oracle   ││Oracle    ││Oracle Retail │
│  │Xstore        ││WMS     ││Fusion   ││HCM Cloud ││Merchandising │
│  │(1,000 POS)   ││Cloud   ││ERP + SCM││(HR/Pay)  ││(RMS/RPM)     │
│  └──────┬───────┘└──┬─────┘└──┬──────┘└──┬───────┘└───────┬──────┘
│         │           │         │           │                │
│    ┌────▼───────────▼─────────▼───────────▼────────────────▼────┐
│    │              Oracle Autonomous Data Warehouse               │
│    └───────────────────────────────────────────────────────────┘
│                          │
│    ┌─────────────────────▼────────────────────────────────────┐
│    │  Oracle Analytics Cloud · EPM Cloud · CX Unity           │
│    └──────────────────────────────────────────────────────────┘
│
│    Integration Points:
│    • POS → Fusion: Xstore → OIC → Fusion SCM (sales + inventory)
│    • Ecom → Fusion: Commerce Cloud → OIC → Fusion Order Mgmt
│    • WMS → Fusion: WMS Cloud → OIC → Fusion SCM (inventory sync)
│    • Retail Mgmt → Fusion: RMS/RPM → OIC → Fusion (pricing, merch)
│    • HR → Fusion: HCM Cloud → native → Fusion ERP (payroll posting)
│    • Vendors: Oracle Supplier Portal → Fusion Procurement
│    • Banks: OIC bank file adapters
│    • PH ISV: VBCS custom extensions (BIR, eFPS)
└─────────────────────────────────────────────────────────────┘
```

**Integration count: ~10+ major integration flows.** Oracle has the most complex integration
landscape because Retail Xstore, WMS Cloud, RMS, RPM, Commerce Cloud, and Fusion ERP/SCM are
all **separate cloud services**. Each requires OIC orchestration. **This is Oracle's biggest
implementation risk** — more moving parts, more latency tuning, more failure points.

---

## 6. Vendor Stack Risk Comparison

| Risk Factor | SAP Full Stack | Microsoft Full Stack | Oracle Full Stack |
|---|---|---|---|
| **POS proven at 1K terminals** | ⚠️ CCO needs scale validation | ✅ D365 Commerce proven | ⚠️ Xstore proven standalone but **Fusion integration unproven at this scale** |
| **POS offline (8+ hours)** | ⚠️ CCO offline needs load testing | ✅ CSU offline proven | ⚠️ Xstore offline proven standalone but **sync-to-Fusion on reconnect needs testing** |
| **PH payroll** | ⚠️ SuccessFactors PH growing | ⚠️ ISV dependency — **highest risk** | ⚠️ Oracle HCM PH localization needs validation |
| **BIR/eFPS compliance** | ⚠️ PH partner needed | ⚠️ PH ISV needed | ⚠️ PH partner needed |
| **Integration complexity** | Medium (8 flows, EWM embedded) | **Low (4 flows, Dataverse native)** | **High (10+ flows, all separate clouds)** |
| **Retail POS ↔ ERP real-time sync** | ⚠️ CCO → CPI → S/4 (2 hops) | ✅ POS ↔ Commerce HQ via CSU (1 hop, native) | ⚠️ Xstore → OIC → Fusion (2 hops) |
| **Single vendor accountability** | ✅ All SAP (except PH ISV) | ✅ All Microsoft (except PH payroll ISV) | ⚠️ Oracle Retail + Oracle Fusion are **different product lines** with different roadmaps |
| **Implementation timeline** | 18–24 months | 12–18 months | 18–24 months |
| **5-year TCO** | $$$ (highest) | $$ (medium) | $$ (medium-high) |

---

## 7. Final Verdict — Full Stack

| | SAP Full Stack | Microsoft Full Stack | Oracle Full Stack |
|---|---|---|---|
| **Must Have coverage** | ~109/130 (84%) | ~106/130 (82%) | ~103/130 (79%) |
| **Remaining Must Have gaps** | 8 (all PH-regulatory) | 7 (PH-payroll + PH-regulatory) | 10 (POS integration + PH-regulatory) |
| **Integration simplicity** | ★★★☆☆ | ★★★★★ | ★★☆☆☆ |
| **POS maturity for big-box** | ★★★☆☆ | ★★★★★ | ★★★★☆ (with Xstore) |
| **Supply chain depth** | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| **HR/Payroll completeness** | ★★★★☆ | ★★☆☆☆ (ISV) | ★★★★☆ |
| **PH localization readiness** | ★★★☆☆ | ★★★☆☆ | ★★☆☆☆ |
| **Time-to-value** | ★★★☆☆ | ★★★★☆ | ★★★☆☆ |
| **Best fit for BuildRight** | **Strong for supply chain & finance** | **Best for unified retail** | **Viable with Oracle Retail suite** |

### Recommendation

| Vendor | Verdict | Rationale |
|---|---|---|
| **Microsoft D365 Full Stack** | **🟢 RECOMMENDED** | Best POS + Commerce + ERP integration; fewest integration points; Power Platform fills remaining gaps; fastest implementation. **Risk**: PH payroll requires ISV. |
| **SAP Full Stack** | **🟡 CONDITIONAL** | Strongest supply chain (IBP) and financials (Group Reporting). **Risk**: POS (CCO) needs proven 1K-terminal reference; highest TCO. Recommend if supply chain complexity is prioritized over retail POS. |
| **Oracle Full Stack** | **🟡 CONDITIONAL** | Strong enterprise suite + Oracle Retail Xstore fills the POS gap. **Risk**: Integration complexity (10+ flows between separate clouds); Oracle Retail and Fusion ERP are different product lines. Recommend only if Oracle demonstrates proven Xstore+Fusion integration at scale. |

### Next Steps

1. **Request reference visits** for:
   - Microsoft: D365 Commerce at 1,000+ POS terminals (e.g., Walmart, Beauchamp)
   - SAP: Customer Checkout at scale (ask for 500+ terminal references)
   - Oracle: Xstore + Fusion Cloud SCM integration (ask for reference with real-time inventory sync)
2. **Engage PH implementation partners** for each vendor:
   - SAP: Accenture PH, DXC, Deloitte PH
   - Microsoft: Hitachi Solutions, Avanade, RSM PH
   - Oracle: Oracle PH consulting, Wipro/Infosys PH teams
3. **Validate PH payroll options**:
   - SAP: SuccessFactors PH payroll completeness
   - Microsoft: ISV partner demo (Itsubmit / SL Global)
   - Oracle: Oracle HCM PH payroll localization demo
4. **Run POS offline proof-of-concept** for all three vendors
5. **Complete scorecards** using [Scoring Methodology](../07-methodology/scoring-methodology.md)

---

*Document Version: 1.0 | Date: 2026-06-03 | Full-stack evaluation of SAP, Microsoft, and Oracle vendor portfolios against 261 BuildRight Depot requirements*
