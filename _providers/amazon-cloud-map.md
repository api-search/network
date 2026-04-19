---
api_count: 1
apis:
- description: API for managing service discovery namespaces, services, and instances with health checking. Enables microservices to dynamically discover dependencies.
  name: Amazon Cloud Map API
  slug: ''
capabilities:
- description: Workflow for dynamically discovering and registering microservices using AWS Cloud Map, enabling DevOps and platform engineers to maintain service registries with health-based routing.
  name: Amazon Cloud Map Service Discovery
  slug: service-discovery
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/cloud-map/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cloud-map/
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
  url: https://console.aws.amazon.com/cloudmap/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-cloud-map
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-cloud-map-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloud-map-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/service-discovery.yaml
created: '2026-03-16'
description: Amazon Cloud Map is a cloud resource discovery service that maintains an updated registry of application resources and their locations. Define custom names for application resources and use Cloud Map to dynamically discover service dependencies with integrated health checking and automatic updates.
features:
- description: Maintain an up-to-date registry of application resources with custom naming.
  name: Service Registry
- description: Continuously monitor health of every IP-based component and route only to healthy endpoints.
  name: Health Monitoring
- description: Automatically update service registries as services scale up or down.
  name: Dynamic Discovery
- description: Define custom names for application resources rather than hardcoding IP addresses.
  name: Custom Names
- description: Maintain service registries across different deployment environments, regions, and application versions.
  name: Multi-Environment Support
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Automatically register ECS task IPs in Cloud Map as containers launch.
  name: Amazon ECS
- description: Integrate Kubernetes service discovery with Cloud Map for hybrid environments.
  name: Amazon EKS
- description: DNS-based service discovery backed by Route 53 private hosted zones.
  name: Amazon Route 53
- description: Use Cloud Map as the service registry for App Mesh virtual services.
  name: AWS App Mesh
- description: Control access to Cloud Map namespaces with IAM policies.
  name: AWS IAM
jsonld:
- class_count: 15
  name: Amazon Cloud Map Context
  property_count: 20
  slug: amazon-cloud-map-context
layout: provider
modified: '2026-04-19'
name: Amazon Cloud Map
rules:
- name: Amazon Cloud Map API Rules
  rule_count: 20
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 6
  slug: amazon-cloud-map-spectral-rules
skills: []
slug: amazon-cloud-map
solutions: []
tags:
- AWS
- Cloud Map
- Service Discovery
- Microservices
- DNS
url: https://raw.githubusercontent.com/api-evangelist/amazon-cloud-map/refs/heads/main/apis.yml
use_cases:
- description: Enable services to locate dependencies in dynamic container environments with ECS and EKS.
  name: Microservice Discovery
- description: Ensure traffic routes only to verified healthy service endpoints.
  name: Health-Based Routing
- description: Automatically register and deregister services during CI/CD pipeline deployments.
  name: CI/CD Integration
- description: Discover services across multiple AWS regions with a unified namespace.
  name: Multi-Region Service Mesh
---
