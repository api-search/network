---
description: ResponseAdditionalDataOpi schema from Adyen API
layout: schema
name: ResponseAdditionalDataOpi
properties_list:
- description: 'Returned in the response if you included `opi.includeTransToken: true` in an ecommerce payment request. This contains an Oracle Payment Interface token that you can store in your Oracle Opera database'
  name: opi.transToken
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-response-additional-data-opi-schema.json
slug: payments-response-additional-data-opi
tags:
- Payments
- Financial Services
- Fintech
title: ResponseAdditionalDataOpi
---
