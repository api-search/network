---
description: A property in Adobe Experience Platform Tags is a container that holds most tag management resources. A property belongs to exactly one company and can have many rules, data elements, extensions, environments, and libraries. Properties are scoped to a specific platform (web, mobile, or edge).
layout: schema
name: Adobe Experience Platform Tags Property
properties_list:
- description: The unique identifier for the property.
  name: id
  type: string
- description: The resource type identifier.
  name: type
  type: string
- description: ''
  name: attributes
  type: object
- description: Related resources linked to this property.
  name: relationships
  type: object
- description: ''
  name: links
  type: object
provider_name: Adobe Launch
provider_slug: adobe-launch
schema_file: json-schema/property.json
slug: property
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: Adobe Experience Platform Tags Property
---
