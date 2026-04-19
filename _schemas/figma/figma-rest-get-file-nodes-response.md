---
description: Response from the Get File Nodes endpoint.
layout: schema
name: GetFileNodesResponse
properties_list:
- description: The name of the file.
  name: name
  type: string
- description: ''
  name: lastModified
  type: string
- description: ''
  name: version
  type: string
- description: ''
  name: role
  type: string
- description: A mapping from node IDs to node data. Each value contains a document subtree and optionally the component metadata for that node.
  name: nodes
  type: object
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-get-file-nodes-response-schema.json
slug: figma-rest-get-file-nodes-response
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: GetFileNodesResponse
---
