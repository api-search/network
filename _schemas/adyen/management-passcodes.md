---
description: Passcodes schema from Adyen API
layout: schema
name: Passcodes
properties_list:
- description: The passcode for the Admin menu and the Settings menu.
  name: adminMenuPin
  type: string
- description: The passcode for referenced and unreferenced refunds on standalone terminals.
  name: refundPin
  type: string
- description: The passcode to unlock the terminal screen after a timeout.
  name: screenLockPin
  type: string
- description: The passcode for the Transactions menu.
  name: txMenuPin
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-passcodes-schema.json
slug: management-passcodes
tags:
- Payments
- Financial Services
- Fintech
title: Passcodes
---
