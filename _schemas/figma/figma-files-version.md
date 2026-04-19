---
description: A version of a file.
layout: schema
name: Version
properties_list:
- description: Unique identifier for version.
  name: id
  type: string
- description: The UTC ISO 8601 time at which the version was created.
  name: createdAt
  type: string
- description: The label given to the version in the editor.
  name: label
  type: '[''string'', ''null'']'
- description: The description of the version as entered in the editor.
  name: description
  type: '[''string'', ''null'']'
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-files-version-schema.json
slug: figma-files-version
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: Version
---
