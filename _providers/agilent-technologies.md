---
api_count: 4
apis:
- description: The iLab API enables customers to seamlessly integrate outside applications with iLab's billing and reporting modules. It leverages a RESTful application architecture with HATEOAS (Hypermedia as the E
  name: Agilent iLab Operations API
  slug: ''
- description: The SLIMS (Smart Laboratory Information Management System) REST API provides programmatic access to Agilent SLIMS laboratory data management platform. SLIMS features three APIs — REST, Java, and Pytho
  name: Agilent SLIMS REST API
  slug: ''
- description: The CrossLab Asset Manager API provides programmatic access to Agilent's CrossLab instrument services platform, enabling management of laboratory assets, instrument service records, maintenance schedu
  name: Agilent CrossLab Asset Manager API
  slug: ''
- description: The VWorks API provides a Component Object Model (COM) application programming interface for VWorks laboratory automation software (version 14.0 and later). It enables programmatic control of laborato
  name: Agilent VWorks Automation API
  slug: ''
capabilities:
- description: 'Unified laboratory operations capability combining iLab core facility management for billing, scheduling, service requests, and reporting. Used by core facility managers, research administrators, and '
  name: Agilent Laboratory Operations
  slug: laboratory-operations
common:
- title: ''
  type: Website
  url: https://www.agilent.com/en
- title: ''
  type: Support
  url: https://www.agilent.com/en/support
- title: ''
  type: Community
  url: https://community.agilent.com
- title: ''
  type: GitHubOrganization
  url: https://github.com/Agilent
- title: ''
  type: TermsOfService
  url: https://www.agilent.com/en/legal
- title: ''
  type: PrivacyPolicy
  url: https://www.agilent.com/en/privacy-statement
- title: ''
  type: SpectralRules
  url: rules/agilent-technologies-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/laboratory-operations.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/agilent-technologies-vocabulary.yaml
created: ''
description: Agilent Technologies is a global leader in life sciences, diagnostics, and applied chemical markets, providing instruments, software, services, and consumables for laboratory workflows. Agilent offers APIs for laboratory operations management including iLab for core facility billing and scheduling, SLIMS for laboratory information management, CrossLab Asset Manager for instrument management, and VWorks for laboratory automation.
features:
- description: iLab and CrossLab APIs leverage RESTful architecture with HATEOAS for discoverable resource navigation.
  name: RESTful Architecture
- description: Secure access to APIs via OAuth2 with client ID and API token-based authentication.
  name: OAuth2 Authentication
- description: Pre-built integration support for SAP, Oracle/PeopleSoft, Lawson, and Banner financial systems.
  name: Financial System Integration
- description: Integration with laboratory information management systems for sample tracking and results management.
  name: LIMS Integration
- description: Ability to import usage logs and data directly from connected laboratory instruments.
  name: Instrument Data Import
- description: SLIMS supports custom plugin development via Java and Python APIs for workflow extension.
  name: Plugin Architecture
- description: SLIMS REST API documentation is automatically generated from each deployed instance.
  name: Auto-Generated API Documentation
image: ''
integrations:
- description: Financial system integration for billing and cost accounting via iLab API.
  name: SAP
- description: ERP integration for institutional billing and financial reporting.
  name: Oracle PeopleSoft
- description: Financial management system integration for laboratory billing workflows.
  name: Lawson
- description: Higher education ERP integration for core facility cost center management.
  name: Banner
- description: Integration between Agilent instruments and LabWare LIMS for data transfer and workflow coordination.
  name: LabWare LIMS
- description: Integration with institutional identity providers for single sign-on and user provisioning.
  name: Identity Management Systems
jsonld:
- class_count: 23
  name: Agilent Ilab Operations Api Context
  property_count: 37
  slug: agilent-ilab-operations-api-context
layout: provider
modified: '2026-04-19'
name: agilent-technologies
rules:
- name: agilent-technologies API Rules
  rule_count: 35
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 21
  slug: agilent-technologies-spectral-rules
skills: []
slug: agilent-technologies
solutions: []
tags:
- Life Sciences
- Diagnostics
- Laboratory
- Scientific Instruments
- LIMS
- Laboratory Automation
url: https://raw.githubusercontent.com/api-evangelist/agilent-technologies/refs/heads/main/apis.yml
use_cases:
- description: Automate billing workflows between iLab core facilities and institutional financial systems such as SAP or Oracle.
  name: Core Facility Billing Automation
- description: Integrate external scheduling applications with iLab's equipment reservation and usage tracking.
  name: Laboratory Scheduling Integration
- description: Use the SLIMS API to track samples from receipt through analysis and reporting across NGS, biobank, and R&D workflows.
  name: Sample Lifecycle Management
- description: Manage laboratory instrument service records, calibration schedules, and compliance documentation via CrossLab Asset Manager API.
  name: Instrument Asset Tracking
- description: Programmatically control VWorks-driven liquid handling robots and integrated workstations for high-throughput workflows.
  name: Automation Workflow Control
- description: Extract and aggregate laboratory data from SLIMS for custom reporting and business intelligence integrations.
  name: LIMS Data Reporting
---
