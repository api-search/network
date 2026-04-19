---
api_count: 1
apis:
- description: The Amazon EC2 Auto Scaling API provides programmatic access to create and manage Auto Scaling groups, launch configurations, scaling policies, scheduled actions, lifecycle hooks, and warm pools for a
  name: Amazon EC2 Auto Scaling API
  slug: ''
capabilities:
- description: Unified capability for managing EC2 Auto Scaling groups, scaling policies, and lifecycle hooks for cloud operations engineers.
  name: Amazon EC2 Auto Scaling Auto Scaling Group Management
  slug: ec2-auto-scaling-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/developer/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/autoscaling/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/compute/category/compute/auto-scaling/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/ec2/autoscaling/
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
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-ec2-auto-scaling
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Security
  url: https://aws.amazon.com/security/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-ec2-auto-scaling-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-ec2-auto-scaling-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/ec2-auto-scaling-management.yaml
created: '2026-03-16'
description: Amazon EC2 Auto Scaling helps you maintain application availability and lets you automatically add or remove EC2 instances according to conditions you define. You can use fleet management features to maintain the health and availability of your fleet, and use dynamic and predictive scaling to add or remove EC2 instances to meet demand.
features:
- description: Automatically scales EC2 capacity up or down in response to real-time demand using target tracking, step, or simple scaling policies.
  name: Dynamic Scaling
- description: Uses machine learning to forecast future demand and proactively adds EC2 instances ahead of anticipated load spikes.
  name: Predictive Scaling
- description: Scales capacity at pre-defined times based on predictable load patterns or business cycles.
  name: Scheduled Scaling
- description: Automatically detects and replaces unhealthy instances to maintain application availability and fleet health.
  name: Fleet Management
- description: Gradually updates EC2 instances in an Auto Scaling group with new AMIs or launch template versions.
  name: Instance Refresh
- description: Pre-initializes EC2 instances to reduce latency for scale-out events by keeping a pool of instances in a stopped or running state.
  name: Warm Pools
- description: Combines On-Demand and Spot instances with multiple instance types for cost optimization and availability.
  name: Mixed Instances Policy
- description: Pauses instance launch or termination to perform custom actions such as installing software or draining connections.
  name: Lifecycle Hooks
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Launches and terminates EC2 instances based on scaling policies and schedules.
  name: Amazon EC2
- description: Uses CloudWatch metrics and alarms to trigger dynamic scaling policies automatically.
  name: Amazon CloudWatch
- description: Automatically registers new instances with load balancers and deregisters terminated instances.
  name: Elastic Load Balancing
- description: Integrates with Systems Manager for instance configuration and patch management during lifecycle hooks.
  name: AWS Systems Manager
- description: Sends notifications for scaling events, instance launches, and terminations via SNS topics.
  name: Amazon SNS
- description: Works with Cost Explorer and Budgets to monitor and optimize spend on Auto Scaling fleets.
  name: AWS Cost Management
jsonld:
- class_count: 48
  name: Amazon Ec2 Auto Scaling Context
  property_count: 200
  slug: amazon-ec2-auto-scaling-context
layout: provider
modified: '2026-04-19'
name: Amazon EC2 Auto Scaling
rules:
- name: Amazon EC2 Auto Scaling API Rules
  rule_count: 19
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 9
  slug: amazon-ec2-auto-scaling-spectral-rules
skills: []
slug: amazon-ec2-auto-scaling
solutions: []
tags:
- Amazon Web Services
- Auto Scaling
- AWS
- Compute
- EC2
- High Availability
- Scaling
url: https://aws.amazon.com/ec2/autoscaling/
use_cases:
- description: Automatically scale web server fleets to handle variable HTTP traffic loads without over-provisioning.
  name: Web Application Scaling
- description: Scale compute capacity up when jobs arrive and down when completed to minimize costs for batch workloads.
  name: Batch Processing
- description: Independently scale each microservice based on its own traffic patterns and resource utilization.
  name: Microservices Autoscaling
- description: Combine Spot and On-Demand instances to reduce EC2 costs while maintaining availability.
  name: Cost Optimization
- description: Use instance refresh to gradually replace old instances with new ones for zero-downtime deployments.
  name: Blue/Green Deployments
---
