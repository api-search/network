---
description: It contains the identifications of the stored value account or the stored value card, and the associated product sold by the Sale System for stored value requests. Identification of the stored value account or the stored value card.
layout: schema
name: StoredValueAccountID
properties_list:
- description: ''
  name: StoredValueAccountType
  type: object
- description: ''
  name: StoredValueProvider
  type: string
- description: ''
  name: OwnerName
  type: string
- description: ''
  name: ExpiryDate
  type: integer
- description: ''
  name: EntryMode
  type: object
- description: ''
  name: IdentificationType
  type: object
- description: ''
  name: StoredValueID
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-stored-value-account-id-schema.json
slug: terminal-stored-value-account-id
tags:
- Payments
- Financial Services
- Fintech
title: StoredValueAccountID
---
