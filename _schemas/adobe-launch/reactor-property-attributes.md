---
description: ''
layout: schema
name: PropertyAttributes
properties_list:
- description: The name of the property.
  name: name
  type: string
- description: The platform type (web, mobile, or edge).
  name: platform
  type: string
- description: A list of domains associated with the property.
  name: domains
  type: array
- description: Whether the property is enabled.
  name: enabled
  type: boolean
- description: Whether the property is in development mode.
  name: development
  type: boolean
- description: The default privacy setting.
  name: privacy
  type: string
- description: Whether SSL is enabled.
  name: ssl_enabled
  type: boolean
- description: Whether rule component sequencing is enabled.
  name: rule_component_sequencing_enabled
  type: boolean
- description: Whether undefined data element variables return empty strings.
  name: undefined_vars_return_empty
  type: boolean
- description: A unique token for the property.
  name: token
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Adobe Launch
provider_slug: adobe-launch
schema_file: json-schema/reactor-property-attributes-schema.json
slug: reactor-property-attributes
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: PropertyAttributes
---
