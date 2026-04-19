---
api_count: 7
apis:
- description: RESTful API for managing Aruba Central cloud networking platform, providing unified network management, AI-based analytics, and IoT device security for wired, wireless, and SD-WAN networks. APIs follo
  name: Aruba Central API
  slug: ''
- description: REST API for ClearPass Policy Manager providing role- and device-based secure network access control for IoT, BYOD, corporate devices, as well as employees, contractors, and guests across any multiven
  name: Aruba ClearPass API
  slug: ''
- description: REST API for AOS-CX switches providing full programmability of switches running the AOS-CX operating system. Supports HTTPS POST, GET, PUT, PATCH, and DELETE methods and includes a built-in Swagger UI
  name: Aruba AOS-CX REST API
  slug: ''
- description: REST API for HPE Aruba Networking EdgeConnect SD-WAN providing programmatic access to Orchestrator and EdgeConnect appliance management, monitoring, and configuration. APIs are available at both the O
  name: Aruba EdgeConnect SD-WAN API
  slug: ''
- description: REST API for HPE Aruba Networking Fabric Composer, an intelligent software-defined orchestration solution that simplifies and accelerates leaf-spine network provisioning and day-to-day operations acro
  name: Aruba Fabric Composer API
  slug: ''
- description: API for HPE Aruba Networking User Experience Insight (UXI) providing programmatic access to onboarding tasks such as creating, modifying, or removing groups and assigning sensors, agents, networks, an
  name: Aruba User Experience Insight API
  slug: ''
- description: API for AirWave network management platform.
  name: Aruba AirWave API
  slug: ''
capabilities:
- description: Unified network management workflow combining Aruba Central API for device inventory, configuration groups, sites, access points, clients, and gateway monitoring. Used by network administrators to man
  name: Aruba Network Management
  slug: network-management
common:
- title: ''
  type: DeveloperPortal
  url: https://developer.arubanetworks.com
- title: ''
  type: Hub
  url: https://devhub.arubanetworks.com
- title: ''
  type: GitHubOrganization
  url: https://github.com/aruba
- title: ''
  type: Blog
  url: https://blogs.arubanetworks.com/
- title: ''
  type: Support
  url: https://www.arubanetworks.com/support-services/
- title: ''
  type: TermsOfService
  url: https://www.arubanetworks.com/company/legal/
- title: ''
  type: PrivacyPolicy
  url: https://www.arubanetworks.com/company/legal/privacy-policy/
created: '2024-01-01'
description: APIs for HPE Aruba Networking cloud networking, security, and infrastructure solutions including Central, AOS-CX, ClearPass, EdgeConnect SD-WAN, Fabric Composer, and User Experience Insight.
features:
- description: Single pane of glass for managing wired, wireless, and SD-WAN infrastructure across distributed enterprise environments.
  name: Unified Cloud Management
- description: Artificial intelligence and machine learning-driven network analytics for proactive troubleshooting and optimization.
  name: AI-Powered Analytics
- description: Role-based and device-based access control with ClearPass for IoT, BYOD, and enterprise devices.
  name: Zero Trust Security
- description: Programmable APIs across all platforms enabling infrastructure-as-code and automated provisioning.
  name: Network Automation
- description: Centralized management of EdgeConnect SD-WAN appliances with application-aware routing and WAN optimization.
  name: SD-WAN Orchestration
- description: Synthetic testing and real-time monitoring of network and application performance from the user perspective.
  name: User Experience Monitoring
image: https://www.arubanetworks.com/assets/img/logo.png
integrations:
- description: Ansible modules and playbooks for automating Aruba Central and AOS-CX switch configuration.
  name: Ansible
- description: Infrastructure-as-code provisioning for Aruba network infrastructure using Terraform providers.
  name: Terraform
- description: Integration with ServiceNow for IT service management and automated incident response.
  name: ServiceNow
- description: Log and event forwarding from Aruba infrastructure to Splunk for security analytics and monitoring.
  name: Splunk
- description: Integration with VMware environments for network-aware virtual infrastructure management.
  name: VMware vSphere
jsonld:
- class_count: 0
  name: Aruba Central Context
  property_count: 0
  slug: aruba-central-context
- class_count: 0
  name: Aruba Context
  property_count: 8
  slug: aruba-context
layout: provider
modified: '2026-04-18'
name: Aruba
rules:
- name: Aruba API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: aruba-spectral-rules
skills: []
slug: aruba
solutions: []
tags:
- Cloud
- Infrastructure
- Network Management
- Networking
- SD-WAN
- Security
- Switches
- Wireless
url: https://raw.githubusercontent.com/api-evangelist/aruba/refs/heads/main/apis.yml
use_cases:
- description: Automate provisioning, monitoring, and troubleshooting of campus wired and wireless networks using Central APIs.
  name: Campus Network Automation
- description: Programmatically deploy and manage EdgeConnect SD-WAN appliances across branch offices with centralized orchestration.
  name: Branch Office SD-WAN Deployment
- description: Automate secure onboarding and policy assignment for IoT devices using ClearPass APIs.
  name: IoT Device Onboarding
- description: Build custom monitoring dashboards using Central APIs to track device health, client connectivity, and network performance.
  name: Network Health Dashboards
- description: Manage groups, sites, and device configurations across multiple locations programmatically.
  name: Multi-Site Configuration Management
---
