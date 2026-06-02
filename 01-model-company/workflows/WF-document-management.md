# Document Management (DOC) Workflows

> ERP-wide electronic document storage & retrieval, and enterprise document retention & archiving policy.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W255. Electronic Document Storage & Retrieval (ERP-wide)](#electronic-document-storage--retrieval-erp-wide)
- [W256. Enterprise Document Retention & Archiving Policy](#enterprise-document-retention--archiving-policy)

---

## W255. Electronic Document Storage & Retrieval (ERP-wide)

| Field | Detail |
|---|---|
| **Trigger** | A transaction is executed that requires supporting documentation (e.g., Goods Receipt, AP Invoice, Capex Request) |
| **Frequency** | Continuous (thousands of documents attached daily) |
| **Owner** | Respective Department Heads (Finance, Procurement, Logistics) |
| **Participants** | End Users, ERP Administrator |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Document Capture**: User receives a physical document (e.g., vendor delivery receipt) and scans it, or receives a digital PDF (e.g., supplier invoice via email) | End User | — | 2 min |
| 2 | **Transaction Attachment**: User drags-and-drops or uploads the document directly to the relevant ERP transaction screen (e.g., attaching the scanned DR to the ERP Goods Receipt record) | End User | — | 1 min |
| 3 | **Metadata Tagging**: System automatically inherits metadata from the transaction (Transaction ID, Vendor Name, Date, Amount, User ID) for searchability | System | — | Automated |
| 4 | **Storage & Linking**: The document is stored in the ERP's secure document repository (or linked cloud storage) and visually indicated with a paperclip/attachment icon on the transaction record | System | — | Automated |
| 5 | **Retrieval**: Approvers or Auditors click the attachment icon during workflow review or audit processes to view the source document without requesting physical copies | Approver / Auditor | — | < 30 sec |

**System Touchpoints**:
- ERP Document Management System (DMS) / Attachment framework
- Workflow approval screens (displaying attachments)

**Pain Points / Risks**:
- Users uploading massive uncompressed images, bloating database storage costs.
- Attaching documents to the wrong transaction, failing 3-way match audits.

---

## W256. Enterprise Document Retention & Archiving Policy

| Field | Detail |
|---|---|
| **Trigger** | End of fiscal year and periodic archiving schedules |
| **Frequency** | Annual batch process |
| **Owner** | Legal & Compliance Officer |
| **Participants** | Finance Controller, IT Database Administrator |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Policy Definition**: Legal Officer defines retention rules in the ERP DMS (e.g., Financial Invoices: 10 years per BIR regulation; HR records: 5 years post-separation) | Legal Officer | Legal Officer | 2–4 hours |
| 2 | **Automated Aging**: ERP DMS continuously monitors document creation dates against the retention policy matrix | System | — | Automated |
| 3 | **Archiving Run**: At fiscal year-end, IT DBA triggers the archiving utility. Documents exceeding the "active" threshold (e.g., 2 years) are compressed and moved to cold storage (cheaper storage tier), but remain accessible via slow-retrieval query | IT DBA | IT DBA | 4–8 hours |
| 4 | **Legal Hold**: For entities under active BIR audit or litigation, Legal Officer places a "Legal Hold" on the location/vendor, overriding automated deletion rules | Legal Officer | — | 30 min |
| 5 | **Purge/Destruction**: Documents reaching the absolute end of their legal retention period (e.g., 10 years + 1 day) are permanently purged from all tiers. IT generates a Certificate of Digital Destruction for compliance records | System | IT DBA | Automated |

**System Touchpoints**:
- ERP Data Archiving Utility
- Cloud Storage Tiers (Hot vs. Cold)
- BIR compliance reporting

**Pain Points / Risks**:
- Accidental purging of documents under audit due to missed Legal Hold flags.
- Inability to retrieve 8-year-old proprietary formats after software upgrades.
