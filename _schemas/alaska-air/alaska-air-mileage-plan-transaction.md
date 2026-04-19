---
description: A Mileage Plan mile earn or redeem transaction
layout: schema
name: Transaction
properties_list:
- description: Unique transaction identifier
  name: transactionId
  type: string
- description: Transaction type
  name: type
  type: string
- description: Miles earned or redeemed
  name: miles
  type: integer
- description: Transaction description
  name: description
  type: string
- description: Transaction date
  name: date
  type: string
- description: Partner name
  name: partner
  type: string
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-mileage-plan-transaction-schema.json
slug: alaska-air-mileage-plan-transaction
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: Transaction
---
