---
aid: stripe:stripe-postsubscriptionschedulesschedulerelease
name: Post Subscription Schedules Schedule Release
tags:
- Subscription Schedules
humanURL: 
properties: []
description: >-
  <p>Releases the subscription schedule immediately, which will stop scheduling of its phases, but leave any existing subscription in place. A schedule can only be released if its status is <code>not_started</code> or <code>active</code>. If the subscription schedule is currently associated with a subscription, releasing it will remove its <code>subscription</code> property and set the subscription’s ID to the <code>released_subscription</code> property.</p>

---
