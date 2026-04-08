---
aid: plaid:plaid-assetreportget
name: Plaid Retrieve an Asset Report
tags:
- Plaid
humanURL: 
properties: []
description: >-
  The `/asset_report/get` endpoint retrieves the Asset Report in JSON format. Before calling `/asset_report/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.  By default, an Asset Report includes transaction descriptions as returned by the bank, as ...

---
