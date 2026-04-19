---
description: Habitat-Lab task configuration
layout: schema
name: TaskConfig
properties_list:
- description: Task type string identifier
  name: type
  type: string
- description: Maximum steps per episode
  name: max_episode_steps
  type: integer
- description: List of measurement names to compute
  name: measurements
  type: array
- description: Available action space configuration
  name: actions
  type: object
- description: UUID of the goal sensor
  name: goal_sensor_uuid
  type: string
provider_name: AI Habitat
provider_slug: ai-habitat
schema_file: json-schema/ai-habitat-task-config-schema.json
slug: ai-habitat-task-config
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
title: TaskConfig
---
