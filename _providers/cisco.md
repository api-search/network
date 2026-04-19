---
api_count: 8
apis:
- description: RESTful API for managing Cisco Meraki cloud-managed networking devices including wireless access points, switches, security appliances, and cameras. Supports network configuration, monitoring, and aut
  name: Cisco Meraki Dashboard API
  slug: meraki-api
- description: REST API for Webex collaboration platform enabling messaging, meeting management, device control, and administration. Supports bots, integrations, and embedded apps for extending Webex functionality.
  name: Cisco Webex API
  slug: webex-api
- description: 'REST API for Cisco Catalyst Center (formerly DNA Center), providing intent-based networking capabilities including network design, provisioning, assurance, and policy management for enterprise campus '
  name: Cisco Catalyst Center API
  slug: catalyst-center-api
- description: REST API for Cisco Application Centric Infrastructure (ACI) providing programmable access to data center network fabric configuration, policy management, and monitoring through the APIC controller.
  name: Cisco ACI API
  slug: aci-api
- description: REST API for Cisco Identity Services Engine (ISE) enabling network access policy management, guest services, BYOD onboarding, and security group administration for zero-trust network access.
  name: Cisco ISE API
  slug: ise-api
- description: REST API for Cisco Intersight cloud operations platform providing infrastructure management, workload optimization, and lifecycle automation for Cisco UCS, HyperFlex, and third-party infrastructure.
  name: Cisco Intersight API
  slug: intersight-api
- description: REST API for Cisco SD-WAN (formerly Viptela) providing programmatic access to WAN edge device management, policy configuration, monitoring, and analytics through the vManage controller.
  name: Cisco SD-WAN API
  slug: sdwan-api
- description: REST API for Cisco ThousandEyes digital experience monitoring platform, providing access to network, application, and internet visibility data for monitoring end-to-end digital experiences.
  name: Cisco ThousandEyes API
  slug: thousandeyes-api
capabilities:
- description: Unified network management workflow combining Meraki, Catalyst Center, and SD-WAN APIs for network administrators.
  name: Cisco Network Management
  slug: network-management
common:
- title: ''
  type: Portal
  url: https://developer.cisco.com/
- title: ''
  type: Documentation
  url: https://developer.cisco.com/docs/
- title: ''
  type: GettingStarted
  url: https://developer.cisco.com/learning/
- title: ''
  type: Blog
  url: https://blogs.cisco.com/developer
- title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- title: ''
  type: Support
  url: https://developer.cisco.com/site/support/
- title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software.html
- title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- title: ''
  type: Sandbox
  url: https://developer.cisco.com/site/sandbox/
- title: ''
  type: Training
  url: https://developer.cisco.com/certification/
- title: ''
  type: YouTube
  url: https://www.youtube.com/ciscodevnet
- title: ''
  type: X
  url: https://twitter.com/CiscoDevNet
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/cisco
created: '2024-01-01'
description: Cisco provides a comprehensive suite of APIs across its networking, security, collaboration, and cloud infrastructure platforms. Through Cisco DevNet, developers can access REST APIs, SDKs, and developer tools for Meraki, Webex, Catalyst Center, ACI, ISE, Intersight, ThousandEyes, SD-WAN, and other Cisco products to automate network operations, build integrations, and extend platform capabilities.
features:
- description: Automate network device configuration, provisioning, and management across campus, branch, and data center environments.
  name: Network Automation
- description: Define business intent and let the network translate it into device configurations automatically.
  name: Intent-Based Networking
- description: Manage distributed networks from the cloud with Meraki APIs for simplified operations.
  name: Cloud-Managed Networking
- description: Monitor end-to-end digital experiences with ThousandEyes for network, application, and internet visibility.
  name: Digital Experience Monitoring
- description: Implement zero-trust network access policies with ISE APIs for identity-based segmentation.
  name: Zero Trust Security
- description: Define and manage network infrastructure programmatically using APIs and configuration management tools.
  name: Infrastructure as Code
image: /assets/icons/cisco.png
integrations:
- description: Network automation modules for Cisco platforms including IOS, NX-OS, ACI, and Meraki.
  name: Ansible
- description: Terraform providers for Cisco ACI, Intersight, Meraki, and other platforms for infrastructure as code.
  name: Terraform
- description: ITSM integration for automated incident management and change control with Cisco platforms.
  name: ServiceNow
- description: Security and network analytics integration for log aggregation and threat detection.
  name: Splunk
- description: Python SDKs and libraries for all major Cisco platforms including Meraki, Webex, and ACI.
  name: Python
jsonld:
- class_count: 4
  name: Cisco Context
  property_count: 14
  slug: cisco-context
layout: provider
modified: '2026-04-18'
name: Cisco
rules:
- name: Cisco API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 6
  slug: cisco-spectral-rules
skills: []
slug: cisco
solutions: []
tags:
- Collaboration
- Enterprise
- Networking
- Security
- SD-WAN
url: https://raw.githubusercontent.com/api-evangelist/cisco/refs/heads/main/apis.yml
use_cases:
- description: Automate network device configuration changes across thousands of devices using APIs and templates.
  name: Network Configuration Management
- description: Programmatically manage access control policies, security groups, and compliance enforcement.
  name: Security Policy Automation
- description: Build bots, integrations, and custom applications on the Webex platform for team collaboration.
  name: Collaboration Integration
- description: Manage hybrid cloud infrastructure with Intersight APIs for lifecycle management and workload optimization.
  name: Cloud Infrastructure Management
- description: Collect and analyze network telemetry data for performance monitoring and troubleshooting.
  name: Network Monitoring and Analytics
---
