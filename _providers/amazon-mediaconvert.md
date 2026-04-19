---
api_count: 1
apis:
- description: AWS Elemental MediaConvert is a file-based video transcoding service that allows you to easily create video-on-demand (VOD) content for broadcast and multiscreen delivery at scale. It supports broadca
  name: Amazon MediaConvert API
  slug: mediaconvert-api
capabilities:
- description: Workflow capability for Amazon MediaConvert media processing operations for broadcast engineers and media developers.
  name: Amazon MediaConvert Workflow
  slug: amazon-mediaconvert-media-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/mediaconvert/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/mediaconvert/
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
  url: https://console.aws.amazon.com/mediaconvert/
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
  url: rules/amazon-mediaconvert-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-mediaconvert-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-mediaconvert-media-workflow.yaml
created: '2026-03-16'
description: AWS Elemental MediaConvert is a file-based video transcoding service that allows you to easily create video-on-demand (VOD) content for broadcast and multiscreen delivery at scale. It supports broadcast-grade features including graphic overlays, content protection, multi-language audio, closed captioning, and a comprehensive range of video formats.
features:
- description: Graphic overlays, content protection, multi-language audio, closed captioning, and professional broadcast formats.
  name: Broadcast-Grade Video Processing
- description: Supports AVC, HEVC, AV1, Apple ProRes, MPEG-2, CMAF, HLS, DASH ISO, Smooth Streaming, 4K, 8K, and HDR including Dolby Vision.
  name: Comprehensive Format Support
- description: Automates workload provisioning, scaling, monitoring, and resource optimization without manual server management.
  name: Automated Infrastructure Management
- description: Jobs run on redundant infrastructure across multiple Availability Zones with automatic health monitoring and failover.
  name: Built-in Reliability
- description: Create reusable job templates and output presets to standardize and accelerate video transcoding workflows.
  name: Job Templates and Presets
- description: Organize and prioritize transcoding jobs using on-demand and reserved queues.
  name: Queue Management
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Use S3 for input and output storage of video files.
  name: Amazon S3
- description: Package transcoded outputs for adaptive bitrate streaming delivery.
  name: AWS Elemental MediaPackage
- description: Monitor job metrics and set alerts for transcoding workflows.
  name: Amazon CloudWatch
- description: Trigger downstream workflows based on MediaConvert job state changes.
  name: Amazon EventBridge
- description: Control access to MediaConvert resources and S3 buckets using IAM roles.
  name: AWS IAM
jsonld:
- class_count: 637
  name: Amazon Mediaconvert Mediaconvert Api Context
  property_count: 646
  slug: amazon-mediaconvert-mediaconvert-api-context
layout: provider
modified: '2026-04-19'
name: Amazon MediaConvert
rules:
- name: Amazon MediaConvert API Rules
  rule_count: 20
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 7
  slug: amazon-mediaconvert-spectral-rules
skills: []
slug: amazon-mediaconvert
solutions: []
tags:
- AWS
- Broadcasting
- Media Processing
- Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-mediaconvert/refs/heads/main/apis.yml
use_cases:
- description: Transcode video files for video-on-demand delivery at broadcast quality.
  name: VOD Content Production
- description: Process large content libraries for multiscreen delivery at any scale.
  name: Large Library Transcoding
- description: Create broadcast-format outputs for television and streaming platform distribution.
  name: Broadcast Distribution
- description: Handle variable transcoding workloads with elastic auto-scaling.
  name: Peak Workload Processing
---
