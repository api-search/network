---
aid: stripe:stripe-postchargeschargecapture
name: Stripe Post   Charges Charge Capture
tags:
- Charges
humanURL: 
properties: []
description: >-
  <p>Capture the payment of an existing, uncaptured charge that was created with the <code>capture</code> option set to false.</p>  <p>Uncaptured payments expire a set number of days after they are created (<a href="/docs/charges/placing-a-hold">7 by default</a>), after which they are marked as refunded and capture attempts will fail.</p>  <p>Don’t use this method to capture a PaymentIntent-initiated charge. Use <a href="/docs/api/payment_intents/capture">Capture a PaymentIntent</a>.</p>

---
