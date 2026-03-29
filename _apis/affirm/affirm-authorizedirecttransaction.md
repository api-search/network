---
aid: affirm:affirm-authorizedirecttransaction
name: Authorize a transaction
tags:
- Authorization
humanURL: 
properties: []
description: >-
  Exchanges a checkout token for a transaction authorization, completing the server-side portion of the Direct API flow. This call must be made from the merchant server after the browser-side affirm.js returns a checkout token via the user_confirmation_url callback. The authorization places a hold on the customer's Affirm credit. The resulting transaction must be captured within the authorization window to transfer funds to the merchant.

---
