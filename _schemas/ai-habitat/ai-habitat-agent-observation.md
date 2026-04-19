---
description: Full observation dict returned to an agent after each step
layout: schema
name: AgentObservation
properties_list:
- description: RGB camera observation
  name: rgb
  type: object
- description: Depth camera observation
  name: depth
  type: object
- description: Point goal with GPS/compass sensor
  name: pointgoal_with_gps_compass
  type: object
- description: Object category name for ObjectNav tasks
  name: objectgoal
  type: string
provider_name: AI Habitat
provider_slug: ai-habitat
schema_file: json-schema/ai-habitat-agent-observation-schema.json
slug: ai-habitat-agent-observation
tags:
- Artificial Intelligence
- Simulation
- Embodied AI
- Robotics
- Computer Vision
- Reinforcement Learning
- Machine Learning
- Open Source
- Research
title: AgentObservation
---
