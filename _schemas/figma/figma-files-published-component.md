---
description: An arrangement of published UI elements.
layout: schema
name: PublishedComponent
properties_list:
- description: The unique identifier for the component.
  name: key
  type: string
- description: The unique identifier of the Figma file that contains the component.
  name: fileKey
  type: string
- description: The unique identifier of the component node within the Figma file.
  name: nodeId
  type: string
- description: A URL to a thumbnail image of the component.
  name: thumbnailUrl
  type: string
- description: The name of the component.
  name: name
  type: string
- description: The description of the component as entered by the publisher.
  name: description
  type: string
- description: The UTC ISO 8601 time when the component was created.
  name: createdAt
  type: string
- description: The UTC ISO 8601 time when the component was last updated.
  name: updatedAt
  type: string
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-files-published-component-schema.json
slug: figma-files-published-component
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
