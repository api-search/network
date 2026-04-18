---
description: ''
layout: schema
name: DataElementAttributes
properties_list:
- description: The human-readable name of the data element.
  name: name
  type: string
- description: The descriptor ID identifying the data element type from an extension.
  name: delegate_descriptor_id
  type: string
- description: The default value when the data element returns no value.
  name: default_value
  type: string
- description: A JSON-encoded string of settings for the data element.
  name: settings
  type: string
- description: How long the data element value persists.
  name: storage_duration
  type: string
- description: Whether to force the value to lowercase.
  name: force_lower_case
  type: boolean
- description: Whether to clean whitespace from the value.
  name: clean_text
  type: boolean
- description: Whether the data element is enabled.
  name: enabled
  type: boolean
- description: ''
  name: published
  type: boolean
- description: ''
  name: dirty
  type: boolean
- description: ''
  name: revision_number
  type: integer
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Adobe Launch
provider_slug: adobe-launch
schema_file: json-schema/reactor-data-element-attributes-schema.json
slug: reactor-data-element-attributes
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: DataElementAttributes
---
