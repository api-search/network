---
aid: paypal:paypal-subscriptionspatch
name: Paypal Update subscription
tags:
- Subscriptions
humanURL: 
properties: []
description: >-
  Updates a subscription which could be in <code>ACTIVE</code> or <code>SUSPENDED</code> status. You can override plan level default attributes by providing customised values for plan path in the patch request.<br /> <ul> <li>You cannot update attributes that have already completed (Example - trial cycles can’t be updated if completed).</li> <li>Once overridden, changes to plan resource will not impact subscription.</li> <li>Any price update will not impact billing cycles within next 10 days (A...

---
