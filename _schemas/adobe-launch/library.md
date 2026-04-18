---
description: A library is a collection of tag resources (extensions, rules, and data elements) that are compiled together into a build for deployment. Libraries follow a publishing workflow from development through staging to production, and serve as the mechanism for testing and deploying tag configurations.
layout: schema
name: Adobe Experience Platform Tags Library
properties_list:
- description: The unique identifier for the library.
  name: id
  type: string
- description: The resource type identifier.
  name: type
  type: string
- description: ''
  name: attributes
  type: object
- description: Related resources linked to this library.
  name: relationships
  type: object
- description: ''
  name: links
  type: object
- description: Metadata for library state transitions.
  name: meta
  type: object
provider_name: Adobe Launch
provider_slug: adobe-launch
schema_file: json-schema/library.json
slug: library
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: Adobe Experience Platform Tags Library
---
