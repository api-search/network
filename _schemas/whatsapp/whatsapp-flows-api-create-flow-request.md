---
description: CreateFlowRequest from WhatsApp API
layout: schema
name: CreateFlowRequest
properties_list:
- description: Flow display name
  name: name
  type: string
- description: ''
  name: categories
  type: array
- description: ID of existing flow to clone
  name: clone_flow_id
  type: string
- description: HTTPS endpoint for data exchange
  name: endpoint_uri
  type: string
provider_name: WhatsApp
provider_slug: whatsapp
schema_file: json-schema/whatsapp-flows-api-create-flow-request-schema.json
slug: whatsapp-flows-api-create-flow-request
tags: []
title: CreateFlowRequest
---
