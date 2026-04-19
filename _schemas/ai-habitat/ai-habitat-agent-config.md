---
description: Configuration for an agent in the simulation
layout: schema
name: AgentConfig
properties_list:
- description: Agent height in meters
  name: height
  type: number
- description: Agent radius in meters for collision
  name: radius
  type: number
- description: List of sensor specs attached to agent
  name: sensor_specifications
  type: array
- description: Discrete action space mapping action names to ActionSpec
  name: action_space
  type: object
- description: 'Agent body type: LocoBot, FetchRobot, Franka, AlienGo'
  name: body_type
  type: string
provider_name: AI Habitat
provider_slug: ai-habitat
schema_file: json-schema/ai-habitat-agent-config-schema.json
slug: ai-habitat-agent-config
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
title: AgentConfig
---
