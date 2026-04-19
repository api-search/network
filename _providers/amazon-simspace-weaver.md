---
api_count: 1
apis:
- description: The AWS SimSpace Weaver API provides programmatic access to create and manage simulations, simulation apps, snapshots, and clocks for running large-scale spatial simulations in the cloud.
  name: AWS SimSpace Weaver API
  slug: aws-simspace-weaver-api
capabilities: []
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/simspaceweaver/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/simspaceweaver/latest/userguide/what-is.html
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/hpc/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/simspaceweaver/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-simspace-weaver-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-simspace-weaver-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/amazon-simspace-weaver.yaml
created: '2026-03-16'
description: AWS SimSpace Weaver is a managed service that helps you build and run large-scale spatial simulations in the AWS Cloud. It provides tools to run custom spatial simulation logic at scale and use simulation workloads for defense, urban planning, and other real-world system simulations.
features:
- description: Run spatial simulations at city or country scale with millions of agents.
  name: Large-scale Simulations
- description: Fully managed compute infrastructure for simulation workloads.
  name: Managed Infrastructure
- description: Deploy custom simulation apps that interact with the simulation world.
  name: App Framework
- description: Start, pause, stop, and control simulation time.
  name: Clock Control
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Deploy SimSpace Weaver simulations using CloudFormation.
  name: AWS CloudFormation
- description: Store simulation schemas and output data in S3.
  name: Amazon S3
- description: Monitor simulation metrics and logs via CloudWatch.
  name: Amazon CloudWatch
jsonld:
- class_count: 43
  name: Amazon Simspace Weaver Context
  property_count: 38
  slug: amazon-simspace-weaver-context
layout: provider
modified: '2026-04-19'
name: Amazon SimSpace Weaver
rules:
- name: Amazon SimSpace Weaver API Rules
  rule_count: 19
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 7
  slug: amazon-simspace-weaver-spectral-rules
skills: []
slug: amazon-simspace-weaver
solutions: []
tags:
- AWS
- Defense
- Digital Twin
- Simulation
- Spatial Simulation
url: https://raw.githubusercontent.com/api-evangelist/amazon-simspace-weaver/refs/heads/main/apis.yml
use_cases:
- description: Simulate traffic, pedestrian movement, and city infrastructure at scale.
  name: Urban Planning
- description: Model disaster scenarios and evacuation plans.
  name: Emergency Response
- description: Run large-scale defense and logistics simulations.
  name: Defense Simulations
---
