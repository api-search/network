---
api_count: 4
apis:
- description: RESTful API for the Ansible Automation Controller (formerly Ansible Tower) providing programmatic access to job templates, workflows, inventories, credentials, projects, and job execution. Supports CR
  name: Ansible Automation Controller API
  slug: controller-api
- description: REST API for Ansible Automation Hub providing access to certified and validated Ansible content collections, roles, and execution environments. Supports searching, downloading, and publishing automati
  name: Ansible Automation Hub API
  slug: hub-api
- description: API for Event-Driven Ansible (EDA) Controller enabling management of rulebooks, activations, and event sources for automated response to infrastructure and application events.
  name: Ansible Event-Driven Automation API
  slug: event-driven-api
- description: REST API for Ansible Galaxy, the community hub for sharing Ansible roles and collections. Supports searching, downloading, and rating community automation content.
  name: Ansible Galaxy API
  slug: galaxy-api
common:
- title: ''
  type: Portal
  url: https://docs.ansible.com/
- title: ''
  type: Documentation
  url: https://docs.ansible.com/automation-controller/
- title: ''
  type: GettingStarted
  url: https://docs.ansible.com/ansible/latest/getting_started/
- title: ''
  type: Blog
  url: https://www.ansible.com/blog
- title: ''
  type: GitHubOrganization
  url: https://github.com/ansible
- title: ''
  type: Support
  url: https://access.redhat.com/products/ansible-automation-platform
- title: ''
  type: TermsOfService
  url: https://www.redhat.com/en/about/agreements
- title: ''
  type: PrivacyPolicy
  url: https://www.redhat.com/en/about/privacy-policy
- title: ''
  type: Training
  url: https://www.ansible.com/products/training-certification
- title: ''
  type: YouTube
  url: https://www.youtube.com/ansibleautomation
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/ansible
- title: ''
  type: Pricing
  url: https://www.redhat.com/en/technologies/management/ansible/pricing
created: '2024-01-01'
description: Ansible Automation Platform (formerly Ansible Tower) provides a REST API for managing automation workflows, job templates, inventories, credentials, and projects. The API enables programmatic access to the automation controller for launching jobs, managing infrastructure inventory, and orchestrating complex multi-tier deployments across hybrid cloud environments.
features:
- description: Define and manage reusable automation job templates with variables, credentials, and inventory assignments.
  name: Job Template Management
- description: Build multi-step automation workflows with conditional logic, error handling, and approval gates.
  name: Workflow Orchestration
- description: Manage dynamic and static inventories of infrastructure hosts with grouping and variable assignment.
  name: Inventory Management
- description: Fine-grained access control for automation resources with teams, users, and permission assignments.
  name: Role-Based Access Control
- description: Automatically respond to infrastructure events with rulebook-driven automation triggers.
  name: Event-Driven Automation
- description: Discover, install, and manage certified Ansible content collections from Automation Hub.
  name: Content Collections
image: /assets/icons/ansible-automation-platform.png
integrations:
- description: Integration with Red Hat Satellite for content management and patch automation.
  name: Red Hat Satellite
- description: ITSM integration for change management approval workflows and incident remediation.
  name: ServiceNow
- description: Cloud automation modules for AWS services including EC2, S3, RDS, and CloudFormation.
  name: AWS
- description: Cloud automation modules for Azure services including VMs, AKS, and Azure Resource Manager.
  name: Azure
- description: Infrastructure as code integration for provisioning with Terraform and configuring with Ansible.
  name: Terraform
- description: CI/CD pipeline integration for automated deployment workflows triggered by Jenkins.
  name: Jenkins
jsonld:
- class_count: 3
  name: Ansible Automation Platform Context
  property_count: 9
  slug: ansible-automation-platform-context
layout: provider
modified: '2026-04-18'
name: Ansible Automation Platform
rules:
- name: Ansible Automation Platform API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: ansible-automation-platform-spectral-rules
skills: []
slug: ansible-automation-platform
solutions: []
tags:
- Automation
- Configuration Management
- DevOps
- Infrastructure as Code
- Orchestration
url: https://raw.githubusercontent.com/api-evangelist/ansible-automation-platform/refs/heads/main/apis.yml
use_cases:
- description: Automate provisioning of servers, networks, and cloud resources across hybrid environments.
  name: Infrastructure Provisioning
- description: Maintain consistent configuration across thousands of servers with idempotent automation.
  name: Configuration Management
- description: Automate application deployment pipelines with rolling updates and rollback capabilities.
  name: Application Deployment
- description: Enforce security policies and compliance standards through automated remediation workflows.
  name: Security Compliance
- description: Automate network device configuration and management across multi-vendor environments.
  name: Network Automation
---
