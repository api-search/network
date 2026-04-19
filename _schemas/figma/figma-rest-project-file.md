---
description: A file within a Figma project.
layout: schema
name: ProjectFile
properties_list:
- description: The file key.
  name: key
  type: string
- description: The name of the file.
  name: name
  type: string
- description: A URL to a thumbnail image of the file.
  name: thumbnail_url
  type: string
- description: The UTC ISO 8601 time at which the file was last modified.
  name: last_modified
  type: string
- description: Branches of this file, if branch_data was requested.
  name: branches
  type: array
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-project-file-schema.json
slug: figma-rest-project-file
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: ProjectFile
---
