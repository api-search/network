---
description: Contains information about a contact.
layout: schema
name: Contact
properties_list:
- description: The Amazon Resource Name (ARN) for the contact.
  name: Arn
  type: string
- description: The identifier for the contact.
  name: Id
  type: string
- description: If this contact is related to other contacts, this is the ID of the initial contact.
  name: InitialContactId
  type: string
- description: If this contact is not the first contact, this is the ID of the previous contact.
  name: PreviousContactId
  type: string
- description: How the contact reached your contact center.
  name: Channel
  type: string
- description: ''
  name: QueueInfo
  type: object
- description: ''
  name: AgentInfo
  type: object
- description: Indicates how the contact was initiated.
  name: InitiationMethod
  type: string
- description: The date and time this contact was initiated.
  name: InitiationTimestamp
  type: string
- description: The timestamp when the customer endpoint disconnected from Amazon Connect.
  name: DisconnectTimestamp
  type: string
- description: The timestamp when contact was last updated.
  name: LastUpdateTimestamp
  type: string
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/contact-schema.json
slug: contact
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: Contact
---
