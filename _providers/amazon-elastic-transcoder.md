---
api_count: 1
apis:
- description: API for creating and managing media transcoding pipelines, presets, and jobs to convert media files for playback on various devices.
  name: Amazon Elastic Transcoder API
  slug: ''
capabilities:
- description: Unified capability for managing Amazon Elastic Transcoder resources. Combines Amazon Elastic Transcoder APIs for Media Engineer workflows in Media Processing.
  name: Amazon Elastic Transcoder Management
  slug: amazon-elastic-transcoder-capability
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/elastictranscoder/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/elastictranscoder/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/elastictranscoder/
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
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/elastictranscoder/faqs/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: Security
  url: https://aws.amazon.com/security/
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/elastictranscoder
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-elastic-transcoder-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-elastic-transcoder-capability.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/api.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-elastic-transcoder-vocabulary.yaml
created: '2024-01-15'
description: Amazon Elastic Transcoder is media transcoding in the cloud. It is designed to be a highly scalable, easy-to-use, and cost-effective way for developers and businesses to convert or transcode media files from their source format into versions that will play back on devices like smartphones, tablets, and PCs.
features:
- description: Create pipelines that manage media transcoding jobs with configurable input/output settings
  name: Managed Transcoding Pipelines
- description: Use built-in presets optimized for popular devices and formats
  name: Preset Library
- description: Create custom presets for specific output requirements
  name: Custom Presets
- description: Automatically generate thumbnails from video files during transcoding
  name: Thumbnail Generation
- description: Apply HLS content protection and digital rights management
  name: Content Protection
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Use S3 for input and output media file storage
  name: Amazon S3
- description: Receive notifications when transcoding jobs complete
  name: Amazon SNS
- description: Distribute transcoded content via CDN
  name: Amazon CloudFront
- description: Trigger transcoding workflows from Lambda functions
  name: AWS Lambda
jsonld:
- class_count: 67
  name: Amazon Elastic Transcoder Context
  property_count: 108
  slug: amazon-elastic-transcoder-context
layout: provider
modified: '2026-04-19'
name: Amazon Elastic Transcoder
rules:
- name: Amazon Elastic Transcoder API Rules
  rule_count: 20
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 9
  slug: amazon-elastic-transcoder-spectral-rules
skills: []
slug: amazon-elastic-transcoder
solutions: []
tags:
- Amazon Web Services
- AWS
- Media
- Transcoding
- Video
url: https://aws.amazon.com/elastictranscoder/
use_cases:
- description: Convert video files for streaming across different devices and bandwidths
  name: Video-on-Demand Transcoding
- description: Transcode content optimized for smartphone and tablet playback
  name: Mobile Video Delivery
- description: Create adaptive bitrate HLS streams for seamless playback
  name: HLS Streaming
- description: Convert audio files between different formats and bitrates
  name: Audio File Conversion
---
