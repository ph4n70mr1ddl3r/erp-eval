# ERP Evaluation — Scoring Methodology

> This document defines the objective scoring model used to compare ERP platforms
> against the BuildRight Depot requirements defined in [ERP Requirements](../01-model-company/erp-requirements.md).

---

## 1. Requirement Weighting

Each requirement has a priority classification that maps to a weight:

| Priority | Weight | Multiplier |
|---|---|---|
| **Must Have** | 10 | Requirements with no workaround; disqualifying if not met |
| **Should Have** | 5 | Important but a partial workaround exists |
| **Nice to Have** | 2 | Beneficial but not critical |

### Category Weights

In addition to per-requirement priority weights, each requirement category has a **business criticality multiplier** reflecting its relative importance to BuildRight Depot:

| Category | Req Prefix | Business Criticality Multiplier | Rationale |
|---|---|---|---|
| Financial Management | FIN | 1.2 | Core ERP; multi-entity consolidation is critical |
| Inventory Management | INV | 1.3 | Retail operations depend on real-time inventory |
| Procurement & Purchasing | PUR | 1.0 | Important but relatively standard processes |
| Warehouse Management | WMS | 1.1 | DC operations drive supply chain efficiency |
| POS & Retail | POS | 1.5 | Highest transaction volume; revenue-critical |
| Ecommerce Integration | ECOM | 1.1 | Growing channel; integration quality matters |
| Supply Chain Planning | SCP | 1.0 | Important for optimization but less urgent |
| HR & Payroll | HR | 1.0 | Must comply; relatively standard |
| CRM & Loyalty | CRM | 0.9 | Important for retention but secondary to core ops |
| Analytics & Reporting | RPT | 1.0 | Standard reporting needs |
| Intercompany | IC | 1.2 | 5-entity structure makes this critical |
| Document Management | DOC | 0.9 | BIR compliance requires this |
| Master Data Management | MDM | 1.0 | Foundational for data quality |
| Non-Functional Requirements | NFR | 1.3 | Performance, uptime, scalability are deal-breakers |
| Installation & Value-Added Services | SRV | 0.9 | Differentiation opportunity but secondary to core retail |
| Wholesale & Reseller Operations | WSL | 0.9 | Growing channel; similar processes to retail |
| Merchandising Execution | MER | 1.0 | Promotional and seasonal execution drives revenue |
| Corporate Governance, Legal & Strategy | GOV | 0.8 | Operational governance; important for compliance but not revenue-critical |

### Scoring Formula

For each requirement **r** in category **c**:

```
Score_r = Fit_Score_r × Priority_Weight_r × Category_Multiplier_c
```

**Total Score** = Σ Score_r for all requirements

---

## 2. Fit Score

Each requirement is scored on a 0–4 fit scale:

| Fit Score | Label | Definition |
|---|---|---|
| **4** | Native Fit | Feature is available out-of-the-box with no customization |
| **3** | Configured Fit | Feature is achievable through configuration/admin setup (no code) |
| **2** | Customization Required | Feature requires custom development, scripting, or third-party add-on |
| **1** | Partial / Workaround | Only partially addressed; requires significant workaround or process change |
| **0** | Not Available | Feature is not available and no viable workaround exists |

### Scoring Rules

- A **Must Have** requirement scored **0** is a **disqualifier** — the ERP cannot proceed unless a viable partner/integration resolves it.
- A **Must Have** requirement scored **1** is a **major risk** — it can proceed but must be flagged and a mitigation plan documented.
- The maximum possible raw score is: (count of requirements) × 4 × (their weights) × (category multipliers). Scores will be normalized to a percentage for comparison.

---

## 3. Evaluation Dimensions

In addition to functional fit, each ERP will be scored on these dimensions:

| Dimension | Weight | Description |
|---|---|---|
| **Functional Fit** | 40% | Weighted score from requirement fit/gap analysis (above) |
| **Total Cost of Ownership (5-year)** | 20% | Licensing + implementation + ongoing support + infrastructure |
| **Implementation Risk** | 15% | Complexity, timeline, partner ecosystem, track record in Philippines retail |
| **Scalability & Performance** | 15% | Ability to handle 2.8M POS txns/month, 1,000 terminals, 300+ store growth |
| **Local Support Ecosystem** | 10% | Philippine partner availability, local support team, language |

### Overall Score

```
Overall = (Functional Fit × 0.40) + (TCO × 0.20) + (Impl Risk × 0.15)
        + (Scalability × 0.15) + (Local Support × 0.10)
```

Each dimension (except Functional Fit) is scored 1–5 by the evaluation team, then weighted.

---

## 4. Scoring Template

Each ERP subfolder should include a `*-scorecard.md` file using this template:

```markdown
# [ERP Name] — Evaluation Scorecard

## Dimension Scores

| Dimension | Score (1–5) | Weight | Weighted Score | Notes |
|---|---|---|---|---|
| Functional Fit | — | 40% | — | See fit-gap analysis |
| TCO (5-year) | — | 20% | — | See cost estimate |
| Implementation Risk | — | 15% | — | |
| Scalability & Performance | — | 15% | — | |
| Local Support Ecosystem | — | 10% | — | |
| **Overall** | | **100%** | **—** | |

## Disqualifiers / Red Flags
- [List any Must Have requirements scored 0 or 1]

## Top Strengths
1.
2.
3.

## Top Gaps / Risks
1.
2.
3.

## Recommendation
[Proceed / Conditional / Eliminate] — with rationale
```

---

## 5. Evaluation Process

| Phase | Activity | Output |
|---|---|---|
| **Phase 1** | Document research per ERP | `*-fit-gap.md`, `*-localization.md` |
| **Phase 2** | Vendor demos (scripted scenarios from model company) | Demo score sheets |
| **Phase 3** | Architecture design per ERP | `*-architecture.md` |
| **Phase 4** | Cost estimation | `*-cost-estimate.md` |
| **Phase 5** | Scorecard completion | `*-scorecard.md` |
| **Phase 6** | Shortlist selection (top 2) | Shortlist report |
| **Phase 7** | Deep-dive / POC with shortlisted vendors | POC results |
| **Phase 8** | Final selection | Decision document |

---

*Document Version: 1.1 | Date: 2026-06-02 | Added GOV, SRV, WSL, MER category weights to align with 18-category requirement structure*
