---
description: This object holds the transaction footprint for a payment transaction.
layout: schema
name: MCTransactionFootprint
properties_list:
- description: The transaction's CO2 emission in grams
  name: carbonEmissionInGrams
  type: number
- description: The transaction's CO2 emission in ounces
  name: carbonEmissionInOunces
  type: number
- description: The transaction's CO2 emission cost
  name: carbonSocialCost
  type: object
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-doconomy-aland-index-mc-transaction-footprint-schema.json
slug: mastercard-doconomy-aland-index-mc-transaction-footprint
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: MCTransactionFootprint
---
