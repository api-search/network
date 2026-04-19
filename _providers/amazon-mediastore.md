---
api_count: 1
apis:
- description: AWS Elemental MediaStore is an AWS storage service optimized for media, providing the performance, consistency, and low latency required to deliver live streaming video content at scale.
  name: Amazon MediaStore API
  slug: mediastore-api
capabilities:
- description: Workflow capability for Amazon MediaStore media processing operations for broadcast engineers and media developers.
  name: Amazon MediaStore Workflow
  slug: amazon-mediastore-media-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/mediastore/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/mediastore/
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
  url: https://console.aws.amazon.com/mediastore/
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
  url: rules/amazon-mediastore-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-mediastore-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-mediastore-media-workflow.yaml
created: '2026-03-16'
description: AWS Elemental MediaStore is an AWS storage service optimized for media, providing the performance, consistency, and low latency required to deliver live streaming video content at scale.
features:
- description: Optimized object storage for live video with consistent low-latency performance.
  name: High-Performance Media Storage
- description: Organize media assets in containers with fine-grained access control policies.
  name: Container and Object Management
- description: Cross-origin resource sharing configuration for browser-based media players.
  name: CORS Support
- description: Automatically expire and delete media objects based on age or other criteria.
  name: Lifecycle Policies
- description: Detailed access logs for auditing and monitoring media storage activity.
  name: Access Logging
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Use MediaStore as an output destination for live encoded streams.
  name: AWS Elemental MediaLive
- description: Serve MediaStore content via CloudFront for global distribution.
  name: Amazon CloudFront
- description: Control access to MediaStore containers using IAM policies.
  name: AWS IAM
- description: Monitor MediaStore request metrics and latency.
  name: Amazon CloudWatch
jsonld:
- class_count: 83
  name: Amazon Mediastore Mediastore Api Context
  property_count: 27
  slug: amazon-mediastore-mediastore-api-context
layout: provider
modified: '2026-04-19'
name: Amazon MediaStore
rules:
- name: Amazon MediaStore API Rules
  rule_count: 20
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 7
  slug: amazon-mediastore-spectral-rules
skills: []
slug: amazon-mediastore
solutions: []
tags:
- AWS
- Broadcasting
- Media Processing
- Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-mediastore/refs/heads/main/apis.yml
use_cases:
- description: Use as a high-performance origin for live video workflows.
  name: Live Video Origin Storage
- description: Store and manage media files with low-latency access.
  name: Media Asset Management
- description: Serve HLS and DASH segments with consistent performance for video streaming.
  name: Streaming Video Delivery
---
