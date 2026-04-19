---
description: SubjectErasureByPspReferenceRequest schema from Adyen API
layout: schema
name: SubjectErasureByPspReferenceRequest
properties_list:
- description: Set this to **true** if you want to delete shopper-related data, even if the shopper has an existing recurring transaction. This only deletes the shopper-related data for the specific payment, but doe
  name: forceErasure
  type: boolean
- description: Your merchant account
  name: merchantAccount
  type: string
- description: The PSP reference of the payment. We will delete all shopper-related data for this payment.
  name: pspReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/data-protection-subject-erasure-by-psp-reference-request-schema.json
slug: data-protection-subject-erasure-by-psp-reference-request
tags:
- Payments
- Financial Services
- Fintech
title: SubjectErasureByPspReferenceRequest
---
