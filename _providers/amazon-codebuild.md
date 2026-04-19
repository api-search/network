---
api_count: 1
apis:
- description: 'The Amazon CodeBuild REST API enables programmatic management of build projects, builds, report groups, and source credentials. Create and configure build projects with custom environments, start and '
  name: Amazon CodeBuild API
  slug: amazon-codebuild-api
capabilities:
- description: Unified workflow for DevOps teams to manage build projects, run builds, monitor build status, and integrate with CI/CD pipelines using Amazon CodeBuild.
  name: Amazon CodeBuild CI/CD
  slug: amazon-codebuild-cicd
common:
- title: ''
  type: GettingStarted
  url: https://aws.amazon.com/codebuild/getting-started/
- title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control.html
- title: ''
  type: Pricing
  url: https://aws.amazon.com/codebuild/pricing/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/codebuild/
- title: ''
  type: Portal
  url: https://aws.amazon.com/codebuild/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/codebuild/latest/userguide/
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
  type: FAQ
  url: https://aws.amazon.com/codebuild/faqs/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/gp/aws/developer/registration/index.html
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-codebuild
- title: ''
  type: SpectralRules
  url: rules/amazon-codebuild-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-codebuild-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-codebuild-cicd.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-codebuild-context.jsonld
created: '2024-01-15'
description: AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces ready-to-deploy software packages. CodeBuild scales continuously and processes multiple builds concurrently so your builds are not left waiting in a queue. It supports popular build environments for Java, Python, Node.js, Ruby, Go, Android, .NET Core, Docker, and more. CodeBuild integrates with AWS CodePipeline, GitHub, Bitbucket, and other source providers for end-to-end CI/CD workflows.
features:
- description: No need to provision, manage, or scale build servers. AWS handles all infrastructure management so you can focus on writing code.
  name: Fully Managed Build Service
- description: Automatically scales to meet peak build demand. Processes multiple builds concurrently so builds are never left waiting in a queue.
  name: Continuous Scaling
- description: Out-of-the-box build environments for Java, Python, Node.js, Ruby, Go, Android, .NET Core, Docker, and more. Customize with your own build tools.
  name: Pre-configured Build Environments
- description: Run multiple related builds in parallel as a batch sharing the same source configuration and retrieve combined results for the entire batch.
  name: Build Batches
- description: Collect and analyze test results from unit tests, integration tests, and code coverage reports. Track test trends and identify flaky tests.
  name: Test Reports
- description: Integrate with CodeCommit, GitHub, GitHub Enterprise, GitLab, Bitbucket, and Amazon S3 as source providers with webhook support for automatic build triggering.
  name: Source Integration
- description: Run builds inside a VPC for access to private resources, configuring VPC settings including subnets and security groups for build environments.
  name: VPC Support
- description: Cache build dependencies in Amazon S3 or locally within the build environment to speed up subsequent builds and reduce build times.
  name: Build Caching
- description: Use your own Docker images as build environments, pulling from Amazon ECR or Docker Hub for fully customized build configurations.
  name: Custom Build Environments
- description: Pay only for the build minutes you consume with no upfront costs or long-term commitments for on-demand build capacity.
  name: Pay-Per-Build Pricing
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Add CodeBuild as build or test actions in CodePipeline deployment stages.
  name: AWS CodePipeline
- description: Use CodeCommit repositories as source for CodeBuild projects with webhook triggers.
  name: AWS CodeCommit
- description: Integrate with GitHub repositories and pull request builds using webhooks.
  name: GitHub
- description: Use GitLab repositories as source for CodeBuild projects.
  name: GitLab
- description: Integrate with Bitbucket repositories for cloud-based CI.
  name: Bitbucket
- description: Pull custom build environment images from ECR and push built container images.
  name: Amazon ECR
- description: Store build artifacts and cache build dependencies in S3 buckets.
  name: Amazon S3
- description: Control access to build projects and builds with fine-grained IAM permissions.
  name: AWS IAM
- description: Monitor build metrics and set alarms on build duration, failure rates, and queued builds.
  name: Amazon CloudWatch
- description: Securely inject secrets and environment variables into build environments.
  name: AWS Secrets Manager
jsonld:
- class_count: 11
  name: Amazon Codebuild Context
  property_count: 29
  slug: amazon-codebuild-context
layout: provider
modified: '2026-04-19'
name: Amazon CodeBuild
rules:
- name: Amazon CodeBuild API Rules
  rule_count: 18
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 8
  slug: amazon-codebuild-spectral-rules
skills: []
slug: amazon-codebuild
solutions: []
tags:
- Amazon
- AWS
- CI/CD
- Build
- Continuous Integration
- DevOps
- Testing
url: https://raw.githubusercontent.com/api-evangelist/amazon-codebuild/refs/heads/main/apis.yml
use_cases:
- description: Automatically compile, test, and validate code changes on every commit to catch issues early and maintain code quality across development teams.
  name: Continuous Integration Pipelines
- description: Run unit tests, integration tests, and end-to-end tests as part of every build to ensure code correctness and prevent regressions.
  name: Automated Testing
- description: Build and push Docker container images to Amazon ECR as part of a containerized application deployment workflow.
  name: Docker Image Building
- description: Use build batches to test across multiple runtime versions or configurations in parallel, identifying compatibility issues efficiently.
  name: Multi-Environment Build Matrix
- description: Use CodeBuild as the build and test stage in an AWS CodePipeline CD pipeline for fully automated code delivery from commit to deployment.
  name: AWS CodePipeline Integration
---
