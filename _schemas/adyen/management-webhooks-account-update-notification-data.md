---
description: AccountUpdateNotificationData schema from Adyen API
layout: schema
name: AccountUpdateNotificationData
properties_list:
- description: Key-value pairs that specify what you can do with the merchant account and its settings. The key is a capability. For example, the **sendToTransferInstrument** is the capability required before you ca
  name: capabilities
  type: object
- description: The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id).
  name: legalEntityId
  type: string
- description: The unique identifier of the merchant account.
  name: merchantId
  type: string
- description: 'The status of the merchant account. Possible values: * **PreActive**: The merchant account has been created. Users cannot access the merchant account in the Customer Area. The account cannot process p'
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-webhooks-account-update-notification-data-schema.json
slug: management-webhooks-account-update-notification-data
tags:
- Payments
- Financial Services
- Fintech
title: AccountUpdateNotificationData
---
