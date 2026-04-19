---
description: Paginated list of test runs
layout: schema
name: TestRunList
properties_list:
- description: Total number of test runs
  name: total
  type: integer
- description: Current page number
  name: page
  type: integer
- description: Number of items per page
  name: pageSize
  type: integer
- description: Array of test run objects
  name: runs
  type: array
provider_name: Acceptance Criteria
provider_slug: acceptance-criteria
schema_file: json-schema/acceptance-criteria-management-test-run-list-schema.json
slug: acceptance-criteria-management-test-run-list
tags:
- Agile
- Behavior Driven Development
- Gherkin
- Quality Assurance
- Requirements
- Testing
- User Stories
title: TestRunList
---
