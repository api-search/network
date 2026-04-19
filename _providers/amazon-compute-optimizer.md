---
api_count: 1
apis:
- description: The Amazon Compute Optimizer API provides 21 operations for analyzing resource utilization and generating rightsizing recommendations for EC2 instances, Auto Scaling groups, EBS volumes, Lambda functi
  name: Amazon Compute Optimizer API
  slug: ''
capabilities:
- description: Workflow capability for AWS resource rightsizing and cost optimization recommendations across EC2 instances, Auto Scaling groups, EBS volumes, Lambda functions, ECS services, and RDS instances. Used b
  name: Amazon Compute Optimizer Resource Optimization
  slug: resource-optimization
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/compute-optimizer/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/compute-optimizer/
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
  url: https://aws.amazon.com/blogs/aws/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/compute-optimizer/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-compute-optimizer-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/resource-optimization.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-compute-optimizer-vocabulary.yaml
created: '2026-03-16'
description: Amazon Compute Optimizer analyzes the configuration and utilization metrics of your AWS resources and provides recommendations to help you identify optimal AWS resource configurations. It uses machine learning to analyze historical utilization metrics and generates rightsizing recommendations for EC2 instances, Auto Scaling groups, EBS volumes, Lambda functions, ECS services on Fargate, and RDS instances to help reduce costs and improve performance.
features:
- description: Get rightsizing recommendations for over-provisioned or under-provisioned EC2 instances based on utilization metrics.
  name: EC2 Instance Recommendations
- description: Optimize Auto Scaling group configurations for cost and performance based on historical usage patterns.
  name: Auto Scaling Group Recommendations
- description: Identify EBS volumes that can be downsized or converted to a different volume type for cost savings.
  name: EBS Volume Recommendations
- description: Optimize Lambda function memory settings based on actual invocation utilization.
  name: Lambda Function Recommendations
- description: Rightsize ECS services running on AWS Fargate for CPU and memory efficiency.
  name: ECS Service Recommendations
- description: Get rightsizing recommendations for RDS database instances and clusters.
  name: RDS Instance Recommendations
- description: Estimate the potential cost savings from implementing rightsizing recommendations.
  name: Savings Opportunity Estimation
- description: Analyze recommendations across all accounts in an AWS Organization.
  name: Organization-Wide Analysis
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Correlate Compute Optimizer recommendations with Cost Explorer data for accurate savings projections.
  name: AWS Cost Explorer
- description: Enroll and analyze recommendations across all accounts in an AWS Organization.
  name: AWS Organizations
- description: Compute Optimizer uses CloudWatch utilization metrics to generate its ML-based recommendations.
  name: Amazon CloudWatch
- description: Complementary service that also provides rightsizing recommendations alongside Compute Optimizer.
  name: AWS Trusted Advisor
- description: Use Systems Manager to implement EC2 instance type changes recommended by Compute Optimizer.
  name: AWS Systems Manager
jsonld:
- class_count: 95
  name: Amazon Compute Optimizer Context
  property_count: 140
  slug: amazon-compute-optimizer-context
layout: provider
modified: '2026-04-19'
name: Amazon Compute Optimizer
rules:
- name: Amazon Compute Optimizer API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 11
  slug: amazon-compute-optimizer-spectral-rules
skills: []
slug: amazon-compute-optimizer
solutions: []
tags:
- AWS
- Cost Optimization
- FinOps
- Machine Learning
- Resource Recommendations
url: https://raw.githubusercontent.com/api-evangelist/amazon-compute-optimizer/refs/heads/main/apis.yml
use_cases:
- description: Identify and eliminate over-provisioned AWS resources to reduce monthly cloud spending.
  name: Cost Reduction
- description: Detect under-provisioned resources that may be causing performance issues and get upgrade recommendations.
  name: Performance Optimization
- description: Generate cross-account optimization reports to support FinOps practices and showback/chargeback processes.
  name: FinOps Reporting
- description: Use recommendations to rightsize resources before or after migrating workloads to AWS.
  name: Migration Planning
- description: Integrate recommendations into CI/CD pipelines to continuously monitor and optimize resource provisioning.
  name: Continuous Optimization
---
