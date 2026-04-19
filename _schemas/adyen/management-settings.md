---
description: Settings schema from Adyen API
layout: schema
name: Settings
properties_list:
- description: 'The preferred Wi-Fi band, for use if the terminals support multiple bands. Possible values: All, 2.4GHz, 5GHz.'
  name: band
  type: string
- description: Indicates whether roaming is enabled on the terminals.
  name: roaming
  type: boolean
- description: 'The connection time-out in seconds. Minimum value: 0.'
  name: timeout
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-settings-schema.json
slug: management-settings
tags:
- Payments
- Financial Services
- Fintech
title: Settings
---
