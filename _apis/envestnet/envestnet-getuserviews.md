---
aid: envestnet:envestnet-getuserviews
name: Fetch the details of all the views associated with a user.
tags:
- View
humanURL: 
properties: []
description: >-
  The GET Views API retrieves details of all the Views that the user has created. To retrieve the rules associated with the Views, pass "include=rules" in the request. Views currently support only aggregated transactions.<br><br> A View is a logical collection of several rules. Processing these rules returns the relevant transactions associated with the rules. This API will not return deleted Views. To fetch the Transactions for a View, call the GET /views/{viewId}/transactions API.

---
