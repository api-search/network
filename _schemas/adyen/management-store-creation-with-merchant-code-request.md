---
description: StoreCreationWithMerchantCodeRequest schema from Adyen API
layout: schema
name: StoreCreationWithMerchantCodeRequest
properties_list:
- description: The address of the store.
  name: address
  type: object
- description: The unique identifiers of the [business lines](https://docs.adyen.com/api-explorer/legalentity/latest/post/businessLines#responses-200-id) that the store is associated with. If not specified, the busi
  name: businessLineIds
  type: array
- description: Your description of the store.
  name: description
  type: string
- description: The unique identifier of the store, used by certain payment methods and tax authorities. Accepts up to 14 digits. Required for CNPJ in Brazil, in the format 00.000.000/00git00-00 separated by dots, sl
  name: externalReferenceId
  type: string
- description: The unique identifier of the merchant account that the store belongs to.
  name: merchantId
  type: string
- description: The phone number of the store, including '+' and country code in the [E.164](https://en.wikipedia.org/wiki/E.164) format. If passed in a different format, we convert and validate the phone number agai
  name: phoneNumber
  type: string
- description: 'Your reference to recognize the store by. Also known as the store code. Allowed characters: lowercase and uppercase letters without diacritics, numbers 0 through 9, hyphen (-), and underscore (_). If '
  name: reference
  type: string
- description: 'The store name to be shown on the shopper''s bank or credit card statement and on the shopper receipt. Maximum length: 22 characters; can''t be all numbers.'
  name: shopperStatement
  type: string
- description: Rules for Adyen for Platforms merchants to split the transaction amount and fees.
  name: splitConfiguration
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-store-creation-with-merchant-code-request-schema.json
slug: management-store-creation-with-merchant-code-request
tags:
- Payments
- Financial Services
- Fintech
title: StoreCreationWithMerchantCodeRequest
---
