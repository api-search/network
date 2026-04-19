---
description: Request body for adding an acceptance criterion to a story
layout: schema
name: CreateAcceptanceCriterionRequest
properties_list:
- description: Plain-language description of the acceptance condition
  name: description
  type: string
- description: Format of the criterion
  name: format
  type: string
- description: Gherkin Given clause
  name: given
  type: string
- description: Gherkin When clause
  name: when
  type: string
- description: Gherkin Then clause
  name: then
  type: string
- description: Display order position
  name: order
  type: integer
provider_name: Acceptance Criteria
provider_slug: acceptance-criteria
schema_file: json-schema/acceptance-criteria-management-create-acceptance-criterion-request-schema.json
slug: acceptance-criteria-management-create-acceptance-criterion-request
tags:
- Agile
- Behavior Driven Development
- Gherkin
- Quality Assurance
- Requirements
- Testing
- User Stories
title: CreateAcceptanceCriterionRequest
---
