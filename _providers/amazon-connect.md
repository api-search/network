---
api_count: 11
apis:
- description: The Amazon Connect Service API provides programmatic access to manage contact center instances, users, routing profiles, contact flows, queues, hours of operation, security profiles, and real-time and
  name: Amazon Connect Service API
  slug: ''
- description: Amazon Connect Streams is a browser-based integration API and JavaScript SDK that enables embedding and controlling the Amazon Connect Contact Control Panel (CCP) within your web application or CRM sy
  name: Amazon Connect Streams SDK
  slug: ''
- description: The Amazon AppIntegrations service enables you to configure and reuse connections to external applications, powering third-party integrations in the Amazon Connect agent workspace.
  name: Amazon AppIntegrations API
  slug: ''
- description: 'Amazon Connect Contact Lens enables you to analyze conversations between customers and agents using speech transcription, natural language processing, and intelligent search capabilities. It performs '
  name: Amazon Connect Contact Lens API
  slug: ''
- description: With the outbound campaigns feature of Amazon Connect, you can create high-volume outbound campaigns for appointment reminders, telemarketing, subscription renewals, or debt collection.
  name: Amazon Connect Outbound Campaigns API
  slug: ''
- description: The outbound campaigns V2 API provides an updated interface for creating high-volume outbound campaigns including multi-channel support and availability in all Amazon Connect regions.
  name: Amazon Connect Outbound Campaigns V2 API
  slug: ''
- description: With Amazon Connect Cases, agents can track and manage customer issues that require multiple interactions, follow-up tasks, and teams in your contact center. A case represents a customer issue includi
  name: Amazon Connect Cases API
  slug: ''
- description: The Amazon Connect Participant Service enables managing chat participants including agents, customers, and managers. Use it to send messages and events, manage connection state, share attachments, and
  name: Amazon Connect Participant Service API
  slug: ''
- description: Amazon Connect Customer Profiles provides a unified customer profile for your contact center with pre-built connectors powered by AppFlow that make it easy to combine customer information from third-p
  name: Amazon Connect Customer Profiles API
  slug: ''
- description: Amazon Q in Connect is a generative AI customer service assistant built on Amazon Bedrock. It provides real-time recommendations to help contact center agents resolve customer issues quickly and accur
  name: Amazon Q Connect API
  slug: ''
- description: Amazon Connect Voice ID provides real-time caller authentication and fraud risk detection to make voice interactions in contact centers more secure and efficient. Note - Voice ID end of support is sch
  name: Amazon Voice ID API
  slug: ''
capabilities:
- description: 'Unified workflow capability for contact center operations combining instance management, agent management, queue management, contact handling, and real-time/historical metrics. Used by contact center '
  name: Amazon Connect Contact Center Operations
  slug: contact-center-operations
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/connect/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/connect/latest/adminguide/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/contact-center/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: GitHubOrganization
  url: https://github.com/amazon-connect
- title: ''
  type: Console
  url: https://console.aws.amazon.com/connect/
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
  url: https://stackoverflow.com/questions/tagged/amazon-connect
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
  type: Pricing
  url: https://aws.amazon.com/connect/pricing/
- title: ''
  type: SpectralRules
  url: rules/amazon-connect-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-connect-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/contact-center-operations.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/connect-service.yaml
created: '2024-01-15'
description: Amazon Connect is a cloud-based contact center service that makes it easy to set up and manage a customer contact center and provide reliable customer engagement at any scale, with omnichannel support for voice, chat, email, and task management. It includes AI-powered features for agent assistance, customer profiles, conversation analytics, and outbound campaign management.
features:
- description: Unified routing across voice, chat, email, and tasks through a single platform with skills-based routing and priority queuing.
  name: Omnichannel Routing
- description: Amazon Q in Connect provides real-time AI-generated recommendations and answers to help agents resolve customer issues faster.
  name: AI-Powered Agent Assist
- description: Drag-and-drop contact flow designer for building IVR, chatbot, and agent guidance workflows without extensive coding.
  name: Contact Flows
- description: Contact Lens provides speech transcription, sentiment analysis, and NLP-powered insights across all customer interactions.
  name: Conversational Analytics
- description: Unified customer profile combining CRM, ITSM, ERP, and contact history data for context-aware agent interactions.
  name: Customer Profiles
- description: High-volume multi-channel outbound campaigns with predictive dialer, answering machine detection, and multiple dialing modes.
  name: Outbound Campaigns
- description: Structured case tracking for customer issues requiring multiple interactions, follow-up tasks, and cross-team coordination.
  name: Cases Management
- description: In-app, web, and video calling with screen share capabilities using 16kHz high-quality audio with packet loss resistance.
  name: Voice and Video Calling
- description: Real-time and asynchronous messaging including SMS, WhatsApp Business, and Apple Messages for Business integration.
  name: Chat and Messaging
- description: Comprehensive dashboards and reporting for contact center performance optimization and workforce planning.
  name: Real-Time and Historical Metrics
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Pre-built AppFlow connector to sync Salesforce customer data into Amazon Connect Customer Profiles.
  name: Salesforce CRM
- description: ITSM integration via AppFlow to bring ServiceNow customer and case data into the Amazon Connect agent workspace.
  name: ServiceNow
- description: Native integration with AWS Lambda for custom automation within contact flows and agent events.
  name: AWS Lambda
- description: Built-in integration with Amazon Lex for building conversational AI bots for voice and chat self-service.
  name: Amazon Lex
- description: Foundation for Amazon Q in Connect generative AI features, providing real-time agent recommendations and answers.
  name: Amazon Bedrock
- description: Storage integration for call recordings, contact transcripts, exported reports, and Contact Lens output data.
  name: Amazon S3
- description: Real-time streaming of contact trace records (CTRs) and agent events to data lakes and analytics pipelines.
  name: Amazon Kinesis
- description: Native channel integration to handle customer messaging through WhatsApp Business within the Amazon Connect platform.
  name: WhatsApp Business
jsonld:
- class_count: 61
  name: Amazon Connect Context
  property_count: 132
  slug: amazon-connect-context
layout: provider
modified: '2026-04-19'
name: Amazon Connect
rules:
- name: Amazon Connect API Rules
  rule_count: 36
  severity_counts:
    error: 16
    hint: 0
    info: 3
    warn: 17
  slug: amazon-connect-spectral-rules
skills: []
slug: amazon-connect
solutions: []
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
url: https://raw.githubusercontent.com/api-evangelist/amazon-connect/refs/heads/main/apis.yml
use_cases:
- description: Deploy an omnichannel contact center handling voice, chat, email, and messaging with intelligent routing to the right agents.
  name: Customer Support Contact Center
- description: Build conversational AI flows that handle common customer requests in 30+ languages without agent involvement.
  name: AI-Powered Self-Service
- description: Reduce average handle time with real-time AI guidance, unified agent workspace, and automated post-contact work.
  name: Agent Productivity Improvement
- description: Run appointment reminders, subscription renewals, payment notifications, and telemarketing campaigns at scale.
  name: Outbound Customer Engagement
- description: Use Voice ID for real-time caller authentication and fraud risk detection in voice contact center interactions.
  name: Fraud Prevention
- description: Analyze 100% of customer interactions with Contact Lens for regulatory compliance and quality assurance.
  name: Compliance and Quality Monitoring
---
