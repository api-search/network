---
aid: vtex:vtex-mkp-order-cancellation
name: VTex Marketplace order cancellation
tags:
- External Seller
humanURL: 
properties: []
description: >-
  This request may be sent from VTEX to the external seller in case of order cancelation. For that, the seller will need to implement the Marketplace order cancellation endpoint. Whenever this request is received by the seller, the order should be canceled and the fulfillment flow should not proceed.   For the seller to:   - **Evaluate a cancellation request:** it is possible to send an empty body as a response to the cancellation request, meaning that the seller is evaluating whether to procee...

---
