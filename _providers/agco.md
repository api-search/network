---
api_count: 1
apis:
- description: The AGCO AgCommand API provides approved third-party developers and service providers with access to machine telemetry data from AGCO equipment. The API enables farming application developers to build
  name: AGCO AgCommand API
  slug: agcommand-api
capabilities:
- description: Unified workflow capability for AGCO precision farming — monitoring machine location, performance telemetry, and operating conditions across a connected fleet. Used by farm managers and precision agri
  name: AGCO Precision Farming
  slug: precision-farming
common:
- title: ''
  type: Portal
  url: https://get.agcoconnect.com/
- title: ''
  type: GettingStarted
  url: https://github.com/agco/agco-json-api-profiles
- title: ''
  type: GitHubOrganization
  url: https://github.com/agco
- title: ''
  type: TermsOfService
  url: https://www.agcocorp.com/legal/privacy-policy.html
- title: ''
  type: JSONSchema
  url: json-schema/agco-location-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/agco-machine-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/agco-telemetry-schema.json
- title: ''
  type: JSONStructure
  url: json-structure/agco-location-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/agco-machine-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/agco-telemetry-structure.json
- title: ''
  type: JSON-LD
  url: json-ld/agco-telematics-context.jsonld
- title: ''
  type: Example
  url: examples/agco-location-example.json
- title: ''
  type: Example
  url: examples/agco-machine-example.json
- title: ''
  type: Example
  url: examples/agco-telemetry-example.json
- title: ''
  type: SpectralRules
  url: rules/agco-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/agco-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/precision-farming.yaml
created: ''
description: AGCO is a global leader in the design, manufacture, and distribution of agricultural machinery and precision ag technology. The AGCO AgCommand API enables approved third-party developers and service providers to access machine telemetry data, location tracking, and performance metrics from AGCO Connect-ready equipment including Fendt, Massey Ferguson, Challenger, and Valtra brands.
features:
- description: Real-time access to machine performance data including engine speed, load, fuel consumption, and fault codes from AGCO Connect-ready equipment.
  name: Machine Telematics
- description: GPS-based machine location history enabling field work tracking and fleet management dashboards.
  name: Fleet Location Tracking
- description: Remote access to machine diagnostic codes enabling proactive maintenance and reducing downtime.
  name: Diagnostic Fault Codes
- description: Standardized filtering, search, and change event profiles for consistent API behavior across all resources.
  name: JSON API Profiles
- description: Single API access to data from Fendt, Massey Ferguson, Challenger, and Valtra agricultural equipment.
  name: Multi-Brand Coverage
image: ''
integrations:
- description: Integration of AGCO telematics data with Procore construction and project management workflows.
  name: Procore
- description: Integration with precision agriculture software platforms for combined field and machine data analysis.
  name: Precision Ag Software
jsonld:
- class_count: 3
  name: Agco Telematics Context
  property_count: 24
  slug: agco-telematics-context
layout: provider
modified: '2026-04-19'
name: agco
rules:
- name: agco API Rules
  rule_count: 24
  severity_counts:
    error: 14
    hint: 0
    info: 0
    warn: 10
  slug: agco-spectral-rules
skills: []
slug: agco
solutions: []
tags: []
url: https://raw.githubusercontent.com/api-evangelist/agco/refs/heads/main/apis.yml
use_cases:
- description: Build web and mobile dashboards that display real-time machine location, performance, and fuel status for farm operators.
  name: Farm Management Dashboard
- description: Monitor machine fault codes and engine hours remotely to schedule preventive maintenance before failures occur.
  name: Predictive Maintenance
- description: Track machine location and activity data to document field operations, coverage areas, and productivity metrics.
  name: Field Work Tracking
- description: Monitor fuel levels and consumption rates across a fleet to optimize refueling logistics and reduce costs.
  name: Fuel Management
- description: Integrate AGCO machine data into existing farm management or precision agriculture software platforms.
  name: Telematics Integration
---
