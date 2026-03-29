---
aid: adyen:adyen-post-paymentmethods
name: Get a list of available payment methods
tags:
- - - - Payments
humanURL: 
properties: []
description: >-
  Queries the available payment methods for a transaction based on the transaction context (like amount, country, and currency). Besides giving back a list of the available payment methods, the response also returns which input details you need to collect from the shopper (to be submitted to `/payments`).  Although we highly recommend using this endpoint to ensure you are always offering the most up-to-date list of payment methods, its usage is optional. You can, for example, also cache the `/p...

---
