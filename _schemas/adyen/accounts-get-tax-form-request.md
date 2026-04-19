---
description: GetTaxFormRequest schema from Adyen API
layout: schema
name: GetTaxFormRequest
properties_list:
- description: The account holder code you provided when you created the account holder.
  name: accountHolderCode
  type: string
- description: Type of the requested tax form. For example, 1099-K.
  name: formType
  type: string
- description: Applicable tax year in the YYYY format.
  name: year
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-get-tax-form-request-schema.json
slug: accounts-get-tax-form-request
tags:
- Payments
- Financial Services
- Fintech
title: GetTaxFormRequest
---
