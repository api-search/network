---
description: A currency conversion occurred in the payment, and the merchant needs to know information related to this conversion (e.g. to print on the sale receipt). Information related to a currency conversion.
layout: schema
name: CurrencyConversion
properties_list:
- description: Notify if the customer has approved something. Indicates if the customer has accepted a currency conversion.
  name: CustomerApprovedFlag
  type: boolean
- description: ''
  name: ConvertedAmount
  type: object
- description: Rate of currency conversion.
  name: Rate
  type: string
- description: Markup of a currency conversion amount as a percentage.
  name: Markup
  type: string
- description: Commission for a currency conversion.
  name: Commission
  type: number
- description: If a declaration has to be presented to the customer.
  name: Declaration
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-currency-conversion-schema.json
slug: terminal-currency-conversion
tags:
- Payments
- Financial Services
- Fintech
title: CurrencyConversion
---
