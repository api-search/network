---
api_count: 5
apis:
- description: The Spot Administration API provides endpoints for managing organizations, accounts, users, access policies, cloud credentials, subscriptions, and event notifications within the Spot by Flexera platfo
  name: Spot Administration API
  slug: administration-api
- description: The Spot Elastigroup API enables programmatic management of Elastigroup compute groups across AWS, Azure, and GCP. Elastigroup simplifies and automates cloud infrastructure for scale-out applications,
  name: Spot Elastigroup API
  slug: elastigroup-api
- description: The Spot Ocean API provides programmatic management of Ocean Kubernetes clusters across AWS EKS, Azure AKS, GCP GKE, and Amazon ECS. Ocean is a serverless Kubernetes infrastructure engine that automat
  name: Spot Ocean API
  slug: ocean-api
- description: The Spot Eco API provides programmatic access to cloud commitment management and optimization across AWS, Azure, and GCP. Eco automates the purchase, management, and optimization of reserved instances
  name: Spot Eco API
  slug: eco-api
- description: The Spot Billing Engine API provides programmatic access to cloud billing management, cost allocation, and invoicing capabilities. Billing Engine streamlines multi-cloud invoicing with intelligent cos
  name: Spot Billing Engine API
  slug: billing-engine-api
capabilities:
- description: Unified workflow for managing cloud compute optimization across Elastigroup and Ocean, combining instance management, autoscaling, and Kubernetes infrastructure automation. Used by DevOps engineers an
  name: Spot Compute Optimization
  slug: compute-optimization
- description: Unified workflow for cloud financial operations combining commitment management (Eco), billing analytics (Billing Engine), and cost optimization. Used by FinOps teams, cloud finance analysts, and plat
  name: Spot FinOps
  slug: finops
common:
- title: ''
  type: GitHubOrganization
  url: https://github.com/spotinst
- title: ''
  type: Documentation
  url: https://docs.spot.io/
- title: ''
  type: APIReference
  url: https://docs.spot.io/api/
- title: ''
  type: OpenAPI
  url: https://github.com/spotinst/openapi
- title: ''
  type: Authentication
  url: https://docs.spot.io/administration/api/create-api-token
- title: ''
  type: Blog
  url: https://spot.io/blog/
- title: ''
  type: TermsOfService
  url: https://spot.io/terms-of-use/
created: '2026-01-02'
description: Spot by Flexera provides cloud infrastructure automation and optimization solutions. The platform includes Elastigroup for compute workload management across spot, reserved, and on-demand instances, Ocean for Kubernetes and container infrastructure automation, and Eco for cloud commitment management. The Spot API enables programmatic control over all platform capabilities including administration, compute groups, Kubernetes clusters, and cost optimization.
features:
- description: Automated management of compute workloads across spot, reserved, and on-demand instances for optimal cost and availability.
  name: Elastigroup Compute Management
- description: Serverless container infrastructure that automatically right-sizes and scales Kubernetes node pools using the lowest-cost compute.
  name: Ocean Kubernetes Automation
- description: Automated purchase and management of reserved instances, savings plans, and committed use discounts across clouds.
  name: Eco Commitment Optimization
- description: Multi-cloud billing management with cost allocation, chargeback, showback, and invoicing analytics.
  name: Billing Engine
- description: Unified management across AWS, Azure, and GCP with consistent APIs and optimization strategies.
  name: Multi-Cloud Support
- description: Predictive and reactive autoscaling that analyzes workload patterns to optimize resource provisioning.
  name: Intelligent Autoscaling
- description: Support for stateful applications with persistent storage, ENI, and IP preservation during instance replacements.
  name: Stateful Workload Management
image: /assets/icons/spot.png
integrations:
- description: Deep integration with EC2, EKS, ECS, EMR, Auto Scaling Groups, and Savings Plans for AWS workload optimization.
  name: AWS
- description: Integration with Azure VMs, AKS, Virtual Machine Scale Sets, and Azure Reserved VM Instances.
  name: Azure
- description: Support for GCP Compute Engine, GKE, and Committed Use Discounts for Google Cloud optimization.
  name: Google Cloud
- description: Native integration with EKS, AKS, GKE, and self-managed Kubernetes clusters through the Ocean controller.
  name: Kubernetes
- description: Official Terraform provider for managing Elastigroup, Ocean, and Eco resources as infrastructure as code.
  name: Terraform
- description: Jenkins plugin for scaling CI/CD build agents dynamically using Elastigroup spot instances.
  name: Jenkins
- description: Ansible modules for automating Spot resource provisioning and configuration management.
  name: Ansible
jsonld:
- class_count: 0
  name: Spot Administration Context
  property_count: 0
  slug: spot-administration-context
- class_count: 0
  name: Spot Billing Engine Context
  property_count: 0
  slug: spot-billing-engine-context
- class_count: 0
  name: Spot Context
  property_count: 9
  slug: spot-context
- class_count: 0
  name: Spot Eco Context
  property_count: 0
  slug: spot-eco-context
- class_count: 0
  name: Spot Elastigroup Context
  property_count: 0
  slug: spot-elastigroup-context
- class_count: 0
  name: Spot Ocean Context
  property_count: 0
  slug: spot-ocean-context
layout: provider
modified: '2026-04-18'
name: Spot
rules:
- name: Spot API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: spot-spectral-rules
skills: []
slug: spot
solutions: []
tags:
- Autoscaling
- Cloud Infrastructure
- Containers
- Cost Optimization
- FinOps
- Kubernetes
- Spot Instances
url: https://raw.githubusercontent.com/api-evangelist/spot/refs/heads/main/apis.yml
use_cases:
- description: Reduce cloud compute costs by up to 90% by leveraging spot instances with automated fallback to on-demand capacity.
  name: Cloud Cost Optimization
- description: Optimize Kubernetes infrastructure costs with bin-packing, right-sizing, and intelligent node pool management.
  name: Kubernetes Cost Management
- description: Centralized cloud cost visibility with chargeback, showback, and commitment utilization reporting across teams.
  name: FinOps Reporting
- description: Run Apache Spark and EMR workloads on spot instances with automatic scaling and cost optimization.
  name: Big Data Cost Reduction
- description: Automate the lifecycle of cloud commitments including purchasing, exchanging, and selling unused reservations.
  name: Reserved Instance Management
- description: Unified access control, audit logging, and policy management across AWS, Azure, and GCP accounts.
  name: Multi-Cloud Governance
---
