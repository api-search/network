---
description: AuthenticationData schema from Adyen API
layout: schema
name: AuthenticationData
properties_list:
- description: 'Indicates when 3D Secure authentication should be attempted. This overrides all other rules, including [Dynamic 3D Secure settings](https://docs.adyen.com/risk-management/dynamic-3d-secure). Possible '
  name: attemptAuthentication
  type: string
- description: If set to true, you will only perform the [3D Secure 2 authentication](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only), and not the payment authorisation. Default
  name: authenticationOnly
  type: boolean
- description: Object with additional parameters for the 3D Secure authentication flow.
  name: threeDSRequestData
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-authentication-data-schema.json
slug: checkout-authentication-data
tags:
- Payments
- Financial Services
- Fintech
title: AuthenticationData
---
