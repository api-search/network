---
api_count: 1
apis:
- description: The EC2 Image Builder API provides programmatic access to create and manage image pipelines, recipes, components, infrastructure configurations, and distribution settings for automated VM and containe
  name: Amazon EC2 Image Builder API
  slug: ''
capabilities:
- description: Unified capability for managing EC2 Image Builder pipelines, recipes, and components for DevOps engineers.
  name: Amazon EC2 Image Builder Image Pipeline Management
  slug: ec2-image-builder-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/developer/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/imagebuilder/
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
  url: https://aws.amazon.com/blogs/compute/tag/ec2-image-builder/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/imagebuilder/
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
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/ec2-image-builder
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
  url: rules/amazon-ec2-image-builder-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-ec2-image-builder-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/ec2-image-builder-management.yaml
created: '2026-03-16'
description: EC2 Image Builder simplifies the building, testing, and deployment of Virtual Machine and container images for use on AWS or on-premises. It provides an automated pipeline to create and maintain secure, up-to-date server images without requiring scripting expertise.
features:
- description: Define end-to-end image creation workflows with build, test, and distribution phases without scripting expertise.
  name: Automated Image Pipelines
- description: Compose reusable image definitions from components including OS, software packages, and custom scripts.
  name: Image Recipes
- description: Catalog of pre-built AWS-managed and custom components for common software installation and configuration tasks.
  name: Component Library
- description: Run automated tests on images before distribution to validate software, security, and compliance requirements.
  name: Automated Testing
- description: Automatically distribute approved images to multiple AWS regions with configurable permissions.
  name: Multi-Region Distribution
- description: Build, test, and publish container images to Amazon ECR alongside traditional AMI workflows.
  name: Container Image Support
- description: Built-in support for CIS Benchmarks and DISA STIG security hardening standards for compliance.
  name: CIS and STIG Hardening
- description: Automatically rebuild images on a schedule to incorporate OS patches and security updates.
  name: Scheduled Builds
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Produces AMIs that can be launched as EC2 instances across regions and accounts.
  name: Amazon EC2
- description: Publishes container images to ECR repositories as part of container image build pipelines.
  name: Amazon ECR
- description: Uses SSM Agent for image build and test execution on temporary build instances.
  name: AWS Systems Manager
- description: Integrates with Amazon Inspector for automated vulnerability scanning of built images.
  name: Amazon Inspector
- description: Encrypts AMIs and snapshots using KMS customer-managed keys during distribution.
  name: AWS Key Management Service
- description: Logs all Image Builder API calls for auditing and compliance tracking.
  name: AWS CloudTrail
jsonld:
- class_count: 50
  name: Amazon Ec2 Image Builder Context
  property_count: 200
  slug: amazon-ec2-image-builder-context
layout: provider
modified: '2026-04-19'
name: Amazon EC2 Image Builder
rules:
- name: Amazon EC2 Image Builder API Rules
  rule_count: 19
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 9
  slug: amazon-ec2-image-builder-spectral-rules
skills: []
slug: amazon-ec2-image-builder
solutions: []
tags:
- Amazon Web Services
- Automation
- AWS
- Container Images
- EC2
- Image Building
- Virtual Machine Images
url: https://aws.amazon.com/image-builder/
use_cases:
- description: Create and maintain standardized, secure, and up-to-date base AMIs for all EC2 workloads across the organization.
  name: Golden AMI Management
- description: Automatically rebuild images with the latest OS security patches and distribute them across regions.
  name: Security Patch Automation
- description: Apply CIS or STIG security benchmarks to create compliant images for regulated environments.
  name: Compliance Image Hardening
- description: Maintain secure, up-to-date container base images and publish them to ECR for development teams.
  name: Container Base Image Management
- description: Build images in a central account and distribute them to multiple AWS accounts and regions.
  name: Multi-Account Image Sharing
---
