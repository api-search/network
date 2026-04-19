---
description: OAuth 2.0 token request using client credentials
layout: schema
name: OAuthTokenRequest
properties_list:
- description: OAuth grant type
  name: grant_type
  type: string
- description: OAuth client ID
  name: client_id
  type: string
- description: OAuth client secret
  name: client_secret
  type: string
provider_name: Abacus
provider_slug: abacus
schema_file: json-schema/abacus-oauth-token-request-schema.json
slug: abacus-oauth-token-request
tags:
- Accounting
- Expense Management
- Finance
- Reimbursement
title: OAuthTokenRequest
---
