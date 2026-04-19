---
description: Repayment schema from Adyen API
layout: schema
name: Repayment
properties_list:
- description: The repayment that is deducted daily from incoming net volume, in [basis points](https://www.investopedia.com/terms/b/basispoint.asp).
  name: basisPoints
  type: integer
- description: An object containing the details of the configuration for repayment term.
  name: term
  type: object
- description: An object containing the details of the 30-day repayment threshold.
  name: threshold
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-repayment-schema.json
slug: configuration-repayment
tags:
- Payments
- Financial Services
- Fintech
title: Repayment
---
