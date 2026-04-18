---
api_count: 6
apis:
- description: 'Ambassador offers a suite of products designed to deliver API developer experiences that fuel innovation. These products, Blackbird API Development Platform, Edge Stack API Gateway, and Telepresence, '
  name: Ambassador
  slug: ambassador
- description: Ambassador Edge Stack is a Kubernetes-native API gateway built on Envoy Proxy that provides routing, load balancing, authentication, rate limiting, and observability for microservices. It supports cus
  name: Ambassador Edge Stack API Gateway
  slug: edge-stack-api-gateway
- description: Emissary-Ingress is an open-source, Kubernetes-native API gateway built on Envoy Proxy and a CNCF incubating project, formerly known as Ambassador API Gateway. It uses custom resource definitions (CRD
  name: Emissary-Ingress
  slug: emissary-ingress
- description: Telepresence provides a RESTful API server that runs on the local host, both on the local workstation and in a pod that contains a traffic-agent. The API includes healthz, consume-here, and intercept-
  name: Ambassador Telepresence RESTful API
  slug: telepresence-api
- description: Blackbird is an API development platform that helps developers design, build, test, and manage APIs with AI-powered code generation, mocking, and production-like test environments. It supports OpenAPI
  name: Ambassador Blackbird API Development Platform
  slug: blackbird-api-development-platform
- description: The Ambassador Edge Stack Developer Portal automatically detects and publishes API documentation, serving as a single point of reference for all microservice APIs. It supports Swagger and OpenAPI V3 s
  name: Ambassador Edge Stack Developer Portal
  slug: edge-stack-developer-portal
capabilities:
- description: Unified gateway management workflow for platform engineers and DevOps teams to configure API routing, TLS termination, rate limiting, and health monitoring across Ambassador Edge Stack instances.
  name: Ambassador Gateway Management
  slug: gateway-management
common:
- title: ''
  type: Customers
  url: https://www.getambassador.io/case-studies
- title: ''
  type: Pricing
  url: https://www.getambassador.io/pricing
- title: ''
  type: Blog
  url: https://www.getambassador.io/blog
- title: ''
  type: FAQ
  url: https://www.getambassador.io/faq
- title: ''
  type: Documentation
  url: https://www.getambassador.io/docs
- title: ''
  type: Support
  url: https://www.getambassador.io/support
- title: ''
  type: Partners
  url: https://www.getambassador.io/company/partnerships
- title: ''
  type: GettingStarted
  url: https://www.getambassador.io/docs/edge-stack/latest/tutorials/getting-started/
- title: ''
  type: GitHubRepository
  url: https://github.com/emissary-ingress/emissary
- title: ''
  type: ChangeLog
  url: https://github.com/emissary-ingress/emissary/blob/master/CHANGELOG.md
- title: ''
  type: StatusPage
  url: https://status.datawire.io/
- title: ''
  type: Authentication
  url: https://www.getambassador.io/products/edge-stack/api-gateway/security-authentication
- title: ''
  type: RateLimits
  url: https://www.getambassador.io/docs/edge-stack/latest/howtos/rate-limiting-tutorial
- title: ''
  type: X
  url: https://x.com/ambassadorlabs
- title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ambassadorlabs
- title: ''
  type: SignUp
  url: https://app.getambassador.io/
- title: ''
  type: GitHubRepository
  url: https://github.com/datawire/ambassador-docs
- title: ''
  type: GitHubOrganization
  url: https://github.com/datawire
- title: ''
  type: JSONLD
  url: json-ld/ambassador-context.jsonld
- title: ''
  type: JSONSchema
  url: json-schema/ambassador-mapping-schema.json
created: '2025-01-08'
description: Ambassador is a Kubernetes-native API Gateway built on Envoy Proxy, providing routing, load balancing, authentication, and observability for microservices.
features:
- description: Purpose-built for Kubernetes with custom resource definitions (CRDs) for declarative configuration of routing, TLS, and rate limiting.
  name: Kubernetes-Native API Gateway
- description: Built on Envoy Proxy for high-performance load balancing, circuit breaking, and observability at the edge.
  name: Envoy Proxy Foundation
- description: Integrated OAuth2, API key, and JWT-based authentication filters to secure API endpoints without custom code.
  name: Authentication and Security
- description: Configurable rate limiting with labels and descriptors to control request throughput to backend services.
  name: Rate Limiting
- description: Automatic API documentation publishing from OpenAPI/Swagger specs with customizable developer portal for onboarding.
  name: Developer Portal
- description: Intercept and debug remote Kubernetes services locally using Telepresence for fast inner-loop development.
  name: Local Development with Telepresence
- description: AI-powered API development platform with mock servers and production-like test environments for rapid iteration.
  name: API Mocking with Blackbird
image: https://www.getambassador.io/images/ambassador-logo.png
integrations:
- description: Native integration with Kubernetes using CRDs for Mapping, Host, TLSContext, and RateLimit resources.
  name: Kubernetes
- description: Built on Envoy Proxy with full access to Envoy's load balancing, circuit breaking, and observability features.
  name: Envoy Proxy
- description: Install and manage Ambassador Edge Stack using Helm charts for Kubernetes deployments.
  name: Helm
- description: Export metrics to Prometheus and visualize API gateway performance in Grafana dashboards.
  name: Prometheus and Grafana
- description: Automatic TLS certificate management via cert-manager and ACME protocol integration.
  name: Cert-Manager
jsonld:
- class_count: 0
  name: Ambassador Context
  property_count: 0
  slug: ambassador-context
layout: provider
modified: '2026-04-18'
name: Ambassador
rules:
- name: Ambassador API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: ambassador-spectral-rules
skills: []
slug: ambassador
solutions: []
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
url: https://raw.githubusercontent.com/api-evangelist/ambassador/refs/heads/main/apis.yml
use_cases:
- description: Route, secure, and observe traffic to microservices running in Kubernetes clusters.
  name: Microservices API Gateway
- description: Design, mock, and test APIs locally with Blackbird before deploying to Kubernetes environments.
  name: API Development and Testing
- description: Enable multiple teams to independently manage their API routing and configuration using Kubernetes CRDs.
  name: Multi-Team API Management
- description: Serve as the edge gateway in a service mesh architecture, handling north-south traffic with TLS termination.
  name: Service Mesh Edge Gateway
- description: Provide a self-service developer portal for internal and external developers to discover and consume APIs.
  name: Developer Onboarding
---
