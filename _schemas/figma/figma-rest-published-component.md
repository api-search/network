---
description: A published component from a team or file library.
layout: schema
name: PublishedComponent
properties_list:
- description: The globally unique identifier for the component.
  name: key
  type: string
- description: The key of the Figma file containing the component.
  name: file_key
  type: string
- description: The node ID of the component within the file.
  name: node_id
  type: string
- description: A URL to a thumbnail image of the component.
  name: thumbnail_url
  type: string
- description: The name of the component.
  name: name
  type: string
- description: The description of the component as entered by the publisher.
  name: description
  type: string
- description: The UTC ISO 8601 time when the component was first published.
  name: created_at
  type: string
- description: The UTC ISO 8601 time when the component was last updated.
  name: updated_at
  type: string
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-published-component-schema.json
slug: figma-rest-published-component
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: PublishedComponent
---
