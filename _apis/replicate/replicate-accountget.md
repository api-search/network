---
aid: replicate:replicate-accountget
name: Replicate Get the authenticated account
tags:
- Accounts
humanURL: 
properties: []
description: >-
  Returns information about the user or organization associated with the provided API token.  Example cURL request:  ```console curl -s \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/account ```  The response will be a JSON object describing the account:  ```json {   "type": "organization",   "username": "acme",   "name": "Acme Corp, Inc.",   "github_url": "https://github.com/acme", } ```

---
