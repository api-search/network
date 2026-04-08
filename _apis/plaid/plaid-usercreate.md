---
aid: plaid:plaid-usercreate
name: Plaid Create user
tags:
- Plaid
humanURL: 
properties: []
description: >-
  This endpoint should be called for each of your end users before they begin a Plaid income flow. This provides you a single token to access all income data associated with the user. You should only create one per end user.  If you call the endpoint multiple times with the same `client_user_id`, the first creation call will succeed and the rest will fail with an error message indicating that the user has been created for the given `client_user_id`.  Ensure that you store the `user_token` along...

---
