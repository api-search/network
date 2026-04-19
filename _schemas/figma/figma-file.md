---
description: A Figma design file containing a document tree with pages, frames, components, styles, and version metadata. This schema represents the response from the GET /v1/files/{file_key} endpoint.
layout: schema
name: Figma File
properties_list:
- description: The name of the file as it appears in the Figma editor and file browser.
  name: name
  type: string
- description: The role of the user making the API request in relation to the file.
  name: role
  type: string
- description: The UTC ISO 8601 time at which the file was last modified.
  name: lastModified
  type: string
- description: The type of editor associated with this file. Figma is for design files, FigJam is for whiteboarding.
  name: editorType
  type: string
- description: A URL to a thumbnail image of the file. The URL expires after a period of time.
  name: thumbnailUrl
  type: string
- description: The current version number of the file. This changes on every save.
  name: version
  type: string
- description: ''
  name: document
  type: object
- description: A mapping from component IDs to component metadata for all components in the file.
  name: components
  type: object
- description: A mapping from component set IDs to component set metadata.
  name: componentSets
  type: object
- description: The version of the Figma file schema that this file uses.
  name: schemaVersion
  type: integer
- description: A mapping from style IDs to style metadata for all styles in the file.
  name: styles
  type: object
- description: The key of the main file. Present only when this file is a branch.
  name: mainFileKey
  type: string
- description: A list of branches for this file. Only present if branch_data was requested.
  name: branches
  type: array
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-file-schema.json
slug: figma-file
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: Figma File
---
