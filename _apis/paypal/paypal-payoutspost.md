---
aid: paypal:paypal-payoutspost
name: Paypal Create batch payout
tags:
- Payouts
humanURL: 
properties: []
description: >-
  Creates a batch payout. In the JSON request body, pass a `sender_batch_header` and an `items` array. The `sender_batch_header` defines how to handle the payout. The `items` array defines the payout items.<br/>You can make payouts to one or more recipients.<blockquote><strong>Notes:</strong> <ul><li><p>PayPal does not process duplicate payouts. If you specify a <code>sender_batch_id</code> that was used in the last 30 days, the API rejects the request with an error message that shows the dupli...

---
