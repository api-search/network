---
description: CardBin schema from Adyen API
layout: schema
name: CardBin
properties_list:
- description: The first 6 digit of the card number. Enable this field via merchant account settings.
  name: bin
  type: string
- description: If true, it indicates a commercial card. Enable this field via merchant account settings.
  name: commercial
  type: boolean
- description: 'The card funding source. Valid values are: * CHARGE * CREDIT * DEBIT * DEFERRED_DEBIT * PREPAID * PREPAID_RELOADABLE * PREPAID_NONRELOADABLE > Enable this field via merchant account settings.'
  name: fundingSource
  type: string
- description: 'Indicates availability of funds. Visa: * "I" (fast funds are supported) * "N" (otherwise) Mastercard: * "I" (product type is Prepaid or Debit, or issuing country is in CEE/HGEM list) * "N" (otherwise)'
  name: fundsAvailability
  type: string
- description: The first 8 digit of the card number. Enable this field via merchant account settings.
  name: issuerBin
  type: string
- description: The issuing bank of the card.
  name: issuingBank
  type: string
- description: The country where the card was issued from.
  name: issuingCountry
  type: string
- description: The currency of the card.
  name: issuingCurrency
  type: string
- description: The payment method associated with the card (e.g. visa, mc, or amex).
  name: paymentMethod
  type: string
- description: 'Indicates whether a payout is eligible or not for this card. Visa: * "Y" * "N" Mastercard: * "Y" (domestic and cross-border) * "D" (only domestic) * "N" (no MoneySend) * "U" (unknown) > Returned when '
  name: payoutEligible
  type: string
- description: The last four digits of the card number.
  name: summary
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/binlookup-card-bin-schema.json
slug: binlookup-card-bin
tags:
- Payments
- Financial Services
- Fintech
title: CardBin
---
