---
description: CreateMerchantRequest schema from Adyen API
layout: schema
name: CreateMerchantRequest
properties_list:
- description: The unique identifier of the [business line](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines). Required for an Adyen for Platforms Manage integration.
  name: businessLineId
  type: string
- description: The unique identifier of the company account.
  name: companyId
  type: string
- description: Your description for the merchant account, maximum 300 characters.
  name: description
  type: string
- description: The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities). Required for an Adyen for Platforms Manage integration.
  name: legalEntityId
  type: string
- description: Sets the pricing plan for the merchant account. Required for an Adyen for Platforms Manage integration. Your Adyen contact will provide the values that you can use.
  name: pricingPlan
  type: string
- description: Your reference for the merchant account. To make this reference the unique identifier of the merchant account, your Adyen contact can set up a template on your company account. The template can have 6
  name: reference
  type: string
- description: List of sales channels that the merchant will process payments with
  name: salesChannels
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-create-merchant-request-schema.json
slug: management-create-merchant-request
tags:
- Payments
- Financial Services
- Fintech
title: CreateMerchantRequest
---
