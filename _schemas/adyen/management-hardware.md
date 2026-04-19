---
description: Hardware schema from Adyen API
layout: schema
name: Hardware
properties_list:
- description: The brightness of the display when the terminal is being used, expressed as a percentage.
  name: displayMaximumBackLight
  type: integer
- description: 'The hour of the day when the terminal is set to reset the Totals report. By default, the reset hour is at 6:00 AM in the timezone of the terminal. Minimum value: 0, maximum value: 23.'
  name: resetTotalsHour
  type: integer
- description: 'The hour of the day when the terminal is set to reboot to apply the configuration and software updates. By default, the restart hour is at 6:00 AM in the timezone of the terminal. Minimum value: 0, ma'
  name: restartHour
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-hardware-schema.json
slug: management-hardware
tags:
- Payments
- Financial Services
- Fintech
title: Hardware
---
