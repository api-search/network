---
api_count: 1
apis:
- description: The Amazon IVS API provides programmatic control over channels, stream keys, recordings, and playback keys for building interactive live streaming applications.
  name: AWS Amazon IVS API
  slug: aws-ivs-api
capabilities:
- description: Unified capability for Developer, Media Engineer to manage managed live streaming with low latency for interactive applications operations.
  name: Amazon Interactive Video Service - Live Streaming Management
  slug: live-streaming-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/ivs/
- title: ''
  type: Website
  url: https://aws.amazon.com/ivs/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/ivs/
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
  url: https://aws.amazon.com/blogs/media/tag/amazon-interactive-video-service/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/ivs/
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
  url: rules/amazon-interactive-video-service-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/ivs.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/live-streaming-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-interactive-video-service-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-interactive-video-service-context.jsonld
created: '2026-03-16'
description: Amazon Interactive Video Service (Amazon IVS) is a managed live streaming solution designed to provide interactive video experiences. It handles the operational complexity of live streaming so you can focus on building engaging applications.
features:
- description: Deliver live video with sub-second latency for real-time interactivity.
  name: Low Latency Streaming
- description: AWS handles all the infrastructure complexity of live streaming at scale.
  name: Managed Infrastructure
- description: Automatically record live streams to S3 and generate playback URLs.
  name: Recording and Playback
- description: Built-in chat messaging for interactive viewer experiences.
  name: Chat Integration
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Stores live stream recordings automatically for on-demand playback.
  name: Amazon S3
- description: Distributes live streams globally with low latency.
  name: Amazon CloudFront
- description: Triggers automation based on stream state changes and events.
  name: AWS Lambda
jsonld:
- class_count: 82
  name: Amazon Interactive Video Service Context
  property_count: 72
  slug: amazon-interactive-video-service-context
layout: provider
modified: '2026-04-19'
name: Amazon Interactive Video Service
rules:
- name: Amazon Interactive Video Service API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: amazon-interactive-video-service-spectral-rules
skills: []
slug: amazon-interactive-video-service
solutions: []
tags:
- AWS
- Live Streaming
- Media
- Video
- Real-Time
url: https://raw.githubusercontent.com/api-evangelist/amazon-interactive-video-service/refs/heads/main/apis.yml
use_cases:
- description: Build gaming livestreams with viewer interaction and real-time overlays.
  name: Interactive Gaming Streams
- description: Host virtual conferences, concerts, and events with large audiences.
  name: Virtual Events
- description: Enable live shopping experiences with interactive product displays.
  name: Social Commerce
---
