---
description: Allows the check information to be provided by the Sale System before requesting the payment, or stored by the Sale System after processing of the payment. Information related to the paper check used for the transaction.
layout: schema
name: CheckData
properties_list:
- description: Mandatory if TrackData absent.
  name: BankID
  type: string
- description: Mandatory if TrackData absent.
  name: AccountNumber
  type: string
- description: Mandatory if TrackData absent.
  name: CheckNumber
  type: string
- description: ''
  name: TrackData
  type: object
- description: If provided by the customer.
  name: CheckCardNumber
  type: string
- description: ''
  name: TypeCode
  type: object
- description: Absent if country of the Sale system.
  name: Country
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-check-data-schema.json
slug: terminal-check-data
tags:
- Payments
- Financial Services
- Fintech
title: CheckData
---
