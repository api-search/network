---
description: CreateCompanyApiCredentialResponse schema from Adyen API
layout: schema
name: CreateCompanyApiCredentialResponse
properties_list:
- description: References to resources linked to the API credential.
  name: _links
  type: object
- description: Indicates if the API credential is enabled. Must be set to **true** to use the credential in your integration.
  name: active
  type: boolean
- description: List of IP addresses from which your client can make requests. If the list is empty, we allow requests from any IP. If the list is not empty and we get a request from an IP which is not on the list, y
  name: allowedIpAddresses
  type: array
- description: List containing the [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) linked to the API credential.
  name: allowedOrigins
  type: array
- description: The API key for the API credential that was created.
  name: apiKey
  type: string
- description: List of merchant accounts that the API credential has access to.
  name: associatedMerchantAccounts
  type: array
- description: Public key used for [client-side authentication](https://docs.adyen.com/development-resources/client-side-authentication). The client key is required for Drop-in and Components integrations.
  name: clientKey
  type: string
- description: Description of the API credential.
  name: description
  type: string
- description: Unique identifier of the API credential.
  name: id
  type: string
- description: The password for the API credential that was created.
  name: password
  type: string
- description: List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential.
  name: roles
  type: array
- description: The name of the [API credential](https://docs.adyen.com/development-resources/api-credentials), for example **ws@Company.TestCompany**.
  name: username
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-create-company-api-credential-response-schema.json
slug: management-create-company-api-credential-response
tags:
- Payments
- Financial Services
- Fintech
title: CreateCompanyApiCredentialResponse
---
