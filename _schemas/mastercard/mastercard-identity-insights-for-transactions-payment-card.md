---
description: ''
layout: schema
name: PaymentCard
properties_list:
- description: Count of days since the payment card and name was first observed in the network. If they have not been observed together before, first seen days will be 0.
  name: cardHolderNamefirstSeenDays
  type: integer
- description: Count of times the payment card and name have been observed in the network over the past 90 days. If they have not been observed together in the past 90 days, velocity will be 0.
  name: cardHolderNameVelocity
  type: integer
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-identity-insights-for-transactions-payment-card-schema.json
slug: mastercard-identity-insights-for-transactions-payment-card
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: PaymentCard
---
