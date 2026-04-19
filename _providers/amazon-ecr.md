---
api_count: 1
apis:
- description: API for managing Amazon ECR repositories, images, and related resources.
  name: Amazon ECR API
  slug: ''
capabilities:
- description: Unified capability for managing ECR repositories, container images, and lifecycle policies for DevOps engineers.
  name: Amazon ECR Container Registry Management
  slug: ecr-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-web-services
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Security
  url: https://aws.amazon.com/security/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-ecr-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-ecr-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/ecr-management.yaml
created: '2024-01-15'
description: Amazon Elastic Container Registry (ECR) is a fully managed container registry that makes it easy to store, manage, share, and deploy container images and artifacts. ECR eliminates the need to operate your own container repositories or worry about scaling the underlying infrastructure, and integrates with Amazon ECS and Amazon EKS for simplified development to production workflows.
features:
- description: Eliminate the need to operate your own container repositories or worry about scaling infrastructure.
  name: Fully Managed Registry
- description: Automated vulnerability assessment via Amazon Inspector integration for continuous image security.
  name: Image Vulnerability Scanning
- description: Automatically expire and delete images based on rules to reduce storage costs.
  name: Lifecycle Policies
- description: Replicate images to registries in other AWS accounts and regions for availability.
  name: Cross-Account Replication
- description: Store and manage OCI-compliant artifacts including Helm charts and SBOMs.
  name: OCI Artifact Support
- description: Sign and verify container images automatically without additional infrastructure.
  name: Image Signing
- description: Cache upstream public registry images in ECR for reduced egress costs and improved availability.
  name: Pull Through Cache
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Natively integrated with ECS for pulling container images to run tasks and services.
  name: Amazon ECS
- description: Authenticate and pull container images from ECR for Kubernetes workloads.
  name: Amazon EKS
- description: Continuous vulnerability scanning of images stored in ECR for security compliance.
  name: Amazon Inspector
- description: Build and push container images to ECR as part of CI/CD build processes.
  name: AWS CodeBuild
- description: Resource-based policies control who can push, pull, and manage images in ECR.
  name: AWS IAM
jsonld:
- class_count: 4
  name: Amazon Ecr Context
  property_count: 22
  slug: amazon-ecr-context
layout: provider
modified: '2026-04-19'
name: Amazon ECR
rules:
- name: Amazon ECR API Rules
  rule_count: 28
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 13
  slug: amazon-ecr-spectral-rules
skills: []
slug: amazon-ecr
solutions: []
tags:
- Amazon Web Services
- AWS
- Container Images
- Container Registry
- Containers
- Docker
- ECR
- OCI
url: https://aws.amazon.com/ecr/
use_cases:
- description: Store container images in ECR and deploy to ECS or EKS as part of automated pipelines.
  name: CI/CD Pipeline Integration
- description: Automated vulnerability scanning and image signing for security-compliant container deployments.
  name: Security and Compliance
- description: Replicate images across regions for low-latency pulls and improved resilience.
  name: Multi-Region Deployments
- description: Store Helm charts as OCI artifacts for Kubernetes application deployment management.
  name: Helm Chart Repository
- description: Manage image retention policies to keep registries clean and reduce storage costs.
  name: Image Lifecycle Management
---
