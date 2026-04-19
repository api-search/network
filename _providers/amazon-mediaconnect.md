---
api_count: 1
apis:
- description: The AWS Elemental MediaConnect API provides programmatic access to create and manage flows, sources, outputs, entitlements, VPC interfaces, bridges, gateways, and media streams for reliable live video
  name: AWS Elemental MediaConnect API
  slug: aws-elemental-mediaconnect-api
capabilities:
- description: Workflow capability for live video transport operations including flow management, source configuration, output routing, and entitlement management for broadcast engineers.
  name: Amazon MediaConnect Live Video Transport
  slug: amazon-mediaconnect-live-video-transport
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/mediaconnect/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/mediaconnect/
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
  url: https://aws.amazon.com/blogs/media/tag/aws-elemental-mediaconnect/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/mediaconnect/
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
  type: SpectralRules
  url: rules/amazon-mediaconnect-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-mediaconnect-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-mediaconnect-live-video-transport.yaml
created: '2026-03-16'
description: AWS Elemental MediaConnect is a high-quality transport service for live video that provides the reliability, security, and visibility customers expect from traditional satellite and fiber services. It enables broadcasters to build live video workflows in the cloud with reliable transport of broadcast-quality content using protocols including Zixi, RIST, SRT, RTP, and RTP with FEC.
features:
- description: Supports Zixi, RIST, SRT, RTP, and RTP with FEC protocols for reliable live video delivery over IP networks.
  name: Video Transport Protocols
- description: Transmit compressed video between on-premises multicast environments and cloud infrastructure via the MediaConnect Gateway.
  name: Gateway Capability
- description: Handle uncompressed and visually-lossless video through AWS CDI and JPEG XS encoding with low-latency delivery.
  name: Uncompressed Video Support
- description: Built-in AES encryption with AWS Secrets Manager integration for encryption key management.
  name: End-to-End Encryption
- description: Grant partner and customer accounts controlled access to your video streams via entitlements.
  name: Entitlements
- description: Programmatically create and manage flows, sources, outputs, and VPC interfaces.
  name: Flow Management
- description: Visualize relationships between resources in live video workflows across connected AWS services.
  name: Workflow Monitor
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Send video flows to MediaLive for transcoding and processing.
  name: AWS Elemental MediaLive
- description: Monitor MediaConnect performance metrics and set alarms.
  name: Amazon CloudWatch
- description: Trigger event-driven workflows based on MediaConnect source health changes.
  name: Amazon EventBridge
- description: Deliver processed video content at scale using CloudFront.
  name: Amazon CloudFront
- description: Securely manage encryption keys for content protection.
  name: AWS Secrets Manager
jsonld:
- class_count: 246
  name: Amazon Mediaconnect Api Context
  property_count: 170
  slug: amazon-mediaconnect-api-context
layout: provider
modified: '2026-04-19'
name: Amazon MediaConnect
rules:
- name: Amazon MediaConnect API Rules
  rule_count: 20
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 9
  slug: amazon-mediaconnect-spectral-rules
skills: []
slug: amazon-mediaconnect
solutions: []
tags:
- AWS
- Broadcasting
- Live Video
- Media
- Media Transport
url: https://raw.githubusercontent.com/api-evangelist/amazon-mediaconnect/refs/heads/main/apis.yml
use_cases:
- description: Transport continuous broadcast streams reliably for round-the-clock television channels.
  name: 24/7 TV Channel Operation
- description: Manage event-based video distribution for sports, concerts, news, and other live events.
  name: Live Event Streaming
- description: Share live video feeds with partners and customers through controlled entitlements.
  name: Content Sharing
- description: Provide redundant video pathways for business continuity in broadcast workflows.
  name: Disaster Recovery
---
