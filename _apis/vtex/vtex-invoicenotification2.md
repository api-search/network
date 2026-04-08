---
aid: vtex:vtex-invoicenotification2
name: VTex Order invoice notification
tags:
- Invoice
humanURL: 
properties: []
description: >-
  Once the order is invoiced, the seller should use this request to send the invoice information to the marketplace.  We strongly recommend that you always send the object of the invoiced items. With this practice, rounding errors will be avoided.  It is not allowed to use the same `invoiceNumber` in more than one request to the Order Invoice Notification endpoint.  Be aware that this endpoint is also used by the seller to send the order tracking information. This, however, should be done in a ...

---
