---
description: A render job in OpenCue
layout: schema
name: Job
properties_list:
- description: Unique job identifier
  name: id
  type: string
- description: Full job name
  name: name
  type: string
- description: Show name this job belongs to
  name: show
  type: string
- description: Current job state
  name: state
  type: string
- description: Job priority (higher is more important)
  name: priority
  type: integer
- description: Total number of frames in the job
  name: totalFrames
  type: integer
- description: Number of completed frames
  name: doneFrames
  type: integer
- description: Number of currently running frames
  name: runningFrames
  type: integer
- description: Number of failed/dead frames
  name: deadFrames
  type: integer
- description: Number of frames waiting to be dispatched
  name: waitingFrames
  type: integer
provider_name: Academy Software Foundation
provider_slug: academy-software-foundation
schema_file: json-schema/opencue-job-schema.json
slug: opencue-job
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
title: Job
---
