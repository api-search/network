---
description: Status of uploaded dpas
layout: schema
name: DpaResults
properties_list:
- description: generated id for srci dpa
  name: srciDpaId
  type: string
- description: 'Status of the individual Digital Payment Application (DPA) item. Potential statuses include: * `SUCCESSFUL` - The DPA is eligible to process transactions. * `FAILED` - The DPA is NOT eligible to proce'
  name: status
  type: string
- description: Registered Legal Name of the Merchant
  name: dpaName
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-unified-checkout-solutions-dpa-results-schema.json
slug: mastercard-unified-checkout-solutions-dpa-results
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: DpaResults
---
