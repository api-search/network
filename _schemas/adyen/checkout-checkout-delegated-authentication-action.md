---
description: CheckoutDelegatedAuthenticationAction schema from Adyen API
layout: schema
name: CheckoutDelegatedAuthenticationAction
properties_list:
- description: A token needed to authorise a payment.
  name: authorisationToken
  type: string
- description: Encoded payment data.
  name: paymentData
  type: string
- description: Specifies the payment method.
  name: paymentMethodType
  type: string
- description: A token to pass to the delegatedAuthentication component.
  name: token
  type: string
- description: '**delegatedAuthentication**'
  name: type
  type: string
- description: Specifies the URL to redirect to.
  name: url
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-checkout-delegated-authentication-action-schema.json
slug: checkout-checkout-delegated-authentication-action
tags:
- Payments
- Financial Services
- Fintech
title: CheckoutDelegatedAuthenticationAction
---
