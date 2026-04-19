---
description: Opi schema from Adyen API
layout: schema
name: Opi
properties_list:
- description: Indicates if Pay at table is enabled.
  name: enablePayAtTable
  type: boolean
- description: The store number to use for Pay at Table.
  name: payAtTableStoreNumber
  type: string
- description: The URL and port number used for Pay at Table communication.
  name: payAtTableURL
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-opi-schema.json
slug: management-opi
tags:
- Payments
- Financial Services
- Fintech
title: Opi
---
