---
api_count: 0
apis: []
capabilities:
- description: Unified capability for managing EKS clusters, node groups, Fargate profiles, and add-ons for platform engineers.
  name: Amazon EKS Kubernetes Cluster Management
  slug: eks-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/eks/
- title: ''
  type: Docs
  url: https://docs.aws.amazon.com/
- title: ''
  type: Terms
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: Privacy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/containers/
- title: ''
  type: GitHub
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/eks/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-eks
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Security
  url: https://aws.amazon.com/security/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-eks-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-eks-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/eks-management.yaml
created: ''
description: Amazon Elastic Kubernetes Service (Amazon EKS) is a managed Kubernetes service that makes it easy to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes. Amazon EKS runs upstream Kubernetes and is certified Kubernetes conformant, so you can use existing tools and plugins from partners and the Kubernetes community.
features:
- description: AWS manages the Kubernetes control plane across multiple Availability Zones with automatic upgrades.
  name: Managed Control Plane
- description: Automates cluster infrastructure management for compute, storage, and networking with machine learning optimization.
  name: EKS Auto Mode
- description: Connect on-premises and edge infrastructure to EKS clusters for unified management.
  name: EKS Hybrid Nodes
- description: Run Kubernetes pods on serverless compute without managing EC2 node groups.
  name: Fargate Integration
- description: Automate provisioning and lifecycle management of EC2 nodes for Kubernetes clusters.
  name: Managed Node Groups
- description: Deploy and manage Kubernetes clusters on customer-managed infrastructure including on-premises.
  name: EKS Anywhere
- description: Manage operational software add-ons like VPC CNI, CoreDNS, and kube-proxy through EKS.
  name: Add-Ons Management
image: ''
integrations:
- description: Pull container images from ECR for Kubernetes workloads with native IAM authentication.
  name: Amazon ECR
- description: Manage Application and Network Load Balancers for Kubernetes Ingress resources.
  name: AWS Load Balancer Controller
- description: Mount EFS file systems as Kubernetes persistent volumes for stateful applications.
  name: Amazon EFS CSI Driver
- description: Grant Kubernetes pods fine-grained IAM permissions using OIDC-based service account annotations.
  name: AWS IAM Roles for Service Accounts
- description: Collect and analyze metrics, logs, and traces from EKS clusters and workloads.
  name: Amazon CloudWatch Container Insights
jsonld:
- class_count: 30
  name: Amazon Eks Context
  property_count: 61
  slug: amazon-eks-context
layout: provider
modified: '2026-04-19'
name: Amazon EKS
rules:
- name: Amazon EKS API Rules
  rule_count: 28
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 13
  slug: amazon-eks-spectral-rules
skills: []
slug: amazon-eks
solutions: []
tags:
- AWS
- Container Orchestration
- Containers
- EKS
- Kubernetes
url: https://aws.amazon.com/eks/
use_cases:
- description: Scale production-grade AI deployments with GPU nodes for distributed training and inference.
  name: Generative AI Applications
- description: Deploy and manage containerized microservices with Kubernetes-native service discovery and scaling.
  name: Microservices Architecture
- description: Standardized Kubernetes environments combining open source with AWS managed services.
  name: Internal Developer Platforms
- description: Unified Kubernetes management across AWS cloud and on-premises infrastructure.
  name: Hybrid Cloud Applications
- description: Scalable batch processing and streaming data workloads using Spark, Flink, or Ray.
  name: Data Processing Platforms
---
