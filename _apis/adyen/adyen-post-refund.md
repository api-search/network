---
aid: adyen:adyen-post-refund
name: Refund a captured payment
tags:
- - - - Modifications
humanURL: 
properties: []
description: >-
  Refunds a payment that has previously been captured, returning a unique reference for this request. Refunding can be done on the full captured amount or a partial amount. Multiple (partial) refunds will be accepted as long as their sum doesn't exceed the captured amount. Payments which have been authorised, but not captured, cannot be refunded, use the /cancel method instead.  Some payment methods/gateways do not support partial/multiple refunds. A margin above the captured limit can be confi...

---
