---
api_count: 6
apis:
- description: The Amazon SageMaker control plane API for creating and managing SageMaker resources including notebook instances, training jobs, models, endpoints, pipelines, experiments, feature groups, and monitor
  name: Amazon SageMaker API
  slug: ''
- description: The Amazon SageMaker AI runtime API for invoking deployed model endpoints to get real-time inference predictions.
  name: Amazon SageMaker Runtime API
  slug: ''
- description: Data plane API operations for the Amazon SageMaker Feature Store supporting put, delete, and retrieve operations for ML features.
  name: Amazon SageMaker Feature Store Runtime API
  slug: ''
- description: Data plane API operations for Amazon SageMaker Metrics for putting and retrieving metrics related to training runs.
  name: Amazon SageMaker Metrics Service API
  slug: ''
- description: APIs for creating and managing Amazon SageMaker geospatial capabilities including earth observation jobs and vector enrichment jobs.
  name: Amazon SageMaker Geospatial API
  slug: ''
- description: SageMaker Edge Manager dataplane service for communicating with active edge agents running ML models on edge devices.
  name: Amazon SageMaker Edge Manager API
  slug: ''
capabilities:
- description: Unified capability for managing the end-to-end machine learning lifecycle including notebook development, training, model management, and endpoint deployment. Used by ML Engineers and Data Scientists.
  name: Amazon SageMaker ML Lifecycle Management
  slug: ml-lifecycle-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: GettingStarted
  url: https://aws.amazon.com/sagemaker/getting-started/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/sagemaker/latest/dg/
- title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/sagemaker/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Pricing
  url: https://aws.amazon.com/sagemaker/pricing/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/sagemaker/faqs/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/
- title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- title: ''
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Security
  url: https://docs.aws.amazon.com/sagemaker/latest/dg/security.html
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-sagemaker
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/sagemaker/
- title: SageMaker HyperPod CLI
  type: CLI
  url: https://github.com/aws/sagemaker-hyperpod-cli
- title: Python SDK (GitHub)
  type: SDK
  url: https://github.com/aws/sagemaker-python-sdk
- title: ''
  type: GitHubRepository
  url: https://github.com/aws/sagemaker-core
- title: ''
  type: GitHubRepository
  url: https://github.com/aws/sagemaker-distribution
- title: ''
  type: SpectralRules
  url: rules/amazon-sagemaker-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-sagemaker-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/ml-lifecycle-management.yaml
- title: ''
  type: Training
  url: https://aws.amazon.com/training/
- title: ''
  type: JSON-LD
  url: json-ld/amazon-sagemaker-context.jsonld
- title: ''
  type: JSONSchema
  url: json-schema/amazon-sagemaker-tag-schema.json
- title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-endpoint-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-model-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-notebook-instance-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-tag-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/amazon-sagemaker-training-job-structure.json
- title: ''
  type: Example
  url: examples/amazon-sagemaker-endpoint-example.json
- title: ''
  type: Example
  url: examples/amazon-sagemaker-model-example.json
- title: ''
  type: Example
  url: examples/amazon-sagemaker-notebook-instance-example.json
- title: ''
  type: Example
  url: examples/amazon-sagemaker-tag-example.json
- title: ''
  type: Example
  url: examples/amazon-sagemaker-training-job-example.json
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/amazon-sagemaker.yaml
created: '2024-01-01'
description: Amazon SageMaker is a fully managed machine learning platform that enables developers and data scientists to build, train, and deploy machine learning models at scale. SageMaker removes the heavy lifting from each step of the machine learning process, providing built-in algorithms, managed Jupyter notebooks, distributed training, automatic model tuning, and one-click deployment to production endpoints with auto-scaling.
features:
- description: Fully integrated development environment for ML work with notebooks, debugging, and experiment tracking.
  name: SageMaker Studio
- description: Purpose-built infrastructure for distributed training that reduces foundation model training time by up to 40%.
  name: SageMaker HyperPod
- description: Hub providing access to foundation models, pre-built algorithms, and one-click deployment.
  name: SageMaker JumpStart
- description: Automated model creation with complete visibility and transparency.
  name: SageMaker Autopilot
- description: No-code visual interface for creating ML models without writing code.
  name: SageMaker Canvas
- description: Store, share, and manage features for machine learning models.
  name: SageMaker Feature Store
- description: Data preparation tool that reduces transformation workflow time significantly.
  name: SageMaker Data Wrangler
- description: Incorporates human feedback throughout the ML lifecycle for data labeling.
  name: SageMaker Ground Truth
- description: Purpose-built CI/CD service for machine learning workflows.
  name: SageMaker Pipelines
- description: Automatically detects concept drift and data quality issues in deployed models.
  name: SageMaker Model Monitor
- description: Provides machine learning explainability and bias detection.
  name: SageMaker Clarify
- description: Streamlines tracking and management of ML experiments.
  name: SageMaker Experiments
- description: Access controls and transparency across the full ML lifecycle with audit trails.
  name: ML Governance
image: ''
integrations:
- description: Store training data, model artifacts, and inference outputs in Amazon S3 data lakes.
  name: Amazon S3
- description: Zero-ETL integration for near real-time data ingestion from Redshift warehouses.
  name: Amazon Redshift
- description: Store and manage Docker containers for custom training and inference environments.
  name: Amazon ECR
- description: Trigger ML inference pipelines and post-processing workflows with Lambda functions.
  name: AWS Lambda
- description: Trigger SageMaker pipelines and workflows based on events.
  name: Amazon EventBridge
- description: Orchestrate multi-step ML workflows using Step Functions state machines.
  name: AWS Step Functions
- description: Lakehouse architecture supporting Apache Iceberg-compatible data tools.
  name: Apache Iceberg
- description: SageMaker Catalog built on Amazon DataZone for data discovery and governance.
  name: Amazon DataZone
- description: Natural language assistance integrated into SageMaker Unified Studio.
  name: Amazon Q Developer
- description: Deploy Hugging Face models directly via SageMaker JumpStart.
  name: Hugging Face
jsonld:
- class_count: 5
  name: Amazon Sagemaker Context
  property_count: 49
  slug: amazon-sagemaker-context
layout: provider
modified: '2026-04-19'
name: Amazon SageMaker
rules:
- name: Amazon SageMaker API Rules
  rule_count: 23
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 11
  slug: amazon-sagemaker-spectral-rules
skills: []
slug: amazon-sagemaker
solutions: []
tags:
- AI
- AWS
- Inference
- Machine Learning
- MLOps
- Training
url: https://aws.amazon.com/sagemaker/
use_cases:
- description: Build custom generative AI applications using proprietary data with foundation model fine-tuning.
  name: Generative AI Applications
- description: Train and deploy ML models across the entire machine learning lifecycle from exploration to production.
  name: ML Model Development
- description: Query and analyze data across unified sources with built-in SQL analytics and data processing.
  name: Data Analytics
- description: Manage data and AI artifacts with fine-grained security controls and compliance tooling.
  name: Enterprise AI Governance
- description: Build and deploy computer vision models for image classification, object detection, and segmentation.
  name: Computer Vision
- description: Train and deploy NLP models for text classification, entity recognition, and language generation.
  name: Natural Language Processing
- description: Build real-time fraud detection models with low-latency inference endpoints.
  name: Fraud Detection
- description: Deploy ML models on edge devices for predictive maintenance use cases.
  name: Predictive Maintenance
---
