---
description: CreateCompanyApiCredentialRequest schema from Adyen API
layout: schema
name: CreateCompanyApiCredentialRequest
properties_list:
- description: List of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the new API credential.
  name: allowedOrigins
  type: array
- description: List of merchant accounts that the API credential has access to.
  name: associatedMerchantAccounts
  type: array
- description: Description of the API credential.
  name: description
  type: string
- description: List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. Only roles assigned to 'ws@Company.<CompanyName>' can be assigned to other API credentials
  name: roles
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-create-company-api-credential-request-schema.json
slug: management-create-company-api-credential-request
tags:
- Payments
- Financial Services
- Fintech
title: CreateCompanyApiCredentialRequest
---
