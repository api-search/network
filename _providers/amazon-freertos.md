---
api_count: 1
apis:
- description: The Amazon FreeRTOS API provides programmatic access to manage FreeRTOS software configurations and over-the-air update jobs for IoT devices running FreeRTOS.
  name: Amazon FreeRTOS API
  slug: amazon-freertos-api
capabilities:
- description: Manage FreeRTOS software configurations and OTA firmware updates for microcontroller IoT devices.
  name: Amazon FreeRTOS Device Management
  slug: amazon-freertos-device-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/freertos/
- title: ''
  type: Website
  url: https://aws.amazon.com/freertos/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/freertos/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/iot/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: GitHubRepository
  url: https://github.com/aws/amazon-freertos
- title: ''
  type: Console
  url: https://console.aws.amazon.com/iot/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-freertos
- title: ''
  type: SpectralRules
  url: rules/amazon-freertos-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/freertos.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-freertos-device-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-freertos-vocabulary.yaml
- title: ''
  type: JSON-LD
  url: json-ld/amazon-freertos-context.jsonld
created: '2026-03-16'
description: Amazon FreeRTOS is an open source, real-time operating system for microcontrollers that makes it easy to program, deploy, secure, connect, and manage small, low-power edge devices. It extends the FreeRTOS kernel with libraries for secure connectivity, over-the-air updates, and more.
features:
- description: Open-source real-time operating system kernel with preemptive multitasking for microcontrollers.
  name: FreeRTOS Kernel
- description: Over-the-air firmware update delivery with code signing verification and rollback support.
  name: OTA Update Management
- description: TLS 1.2/1.3 encrypted MQTT and HTTP connectivity using AWS IoT Core.
  name: Secure Connectivity
- description: Zero-touch device provisioning using AWS IoT Fleet Provisioning and Just-In-Time Registration.
  name: Device Provisioning
- description: Cryptographic library for secure key storage and operations on embedded devices.
  name: corePKCS11
- description: IPv4/IPv6 TCP/IP networking stack optimized for embedded systems.
  name: FreeRTOS+TCP
- description: Over 100 partner-qualified hardware platforms from major MCU vendors including Espressif, ST, NXP, Renesas.
  name: Qualified Hardware
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Primary cloud backend for FreeRTOS device messaging, shadow state, and job management.
  name: AWS IoT Core
- description: Extend cloud intelligence to FreeRTOS edge devices for local compute and ML inference.
  name: AWS IoT Greengrass
- description: Register, organize, monitor, and remotely manage FreeRTOS device fleets.
  name: AWS IoT Device Management
- description: Audit and monitor FreeRTOS device security posture for anomalies and policy violations.
  name: AWS IoT Device Defender
- description: Store firmware binaries for OTA update delivery to FreeRTOS devices.
  name: Amazon S3
- description: Manage code signing keys for secure firmware distribution.
  name: AWS KMS
- description: Automate FreeRTOS fleet infrastructure provisioning with infrastructure-as-code templates.
  name: AWS CloudFormation
jsonld:
- class_count: 5
  name: Amazon Freertos Context
  property_count: 11
  slug: amazon-freertos-context
layout: provider
modified: '2026-04-19'
name: Amazon FreeRTOS
rules:
- name: Amazon FreeRTOS API Rules
  rule_count: 25
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 16
  slug: amazon-freertos-spectral-rules
skills: []
slug: amazon-freertos
solutions: []
tags:
- AWS
- Embedded Systems
- IoT
- Microcontrollers
- RTOS
url: https://raw.githubusercontent.com/api-evangelist/amazon-freertos/refs/heads/main/apis.yml
use_cases:
- description: Deploy FreeRTOS on industrial sensors for secure cloud connectivity and remote firmware updates.
  name: Industrial IoT Sensors
- description: Build connected home devices with low-power FreeRTOS firmware and AWS IoT integration.
  name: Smart Home Devices
- description: Develop GPS and location tracking devices with FreeRTOS for fleet and supply chain monitoring.
  name: Asset Tracking
- description: Collect vibration, temperature, and current data from FreeRTOS devices for ML-based maintenance prediction.
  name: Predictive Maintenance
- description: Build FDA-validated medical devices with FreeRTOS for remote patient monitoring and diagnostics.
  name: Medical IoT
- description: Deploy smart meters and grid sensors running FreeRTOS for utility data collection and OTA updates.
  name: Energy Management
---
