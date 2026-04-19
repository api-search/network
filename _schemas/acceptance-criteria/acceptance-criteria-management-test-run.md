---
description: An execution instance of acceptance criteria tests across one or more stories or scenarios
layout: schema
name: TestRun
properties_list:
- description: Unique identifier for the test run
  name: id
  type: string
- description: User story IDs included in this test run
  name: storyIds
  type: array
- description: Specific scenario IDs included in this test run
  name: scenarioIds
  type: array
- description: Overall test run status
  name: status
  type: string
- description: Total number of scenarios in this run
  name: totalScenarios
  type: integer
- description: Number of scenarios that passed
  name: passedScenarios
  type: integer
- description: Number of scenarios that failed
  name: failedScenarios
  type: integer
- description: Number of scenarios that were skipped
  name: skippedScenarios
  type: integer
- description: Timestamp when the test run started
  name: startedAt
  type: string
- description: Timestamp when the test run completed
  name: completedAt
  type: string
- description: URL to the detailed test run report
  name: reportUrl
  type: string
provider_name: Acceptance Criteria
provider_slug: acceptance-criteria
schema_file: json-schema/acceptance-criteria-management-test-run-schema.json
slug: acceptance-criteria-management-test-run
tags:
- Agile
- Behavior Driven Development
- Gherkin
- Quality Assurance
- Requirements
- Testing
- User Stories
title: TestRun
---
