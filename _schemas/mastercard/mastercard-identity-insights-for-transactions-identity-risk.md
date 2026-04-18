---
description: ''
layout: schema
name: IdentityRisk
properties_list:
- description: A comprehensive 0-500 score associated with the individual's identity.
  name: score
  type: integer
- description: 'Reason code explanation value for the identity risk score based on data provided. Possible values are: * High Severity : AA-AP * Medium Severity : JA-JF * Low Severity : RA-RP'
  name: reasonCode
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-identity-insights-for-transactions-identity-risk-schema.json
slug: mastercard-identity-insights-for-transactions-identity-risk
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: IdentityRisk
---
