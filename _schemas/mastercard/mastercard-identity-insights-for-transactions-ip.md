---
description: ''
layout: schema
name: Ip
properties_list:
- description: The distance (in miles) between the IP address and the physical address.
  name: billingAddressDistance
  type: integer
- description: Number of days that have passed since the IP address was last seen.
  name: lastSeenDays
  type: integer
- description: 'Ip Connection type description. Possible values are: * cable-dsl * corporate * cellular * dialup'
  name: connectionType
  type: string
- description: The distance (in miles) between the IP address and the physical address.
  name: shippingAddressDistance
  type: integer
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-identity-insights-for-transactions-ip-schema.json
slug: mastercard-identity-insights-for-transactions-ip
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Ip
---
