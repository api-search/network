---
description: A Mastercard payment card representing a physical or virtual card instrument issued to a cardholder. Covers prepaid, debit, credit, and commercial card products across Card Issuance, BIN Lookup, Benefit Eligibility, and tokenization services.
layout: schema
name: Mastercard Card
properties_list:
- description: Primary Account Number (PAN) for the card. Must pass Luhn algorithm validation.
  name: cardNumber
  type: string
- description: Unique system-generated identifier for the card within the Mastercard issuing platform.
  name: cardId
  type: string
- description: Identifier for the card pack, used in card issuance and fulfillment.
  name: cardPackId
  type: string
- description: Classification of the card product.
  name: cardType
  type: string
- description: Three-character code identifying the specific card product (e.g., MSI for Mastercard Standard, MWE for World Elite, MWO for World).
  name: cardProductCode
  type: string
- description: Card plan code defining the card product configuration and features.
  name: planCode
  type: string
- description: Program code for the card product within the issuing institution.
  name: programCode
  type: string
- description: Card brand within the Mastercard network.
  name: brand
  type: string
- description: Card tier or level indicating the product benefits tier.
  name: tier
  type: string
- description: Current lifecycle status of the card.
  name: status
  type: string
- description: Date the card was issued, in ISO 8601 date format.
  name: issuedDate
  type: string
- description: Card expiration date in MMYY format.
  name: expirationDate
  type: string
- description: Name embossed or printed on the physical card.
  name: embossedName
  type: string
- description: Indicates whether the card number is printed on the physical card. True means the number is not printed.
  name: numberless
  type: boolean
- description: Indicates whether the card was issued as an instant card (immediately generated).
  name: instant
  type: boolean
- description: Indicates whether this is a virtual card with no physical plastic.
  name: virtual
  type: boolean
- description: Indicates whether the card supports contactless (NFC/PayPass) transactions.
  name: contactless
  type: boolean
- description: Indicates whether a photo is required on the card.
  name: photoIndicator
  type: string
- description: Mode of card delivery to the cardholder.
  name: deliveryMode
  type: string
- description: Date the card was delivered or handed over to the client, in ISO 8601 format.
  name: deliveryDate
  type: string
- description: MDES (Mastercard Digital Enablement Service) token representing this card for digital transactions.
  name: tokenNumber
  type: string
- description: Bank Identification Number (BIN), the first 6-8 digits of the card number identifying the issuing institution.
  name: binNumber
  type: string
- description: ICA (Interbank Card Association) number of the issuing institution.
  name: issuerId
  type: string
- description: Name of the financial institution that issued the card.
  name: issuerName
  type: string
- description: ISO 3166-1 alpha-3 country code of the issuing institution.
  name: issuerCountryCode
  type: string
- description: ''
  name: cardholder
  type: object
- description: ''
  name: limits
  type: object
- description: Type of card issuance application.
  name: applicationType
  type: string
- description: Unique code of the corporate entity for commercial/corporate cards.
  name: corporateCode
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/card.json
slug: card
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Mastercard Card
---
