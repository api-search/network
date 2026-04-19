---
api_count: 1
apis:
- description: 'The AWS App Mesh API provides programmatic access to configure and manage service mesh resources for microservices. It enables developers to create and manage meshes, virtual services, virtual nodes, '
  name: AWS App Mesh API
  slug: ''
capabilities:
- description: Workflow for managing Amazon App Mesh API resources.
  name: App Mesh Management
  slug: app-mesh-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/app-mesh/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/app-mesh/
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
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/appmesh/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
- title: ''
  type: Status
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-app-mesh-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/app-mesh-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-app-mesh-vocabulary.yaml
created: '2024-01-15'
description: AWS App Mesh is a service mesh that provides application-level networking to make it easy for your services to communicate with each other across multiple types of compute infrastructure.
features:
- description: Create and manage service meshes that define the logical boundary for network traffic between microservices.
  name: Service Mesh Management
- description: Define virtual services that act as logical routers for microservice traffic, abstracting the underlying routing logic.
  name: Virtual Service Configuration
- description: Configure virtual routers and routes to implement traffic management policies including weighted routing and retry policies.
  name: Traffic Routing Control
- description: Manage virtual nodes representing microservice task groups with service discovery and health check configurations.
  name: Virtual Node Management
- description: Configure access logs and tracing for end-to-end visibility of traffic flowing through the service mesh.
  name: Observability Integration
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Deploy App Mesh sidecar proxies alongside ECS tasks for automatic traffic interception and routing.
  name: AWS ECS
- description: Run App Mesh with Kubernetes via the App Mesh Controller for Kubernetes for native K8s integration.
  name: AWS EKS
- description: Use X-Ray for distributed tracing of requests flowing through the App Mesh service mesh.
  name: AWS X-Ray
- description: Integrate App Mesh with Cloud Map for service discovery across ECS, EKS, and EC2 compute.
  name: AWS Cloud Map
jsonld:
- class_count: 0
  name: Amazon App Mesh Context
  property_count: 1
  slug: amazon-app-mesh-context
layout: provider
modified: '2026-04-19'
name: Amazon App Mesh
rules:
- name: Amazon App Mesh API Rules
  rule_count: 3
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 0
  slug: amazon-app-mesh-spectral-rules
skills: []
slug: amazon-app-mesh
solutions: []
tags:
- AWS
- Microservices
- Networking
- Service Mesh
url: https://raw.githubusercontent.com/api-evangelist/amazon-app-mesh/refs/heads/main/apis.yml
use_cases:
- description: Control traffic routing between microservices with weighted routing, canary deployments, and circuit breaking.
  name: Microservices Traffic Management
- description: Integrate App Mesh with AWS Cloud Map for automatic service discovery across compute types.
  name: Service Discovery Integration
- description: Connect services running on ECS, EKS, and EC2 instances within a unified service mesh for consistent networking policies.
  name: Multi-Cluster Networking
---
