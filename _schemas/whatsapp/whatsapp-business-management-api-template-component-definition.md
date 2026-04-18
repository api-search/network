---
description: TemplateComponentDefinition from WhatsApp API
layout: schema
name: TemplateComponentDefinition
properties_list:
- description: ''
  name: type
  type: string
- description: Header format type
  name: format
  type: string
- description: Component text content
  name: text
  type: string
- description: Example values for variables
  name: example
  type: object
- description: ''
  name: buttons
  type: array
- description: Authentication templates only
  name: add_security_recommendation
  type: boolean
- description: Authentication templates only (1-90)
  name: code_expiration_minutes
  type: integer
provider_name: WhatsApp
provider_slug: whatsapp
schema_file: json-schema/whatsapp-business-management-api-template-component-definition-schema.json
slug: whatsapp-business-management-api-template-component-definition
tags: []
title: TemplateComponentDefinition
---
