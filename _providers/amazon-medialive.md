---
api_count: 1
apis:
- description: AWS Elemental MediaLive is a broadcast-grade live video processing service that creates high-quality video streams for delivery to broadcast televisions and internet-connected multiscreen devices.
  name: Amazon MediaLive API
  slug: medialive-api
capabilities:
- description: Workflow capability for Amazon MediaLive media processing operations for broadcast engineers and media developers.
  name: Amazon MediaLive Workflow
  slug: amazon-medialive-media-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/medialive/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/medialive/
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
  url: https://aws.amazon.com/blogs/media/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/medialive/
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
  url: rules/amazon-medialive-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-medialive-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-medialive-media-workflow.yaml
created: '2026-03-16'
description: AWS Elemental MediaLive is a broadcast-grade live video processing service that creates high-quality video streams for delivery to broadcast televisions and internet-connected multiscreen devices.
features:
- description: Broadcast-grade live video encoding supporting H.264, H.265, and other professional codecs.
  name: Live Video Encoding
- description: Accept live video from RTP, RTMP, HLS pull, MediaConnect, MP4, and other source types.
  name: Multiple Input Types
- description: Pipeline redundancy for high-availability live events with automatic failover.
  name: Redundant Encoding
- description: Insert SCTE-35 markers for downstream ad replacement in live streams.
  name: Dynamic Ad Insertion Markers
- description: Deliver to HLS, DASH, RTMP, archive, UDP, MediaPackage, and other output destinations simultaneously.
  name: Multiple Output Groups
- description: Dynamically switch between input sources during a live event without interruption.
  name: Input Switching
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Receive high-quality video transport feeds from MediaConnect.
  name: AWS Elemental MediaConnect
- description: Send encoded outputs to MediaPackage for adaptive bitrate packaging.
  name: AWS Elemental MediaPackage
- description: Archive live stream recordings to S3 for storage and later processing.
  name: Amazon S3
- description: Monitor channel health metrics and set alerts for live events.
  name: Amazon CloudWatch
- description: Trigger workflows based on channel state change events.
  name: Amazon EventBridge
jsonld:
- class_count: 622
  name: Amazon Medialive Medialive Api Context
  property_count: 675
  slug: amazon-medialive-medialive-api-context
layout: provider
modified: '2026-04-19'
name: Amazon MediaLive
rules:
- name: Amazon MediaLive API Rules
  rule_count: 20
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 7
  slug: amazon-medialive-spectral-rules
skills: []
slug: amazon-medialive
solutions: []
tags:
- AWS
- Broadcasting
- Media Processing
- Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-medialive/refs/heads/main/apis.yml
use_cases:
- description: Encode and deliver live TV channels with broadcast-grade quality.
  name: Live Television Broadcast
- description: Handle large-scale live sports events with redundant pipelines.
  name: Live Sports Streaming
- description: Create live news channel workflows with multi-source input switching.
  name: Live News Production
- description: Stream virtual conferences, concerts, and entertainment events.
  name: Virtual Events
---
