---
description: Request body for creating and triggering a test run
layout: schema
name: CreateTestRunRequest
properties_list:
- description: User story IDs to test (all scenarios for these stories)
  name: storyIds
  type: array
- description: Specific scenario IDs to execute
  name: scenarioIds
  type: array
provider_name: Acceptance Criteria
provider_slug: acceptance-criteria
schema_file: json-schema/acceptance-criteria-management-create-test-run-request-schema.json
slug: acceptance-criteria-management-create-test-run-request
tags:
- Agile
- Behavior Driven Development
- Gherkin
- Quality Assurance
- Requirements
- Testing
- User Stories
title: CreateTestRunRequest
---
