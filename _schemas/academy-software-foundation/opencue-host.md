---
description: A render host machine
layout: schema
name: Host
properties_list:
- description: Unique host identifier
  name: id
  type: string
- description: Hostname
  name: name
  type: string
- description: Host state
  name: state
  type: string
- description: Host lock state
  name: lock
  type: string
- description: Total CPU cores on the host
  name: totalCores
  type: integer
- description: Currently idle CPU cores
  name: idleCores
  type: integer
- description: Total memory in MB
  name: totalMemory
  type: integer
- description: Currently idle memory in MB
  name: idleMemory
  type: integer
- description: Current system load (percentage)
  name: load
  type: integer
provider_name: Academy Software Foundation
provider_slug: academy-software-foundation
schema_file: json-schema/opencue-host-schema.json
slug: opencue-host
tags:
- Animation
- Color Management
- Film
- Linux Foundation
- Open Source
- Rendering
- Standards
- Visual Effects
- VFX
title: Host
---
