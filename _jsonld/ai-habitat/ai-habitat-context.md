---
class_count: 7
classes:
- SimulatorConfig
- AgentConfig
- SensorSpec
- Observation
- Episode
- NavigationGoal
- TaskConfig
context_file: json-ld/ai-habitat-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/ai-habitat/refs/heads/main/json-ld/ai-habitat-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Ai Habitat from AI Habitat.
layout: jsonld
name: Ai Habitat Context
namespaces:
- prefix: habitat
  uri: https://aihabitat.org/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: sceneId
  type: string
- container: ''
  name: agentId
  type: integer
- container: ''
  name: sensorType
  type: string
- container: set
  name: resolution
  type: integer
- container: ''
  name: episodeId
  type: string
- container: set
  name: startPosition
  type: double
- container: set
  name: goals
  type: reference
- container: ''
  name: maxEpisodeSteps
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: radius
  type: double
- container: set
  name: position
  type: double
- container: ''
  name: height
  type: double
- container: ''
  name: enablePhysics
  type: boolean
property_count: 13
provider_name: AI Habitat
provider_slug: ai-habitat
slug: ai-habitat-context
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
- JSON-LD
- Linked Data
- Semantic Web
---
