---
api_count: 1
apis:
- description: The AmTrust Commercial Lines API enables insurance agents, brokers, and technology partners to programmatically review coverage appetite, generate quotes, and bind commercial lines policies. It suppor
  name: AmTrust Commercial Lines API
  slug: commercial-lines-api
capabilities:
- description: Workflow capability for reviewing appetite, generating quotes, and binding commercial lines policies. Used by insurance agents and broker platforms.
  name: AmTrust Insurance Quoting and Binding
  slug: amtrust-insurance-quoting-and-binding
common:
- title: ''
  type: Portal
  url: https://amtrustfinancial.com
- title: ''
  type: DeveloperPortal
  url: https://utapiportal.amtrustgroup.com
- title: ''
  type: Documentation
  url: https://amtrustfinancial.com/api
- title: ''
  type: Authentication
  url: https://utapiportal.amtrustgroup.com/authentication
- title: ''
  type: SignUp
  url: https://amtrustfinancial.com/api
- title: ''
  type: Support
  url: https://amtrustfinancial.com/contact-us
- title: ''
  type: TermsOfService
  url: https://amtrustfinancial.com/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://amtrustfinancial.com/privacy-policy
- title: ''
  type: SpectralRules
  url: rules/amtrust-financial-services-spectral-rules.yml
- title: ''
  type: JSONSchema
  url: json-schema/amtrust-financial-services-quote-request-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/amtrust-financial-services-quote-response-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/amtrust-financial-services-policy-schema.json
- title: ''
  type: JSONLD
  url: json-ld/amtrust-financial-services-context.jsonld
- title: ''
  type: Vocabulary
  url: vocabulary/amtrust-financial-services-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amtrust-insurance-quoting-and-binding.yaml
- title: ''
  type: JSONStructure
  url: json-structure/amtrust-financial-services-quote-request-structure.json
created: ''
description: AmTrust Financial Services is a multinational specialty property and casualty insurer focused on small to mid-sized businesses. AmTrust provides APIs that enable insurance agents, brokers, and technology partners to review appetite, generate quotes, and bind policies programmatically. The API platform processes over 12 million API calls daily with 99.68% availability and supports workers' compensation, business owners' policies, general liability, and other commercial insurance products across 300+ eligible class codes.
features:
- description: Review coverage eligibility for specific business classes and risk profiles.
  name: Appetite Check
- description: Generate commercial lines quotes in real time via API.
  name: Instant Quoting
- description: Bind policies programmatically for eligible class codes.
  name: Online Binding
- description: Access over 300 bind-online eligible class codes.
  name: 300+ Class Codes
- description: Token-based authentication with 4-hour access tokens.
  name: OAuth 2.0 Authentication
- description: 12 million daily API calls with 99.68% uptime SLA.
  name: High Availability
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Workers' compensation digital submission integration.
  name: Appulate
- description: Commercial lines quoting platform integration.
  name: Semsee
- description: Commercial lines quoting marketplace integration.
  name: Tarmika
- description: Commercial lines rating platform integration.
  name: IBQ Systems
jsonld:
- class_count: 6
  name: Amtrust Financial Services Context
  property_count: 13
  slug: amtrust-financial-services-context
layout: provider
modified: '2026-04-19'
name: AmTrust Financial Services
rules:
- name: AmTrust Financial Services API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 3
  slug: amtrust-financial-services-spectral-rules
skills: []
slug: amtrust-financial-services
solutions: []
tags:
- Commercial Insurance
- Insurance
- Property And Casualty
- Small Business
- Workers Compensation
url: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/apis.yml
use_cases:
- description: Embed AmTrust quoting and binding in agent management systems.
  name: Agent Platform Integration
- description: Automate workers' compensation submissions from wholesale platforms.
  name: Wholesale Brokerage Automation
- description: Connect agency management software to AmTrust for policy lifecycle management.
  name: AMS Software Integration
- description: Streamline small business workers' compensation from quote to bind.
  name: Workers Compensation Automation
---
