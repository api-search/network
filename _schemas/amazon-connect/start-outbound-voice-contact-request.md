---
description: StartOutboundVoiceContactRequest schema from Amazon Connect Service API
layout: schema
name: StartOutboundVoiceContactRequest
properties_list:
- description: The phone number of the customer, in E.164 format.
  name: DestinationPhoneNumber
  type: string
- description: The identifier of the contact flow for the outbound call.
  name: ContactFlowId
  type: string
- description: The identifier of the Amazon Connect instance.
  name: InstanceId
  type: string
- description: Idempotency token.
  name: ClientToken
  type: string
- description: The phone number associated with the Amazon Connect instance, in E.164 format.
  name: SourcePhoneNumber
  type: string
- description: The queue for the call.
  name: QueueId
  type: string
- description: ''
  name: Attributes
  type: object
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/start-outbound-voice-contact-request-schema.json
slug: start-outbound-voice-contact-request
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: StartOutboundVoiceContactRequest
---
