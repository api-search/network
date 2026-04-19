---
description: ModificationResult schema from Adyen API
layout: schema
name: ModificationResult
properties_list:
- description: This field contains additional data, which may be returned in a particular modification response.
  name: additionalData
  type: object
- description: Adyen's 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request.
  name: pspReference
  type: string
- description: Indicates if the modification request has been received for processing.
  name: response
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-modification-result-schema.json
slug: payments-modification-result
tags:
- Payments
- Financial Services
- Fintech
title: ModificationResult
---
