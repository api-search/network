---
api_count: 1
apis:
- description: Akri exposes Prometheus metrics on port 8080 at /metrics for the Agent, Controller, and broker pods. Metrics include instance count, discovery response results and latency, and broker pod count. Suppo
  name: Akri Metrics API
  slug: metrics-api
capabilities:
- description: Workflow capability for monitoring Akri edge device discovery and broker health in Kubernetes clusters. Combines Prometheus metrics to provide visibility into discovered instances, discovery handler p
  name: Akri Edge Device Monitoring
  slug: edge-device-monitoring
common:
- title: ''
  type: GitHubOrganization
  url: https://github.com/project-akri
- title: ''
  type: GitHubRepository
  url: https://github.com/project-akri/akri
- title: ''
  type: Documentation
  url: https://docs.akri.sh/
- title: ''
  type: GettingStarted
  url: https://docs.akri.sh/user-guide/getting-started
- title: ''
  type: ChangeLog
  url: https://github.com/project-akri/akri/blob/main/CHANGELOG.md
- title: Helm Chart
  type: SDK
  url: https://artifacthub.io/packages/helm/akri-helm-charts/akri
- title: Example Brokers and Applications
  type: CodeExamples
  url: https://github.com/project-akri/examples
- title: Discovery Handler Template (Rust)
  type: SDK
  url: https://github.com/project-akri/akri-discovery-handler-template
- title: ''
  type: SpectralRules
  url: rules/akri-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/akri-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/akri-akri-context.jsonld
- title: Akri Metrics Shared Capability
  type: NaftikoCapability
  url: capabilities/shared/metrics.yaml
- title: Edge Device Monitoring Workflow
  type: NaftikoCapability
  url: capabilities/edge-device-monitoring.yaml
created: '2025-01-01'
description: Akri is a CNCF Sandbox project that exposes heterogeneous leaf devices (such as IP cameras and USB devices) as resources in a Kubernetes cluster. It enables dynamic discovery and utilization of IoT edge devices through protocol-specific Discovery Handlers for ONVIF, OPC UA, and udev, with automatic workload scheduling and high availability.
features:
- description: Automatically discovers heterogeneous leaf devices (IP cameras, USB devices, industrial sensors) across Kubernetes cluster nodes using protocol-specific Discovery Handlers.
  name: Dynamic Device Discovery
- description: Discovers IP cameras via ONVIF standards and RTSP streams, with filtering by IP address, MAC address, ONVIF scopes, and device UUIDs.
  name: ONVIF Discovery Handler
- description: Discovers industrial automation servers and Local Discovery Servers via OPC UA protocol, supporting x509 certificate authentication for secure connections.
  name: OPC UA Discovery Handler
- description: Discovers locally attached hardware (USB devices, cameras, microphones) on Linux nodes using udev rules with kernel device name and capability filtering.
  name: udev Discovery Handler
- description: Automatically schedules broker Pods or Jobs per discovered device based on Akri Configuration specifications, managing the full workload lifecycle.
  name: Automatic Workload Scheduling
- description: Multiple nodes can access a single leaf device, ensuring service continuity if a node fails. Supports multi-node device reservation.
  name: High Availability
- description: 'Two CRDs: configurations.akri.sh for discovery specification and instances.akri.sh representing each discovered device as a Kubernetes resource.'
  name: Kubernetes Custom Resources
- description: Community can implement custom Discovery Handlers as DaemonSets using the akri-discovery-handler-template, enabling support for any device protocol.
  name: Extensible Discovery Handler Framework
- description: Built-in Prometheus metrics on port 8080 for instance count, discovery response results, discovery latency, and broker pod count, with Grafana visualization support.
  name: Prometheus Metrics
- description: Supports Linux nodes on amd64, arm64v8, and arm32v7 architectures with Kubernetes v1.16+, K3s, and MicroK8s distributions.
  name: Multi-Architecture Support
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Native Prometheus metrics integration via ServiceMonitor and PodMonitor custom resources, with Grafana visualization support.
  name: Prometheus
- description: Official Helm chart packaging for deploying Akri Controller, Agent DaemonSet, and Discovery Handler DaemonSets.
  name: Helm
- description: Extends the Kubernetes Device Plugin Framework with edge-specific capabilities for heterogeneous leaf device management.
  name: Kubernetes Device Plugin Framework
- description: Built-in ONVIF protocol support for discovering and managing standards-compliant IP cameras and video devices.
  name: ONVIF
- description: Built-in OPC UA protocol support for industrial automation device discovery with certificate-based security.
  name: OPC UA
- description: Built-in udev integration for discovering locally attached hardware devices on Linux Kubernetes nodes.
  name: Linux udev
- description: CNCF Sandbox project integrating with cloud native tooling including K3s, MicroK8s, and standard Kubernetes distributions.
  name: CNCF Ecosystem
jsonld:
- class_count: 6
  name: Akri Akri Context
  property_count: 19
  slug: akri-akri-context
layout: provider
modified: '2026-04-19'
name: Akri
rules:
- name: Akri API Rules
  rule_count: 25
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 12
  slug: akri-spectral-rules
skills: []
slug: akri
solutions: []
tags:
- Device Management
- Edge Computing
- IoT
- Kubernetes
- CNCF
- Open Source
- OPC UA
- ONVIF
- udev
url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/apis.yml
use_cases:
- description: Expose and manage IoT leaf devices such as IP cameras and USB sensors as first-class Kubernetes resources for edge computing workloads.
  name: Edge IoT Device Management
- description: Connect industrial OPC UA servers and automation equipment to Kubernetes clusters for real-time monitoring and control workflows.
  name: Industrial Automation Integration
- description: Deploy ONVIF-compliant IP camera brokers automatically as cameras are discovered, enabling distributed computer vision processing.
  name: Computer Vision at the Edge
- description: Automatically schedule GPU, FPGA, or specialized hardware workloads based on real-time device availability across cluster nodes.
  name: Dynamic Hardware Resource Scheduling
- description: Manage fleets of diverse edge devices with different protocols from a single Kubernetes control plane using unified Configuration resources.
  name: Heterogeneous Device Fleet Management
---
