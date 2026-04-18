---
description: ''
layout: schema
name: ExtensionAttributes
properties_list:
- description: The unique name of the extension.
  name: name
  type: string
- description: The human-readable display name.
  name: display_name
  type: string
- description: The version of the installed extension.
  name: version
  type: string
- description: The descriptor ID for the extension configuration.
  name: delegate_descriptor_id
  type: string
- description: A JSON-encoded string of configuration settings.
  name: settings
  type: string
- description: Whether the extension is enabled.
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
  name: deleted_at
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Adobe Launch
provider_slug: adobe-launch
schema_file: json-schema/extension-extension-attributes-schema.json
slug: extension-extension-attributes
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: ExtensionAttributes
---
