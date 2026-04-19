---
description: CreatePermitResult schema from Adyen API
layout: schema
name: CreatePermitResult
properties_list:
- description: List of new permits.
  name: permitResultList
  type: array
- description: A unique reference associated with the request. This value is globally unique; quote it when communicating with us about this request.
  name: pspReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/recurring-create-permit-result-schema.json
slug: recurring-create-permit-result
tags:
- Payments
- Financial Services
- Fintech
title: CreatePermitResult
---
