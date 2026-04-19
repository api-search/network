---
api_count: 12
apis:
- description: RESTful API for programmatic access to Nexus switches using HTTP/HTTPS.
  name: Cisco NX-API REST
  slug: ''
- description: API that accepts show commands and configuration commands in CLI format.
  name: Cisco NX-API CLI
  slug: ''
- description: Unified API for Nexus Dashboard Insights, Orchestrator, and Fabric Controller.
  name: Cisco Nexus Dashboard REST API
  slug: ''
- description: REST API for managing and automating Nexus and MDS fabrics including LAN, SAN, and IP Fabric for Media deployments.
  name: Cisco Nexus Dashboard Fabric Controller API
  slug: ''
- description: API for multi-site orchestration of ACI, Cloud ACI, and DCNM fabrics with policy management and segmentation.
  name: Cisco Nexus Dashboard Orchestrator API
  slug: ''
- description: API for network analytics, telemetry, anomaly detection, and troubleshooting across data center fabrics.
  name: Cisco Nexus Dashboard Insights API
  slug: ''
- description: Data Center Network Manager API for managing Nexus fabric deployments.
  name: Cisco DCNM REST API
  slug: ''
- description: Model-driven API using YANG data models for Nexus devices.
  name: Cisco NETCONF/YANG API
  slug: ''
- description: HTTP-based protocol for configuring YANG-defined data on Nexus switches supporting XML and JSON payload encodings.
  name: Cisco NX-OS RESTCONF API
  slug: ''
- description: gRPC Network Management Interface for streaming telemetry and configuration management on Nexus switches.
  name: Cisco NX-OS gNMI/gRPC API
  slug: ''
- description: Streaming telemetry interface for real-time operational data collection from Nexus switches using YANG models.
  name: Cisco NX-OS Model-Driven Telemetry API
  slug: ''
- description: Python Software Development Kit for programmatic access to Nexus 9000 Series switch modules including interfaces, VLANs, ACLs, and routes.
  name: Cisco NX-OS Python SDK API
  slug: ''
capabilities:
- description: Unified workflow for network administrators to configure and monitor Cisco Nexus switches including interfaces, VLANs, routing, and system features via the NX-API REST DME object model.
  name: Cisco Nexus Switch Management
  slug: switch-management
common:
- title: ''
  type: DeveloperPortal
  url: https://developer.cisco.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- title: ''
  type: Training
  url: https://developer.cisco.com/learning/labs/tags/Nexus/
- title: ''
  type: Sandbox
  url: https://devnetsandbox.cisco.com/
- title: ''
  type: Support
  url: https://developer.cisco.com/site/support/
- title: ''
  type: StatusPage
  url: https://status.cisco.com/
- title: ''
  type: CodeExamples
  url: https://developer.cisco.com/codeexchange/
- title: ''
  type: NaftikoCapability
  url: capabilities/switch-management.yaml
created: '2024'
description: APIs for managing and monitoring Cisco Nexus data center switches and network infrastructure.
features:
- description: RESTful access to the NX-OS Data Management Engine object model for switch configuration and operational state through managed objects.
  name: DME Object Model REST API
- description: Create, modify, and delete VLAN bridge domains and Switch Virtual Interfaces for Layer 2 and Layer 3 networking.
  name: VLAN and SVI Management
- description: Programmatically configure physical Ethernet interfaces including speed, duplex, MTU, switchport mode, and VLAN assignment.
  name: Interface Configuration
- description: Configure and monitor BGP routing protocol including neighbors, route policies, and address families.
  name: BGP Routing Management
- description: Create and manage IPv4 static routes across VRFs with next-hop specifications and route preferences.
  name: Static Route Management
- description: Enable and disable NX-OS features programmatically including interface-vlan, BGP, OSPF, and LACP.
  name: Feature Management
- description: Real-time operational data collection using gNMI/gRPC and model-driven telemetry with YANG models.
  name: Streaming Telemetry
- description: Unified policy management and orchestration across multiple ACI, Cloud ACI, and DCNM fabrics.
  name: Multi-Site Orchestration
image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
integrations:
- description: Automate Nexus switch configuration using Ansible NX-OS modules and playbooks for declarative network management.
  name: Ansible
- description: Provision and manage Cisco ACI and Nexus infrastructure using the Terraform Cisco provider.
  name: Terraform
- description: Application Centric Infrastructure integration for policy-driven network automation with Nexus 9000 switches.
  name: Cisco ACI
- description: Forward NX-OS streaming telemetry and syslog data to Splunk for network analytics and SIEM integration.
  name: Splunk
- description: Integrate Nexus Dashboard events and alerts with ServiceNow ITSM for automated incident management.
  name: ServiceNow
jsonld:
- class_count: 3
  name: Cisco Nexus Context
  property_count: 15
  slug: cisco-nexus-context
- class_count: 0
  name: Cisco Nexus Nxapi Rest Context
  property_count: 0
  slug: cisco-nexus-nxapi-rest-context
layout: provider
modified: '2026-04-19'
name: Cisco Nexus Dashboard
rules:
- name: Cisco Nexus Dashboard API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: cisco-nexus-spectral-rules
skills: []
slug: cisco-nexus
solutions: []
tags:
- Data Center
- Infrastructure
- Network Automation
- Networking
- SDN
- Switches
url: https://developer.cisco.com/site/nexus/
use_cases:
- description: Automate switch configuration, VLAN provisioning, and routing changes across large-scale data center fabrics.
  name: Data Center Network Automation
- description: Collect real-time telemetry data from Nexus switches for performance monitoring, anomaly detection, and capacity planning.
  name: Network Monitoring and Analytics
- description: Orchestrate network policies and connectivity across geographically distributed data center fabrics.
  name: Multi-Site Fabric Management
- description: Define and manage network infrastructure configurations using YANG models, NETCONF, and RESTCONF for version-controlled deployments.
  name: Infrastructure as Code
- description: Programmatically verify switch configurations against security baselines and generate compliance reports.
  name: Compliance and Auditing
---
