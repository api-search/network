---
description: ResponseAdditionalDataCard schema from Adyen API
layout: schema
name: ResponseAdditionalDataCard
properties_list:
- description: 'The first six digits of the card number. This is the [Bank Identification Number (BIN)](https://docs.adyen.com/get-started-with-adyen/payment-glossary#bank-identification-number-bin) for card numbers '
  name: cardBin
  type: string
- description: The cardholder name passed in the payment request.
  name: cardHolderName
  type: string
- description: The bank or the financial institution granting lines of credit through card association branded payment cards. This information can be included when available.
  name: cardIssuingBank
  type: string
- description: 'The country where the card was issued. Example: US'
  name: cardIssuingCountry
  type: string
- description: 'The currency in which the card is issued, if this information is available. Provided as the currency code or currency number from the ISO-4217 standard. Example: USD'
  name: cardIssuingCurrency
  type: string
- description: 'The card payment method used for the transaction. Example: amex'
  name: cardPaymentMethod
  type: string
- description: The last four digits of a card number. > Returned only in case of a card payment.
  name: cardSummary
  type: string
- description: The first eight digits of the card number. Only returned if the card number is 16 digits or more. This is the [Bank Identification Number (BIN)](https://docs.adyen.com/get-started-with-adyen/payment-g
  name: issuerBin
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payouts-response-additional-data-card-schema.json
slug: payouts-response-additional-data-card
tags:
- Payments
- Financial Services
- Fintech
title: ResponseAdditionalDataCard
---
