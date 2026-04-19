---
description: 'Array of field paths specifying which fields to update. Uses dot notation for nested fields (e.g., "config.revision", "metadata.tags"). **Field Path Rules:** - Use dot notation for nested objects: `parent.child.field` - Escape special characters: `field\.with\.dots`, `field\:with\:colons` - Array elements not directly addressable - Object names can be specified directly (e.g., "config.content.read.objects.contacts") - The * operator in paths like "config.content.read.objects.*" allows you to specify any object name - Example: "config.content.read.objects.*" pattern allows "config.content.read.objects.contacts", "config.content.read.objects.leads", etc.'
layout: schema
name: UpdateMask
properties_list: []
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-update-mask-schema.json
slug: ampersand-api-update-mask
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: UpdateMask
---
