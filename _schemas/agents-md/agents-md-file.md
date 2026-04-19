---
description: Representation of an AGENTS.md file's structured content providing context and instructions to AI coding agents.
layout: schema
name: AgentsMdFile
properties_list:
- description: The filename, typically AGENTS.md.
  name: filename
  type: string
- description: File path within the repository.
  name: location
  type: string
- description: Name of the project or subproject this file applies to.
  name: project_name
  type: string
- description: Brief description of the project's purpose and architecture.
  name: description
  type: string
- description: Commands for building the project.
  name: build_commands
  type: array
- description: Commands for running tests.
  name: test_commands
  type: array
- description: Commands for linting and formatting code.
  name: lint_commands
  type: array
- description: Coding conventions and style guidelines for the project.
  name: coding_standards
  type: array
- description: Security considerations and sensitive file locations agents should be aware of.
  name: security_notes
  type: array
- description: Date the AGENTS.md file was created.
  name: created
  type: string
- description: Date the AGENTS.md file was last modified.
  name: modified
  type: string
provider_name: AGENTS.md
provider_slug: agents-md
schema_file: json-schema/agents-md-file-schema.json
slug: agents-md-file
tags:
- AI Agents
- AI Copilot
- Coding Standards
- Developer Workflow
- Open Standard
- Documentation
title: AgentsMdFile
---
