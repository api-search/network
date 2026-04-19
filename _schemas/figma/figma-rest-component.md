---
description: Metadata about a main component in a Figma file. Components are reusable design elements.
layout: schema
name: Component
properties_list:
- description: The globally unique key of the component.
  name: key
  type: string
- description: Name of the component.
  name: name
  type: string
- description: The description of the component as entered in the editor.
  name: description
  type: string
- description: The ID of the component set this component belongs to, if any.
  name: componentSetId
  type: '[''string'', ''null'']'
- description: An array of documentation links attached to this component.
  name: documentationLinks
  type: array
- description: Whether this component is a remote component that was pulled from an external library.
  name: remote
  type: boolean
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-component-schema.json
slug: figma-rest-component
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
