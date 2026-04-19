---
description: A published component set from a team or file library.
layout: schema
name: PublishedComponentSet
properties_list:
- description: The globally unique identifier for the component set.
  name: key
  type: string
- description: The key of the Figma file containing the component set.
  name: file_key
  type: string
- description: The node ID of the component set within the file.
  name: node_id
  type: string
- description: A URL to a thumbnail image of the component set.
  name: thumbnail_url
  type: string
- description: The name of the component set.
  name: name
  type: string
- description: The description of the component set.
  name: description
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-published-component-set-schema.json
slug: figma-rest-published-component-set
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: PublishedComponentSet
---
