---
class_count: 4
classes:
- AIIgnoreRule
- AIIgnoreConfig
- ExclusionPattern
- AIToolCompatibility
context_file: json-ld/aiignore-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/aiignore/refs/heads/main/json-ld/aiignore-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Aiignore from .AIIgnore.
layout: jsonld
name: Aiignore Context
namespaces:
- prefix: aiignore
  uri: https://aiignore.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: pattern
  type: string
- container: ''
  name: comment
  type: string
- container: ''
  name: negated
  type: boolean
- container: ''
  name: scope
  type: string
- container: ''
  name: tool
  type: string
- container: set
  name: rules
  type: reference
- container: set
  name: patterns
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: rationale
  type: string
- container: ''
  name: toolName
  type: string
- container: ''
  name: fileName
  type: string
- container: ''
  name: documentationUrl
  type: reference
property_count: 12
provider_name: .AIIgnore
provider_slug: aiignore
slug: aiignore-context
tags:
- AI Agents
- Configuration
- Developer Workflow
- Security
- Privacy
- Developer Tools
- LLM
- Secrets Management
- JSON-LD
- Linked Data
- Semantic Web
---
