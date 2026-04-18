---
description: ''
layout: schema
name: Conversion
properties_list:
- description: Rate applied to the transaction to convert from Transaction Currency to Cardholder Billing Currency.
  name: conversionRate
  type: number
- description: Amount in the cardholder billing currency.
  name: crdhldBillAmt
  type: number
- description: Date of the requested FX rates.
  name: fxDate
  type: string
- description: Currency of the transaction.
  name: transCurr
  type: string
- description: Cardholder billing currency.
  name: crdhldBillCurr
  type: string
- description: Amount in the transaction currency.
  name: transAmt
  type: number
- description: Additional fees imposed by the bank.
  name: bankFee
  type: number
- description: The error code associated with the error being returned.
  name: errorCode
  type: string
- description: The reason for the error.
  name: errorMessage
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-standard-currency-conversion-calculator-conversion-schema.json
slug: mastercard-standard-currency-conversion-calculator-conversion
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Conversion
---
