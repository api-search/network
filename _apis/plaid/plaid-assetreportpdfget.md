---
aid: plaid:plaid-assetreportpdfget
name: Plaid Retrieve a PDF Asset Report
tags:
- Plaid
humanURL: 
properties: []
description: >-
  The `/asset_report/pdf/get` endpoint retrieves the Asset Report in PDF format. Before calling `/asset_report/pdf/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.  The response to `/asset_report/pdf/get` is the PDF binary data. The `request_id`  i...

---
