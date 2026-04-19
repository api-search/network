---
description: GetTaxFormResponse schema from Adyen API
layout: schema
name: GetTaxFormResponse
properties_list:
- description: The content of the tax form in the Base64 binary format.
  name: content
  type: string
- description: The content type of the tax form.
  name: contentType
  type: string
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
schema_file: json-schema/accounts-get-tax-form-response-schema.json
slug: accounts-get-tax-form-response
tags:
- Payments
- Financial Services
- Fintech
title: GetTaxFormResponse
---
