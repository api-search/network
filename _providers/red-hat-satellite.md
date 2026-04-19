---
api_count: 5
apis:
- description: The main REST API for Red Hat Satellite 6.x, providing programmatic access to all Satellite functions including host management, content management, provisioning, and configuration.
  name: Red Hat Satellite REST API
  slug: ''
- description: Command-line interface tool for Red Hat Satellite that provides scriptable access to Satellite functions including host management, content views, and provisioning.
  name: Red Hat Satellite Hammer CLI
  slug: ''
- description: Core Foreman API integrated into Red Hat Satellite for host lifecycle management, provisioning, and configuration management. This is the upstream project API that powers Satellite's core functionalit
  name: Red Hat Satellite Foreman API
  slug: ''
- description: Content management API for Red Hat Satellite handling repositories, content views, lifecycle environments, subscriptions, and errata. Katello is the upstream plugin that provides Satellite's content a
  name: Red Hat Satellite Katello API
  slug: ''
- description: The redhat.satellite Ansible collection provides modules, roles, and plugins for automating Red Hat Satellite configuration and management through the Satellite API. Based on the theforeman.foreman co
  name: Red Hat Satellite Ansible Collection
  slug: ''
capabilities:
- description: Unified workflow for managing the complete lifecycle of physical, virtual, and cloud hosts including provisioning, content management, patching, and subscription management. Used by system administrat
  name: Red Hat Satellite Systems Lifecycle Management
  slug: systems-lifecycle-management
common:
- title: ''
  type: Portal
  url: https://access.redhat.com/
- title: ''
  type: Documentation
  url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16
- title: ''
  type: Support
  url: https://access.redhat.com/support/
- title: ''
  type: StatusPage
  url: https://status.redhat.com/
- title: ''
  type: Blog
  url: https://www.redhat.com/en/blog/channel/red-hat-satellite
- title: ''
  type: GitHubOrganization
  url: https://github.com/theforeman
- title: ''
  type: KnowledgeCenter
  url: https://access.redhat.com/solutions/
- title: Community
  type: Support
  url: https://access.redhat.com/community/
- title: Foreman Community
  type: Support
  url: https://community.theforeman.org/
- title: ''
  type: ReleaseNotes
  url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.18/html-single/release_notes/index
- title: Product Lifecycle
  type: Documentation
  url: https://access.redhat.com/support/policy/updates/satellite
- title: Release Dates
  type: Documentation
  url: https://access.redhat.com/articles/1365633
- title: Provisioning Guide
  type: Documentation
  url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html/provisioning_hosts/index
- title: Managing Hosts Guide
  type: Documentation
  url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html-single/managing_content/index
- title: ''
  type: APIReference
  url: https://apidocs.theforeman.org/
- title: Hammer CLI
  type: CLI
  url: https://github.com/theforeman/hammer-cli-foreman
- title: Ansible Modules
  type: GitHubRepository
  url: https://github.com/theforeman/foreman-ansible-modules
- title: ''
  type: SpectralRules
  url: rules/red-hat-satellite-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/red-hat-satellite-vocabulary.yaml
- title: Satellite API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/satellite-api.yaml
- title: Systems Lifecycle Management Workflow
  type: NaftikoCapability
  url: capabilities/systems-lifecycle-management.yaml
created: '2024-01-01'
description: Red Hat Satellite is a systems management product that helps deploy, configure, and maintain systems across physical, virtual, and cloud environments.
features:
- description: Manage physical, virtual, and cloud hosts across the entire lifecycle from provisioning to decommissioning.
  name: Host Management
- description: Curate and distribute RPM packages, errata, and container images through content views and lifecycle environments.
  name: Content Management
- description: Apply security patches and errata across managed systems with controlled rollouts through lifecycle stages.
  name: Patch Management
- description: Track and manage Red Hat subscriptions and entitlements across organizations and hosts.
  name: Subscription Management
- description: Automate bare-metal and virtual machine provisioning with kickstart templates, PXE boot, and compute resources.
  name: Provisioning
- description: Enforce desired-state configuration using Puppet classes and Ansible roles across managed hosts.
  name: Configuration Management
- description: Organize hosts, content, and subscriptions into isolated organizations and locations.
  name: Multi-Tenancy
image: https://www.redhat.com/profiles/rh/themes/redhatdotcom/img/logo.png
integrations:
- description: Automate Satellite operations and host configuration using the redhat.satellite Ansible collection.
  name: Ansible
- description: Proactive risk analysis and remediation recommendations for managed hosts.
  name: Red Hat Insights
- description: Apply and enforce configuration management policies using Puppet modules and classes.
  name: Puppet
- description: Security compliance scanning and reporting using SCAP content and policies.
  name: OpenSCAP
- description: Provision and manage virtual machines on VMware infrastructure as compute resources.
  name: VMware vSphere
- description: Provision and manage instances on OpenStack as compute resources.
  name: Red Hat OpenStack
- description: Provision and manage cloud instances on AWS as compute resources.
  name: Amazon EC2
- description: Provision and manage cloud instances on Google Cloud as compute resources.
  name: Google GCE
jsonld:
- class_count: 0
  name: Red Hat Satellite Context
  property_count: 0
  slug: red-hat-satellite-context
layout: provider
modified: '2026-04-18'
name: Red Hat Satellite
rules:
- name: Red Hat Satellite API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: red-hat-satellite-spectral-rules
skills: []
slug: red-hat-satellite
solutions: []
tags:
- Configuration Management
- Lifecycle Management
- Patch Management
- Subscription Management
- Systems Management
url: https://raw.githubusercontent.com/api-evangelist/red-hat-satellite/refs/heads/main/apis.yml
use_cases:
- description: Provision new servers automatically using compute resources, host groups, and kickstart templates.
  name: Automated Server Provisioning
- description: Identify, test, and deploy security errata across thousands of hosts using content views and promotion workflows.
  name: Security Patching at Scale
- description: Manage hosts across on-premises data centers and cloud providers from a single console.
  name: Hybrid Cloud Management
- description: Generate compliance reports using OpenSCAP integration to verify hosts meet security baselines.
  name: Compliance Reporting
- description: Manage systems in disconnected environments using content synchronization and inter-satellite sync.
  name: Air-Gapped Environment Management
---
