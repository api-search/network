---
description: Project schema from Microsoft Project Online REST API
layout: schema
name: Project
properties_list:
- description: Unique identifier of the project
  name: Id
  type: string
- description: Name of the project
  name: Name
  type: string
- description: Description of the project
  name: Description
  type: string
- description: Project start date
  name: StartDate
  type: string
- description: Project finish date
  name: FinishDate
  type: string
- description: Date the project was created
  name: CreatedDate
  type: string
- description: Date the project was last modified
  name: ModifiedDate
  type: string
- description: Whether the project is currently checked out
  name: IsCheckedOut
  type: boolean
- description: User who checked out the project
  name: CheckedOutBy
  type: string
- description: Overall completion percentage
  name: PercentComplete
  type: integer
- description: Enterprise project type identifier
  name: ProjectType
  type: integer
- description: URL to the project site
  name: ProjectSiteUrl
  type: string
provider_name: Microsoft Project
provider_slug: microsoft-project
schema_file: json-schema/rest-api-project-schema.json
slug: rest-api-project
tags:
- Budgeting
- Gantt Charts
- Microsoft
- Portfolio Management
- Project Management
- Resource Management
- Scheduling
- Task Management
title: Project
---
