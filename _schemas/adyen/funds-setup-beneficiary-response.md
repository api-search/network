---
description: SetupBeneficiaryResponse schema from Adyen API
layout: schema
name: SetupBeneficiaryResponse
properties_list:
- description: Contains field validation errors that would prevent requests from being processed.
  name: invalidFields
  type: array
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The result code.
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-setup-beneficiary-response-schema.json
slug: funds-setup-beneficiary-response
tags:
- Payments
- Financial Services
- Fintech
title: SetupBeneficiaryResponse
---
