---
description: CreatePermitRequest schema from Adyen API
layout: schema
name: CreatePermitRequest
properties_list:
- description: The merchant account identifier, with which you want to process the transaction.
  name: merchantAccount
  type: string
- description: The permits to create for this recurring contract.
  name: permits
  type: array
- description: The recurring contract the new permits will use.
  name: recurringDetailReference
  type: string
- description: The shopper's reference to uniquely identify this shopper (e.g. user ID or account ID).
  name: shopperReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/recurring-create-permit-request-schema.json
slug: recurring-create-permit-request
tags:
- Payments
- Financial Services
- Fintech
title: CreatePermitRequest
---
