---
description: Paginated list of BDD scenarios
layout: schema
name: ScenarioList
properties_list:
- description: Total number of scenarios matching the query
  name: total
  type: integer
- description: Current page number
  name: page
  type: integer
- description: Number of items per page
  name: pageSize
  type: integer
- description: Array of scenario objects
  name: scenarios
  type: array
provider_name: Acceptance Criteria
provider_slug: acceptance-criteria
schema_file: json-schema/acceptance-criteria-management-scenario-list-schema.json
slug: acceptance-criteria-management-scenario-list
tags:
- Agile
- Behavior Driven Development
- Gherkin
- Quality Assurance
- Requirements
- Testing
- User Stories
title: ScenarioList
---
