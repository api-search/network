---
description: PaymentDetailsRequest schema from Adyen API
layout: schema
name: PaymentDetailsRequest
properties_list:
- description: Data for 3DS authentication.
  name: authenticationData
  type: object
- description: Use this collection to submit the details that were returned as a result of the `/payments` call.
  name: details
  type: object
- description: Encoded payment data. For [authorizing a payment after using 3D Secure 2 Authentication-only](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only/#authorise-the-paymen
  name: paymentData
  type: string
- description: Change the `authenticationOnly` indicator originally set in the `/payments` request. Only needs to be set if you want to modify the value set previously.
  name: threeDSAuthenticationOnly
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-details-request-schema.json
slug: checkout-payment-details-request
tags:
- Payments
- Financial Services
- Fintech
title: PaymentDetailsRequest
---
