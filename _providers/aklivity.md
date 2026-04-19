---
api_count: 3
apis:
- description: 'Zilla is a stateless, cloud-native multi-protocol edge and service proxy that enables seamless access to Apache Kafka through HTTP REST, gRPC, SSE, MQTT, and WebSocket protocols. Zilla eliminates the '
  name: Zilla Gateway
  slug: zilla-gateway
- description: 'The Zilla Platform adds an enterprise management layer on top of Zilla Gateway, providing API data products with versioning and rate limits, Kafka governance policies, a self-service developer portal '
  name: Zilla Platform
  slug: zilla-platform
- description: ZillaBase is an event-driven backend framework for the next generation of web, mobile, and AI applications, built on top of Apache Kafka and Zilla to enable real-time, event-sourced application develo
  name: ZillaBase
  slug: zillabase
capabilities:
- description: Workflow for exposing Apache Kafka topics as REST APIs and managing event-driven integrations via Zilla. Enables HTTP, MQTT, and gRPC clients to produce and consume Kafka events without Kafka client l
  name: Aklivity Kafka API Gateway
  slug: kafka-api-gateway
common:
- title: ''
  type: Website
  url: https://www.aklivity.io/
- title: ''
  type: Documentation
  url: https://docs.aklivity.io/zilla/latest/
- title: ''
  type: GettingStarted
  url: https://docs.aklivity.io/zilla/next/getting-started/quickstart/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aklivity
- title: ''
  type: GitHubRepository
  url: https://github.com/aklivity/zilla
- title: ''
  type: Pricing
  url: https://www.aklivity.io/pricing
created: '2026-01-02'
description: Aklivity provides the Zilla multi-protocol edge and service proxy for event-driven architectures, enabling seamless integration between web apps, IoT clients, and microservices with Apache Kafka via declaratively defined, stateless APIs. Zilla supports HTTP, gRPC, MQTT, SSE, and WebSocket protocols, translating them to and from Kafka without custom code or connectors. The Zilla Platform adds enterprise governance, observability, and self-service access management for Kafka deployments.
features:
- description: Translates HTTP REST, gRPC, MQTT, SSE, and WebSocket protocols directly to Kafka topics without custom code, connectors, or middleware.
  name: Multi-Protocol Kafka Access
- description: Define gateways and protocol mappings via YAML configuration or AsyncAPI specifications, then deploy with Docker, Helm, or native binaries.
  name: Declarative Configuration
- description: Built-in JWT token validation, TLS termination, and Kafka SASL support for securing API access to Kafka clusters.
  name: JWT Authentication and TLS
- description: SIMD-optimized runtime schema validation for JSON, Avro, and Protobuf via Confluent Schema Registry or AWS Glue Schema Registry.
  name: Schema Validation
- description: Metrics and logs exported to Prometheus and OpenTelemetry for unified visibility across Kafka API traffic.
  name: Observability
- description: Topic naming policies, runtime enforcement, schema compliance rules, and API data product versioning with rate limits via Zilla Platform.
  name: Kafka Governance
- description: API key and certificate management self-service portal for Kafka consumers and producers via Zilla Platform.
  name: Self-Service Developer Portal
- description: PII classification and field-level encryption for sensitive data in Kafka messages via Zilla Platform.
  name: Field-Level Encryption
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Core integration — Zilla acts as a multi-protocol proxy in front of any Kafka cluster
  name: Apache Kafka
- description: Managed Streaming for Apache Kafka integration with AWS-native security
  name: AWS MSK
- description: Schema validation and enforcement using Confluent Schema Registry
  name: Confluent Schema Registry
- description: Schema validation using AWS Glue Schema Registry
  name: AWS Glue Schema Registry
- description: Metrics export for monitoring Zilla gateway performance
  name: Prometheus
- description: Distributed tracing and observability via OpenTelemetry
  name: OpenTelemetry
- description: Secure credential management for Kafka and TLS configurations
  name: AWS Secrets Manager
jsonld:
- class_count: 2
  name: Aklivity Context
  property_count: 7
  slug: aklivity-context
layout: provider
modified: '2026-04-19'
name: Aklivity
rules:
- name: Aklivity API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: aklivity-spectral-rules
skills: []
slug: aklivity
solutions: []
tags:
- API Gateway
- Apache Kafka
- Event-Driven
- IoT
- Kafka Proxy
- Multi-Protocol
- Real-Time
url: https://raw.githubusercontent.com/api-evangelist/aklivity/refs/heads/main/apis.yml
use_cases:
- description: Expose Kafka topics as REST API endpoints, allowing any HTTP client to produce and consume Kafka messages without Kafka client libraries.
  name: HTTP to Kafka REST API
- description: Connect IoT devices using MQTT protocol directly to Kafka topics, eliminating the need for a separate MQTT broker.
  name: IoT MQTT to Kafka
- description: Route gRPC calls from microservices to Kafka topics for event-driven inter-service communication.
  name: gRPC to Kafka
- description: Platform teams build internal developer portals for Kafka access with governance, rate limiting, and self-service API key management.
  name: Kafka Self-Service Platform
- description: Enterprises expose Kafka event streams to external partners via secured, rate-limited REST or SSE APIs.
  name: Event-Driven Partner Integration
- description: Financial institutions distribute real-time market data and trade events via secured Kafka API gateways.
  name: Financial Services Data Distribution
---
