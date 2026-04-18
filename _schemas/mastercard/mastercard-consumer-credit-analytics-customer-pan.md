---
description: ''
layout: schema
name: CustomerPAN
properties_list:
- description: The card number for which the score needs to be retrieved. A minimum of 16 and a maximum of 19 digits are allowed.
  name: customerPAN
  type: string
- description: A parameter indicating that the user of this API has consent to pull the score for the requested PAN number.
  name: hasConsent
  type: boolean
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-consumer-credit-analytics-customer-pan-schema.json
slug: mastercard-consumer-credit-analytics-customer-pan
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: CustomerPAN
---
