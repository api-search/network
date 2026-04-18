---
description: ''
layout: schema
name: RuleComponentAttributes
properties_list:
- description: The human-readable name of the rule component.
  name: name
  type: string
- description: The descriptor ID identifying the component type from an extension package.
  name: delegate_descriptor_id
  type: string
- description: The execution order within its type group.
  name: order
  type: integer
- description: The order relative to other components in the rule.
  name: rule_order
  type: number
- description: A JSON-encoded string of settings for the component.
  name: settings
  type: string
- description: Timeout in milliseconds for the component.
  name: timeout
  type: integer
- description: Whether to delay the next action.
  name: delay_next
  type: boolean
- description: Whether to negate the condition result.
  name: negate
  type: boolean
- description: Whether the rule component is enabled.
  name: enabled
  type: boolean
- description: ''
  name: published
  type: boolean
- description: ''
  name: dirty
  type: boolean
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Adobe Launch
provider_slug: adobe-launch
schema_file: json-schema/reactor-rule-component-attributes-schema.json
slug: reactor-rule-component-attributes
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: RuleComponentAttributes
---
