---
aid: plaid:plaid-transfermigrateaccount
name: Plaid Migrate account into Transfers
tags:
- Plaid
humanURL: 
properties: []
description: >-
  As an alternative to adding Items via Link, you can also use the `/transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items. If you intend to create wire transfers on this account, you must provide `wire_routing_number`. Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Transfer endpoints.  If you require access to other endpoints, create the Item through Li...

---
