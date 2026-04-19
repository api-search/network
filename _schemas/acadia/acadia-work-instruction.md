---
description: A digital work instruction document
layout: schema
name: WorkInstruction
properties_list:
- description: Unique work instruction identifier
  name: id
  type: string
- description: Title of the work instruction
  name: title
  type: string
- description: Publication status
  name: status
  type: string
- description: Category or department the instruction belongs to
  name: category
  type: string
- description: Version number of the work instruction
  name: version
  type: integer
- description: Description of the work instruction purpose
  name: description
  type: string
- description: Ordered steps in the work instruction
  name: steps
  type: array
- description: Timestamp when the instruction was created
  name: createdAt
  type: string
- description: Timestamp of last update
  name: updatedAt
  type: string
provider_name: Acadia
provider_slug: acadia
schema_file: json-schema/acadia-work-instruction-schema.json
slug: acadia-work-instruction
tags:
- Connected Worker
- Knowledge Management
- Manufacturing
- Skills Management
- Training
- Workforce Development
title: WorkInstruction
---
