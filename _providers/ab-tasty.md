---
api_count: 3
apis:
- description: 'The AB Tasty Decision API is a server-side service that evaluates a visitors context against your active experiments, personalizations, and feature flags, then returns a deterministic decision: which '
  name: AB Tasty Decision API
  slug: ab-tasty-decision-api
- description: AB Tastys Remote Control API is a developer and QA tool that lets you programmatically drive the AB Tasty SDK from outside your app or page, so you can precisely control and observe experiments withou
  name: AB Tasty Remote Control API
  slug: ab-tasty-remote-control-api
- description: The AB Tasty Public API provides programmatic access to manage campaigns, monitor and control experiments, manage account users, and integrate AB Tasty with third-party tools. It uses OAuth-style cred
  name: AB Tasty Public API
  slug: ab-tasty-public-api
capabilities:
- description: Unified workflow for server-side feature experimentation, A/B testing, and feature flag management. Enables developers and product teams to evaluate campaigns, retrieve flag values, and track activati
  name: AB Tasty Feature Experimentation
  slug: feature-experimentation
common:
- title: ''
  type: Website
  url: https://www.abtasty.com/
- title: ''
  type: Portal
  url: https://developers.abtasty.com/
- title: ''
  type: Documentation
  url: https://docs.abtasty.com/
- title: ''
  type: Pricing
  url: https://www.abtasty.com/pricing/
- title: ''
  type: Support
  url: https://support.abtasty.com/hc/en-us
- title: ''
  type: Legal
  url: https://www.abtasty.com/legal-notices/
- title: ''
  type: PrivacyPolicy
  url: https://www.abtasty.com/privacy-policy/
- title: ''
  type: GitHubOrganization
  url: https://github.com/flagship-io
- title: ''
  type: CLI
  url: https://github.com/flagship-io/abtasty-cli
- title: MCP Server
  type: Tools
  url: https://github.com/flagship-io/mcp-server
- title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/rules/ab-tasty-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/vocabulary/ab-tasty-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/capabilities/feature-experimentation.yaml
- title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-ld/ab-tasty-decision-api-context.jsonld
created: '2025-06-05'
description: At AB Tasty, we are your partner for pushing great ideas even further through optimization. We achieve this by empowering brands to build better experiences using personalization, experimentation, recommendations, merchandising, and the market's only emotions-based segmentation solution.
features:
- description: Advanced A/B testing with conversion safety mechanisms and unlimited variations
  name: A/B Testing
- description: Server-side feature flags with targeting and gradual rollouts
  name: Feature Flags
- description: Experience customization based on emotional needs and engagement segmentation
  name: Personalization
- description: Unified search, recommendations, and product visibility control
  name: E-Merchandising
- description: Progressive feature release with automatic KPI-triggered rollbacks
  name: Progressive Rollouts
- description: AI-powered prompt-based visual modifications for experiments
  name: AI Visual Editor
- description: Real-time predictive AI for anonymous visitor personalization targeting 90% of visitors
  name: AdaptiveCX
- description: Test multiple variables simultaneously across web and mobile
  name: Multivariate Testing
image: /assets/icons/ab-tasty.png
integrations:
- description: Partnership with Google Cloud for infrastructure and analytics integration
  name: Google Cloud
- description: Connect with analytics platforms via the integration hub for data sharing
  name: Analytics Tools
- description: Customer Data Platform integrations for enhanced visitor profiling
  name: CDPs
- description: OpenFeature provider integration for standardized feature flag management
  name: OpenFeature
- description: Edge function integration with Vercel for server-side experimentation
  name: Vercel
- description: Cloudflare Worker integration for edge-based feature experimentation
  name: Cloudflare
- description: AWS Lambda integration for serverless feature experimentation
  name: AWS Lambda
- description: Fastly worker integration for CDN-level feature experimentation
  name: Fastly
- description: Akamai worker integration for CDN-level feature experimentation
  name: Akamai
- description: Shopify Hydrogen framework integration for headless commerce experimentation
  name: Shopify Hydrogen
jsonld:
- class_count: 13
  name: Ab Tasty Decision Api Context
  property_count: 29
  slug: ab-tasty-decision-api-context
layout: provider
modified: '2026-04-19'
name: AB Tasty
rules:
- name: AB Tasty API Rules
  rule_count: 40
  severity_counts:
    error: 13
    hint: 0
    info: 5
    warn: 22
  slug: ab-tasty-spectral-rules
skills: []
slug: ab-tasty
solutions: []
tags:
- Aggregation
- Experimentation
- Feature Flags
- Personalization
- A/B Testing
url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/apis.yml
use_cases:
- description: Run A/B tests and multivariate experiments on websites to optimize conversion rates
  name: Web Experimentation
- description: Multi-channel feature testing across devices via API or SDK implementation
  name: Feature Experimentation
- description: Backend and edge worker experiments using the Decision API
  name: Server-Side Testing
- description: Merchandising, recommendations, and personalized product experiences
  name: E-commerce Optimization
- description: Gradual feature rollouts with automated rollback based on KPI monitoring
  name: Progressive Deployment
- description: AI-driven real-time personalization for anonymous visitors
  name: Anonymous Personalization
---
