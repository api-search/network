---
description: ApiCredentialLinks schema from Adyen API
layout: schema
name: ApiCredentialLinks
properties_list:
- description: List of allowed origins.
  name: allowedOrigins
  type: object
- description: Company account that the API credential is linked to. Only present for company-level webhooks.
  name: company
  type: object
- description: Generates a new API key. When you generate a new one, the existing key remains valid for 24 hours.
  name: generateApiKey
  type: object
- description: Generates a new client key, used to authenticate client-side requests. When you generate a new one, the existing key remains valid for 24 hours.
  name: generateClientKey
  type: object
- description: The merchant account that the API credential is linked to. Only present for merchant-level API credentials.
  name: merchant
  type: object
- description: Link to the resource itself.
  name: self
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-api-credential-links-schema.json
slug: management-api-credential-links
tags:
- Payments
- Financial Services
- Fintech
title: ApiCredentialLinks
---
