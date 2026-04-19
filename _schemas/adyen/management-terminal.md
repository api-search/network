---
description: Terminal schema from Adyen API
layout: schema
name: Terminal
properties_list:
- description: Indicates the account level to which the terminal is assigned, the [assignment status](https://docs.adyen.com/point-of-sale/automating-terminal-management/assign-terminals-api), and where the terminal
  name: assignment
  type: object
- description: Information about bluetooth, cellular, ethernet and wifi connectivity for the terminal.
  name: connectivity
  type: object
- description: The software release currently in use on the terminal.
  name: firmwareVersion
  type: string
- description: The unique identifier of the terminal.
  name: id
  type: string
- description: Date and time of the last activity on the terminal. Not included when the last activity was more than 14 days ago.
  name: lastActivityAt
  type: string
- description: Date and time of the last transaction on the terminal. Not included when the last transaction was more than 14 days ago.
  name: lastTransactionAt
  type: string
- description: The model name of the terminal.
  name: model
  type: string
- description: The serial number of the terminal.
  name: serialNumber
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-terminal-schema.json
slug: management-terminal
tags:
- Payments
- Financial Services
- Fintech
title: Terminal
---
