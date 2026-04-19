---
description: CreateMerchantApiCredentialRequest schema from Adyen API
layout: schema
name: CreateMerchantApiCredentialRequest
properties_list:
- description: The list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the new API credential.
  name: allowedOrigins
  type: array
- description: Description of the API credential.
  name: description
  type: string
- description: List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. Only roles assigned to 'ws@Company.<CompanyName>' can be assigned to other API credentials
  name: roles
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-create-merchant-api-credential-request-schema.json
slug: management-create-merchant-api-credential-request
tags:
- Payments
- Financial Services
- Fintech
title: CreateMerchantApiCredentialRequest
---
