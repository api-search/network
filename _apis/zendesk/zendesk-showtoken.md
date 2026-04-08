---
aid: zendesk:zendesk-showtoken
name: Zendesk Get  Api V2 Oauth Tokens Oauth_token_id
tags:
- OAuth Tokens
humanURL: 
properties: []
description: >-
  Returns the properties of the specified token. For security reasons, only the first 10 characters of the access token are included.  In the first endpoint, `id` is a token id, not the full token.  In the second endpoint, include an `Authorization: Bearer` header with the full token to get its associated properties. Example:  ```sh curl https://{subdomain}.zendesk.com/api/v2/oauth/tokens/current.json \   -H 'Authorization: Bearer ${authToken}' \   -v -u {email_address}/token:{api_token} ```  #...

---
