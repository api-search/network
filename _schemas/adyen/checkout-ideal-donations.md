---
description: IdealDonations schema from Adyen API
layout: schema
name: IdealDonations
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The iDEAL issuer value of the shopper's selected bank. Set this to an **id** of an iDEAL issuer to preselect it.
  name: issuer
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: '**ideal**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-ideal-donations-schema.json
slug: checkout-ideal-donations
tags:
- Payments
- Financial Services
- Fintech
title: IdealDonations
---
