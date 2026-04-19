---
description: A user story representing a feature or requirement from the perspective of an end user
layout: schema
name: UserStory
properties_list:
- description: Unique identifier for the user story
  name: id
  type: string
- description: Short title summarizing the user story (As a... I want... So that...)
  name: title
  type: string
- description: Full user story narrative including role, goal, and benefit
  name: description
  type: string
- description: Current lifecycle status of the user story
  name: status
  type: string
- description: Priority level of the user story
  name: priority
  type: string
- description: Effort estimate in story points
  name: storyPoints
  type: integer
- description: List of acceptance criteria that define done for this story
  name: acceptanceCriteria
  type: array
- description: Labels or tags associated with the story
  name: tags
  type: array
- description: Username or ID of the person assigned to this story
  name: assignee
  type: string
- description: Timestamp when the user story was created
  name: createdAt
  type: string
- description: Timestamp when the user story was last updated
  name: updatedAt
  type: string
provider_name: Acceptance Criteria
provider_slug: acceptance-criteria
schema_file: json-schema/acceptance-criteria-management-user-story-schema.json
slug: acceptance-criteria-management-user-story
tags:
- Agile
- Behavior Driven Development
- Gherkin
- Quality Assurance
- Requirements
- Testing
- User Stories
title: UserStory
---
