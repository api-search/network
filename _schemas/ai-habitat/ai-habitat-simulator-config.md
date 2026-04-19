---
description: Configuration for the Habitat-Sim simulator instance
layout: schema
name: SimulatorConfig
properties_list:
- description: Path to the 3D scene file (.glb, .ply)
  name: scene_id
  type: string
- description: Default agent index
  name: default_agent_id
  type: integer
- description: List of sensor configurations
  name: sensor_specifications
  type: array
- description: Physics engine to use
  name: physics_simulation_library
  type: string
- description: GPU device ID for rendering
  name: gpu_device_id
  type: integer
- description: Random seed for reproducibility
  name: random_seed
  type: integer
- description: Enable physics simulation
  name: enable_physics
  type: boolean
provider_name: AI Habitat
provider_slug: ai-habitat
schema_file: json-schema/ai-habitat-simulator-config-schema.json
slug: ai-habitat-simulator-config
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
title: SimulatorConfig
---
