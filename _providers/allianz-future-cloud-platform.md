---
api_count: 2
apis:
- description: Platform engineering APIs for managing cloud-native services on the Allianz Future Cloud Platform. Provides capabilities for service registration, deployment management, observability configuration, a
  name: Allianz Future Cloud Platform Services API
  slug: platform-services-api
- description: 'Insurance policy microservice running on the Allianz Future Cloud Platform. Provides REST APIs for policy lifecycle management including creation, endorsements, renewals, and cancellations built with '
  name: Allianz Insurance Policy Microservice API
  slug: policy-microservice-api
capabilities:
- description: Workflow capability for platform engineering and DevOps teams operating the Allianz Future Cloud Platform, combining service management, deployment automation, observability, and infrastructure provis
  name: Allianz Cloud Platform Operations
  slug: cloud-platform-operations
common:
- title: ''
  type: Website
  url: https://www.allianz.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/allianz
- title: ''
  type: Documentation
  url: https://architecture.cncf.io/architectures/allianz/
- title: ''
  type: SpectralRules
  url: rules/allianz-future-cloud-platform-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/allianz-future-cloud-platform-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/cloud-platform-operations.yaml
created: '2024-01-15'
description: The Allianz Future Cloud Platform is an internal developer platform powering cloud-native insurance microservices at Allianz. Built on Kubernetes and AWS, it provides platform engineering capabilities including service deployment, infrastructure management, observability, and GitOps automation across Allianz's global insurance operations.
features:
- description: Internal developer platform built on Kubernetes (EKS) providing standardized deployment, scaling, and orchestration for insurance microservices.
  name: Kubernetes Platform Engineering
- description: ArgoCD and Tekton-based CI/CD pipelines enabling GitOps workflows for continuous delivery of insurance applications.
  name: GitOps Deployment
- description: Terraform and Crossplane-based infrastructure management enabling repeatable, auditable cloud resource provisioning.
  name: Infrastructure as Code
- description: Prometheus, Grafana, and OpenTelemetry based observability platform providing metrics, tracing, and alerting for platform services.
  name: Observability Stack
- description: Namespace-level multi-tenancy supporting multiple insurance product teams on shared Kubernetes infrastructure.
  name: Multi-tenant Architecture
- description: AWS MSK (Managed Kafka) for high-throughput event streaming between insurance microservices and downstream consumers.
  name: Event Streaming
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Primary cloud provider with EKS, MSK, ElastiCache Redis, and storage services powering the platform.
  name: Amazon Web Services
- description: GitOps continuous delivery for declarative application deployment and state synchronization.
  name: ArgoCD
- description: Infrastructure as code for cloud resource provisioning and management integrated with Atlantis for PR automation.
  name: Terraform
- description: Multi-cloud resource management extending Kubernetes for cloud-agnostic infrastructure provisioning.
  name: Crossplane
- description: Distributed tracing and metrics collection across microservices for observability and performance analysis.
  name: OpenTelemetry
- description: AWS MSK for event-driven communication between insurance microservices and downstream systems.
  name: Apache Kafka
jsonld:
- class_count: 12
  name: Allianz Future Cloud Platform Context
  property_count: 35
  slug: allianz-future-cloud-platform-context
layout: provider
modified: '2026-04-19'
name: Allianz Future Cloud Platform
rules:
- name: Allianz Future Cloud Platform API Rules
  rule_count: 24
  severity_counts:
    error: 15
    hint: 0
    info: 3
    warn: 6
  slug: allianz-future-cloud-platform-spectral-rules
skills: []
slug: allianz-future-cloud-platform
solutions: []
tags:
- Cloud Platform
- Enterprise
- Financial Services
- Insurance
- Platform Engineering
- Kubernetes
url: https://raw.githubusercontent.com/api-evangelist/allianz-future-cloud-platform/refs/heads/main/apis.yml
use_cases:
- description: Deploy and manage Kotlin and Java insurance microservices on the platform with standardized CI/CD pipelines and GitOps workflows.
  name: Insurance Microservice Deployment
- description: Onboard new insurance product teams onto the shared Kubernetes platform with pre-configured namespaces and RBAC policies.
  name: Platform Onboarding
- description: Configure monitoring dashboards and alerting for insurance services using the platform's built-in Prometheus and Grafana stack.
  name: Observability and Monitoring
- description: Provision cloud infrastructure resources using Terraform and Crossplane through the platform's infrastructure API.
  name: Infrastructure Provisioning
---
