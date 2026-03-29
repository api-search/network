---
aid: cloudevents:cloudevents-deletesubscription
name: Delete a subscription
tags:
- Subscriptions
humanURL: 
properties: []
description: >-
  Deletes an existing subscription. Once deleted, the broker stops delivering events to the subscription's sink. In-flight events at the time of deletion may or may not be delivered depending on broker implementation. Returns 404 if the subscription does not exist.

---
