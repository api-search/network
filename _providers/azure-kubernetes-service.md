---
api_count: 8
apis:
- description: REST API for managing Azure Kubernetes Service clusters.
  name: Azure Kubernetes Service REST API
  slug: ''
- description: REST API for creating, updating, deleting, and managing AKS managed clusters including cluster configuration, upgrades, credentials, and run commands.
  name: Azure Kubernetes Service Managed Clusters API
  slug: ''
- description: REST API for creating, updating, deleting, and managing agent pools (node pools) within AKS managed clusters, including scaling and configuration.
  name: Azure Kubernetes Service Agent Pools API
  slug: ''
- description: REST API for managing planned maintenance configurations, used to configure when updates can be deployed to an AKS managed cluster.
  name: Azure Kubernetes Service Maintenance Configurations API
  slug: ''
- description: REST API for creating, updating, deleting, and managing node pool snapshots in AKS, including listing snapshots by resource group.
  name: Azure Kubernetes Service Snapshots API
  slug: ''
- description: REST API for managing private endpoint connections for AKS clusters, enabling secure private network access to the cluster API server.
  name: Azure Kubernetes Service Private Endpoint Connections API
  slug: ''
- description: REST API for managing trusted access role bindings that give Azure services secure access to AKS API server using system-assigned managed identities.
  name: Azure Kubernetes Service Trusted Access Role Bindings API
  slug: ''
- description: Kubernetes API accessible via kubectl for cluster operations.
  name: Azure Kubernetes Service kubectl API
  slug: ''
capabilities:
- description: Workflow for managing AKS clusters and agent pools including lifecycle operations, upgrades, scaling, and credentials. Used by DevOps engineers and platform administrators.
  name: Azure Kubernetes Service Cluster Management
  slug: cluster-management
common:
- title: ''
  type: Portal
  url: https://portal.azure.com/
- title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-portal
- title: ''
  type: CLI
  url: https://learn.microsoft.com/en-us/cli/azure/aks
- title: ''
  type: StatusPage
  url: https://status.azure.com/
- title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/options/
- title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/topics/kubernetes/
- title: ''
  type: GitHubRepository
  url: https://github.com/Azure/AKS
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-aks
- title: ''
  type: Security
  url: https://learn.microsoft.com/en-us/azure/aks/concepts-security
- title: ''
  type: Compliance
  url: https://learn.microsoft.com/en-us/azure/aks/concepts-security#azure-policy
- title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/aks/
- title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/kubernetes-service/
- title: ''
  type: SignUp
  url: https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account
- title: ''
  type: Login
  url: https://portal.azure.com/
- title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- title: ''
  type: ChangeLog
  url: https://github.com/Azure/AKS/blob/master/CHANGELOG.md
- title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/azure/aks/release-tracker
- title: ''
  type: FAQ
  url: https://learn.microsoft.com/en-us/azure/aks/faq
- title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/modules/intro-to-azure-kubernetes-service/
- title: ''
  type: YouTube
  url: https://www.youtube.com/c/MicrosoftAzure
- title: ''
  type: SpectralRules
  url: rules/azure-kubernetes-service-spectral-rules.yml
- title: AKS REST API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/aks-rest.yaml
- title: Cluster Management Workflow
  type: NaftikoCapability
  url: capabilities/cluster-management.yaml
created: '2024-01-15'
description: Azure Kubernetes Service (AKS) simplifies deploying a managed Kubernetes cluster in Azure by offloading the operational overhead to Azure. As a hosted Kubernetes service, Azure handles critical tasks, like health monitoring and maintenance.
features:
- description: Create, update, delete, start, and stop AKS managed clusters with full lifecycle management.
  name: Managed Cluster Lifecycle
- description: Create and manage node pools with configurable VM sizes, scaling, and upgrade policies.
  name: Agent Pool Management
- description: Upgrade Kubernetes versions and node images with controlled rollout and upgrade profiles.
  name: Cluster Upgrades
- description: Retrieve admin, user, and monitoring credentials for cluster access and authentication.
  name: Credential Management
- description: Deploy private AKS clusters with private endpoint connections for secure API server access.
  name: Private Clusters
- description: Configure planned maintenance windows to control when updates are applied to clusters.
  name: Maintenance Windows
- description: Create and manage snapshots of node pools for backup and recovery scenarios.
  name: Node Pool Snapshots
- description: Grant Azure services secure access to AKS API server using managed identities and role bindings.
  name: Trusted Access
- description: Execute commands on cluster nodes remotely through the AKS API without direct SSH access.
  name: Run Commands
- description: Automatically scale node pools based on workload demands with configurable auto-scaler profiles.
  name: Auto-Scaling
image: https://azure.microsoft.com/images/aks-icon.png
integrations:
- description: Pull container images from Azure Container Registry with managed identity authentication.
  name: Azure Container Registry
- description: Monitor cluster health, performance, and logs with Azure Monitor and Container Insights.
  name: Azure Monitor
- description: Enforce organizational standards and compliance with Azure Policy for Kubernetes.
  name: Azure Policy
- description: Integrate with Azure AD for cluster authentication and role-based access control.
  name: Azure Active Directory
- description: Automate deployments to AKS using Azure Pipelines with native Kubernetes tasks.
  name: Azure DevOps
jsonld:
- class_count: 0
  name: Azure Kubernetes Service Context
  property_count: 0
  slug: azure-kubernetes-service-context
layout: provider
modified: '2026-04-18'
name: Azure Kubernetes Service
rules:
- name: Azure Kubernetes Service API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: azure-kubernetes-service-spectral-rules
skills: []
slug: azure-kubernetes-service
solutions: []
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
url: https://azure.microsoft.com/en-us/services/kubernetes-service/
use_cases:
- description: Deploy and manage microservices architectures with container orchestration and service mesh capabilities.
  name: Microservices Deployment
- description: Integrate AKS with Azure DevOps and GitHub Actions for automated build, test, and deployment workflows.
  name: CI/CD Pipelines
- description: Run Kubernetes workloads across on-premises and Azure environments with Azure Arc integration.
  name: Hybrid Cloud
- description: Deploy and scale ML model serving infrastructure using AKS with GPU-enabled node pools.
  name: Machine Learning
- description: Deploy containerized workloads to edge locations using AKS Edge Essentials and Azure IoT.
  name: Edge Computing
---
