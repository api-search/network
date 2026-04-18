---
api_count: 11
apis:
- description: The iControl REST API provides programmatic access to manage and configure F5 BIG-IP devices. Enables automation of network, security, and application delivery services.
  name: F5 BIG-IP iControl REST API
  slug: ''
- description: API for F5 Distributed Cloud Services providing multi-cloud networking, application security, and edge computing capabilities.
  name: F5 Distributed Cloud API
  slug: ''
- description: REST API for managing NGINX instances, monitoring performance, and configuring application delivery through NGINX Management Suite.
  name: F5 NGINX Management Suite API
  slug: ''
- description: API for managing F5's application security services including WAF policies, bot defense, and API protection.
  name: F5 Essential App Protect API
  slug: ''
- description: REST API for BIG-IQ Centralized Management providing programmatic control over BIG-IP device management, licensing, monitoring, and analytics across your F5 infrastructure.
  name: F5 BIG-IQ Centralized Management API
  slug: ''
- description: Declarative API for automating layer 4-7 application services on BIG-IP using JSON declarations. AS3 enables infrastructure-as-code for application delivery configuration.
  name: F5 BIG-IP Application Services 3 Extension API
  slug: ''
- description: Declarative API for automating layer 1-3 BIG-IP onboarding and initial device configuration using JSON declarations, making BIG-IP available on the network and ready for application services.
  name: F5 Declarative Onboarding API
  slug: ''
- description: Declarative API for aggregating, normalizing, and forwarding BIG-IP statistics and events to third-party analytics consumers including Splunk, Azure Log Analytics, AWS CloudWatch, and more.
  name: F5 Telemetry Streaming API
  slug: ''
- description: REST API for NGINX Plus providing real-time live activity monitoring, dynamic upstream configuration, key-value store management, and server health statistics without requiring configuration reloads.
  name: F5 NGINX Plus API
  slug: ''
- description: API for managing and monitoring NGINX instances across environments from a single console, including configuration management, performance metrics, security vulnerability tracking, and SSL certificate
  name: F5 NGINX One Console API
  slug: ''
- description: Kubernetes Ingress Controller implementation for NGINX and NGINX Plus providing load balancing, SSL/TLS termination, content-based routing, and advanced traffic management for containerized applicatio
  name: F5 NGINX Ingress Controller API
  slug: ''
capabilities:
- description: Unified workflow for managing application delivery infrastructure including virtual servers, server pools, backend nodes, and traffic profiles on F5 BIG-IP. Used by network administrators and DevOps e
  name: F5 Application Delivery
  slug: application-delivery
common:
- title: ''
  type: Documentation
  url: https://docs.nginx.com/
- title: ''
  type: DeveloperPortal
  url: https://clouddocs.f5.com/
- title: ''
  type: Blog
  url: https://www.f5.com/company/blog
- title: ''
  type: GitHubOrganization
  url: https://github.com/F5Networks
- title: F5 DevCentral
  type: GitHubOrganization
  url: https://github.com/f5devcentral/
- title: ''
  type: Support
  url: https://support.f5.com/
- title: ''
  type: StatusPage
  url: https://www.f5cloudstatus.com/
- title: ''
  type: TermsOfService
  url: https://www.f5.com/company/policies/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://www.f5.com/company/policies/privacy-notice
- title: ''
  type: SignUp
  url: https://account.f5.com/myf5
- title: ''
  type: Login
  url: https://identity.account.f5.com/
- title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/f5
- title: ''
  type: X
  url: https://twitter.com/f5networks
- title: ''
  type: YouTube
  url: https://www.f5.com/resources/videos
created: '2024'
description: F5 Networks is a leader in application delivery networking technology that specializes in application availability, acceleration, and security solutions.
features:
- description: Connect and secure applications across any cloud, data center, or edge environment with consistent policy and visibility.
  name: Multi-Cloud Networking
- description: Advanced load balancing, traffic management, and application acceleration for high availability and performance.
  name: Application Delivery Controller
- description: Comprehensive protection against OWASP Top 10 threats, bot attacks, and API vulnerabilities.
  name: Web Application Firewall
- description: Declarative APIs (AS3, DO, TS) for automating BIG-IP configuration and application delivery.
  name: Infrastructure as Code
- description: High-performance reverse proxy, load balancing, and web serving for modern applications.
  name: NGINX Reverse Proxy
- description: Secure and manage API traffic with rate limiting, authentication, and traffic shaping.
  name: API Gateway
- description: Volumetric and application-layer DDoS mitigation with always-on or on-demand protection.
  name: DDoS Protection
- description: Centralized SSL/TLS certificate management and encryption offloading for improved performance.
  name: SSL/TLS Offloading
image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
integrations:
- description: Deploy BIG-IP and Distributed Cloud services natively on AWS with CloudFormation templates and marketplace offerings.
  name: AWS
- description: Integrate F5 solutions with Azure services including AKS, App Gateway, and Azure AD for cloud-native security.
  name: Azure
- description: Deploy F5 solutions on GCP with support for GKE, Cloud Load Balancing, and Anthos.
  name: Google Cloud
- description: Native Kubernetes integration through NGINX Ingress Controller, Container Ingress Services, and Helm charts.
  name: Kubernetes
- description: Infrastructure as Code support with official Terraform providers for BIG-IP and Distributed Cloud.
  name: Terraform
- description: Ansible modules and roles for automating BIG-IP configuration, deployment, and orchestration.
  name: Ansible
- description: Forward telemetry data to Splunk for centralized logging, analytics, and security monitoring.
  name: Splunk
- description: ITSM integration for automated incident management and change control of F5 infrastructure.
  name: ServiceNow
jsonld:
- class_count: 0
  name: Bigip Icontrol Rest Context
  property_count: 0
  slug: bigip-icontrol-rest-context
- class_count: 0
  name: F5 Networks Context
  property_count: 6
  slug: f5-networks-context
layout: provider
modified: '2026-04-18'
name: F5 Networks
rules:
- name: F5 Networks API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: f5-networks-spectral-rules
skills: []
slug: f5-networks
solutions: []
tags:
- API Gateway
- Application Delivery
- Automation
- Edge Computing
- Kubernetes
- Load Balancing
- Multi-Cloud
- NGINX
- Security
- WAF
url: https://www.f5.com/apis
use_cases:
- description: Distribute application traffic across servers for high availability, performance, and fault tolerance.
  name: Application Load Balancing
- description: Implement zero trust architecture with identity-aware proxy, micro-segmentation, and continuous verification.
  name: Zero Trust Security
- description: Manage ingress traffic for containerized applications with NGINX Ingress Controller in Kubernetes clusters.
  name: Kubernetes Ingress
- description: Deliver applications consistently across AWS, Azure, GCP, and on-premises with unified policy management.
  name: Multi-Cloud Application Delivery
- description: Protect APIs from abuse, injection attacks, and unauthorized access with granular security policies.
  name: API Security
- description: Automate network and security infrastructure provisioning using declarative APIs and CI/CD pipelines.
  name: DevOps Automation
---
