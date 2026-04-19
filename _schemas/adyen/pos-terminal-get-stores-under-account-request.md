---
description: GetStoresUnderAccountRequest schema from Adyen API
layout: schema
name: GetStoresUnderAccountRequest
properties_list:
- description: The company account. If you only specify this parameter, the response includes the stores of all merchant accounts that are associated with the company account.
  name: companyAccount
  type: string
- description: The merchant account. With this parameter, the response only includes the stores of the specified merchant account.
  name: merchantAccount
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/pos-terminal-get-stores-under-account-request-schema.json
slug: pos-terminal-get-stores-under-account-request
tags:
- Payments
- Financial Services
- Fintech
title: GetStoresUnderAccountRequest
---
