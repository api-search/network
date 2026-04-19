---
description: A Gherkin BDD scenario that automates verification of an acceptance criterion
layout: schema
name: Scenario
properties_list:
- description: Unique identifier for the scenario
  name: id
  type: string
- description: ID of the parent user story
  name: storyId
  type: string
- description: ID of the linked acceptance criterion
  name: criterionId
  type: string
- description: Scenario title as it appears in the feature file
  name: title
  type: string
- description: Path to the Gherkin feature file containing this scenario
  name: featureFile
  type: string
- description: Full Gherkin text of the scenario including Given/When/Then steps
  name: gherkin
  type: string
- description: Latest test execution status
  name: status
  type: string
- description: Timestamp of the most recent test execution
  name: lastRunAt
  type: string
- description: Timestamp when the scenario was created
  name: createdAt
  type: string
provider_name: Acceptance Criteria
provider_slug: acceptance-criteria
schema_file: json-schema/acceptance-criteria-management-scenario-schema.json
slug: acceptance-criteria-management-scenario
tags:
- Agile
- Behavior Driven Development
- Gherkin
- Quality Assurance
- Requirements
- Testing
- User Stories
title: Scenario
---
