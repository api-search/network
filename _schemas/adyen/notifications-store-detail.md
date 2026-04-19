---
description: StoreDetail schema from Adyen API
layout: schema
name: StoreDetail
properties_list:
- description: The address of the physical store where the account holder will process payments from.
  name: address
  type: object
- description: 'The phone number of the store provided as a single string. It will be handled as a landline phone. Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"'
  name: fullPhoneNumber
  type: string
- description: Store logo for payment method setup.
  name: logo
  type: string
- description: The merchant account to which the store belongs.
  name: merchantAccount
  type: string
- description: The merchant category code (MCC) that classifies the business of the account holder.
  name: merchantCategoryCode
  type: string
- description: Merchant house number for payment method setup.
  name: merchantHouseNumber
  type: string
- description: The phone number of the store.
  name: phoneNumber
  type: object
- description: 'The sales channel. Possible values: **Ecommerce**, **POS**.'
  name: shopperInteraction
  type: string
- description: The unique reference for the split configuration, returned when you configure splits in your Customer Area. When this is provided, the `virtualAccount` is also required. Adyen uses the configuration a
  name: splitConfigurationUUID
  type: string
- description: 'The status of the store. Possible values: **Pending**, **Active**, **Inactive**, **InactiveWithModifications**, **Closed**.'
  name: status
  type: string
- description: Adyen-generated unique alphanumeric identifier (UUID) for the store, returned in the response when you create a store. Required when updating an existing store in an `/updateAccountHolder` request.
  name: store
  type: string
- description: 'The name of the account holder''s store. This value is shown in shopper statements. * Length: Between 3 to 22 characters * The following characters are *not* supported: **:;}{$#@!|<>%^*+=\\**'
  name: storeName
  type: string
- description: 'Your unique identifier for the store. The Customer Area also uses this value for the store description. * Length: Between 3 to 128 characters * The following characters are *not* supported: **:;}{$#@!'
  name: storeReference
  type: string
- description: The account holder's `accountCode` where the split amount will be sent. Required when you provide the `splitConfigurationUUID`.
  name: virtualAccount
  type: string
- description: URL of the ecommerce store.
  name: webAddress
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-store-detail-schema.json
slug: notifications-store-detail
tags:
- Payments
- Financial Services
- Fintech
title: StoreDetail
---
