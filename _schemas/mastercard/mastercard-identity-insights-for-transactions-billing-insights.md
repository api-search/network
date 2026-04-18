---
description: ''
layout: schema
name: BillingInsights
properties_list:
- description: 'The most granular level to which the address could be validated. Ex. If the address was only valid to the city level (but not to the house level), it would return valid_to_city.Possible Values are: * '
  name: validityLevel
  type: string
- description: Number of days that have passed since the address was first seen.
  name: firstSeenDays
  type: integer
- description: Number of days that have passed since the address was last seen.
  name: lastSeenDays
  type: integer
- description: 'The match status between either of the input names (person or business) and the queried entity. Possible values are: * not-found * match * no-match'
  name: matchToName
  type: string
- description: 'The relationship between billing and shipping address. Possible values are: * `match` * `city_match` * `seen_together` * `seen_with_others` * `no_relationship` * `null`'
  name: shippingAddressRelationship
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-identity-insights-for-transactions-billing-insights-schema.json
slug: mastercard-identity-insights-for-transactions-billing-insights
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: BillingInsights
---
