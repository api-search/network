---
description: Tax address for a customer
layout: schema
name: Address
properties_list:
- description: Whether the address has been verified
  name: verified
  type: boolean
- description: Address line 1
  name: line1
  type: string
- description: State or province
  name: state
  type: string
- description: City
  name: city
  type: string
- description: Postal or ZIP code
  name: postalCode
  type: string
- description: ISO country code
  name: country
  type: string
provider_name: Amberflo
provider_slug: amberflo
schema_file: json-schema/billing-address-schema.json
slug: billing-address
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
title: Address
---
