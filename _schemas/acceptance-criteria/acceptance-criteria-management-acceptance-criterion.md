---
description: A single testable condition that must be met for a user story to be accepted as complete
layout: schema
name: AcceptanceCriterion
properties_list:
- description: Unique identifier for the acceptance criterion
  name: id
  type: string
- description: ID of the parent user story
  name: storyId
  type: string
- description: Plain-language description of the acceptance condition
  name: description
  type: string
- description: Format used to express the criterion
  name: format
  type: string
- description: Gherkin Given clause (context/precondition) if format is gherkin
  name: given
  type: string
- description: Gherkin When clause (action/trigger) if format is gherkin
  name: when
  type: string
- description: Gherkin Then clause (expected outcome) if format is gherkin
  name: then
  type: string
- description: Verification status of this criterion
  name: status
  type: string
- description: Display order position within the parent story
  name: order
  type: integer
- description: Timestamp when the criterion was created
  name: createdAt
  type: string
provider_name: Acceptance Criteria
provider_slug: acceptance-criteria
schema_file: json-schema/acceptance-criteria-management-acceptance-criterion-schema.json
slug: acceptance-criteria-management-acceptance-criterion
tags:
- Agile
- Behavior Driven Development
- Gherkin
- Quality Assurance
- Requirements
- Testing
- User Stories
title: AcceptanceCriterion
---
