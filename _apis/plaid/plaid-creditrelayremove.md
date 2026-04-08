---
aid: plaid:plaid-creditrelayremove
name: Plaid Remove relay token
tags:
- Plaid
humanURL: 
properties: []
description: >-
  The `/credit/relay/remove` endpoint allows you to invalidate a `relay_token`. The third party holding the token will no longer be able to access or refresh the reports which the `relay_token` gives access to. The original report, associated Items, and other relay tokens that provide access to the same report are not affected and will remain accessible after removing the given `relay_token`.

---
