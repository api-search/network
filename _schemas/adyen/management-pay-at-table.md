---
description: PayAtTable schema from Adyen API
layout: schema
name: PayAtTable
properties_list:
- description: 'Allowed authentication methods: Magswipe, Manual Entry.'
  name: authenticationMethod
  type: string
- description: Enable Pay at table.
  name: enablePayAtTable
  type: boolean
- description: 'Sets the allowed payment instrument for Pay at table transactions. Can be: **cash** or **card**. If not set, the terminal presents both options.'
  name: paymentInstrument
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-pay-at-table-schema.json
slug: management-pay-at-table
tags:
- Payments
- Financial Services
- Fintech
title: PayAtTable
---
