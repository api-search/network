---
description: It conveys Information related to the Sale to POI protocol management. Message header of the Sale to POI protocol message.
layout: schema
name: MessageHeader
properties_list:
- description: If MessageCategory is Login or Diagnosis.
  name: ProtocolVersion
  type: string
- description: ''
  name: MessageClass
  type: object
- description: ''
  name: MessageCategory
  type: object
- description: ''
  name: MessageType
  type: object
- description: Required if Service or Event MessageClass message or if Device MessageClass and request from POI or response from Sale.
  name: ServiceID
  type: string
- description: If Device MessageClass.
  name: DeviceID
  type: string
- description: Identification of a Sale System or a Sale Terminal for the Sale to POI protocol.
  name: SaleID
  type: string
- description: Identification of a POI System or a POI Terminal for the Sale to POI protocol.
  name: POIID
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-message-header-schema.json
slug: terminal-message-header
tags:
- Payments
- Financial Services
- Fintech
title: MessageHeader
---
