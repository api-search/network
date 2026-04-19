---
api_count: 1
apis:
- description: API for creating and managing secure collaboration workspaces, memberships, configured tables, analysis templates, and executing privacy-preserving protected queries and jobs.
  name: Amazon Clean Rooms API
  slug: ''
capabilities:
- description: Workflow for establishing and operating secure multi-party data clean rooms on AWS, enabling data analysts and marketing teams to run collaborative analytics without sharing raw data.
  name: Amazon Clean Rooms Secure Data Collaboration
  slug: secure-data-collaboration
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/clean-rooms/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/clean-rooms/
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
  url: https://aws.amazon.com/blogs/big-data/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/cleanrooms/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-clean-rooms
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-clean-rooms-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-clean-rooms-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/secure-data-collaboration.yaml
created: '2026-03-16'
description: Amazon Clean Rooms enables organizations to collaborate and analyze shared datasets without exposing underlying raw data to partners. Create secure data clean rooms in minutes and collaborate with any company while maintaining data privacy through differential privacy, cryptographic computing, and flexible analytics.
features:
- description: Analyze shared datasets without exposing underlying raw data using differential privacy and cryptographic computing.
  name: Privacy-Preserving Analytics
- description: Collaborate with Snowflake and AWS datasets without data movement or ETL pipelines.
  name: Zero-ETL Integration
- description: Execute SQL, PySpark, or ML model queries on partner data with configurable privacy controls.
  name: Protected Queries
- description: Run analytics using SQL, PySpark, or custom ML models with granular access controls.
  name: Flexible Analysis Methods
- description: Audit data usage with analysis logging to track all queries run within a collaboration.
  name: Analysis Logging
- description: Match customer records across applications and channels without sharing PII.
  name: Customer Record Matching
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Store and retrieve collaboration data and query results in S3.
  name: Amazon S3
- description: Zero-ETL integration with Snowflake datasets for cross-platform collaboration.
  name: Snowflake
- description: Configure Glue tables as the underlying data source for Clean Rooms configured tables.
  name: AWS Glue
- description: Run analytics on collaboration results stored in S3 using Athena.
  name: Amazon Athena
- description: Apply ML models within protected Clean Rooms jobs.
  name: Amazon SageMaker
- description: Control access to Clean Rooms resources with IAM policies.
  name: AWS IAM
- description: Audit all Clean Rooms API calls via CloudTrail.
  name: AWS CloudTrail
jsonld:
- class_count: 19
  name: Amazon Clean Rooms Context
  property_count: 32
  slug: amazon-clean-rooms-context
layout: provider
modified: '2026-04-19'
name: Amazon Clean Rooms
rules:
- name: Amazon Clean Rooms API Rules
  rule_count: 29
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 13
  slug: amazon-clean-rooms-spectral-rules
skills: []
slug: amazon-clean-rooms
solutions: []
tags:
- AWS
- Clean Rooms
- Data Collaboration
- Privacy
- Analytics
- Marketing
url: https://raw.githubusercontent.com/api-evangelist/amazon-clean-rooms/refs/heads/main/apis.yml
use_cases:
- description: Measure campaign effectiveness by combining advertiser and publisher data in a privacy-safe environment.
  name: Marketing Measurement
- description: Build comprehensive customer views by combining data from multiple channels and partners.
  name: Customer Insights
- description: Enable multi-company research and product development with secure data sharing.
  name: Collaborative Research
- description: Analyze sensitive financial or health data across organizations for risk prediction without data exposure.
  name: Risk Assessment
- description: Create and activate privacy-safe audience segments across advertising platforms.
  name: Audience Activation
---
