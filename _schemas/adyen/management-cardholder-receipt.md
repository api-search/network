---
description: CardholderReceipt schema from Adyen API
layout: schema
name: CardholderReceipt
properties_list:
- description: A custom header to show on the shopper receipt for an authorised transaction. Allows one or two comma-separated header lines, and blank lines. For example, `header,header,filler`
  name: headerForAuthorizedReceipt
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-cardholder-receipt-schema.json
slug: management-cardholder-receipt
tags:
- Payments
- Financial Services
- Fintech
title: CardholderReceipt
---
