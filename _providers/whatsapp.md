---
api_count: 4
apis:
- description: The Cloud API and On-Premises API that enables medium and large businesses to communicate with customers at scale.
  name: WhatsApp Business Platform API
  slug: business-platform-api
- description: API for managing WhatsApp Business Accounts, phone numbers, and messaging templates.
  name: WhatsApp Business Account Management API
  slug: business-account-management-api
- description: 'API for creating structured, interactive forms and multi-step flows within WhatsApp conversations, enabling appointment booking, surveys, lead capture, and other guided experiences using a JSON-based '
  name: WhatsApp Flows API
  slug: flows-api
- description: 'The self-hosted version of the WhatsApp Business API that allowed businesses to run the API on their own infrastructure. This API was deprecated on October 23, 2025, and all users must migrate to the '
  name: WhatsApp On-Premises API
  slug: on-premises-api
asyncapis:
- description: 'WhatsApp Business Platform webhooks deliver real-time notifications for incoming messages, message status updates, template status changes, account updates, phone number quality changes, and security '
  name: WhatsApp Webhooks
  slug: whatsapp-webhooks-asyncapi
capabilities:
- description: Unified workflow for managing WhatsApp Business Accounts, phone numbers, business profiles, user assignments, product catalogs, and phone registration. Combines Business Management API and Cloud API c
  name: WhatsApp Account And Phone Management
  slug: account-and-phone-management
- description: Unified workflow for creating and managing interactive flows, publishing lifecycle management, and webhook subscriptions. Combines Flows API and Business Management API webhook capabilities used by de
  name: WhatsApp Flows And Automation
  slug: flows-and-automation
- description: Unified workflow for sending messages, managing media files, and creating QR codes for customer conversations. Combines WhatsApp Cloud API messaging, media management, and QR code capabilities used by
  name: WhatsApp Messaging And Media
  slug: messaging-and-media
- description: 'Unified workflow for managing message templates and analyzing conversation and template performance. Combines Business Management API template CRUD and analytics capabilities used by marketing teams, '
  name: WhatsApp Templates And Analytics
  slug: templates-and-analytics
common:
- title: ''
  type: TermsOfService
  url: https://www.whatsapp.com/legal/business-terms
- title: ''
  type: PrivacyPolicy
  url: https://www.whatsapp.com/legal/privacy-policy-eea
- title: ''
  type: Commerce Policy
  url: https://www.whatsapp.com/legal/commerce-policy
- title: ''
  type: Developer Portal
  url: https://developers.facebook.com/
- title: ''
  type: GettingStarted
  url: https://developers.facebook.com/docs/whatsapp/cloud-api/get-started
- title: ''
  type: Authentication
  url: https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
- title: ''
  type: Best Practices
  url: https://developers.facebook.com/docs/whatsapp/cloud-api/best-practices
- title: ''
  type: Use Cases
  url: https://business.whatsapp.com/products/business-platform
- title: ''
  type: Change Log
  url: https://developers.facebook.com/docs/whatsapp/cloud-api/changelog
- title: ''
  type: StatusPage
  url: https://metastatus.com/
- title: ''
  type: Blog
  url: https://business.whatsapp.com/blog
- title: ''
  type: Support
  url: https://developers.facebook.com/support/
- title: ''
  type: Console
  url: https://developers.facebook.com/apps/
- title: ''
  type: GitHub Organization
  url: https://github.com/WhatsApp
- title: ''
  type: Community
  url: https://business.whatsapp.com/developers/developer-hub
- title: ''
  type: Stack Overflow
  url: https://stackoverflow.com/questions/tagged/whatsapp-cloud-api
- title: ''
  type: Security
  url: https://www.whatsapp.com/security/WhatsApp-Security-Whitepaper.pdf
- title: ''
  type: PostmanCollection
  url: https://www.postman.com/meta/whatsapp-business-platform/overview
- title: ''
  type: Pricing
  url: https://business.whatsapp.com/products/platform-pricing
- title: ''
  type: JSON-LD
  url: json-ld/whatsapp-context.jsonld
- title: ''
  type: JSONSchema
  url: json-schema/whatsapp-webhook-payload-schema.json
