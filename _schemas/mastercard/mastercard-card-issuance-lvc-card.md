---
description: LVC Card information
layout: schema
name: LVCCard
properties_list:
- description: It is the limit set for each transaction. <BR/> **Conditional Mandatory**<font color='red'>* </font> field - Required while requesting for LVC card.
  name: perTransactionLimit
  type: string
- description: It is the maximum transaction limit configured for the client. <BR/> **Conditional Mandatory**<font color='red'>* </font> field - Required while requesting for LVC card.
  name: totalTransactionLimit
  type: string
- description: Number of times the card can be used in a configured duration. <BR/> **Conditional Mandatory**<font color='red'>* </font> field - Required while requesting for LVC card.
  name: velocity
  type: string
- description: Card validity duration after which the card gets expired. <BR/> **Conditional Mandatory**<font color='red'>* </font> field - Required while requesting for LVC card. <BR/> Must be expressed in ISO 8601
  name: validity
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-lvc-card-schema.json
slug: mastercard-card-issuance-lvc-card
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: LVCCard
---
