---
description: UltimatePartyIdentification schema from Adyen API
layout: schema
name: UltimatePartyIdentification
properties_list:
- description: Address of the bank account owner.
  name: address
  type: object
- description: The date of birth of the individual in [ISO-8601](https://www.w3.org/TR/NOTE-datetime) format. For example, **YYYY-MM-DD**. Should not be before January 1, 1900. Allowed only when `type` is **individu
  name: dateOfBirth
  type: string
- description: First name of the individual. Allowed only when `type` is **individual**.
  name: firstName
  type: string
- description: The name of the entity.
  name: fullName
  type: string
- description: Last name of the individual. Allowed only when `type` is **individual**.
  name: lastName
  type: string
- description: A unique reference to identify the party or counterparty involved in transfers. This identifier ensures consistency and uniqueness throughout all transactions initiated to and from the same party. For
  name: reference
  type: string
- description: 'The type of entity that owns the bank account. Possible values: **individual**, **organization**, or **unknown**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-ultimate-party-identification-schema.json
slug: transfers-ultimate-party-identification
tags:
- Payments
- Financial Services
- Fintech
title: UltimatePartyIdentification
---
