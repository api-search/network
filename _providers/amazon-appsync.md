---
api_count: 1
apis:
- description: REST management API for Amazon AppSync covering GraphQL APIs, data sources, resolvers, functions, types, schema, API keys, and custom domain names.
  name: Amazon AppSync API
  slug: amazon-appsync-api
capabilities:
- description: Workflow capability for building and managing GraphQL APIs with AppSync including data sources, resolvers, and schema management.
  name: GraphQL Api Management Workflow
  slug: graphql-api-management
common: []
created: '2024-01-15'
description: Amazon AppSync creates serverless GraphQL and Pub/Sub APIs that simplify application development through a single endpoint to securely query, update, or publish data.
features:
- Managed GraphQL API hosting with automatic scaling
- Multiple authentication modes including API key, IAM, Cognito, and Lambda
- Real-time subscriptions via WebSocket connections
- Pipeline resolvers for composing multi-step data access patterns
- Direct Lambda resolvers with APPSYNC_JS runtime support
- Built-in caching for improved performance
- Conflict detection and resolution for offline sync use cases
- Custom domain names with ACM certificate integration
- X-Ray tracing and CloudWatch logging integration
- Merged APIs for combining multiple GraphQL APIs
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- Amazon DynamoDB
- AWS Lambda
- Amazon OpenSearch Service
- Amazon RDS
- Amazon EventBridge
- Amazon Cognito
- AWS IAM
- AWS WAF
- Amazon CloudWatch
- AWS X-Ray
- AWS Certificate Manager
- Amazon Route 53
jsonld:
- class_count: 73
  name: Amazon Appsync Context
  property_count: 0
  slug: amazon-appsync-context
layout: provider
modified: '2026-04-19'
name: Amazon AppSync
rules:
- name: Amazon AppSync API Rules
  rule_count: 20
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 5
  slug: amazon-appsync-spectral-rules
skills: []
slug: amazon-appsync
solutions: []
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
url: https://raw.githubusercontent.com/api-evangelist/amazon-appsync/refs/heads/main/apis.yml
use_cases:
- Build mobile and web applications with a unified GraphQL data layer
- Implement real-time features like live notifications and chat with subscriptions
- Create a unified data access layer across multiple microservices
- Build offline-capable mobile apps with automatic conflict resolution
- Expose DynamoDB tables, Lambda functions, and OpenSearch as GraphQL APIs
- Implement federated GraphQL across multiple teams with Merged APIs
---
