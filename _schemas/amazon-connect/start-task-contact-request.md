---
description: StartTaskContactRequest schema from Amazon Connect Service API
layout: schema
name: StartTaskContactRequest
properties_list:
- description: The identifier of the Amazon Connect instance.
  name: InstanceId
  type: string
- description: The identifier of the previous chat, voice, or task contact.
  name: PreviousContactId
  type: string
- description: The identifier of the contact flow for initiating the tasks.
  name: ContactFlowId
  type: string
- description: ''
  name: Attributes
  type: object
- description: The name of a task that is shown to an agent in the Contact Control Panel (CCP).
  name: Name
  type: string
- description: ''
  name: References
  type: object
- description: A description of the task that is shown to an agent in the Contact Control Panel.
  name: Description
  type: string
- description: ''
  name: ClientToken
  type: string
- description: ''
  name: ScheduledTime
  type: string
- description: ''
  name: TaskTemplateId
  type: string
- description: ''
  name: QuickConnectId
  type: string
- description: ''
  name: RelatedContactId
  type: string
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/start-task-contact-request-schema.json
slug: start-task-contact-request
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: StartTaskContactRequest
---
