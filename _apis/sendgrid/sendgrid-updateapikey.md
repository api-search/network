---
aid: sendgrid:sendgrid-updateapikey
name: Update API key name and scopes
tags:
- API Keys
humanURL: 
properties: []
description: >-
  **This endpoint allows you to update the name and scopes of a given API key.**  You must pass this endpoint a JSON request body with a `name` field and a `scopes` array containing at least one scope. The `name` and `scopes` fields will be used to update the key associated with the `api_key_id` in the request URL.  If you need to update a key's scopes only, pass the `name` field with the key's existing name; the `name` will not be modified. If you need to update a key's name only, use the "Upd...

---
