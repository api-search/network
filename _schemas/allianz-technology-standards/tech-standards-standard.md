---
description: An Allianz technology standard definition
layout: schema
name: Standard
properties_list:
- description: Unique identifier for the standard
  name: standard_id
  type: string
- description: Human-readable name of the standard
  name: name
  type: string
- description: Category of the technology standard
  name: category
  type: string
- description: Current version of the standard
  name: version
  type: string
- description: Lifecycle status of the standard
  name: status
  type: string
- description: Description of what the standard covers
  name: description
  type: string
- description: List of rules defined by this standard
  name: rules
  type: array
provider_name: Allianz Technology Standards
provider_slug: allianz-technology-standards
schema_file: json-schema/tech-standards-standard-schema.json
slug: tech-standards-standard
tags:
- Best Practices
- Enterprise Architecture
- Guidelines
- Software Development
- Technology Standards
- API Design
- OpenAPI
title: Standard
---
