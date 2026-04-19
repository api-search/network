---
description: It contains the result of the requested service, APDU response sent by the chip of the card in response to the APDU request. Content of the Card Reader APDU Response message.
layout: schema
name: CardReaderAPDUResponse
properties_list:
- description: ''
  name: Response
  type: object
- description: Data field of the APDU command (Lc + Data).
  name: APDUData
  type: string
- description: Status of a smartcard response to a command (SW1-SW2).
  name: CardStatusWords
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-card-reader-apdu-response-schema.json
slug: terminal-card-reader-apdu-response
tags:
- Payments
- Financial Services
- Fintech
title: CardReaderAPDUResponse
---
