---
description: OAuth 2.0 access token response
layout: schema
name: OAuthTokenResponse
properties_list:
- description: Access token for API requests
  name: access_token
  type: string
- description: Token type (always Bearer)
  name: token_type
  type: string
- description: Token expiration time in seconds
  name: expires_in
  type: integer
provider_name: Abacus
provider_slug: abacus
schema_file: json-schema/abacus-oauth-token-response-schema.json
slug: abacus-oauth-token-response
tags:
- Accounting
- Expense Management
- Finance
- Reimbursement
title: OAuthTokenResponse
---
