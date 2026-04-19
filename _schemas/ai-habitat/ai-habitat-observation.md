---
description: Sensor observation returned from a simulation step
layout: schema
name: Observation
properties_list:
- description: RGB image array (H x W x 4)
  name: rgb
  type: object
- description: Depth image array (H x W x 1) in meters
  name: depth
  type: object
- description: Semantic segmentation array (H x W x 1) with object instance IDs
  name: semantic
  type: object
- description: GPS coordinates [x, z] relative to start
  name: gps
  type: array
- description: Compass heading in radians
  name: compass
  type: array
provider_name: AI Habitat
provider_slug: ai-habitat
schema_file: json-schema/ai-habitat-observation-schema.json
slug: ai-habitat-observation
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
title: Observation
---
