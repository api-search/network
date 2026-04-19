---
description: Indicate the status and the remaining coins and bill in a cash handling device. Status of cash handling device.
layout: schema
name: CashHandlingDevice
properties_list:
- description: Indicates if the cash handling device is working and usable.
  name: CashHandlingOKFlag
  type: boolean
- description: Currency of a monetary amount.
  name: Currency
  type: string
- description: ''
  name: CoinsOrBills
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-cash-handling-device-schema.json
slug: terminal-cash-handling-device
tags:
- Payments
- Financial Services
- Fintech
title: CashHandlingDevice
---
