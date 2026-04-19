---
description: Request body for creating a BDD scenario
layout: schema
name: CreateScenarioRequest
properties_list:
- description: ID of the parent user story
  name: storyId
  type: string
- description: ID of the linked acceptance criterion
  name: criterionId
  type: string
- description: Scenario title
  name: title
  type: string
- description: Feature file path
  name: featureFile
  type: string
- description: Full Gherkin scenario text
  name: gherkin
  type: string
provider_name: Acceptance Criteria
provider_slug: acceptance-criteria
schema_file: json-schema/acceptance-criteria-management-create-scenario-request-schema.json
slug: acceptance-criteria-management-create-scenario-request
tags:
- Agile
- Behavior Driven Development
- Gherkin
- Quality Assurance
- Requirements
- Testing
- User Stories
title: CreateScenarioRequest
---
