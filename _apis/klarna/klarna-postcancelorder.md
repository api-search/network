---
aid: klarna:klarna-postcancelorder
name: Request order cancellation
tags:
- API
humanURL: 
properties: []
description: >-
  Request cancellation for an order. If the order is already cancelled, a `200` status is returned.  Otherwise, the order will be queued for cancellation with a `202` status. Actual order cancellation will happen asynchronously at a later time. You can call the corresponding GET endpoint to view the status of the request.  This cancellation endpoint is limited to the scope of the Virtual Credit Cards product. Therefore the order provided must have an associated Virtual Card Settlement, otherwis...

---
