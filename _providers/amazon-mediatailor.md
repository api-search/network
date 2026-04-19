---
api_count: 1
apis:
- description: AWS Elemental MediaTailor is a channel assembly and personalized ad-insertion service that enables you to monetize your video content with server-side targeted advertising while maintaining broadcast-
  name: Amazon MediaTailor API
  slug: mediatailor-api
capabilities:
- description: Workflow capability for Amazon MediaTailor media processing operations for broadcast engineers and media developers.
  name: Amazon MediaTailor Workflow
  slug: amazon-mediatailor-media-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/mediatailor/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/mediatailor/
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
  url: https://console.aws.amazon.com/mediatailor/
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
  url: rules/amazon-mediatailor-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-mediatailor-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-mediatailor-media-workflow.yaml
created: '2026-03-16'
description: AWS Elemental MediaTailor is a channel assembly and personalized ad-insertion service that enables you to monetize your video content with server-side targeted advertising while maintaining broadcast-quality.
features:
- description: Seamless ad replacement at the server side for consistent viewer experience across devices.
  name: Server-Side Ad Insertion
- description: Insert targeted ads based on viewer demographics, geography, and behavioral data.
  name: Personalized Ad Targeting
- description: Create linear channels from VOD assets and live streams with automated ad scheduling.
  name: Channel Assembly
- description: Connect to any VAST/VPAID-compliant ad decision server for programmatic advertising.
  name: Ad Decision Server Integration
- description: Configure ad insertion parameters, slate, and CDN settings per playback session.
  name: Playback Configuration
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Ingest packaged live streams for ad insertion.
  name: AWS Elemental MediaPackage
- description: Deliver ad-inserted content via CloudFront with low latency.
  name: Amazon CloudFront
- description: Store VOD source content and slate media assets in S3.
  name: Amazon S3
- description: Monitor ad insertion metrics and playback session data.
  name: Amazon CloudWatch
jsonld:
- class_count: 154
  name: Amazon Mediatailor Mediatailor Api Context
  property_count: 116
  slug: amazon-mediatailor-mediatailor-api-context
layout: provider
modified: '2026-04-19'
name: Amazon MediaTailor
rules:
- name: Amazon MediaTailor API Rules
  rule_count: 20
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 7
  slug: amazon-mediatailor-spectral-rules
skills: []
slug: amazon-mediatailor
solutions: []
tags:
- AWS
- Broadcasting
- Media Processing
- Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-mediatailor/refs/heads/main/apis.yml
use_cases:
- description: Insert targeted ads into video-on-demand content for revenue generation.
  name: VOD Monetization
- description: Replace live ad markers with personalized ads during live events.
  name: Live Stream Advertising
- description: Build free ad-supported streaming TV channels from VOD libraries.
  name: FAST Channel Creation
- description: Deliver personalized ad experiences to individual viewers at scale.
  name: Addressable Advertising
---
