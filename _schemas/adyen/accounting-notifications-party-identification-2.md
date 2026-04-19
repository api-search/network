---
description: PartyIdentification-2 schema from Adyen API
layout: schema
name: PartyIdentification-2
properties_list:
- description: Address of the bank account owner.
  name: address
  type: object
- description: First name of the individual. Required when `type` is **individual**.
  name: firstName
  type: string
- description: The name of the entity.
  name: fullName
  type: string
- description: Last name of the individual. Required when `type` is **individual**.
  name: lastName
  type: string
- description: 'The type of entity that owns the bank account. Possible values: **individual**, **organization**, or **unknown**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounting-notifications-party-identification-2-schema.json
slug: accounting-notifications-party-identification-2
tags:
- Payments
- Financial Services
- Fintech
title: PartyIdentification-2
---
