---
aid: plaid:plaid-incomeverificationdocumentsdownload
name: Plaid (Deprecated) Download the original documents used for income verification
tags:
- Plaid
humanURL: 
properties: []
description: >-
  `/income/verification/documents/download` provides the ability to download the source documents associated with the verification.  If Document Income was used, the documents will be those the user provided in Link. For Payroll Income, the most recent files available for download from the payroll provider will be available from this endpoint.  The response to `/income/verification/documents/download` is a ZIP file in binary data. If a `document_id` is passed, a single document will be containe...

---
