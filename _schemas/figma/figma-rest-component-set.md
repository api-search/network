---
description: A component set groups variants of a component together. Useful for organizing different states or configurations of a design element.
layout: schema
name: ComponentSet
properties_list:
- description: The globally unique key of the component set.
  name: key
  type: string
- description: Name of the component set.
  name: name
  type: string
- description: The description of the component set as entered in the editor.
  name: description
  type: string
- description: Documentation links attached to this component set.
  name: documentationLinks
  type: array
- description: Whether this is a remote component set.
  name: remote
  type: boolean
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-component-set-schema.json
slug: figma-rest-component-set
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: ComponentSet
---
