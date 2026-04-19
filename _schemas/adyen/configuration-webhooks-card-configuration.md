---
description: CardConfiguration schema from Adyen API
layout: schema
name: CardConfiguration
properties_list:
- description: Overrides the activation label design ID defined in the `configurationProfileId`. The activation label is attached to the card and contains the activation instructions.
  name: activation
  type: string
- description: Your app's URL, if you want to activate cards through your app. For example, **my-app://ref1236a7d**. A QR code is created based on this URL, and is included in the carrier. Before you use this field,
  name: activationUrl
  type: string
- description: Overrides the shipment bulk address defined in the `configurationProfileId`.
  name: bulkAddress
  type: object
- description: The ID of the card image. This is the image that will be printed on the full front of the card.
  name: cardImageId
  type: string
- description: Overrides the carrier design ID defined in the `configurationProfileId`. The carrier is the letter or packaging to which the card is attached.
  name: carrier
  type: string
- description: The ID of the carrier image. This is the image that will printed on the letter to which the card is attached.
  name: carrierImageId
  type: string
- description: The ID of the card configuration profile that contains the settings of the card. For example, the envelope and PIN mailer designs or the logistics company handling the shipment. All the settings in th
  name: configurationProfileId
  type: string
- description: The three-letter [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217) currency code of the card. For example, **EUR**.
  name: currency
  type: string
- description: Overrides the envelope design ID defined in the `configurationProfileId`.
  name: envelope
  type: string
- description: Overrides the insert design ID defined in the `configurationProfileId`. An insert is any additional material, such as marketing materials, that are shipped together with the card.
  name: insert
  type: string
- description: The two-letter [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code of the card. For example, **en**.
  name: language
  type: string
- description: The ID of the logo image. This is the image that will be printed on the partial front of the card, such as a logo on the upper right corner.
  name: logoImageId
  type: string
- description: Overrides the PIN mailer design ID defined in the `configurationProfileId`. The PIN mailer is the letter on which the PIN is printed.
  name: pinMailer
  type: string
- description: Overrides the logistics company defined in the `configurationProfileId`.
  name: shipmentMethod
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-webhooks-card-configuration-schema.json
slug: configuration-webhooks-card-configuration
tags:
- Payments
- Financial Services
- Fintech
title: CardConfiguration
---
