---
description: It contains the APDU request to send to the chip of the card, and a possible invitation message to display on the CashierInterface or the CustomerInterface. Content of the Card Reader APDU Request message.
layout: schema
name: CardReaderAPDURequest
properties_list:
- description: Class field of the APDU command (CLA).
  name: APDUClass
  type: string
- description: Instruction field of the APDU command (INS).
  name: APDUInstruction
  type: string
- description: Parameter 1 field of the APDU command (P1).
  name: APDUPar1
  type: string
- description: Parameter 2 field of the APDU command(P2).
  name: APDUPar2
  type: string
- description: Data field of the APDU command (Lc + Data).
  name: APDUData
  type: string
- description: Expected length of the data field of the APDU response to the command (Le).
  name: APDUExpectedLength
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-card-reader-apdu-request-schema.json
slug: terminal-card-reader-apdu-request
tags:
- Payments
- Financial Services
- Fintech
title: CardReaderAPDURequest
---
