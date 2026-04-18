---
description: Custom field schema from Microsoft Project Online REST API
layout: schema
name: CustomField
properties_list:
- description: Custom field identifier
  name: Id
  type: string
- description: Internal name of the custom field
  name: InternalName
  type: string
- description: Display name of the custom field
  name: Name
  type: string
- description: Field data type (0=Cost, 1=Date, 2=Duration, 3=Finish, 4=Flag, 5=Number, 6=Start, 7=Text)
  name: FieldType
  type: integer
- description: Entity type (0=Project, 1=Resource, 2=Task)
  name: EntityType
  type: integer
- description: Field description
  name: Description
  type: string
- description: Associated lookup table ID
  name: LookupTableId
  type: string
- description: Whether the field is required
  name: IsRequired
  type: boolean
- description: Whether the text field supports multiple lines
  name: IsMultilineText
  type: boolean
- description: Calculated field formula
  name: Formula
  type: string
provider_name: Microsoft Project
provider_slug: microsoft-project
schema_file: json-schema/rest-api-custom-field-schema.json
slug: rest-api-custom-field
tags:
- Budgeting
- Gantt Charts
- Microsoft
- Portfolio Management
- Project Management
- Resource Management
- Scheduling
- Task Management
title: CustomField
---
