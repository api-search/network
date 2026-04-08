---
aid: stripe:stripe-postsubscriptionssubscriptionresume
name: Post Subscriptions Subscription Resume
tags:
- Subscriptions
humanURL: 
properties: []
description: >-
  <p>Initiates resumption of a paused subscription, optionally resetting the billing cycle anchor and creating prorations. If a resumption invoice is generated, it must be paid or marked uncollectible before the subscription will be unpaused. If payment succeeds the subscription will become <code>active</code>, and if payment fails the subscription will be <code>past_due</code>. The resumption invoice will void automatically if not paid by the expiration date.</p>

---
