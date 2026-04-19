---
description: Indicates the remaining number of coins or bills of a given value in a cash handling device. When the cash handling machine does not have any more coins or bills of a certain value, the number must be equal to 0. Number of coins or bills of a given value.
layout: schema
name: CoinsOrBills
properties_list:
- description: Value of a coin or bill.
  name: UnitValue
  type: number
- description: Number of elements.
  name: Number
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-coins-or-bills-schema.json
slug: terminal-coins-or-bills
tags:
- Payments
- Financial Services
- Fintech
title: CoinsOrBills
---
