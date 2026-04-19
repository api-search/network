---
description: CloseAccountResponse schema from Adyen API
layout: schema
name: CloseAccountResponse
properties_list:
- description: The account code of the account that is closed.
  name: accountCode
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
- description: 'The new status of the account. >Permitted values: `Active`, `Inactive`, `Suspended`, `Closed`.'
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-close-account-response-schema.json
slug: notifications-close-account-response
tags:
- Payments
- Financial Services
- Fintech
title: CloseAccountResponse
---
