---
api_count: 1
apis:
- description: This API allows you to create and query a number of objects in your 1Factory account. The API accepts and returns request and response bodies as JSON, using UTF-8 encoding. Supports part master manage
  name: 1Factory API
  slug: 1factory
capabilities:
- description: Unified quality management workflow for 1Factory. Combines manufacturing inspections, receiving inspections, supplier quality, customer quality, FAI, part master management, and QMS records (NCRs, CAP
  name: 1Factory Quality Management
  slug: 1factory-quality-management
common:
- title: ''
  type: Website
  url: https://www.1factory.com/
- title: ''
  type: Documentation
  url: https://www.1factory.com/api-doc/index.html
- title: ''
  type: Security
  url: https://www.1factory.com/technical-overview.html
- title: ''
  type: Support
  url: https://1factoryhelp.zendesk.com/hc/en-us
- title: ''
  type: TermsOfService
  url: https://www.1factory.com/resources/TOS%20May%2020%202021.pdf
- title: ''
  type: RateLimits
  url: https://www.1factory.com/api-doc/index.html
- title: ''
  type: SpectralRules
  url: rules/1factory-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/1factory-quality-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/1factory-vocabulary.yaml
- title: ''
  type: JSON-LD
  url: json-ld/1factory-context.jsonld
created: '2025-02-08'
description: 1Factory is a leading provider of quality management software solutions for manufacturing companies. The platform helps businesses streamline their operations, improve efficiency, and ensure product quality at every stage of the production process. Features include real-time monitoring, automated data collection, advanced analytics, and integration with ERP and PLM systems via a REST API.
features:
- description: Factory floor quality control, inspection planning, and statistical process control (SPC)
  name: Manufacturing Quality Control
- description: Document control, training management, audits, and compliance workflows
  name: Quality Management System (QMS)
- description: Vendor oversight, incoming inspection management, and supplier corrective actions
  name: Supplier Quality Management
- description: Automated drawing ballooning and AS9102-compliant first article inspection
  name: First Article Inspection (FAI)
- description: Real-time quality analytics and audit-ready reporting dashboards
  name: Real-Time Analytics
- description: Automatic import of CMM measurement data with SPC analysis
  name: CMM Data Integration
- description: API-based integration with ERP and PLM systems for part and work order sync
  name: ERP/PLM Integration
image: /assets/icons/1factory.png
integrations:
- description: Sync part master data, work orders, and inspection records with ERP platforms
  name: ERP Systems
- description: Connect with PLM systems for design-to-manufacturing quality continuity
  name: PLM Systems
- description: Auto-import measurement data from CMM equipment directly into inspections
  name: CMM Equipment
jsonld:
- class_count: 29
  name: 1Factory Context
  property_count: 127
  slug: 1factory-context
layout: provider
modified: '2026-04-19'
name: 1Factory
rules:
- name: 1Factory API Rules
  rule_count: 32
  severity_counts:
    error: 13
    hint: 0
    info: 4
    warn: 15
  slug: 1factory-spectral-rules
skills: []
slug: 1factory
solutions: []
tags:
- Analytics
- Data Collection
- Manufacturing
- Monitoring
- Quality
url: https://raw.githubusercontent.com/api-evangelist/1factory/refs/heads/main/apis.yml
use_cases:
- description: Create and track manufacturing inspections with measurement data and SPC analysis
  name: Manufacturing Inspection
- description: Manage supplier certifications, conduct receiving inspections, and track supplier CAPAs
  name: Supplier Qualification
- description: Log, track, and resolve non-conformances, CAPAs, and customer complaints
  name: Non-Conformance Management
- description: Conduct and document AS9102 first article inspections for aerospace and defense
  name: First Article Inspection
- description: Synchronize part master data, work orders, and inspection results with ERP systems
  name: ERP Data Sync
---
