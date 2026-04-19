---
api_count: 3
apis:
- description: ACORD XML Standards define data exchange formats for property & casualty, life, annuity, and reinsurance using SOAP/XML protocols. APIs enable claims inquiry, policy administration, and regulatory rep
  name: ACORD XML Standards API
  slug: acord-xml-standards-api
- description: The ACORD Next-Generation Digital Standards (NGDS) Object Model provides granular, transaction-centric standards for APIs, microservices, IoT, and RESTful architectures. Based on JSON and YAML data-in
  name: ACORD Next-Generation Digital Standards (NGDS) API
  slug: acord-ngds-api
- description: ACORD Global Reinsurance & Large Commercial Data Standards define XML data exchange formats for reinsurance and large commercial lines. APIs support facultative and treaty reinsurance transactions, pl
  name: ACORD Reinsurance & Large Commercial Data Standards API
  slug: acord-reinsurance-standards-api
capabilities:
- description: Unified insurance data exchange workflow for policy administration, claims management, party registry, and underwriting using ACORD Next-Generation Digital Standards (NGDS). Used by insurance carriers
  name: ACORD Insurance Data Exchange
  slug: insurance-data-exchange
common:
- title: ''
  type: Website
  url: https://www.acord.org
- title: ''
  type: Portal
  url: https://www.acord.org/standards-architecture/acord-data-standards
- title: ''
  type: Documentation
  url: https://www.acord.org/standards-architecture/acord-data-standards
- title: ''
  type: GettingStarted
  url: https://www.acord.org/standards-architecture/acord-data-standards/next-generation-digital-standards
- title: ''
  type: Documentation
  url: https://www.acord.org/standards-architecture/reference-architecture
- title: ''
  type: Support
  url: https://www.acord.org/standards-architecture/get-involved/standards-project-advisory-groups
- title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/openapi/acord-ngds-openapi.yml
- title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-schema/acord-policy-schema.json
- title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-schema/acord-claim-schema.json
- title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-ld/acord-context.jsonld
- title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist/acord
- title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/rules/acord-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/capabilities/insurance-data-exchange.yaml
- title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/vocabulary/acord-vocabulary.yaml
created: ''
description: ACORD is a global standards-setting body for the insurance industry, providing data standards, reference architecture, and digital tools that enable insurers, brokers, and software providers to exchange information.
features:
- description: ACORD XML standards for property & casualty, life, annuity, and reinsurance SOAP/XML data exchange.
  name: XML Data Standards
- description: JSON/YAML-based NGDS for RESTful APIs, microservices, and IoT insurance data exchange.
  name: Next-Generation Digital Standards
- description: Global reinsurance and large commercial data standards for facultative and treaty transactions.
  name: Reinsurance Standards
- description: Electronic data standards for life insurance and annuity products covering underwriting and policy management.
  name: Life and Annuity Standards
- description: ACORD reference architecture providing structural frameworks for insurance technology implementations.
  name: Reference Architecture
image: /assets/icons/acord.png
integrations:
- description: Integration with policy administration systems (PAS) and claims management systems (CMS).
  name: Insurance Core Systems
- description: Integration with reinsurance management platforms supporting ACORD AL3 and RIBO formats.
  name: Reinsurance Platforms
- description: Modern insurtech API platforms consuming ACORD NGDS JSON standards.
  name: Insurtech Solutions
- description: Integration with state and national insurance regulatory reporting systems.
  name: Regulatory Systems
jsonld:
- class_count: 0
  name: Acord Context
  property_count: 5
  slug: acord-context
- class_count: 19
  name: Acord Ngds Context
  property_count: 55
  slug: acord-ngds-context
layout: provider
modified: '2026-04-19'
name: ACORD
rules:
- name: ACORD API Rules
  rule_count: 33
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 17
  slug: acord-spectral-rules
skills: []
slug: acord
solutions: []
tags:
- Claims
- Insurance
- Policy
- Standards
- Underwriting
url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/apis.yml
use_cases:
- description: Standardized ACORD XML or NGDS JSON claims transaction exchange between carriers, adjusters, and reinsurers.
  name: Claims Data Exchange
- description: Automated policy issuance, endorsement, and renewal using ACORD NGDS microservices architecture.
  name: Policy Administration
- description: Straight-through processing of insurance applications using ACORD standardized data elements.
  name: Underwriting Automation
- description: Facultative and treaty reinsurance data exchange using ACORD Global Reinsurance Data Standards.
  name: Reinsurance Settlement
- description: Compliance reporting using ACORD-standardized data formats for regulatory submissions.
  name: Regulatory Reporting
---
