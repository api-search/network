---
description: CreateMerchantResponse schema from Adyen API
layout: schema
name: CreateMerchantResponse
properties_list:
- description: The unique identifier of the [business line](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines).
  name: businessLineId
  type: string
- description: The unique identifier of the company account.
  name: companyId
  type: string
- description: Your description for the merchant account, maximum 300 characters.
  name: description
  type: string
- description: The unique identifier of the merchant account. If Adyen set up a template for the `reference`, then the `id` will have the same value as the `reference` that you sent in the request. Otherwise, the va
  name: id
  type: string
- description: The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities).
  name: legalEntityId
  type: string
- description: Partner pricing plan for the merchant, applicable for merchants under AfP managed company accounts.
  name: pricingPlan
  type: string
- description: Your reference for the merchant account.
  name: reference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-create-merchant-response-schema.json
slug: management-create-merchant-response
tags:
- Payments
- Financial Services
- Fintech
title: CreateMerchantResponse
---
