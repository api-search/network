---
description: Object for individual Digital Payment Application (DPA) item status data.
layout: schema
name: DpaResults
properties_list:
- description: 'The registered identifier for the Digital Payment Application (DPA) accessing the service. Conditional: Required if you are a Merchant directly integrating with Mastercard Checkout Solutions (MCS) API'
  name: srcDpaId
  type: string
- description: 'Status of the individual Digital Payment Application (DPA) item. Potential statuses include: * SUCCESSFUL - The DPA is eligible to process transactions. * FAILED - The DPA is NOT eligible to process t'
  name: status
  type: string
- description: Legal name of Merchant (which may differ from dpaPresentationName).
  name: dpaName
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-checkout-solutions-dpa-results-schema.json
slug: mastercard-checkout-solutions-dpa-results
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: DpaResults
---
