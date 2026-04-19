---
description: TransactionDescriptionInfo schema from Adyen API
layout: schema
name: TransactionDescriptionInfo
properties_list:
- description: 'The text to be shown on the shopper''s bank statement. We recommend sending a maximum of 22 characters, otherwise banks might truncate the string. Allowed characters: **a-z**, **A-Z**, **0-9**, spaces,'
  name: doingBusinessAsName
  type: string
- description: 'The type of transaction description you want to use: - **fixed**: The transaction description set in this request is used for all payments with this payment method. - **append**: The transaction descr'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-transaction-description-info-schema.json
slug: management-transaction-description-info
tags:
- Payments
- Financial Services
- Fintech
title: TransactionDescriptionInfo
---
