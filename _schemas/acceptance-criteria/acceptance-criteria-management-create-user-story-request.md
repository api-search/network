---
description: Request body for creating a new user story
layout: schema
name: CreateUserStoryRequest
properties_list:
- description: Short title for the user story
  name: title
  type: string
- description: Full user story narrative
  name: description
  type: string
- description: Priority level
  name: priority
  type: string
- description: Effort estimate in story points
  name: storyPoints
  type: integer
- description: Labels or tags
  name: tags
  type: array
- description: Assignee username or ID
  name: assignee
  type: string
provider_name: Acceptance Criteria
provider_slug: acceptance-criteria
schema_file: json-schema/acceptance-criteria-management-create-user-story-request-schema.json
slug: acceptance-criteria-management-create-user-story-request
tags:
- Agile
- Behavior Driven Development
- Gherkin
- Quality Assurance
- Requirements
- Testing
- User Stories
title: CreateUserStoryRequest
---