- title: ''
  type: Node.js SDK
  url: https://github.com/WhatsApp/WhatsApp-Nodejs-SDK
- title: ''
  type: API Examples
  url: https://github.com/fbsamples/whatsapp-api-examples
- title: ''
  type: Business Messaging Policy
  url: https://business.whatsapp.com/policy
- title: ''
  type: Meta Terms
  url: https://www.whatsapp.com/legal/meta-terms-whatsapp-business
- title: ''
  type: FAQ
  url: https://business.whatsapp.com/resources/faq
- title: ''
  type: Sandbox
  url: https://business.whatsapp.com/developers/developer-hub
- title: ''
  type: Versioning
  url: https://developers.facebook.com/docs/graph-api/guides/versioning
- title: ''
  type: Migration Guide
  url: https://developers.facebook.com/docs/whatsapp/cloud-api/migrate-to-cloud-api
- title: ''
  type: RateLimits
  url: https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput
- title: ''
  type: Error Codes
  url: https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes
created: '2024-01-15'
description: APIs for the WhatsApp messaging platform, enabling businesses to communicate with customers through the world's most popular messaging app.
features:
- description: Send and receive messages, media, and interactive content through Meta-hosted WhatsApp infrastructure.
  name: Cloud API
- description: Pre-approved message templates for proactive customer communication with variable substitution.
  name: Message Templates
- description: Buttons, lists, product catalogs, and flows for rich customer engagement.
  name: Interactive Messages
- description: Send and receive images, videos, documents, audio, stickers, and location data.
  name: Media Messaging
- description: Real-time notifications for incoming messages, delivery status, and account events.
  name: Webhooks
- description: Manage WhatsApp Business accounts, phone numbers, and messaging limits.
  name: Business Management API
- description: Build interactive multi-step forms and workflows within WhatsApp conversations.
  name: Flows
- description: Share product catalogs and enable in-chat commerce experiences.
  name: Catalogs and Commerce
- description: End-to-end encryption for all messages and media.
  name: Encryption
- description: Route conversations to multiple agents with conversation assignment.
  name: Multi-Agent Support
image: /assets/icons/whatsapp.png
integrations:
- description: Manage WhatsApp alongside Facebook and Instagram from a unified dashboard.
  name: Meta Business Suite
- description: CRM integration for managing customer conversations and contact history.
  name: Salesforce
- description: E-commerce integration for order notifications and customer messaging.
  name: Shopify
- description: Marketing and sales integration for lead nurturing via WhatsApp.
  name: HubSpot
- description: Help desk integration for ticketed WhatsApp customer support.
  name: Zendesk
jsonld:
- class_count: 33
  name: Whatsapp Context
  property_count: 109
  slug: whatsapp-context
layout: provider
modified: '2026-04-17'
name: WhatsApp
rules:
- name: WhatsApp API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: whatsapp-spectral-rules
skills: []
slug: whatsapp
solutions:
- description: Cloud API and On-Premises API for medium and large businesses at scale.
  name: WhatsApp Business Platform
- description: Free mobile app for small businesses with basic messaging features.
  name: WhatsApp Business App
- description: Interactive forms and workflows within WhatsApp conversations.
  name: WhatsApp Flows
tags: []
url: https://raw.githubusercontent.com/api-evangelist/whatsapp/refs/heads/main/apis.yml
use_cases:
- description: Provide real-time customer service and support through WhatsApp messaging.
  name: Customer Support
- description: Send order confirmations, shipping updates, and delivery notifications.
  name: Order Notifications
- description: Send appointment reminders and allow rescheduling via interactive messages.
  name: Appointment Reminders
- description: Send promotional messages using approved templates to opted-in customers.
  name: Marketing Campaigns
- description: Send OTP codes and verification messages for account security.
  name: Two-Factor Authentication
- description: Build automated conversational bots for FAQs and self-service workflows.
  name: Chatbot Integration
- description: Share product catalogs, process orders, and send payment reminders.
  name: E-commerce
- description: Send appointment reminders, test results, and health tips to patients.
  name: Healthcare Communication
---
