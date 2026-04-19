---
api_count: 1
apis:
- description: REST API for AWS Application Discovery Service covering agents, applications, configurations, exports, imports, and tags for on-premises infrastructure discovery.
  name: Amazon Application Discovery Service API
  slug: amazon-application-discovery-service-api
capabilities:
- description: Workflow capability for discovering on-premises infrastructure and preparing migration plans using AWS Application Discovery Service.
  name: Migration Discovery Workflow
  slug: migration-discovery
common: []
created: '2026-03-16'
description: Amazon Application Discovery Service helps enterprise customers plan application migration projects by automatically identifying servers, virtual machines, software, and software dependencies running in their on-premises data centers.
features:
- Agentless Discovery via VMware vCenter integration
- Agent-based discovery for physical and virtual servers
- Automatic server dependency mapping via network traffic analysis
- Application grouping and tagging for migration planning
- Data export to Amazon S3 in CSV and GraphML formats
- Bulk import of server inventory via CSV files
- Integration with AWS Migration Hub for centralized tracking
- Continuous data collection with configurable intervals
- Server neighbor discovery for dependency visualization
- Tag-based filtering and organization of discovered assets
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- AWS Migration Hub
- AWS Server Migration Service
- AWS Application Migration Service
- Amazon EC2
- Amazon S3
- VMware vCenter
- AWS Database Migration Service
- AWS CloudFormation
- AWS Systems Manager
- AWS Cost Explorer
jsonld:
- class_count: 69
  name: Amazon Application Discovery Service Context
  property_count: 113
  slug: amazon-application-discovery-service-context
layout: provider
modified: '2026-04-19'
name: Amazon Application Discovery Service
rules:
- name: Amazon Application Discovery Service API Rules
  rule_count: 21
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 6
  slug: amazon-application-discovery-service-spectral-rules
skills: []
slug: amazon-application-discovery-service
solutions: []
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
url: https://raw.githubusercontent.com/api-evangelist/amazon-application-discovery-service/refs/heads/main/apis.yml
use_cases:
- Discover all servers and processes in on-premises data centers before migration
- Map application dependencies to create migration groups and waves
- Export inventory data for detailed analysis and migration planning in third-party tools
- Import existing server inventory from CMDBs or spreadsheets without installing agents
- Track migration readiness across thousands of servers in a single dashboard
- Identify unknown servers and shadow IT in large enterprise environments
---
