---
api_count: 6
apis:
- description: 'The Amazon Selling Partner API (SP-API) is a RESTful API that enables Amazon sellers and vendors to programmatically manage their marketplace operations including listings, orders, payments, reports, '
  name: Amazon Selling Partner API
  slug: selling-partner-api
- description: The Amazon Advertising API enables programmatic management of advertising campaigns on Amazon including Sponsored Products, Sponsored Brands, and Sponsored Display campaigns across various marketplace
  name: Amazon Advertising API
  slug: advertising-api
- description: The Amazon Creators API provides programmatic access to Amazon product data for publishers, influencers, and affiliate partners. It is the recommended replacement for the Product Advertising API and r
  name: Amazon Creators API
  slug: creators-api
- description: The Amazon Pay API enables merchants to integrate Amazon Pay for payment processing on their websites and mobile applications. It supports one-time purchases, subscriptions, and recurring payments wit
  name: Amazon Pay API
  slug: pay-api
- description: The Alexa Skills Kit (ASK) REST APIs enable developers to create, manage, test, and deploy custom voice skills for Alexa-enabled devices including skill manifest management, interaction model building
  name: Amazon Alexa Skills Kit API
  slug: alexa-skills-kit-api
- description: The Amazon Appstore Developer APIs provide tools for managing app submissions, testing, and monetization through in-app purchases on the Amazon Appstore for Android and Fire OS applications.
  name: Amazon Appstore API
  slug: appstore-api
capabilities:
- description: Unified workflow for Amazon sellers, advertisers, and merchants to manage marketplace listings and orders, run advertising campaigns, and process payments using Amazon Selling Partner API, Amazon Adve
  name: Amazon Seller and Commerce Workflow
  slug: amazon-seller-and-commerce
common:
- title: ''
  type: Portal
  url: https://developer.amazon.com/
- title: ''
  type: Website
  url: https://www.amazon.com/
- title: ''
  type: Documentation
  url: https://developer.amazon.com/docs/
- title: ''
  type: TermsOfService
  url: https://developer.amazon.com/support/legal/da
- title: ''
  type: PrivacyPolicy
  url: https://www.amazon.com/gp/help/customer/display.html?nodeId=468496
- title: ''
  type: Support
  url: https://developer.amazon.com/support
- title: ''
  type: GitHubOrganization
  url: https://github.com/amzn
- title: ''
  type: Console
  url: https://developer.amazon.com/dashboard
- title: ''
  type: SignUp
  url: https://www.amazon.com/ap/register?openid.assoc_handle=aws
- title: ''
  type: Login
  url: https://developer.amazon.com/login
- title: ''
  type: Blog
  url: https://developer.amazon.com/blogs/
- title: ''
  type: YouTube
  url: https://www.youtube.com/c/AmazonDeveloper
- title: ''
  type: Contact
  url: https://www.amazon.com/gp/help/customer/contact-us
- title: ''
  type: JSONLD
  url: json-ld/amazon-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/amazon-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-seller-and-commerce.yaml
created: '2024-01-15'
description: Amazon is a global technology and e-commerce company offering a wide range of consumer and developer APIs including the Selling Partner API for marketplace sellers, Advertising API for campaign management, Amazon Pay for payments, Alexa Skills Kit for voice experiences, Amazon Appstore for mobile applications, and the Creators API for affiliate publishers. These APIs power Amazon's ecosystem of sellers, developers, advertisers, and content creators.
features:
- description: Full lifecycle management of Amazon marketplace seller operations including catalog, inventory, orders, shipping, and financial reporting.
  name: Marketplace Seller Operations
- description: Create and optimize Sponsored Products, Sponsored Brands, and Sponsored Display advertising campaigns with granular targeting and reporting.
  name: Programmatic Advertising
- description: Enable Amazon Pay on external websites and mobile apps with checkout session management, one-time charges, subscriptions, and refunds.
  name: Amazon Pay Integration
- description: Build Alexa voice skills for Echo devices, Fire TV, and third-party Alexa-enabled hardware with the Alexa Skills Kit.
  name: Voice Experience Development
- description: Access Amazon product data for affiliate marketing and content creation through the Creators API with product search and deep linking.
  name: Affiliate and Creator Commerce
- description: Publish and monetize apps on the Amazon Appstore with in-app purchasing for digital goods, subscriptions, and consumables.
  name: Mobile App Monetization
- description: Access North America, Europe, and Far East marketplaces through region-specific SP-API endpoints.
  name: Multi-Region Marketplace Support
- description: Sandbox environments, developer consoles, and testing tools for building and validating Amazon integrations before going live.
  name: Developer Console and Testing Tools
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: SP-API is the modern replacement for the deprecated Amazon Marketplace Web Service (MWS) for all seller operations.
  name: Amazon MWS Legacy Migration
- description: Integrate smart home devices and services with Alexa voice control using the Smart Home Skill API.
  name: Alexa Smart Home
- description: OAuth 2.0 authentication for all Amazon developer APIs including SP-API, Advertising API, and ASK via Login with Amazon (LWA).
  name: Login with Amazon
- description: Affiliate program integration for the Creators API and Product Advertising API for commission-based product promotion.
  name: Amazon Associates Program
- description: Amazon Appstore SDK for Fire OS and Android apps with in-app purchasing and device targeting capabilities.
  name: Fire OS and Android
jsonld:
- class_count: 53
  name: Amazon Context
  property_count: 113
  slug: amazon-context
layout: provider
modified: '2026-04-19'
name: Amazon
rules:
- name: Amazon API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 6
  slug: amazon-spectral-rules
skills: []
slug: amazon
solutions: []
tags:
- Amazon
- Advertising
- Alexa
- E-Commerce
- Marketplace
- Payments
- Voice
url: https://raw.githubusercontent.com/api-evangelist/amazon/refs/heads/main/apis.yml
use_cases:
- description: Automate product listing creation, price updates, inventory management, and order fulfillment for Amazon marketplace sellers.
  name: Marketplace Seller Automation
- description: Build automated bid management and campaign optimization tools using the Amazon Advertising API and performance reporting.
  name: Advertising Campaign Optimization
- description: Add Amazon Pay as a payment option for external e-commerce sites to reduce checkout friction and increase conversion rates.
  name: E-Commerce Payment Integration
- description: Create Alexa skills for voice-driven shopping, home automation, and customer service interactions.
  name: Voice Commerce and Smart Home
- description: Build product recommendation engines and affiliate content sites using the Creators API for real-time Amazon product data.
  name: Affiliate Content Monetization
---
