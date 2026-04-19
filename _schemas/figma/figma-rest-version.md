---
description: A recorded version in the file's version history.
layout: schema
name: Version
properties_list:
- description: Unique identifier for the version.
  name: id
  type: string
- description: The UTC ISO 8601 time at which the version was created.
  name: created_at
  type: string
- description: The label given to the version in the editor.
  name: label
  type: '[''string'', ''null'']'
- description: The description of the version as entered in the editor.
  name: description
  type: '[''string'', ''null'']'
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-version-schema.json
slug: figma-rest-version
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
