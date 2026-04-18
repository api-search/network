---
description: CreateTemplateRequest from WhatsApp API
layout: schema
name: CreateTemplateRequest
properties_list:
- description: Template name (lowercase, underscores only, max 512 chars)
  name: name
  type: string
- description: Language code
  name: language
  type: string
- description: ''
  name: category
  type: string
- description: ''
  name: components
  type: array
- description: ''
  name: parameter_format
  type: string
provider_name: WhatsApp
provider_slug: whatsapp
schema_file: json-schema/whatsapp-business-management-api-create-template-request-schema.json
slug: whatsapp-business-management-api-create-template-request
tags: []
title: CreateTemplateRequest
---
