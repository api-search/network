---
description: An external reference attached to a Planner task
layout: schema
name: PlannerExternalReference
properties_list:
- description: ''
  name: '@odata.type'
  type: string
- description: A name alias for the reference
  name: alias
  type: string
- description: The date and time the reference was last modified
  name: lastModifiedDateTime
  type: string
- description: Hint used to set the relative priority order in which the reference will be shown as a preview on the task
  name: previewPriority
  type: string
- description: The type of the reference (e.g., PowerPoint, Word, Excel, Other)
  name: type
  type: string
provider_name: Microsoft Planner
provider_slug: microsoft-planner
schema_file: json-schema/microsoft-planner-planner-external-reference-schema.json
slug: microsoft-planner-planner-external-reference
tags:
- Collaboration
- Microsoft 365
- Productivity
- Project Management
- Task Management
title: PlannerExternalReference
---
