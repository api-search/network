---
description: Card schema from Adyen API
layout: schema
name: Card
properties_list:
- description: Contains the card user's password and mobile phone number. This is required when you issue cards that can be used to make online payments within the EEA and the UK, or can be added to digital wallets.
  name: authentication
  type: object
- description: The bank identification number (BIN) of the card number.
  name: bin
  type: string
- description: 'The brand of the physical or the virtual card. Possible values: **visa**, **mc**.'
  name: brand
  type: string
- description: The brand variant of the physical or the virtual card. For example, **visadebit** or **mcprepaid**. >Reach out to your Adyen contact to get the values relevant for your integration.
  name: brandVariant
  type: string
- description: 'The name of the cardholder. Maximum length: 26 characters.'
  name: cardholderName
  type: string
- description: Settings required when creating a physical or a virtual card. Reach out to your Adyen contact to get the values that you can send in this object.
  name: configuration
  type: object
- description: The CVC2 value of the card. > The CVC2 is not sent by default. This is only returned in the `POST` response for single-use virtual cards.
  name: cvc
  type: string
- description: The delivery contact (name and address) for physical card delivery.
  name: deliveryContact
  type: object
- description: The expiration date of the card.
  name: expiration
  type: object
- description: 'The form factor of the card. Possible values: **virtual**, **physical**.'
  name: formFactor
  type: string
- description: Last last four digits of the card number.
  name: lastFour
  type: string
- description: The primary account number (PAN) of the card. > The PAN is masked by default and returned only for single-use virtual cards.
  name: number
  type: string
- description: 'Allocates a specific product range for either a physical or a virtual card. Possible values: **fullySupported**, **secureCorporate**. >Reach out to your Adyen contact to get the values relevant for yo'
  name: threeDSecure
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-card-schema.json
slug: configuration-card
tags:
- Payments
- Financial Services
- Fintech
title: Card
---
