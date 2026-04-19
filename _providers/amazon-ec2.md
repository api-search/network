---
api_count: 1
apis:
- description: Core API for managing Amazon EC2 instances, AMIs, key pairs, security groups, Elastic IPs, launch templates, spot instances, capacity reservations, and other compute resources.
  name: Amazon EC2 API
  slug: ''
capabilities:
- description: Unified capability for managing EC2 instances, AMIs, security groups, and networking for cloud infrastructure engineers.
  name: Amazon EC2 Cloud Compute Management
  slug: ec2-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/ec2/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/ec2/
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
  url: https://aws.amazon.com/blogs/compute/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/ec2/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
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
  url: https://stackoverflow.com/questions/tagged/amazon-ec2
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Security
  url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-ec2-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-ec2-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/ec2-management.yaml
created: '2024-01-15'
description: Amazon Elastic Compute Cloud (EC2) provides resizable compute capacity in the cloud, allowing you to launch virtual server instances, manage networking, and configure storage with complete control over your computing resources.
features:
- description: Over 750 instance types optimized for compute, memory, storage, GPU, and inferencing workloads.
  name: Diverse Instance Types
- description: Pre-configured OS images for Windows, Linux, and macOS with custom and marketplace options.
  name: Amazon Machine Images
- description: Static IPv4 addresses that can be quickly remapped to different instances for fault tolerance.
  name: Elastic IPs
- description: Virtual firewalls to control inbound and outbound traffic to EC2 instances.
  name: Security Groups
- description: Access spare EC2 capacity at up to 90% discount over On-Demand prices for flexible workloads.
  name: Spot Instances
- description: Control instance placement for low-latency cluster networking or high-availability distribution.
  name: Placement Groups
- description: Version-controlled configurations for launching EC2 instances with consistent settings.
  name: Launch Templates
- description: Next-generation virtualization infrastructure delivering near bare-metal performance and security.
  name: Nitro System
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Launch EC2 instances in logically isolated virtual networks with full networking control.
  name: Amazon VPC
- description: Distribute incoming traffic across multiple EC2 instances for high availability.
  name: Elastic Load Balancing
- description: Connect EC2 instances to managed relational database services within the same VPC.
  name: Amazon RDS
- description: Automatically scale EC2 fleets based on demand metrics and scheduling policies.
  name: AWS Auto Scaling
- description: Manage, patch, and operate EC2 instances at scale without SSH access.
  name: AWS Systems Manager
jsonld:
- class_count: 6
  name: Amazon Ec2 Context
  property_count: 35
  slug: amazon-ec2-context
layout: provider
modified: '2026-04-19'
name: Amazon EC2
rules:
- name: Amazon EC2 API Rules
  rule_count: 28
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 13
  slug: amazon-ec2-spectral-rules
skills: []
slug: amazon-ec2
solutions: []
tags:
- AWS
- Cloud Computing
- Compute
- IaaS
- Infrastructure
- Virtual Machines
url: https://aws.amazon.com/ec2/
use_cases:
- description: Deploy scalable web applications and APIs with full control over the compute environment.
  name: Web Application Hosting
- description: GPU-accelerated instances for deep learning model training and inference workloads.
  name: Machine Learning Training
- description: Cluster networking instances for computational fluid dynamics, genomics, and financial modeling.
  name: High-Performance Computing
- description: Certified instances for SAP HANA, SAP S/4HANA, and other enterprise database applications.
  name: SAP and Enterprise Workloads
- description: Flexible on-demand compute for CI/CD pipelines, dev environments, and test automation.
  name: Development and Testing
---
