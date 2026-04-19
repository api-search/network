---
description: An accessibility conformance report documenting the evaluation of a website or application against WCAG criteria.
layout: schema
name: WcagConformanceReport
properties_list:
- description: Unique identifier for this conformance report
  name: id
  type: string
- description: The website or application being evaluated
  name: subject
  type: object
- description: The WCAG version evaluated against
  name: standard
  type: string
- description: The claimed conformance level
  name: conformanceLevel
  type: string
- description: Overall conformance status
  name: status
  type: string
- description: Date the evaluation was conducted
  name: evaluationDate
  type: string
- description: Name or organization that performed the evaluation
  name: evaluator
  type: string
- description: List of accessibility violations found
  name: violations
  type: array
provider_name: Accessibility Standards
provider_slug: accessibility-standards
schema_file: json-schema/wcag-conformance-report-schema.json
slug: wcag-conformance-report
tags:
- Accessibility
- Compliance
- UX
- Web Standards
- WCAG
- ARIA
- Section 508
- Disability
title: WcagConformanceReport
---
