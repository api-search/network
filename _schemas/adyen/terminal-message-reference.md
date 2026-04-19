---
description: To abort a transaction in progress or to request the status of a transaction from which no response has been received. It identifies the message header of the message request to abort or request the status. Identification of a previous POI transaction.
layout: schema
name: MessageReference
properties_list:
- description: ''
  name: MessageCategory
  type: object
- description: Identification of a message pair, which processes a transaction.
  name: ServiceID
  type: string
- description: Identification of a device message pair.
  name: DeviceID
  type: string
- description: default MessageHeader.SaleID.
  name: SaleID
  type: string
- description: default MessageHeader.POIID.
  name: POIID
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-message-reference-schema.json
slug: terminal-message-reference
tags:
- Payments
- Financial Services
- Fintech
title: MessageReference
---
