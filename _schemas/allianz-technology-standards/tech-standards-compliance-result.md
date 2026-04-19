---
description: Result of a compliance check
layout: schema
name: ComplianceResult
properties_list:
- description: Unique identifier for the compliance check
  name: check_id
  type: string
- description: Status of the compliance check
  name: status
  type: string
- description: Number of rules that passed
  name: passed
  type: integer
- description: Number of rules that failed
  name: failed
  type: integer
- description: Number of warnings found
  name: warnings
  type: integer
- description: List of compliance violations found
  name: violations
  type: array
provider_name: Allianz Technology Standards
provider_slug: allianz-technology-standards
schema_file: json-schema/tech-standards-compliance-result-schema.json
slug: tech-standards-compliance-result
tags:
- Best Practices
- Enterprise Architecture
- Guidelines
- Software Development
- Technology Standards
- API Design
- OpenAPI
title: ComplianceResult
---
