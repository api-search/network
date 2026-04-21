---
api_count: 2
apis:
- description: Allianz Trade API design guidelines covering REST API conventions, pagination standards (pageSize, page, totalRequired), sorting conventions, asynchronous processing with JobID management, webhook not
  name: Allianz Trade API Design Standards
  slug: allianz-trade-api-standards
- description: Allianz Global Digital Factory backend development standards. Uses Java and Kotlin with Spring Boot for microservices, API-first approach with OpenAPI specifications, Backend for Frontends (BFF) archi
  name: Allianz Backend Development Standards
  slug: allianz-backend-standards
capabilities:
- description: Workflow capability for architects and developers querying Allianz technology standards and checking API compliance against documented guidelines.
  name: Allianz Standards Compliance Workflow
  slug: standards-compliance-workflow
common:
- title: ''
  type: GitHubOrganization
  url: https://github.com/Allianz
- title: ''
  type: Website
  url: https://www.allianz.com/
- title: ''
  type: Blog
  url: https://globaldigitalfactory.allianz.com/
- title: ''
  type: SpectralRules
  url: rules/allianz-technology-standards-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/allianz-technology-standards-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/standards-compliance-workflow.yaml
created: '2024-01-01'
description: A collection of technology standards and guidelines maintained by Allianz for software development, API design, architecture, and engineering practices. Allianz follows API-first development using OpenAPI specifications, Backend for Frontends (BFF) architecture, and standardized patterns for pagination, sorting, webhooks, and asynchronous processing.
features:
- description: Allianz mandates API-first design using OpenAPI specifications before implementation, enabling frontend teams to work with mock servers independently.
  name: API First Development
- description: Standardized pagination using pageSize (default 20), page (default 1), and totalRequired parameters with Total-Items and Total-Pages response headers.
  name: Pagination Standards
- description: JobID-based pattern for POST/PATCH/DELETE operations returning a job identifier that clients poll until status transitions from pending to processed.
  name: Asynchronous Processing Pattern
- description: Standardized webhook patterns with technical and functional notification types, HTTPS requirement, IP whitelisting, and pre-signed URL support.
  name: Webhook Notification Standards
- description: Allianz Trade APIs standardize on OAuth2 client credentials for programmatic API authentication across all API products.
  name: OAuth2 Security Standard
- description: BFF pattern where each backend service serves a single frontend, enabling clean separation and independent product team decisions.
  name: Backend for Frontends Architecture
image: /assets/icons/allianz-technology-standards.png
integrations:
- description: Allianz follows the OpenAPI Specification as the standard format for API documentation and developer portal integration.
  name: OpenAPI Initiative
- description: Swagger UI used to make API documentation live and executable from OpenAPI specifications.
  name: Swagger UI
- description: Spring Boot is the standard framework for delivering Allianz backend services with REST, security, caching, and logging.
  name: Spring Boot
jsonld:
- class_count: 8
  name: Allianz Technology Standards Context
  property_count: 24
  slug: allianz-technology-standards-context
layout: provider
modified: '2026-04-19'
name: Allianz Technology Standards
rules:
- name: Allianz Technology Standards API Rules
  rule_count: 22
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 7
  slug: allianz-technology-standards-spectral-rules
skills: []
slug: allianz-technology-standards
solutions: []
tags:
- Best Practices
- Enterprise Architecture
- Guidelines
- Software Development
- Technology Standards
- API Design
- OpenAPI
url: https://raw.githubusercontent.com/api-evangelist/allianz-technology-standards/refs/heads/main/apis.yml
use_cases:
- description: Verify that Allianz API implementations conform to documented design guidelines for pagination, sorting, webhooks, and authentication.
  name: API Standards Compliance
- description: Guide new developers on Allianz technology conventions for Java/Kotlin backend services, Spring Boot frameworks, and OpenAPI documentation.
  name: Developer Onboarding
- description: Use BFF and API-first standards as criteria for architecture reviews and technical decision documentation.
  name: Architecture Review
---
