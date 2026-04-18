---
api_count: 4
apis:
- description: REST API for managing Microsoft Edge browser extensions through the Partner Center. Enables programmatic publishing, updating, and managing Edge extensions in the Microsoft Edge Add-ons store, support
  name: Microsoft Edge Add-ons API
  slug: edge-addons-api
- description: HTTP endpoints for the Microsoft Edge DevTools Protocol, based on the Chromium DevTools Protocol. These endpoints allow programmatic discovery and management of debuggable browser targets including pa
  name: Microsoft Edge DevTools Protocol HTTP API
  slug: edge-devtools-api
- description: Build browser extensions for Microsoft Edge using the Chromium-based extensions platform. Supports the WebExtensions API standard for cross-browser compatibility.
  name: Microsoft Edge Extensions API
  slug: edge-extensions-api
- description: Modern web APIs and standards supported in Microsoft Edge, including Progressive Web App capabilities, Web Components, and emerging web platform features.
  name: Microsoft Edge Web Platform APIs
  slug: edge-web-platform-apis
capabilities:
- description: Unified workflow for Microsoft Edge browser development combining DevTools Protocol debugging with Add-ons extension lifecycle management. Used by extension developers, web developers, and QA engineer
  name: Microsoft Edge Browser Development
  slug: browser-development
common:
- title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/microsoft-edge/
- title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/microsoft-edge/
- title: ''
  type: Blog
  url: https://blogs.windows.com/msedgedev/
- title: ''
  type: GitHubOrganization
  url: https://github.com/MicrosoftEdge
- title: ''
  type: GitHubRepository
  url: https://github.com/MicrosoftEdge/WebView2Samples
- title: ''
  type: GitHubRepository
  url: https://github.com/nicedoc/nicedoc.io
- title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/
- title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/microsoft-edge/web-platform/release-notes/
- title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel
- title: ''
  type: StatusPage
  url: https://developer.microsoft.com/en-us/microsoft-edge/status/
- title: ''
  type: X
  url: https://twitter.com/MSEdgeDev
- title: ''
  type: TermsOfService
  url: https://www.microsoft.com/legal/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/privacystatement
- title: ''
  type: SDK
  url: https://www.nuget.org/packages/Microsoft.Web.WebView2
- title: ''
  type: SignUp
  url: https://partner.microsoft.com/dashboard/microsoftedge/
- title: ''
  type: Login
  url: https://partner.microsoft.com/dashboard/
- title: ''
  type: Marketplace
  url: https://microsoftedge.microsoft.com/addons/
- title: DevTools API Context
  type: JSONLD
  url: json-ld/microsoft-edge-devtools-api-context.jsonld
- title: Add-ons API Context
  type: JSONLD
  url: json-ld/microsoft-edge-addons-api-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/microsoft-edge-spectral-rules.yml
- title: Browser Development Workflow
  type: NaftikoCapability
  url: capabilities/browser-development.yaml
- title: DevTools API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/devtools-api.yaml
- title: Add-ons API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/addons-api.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/microsoft-edge-vocabulary.yaml
created: '2024-01-01'
description: APIs and resources for Microsoft Edge browser development and integration, including the Edge Add-ons API for extension management, DevTools Protocol for browser debugging and automation, Extensions API for building browser extensions, and Web Platform APIs for progressive web app development.
features:
- description: Programmatically publish, update, and manage browser extensions in the Edge Add-ons store via REST API.
  name: Extension Publishing API
- description: Debug and inspect web pages, service workers, and extensions using the Chrome DevTools Protocol over WebSocket.
  name: Remote Debugging Protocol
- description: Embed Microsoft Edge rendering engine in native desktop applications using the WebView2 SDK.
  name: WebView2 Embedding
- description: Build installable PWAs with offline capability, push notifications, and system integration.
  name: Progressive Web App Support
- description: Build extensions using the Chromium WebExtensions API standard for cross-browser portability.
  name: Cross-Browser Extension Compatibility
- description: Automate browser tasks including page navigation, target management, and performance profiling.
  name: Browser Automation
- description: Load and test unpacked extensions locally during development without publishing to the store.
  name: Extension Sideloading
- description: Build extensions using the latest Manifest V3 specification with service workers and declarative APIs.
  name: Manifest V3 Support
image: https://www.microsoft.com/edge/favicon.ico
integrations:
- description: Authenticate to the Edge Add-ons API using Azure AD OAuth 2.0 client credentials flow.
  name: Azure Active Directory
- description: Manage extension listings, submissions, and analytics through the Partner Center dashboard.
  name: Microsoft Partner Center
- description: Debug Edge browser content directly from VS Code using the Edge DevTools extension.
  name: Visual Studio Code
- description: Automate Microsoft Edge browser for testing using Selenium with the Edge WebDriver.
  name: Selenium WebDriver
- description: Cross-browser automation framework with first-class support for Microsoft Edge testing.
  name: Playwright
- description: Control headless Microsoft Edge instances programmatically using the Puppeteer Node.js library.
  name: Puppeteer
- description: Automate extension publishing and browser testing in CI/CD workflows using GitHub Actions.
  name: GitHub Actions
- description: Integrate WebView2 into Windows desktop applications built with WinUI 3 and the Windows App SDK.
  name: Windows App SDK
jsonld:
- class_count: 3
  name: Microsoft Edge Addons Api Context
  property_count: 13
  slug: microsoft-edge-addons-api-context
- class_count: 3
  name: Microsoft Edge Devtools Api Context
  property_count: 16
  slug: microsoft-edge-devtools-api-context
layout: provider
modified: '2026-04-18'
name: Microsoft Edge
rules:
- name: Microsoft Edge API Rules
  rule_count: 27
  severity_counts:
    error: 15
    hint: 0
    info: 0
    warn: 12
  slug: microsoft-edge-spectral-rules
skills: []
slug: microsoft-edge
solutions: []
tags:
- Browser
- Chromium
- Developer Tools
- Edge
- Extensions
- Microsoft
- Progressive Web Apps
- Web Development
- WebView
url: https://www.microsoft.com/edge
use_cases:
- description: Use the Add-ons API to automate CI/CD pipelines for publishing and updating browser extensions.
  name: Automated Extension Deployment
- description: Leverage DevTools Protocol for automated browser testing, performance auditing, and regression detection.
  name: Browser Testing and QA
- description: Embed Edge rendering in desktop applications for custom browser experiences using WebView2.
  name: Custom Browser Controls
- description: Build enterprise extensions for content filtering, security policy enforcement, and compliance monitoring.
  name: Enterprise Content Filtering
- description: Use DevTools Protocol to programmatically navigate pages and extract structured data.
  name: Web Scraping and Data Extraction
- description: Automate accessibility audits using DevTools Protocol to inspect DOM, ARIA attributes, and contrast ratios.
  name: Accessibility Testing
- description: Collect real-time performance metrics, network traces, and JavaScript profiling data via DevTools Protocol.
  name: Performance Monitoring
- description: Build and distribute PWAs through the Microsoft Store with native-like installation and system integration.
  name: Progressive Web App Distribution
---
