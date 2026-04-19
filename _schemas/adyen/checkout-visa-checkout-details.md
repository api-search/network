---
description: VisaCheckoutDetails schema from Adyen API
layout: schema
name: VisaCheckoutDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**.
  name: fundingSource
  type: string
- description: '**visacheckout**'
  name: type
  type: string
- description: The Visa Click to Pay Call ID value. When your shopper selects a payment and/or a shipping address from Visa Click to Pay, you will receive a Visa Click to Pay Call ID.
  name: visaCheckoutCallId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-visa-checkout-details-schema.json
slug: checkout-visa-checkout-details
tags:
- Payments
- Financial Services
- Fintech
title: VisaCheckoutDetails
---
