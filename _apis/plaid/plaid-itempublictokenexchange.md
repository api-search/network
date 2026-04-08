---
aid: plaid:plaid-itempublictokenexchange
name: Plaid Exchange public token for an access token
tags:
- Plaid
humanURL: 
properties: []
description: >-
  Exchange a Link `public_token` for an API `access_token`. Link hands off the `public_token` client-side via the `onSuccess` callback once a user has successfully created an Item. The `public_token` is ephemeral and expires after 30 minutes. An `access_token` does not expire, but can be revoked by calling `/item/remove`.  The response also includes an `item_id` that should be stored with the `access_token`. The `item_id` is used to identify an Item in a webhook. The `item_id` can also be retri...

---
