---
api_count: 1
apis:
- description: The Amazon CodeGuru Profiler REST API.
  name: Amazon CodeGuru Profiler API
  slug: amazon-codeguru-profiler-api
capabilities:
- description: Unified workflow for DevOps teams to manage profiling groups, retrieve CPU and heap profile data, and act on performance recommendations for production applications.
  name: Amazon CodeGuru Profiler Application Performance Profiling
  slug: amazon-codeguru-profiler-application-performance
common:
- title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/codeguru/profiler
- title: ''
  type: Pricing
  url: https://aws.amazon.com/codeguruprofiler/pricing/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/codeguruprofiler/
- title: ''
  type: Portal
  url: https://aws.amazon.com/codeguruprofiler/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/codeguruprofiler/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/devops/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/gp/aws/developer/registration/index.html
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: SpectralRules
  url: rules/amazon-codeguru-profiler-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-codeguru-profiler-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-codeguru-profiler-application-performance.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-codeguru-profiler-context.jsonld
created: '2026-03-16'
description: Amazon CodeGuru Profiler collects runtime performance data from your live applications, providing recommendations to help you reduce CPU utilization, cut costs, and improve application performance. The profiler analyzes your application's CPU and heap usage to identify the most expensive lines of code and offers actionable recommendations.
features:
- description: Continuously profile application CPU utilization and heap usage in production without significant overhead.
  name: Application Profiling
- description: Receive actionable recommendations from machine learning models identifying expensive code paths and resource inefficiencies.
  name: AI-Powered Recommendations
- description: Visualize CPU usage with flame graphs that highlight the most resource-intensive code paths.
  name: Flame Graphs
- description: Automatically detect anomalies in application performance and CPU utilization patterns.
  name: Anomaly Detection
- description: Profile JVM-based applications and Python applications using language-specific profiling agents.
  name: Java and Python Support
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Profile Lambda function execution to identify performance bottlenecks.
  name: AWS Lambda
- description: Profile containerized applications running on ECS.
  name: Amazon ECS
- description: Profile applications running on EC2 instances.
  name: Amazon EC2
- description: Combine profiling insights with code review recommendations.
  name: AWS CodeGuru Reviewer
jsonld:
- class_count: 71
  name: Amazon Codeguru Profiler Context
  property_count: 71
  slug: amazon-codeguru-profiler-context
layout: provider
modified: '2026-04-19'
name: Amazon CodeGuru Profiler
rules:
- name: Amazon CodeGuru Profiler API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 4
  slug: amazon-codeguru-profiler-spectral-rules
skills: []
slug: amazon-codeguru-profiler
solutions: []
tags:
- Amazon
- AWS
- Application Performance
- Profiling
- DevOps
- Machine Learning
url: https://raw.githubusercontent.com/api-evangelist/amazon-codeguru-profiler/refs/heads/main/apis.yml
use_cases:
- description: Identify and eliminate the most expensive code paths consuming CPU in live production applications.
  name: Production Performance Optimization
- description: Reduce compute costs by optimizing code that consumes excessive CPU time and cloud resources.
  name: Cost Reduction
- description: Investigate application latency issues by profiling which code paths contribute most to request processing time.
  name: Latency Investigation
---
