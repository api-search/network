---
api_count: 1
apis:
- description: 'The Amazon Mechanical Turk API provides programmatic access to create and manage HITs, qualifications, workers, assignments, and bonuses for coordinating crowdsourced human intelligence tasks. Covers '
  name: Amazon Mechanical Turk API
  slug: amazon-mturk-api
capabilities:
- description: Workflow capability for data scientists and researchers to create HITs, manage worker assignments, approve work, and coordinate crowdsourced human intelligence tasks through Amazon Mechanical Turk.
  name: Amazon Mechanical Turk - Crowdsourcing Workflow
  slug: crowdsourcing-workflow
common:
- title: ''
  type: Portal
  url: https://www.mturk.com/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/mturk/
- title: ''
  type: TermsOfService
  url: https://www.mturk.com/participation-agreement
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://www.mturk.com/contact
- title: ''
  type: Blog
  url: https://blog.mturk.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: SignUp
  url: https://www.mturk.com/get-started
- title: ''
  type: Login
  url: https://requester.mturk.com/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://www.mturk.com/contact
- title: ''
  type: SpectralRules
  url: rules/amazon-mechanical-turk-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-mechanical-turk-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/crowdsourcing-workflow.yaml
created: '2026-03-16'
description: Amazon Mechanical Turk (MTurk) is a crowdsourcing marketplace that makes it easier for individuals and businesses to coordinate the use of human intelligence to perform tasks that computers are currently unable to do well. It enables access to a global, on-demand, 24x7 workforce for data labeling, content moderation, surveys, transcription, and machine learning training data collection.
features:
- description: Create and manage discrete units of work distributed to the global MTurk worker population.
  name: Human Intelligence Tasks (HITs)
- description: Define custom qualification tests and requirements to target the right worker pool for each task type.
  name: Qualification Types
- description: Review submitted assignments and approve or reject work with feedback to workers.
  name: Assignment Review and Approval
- description: Award bonus payments to workers for exceptional task completion beyond the base HIT reward.
  name: Worker Bonuses
- description: Send targeted messages to specific workers to communicate task updates or instructions.
  name: Worker Notifications
- description: Prevent specific workers from accessing your HITs when quality does not meet requirements.
  name: Worker Blocks
- description: Test HIT templates and requester workflows using the MTurk sandbox before going to production.
  name: Sandbox Environment
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Use MTurk workers directly within SageMaker Ground Truth for ML data labeling jobs.
  name: Amazon SageMaker Ground Truth
- description: Trigger Lambda functions on HIT completion events for automated downstream processing.
  name: AWS Lambda
- description: Store HIT input data and collect worker output files in S3 buckets.
  name: Amazon S3
- description: Monitor MTurk task completion rates and worker performance metrics.
  name: Amazon CloudWatch
- description: Control requester access to the MTurk API through IAM policies and roles.
  name: AWS IAM
jsonld:
- class_count: 96
  name: Amazon Mechanical Turk Context
  property_count: 120
  slug: amazon-mechanical-turk-context
layout: provider
modified: '2026-04-19'
name: Amazon Mechanical Turk
rules:
- name: Amazon Mechanical Turk API Rules
  rule_count: 18
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 7
  slug: amazon-mechanical-turk-spectral-rules
skills: []
slug: amazon-mechanical-turk
solutions: []
tags:
- AWS
- Crowdsourcing
- Human Intelligence
- Labor
- Machine Learning
- Tasks
url: https://raw.githubusercontent.com/api-evangelist/amazon-mechanical-turk/refs/heads/main/apis.yml
use_cases:
- description: Label images, text, audio, and video to create training datasets for machine learning models.
  name: Machine Learning Data Labeling
- description: Review and moderate user-generated content for inappropriate material at scale.
  name: Content Moderation
- description: Transcribe audio and video recordings using human workers for high accuracy.
  name: Transcription Services
- description: Conduct surveys and collect research data from a diverse global workforce.
  name: Survey and Research Data Collection
- description: Validate and verify structured data for accuracy using human review.
  name: Data Validation and Quality Assurance
- description: Generate labeled sentiment data for training NLP and sentiment analysis models.
  name: Sentiment Analysis Training Data
---
