---
description: CardInfo schema from Adyen API
layout: schema
name: CardInfo
properties_list:
- description: Contains the card user's password and mobile phone number. This is required when you issue cards that can be used to make online payments within the EEA and the UK, or can be added to digital wallets.
  name: authentication
  type: object
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
- description: The delivery contact (name and address) for physical card delivery.
  name: deliveryContact
  type: object
- description: 'The form factor of the card. Possible values: **virtual**, **physical**.'
  name: formFactor
  type: string
- description: 'Allocates a specific product range for either a physical or a virtual card. Possible values: **fullySupported**, **secureCorporate**. >Reach out to your Adyen contact to get the values relevant for yo'
  name: threeDSecure
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-card-info-schema.json
slug: configuration-card-info
tags:
- Payments
- Financial Services
- Fintech
title: CardInfo
---
