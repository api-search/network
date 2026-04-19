---
description: PaymentSetupResponse schema from Adyen API
layout: schema
name: PaymentSetupResponse
properties_list:
- description: The encoded payment session that you need to pass to the SDK.
  name: paymentSession
  type: string
- description: The detailed list of stored payment details required to generate payment forms. Will be empty if oneClick is set to false in the request.
  name: recurringDetails
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-setup-response-schema.json
slug: checkout-payment-setup-response
tags:
- Payments
- Financial Services
- Fintech
title: PaymentSetupResponse
---
