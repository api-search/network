---
description: GetAccountHolderRequest schema from Adyen API
layout: schema
name: GetAccountHolderRequest
properties_list:
- description: The code of the account of which to retrieve the details. > Required if no `accountHolderCode` is provided.
  name: accountCode
  type: string
- description: The code of the account holder of which to retrieve the details. > Required if no `accountCode` is provided.
  name: accountHolderCode
  type: string
- description: True if the request should return the account holder details
  name: showDetails
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-get-account-holder-request-schema.json
slug: accounts-get-account-holder-request
tags:
- Payments
- Financial Services
- Fintech
title: GetAccountHolderRequest
---
