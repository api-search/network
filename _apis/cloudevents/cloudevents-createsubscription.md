---
aid: cloudevents:cloudevents-createsubscription
name: Create a subscription
tags:
- Subscriptions
humanURL: 
properties: []
description: >-
  Creates a new subscription to an event stream. The request body specifies the sink (delivery endpoint), the source of events, optional event type filters, and protocol settings. Upon successful creation, the broker begins delivering matching events to the specified sink. The response returns the fully populated subscription object including its assigned identifier.

---
