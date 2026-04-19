---
api_count: 3
apis:
- description: The Acquia Cloud API is a powerful tool that allows developers to programmatically interact with Acquia's cloud hosting platform. This API enables users to automate tasks, manage infrastructure, and d
  name: Acquia Cloud API
  slug: acquia-cloud-api
- description: Acquia Cloud Site Factory API is a powerful tool that allows developers to manage, customize, and automate various aspects of their websites and digital experiences. With this API, users can programma
  name: Acquia Cloud Site Factory API
  slug: acquia-cloud-site-factory-api
- description: The Acquia Content Hub API is a powerful tool that allows users to easily distribute and share content across multiple websites and digital channels. By leveraging this API, content managers can autom
  name: Acquia Content Hub API
  slug: acquia-content-hub-api
capabilities:
- description: Unified workflow for managing Drupal applications on Acquia Cloud, including application discovery, environment management, organization administration, and account operations. Used by Drupal develope
  name: Acquia Drupal Application Management
  slug: drupal-application-management
common:
- title: ''
  type: Partners
  url: https://www.acquia.com/partners
- title: ''
  type: Blog
  url: https://www.acquia.com/blog
- title: ''
  type: Webinars
  url: https://www.acquia.com/events/online
- title: ''
  type: Certifications
  url: https://www.acquia.com/support/acquia-training-certification
- title: ''
  type: Portal
  url: https://dev.acquia.com/
- title: ''
  type: Tutorials
  url: https://dev.acquia.com/tutorial
- title: ''
  type: Support
  url: https://docs.acquia.com/service-offerings/support/support-users-guide#contacting-acquia-support
- title: ''
  type: StatusPage
  url: https://status.acquia.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/acquia
- title: Acquia CLI
  type: CLI
  url: https://github.com/acquia/cli
- title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/rules/acquia-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/capabilities/drupal-application-management.yaml
- title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/vocabulary/acquia-vocabulary.yaml
- title: ''
  type: TermsOfService
  url: https://www.acquia.com/about-us/legal
- title: ''
  type: SignUp
  url: https://accounts.acquia.com/register
created: '2025-02-17'
description: Acquia is a leading provider of digital experience management solutions for organizations looking to enhance their online presence. They offer a range of services, including cloud hosting, digital asset management, and content management, to help businesses create, manage, and optimize their websites and digital experiences.
features:
- description: Managed Drupal hosting on Acquia Cloud with auto-scaling, CDN, and DDoS protection.
  name: Cloud Hosting
- description: Programmatic management of Drupal applications, environments, and deployments via Cloud API.
  name: Application Management
- description: Acquia Cloud Site Factory for managing hundreds of Drupal sites from a centralized platform.
  name: Multi-Site Factory
- description: Acquia Content Hub for distributing and synchronizing Drupal content across multiple sites.
  name: Content Syndication
- description: Browser-based Cloud IDE for remote Drupal development with pre-configured environments.
  name: Cloud IDE
- description: Secure API access via OAuth2 authorization code flow with scoped tokens.
  name: OAuth2 Authentication
image: /assets/icons/acquia.png
integrations:
- description: Native Drupal module integrations for Acquia Cloud, Content Hub, and Site Studio.
  name: Drupal CMS
- description: GitHub Actions workflows for Acquia Cloud deployment automation using Acquia CLI.
  name: GitHub Actions
- description: Headless Drupal with Next.js using Acquia CMS headless starter kit.
  name: Next.js
- description: Digital Asset Management integration via Widen Collective for media management in Drupal.
  name: Acquia DAM
jsonld:
- class_count: 17
  name: Acquia Context
  property_count: 73
  slug: acquia-context
layout: provider
modified: '2026-04-19'
name: Acquia
rules:
- name: Acquia API Rules
  rule_count: 32
  severity_counts:
    error: 14
    hint: 0
    info: 8
    warn: 10
  slug: acquia-spectral-rules
skills: []
slug: acquia
solutions: []
tags:
- Content
- Experience
url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/apis.yml
use_cases:
- description: Integrate Acquia Cloud API into CI/CD pipelines for automated code deployment and cache clearing.
  name: Automated Deployment Pipelines
- description: Manage dev, staging, and production Drupal environments programmatically.
  name: Multi-Environment Management
- description: Automate team provisioning, SSH key management, and organizational access control.
  name: Platform Administration
- description: Use Content Hub API to distribute content across a network of Drupal sites.
  name: Content Distribution
- description: Manage decoupled Drupal applications with Next.js or other frontend frameworks via Acquia APIs.
  name: Headless Drupal
---
