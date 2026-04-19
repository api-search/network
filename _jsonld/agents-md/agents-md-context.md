---
class_count: 1
classes:
- AgentsMdFile
context_file: json-ld/agents-md-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/agents-md/refs/heads/main/json-ld/agents-md-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Agents Md from AGENTS.md.
layout: jsonld
name: Agents Md Context
namespaces:
- prefix: amd
  uri: https://agents.md/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: filename
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: project_name
  type: string
- container: ''
  name: description
  type: string
- container: set
  name: build_commands
  type: reference
- container: set
  name: test_commands
  type: reference
- container: set
  name: lint_commands
  type: reference
- container: set
  name: coding_standards
  type: string
- container: set
  name: security_notes
  type: string
- container: ''
  name: label
  type: string
- container: ''
  name: command
  type: string
- container: ''
  name: created
  type: date
- container: ''
  name: modified
  type: date
property_count: 13
provider_name: AGENTS.md
provider_slug: agents-md
slug: agents-md-context
tags:
- AI Agents
- AI Copilot
- Coding Standards
- Developer Workflow
- Open Standard
- Documentation
- JSON-LD
- Linked Data
- Semantic Web
---
