---
description: A WCAG success criterion defining a testable requirement for accessible web content.
layout: schema
name: WcagSuccessCriterion
properties_list:
- description: The WCAG success criterion identifier, e.g. 1.1.1
  name: id
  type: string
- description: Short name of the success criterion
  name: title
  type: string
- description: Conformance level of the success criterion
  name: level
  type: string
- description: The POUR principle the criterion belongs to
  name: principle
  type: string
- description: The guideline number the criterion belongs to
  name: guideline
  type: string
- description: Full text of the success criterion requirement
  name: description
  type: string
- description: URL to the official WCAG success criterion documentation
  name: url
  type: string
- description: WCAG version that introduced this criterion
  name: version
  type: string
- description: URL to the understanding document for this criterion
  name: understanding
  type: string
- description: List of technique identifiers applicable to this criterion
  name: techniques
  type: array
provider_name: Accessibility Standards
provider_slug: accessibility-standards
schema_file: json-schema/wcag-success-criterion-schema.json
slug: wcag-success-criterion
tags:
- Accessibility
- Compliance
- UX
- Web Standards
- WCAG
- ARIA
- Section 508
- Disability
title: WcagSuccessCriterion
---
