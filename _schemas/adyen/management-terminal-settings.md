---
description: TerminalSettings schema from Adyen API
layout: schema
name: TerminalSettings
properties_list:
- description: Settings to define the header of the shopper receipt.
  name: cardholderReceipt
  type: object
- description: Settings for terminal connectivity features.
  name: connectivity
  type: object
- description: Settings for tipping with or without predefined options to choose from. The maximum number of predefined options is four, or three plus the option to enter a custom tip.
  name: gratuities
  type: array
- description: Settings for terminal hardware features.
  name: hardware
  type: object
- description: Settings for localization.
  name: localization
  type: object
- description: Settings for a Terminal API integration.
  name: nexo
  type: object
- description: Settings for [offline payment](https://docs.adyen.com/point-of-sale/offline-payments) features.
  name: offlineProcessing
  type: object
- description: Settings for an Oracle Payment Interface (OPI) integration.
  name: opi
  type: object
- description: Settings for [passcodes](https://docs.adyen.com/point-of-sale/managing-terminals/menu-access?tab=manage_passcodes_with_an_api_call_2#manage-passcodes) features.
  name: passcodes
  type: object
- description: Settings for [Pay-at-table](https://docs.adyen.com/point-of-sale/pay-at-x) features.
  name: payAtTable
  type: object
- description: Settings for payment features.
  name: payment
  type: object
- description: Generic receipt settings.
  name: receiptOptions
  type: object
- description: Transaction outcomes that you want the terminal to print a merchant receipt or a shopper receipt for.
  name: receiptPrinting
  type: object
- description: Settings for refunds.
  name: refunds
  type: object
- description: Settings to skip signature, sign on display, or sign on receipt.
  name: signature
  type: object
- description: Settings for [standalone](https://docs.adyen.com/point-of-sale/standalone/standalone-build/set-up-standalone#set-up-standalone-using-an-api-call) features.
  name: standalone
  type: object
- description: Settings for payment [surcharge](https://docs.adyen.com/point-of-sale/surcharge) features.
  name: surcharge
  type: object
- description: Settings for Tap to Pay.
  name: tapToPay
  type: object
- description: Settings for device [time-outs](https://docs.adyen.com/point-of-sale/pos-timeouts#device-time-out).
  name: timeouts
  type: object
- description: Remote Wi-Fi profiles for WPA and WPA2 PSK and EAP Wi-Fi networks.
  name: wifiProfiles
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-terminal-settings-schema.json
slug: management-terminal-settings
tags:
- Payments
- Financial Services
- Fintech
title: TerminalSettings
---
