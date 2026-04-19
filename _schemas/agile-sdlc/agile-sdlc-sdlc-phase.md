---
description: A phase in the Agile Software Development Life Cycle representing a stage of development from planning through deployment.
layout: schema
name: SDLCPhase
properties_list:
- description: Name of the SDLC phase.
  name: name
  type: string
- description: Description of activities performed in this phase.
  name: description
  type: string
- description: The sprint this phase belongs to.
  name: sprint_id
  type: string
- description: Phase start date.
  name: start_date
  type: string
- description: Phase end date.
  name: end_date
  type: string
- description: List of artifacts produced in this phase.
  name: artifacts
  type: array
provider_name: Agile SDLC
provider_slug: agile-sdlc
schema_file: json-schema/agile-sdlc-sdlc-phase-schema.json
slug: agile-sdlc-sdlc-phase
tags:
- Iterative Development
- Methodology
- Project Management
- Software Development
- SDLC
- DevOps
- CI/CD
title: SDLCPhase
---
