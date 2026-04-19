---
description: AddressRequirement schema from Adyen API
layout: schema
name: AddressRequirement
properties_list:
- description: Specifies the required address related fields for a particular route.
  name: description
  type: string
- description: List of address fields.
  name: requiredAddressFields
  type: array
- description: '**addressRequirement**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-address-requirement-schema.json
slug: configuration-address-requirement
tags:
- Payments
- Financial Services
- Fintech
title: AddressRequirement
---
