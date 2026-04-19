---
description: ''
layout: schema
name: GetFileResponseBody
properties_list:
- description: The name of the file as it appears in the editor.
  name: name
  type: string
- description: The role of the user making the API request in relation to the file.
  name: role
  type: string
- description: The UTC ISO 8601 time at which the file was last modified.
  name: lastModified
  type: string
- description: The type of editor associated with this file.
  name: editorType
  type: string
- description: A URL to a thumbnail image of the file.
  name: thumbnailUrl
  type: string
- description: The version number of the file.
  name: version
  type: string
- description: A mapping from component IDs to component metadata.
  name: components
  type: object
- description: A mapping from component set IDs to component set metadata.
  name: componentSets
  type: object
- description: The version of the file schema that this file uses.
  name: schemaVersion
  type: number
- description: A mapping from style IDs to style metadata.
  name: styles
  type: object
- description: The key of the main file for this file.
  name: mainFileKey
  type: string
- description: A list of branches for this file.
  name: branches
  type: array
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-files-get-file-response-body-schema.json
slug: figma-files-get-file-response-body
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: GetFileResponseBody
---
