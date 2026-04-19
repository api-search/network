---
api_count: 1
apis:
- description: AI Habitat simulation framework for embodied AI research, including Habitat-Sim (high-performance 3D simulator) and Habitat-Lab (modular training library). Supports navigation, manipulation, and human
  name: AI Habitat
  slug: ai-habitat
common:
- title: ''
  type: GitHubOrganization
  url: https://github.com/facebookresearch
- title: ''
  type: GitHubRepository
  url: https://github.com/facebookresearch/habitat-sim
- title: ''
  type: GitHubRepository
  url: https://github.com/facebookresearch/habitat-lab
- title: ''
  type: Documentation
  url: https://aihabitat.org/docs/
- title: ''
  type: Portal
  url: https://aihabitat.org/challenge/
- title: ''
  type: Forum
  url: https://github.com/facebookresearch/habitat-lab/discussions
- title: ''
  type: Portal
  url: https://huggingface.co/ai-habitat
- title: Python Package (habitat-sim)
  type: SDK
  url: https://pypi.org/project/habitat-sim/
- title: Python Package (habitat-lab)
  type: SDK
  url: https://pypi.org/project/habitat-lab/
- title: ''
  type: Tools
  url: https://github.com/facebookresearch/partnr-planner
created: '2025-02-17'
description: AI Habitat is an open-source simulation platform from Meta AI Research for embodied AI research. It provides high-performance 3D simulated environments for training and evaluating AI agents on navigation, manipulation, and human-robot collaboration tasks. Habitat-Sim delivers 10,000+ FPS simulation and Habitat-Lab provides a modular library for defining tasks, training agents, and running benchmarks.
features:
- description: Habitat-Sim achieves 10,000+ FPS on a single GPU and 8,000+ steps/second for robot simulation, enabling fast RL training.
  name: High-Performance Simulation
- description: Supports HM3D, MatterPort3D, Gibson, Replica, and HSSD datasets with high visual fidelity.
  name: Photorealistic 3D Environments
- description: Bullet physics engine integration for realistic object interactions and manipulation tasks.
  name: Physics-Enabled Simulation
- description: Configurable robot models including Fetch mobile manipulator, Franka arm, and AlienGo quadruped.
  name: Robot Support via URDF
- description: RGB, depth, semantic, and egomotion sensors for varied agent perception configurations.
  name: Configurable Sensors
- description: Habitat-Lab provides modular task definition, agent configuration, and benchmarking tools.
  name: Modular Task Framework
- description: Built-in support for IL and RL training pipelines for embodied AI agents.
  name: Imitation and Reinforcement Learning
- description: Habitat 3.0 co-habitat supports humans, avatars, and robots sharing simulated environments.
  name: Human-Robot Collaboration
- description: Designed for large-scale distributed training across GPU clusters.
  name: Parallelizable Across Clusters
- description: Habitat Challenge on EvalAI provides standardized evaluation of navigation and manipulation agents.
  name: Annual Benchmark Challenge
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Deep learning framework integration for neural network training and inference.
  name: PyTorch
- description: Datasets and models available on HuggingFace Hub at ai-habitat organization.
  name: HuggingFace
- description: Habitat Challenge evaluation hosted on EvalAI platform for standardized benchmarking.
  name: EvalAI
- description: Conda package distribution via conda-forge and aihabitat channels.
  name: Conda / conda-forge
- description: Bullet physics engine for realistic rigid-body simulation and manipulation.
  name: Bullet Physics
- description: Robot Operating System integration for sim-to-real transfer research.
  name: ROS
jsonld:
- class_count: 7
  name: Ai Habitat Context
  property_count: 13
  slug: ai-habitat-context
layout: provider
modified: '2026-04-19'
name: AI Habitat
skills: []
slug: ai-habitat
solutions: []
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
url: https://raw.githubusercontent.com/api-evangelist/ai-habitat/refs/heads/main/apis.yml
use_cases:
- description: Train and evaluate AI agents on point-goal, object-goal, and image-goal navigation tasks in 3D environments.
  name: Embodied Navigation Research
- description: Develop manipulation skills for pick-and-place, rearrangement, and tool use with simulated robot arms.
  name: Robot Manipulation Research
- description: Research human-robot teaming for household tasks using the PARTNR benchmark and Habitat 3.0.
  name: Human-Robot Collaboration
- description: Fast simulation enables RL agents to explore millions of environment steps for policy learning.
  name: Reinforcement Learning Training
- description: Generate synthetic data, annotations, and demonstrations for embodied AI training datasets.
  name: Dataset Creation and Annotation
---
