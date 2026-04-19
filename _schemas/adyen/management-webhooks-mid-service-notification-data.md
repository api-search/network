---
description: MidServiceNotificationData schema from Adyen API
layout: schema
name: MidServiceNotificationData
properties_list:
- description: Indicates whether receiving payments is allowed. This value is set to **true** by Adyen after screening your merchant account.
  name: allowed
  type: boolean
- description: Indicates whether the payment method is enabled (**true**) or disabled (**false**).
  name: enabled
  type: boolean
- description: The unique identifier of the resource.
  name: id
  type: string
- description: The unique identifier of the merchant account.
  name: merchantId
  type: string
- description: Your reference for the payment method.
  name: reference
  type: string
- description: 'The status of the request to add a payment method. Possible values: * **success**: the payment method was added. * **failure**: the request failed. * **capabilityPending**: the **receivePayments** cap'
  name: status
  type: string
- description: The unique identifier of the [store](https://docs.adyen.com/api-explorer/#/ManagementService/latest/post/merchants/{id}/paymentMethodSettings__reqParam_storeId), if any.
  name: storeId
  type: string
- description: Payment method [variant](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api).
  name: type
  type: string
- description: 'Payment method status. Possible values: * **valid** * **pending** * **invalid** * **rejected**'
  name: verificationStatus
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-webhooks-mid-service-notification-data-schema.json
slug: management-webhooks-mid-service-notification-data
tags:
- Payments
- Financial Services
- Fintech
title: MidServiceNotificationData
---
