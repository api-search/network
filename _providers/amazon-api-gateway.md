---
api_count: 4
apis:
- description: RESTful APIs that are optimized for serverless workloads and HTTP backends using HTTP APIs.
  name: Amazon API Gateway REST API
  slug: rest-api
- description: Build real-time two-way communication applications with WebSocket APIs.
  name: Amazon API Gateway WebSocket API
  slug: websocket-api
- description: Lower latency and lower cost alternative to REST APIs with essential features for building HTTP-based APIs.
  name: Amazon API Gateway HTTP API
  slug: http-api
- description: API for directly managing runtime aspects of deployed APIs, including sending data to connected WebSocket clients via the @connections endpoint and managing connection state.
  name: Amazon API Gateway Management API
  slug: management-api
asyncapis:
- description: Amazon API Gateway WebSocket APIs enable real-time two-way communication between clients and backend services. Clients connect via WebSocket protocol and exchange messages through routes that map to L
  name: Amazon API Gateway WebSocket API
  slug: amazon-api-gateway-websocket-asyncapi
capabilities:
- description: Workflow capability for managing API Gateway REST APIs including lifecycle management, stage deployment, and configuration.
  name: Amazon API Gateway Management
  slug: api-gateway-management
common:
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/compute/category/application-services/amazon-api-gateway/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/apigateway
- title: ''
  type: CLIReference
  url: https://docs.aws.amazon.com/cli/latest/reference/apigateway/
- title: ''
  type: SDK
  url: https://aws.amazon.com/tools/
- title: ''
  type: Status
  url: https://status.aws.amazon.com/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: Website
  url: https://aws.amazon.com/api-gateway/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/apigateway/
- title: ''
  type: Pricing
  url: https://aws.amazon.com/api-gateway/pricing/
- title: ''
  type: Getting Started
  url: https://aws.amazon.com/api-gateway/getting-started/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/api-gateway/faqs/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-api-gateway
- title: ''
  type: CodeExamples
  url: https://docs.aws.amazon.com/code-library/latest/ug/api-gateway_code_examples.html
- title: ''
  type: SpectralRules
  url: rules/amazon-api-gateway-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/api-gateway-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-api-gateway-vocabulary.yaml
created: '2024-01-15'
description: Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.
features:
- description: Create, configure, and manage REST APIs with resources, methods, integrations, and request/response transformations.
  name: REST API Management
- description: Build real-time two-way communication applications with WebSocket APIs supporting persistent connections and message routing.
  name: WebSocket API Support
- description: Deploy lightweight HTTP APIs with lower latency and cost than REST APIs, optimized for Lambda and HTTP backends.
  name: HTTP API Support
- description: Manage deployment stages with canary releases, stage variables, and throttling configurations for blue/green deployments.
  name: Stage and Deployment Management
- description: Secure APIs with IAM authorization, Lambda authorizers, Cognito user pools, and resource-based policies.
  name: API Security and Authorization
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Integrate API Gateway with Lambda functions for serverless request processing without managing infrastructure.
  name: AWS Lambda
- description: Use Cognito user pools and identity pools for managed authentication and authorization in API Gateway.
  name: AWS Cognito
- description: Protect API Gateway endpoints with AWS WAF rules for rate limiting and protection against common web exploits.
  name: AWS WAF
- description: Monitor API performance, errors, and latency using CloudWatch metrics and logs integrated with API Gateway.
  name: AWS CloudWatch
jsonld:
- class_count: 0
  name: Amazon Api Gateway Context
  property_count: 13
  slug: amazon-api-gateway-context
layout: provider
modified: '2026-04-19'
name: Amazon API Gateway
rules:
- name: Amazon API Gateway API Rules
  rule_count: 5
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 0
  slug: amazon-api-gateway-spectral-rules
skills: []
slug: amazon-api-gateway
solutions: []
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
url: https://raw.githubusercontent.com/api-evangelist/amazon-api-gateway/refs/heads/main/apis.yml
use_cases:
- description: Build serverless REST APIs backed by Lambda functions using API Gateway as the front door for request routing.
  name: Serverless API Backend
- description: Use API Gateway as a unified entry point for microservices, providing routing, authentication, and rate limiting.
  name: Microservices Gateway
- description: Build chat, collaboration, and live data streaming applications using WebSocket APIs with persistent client connections.
  name: Real-Time Applications
- description: Automate API creation, deployment, and versioning using the API Gateway control plane API in CI/CD pipelines.
  name: API Lifecycle Automation
---
