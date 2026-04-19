---
description: CloseAccountHolderResponse schema from Adyen API
layout: schema
name: CloseAccountHolderResponse
properties_list:
- description: The new status of the Account Holder.
  name: accountHolderStatus
  type: object
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
schema_file: json-schema/accounts-close-account-holder-response-schema.json
slug: accounts-close-account-holder-response
tags:
- Payments
- Financial Services
- Fintech
title: CloseAccountHolderResponse
---
