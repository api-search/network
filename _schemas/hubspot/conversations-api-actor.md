---
description: Represents a participant in a conversation (visitor, agent, or bot).
layout: schema
name: Actor
properties_list:
- description: Unique identifier for the actor
  name: id
  type: string
- description: Actor ID reference
  name: actorId
  type: string
- description: Display name of the actor
  name: name
  type: string
- description: Email address of the actor
  name: email
  type: string
- description: Type of actor (e.g., VISITOR, AGENT, BOT)
  name: type
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/conversations-api-actor-schema.json
slug: conversations-api-actor
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
title: Actor
---
