---
description: A rule in Adobe Experience Platform Tags controls resource behavior through a combination of events (triggers), conditions (criteria), and actions (executions). A rule belongs to exactly one property, and a property can have many rules. Rules are composed of rule components that define the specific logic.
layout: schema
name: Adobe Experience Platform Tags Rule
properties_list:
- description: The unique identifier for the rule.
  name: id
  type: string
- description: The resource type identifier.
  name: type
  type: string
- description: ''
  name: attributes
  type: object
- description: Related resources linked to this rule.
  name: relationships
  type: object
- description: ''
  name: links
  type: object
provider_name: Adobe Launch
provider_slug: adobe-launch
schema_file: json-schema/rule.json
slug: rule
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: Adobe Experience Platform Tags Rule
---
