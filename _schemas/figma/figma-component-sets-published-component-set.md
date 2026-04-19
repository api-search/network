---
description: A node containing a set of variants of a component.
layout: schema
name: PublishedComponentSet
properties_list:
- description: The unique identifier for the component set.
  name: key
  type: string
- description: The unique identifier of the Figma file that contains the component set.
  name: fileKey
  type: string
- description: The unique identifier of the component set node within the Figma file.
  name: nodeId
  type: string
- description: A URL to a thumbnail image of the component set.
  name: thumbnailUrl
  type: string
- description: The name of the component set.
  name: name
  type: string
- description: The description of the component set as entered by the publisher.
  name: description
  type: string
- description: The UTC ISO 8601 time when the component set was created.
  name: createdAt
  type: string
- description: The UTC ISO 8601 time when the component set was last updated.
  name: updatedAt
  type: string
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-component-sets-published-component-set-schema.json
slug: figma-component-sets-published-component-set
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
