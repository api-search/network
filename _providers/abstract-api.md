---
api_count: 14
apis:
- description: Validate email addresses for deliverability, detect disposable or risky domains, verify SMTP/MX records, and enrich email data with sender information, breach history, and risk scoring.
  name: Email Reputation API
  slug: email-reputation
- description: Identify carrier, line type, validity, location, and get deep insights including line status, VoIP detection, and risk scoring for any phone number globally.
  name: Phone Intelligence API
  slug: phone-intelligence
- description: Geolocate any IPv4 or IPv6 address to country, region, city, coordinates, timezone, currency, and flag data covering 4 billion+ IP addresses across 250,000+ cities worldwide.
  name: IP Geolocation API
  slug: ip-geolocation
- description: Detect VPNs, proxies, Tor exit nodes, abuse potential, hosting services, relays, and mobile IPs. Also provides ASN, company, location, timezone, flag, and currency data for any IP address.
  name: IP Intelligence API
  slug: ip-intelligence
- description: Retrieve comprehensive details about businesses using their domain or email address, including name, logo, headcount, location, industry, and more.
  name: Company Enrichment API
  slug: company-enrichment
- description: Look up the latest exchange rates for 80+ currencies, convert between currencies, and retrieve historical exchange rate data using ISO 4217 currency codes.
  name: Exchange Rates API
  slug: exchange-rates
- description: Get public, local, religious, and other holidays for any country. Supports year and country filtering with comprehensive holiday metadata.
  name: Public Holidays API
  slug: public-holidays
- description: Find, convert, and manage time and timezone data across the world. Supports lookup by location or coordinates and returns local time, timezone abbreviation, UTC offset, and DST information.
  name: Timezone API
  slug: timezones
- description: Validate VAT numbers, look up current VAT rates by country, and calculate VAT-inclusive or VAT-exclusive prices to stay compliant for domestic and cross-border sales.
  name: VAT Validation API
  slug: vat-validation
- description: Determine the validity and details of International Bank Account Numbers (IBANs), including bank name, account type, and country code.
  name: IBAN Validation API
  slug: iban-validation
- description: Capture high-quality screenshots of any website with optional customizations including CSS injection, delay settings, and viewport configuration.
  name: Website Screenshot API
  slug: website-screenshot
- description: Compress, convert, and optimize images by URL or direct upload. Supports format conversion, quality adjustment, and size reduction.
  name: Image Processing API
  slug: image-processing
- description: Extract data from any website by providing the target URL. Handles JavaScript rendering and returns the full HTML content of any web page.
  name: Web Scraping API
  slug: web-scraping
- description: Create highly customizable avatar images using a person's name or initials. Supports color, font, and size customization for user profile images.
  name: Avatars API
  slug: avatars
capabilities:
- description: Unified data enrichment workflow combining IP geolocation, company enrichment, and timezone APIs. Used by product teams and data engineers to automatically enrich user profiles, personalize experience
  name: Abstract API Data Enrichment
  slug: data-enrichment
- description: Unified financial compliance workflow combining exchange rates, VAT validation, and IBAN validation APIs. Used by finance teams, e-commerce platforms, and fintech developers to automate VAT compliance
  name: Abstract API Financial Compliance
  slug: financial-compliance
- description: Unified fraud detection and risk assessment workflow combining email reputation, phone intelligence, and IP intelligence APIs. Used by security engineers, fraud analysts, and compliance teams to detec
  name: Abstract API Fraud Detection
  slug: fraud-detection
common:
- title: ''
  type: Website
  url: https://www.abstractapi.com/
- title: ''
  type: Portal
  url: https://app.abstractapi.com/
- title: ''
  type: SignUp
  url: https://app.abstractapi.com/users/signup
- title: ''
  type: Login
  url: https://app.abstractapi.com/users/login
- title: ''
  type: Pricing
  url: https://www.abstractapi.com/pricing
- title: ''
  type: Blog
  url: https://www.abstractapi.com/blog
- title: ''
  type: Documentation
  url: https://docs.abstractapi.com/
- title: ''
  type: GettingStarted
  url: https://docs.abstractapi.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/abstractapi
- title: ''
  type: TermsOfService
  url: https://www.abstractapi.com/legal/terms
- title: ''
  type: PrivacyPolicy
  url: https://www.abstractapi.com/legal/privacy
- title: ''
  type: Authentication
  url: https://docs.abstractapi.com/
- title: ''
  type: SpectralRules
  url: rules/abstract-api-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/fraud-detection.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/data-enrichment.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/financial-compliance.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/abstract-api-vocabulary.yaml
