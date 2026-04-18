---
description: Core Banking System Account Info. Applicable for Debit Cards only
layout: schema
name: CbsAccount
properties_list:
- description: Primary Account number in CBS. <br/> **Conditional Mandatory**<font color='red'>* </font> field - Required while creating new client.
  name: number
  type: string
- description: Unique id/code/reference assigned to the client in CBS.
  name: clientId
  type: string
- description: '"The currency in which the amount is loaded. <br> Values - 3 letter alphabetic currency codes in `ISO 4217`" <br/> **Conditional Mandatory**<font color=''red''>* </font> field - Required while creating '
  name: currency
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-cbs-account-schema.json
slug: mastercard-card-issuance-cbs-account
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: CbsAccount
---
