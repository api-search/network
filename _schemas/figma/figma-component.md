---
description: A published component from a Figma team or file library. Published components are reusable design elements that can be shared across files and teams. This schema represents components as returned by the component endpoints of the Figma REST API.
layout: schema
name: Figma Published Component
properties_list:
- description: The globally unique identifier for the component. This key is stable across file versions and can be used to reference the component via the GET /v1/components/{key} endpoint.
  name: key
  type: string
- description: The unique identifier of the Figma file that contains this component.
  name: file_key
  type: string
- description: The unique identifier of the component node within the Figma file. The node_id combined with file_key can be used to construct a direct URL to the component.
  name: node_id
  type: string
- description: A URL to a thumbnail image of the component. Thumbnail URLs are temporary and expire after a period of time.
  name: thumbnail_url
  type: string
- description: The name of the component as it appears in the assets panel and library.
  name: name
  type: string
- description: The description of the component as entered by the publisher. Useful for documenting usage guidelines and design intent.
  name: description
  type: string
- description: The UTC ISO 8601 time when the component was first published to the library.
  name: created_at
  type: string
- description: The UTC ISO 8601 time when the component was last updated in the library.
  name: updated_at
  type: string
- description: ''
  name: user
  type: object
- description: ''
  name: containing_frame
  type: object
- description: If this component belongs to a component set (variant group), this is the ID of that component set.
  name: component_set_id
  type:
  - string
  - 'null'
- description: An array of documentation links attached to this component, providing external references to code, design specs, or other resources.
  name: documentation_links
  type: array
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-component-schema.json
slug: figma-component
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: Figma Published Component
---
