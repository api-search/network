---
description: Contains summary information about a contact.
layout: schema
name: ContactSummary
properties_list:
- description: The identifier of the contact.
  name: Id
  type: string
- description: The ARN of the contact.
  name: Arn
  type: string
- description: How the contact reached your contact center.
  name: Channel
  type: string
- description: Indicates how the contact was initiated.
  name: InitiationMethod
  type: string
- description: ''
  name: InitiationTimestamp
  type: string
- description: ''
  name: DisconnectTimestamp
  type: string
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/contact-summary-schema.json
slug: contact-summary
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: ContactSummary
---
