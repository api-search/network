---
api_count: 1
apis:
- description: The Amazon Kinesis Video Streams API provides programmatic access to create and manage video streams, signaling channels, and WebRTC connections for streaming video from connected devices to AWS.
  name: Amazon Kinesis Video Streams API
  slug: amazon-kinesis-video-streams-api
capabilities:
- description: Unified workflow capability for Amazon Kinesis Video Streams combining resource management and operations.
  name: Amazon Kinesis Video Streams Workflow
  slug: amazon-kinesis-video-streams-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/kinesis/video-streams/
- title: ''
  type: Portal
  url: https://aws.amazon.com/kinesis/video-streams/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/kinesisvideostreams/
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
  url: https://aws.amazon.com/blogs/media/tag/amazon-kinesis-video-streams/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/kinesisvideo/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: Status
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-kinesis-video-streams-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-kinesis-video-streams-workflow.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-kinesis-video-streams-vocabulary.yaml
created: '2026-03-16'
description: Amazon Kinesis Video Streams makes it easy to securely stream video from connected devices to AWS for analytics, machine learning, playback, and other processing. It automatically provisions and elastically scales all the infrastructure needed to ingest streaming video data from millions of devices.
features:
- description: Stores, encrypts, and indexes video data in streams and allows access to data through APIs.
  name: Durable Video Storage
- description: Provides signaling and relay services for two-way real-time media streaming between WebRTC-enabled devices.
  name: WebRTC Support
- description: Integrates with Amazon Rekognition Video for real-time computer vision and object detection.
  name: ML Integration
- description: Automatically provisions and elastically scales infrastructure to ingest video from millions of devices.
  name: Scalable Ingestion
- description: Supports live and on-demand playback with HLS streaming.
  name: Playback
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Analyze streaming video with computer vision for object and face detection.
  name: Amazon Rekognition
- description: Connect IoT cameras and devices to stream video to Amazon Kinesis Video Streams.
  name: AWS IoT Core
- description: Use video data for machine learning model training and inference.
  name: Amazon SageMaker
jsonld:
- class_count: 2
  name: Amazon Kinesis Video Streams Context
  property_count: 7
  slug: amazon-kinesis-video-streams-context
layout: provider
modified: '2026-04-19'
name: Amazon Kinesis Video Streams
rules:
- name: Amazon Kinesis Video Streams API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 7
  slug: amazon-kinesis-video-streams-spectral-rules
skills: []
slug: amazon-kinesis-video-streams
solutions: []
tags:
- AWS
- IoT
- Machine Learning
- Media
- Video Streaming
url: https://raw.githubusercontent.com/api-evangelist/amazon-kinesis-video-streams/refs/heads/main/apis.yml
use_cases:
- description: Stream video from security cameras for real-time monitoring and alerts.
  name: Smart Home Security
- description: Monitor manufacturing processes and equipment with video analytics.
  name: Industrial Monitoring
- description: Ingest sensor and video streams from autonomous vehicles for ML model training.
  name: Autonomous Vehicles
- description: Deliver live video streams to viewers with low latency using WebRTC.
  name: Live Video Streaming
---
