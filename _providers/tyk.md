---
api_count: 4
apis:
- description: The Tyk Gateway API provides a RESTful interface for managing API definitions, keys, certificates, and health checks directly on a Tyk Gateway node. It is used to configure and operate the gateway pro
  name: Tyk Gateway API
  slug: tyk-gateway-api
- description: The Tyk Dashboard API is a superset of the Gateway API providing programmatic access to a centralized database of API definitions, keys, policies, users, and organizations. It is the primary integrati
  name: Tyk Dashboard API
  slug: tyk-dashboard-api
- description: The Tyk Dashboard Admin API provides super-administrative access to the Tyk Dashboard, enabling management of organizations and system-level configuration. It is used for bootstrapping and managing mu
  name: Tyk Dashboard Admin API
  slug: tyk-dashboard-admin-api
- description: The Tyk Multi Data Centre Bridge (MDCB) API enables synchronization of API configurations, keys, and policies across geographically distributed Tyk Gateway clusters. It provides a control plane for ma
  name: Tyk MDCB API
  slug: tyk-mdcb-api
capabilities:
- description: Unified API management workflow combining Gateway and Dashboard APIs for API developers and platform engineers to manage API definitions, keys, policies, and portal configurations.
  name: Tyk API Management
  slug: api-management
- description: Platform administration workflow combining Dashboard Admin and MDCB APIs for platform administrators to manage organizations, multi-data center deployments, and system diagnostics.
  name: Tyk Platform Administration
  slug: platform-administration
common:
- title: ''
  type: Portal
  url: https://tyk.io/
- title: ''
  type: Documentation
  url: https://tyk.io/docs/
- title: ''
  type: GettingStarted
  url: https://tyk.io/docs/getting-started/
- title: ''
  type: Authentication
  url: https://tyk.io/docs/basic-config-and-security/security/authentication-authorization/
- title: ''
  type: Blog
  url: https://tyk.io/blog/
- title: ''
  type: ChangeLog
  url: https://tyk.io/docs/developer-support/release-notes/dashboard
- title: ''
  type: GitHubOrganization
  url: https://github.com/TykTechnologies
- title: ''
  type: GitHubRepository
  url: https://github.com/TykTechnologies/tyk
- title: ''
  type: Support
  url: https://community.tyk.io/
- title: ''
  type: FAQ
  url: https://tyk.io/docs/frequently-asked-questions/
- title: ''
  type: Pricing
  url: https://tyk.io/price-comparison/
- title: ''
  type: CLI
  url: https://github.com/TykTechnologies/tyk-cli
- title: Go Gateway SDK
  type: SDK
  url: https://github.com/TykTechnologies/tyk
- title: ''
  type: SpectralRules
  url: rules/tyk-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/tyk-vocabulary.yaml
created: '2026-03-18'
description: Tyk is an open-source API gateway and management platform supporting REST, GraphQL, gRPC, and Async APIs with a developer portal, analytics, and flexible deployment across cloud, on-premise, and hybrid environments.
features:
- description: High-performance, open-source API gateway supporting REST, GraphQL, gRPC, TCP, and async APIs with low-latency request proxying.
  name: API Gateway
- description: Configurable rate limiting and throttling policies to protect backend services from traffic spikes and abuse.
  name: Rate Limiting
- description: Multiple authentication methods including API keys, JWT, OAuth 2.0, mutual TLS, OpenID Connect, and basic auth.
  name: Authentication
- description: Real-time API analytics, traffic monitoring, and detailed logging with export to multiple backend stores.
  name: Analytics and Monitoring
- description: Customizable developer portal for API documentation, key management, and developer onboarding.
  name: Developer Portal
- description: Native GraphQL proxy and Universal Data Graph for federating REST and GraphQL APIs into a single graph endpoint.
  name: GraphQL Support
- description: Built-in support for API versioning with URL, header, and query parameter-based version routing.
  name: API Versioning
- description: Centralized access control policies for managing rate limits, quotas, and access rights across multiple APIs.
  name: Policy Management
- description: MDCB enables synchronization of API configurations and keys across geographically distributed gateway clusters.
  name: Multi Data Center
- description: Extensible middleware plugin system supporting Go, Python, JavaScript, Lua, and gRPC-based custom plugins.
  name: Plugin System
- description: Tyk AI Studio provides an AI gateway for managing, governing, and interacting with AI models across your organization.
  name: AI Gateway
image: /assets/icons/tyk.png
integrations:
- description: Tyk Operator provides native Kubernetes integration for managing API definitions and policies as custom resources.
  name: Kubernetes
- description: Infrastructure-as-code provider for managing Tyk configurations through Terraform.
  name: Terraform
- description: Integration with Keycloak for OAuth 2.0 and OpenID Connect authentication flows.
  name: Keycloak
- description: Support for Auth0 as an identity provider for JWT validation and OAuth 2.0 token management.
  name: Auth0
- description: Export gateway metrics to Prometheus for monitoring and alerting with Grafana dashboards.
  name: Prometheus
- description: Distributed tracing integration with OpenTelemetry for end-to-end request visibility.
  name: OpenTelemetry
- description: Backstage plugin for viewing and managing Tyk API definitions from within the Backstage developer portal.
  name: Backstage
- description: CI/CD integration for automated API deployment and configuration updates through Jenkins pipelines.
  name: Jenkins
- description: Ansible playbooks for automated Tyk gateway and dashboard provisioning and configuration.
  name: Ansible
- description: Official Helm charts for deploying Tyk components on Kubernetes clusters.
  name: Helm Charts
jsonld:
- class_count: 0
  name: Tyk Gateway Context
  property_count: 0
  slug: tyk-gateway-context
- class_count: 0
  name: Tyk Mdcb Context
  property_count: 0
  slug: tyk-mdcb-context
layout: provider
modified: '2026-04-19'
name: Tyk
rules:
- name: Tyk API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: tyk-spectral-rules
skills: []
slug: tyk
solutions: []
tags:
- API Gateway
- API Management
- GraphQL
- Open Source
url: https://raw.githubusercontent.com/api-evangelist/tyk/refs/heads/main/apis.yml
use_cases:
- description: Enable API-as-a-product strategies with tiered plans, usage tracking, and developer self-service through the portal.
  name: API Monetization
- description: Centralize traffic management, authentication, and observability for microservices architectures.
  name: Microservices Gateway
- description: Deploy gateways across cloud, on-premise, and hybrid environments with centralized management.
  name: Multi-Cloud API Management
- description: Wrap legacy SOAP and XML APIs with modern REST or GraphQL interfaces using Tyk's transformation middleware.
  name: Legacy API Modernization
- description: Manage third-party developer access with fine-grained policies, quota management, and analytics per consumer.
  name: Partner API Program
- description: Govern and manage AI model APIs with rate limiting, access control, and usage analytics through Tyk AI Studio.
  name: AI API Management
---
