---
description: AuthenticationNotificationData schema from Adyen API
layout: schema
name: AuthenticationNotificationData
properties_list:
- description: Information about the authentication.
  name: authentication
  type: object
- description: The unique identifier of the balance platform.
  name: balancePlatform
  type: string
- description: Unique identifier of the authentication.
  name: id
  type: string
- description: Unique identifier of the payment instrument that was used for the authentication.
  name: paymentInstrumentId
  type: string
- description: Information about the purchase.
  name: purchase
  type: object
- description: 'Outcome of the authentication. Allowed values: * authenticated * rejected * error'
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/authentication-webhooks-authentication-notification-data-schema.json
slug: authentication-webhooks-authentication-notification-data
tags:
- Payments
- Financial Services
- Fintech
title: AuthenticationNotificationData
---
