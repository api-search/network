---
api_count: 1
apis:
- description: The Amazon Fraud Detector API provides programmatic access to create and manage detectors, models, event types, entities, labels, outcomes, rules, and variables for automated fraud detection workflows
  name: Amazon Fraud Detector API
  slug: amazon-fraud-detector-api
capabilities:
- description: Orchestrate ML models and business rules for real-time transaction fraud scoring and decision-making.
  name: Amazon Fraud Detector Real-Time Detection
  slug: amazon-fraud-detector-real-time-detection
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/fraud-detector/
- title: ''
  type: Website
  url: https://aws.amazon.com/fraud-detector/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/frauddetector/
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
  url: https://aws.amazon.com/blogs/machine-learning/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/frauddetector/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-fraud-detector
- title: ''
  type: SpectralRules
  url: rules/amazon-fraud-detector-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/fraud-detector.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-fraud-detector-real-time-detection.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-fraud-detector-vocabulary.yaml
- title: ''
  type: JSON-LD
  url: json-ld/amazon-fraud-detector-context.jsonld
created: '2026-03-16'
description: Amazon Fraud Detector is a fully managed service that uses machine learning to identify potentially fraudulent activities and accurately distinguish between legitimate and high-risk transactions. It uses your data and the same technology that Amazon uses to protect its own business from fraud.
features:
- description: Automatically trains and deploys ML models using your historical transaction data without requiring ML expertise.
  name: No ML Expertise Required
- description: Returns fraud scores within milliseconds for integration into transaction approval flows.
  name: Real-Time Fraud Scoring
- description: Online Fraud Insights (OFI), Transaction Fraud Insights (TFI), and Account Takeover Insights (ATI) pre-trained model types.
  name: Pre-Built Models
- description: DETECTORPL rule language allows writing conditional logic using model scores and event variables.
  name: Rule Engine
- description: Variable importance scores explain which factors most influenced a fraud prediction.
  name: Model Explainability
- description: Uses Amazon fraud experience to provide immediate predictions even with limited historical data.
  name: Cold Start Protection
- description: Ingest historical labeled events to continuously improve model accuracy over time.
  name: Event Ingestion
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Store training datasets and export labeled event data to S3 for model training.
  name: Amazon S3
- description: Control access to detectors, models, and predictions using IAM roles and policies.
  name: AWS IAM
- description: Combine Fraud Detector with SageMaker for custom ML pipelines and model integration.
  name: Amazon SageMaker
- description: Monitor prediction volumes, model performance, and API error rates.
  name: Amazon CloudWatch
- description: Encrypt training data and model artifacts with customer-managed KMS keys.
  name: AWS KMS
- description: Route fraud detection outcomes to downstream systems for automated response workflows.
  name: Amazon EventBridge
- description: Send real-time fraud alert notifications to operations teams via SNS topics.
  name: Amazon SNS
jsonld:
- class_count: 5
  name: Amazon Fraud Detector Context
  property_count: 12
  slug: amazon-fraud-detector-context
layout: provider
modified: '2026-04-19'
name: Amazon Fraud Detector
rules:
- name: Amazon Fraud Detector API Rules
  rule_count: 25
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 16
  slug: amazon-fraud-detector-spectral-rules
skills: []
slug: amazon-fraud-detector
solutions: []
tags:
- AWS
- Financial Services
- Fraud Detection
- Machine Learning
- Security
url: https://raw.githubusercontent.com/api-evangelist/amazon-fraud-detector/refs/heads/main/apis.yml
use_cases:
- description: Score credit card and payment transactions in real-time to block fraudulent purchases.
  name: Payment Fraud Detection
- description: Detect unauthorized login attempts and account compromise using behavioral signals.
  name: Account Takeover Prevention
- description: Identify fraudulent new account registrations at signup to prevent synthetic identity fraud.
  name: New Account Fraud
- description: Flag users abusing discount codes, referral bonuses, and promotional offers.
  name: Promotion Abuse Detection
- description: Reduce chargeback rates by blocking high-risk transactions before they complete.
  name: Chargeback Prevention
- description: Score insurance claims for fraudulent patterns in real-time during claim submission.
  name: Insurance Claims Fraud
---
