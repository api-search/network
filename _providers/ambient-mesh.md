---
api_count: 1
apis:
- description: Ambient Mesh provides a sidecar-less service mesh via the Kubernetes Gateway API and Istio ambient mode. It exposes configuration APIs for traffic management, security policies, resilience settings, a
  name: Ambient Mesh
  slug: ambient-mesh
common:
- title: ''
  type: Website
  url: https://ambientmesh.io/
- title: ''
  type: Documentation
  url: https://ambientmesh.io/docs/
- title: ''
  type: GettingStarted
  url: https://ambientmesh.io/docs/quickstart/
- title: ''
  type: Blog
  url: https://ambientmesh.io/blog/
- title: ''
  type: GitHubOrganization
  url: https://github.com/istio
- title: ''
  type: GitHubRepository
  url: https://github.com/istio/istio
created: '2026-04-19'
description: Ambient Mesh is a sidecar-less service mesh architecture built on Istio that simplifies microservices communication, enhances zero-trust security, and improves observability without requiring sidecar proxy injection. It uses a shared per-node proxy (ztunnel) for zero-trust security and optional waypoint proxies for advanced Layer 7 policies, enabling seamless migration from sidecar-based meshes with zero downtime.
features:
- description: Operates at the platform layer without sidecar proxy injection, reducing resource overhead and operational complexity while maintaining full service mesh capabilities.
  name: Sidecar-Less Architecture
- description: SPIFFE-based workload identity with automatic mutual TLS encryption between workloads, certificate management, and zero-trust network policies enforced by ztunnel.
  name: Zero-Trust Security
- description: Advanced traffic routing, load balancing, traffic splitting, mirroring, blue-green deployments, and gateway management via Kubernetes Gateway API HTTPRoute resources.
  name: Traffic Management
- description: Zone-aware load balancing, circuit breaking, outlier detection, fault injection, timeouts, and retry budgets for high-availability workloads.
  name: Resilience
- description: Distributed tracing, performance metrics via Prometheus, Kiali observability console, and HTTP observability for traffic visualization and security verification.
  name: Observability
- description: Free migration tooling for upgrading from sidecar-based architectures with automated workload analysis and risk mitigation for waypoint proxy requirements.
  name: Zero-Downtime Migration
- description: Optional per-namespace or per-workload Layer 7 proxies that provide advanced policy enforcement without requiring per-pod sidecar containers.
  name: Waypoint Proxies
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Ambient Mesh is built on Istio ambient mode, using its control plane and CRDs for configuration.
  name: Istio
- description: Uses the standard Kubernetes Gateway API with HTTPRoute, Gateway, and GRPCRoute resources for traffic management.
  name: Kubernetes Gateway API
- description: Integrates with Prometheus for metrics collection and monitoring of mesh traffic and performance.
  name: Prometheus
- description: Integrates with Kiali for service mesh observability, traffic visualization, and security verification.
  name: Kiali
- description: Solo.io's Gloo Mesh provides enterprise-grade ambient mesh management for scaling across enterprise workloads.
  name: Gloo Mesh
- description: Red Hat OpenShift Service Mesh 3.x supports Istio ambient mode for OpenShift deployments.
  name: OpenShift
layout: provider
modified: '2026-04-19'
name: Ambient Mesh
skills: []
slug: ambient-mesh
solutions: []
tags:
- Service Mesh
- Istio
- Kubernetes
- Zero Trust
- Observability
- Traffic Management
- Microservices
url: https://raw.githubusercontent.com/api-evangelist/ambient-mesh/refs/heads/main/apis.yml
use_cases:
- description: Enforce mutual TLS and zero-trust policies across microservices without modifying application code or injecting sidecar proxies.
  name: Microservices Security
- description: Implement advanced traffic routing, A/B testing, canary deployments, and traffic mirroring across Kubernetes workloads.
  name: Traffic Management
- description: Migrate existing Istio sidecar-based deployments to ambient mode with zero downtime using the free migration tooling.
  name: Istio Migration
- description: Gain full visibility into service-to-service communication with metrics, tracing, and traffic visualization via Kiali and Prometheus.
  name: Kubernetes Observability
- description: Extend ambient mesh policies and security across multiple Kubernetes clusters for hybrid and multi-cloud architectures.
  name: Multi-Cluster Networking
---
