---
api_count: 1
apis:
- description: The Amazon GameLift API provides programmatic access to create and manage fleets, game sessions, player sessions, matchmaking configurations, and game server groups for hosting multiplayer game server
  name: Amazon GameLift API
  slug: amazon-gamelift-api
capabilities:
- description: Unified workflow capability for game developers and operations teams managing Amazon GameLift resources. Combines fleet management, game session lifecycle, player matchmaking, and scaling operations i
  name: Amazon GameLift Game Operations
  slug: amazon-gamelift-game-operations
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/gamelift/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/gamelift/
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
  url: https://aws.amazon.com/blogs/gametech/tag/amazon-gamelift/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/gamelift/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SDK
  url: https://aws.amazon.com/developer/tools/
- title: ''
  type: CLI
  url: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html
- title: ''
  type: SpectralRules
  url: rules/amazon-gamelift-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-gamelift-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-gamelift-game-operations.yaml
created: '2026-03-16'
description: Amazon GameLift is a dedicated game server hosting solution that deploys, operates, and scales cloud servers for multiplayer games. It provides low-latency, low-cost server infrastructure, eliminates operational overhead, and allows you to focus on creating great gaming experiences. The service includes FlexMatch for matchmaking, FleetIQ for optimized Spot Instance usage, and Realtime Servers for rapid game server deployment.
features:
- description: Fully managed service to deploy, operate, and scale dedicated game servers with automatic lifecycle management for game and player sessions.
  name: Managed Game Server Hosting
- description: Customizable matchmaking service that connects up to 200 players into single game sessions based on configurable matching rules.
  name: FlexMatch Matchmaking
- description: Optimizes use of low-cost Spot Instances for game hosting, improving viability and reducing costs while maintaining performance.
  name: FleetIQ Optimization
- description: Rapidly configurable game server framework with core Amazon GameLift infrastructure built in for quick deployment.
  name: Realtime Servers
- description: Automatically scales fleet capacity up to 9,000 servers per minute to balance player demand and hosting costs.
  name: Auto Scaling
- description: Deploy game servers across multiple AWS regions with global queues for optimal player latency and resiliency.
  name: Multi-Region Deployment
- description: Multi-fleet, multi-region queues that use FleetIQ algorithms to prioritize game session placements based on latency, cost, and availability.
  name: Game Session Queues
- description: Create and manage VPC peering connections between GameLift hosting resources and other AWS resources.
  name: VPC Peering
- description: Create fleet aliases to simplify game server transitions and updates without changing client configurations.
  name: Alias Management
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: GameLift uses EC2 instances as the underlying compute for managed game server hosting.
  name: AWS EC2
- description: Integrates with Auto Scaling groups for FleetIQ standalone deployment.
  name: AWS Auto Scaling
- description: Monitor fleet metrics, game session activity, and performance data through CloudWatch.
  name: Amazon CloudWatch
- description: Receive notifications for matchmaking events and game session placement status.
  name: Amazon SNS
- description: Use IAM roles and policies to control access to GameLift resources and operations.
  name: AWS IAM
- description: Store and retrieve game server build files using S3 buckets for fleet deployment.
  name: Amazon S3
- description: Provision and manage GameLift resources using infrastructure-as-code templates.
  name: AWS CloudFormation
jsonld:
- class_count: 237
  name: Amazon Gamelift Context
  property_count: 270
  slug: amazon-gamelift-context
layout: provider
modified: '2026-04-19'
name: Amazon GameLift
rules:
- name: Amazon GameLift API Rules
  rule_count: 18
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 8
  slug: amazon-gamelift-spectral-rules
skills: []
slug: amazon-gamelift
solutions: []
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
url: https://raw.githubusercontent.com/api-evangelist/amazon-gamelift/refs/heads/main/apis.yml
use_cases:
- description: Deploy and scale game servers for launch day without uncertainty about player demand using predictive autoscaling.
  name: Multiplayer Game Launches
- description: Host dedicated game servers for real-time multiplayer games with low latency and high performance.
  name: Session-Based Multiplayer
- description: Use FlexMatch to create fair, customizable matchmaking for players based on skill level, region, and other criteria.
  name: Player Matchmaking
- description: Leverage FleetIQ with Spot Instances to reduce game hosting costs while maintaining reliability.
  name: Cost-Optimized Hosting
- description: Deploy game servers across multiple AWS regions to minimize player latency worldwide.
  name: Global Game Distribution
---
