---
description: UpdateCompanyApiCredentialRequest schema from Adyen API
layout: schema
name: UpdateCompanyApiCredentialRequest
properties_list:
- description: Indicates if the API credential is enabled.
  name: active
  type: boolean
- description: The new list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the API credential.
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
schema_file: json-schema/management-update-company-api-credential-request-schema.json
slug: management-update-company-api-credential-request
tags:
- Payments
- Financial Services
- Fintech
title: UpdateCompanyApiCredentialRequest
---
