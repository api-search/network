---
description: A WAI-ARIA role definition that provides semantic meaning to HTML elements for assistive technologies.
layout: schema
name: AriaRole
properties_list:
- description: The ARIA role name
  name: name
  type: string
- description: The role category in the ARIA taxonomy
  name: category
  type: string
- description: Description of the role and its semantic meaning
  name: description
  type: string
- description: Parent roles in the ARIA role hierarchy
  name: superclassRole
  type: array
- description: ARIA states required for this role
  name: requiredStates
  type: array
- description: ARIA properties supported by this role
  name: supportedProperties
  type: array
- description: HTML elements that natively carry this role
  name: implicitAriaSemantics
  type: string
- description: URL to the WAI-ARIA spec definition
  name: specUrl
  type: string
provider_name: Accessibility Standards
provider_slug: accessibility-standards
schema_file: json-schema/aria-role-schema.json
slug: aria-role
tags:
- Accessibility
- Compliance
- UX
- Web Standards
- WCAG
- ARIA
- Section 508
- Disability
title: AriaRole
---
