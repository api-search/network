---
aid: plaid:plaid-assetreportcreate
name: Plaid Create an Asset Report
tags:
- Plaid
humanURL: 
properties: []
description: >-
  The `/asset_report/create` endpoint initiates the process of creating an Asset Report, which can then be retrieved by passing the `asset_report_token` return value to the `/asset_report/get` or `/asset_report/pdf/get` endpoints.  The Asset Report takes some time to be created and is not available immediately after calling `/asset_report/create`. The exact amount of time to create the report will vary depending on how many days of history are requested and will typically range from a few secon...

---
