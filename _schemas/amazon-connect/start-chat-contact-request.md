---
description: StartChatContactRequest schema from Amazon Connect Service API
layout: schema
name: StartChatContactRequest
properties_list:
- description: The identifier of the Amazon Connect instance.
  name: InstanceId
  type: string
- description: The identifier of the contact flow for initiating the chat.
  name: ContactFlowId
  type: string
- description: A custom key-value pair using an attribute map.
  name: Attributes
  type: object
- description: ''
  name: ParticipantDetails
  type: object
- description: ''
  name: InitialMessage
  type: object
- description: Idempotency token.
  name: ClientToken
  type: string
- description: The total duration of the newly started chat session.
  name: ChatDurationInMinutes
  type: integer
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/start-chat-contact-request-schema.json
slug: start-chat-contact-request
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: StartChatContactRequest
---
