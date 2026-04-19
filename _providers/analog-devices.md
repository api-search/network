---
api_count: 3
apis:
- description: The libiio library provides a cross-platform C API for interfacing with Linux Industrial I/O (IIO) devices including ADCs, DACs, and RF transceivers. It supports local and remote device access via a n
  name: Analog Devices libiio API
  slug: libiio-api
- description: PyADI-IIO provides Python interfaces for ADI hardware with IIO drivers, enabling Python developers to interact with ADI evaluation boards and production hardware. It abstracts libiio with device-speci
  name: Analog Devices PyADI-IIO Python API
  slug: pyadi-iio-api
- description: CodeFusion Studio is ADI's embedded software development environment built on Visual Studio Code for ADI microcontrollers and DSPs. It provides graphical system configuration, code generation, debuggi
  name: Analog Devices CodeFusion Studio
  slug: codefusion-studio
common:
- title: ''
  type: Portal
  url: https://www.analog.com
- title: ''
  type: DeveloperPortal
  url: https://developer.analog.com
- title: ''
  type: Documentation
  url: https://www.analog.com/en/software.html
- title: ''
  type: GitHubOrganization
  url: https://github.com/analogdevicesinc
- title: ''
  type: Blog
  url: https://www.analog.com/en/resources/media-center/analog-dialogue.html
- title: ''
  type: Support
  url: https://ez.analog.com/
- title: ''
  type: JSONSchema
  url: json-schema/analog-devices-iio-device-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/analog-devices-iio-context-schema.json
- title: ''
  type: JSONLD
  url: json-ld/analog-devices-context.jsonld
- title: ''
  type: Vocabulary
  url: vocabulary/analog-devices-vocabulary.yaml
- title: ''
  type: SpectralRules
  url: rules/analog-devices-spectral-rules.yml
created: ''
description: Analog Devices (ADI) is a global semiconductor company designing high-performance analog, mixed-signal, and digital signal processing integrated circuits for industrial, communications, automotive, and consumer markets. ADI provides developer tools through its CodeFusion Studio embedded development environment and the ADI Developer Portal. ADI's APIs are primarily embedded software APIs for microcontrollers and DSPs via the libiio library for Linux Industrial I/O devices, pyadi-iio Python interfaces, and security APIs within the ADI Assure Trusted Edge Security Architecture. The company also maintains the no-OS driver library for bare-metal embedded systems.
features:
- description: libiio library for accessing Linux Industrial I/O devices over USB, network, and local interfaces.
  name: Linux IIO Interface
- description: PyADI-IIO provides Pythonic device-specific APIs for ADI transceivers, converters, and sensors.
  name: Python Hardware Interfaces
- description: ADI Assure security APIs for hardware root of trust, secure boot, and cryptographic operations.
  name: Embedded Security APIs
- description: Bare-metal C drivers for ADI ICs without requiring an operating system.
  name: No-OS Drivers
- description: VS Code-based IDE for ADI MCUs and DSPs with graphical configuration and code generation.
  name: CodeFusion Studio
- description: Active contributor to Linux kernel IIO subsystem, Zephyr RTOS, and other open source projects.
  name: Open Source Ecosystem
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: ADI actively contributes drivers to the Linux kernel IIO framework.
  name: Linux Kernel IIO Subsystem
- description: ADI maintains hardware support for ADI MCUs in the Zephyr real-time operating system.
  name: Zephyr RTOS
- description: Integration with GNU Radio for software-defined radio applications using ADI transceivers.
  name: GNU Radio
- description: MathWorks toolbox support for ADI hardware for signal processing prototyping.
  name: MATLAB/Simulink
- description: CodeFusion Studio is built as a VS Code extension for embedded development.
  name: Microsoft Visual Studio Code
jsonld:
- class_count: 5
  name: Analog Devices Context
  property_count: 6
  slug: analog-devices-context
layout: provider
modified: '2026-04-19'
name: Analog Devices
rules:
- name: Analog Devices API Rules
  rule_count: 4
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 0
  slug: analog-devices-spectral-rules
skills: []
slug: analog-devices
solutions: []
tags:
- Embedded Systems
- Hardware
- IoT
- Semiconductor
- Signal Processing
url: https://raw.githubusercontent.com/api-evangelist/analog-devices/refs/heads/main/apis.yml
use_cases:
- description: High-accuracy data acquisition from ADI ADCs and sensors using libiio or PyADI-IIO.
  name: Precision Measurement
- description: Control of RF transceivers like ADRV9002 and AD9361 for SDR and communications applications.
  name: RF and Communications
- description: Integration of ADI industrial ICs into factory automation and process control systems.
  name: Industrial Automation
- description: Building secure edge devices with hardware root of trust using ADI Assure security APIs.
  name: Secure IoT Devices
- description: Developing motor drive applications using ADI ADSP processors and evaluation kits.
  name: Motor Control
---
