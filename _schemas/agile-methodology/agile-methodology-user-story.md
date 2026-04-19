---
description: A user story representing a feature or requirement from the perspective of an end user in agile methodology.
layout: schema
name: UserStory
properties_list:
- description: Unique identifier for the user story.
  name: id
  type: string
- description: Short summary of the user story.
  name: title
  type: string
- description: 'Full user story in the format: As a [role], I want [feature], so that [benefit].'
  name: description
  type: string
- description: List of acceptance criteria that must be met for the story to be considered done.
  name: acceptance_criteria
  type: array
- description: Relative effort estimate for completing the user story.
  name: story_points
  type: integer
- description: ''
  name: priority
  type: string
- description: ''
  name: status
  type: string
provider_name: Agile Methodology
provider_slug: agile-methodology
schema_file: json-schema/agile-methodology-user-story-schema.json
slug: agile-methodology-user-story
tags:
- Agile Methodology
- Kanban
- Project Management
- Scrum
- Software Development
- SAFe
- XP
title: UserStory
---
