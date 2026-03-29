---
aid: envestnet:envestnet-getusersubscriptions
name: Provides user-level preferences for each insight.
tags:
- User
humanURL: 
properties: []
description: >-
  This API returns the details of all the Insights which are subscribed by the customer. If any of the insight has been turned off by setting isSubscribed = false at the customerSubscription level, those insights will not be shown in the userSubscription API.<br /><br />Each Insight details contain attributes such as Insight Frequency, Threshold, etc. By default, all the configurations set by the customer will be inherited by the user. Using a separate PATCH API, consumers can override customer...

---
