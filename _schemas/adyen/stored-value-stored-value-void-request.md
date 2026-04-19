---
description: StoredValueVoidRequest schema from Adyen API
layout: schema
name: StoredValueVoidRequest
properties_list:
- description: The merchant account identifier, with which you want to process the transaction.
  name: merchantAccount
  type: string
- description: The original pspReference of the payment to modify.
  name: originalReference
  type: string
- description: 'Your reference for the payment modification. This reference is visible in Customer Area and in reports. Maximum length: 80 characters.'
  name: reference
  type: string
- description: The physical store, for which this payment is processed.
  name: store
  type: string
- description: The reference of the tender.
  name: tenderReference
  type: string
- description: The unique ID of a POS terminal.
  name: uniqueTerminalId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/stored-value-stored-value-void-request-schema.json
slug: stored-value-stored-value-void-request
tags:
- Payments
- Financial Services
- Fintech
title: StoredValueVoidRequest
---
