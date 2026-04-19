---
description: A description of a main component.
layout: schema
name: Component
properties_list:
- description: The key of the component.
  name: key
  type: string
- description: Name of the component.
  name: name
  type: string
- description: The description of the component as entered in the editor.
  name: description
  type: string
- description: The ID of the component set if the component belongs to one.
  name: componentSetId
  type: string
- description: An array of documentation links attached to this component.
  name: documentationLinks
  type: array
- description: Whether this component is a remote component.
  name: remote
  type: boolean
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-files-component-schema.json
slug: figma-files-component
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: Component
---
