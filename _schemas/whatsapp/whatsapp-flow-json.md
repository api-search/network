---
description: Schema for WhatsApp Flow JSON definitions uploaded via the Flows API. Defines the UI screens, components, and navigation logic for interactive flows within WhatsApp conversations.
layout: schema
name: WhatsApp Flow JSON
properties_list:
- description: Flow JSON schema version (e.g., '7.0')
  name: version
  type: string
- description: Data exchange protocol version (e.g., '3.0')
  name: data_api_version
  type: string
- description: Screen transition rules
  name: routing_model
  type: object
- description: ''
  name: screens
  type: array
provider_name: WhatsApp
provider_slug: whatsapp
schema_file: json-schema/whatsapp-flow-json-schema.json
slug: whatsapp-flow-json
tags: []
title: WhatsApp Flow JSON
---
