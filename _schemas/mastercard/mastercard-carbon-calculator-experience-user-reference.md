---
description: Successful user enrollment response
layout: schema
name: UserReference
properties_list:
- description: Last 4 digits of a full payment card number which were provided as enrollment request.
  name: cardNumberLastFourDigits
  type: string
- description: Status of the user on Carbon Calculator Experience API. Possible values are ACTIVE and INACTIVE.
  name: status
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-carbon-calculator-experience-user-reference-schema.json
slug: mastercard-carbon-calculator-experience-user-reference
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: UserReference
---
