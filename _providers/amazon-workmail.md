---
api_count: 1
apis:
- description: The Amazon WorkMail API provides programmatic access to manage organizations, users, groups, aliases, mailboxes, resources, and mobile device access. It enables automation of email infrastructure prov
  name: Amazon WorkMail API
  slug: amazon-workmail-api
capabilities:
- description: Unified workflow for IT administrators and email operations teams to manage Amazon WorkMail organizations, users, groups, and mobile device access. Enables programmatic provisioning, deprovisioning, a
  name: Amazon WorkMail Email Management
  slug: email-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/workmail/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/workmail/latest/adminguide/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/workmail/
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
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: SpectralRules
  url: rules/amazon-workmail-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-workmail-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/email-management.yaml
created: '2026-03-16'
description: Amazon WorkMail is a secure, managed business email and calendar service with support for existing desktop and mobile email client applications. It provides encrypted mailboxes, corporate calendaring, full Outlook compatibility, and enterprise-grade security controls for business communications. WorkMail integrates with Active Directory, supports IMAP and Exchange ActiveSync for mobile devices, and provides 80 API operations for programmatic management.
features:
- description: Native support for Microsoft Outlook on Windows and Mac OS X with free/busy scheduling, delegation, and out-of-office replies.
  name: Outlook Compatibility
- description: Automatic encryption at rest using AWS KMS and SSL encryption in transit with spam and virus protection.
  name: Enterprise-Grade Security
- description: Integration with AWS Directory Service AD Connector and Microsoft Active Directory for seamless enterprise authentication.
  name: Active Directory Integration
- description: Exchange ActiveSync support with remote device encryption, lock, password reset, and wipe capabilities across iOS, Android, and Windows.
  name: Mobile Device Management
- description: Hybrid environments with Microsoft Exchange Server 2010 and 2013 for gradual migration scenarios.
  name: Exchange Interoperability
- description: Programmatic API for managing users, groups, resources, and organizational settings at scale.
  name: Administrative SDK
- description: Configurable email flow rules for filtering and routing messages based on custom organizational policies.
  name: Email Flow Rules
- description: Email journaling capabilities for compliance archiving and e-discovery requirements.
  name: Journaling and Archiving
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: AD Connector and Simple AD for directory integration and single sign-on capabilities.
  name: AWS Directory Service
- description: Key Management Service for managing encryption keys for mailbox data at rest.
  name: AWS KMS
- description: Audit logging of all WorkMail API calls for compliance and security monitoring.
  name: AWS CloudTrail
- description: Lambda integration for email flow rules and custom email processing workflows.
  name: AWS Lambda
- description: Native Outlook MAPI support for Windows and Mac desktops.
  name: Microsoft Outlook
jsonld:
- class_count: 184
  name: Amazon Workmail Context
  property_count: 125
  slug: amazon-workmail-context
layout: provider
modified: '2026-04-19'
name: Amazon WorkMail
rules:
- name: Amazon WorkMail API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 8
  slug: amazon-workmail-spectral-rules
skills: []
slug: amazon-workmail
solutions: []
tags:
- AWS
- Business Communication
- Calendar
- Email
- Exchange
- Enterprise
url: https://raw.githubusercontent.com/api-evangelist/amazon-workmail/refs/heads/main/apis.yml
use_cases:
- description: Migrate from Microsoft Exchange to Amazon WorkMail with minimal disruption using hybrid environment support.
  name: Exchange Migration
- description: Automate user and mailbox provisioning via API for large-scale enterprise deployments.
  name: Enterprise Email Provisioning
- description: Use journaling and encryption for HIPAA-compliant and regulatory email archiving programs.
  name: Compliance Email Archiving
- description: Provide secure mobile email access with ActiveSync and mobile device management policies.
  name: Mobile Workforce Enablement
- description: Run WorkMail alongside existing Exchange infrastructure for gradual cloud migration.
  name: Hybrid Cloud Email
---
