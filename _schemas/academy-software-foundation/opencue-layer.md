---
description: A layer within a render job
layout: schema
name: Layer
properties_list:
- description: Unique layer identifier
  name: id
  type: string
- description: Layer name
  name: name
  type: string
- description: Layer type
  name: type
  type: string
- description: Layer state
  name: state
  type: string
- description: Minimum cores required per frame
  name: minCores
  type: integer
- description: Maximum cores allowed per frame
  name: maxCores
  type: integer
- description: Whether frames can run multi-threaded
  name: threadable
  type: boolean
- description: Total number of frames in this layer
  name: totalFrames
  type: integer
- description: Number of completed frames in this layer
  name: doneFrames
  type: integer
provider_name: Academy Software Foundation
provider_slug: academy-software-foundation
schema_file: json-schema/opencue-layer-schema.json
slug: opencue-layer
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
title: Layer
---
