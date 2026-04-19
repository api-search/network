---
description: UpdateStoreRequest schema from Adyen API
layout: schema
name: UpdateStoreRequest
properties_list:
- description: The address of the store. It is not possible to update the country of the store.
  name: address
  type: object
- description: The unique identifiers of the [business lines](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines__resParam_id) that the store is associated with.
  name: businessLineIds
  type: array
- description: The description of the store.
  name: description
  type: string
- description: The unique identifier of the store, used by certain payment methods and tax authorities. Accepts up to 14 digits. Required for CNPJ in Brazil, in the format 00.000.000/00git00-00 separated by dots, sl
  name: externalReferenceId
  type: string
- description: The phone number of the store, including '+' and country code in the [E.164](https://en.wikipedia.org/wiki/E.164) format. If passed in a different format, we convert and validate the phone number agai
  name: phoneNumber
  type: string
- description: Rules for Adyen for Platforms merchants to split the transaction amount and fees.
  name: splitConfiguration
  type: object
- description: 'The status of the store. Possible values are: - **active**: This value is assigned automatically when a store is created. - **inactive**: The maximum [transaction limits and number of Store-and-Forwar'
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-update-store-request-schema.json
slug: management-update-store-request
tags:
- Payments
- Financial Services
- Fintech
title: UpdateStoreRequest
---
