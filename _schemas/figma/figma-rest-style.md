---
description: A published style that can be applied to nodes in Figma.
layout: schema
name: Style
properties_list:
- description: The globally unique key of the style.
  name: key
  type: string
- description: Name of the style.
  name: name
  type: string
- description: Description of the style.
  name: description
  type: string
- description: Whether this style is a remote style from an external library.
  name: remote
  type: boolean
- description: The type of style.
  name: style_type
  type: string
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-style-schema.json
slug: figma-rest-style
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: Style
---
