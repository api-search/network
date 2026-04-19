---
api_count: 3
apis:
- description: Provides access to Search Console data including search analytics, sitemaps, URL inspection, and index coverage reports.
  name: Google Search Console API
  slug: ''
- description: Provides tools for running validation tests against single URLs, including mobile-friendly testing and rich results validation for structured data.
  name: Google Search Console URL Testing Tools API
  slug: ''
- description: The Indexing API allows any site owner to directly notify Google when pages are added or removed, enabling faster crawling and indexing of content such as job postings and livestream videos.
  name: Google Indexing API
  slug: ''
capabilities:
- description: Unified SEO management workflow combining search analytics, sitemap management, URL inspection, and site management for SEO specialists and webmasters.
  name: Google Search Console SEO Management
  slug: seo-management
common:
- title: ''
  type: DeveloperPortal
  url: https://developers.google.com/
- title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- title: ''
  type: Blog
  url: https://developers.googleblog.com/
- title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- title: OAuth 2.0 Scopes
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2/scopes
- title: API Client Libraries
  type: SDK
  url: https://developers.google.com/api-client-library
- title: Google Search Central Blog
  type: Blog
  url: https://developers.google.com/search/updates
- title: Search Console Help
  type: Support
  url: https://support.google.com/webmasters/
- title: ''
  type: Console
  url: https://console.cloud.google.com/
- title: ''
  type: SpectralRules
  url: rules/google-search-console-spectral-rules.yml
- title: Search Console Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/search-console.yaml
- title: SEO Management Workflow
  type: NaftikoCapability
  url: capabilities/seo-management.yaml
created: '2024-01-01'
description: The Google Search Console API provides programmatic access to Search Console data, allowing you to monitor and maintain your site's presence in Google Search results.
features:
- description: Analyze search traffic data including impressions, clicks, CTR, and average position by query, page, country, device, and date.
  name: Search Analytics
- description: Submit, monitor, and manage XML sitemaps and sitemap indexes to optimize crawling and indexing.
  name: Sitemap Management
- description: Inspect individual URLs for indexing status, crawl details, mobile usability, and rich results eligibility.
  name: URL Inspection
- description: Monitor which pages are indexed, identify indexing errors, and track coverage status across your site.
  name: Index Coverage
- description: Test pages for mobile-friendliness and identify mobile usability issues.
  name: Mobile Usability Testing
- description: Validate structured data markup and check rich results eligibility for individual URLs.
  name: Rich Results Validation
- description: Manage site ownership verification and access permissions for Search Console properties.
  name: Site Verification
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
integrations:
- description: Combine Search Console data with Google Analytics for comprehensive website performance analysis.
  name: Google Analytics
- description: Connect search performance data with advertising campaigns to optimize paid and organic strategy together.
  name: Google Ads
- description: Deploy Search Console API integrations on Google Cloud Platform infrastructure.
  name: Google Cloud
- description: Export Search Console data to BigQuery for advanced analytics and cross-platform reporting.
  name: BigQuery
- description: Visualize Search Console metrics in dashboards for stakeholder reporting and trend analysis.
  name: Data Studio / Looker
jsonld:
- class_count: 0
  name: Google Search Console Context
  property_count: 0
  slug: google-search-console-context
layout: provider
modified: '2026-04-18'
name: Google Search Console
rules:
- name: Google Search Console API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: google-search-console-spectral-rules
skills: []
slug: google-search-console
solutions: []
tags:
- Analytics
- Google
- Search
- SEO
- Webmaster Tools
url: https://search.google.com/search-console/about
use_cases:
- description: Track organic search performance metrics to identify trends, measure optimization impact, and report on search visibility.
  name: SEO Performance Monitoring
- description: Identify and resolve indexing issues, crawl errors, and mobile usability problems affecting search performance.
  name: Technical SEO Auditing
- description: Analyze which queries drive traffic to specific pages and optimize content to improve rankings and click-through rates.
  name: Content Optimization
- description: Programmatically submit sitemaps when content is published or updated to accelerate indexing.
  name: Automated Sitemap Submission
- description: Monitor and manage search performance across multiple websites from a single integration.
  name: Multi-Site Management
---
