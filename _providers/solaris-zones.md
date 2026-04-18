---
api_count: 9
apis:
- description: Core API for creating, managing, and monitoring Solaris Zones.
  name: Solaris Zones Management API
  slug: ''
- description: API endpoints for zone configuration and resource management.
  name: Zone Configuration API
  slug: ''
- description: API for zone lifecycle management including install, boot, halt, and delete operations.
  name: Zone Administration API
  slug: ''
- description: API for monitoring zone status, resource usage, and performance metrics.
  name: Zone Monitoring API
  slug: ''
- description: 'Remote Administration Daemon REST API for programmatic zone management via the com.oracle.solaris.rad.zonemgr module, supporting zone creation, configuration, migration, and lifecycle operations over '
  name: RAD Zone Management REST API
  slug: ''
- description: The libzonestat.so.1 C library API used to retrieve and compute zone-related resource utilization information including physical memory, virtual memory, and CPU resources with sorting and filtering op
  name: Zones Monitoring Statistics API (libzonestat)
  slug: ''
- description: API for creating and managing Oracle Solaris Kernel Zones, which are non-global zones with their own kernel providing greater independence and enhanced security isolation.
  name: Oracle Solaris Kernel Zones API
  slug: ''
- description: 'REST API and web interface for accessing the Oracle Solaris 11.4 StatsStore, providing consolidated zone resource statistics, system performance data, and historical analytics via CLI, C, Python, and '
  name: Oracle Solaris StatsStore and Analytics API
  slug: ''
- description: API for creating, deploying, and managing Unified Archives for zone system recovery, cloning, and migration across Oracle Solaris systems.
  name: Oracle Solaris Unified Archives Zones API
  slug: ''
capabilities:
- description: Unified zone lifecycle workflow combining zone creation, configuration, administration, monitoring, and migration. Used by system administrators and platform engineers to manage Solaris virtualization
  name: Solaris Zone Lifecycle Management
  slug: zone-lifecycle
common:
- title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- title: ''
  type: Authentication
  url: https://docs.oracle.com/en/cloud/paas/api-platform/authentication.html
- title: ''
  type: Support
  url: https://www.oracle.com/support/
- title: ''
  type: Blog
  url: https://blogs.oracle.com/solaris/
- title: ''
  type: Portal
  url: https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/index.html
- title: Developer Resources
  type: Resources
  url: https://www.oracle.com/solaris/technologies/solarisdeveloper.html
- title: ''
  type: GitHubOrganization
  url: https://github.com/oracle/oraclesolaris-contrib
- title: ''
  type: GettingStarted
  url: https://docs.oracle.com/cd/E37838_01/html/E61038/gitsf.html
- title: Virtual Environments Overview
  type: Documentation
  url: https://docs.oracle.com/cd/E37838_01/html/E61037/zonesoverview.html
- title: Zones Configuration Resources
  type: Documentation
  url: https://docs.oracle.com/cd/E37838_01/html/E61040/
- title: RAD Client Guide
  type: Documentation
  url: https://docs.oracle.com/cd/E37838_01/html/E68270/gpzpd.html
- title: ''
  type: JSONLD
  url: json-ld/solaris-context.jsonld
- title: ''
  type: JSONSchema
  url: json-schema/solaris-zone-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/solaris-zone-resource-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/solaris-zone-stats-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/solaris-zone-migration-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/solaris-zone-evacuation-schema.json
created: '2024'
description: API for managing Solaris Zones (containers) and virtualization on Oracle Solaris systems.
features:
- description: Hardware-enforced isolation between zones providing secure multi-tenant environments on a single physical system.
  name: Zone Isolation
- description: Move running zones between physical systems without downtime using live migration capabilities.
  name: Live Migration
- description: Non-global zones with their own independent kernel for enhanced security isolation and OS independence.
  name: Kernel Zones
- description: Create portable system archives for zone cloning, recovery, and migration across Solaris systems.
  name: Unified Archives
- description: Consolidated resource statistics and historical analytics for monitoring zone performance and capacity planning.
  name: StatsStore Analytics
- description: RESTful remote administration daemon enabling programmatic zone management over HTTP/JSON.
  name: RAD Remote Administration
- description: Fine-grained CPU, memory, and swap resource controls with configurable caps per zone.
  name: Resource Capping
image: https://www.oracle.com/a/ocom/img/cb71-solaris.jpg
integrations:
- description: Manage Solaris Zones through Oracle Enterprise Manager for centralized infrastructure monitoring and control.
  name: Oracle Enterprise Manager
- description: Automate zone provisioning and configuration management using Ansible playbooks with Oracle Solaris modules.
  name: Ansible
- description: Configure and manage Solaris Zones infrastructure as code using Puppet modules for Oracle Solaris.
  name: Puppet
jsonld:
- class_count: 0
  name: Solaris Context
  property_count: 12
  slug: solaris-context
- class_count: 0
  name: Solaris Kernel Zones Context
  property_count: 0
  slug: solaris-kernel-zones-context
- class_count: 0
  name: Solaris Rad Zonemgr Context
  property_count: 0
  slug: solaris-rad-zonemgr-context
- class_count: 0
  name: Solaris Statsstore Context
  property_count: 0
  slug: solaris-statsstore-context
- class_count: 0
  name: Solaris Unified Archives Context
  property_count: 0
  slug: solaris-unified-archives-context
- class_count: 0
  name: Solaris Zone Administration Context
  property_count: 0
  slug: solaris-zone-administration-context
- class_count: 0
  name: Solaris Zone Configuration Context
  property_count: 0
  slug: solaris-zone-configuration-context
- class_count: 0
  name: Solaris Zone Monitoring Context
  property_count: 0
  slug: solaris-zone-monitoring-context
- class_count: 0
  name: Solaris Zone Stats Context
  property_count: 0
  slug: solaris-zone-stats-context
- class_count: 0
  name: Solaris Zones Context
  property_count: 15
  slug: solaris-zones-context
- class_count: 0
  name: Solaris Zones Management Context
  property_count: 0
  slug: solaris-zones-management-context
layout: provider
modified: '2026-04-18'
name: Solaris Zones
rules:
- name: Solaris Zones API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: solaris-zones-spectral-rules
skills: []
slug: solaris-zones
solutions: []
tags:
- Containers
- Kernel Zones
- Operating Systems
- Oracle
- RAD
- Resource Management
- Solaris
- StatsStore
- Virtualization
- Zones
url: https://docs.oracle.com/en/operating-systems/solaris.html
use_cases:
- description: Consolidate multiple workloads onto a single physical system using zones for resource isolation and management.
  name: Server Consolidation
- description: Create isolated development and testing environments that mirror production without dedicated hardware.
  name: Development and Testing
- description: Use Unified Archives and zone migration to implement disaster recovery workflows across Solaris systems.
  name: Disaster Recovery
- description: Monitor zone resource utilization and system performance using StatsStore and zonestat APIs.
  name: Performance Monitoring
- description: Programmatically create, configure, and deploy zones using RAD REST APIs for automated infrastructure provisioning.
  name: Automated Provisioning
---
