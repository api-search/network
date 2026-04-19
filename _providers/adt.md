---
api_count: 2
apis:
- description: The ADT+ Platform API provides programmatic access to ADT's smart home security platform, enabling management of security devices, sensors, cameras, locks, and automation rules. Supports real-time sta
  name: ADT+ Platform API
  slug: ''
- description: The ADT Business API provides commercial security management capabilities including multi-site access control, commercial alarm management, video surveillance integration, and security event monitorin
  name: ADT Business API
  slug: ''
capabilities:
- description: Unified workflow capability for managing ADT smart home security systems, monitoring alarm events, controlling devices, managing access codes, and retrieving video clips. Designed for homeowners, prop
  name: ADT Home Security Management
  slug: home-security-management
common:
- title: ''
  type: Website
  url: https://www.adt.com
- title: ''
  type: Portal
  url: https://www.adt.com/smart-home
- title: ''
  type: Support
  url: https://www.adt.com/support
- title: ''
  type: Blog
  url: https://www.adt.com/about-adt/news
- title: ''
  type: TermsOfService
  url: https://www.adt.com/terms-of-service
- title: ''
  type: PrivacyPolicy
  url: https://www.adt.com/privacy-policy
- title: ''
  type: Login
  url: https://www.adt.com/login
- title: ''
  type: SignUp
  url: https://www.adt.com/get-a-quote
created: '2024-01-01'
description: ADT is a provider of monitored security, interactive home and business automation, and related monitoring services for residential and small business customers across the United States and Canada. ADT offers smart home security systems, professional monitoring, video surveillance, access control, and automation integrations with Google Nest, Amazon Alexa, and Z-Wave smart home devices through the ADT+ platform.
features:
- description: 24/7 professional monitoring center that responds to alarms, contacts emergency services, and alerts homeowners.
  name: Professional Security Monitoring
- description: Programmatic control of lights, locks, thermostats, and smart plugs integrated with the ADT+ security platform.
  name: Smart Home Automation
- description: Access and retrieve recorded video clips from indoor, outdoor, and doorbell cameras via API.
  name: Video Surveillance and Clips
- description: Remotely arm and disarm security systems and zones through authenticated API calls.
  name: Remote Arm and Disarm
- description: Real-time status monitoring of door sensors, motion detectors, smoke detectors, and flood sensors.
  name: Sensor and Device Status
- description: Manage smart locks, access codes, and entry permissions for residential and commercial properties.
  name: Access Control Management
- description: Receive real-time webhook notifications for alarm events, zone violations, and system status changes.
  name: Alarm Event Notifications
- description: Manage multiple properties and security systems from a single API integration for commercial customers.
  name: Multi-Site Management
image: /assets/icons/adt.png
integrations:
- description: Integration with Google Nest thermostats, cameras, and smart displays through ADT+ with Google partnership.
  name: Google Nest
- description: Voice control of ADT security system including arm, disarm, and status queries via Amazon Alexa.
  name: Amazon Alexa
- description: Voice control and smart home automation via Google Assistant and Nest Hub displays.
  name: Google Assistant
- description: Z-Wave wireless protocol support for smart locks, lights, thermostats, and other smart home devices.
  name: Z-Wave
- description: HomeKit-compatible devices that integrate with ADT security ecosystem.
  name: Apple HomeKit
- description: Integration with Ring video doorbells and cameras as complementary security devices.
  name: Ring
- description: Smart lighting control integration with Lutron Caseta and RadioRA systems.
  name: Lutron
jsonld:
- class_count: 11
  name: Adt Business Api Context
  property_count: 17
  slug: adt-business-api-context
- class_count: 19
  name: Adt Platform Api Context
  property_count: 31
  slug: adt-platform-api-context
layout: provider
modified: '2026-04-19'
name: ADT
rules:
- name: ADT API Rules
  rule_count: 31
  severity_counts:
    error: 16
    hint: 0
    info: 4
    warn: 11
  slug: adt-spectral-rules
skills: []
slug: adt
solutions: []
tags:
- Access Control
- Automation
- Home Security
- IoT
- Monitoring
- Security
- Smart Home
url: https://raw.githubusercontent.com/api-evangelist/adt/refs/heads/main/apis.yml
use_cases:
- description: Integrate ADT security with third-party home automation platforms like Google Home, Amazon Alexa, and Apple HomeKit.
  name: Home Automation Integration
- description: Manage access codes and security schedules for rental properties, vacation homes, and commercial buildings.
  name: Property Management
- description: Share security monitoring data with insurance providers for smart home insurance discount programs.
  name: Insurance Integration
- description: Trigger automated emergency responses, notifications, and camera recordings when alarms are triggered.
  name: Emergency Response Automation
- description: Analyze security events, access patterns, and alarm history for business operational insights.
  name: Business Intelligence
- description: Issue temporary access codes for service contractors with time-limited entry permissions.
  name: Contractor Access Management
---
