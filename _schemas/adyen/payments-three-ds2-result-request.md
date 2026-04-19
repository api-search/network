---
description: ThreeDS2ResultRequest schema from Adyen API
layout: schema
name: ThreeDS2ResultRequest
properties_list:
- description: The merchant account identifier, with which you want to process the transaction.
  name: merchantAccount
  type: string
- description: The pspReference returned in the /authorise call.
  name: pspReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-three-ds2-result-request-schema.json
slug: payments-three-ds2-result-request
tags:
- Payments
- Financial Services
- Fintech
title: ThreeDS2ResultRequest
---
