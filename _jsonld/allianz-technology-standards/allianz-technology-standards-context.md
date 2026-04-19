---
class_count: 8
classes:
- StandardList
- WebhookGuideline
- StandardRule
- ComplianceCheckRequest
- ComplianceViolation
- Standard
- ComplianceResult
- PaginationGuideline
context_file: json-ld/allianz-technology-standards-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/allianz-technology-standards/refs/heads/main/json-ld/allianz-technology-standards-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Allianz Technology Standards from Allianz Technology Standards.
layout: jsonld
name: Allianz Technology Standards Context
namespaces:
- prefix: allianz
  uri: https://standards.allianz.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: total
  type: integer
- container: set
  name: items
  type: string
- container: ''
  name: guidelineId
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: version
  type: string
- container: set
  name: notificationTypes
  type: string
- container: set
  name: securityRequirements
  type: string
- container: ''
  name: ruleId
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: openapiUrl
  type: reference
- container: set
  name: standardIds
  type: string
- container: ''
  name: path
  type: string
- container: ''
  name: standardId
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: status
  type: string
- container: set
  name: rules
  type: string
- container: ''
  name: checkId
  type: string
- container: ''
  name: passed
  type: integer
- container: ''
  name: failed
  type: integer
- container: ''
  name: warnings
  type: integer
- container: set
  name: violations
  type: string
- container: set
  name: parameters
  type: string
- container: set
  name: responseHeaders
  type: string
property_count: 24
provider_name: Allianz Technology Standards
provider_slug: allianz-technology-standards
slug: allianz-technology-standards-context
tags:
- Best Practices
- Enterprise Architecture
- Guidelines
- Software Development
- Technology Standards
- API Design
- OpenAPI
- JSON-LD
- Linked Data
- Semantic Web
---
