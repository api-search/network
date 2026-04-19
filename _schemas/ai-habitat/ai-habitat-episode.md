---
description: A single training/evaluation episode with start and goal specification
layout: schema
name: Episode
properties_list:
- description: Unique episode identifier
  name: episode_id
  type: string
- description: Scene file path for this episode
  name: scene_id
  type: string
- description: Agent starting position [x, y, z]
  name: start_position
  type: array
- description: Agent starting rotation quaternion
  name: start_rotation
  type: array
- description: List of goal specifications
  name: goals
  type: array
- description: Additional episode metadata
  name: info
  type: object
provider_name: AI Habitat
provider_slug: ai-habitat
schema_file: json-schema/ai-habitat-episode-schema.json
slug: ai-habitat-episode
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
title: Episode
---
