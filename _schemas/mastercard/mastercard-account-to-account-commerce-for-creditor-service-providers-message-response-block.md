---
description: ''
layout: schema
name: MessageResponseBlock
properties_list:
- description: Unique identifier of the message sender.
  name: initiatingPartyId
  type: string
- description: A point-to-point unique identifier is assigned to every message by the message initiator.
  name: messageId
  type: string
- description: ISO 8601 format date and time in Coordinated Universal Time (UTC) when this message was created.
  name: creationDateTime
  type: string
- description: Original message identifier generated and sent by the initiator of the request message.
  name: originalMessageId
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-account-to-account-commerce-for-creditor-service-providers-message-response-block-schema.json
slug: mastercard-account-to-account-commerce-for-creditor-service-providers-message-response-block
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: MessageResponseBlock
---
