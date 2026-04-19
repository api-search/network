---
description: BankAccountInfo schema from Adyen API
layout: schema
name: BankAccountInfo
properties_list:
- description: The address of the bank account owner.
  name: address
  type: object
- description: The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard.
  name: iban
  type: string
- description: The name of the bank account owner.
  name: ownerName
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-bank-account-info-schema.json
slug: notification-webhooks-bank-account-info
tags:
- Payments
- Financial Services
- Fintech
title: BankAccountInfo
---
