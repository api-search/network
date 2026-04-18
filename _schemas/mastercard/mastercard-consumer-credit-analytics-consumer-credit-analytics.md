---
description: Object containing list of customer PAN's along with score type and product type for which score will be fetched.
layout: schema
name: ConsumerCreditAnalytics
properties_list:
- description: A boolean indicating that the user of this API has requested for embedding data for the PANs. Possible value - true or false
  name: hasEmbedding
  type: boolean
- description: The 3-letter country abbreviation for the customer. These abbreviations follow https://www.iso.org/iso-3166-country-codes.html.
  name: countryCode
  type: string
- description: The card numbers and consents for which score needs to be retrieved. Max 20 PAN numbers are allowed in a request.
  name: customerPANs
  type: array
- description: Type of score needs to be retrieved for the card number, Possible value - DELINQUENCY.
  name: scoreTypes
  type: array
- description: Type of products for which score needs to be retrieved of the card number, Possible value - CREDIT_CARD.
  name: productTypes
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-consumer-credit-analytics-consumer-credit-analytics-schema.json
slug: mastercard-consumer-credit-analytics-consumer-credit-analytics
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: ConsumerCreditAnalytics
---