created: '2025-02-24'
description: Abstract API is a platform that offers a wide range of API services for developers to easily integrate various functionalities into their applications. Services include IP geolocation, IP intelligence, email validation, phone validation, currency exchange, website screenshots, image processing, web scraping, company enrichment, public holidays, timezone lookup, VAT validation, IBAN validation, and user avatar generation. Abstract API provides a seamless way for developers to access powerful features without having to build them from scratch.
features:
- description: Each API uses a unique API key passed as a query parameter or Bearer token header
  name: API Key Authentication
- description: Each API offers a free tier with limited monthly requests and 1 request/second rate limit
  name: Free Tier
- description: All APIs follow a simple REST pattern with a single base URL and query parameters
  name: Simple REST API
- description: Data covers global locations with 80+ currencies, 250,000+ cities, and worldwide phone/IP coverage
  name: Global Coverage
- description: All API responses return structured JSON data with consistent error codes
  name: JSON Responses
- description: Each API is independently keyed and priced, allowing granular subscription management
  name: Modular Services
image: /assets/icons/abstract-api.png
integrations:
- description: Official JavaScript SDK for Exchange Rates, Email Validation, IP Geolocation, and Phone Validation
  name: JavaScript
- description: Official Python SDK for Exchange Rates, Email Validation, IP Geolocation, and Phone Validation
  name: Python
- description: Official PHP SDK for Exchange Rates, Email Validation, IP Geolocation, and Phone Validation
  name: PHP
jsonld:
- class_count: 1
  name: Abstract Api Company Enrichment Context
  property_count: 11
  slug: abstract-api-company-enrichment-context
- class_count: 7
  name: Abstract Api Email Reputation Context
  property_count: 42
  slug: abstract-api-email-reputation-context
- class_count: 3
  name: Abstract Api Exchange Rates Context
  property_count: 8
  slug: abstract-api-exchange-rates-context
- class_count: 1
  name: Abstract Api Iban Validation Context
  property_count: 12
  slug: abstract-api-iban-validation-context
- class_count: 1
  name: Abstract Api Image Processing Context
  property_count: 5
  slug: abstract-api-image-processing-context
- class_count: 5
  name: Abstract Api Ip Geolocation Context
  property_count: 32
  slug: abstract-api-ip-geolocation-context
- class_count: 8
  name: Abstract Api Ip Intelligence Context
  property_count: 35
  slug: abstract-api-ip-intelligence-context
- class_count: 2
  name: Abstract Api Phone Intelligence Context
  property_count: 11
  slug: abstract-api-phone-intelligence-context
- class_count: 1
  name: Abstract Api Public Holidays Context
  property_count: 12
  slug: abstract-api-public-holidays-context
- class_count: 1
  name: Abstract Api Timezones Convert Context
  property_count: 10
  slug: abstract-api-timezones-convert-context
- class_count: 1
  name: Abstract Api Timezones Current Context
  property_count: 9
  slug: abstract-api-timezones-current-context
- class_count: 3
  name: Abstract Api Vat Validation Context
  property_count: 18
  slug: abstract-api-vat-validation-context
- class_count: 1
  name: Abstract Api Web Scraping Context
  property_count: 3
  slug: abstract-api-web-scraping-context
layout: provider
modified: '2026-04-19'
name: Abstract API
rules:
- name: Abstract API API Rules
  rule_count: 34
  severity_counts:
    error: 17
    hint: 0
    info: 6
    warn: 11
  slug: abstract-api-spectral-rules
skills: []
slug: abstract-api
solutions: []
tags:
- Avatars
- Company Enrichment
- Contacts
- Currencies
- Email Validation
- Exchange Rates
- IBAN Validation
- Image Processing
- IP Geolocation
- IP Intelligence
- Phone Validation
- Public Holidays
- Screenshots
- Timezones
- VAT Validation
- Web Scraping
url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/apis.yml
use_cases:
- description: Validate and filter email lists to improve deliverability and reduce bounce rates
  name: Email List Cleaning
- description: Use IP intelligence, email reputation, and phone intelligence to detect and block fraudulent users
  name: Fraud Detection
- description: Automatically enrich user profiles with geolocation, company, and contact data at signup
  name: User Onboarding Enrichment
- description: Display localized pricing or perform currency conversions in e-commerce and fintech apps
  name: Currency Conversion
- description: Validate VAT numbers and IBAN codes to automate financial compliance workflows
  name: Compliance Automation
- description: Use web scraping API to extract structured data from any website for data pipelines
  name: Content Extraction
- description: Generate placeholder avatars for users without profile photos using the Avatars API
  name: Dynamic User Avatars
---
