---
description: Paginated list of user stories
layout: schema
name: UserStoryList
properties_list:
- description: Total number of user stories matching the query
  name: total
  type: integer
- description: Current page number
  name: page
  type: integer
- description: Number of items per page
  name: pageSize
  type: integer
- description: Array of user story objects
  name: stories
  type: array
provider_name: Acceptance Criteria
provider_slug: acceptance-criteria
schema_file: json-schema/acceptance-criteria-management-user-story-list-schema.json
slug: acceptance-criteria-management-user-story-list
tags:
- Agile
- Behavior Driven Development
- Gherkin
- Quality Assurance
- Requirements
- Testing
- User Stories
title: UserStoryList
---
