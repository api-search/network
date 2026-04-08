---
aid: plaid:plaid-creditrelaypdfget
name: Plaid Retrieve the pdf reports associated with a relay token that was shared with you (beta)
tags:
- Plaid
humanURL: 
properties: []
description: >-
  `/credit/relay/pdf/get` allows third parties to receive a pdf report that was shared with them, using a `relay_token` that was created by the report owner.  The `/credit/relay/pdf/get` endpoint retrieves the Asset Report in PDF format. Before calling `/credit/relay/pdf/get`, you must first create the Asset Report using `/credit/relay/create` and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready t...

---
