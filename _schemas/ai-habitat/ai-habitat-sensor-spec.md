---
description: Specification for a simulated sensor
layout: schema
name: SensorSpec
properties_list:
- description: Unique sensor identifier
  name: uuid
  type: string
- description: 'Sensor type: COLOR, DEPTH, SEMANTIC, EQUIRECTANGULAR'
  name: sensor_type
  type: string
- description: '[height, width] in pixels'
  name: resolution
  type: array
- description: Sensor position [x, y, z] relative to agent
  name: position
  type: array
- description: Sensor orientation quaternion
  name: orientation
  type: array
- description: Horizontal field of view in degrees
  name: hfov
  type: number
provider_name: AI Habitat
provider_slug: ai-habitat
schema_file: json-schema/ai-habitat-sensor-spec-schema.json
slug: ai-habitat-sensor-spec
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
title: SensorSpec
---
