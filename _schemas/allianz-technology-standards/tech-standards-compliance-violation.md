---
description: A compliance violation found during a check
layout: schema
name: ComplianceViolation
properties_list:
- description: Rule that was violated
  name: rule_id
  type: string
- description: Description of the violation
  name: description
  type: string
- description: Severity of the violation
  name: severity
  type: string
- description: API path where the violation was found
  name: path
  type: string
provider_name: Allianz Technology Standards
provider_slug: allianz-technology-standards
schema_file: json-schema/tech-standards-compliance-violation-schema.json
slug: tech-standards-compliance-violation
tags:
- Best Practices
- Enterprise Architecture
- Guidelines
- Software Development
- Technology Standards
- API Design
- OpenAPI
title: ComplianceViolation
---
