---
description: OAuth2 access token response.
layout: schema
name: AccessToken
properties_list:
- description: The bearer access token for authenticating API requests.
  name: access_token
  type: string
- description: The type of token issued. Always "Bearer".
  name: token_type
  type: string
- description: The number of seconds until the access token expires.
  name: expires_in
  type: integer
provider_name: Moody's
provider_slug: moodys
schema_file: json-schema/moodys-data-buffet-access-token-schema.json
slug: moodys-data-buffet-access-token
tags:
- Climate Risk
- Compliance
- Credit Risk
- Economic Data
- Entity Verification
- Financial Analytics
- Insurance
- KYC
- Risk
- Screening
title: AccessToken
---
