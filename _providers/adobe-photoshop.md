---
api_count: 7
apis:
- description: A cloud-based REST API that provides programmatic access to Photoshop's image editing capabilities without requiring a local installation. Part of Adobe Firefly Services, the API supports PSD document
  name: Adobe Photoshop API
  slug: photoshop-api
- description: A unified Node.js and TypeScript SDK that provides typed client libraries for accessing the Photoshop API and other Firefly Services. The PhotoshopClient class offers methods for background removal, m
  name: Adobe Firefly Services SDK for JavaScript
  slug: firefly-services-sdk
- description: The modern plugin development platform for Photoshop, replacing the legacy CEP framework. UXP (Unified Extensibility Platform) is powered by a V8 JavaScript engine supporting ES6+ and provides Spectru
  name: Adobe Photoshop UXP Plugin API
  slug: uxp-plugin-api
- description: A modern scripting system for Photoshop that allows developers to execute standalone JavaScript files with the .psjs extension to automate tasks. Unlike full UXP plugins, scripts are single files that
  name: Adobe Photoshop UXP Scripting
  slug: uxp-scripting
- description: 'A specialized plugin type that combines UXP''s JavaScript, HTML, and CSS plugin framework with native C++ code compiled as a .uxpaddon. This allows developers to write performance-critical code in C++ '
  name: Adobe Photoshop UXP Hybrid Plugins
  slug: uxp-hybrid-plugins
- description: A C++ based SDK for building low-level native Photoshop plugins. The SDK enables developers to extend Photoshop in seven categories including filters appearing under the Filter menu, file format impor
  name: Adobe Photoshop C++ Plugin SDK
  slug: cpp-plugin-sdk
- description: The legacy scripting system based on ExtendScript, Adobe's implementation of ECMAScript 3. ExtendScript scripts use the .jsx file extension and can automate nearly all Photoshop operations through a c
  name: Adobe Photoshop ExtendScript Scripting API
  slug: extendscript-scripting
asyncapis:
- description: Event-driven notifications for Adobe Photoshop API asynchronous job processing. When registered through Adobe I/O Events, webhooks deliver real-time notifications when Photoshop API jobs complete or f
  name: Adobe Photoshop API Webhook Events
  slug: adobe-photoshop-api-asyncapi-original
common:
- title: ''
  type: Portal
  url: https://developer.adobe.com/photoshop/
- title: ''
  type: Documentation
  url: https://developer.adobe.com/firefly-services/docs/photoshop/
- title: ''
  type: Documentation
  url: https://developer.adobe.com/photoshop/uxp/2022/
- title: ''
  type: GettingStarted
  url: https://developer.adobe.com/firefly-services/docs/photoshop/getting_started/
- title: ''
  type: Portal
  url: https://developer.adobe.com/developer-console/
- title: ''
  type: APIReference
  url: https://developer.adobe.com/firefly-services/docs/photoshop/api/
- title: ''
  type: Documentation
  url: https://developer.adobe.com/firefly-services/docs/guides/sdks/
- title: ''
  type: GitHubRepository
  url: https://github.com/Firefly-Services/firefly-services-sdk-js
- title: ''
  type: GitHubRepository
  url: https://github.com/AdobeDocs/photoshop-cpp-sdk
- title: ''
  type: Website
  url: https://www.adobe.com/products/photoshop.html
- title: ''
  type: Blog
  url: https://blog.developer.adobe.com/
- title: ''
  type: Forum
  url: https://community.adobe.com/t5/photoshop-ecosystem-discussions/bd-p/photoshop
- title: ''
  type: Forum
  url: https://forums.creativeclouddeveloper.com
- title: ''
  type: Status
  url: https://status.adobe.com/
- title: ''
  type: Security
  url: https://helpx.adobe.com/security/products/photoshop.html
- title: ''
  type: X
  url: https://x.com/Photoshop
- title: ''
  type: YouTube
  url: https://www.youtube.com/@AdobeCreativeCloud
- title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy/policy.html
- title: ''
  type: License
  url: https://www.adobe.com/legal/licenses-terms.html
created: '2025-02-28'
description: Adobe Photoshop is the industry-standard image editing and digital design application. Its developer platform offers a cloud-based REST API for programmatic image processing via Firefly Services, the UXP plugin framework for building desktop extensions with modern JavaScript, a C++ plugin SDK for native filters and file formats, and scripting interfaces for workflow automation.
features:
- description: Process images in the cloud without local Photoshop installation via the REST API.
  name: Cloud Image Processing
- description: AI-powered automatic background removal and mask generation.
  name: Background Removal
- description: Create, read, and modify PSD files including layers, Smart Objects, and text.
  name: PSD Document Editing
- description: AI-powered content generation to fill, extend, or replace image regions.
  name: Generative Fill
- description: Replace embedded Smart Object content across PSD templates programmatically.
  name: Smart Object Replacement
- description: Modify text content, fonts, colors, and styling in PSD text layers.
  name: Text Layer Editing
- description: Run recorded Photoshop Actions (.atn files) on images in the cloud.
  name: Photoshop Actions Execution
- description: Build desktop plugins with modern JavaScript, HTML, CSS, and Spectrum UI components.
  name: UXP Plugin Framework
- description: Create native filters, file format support, and selection tools with the C++ SDK.
  name: C++ Plugin SDK
- description: Legacy scripting interface for batch processing and workflow automation.
  name: ExtendScript Automation
- description: AI-powered automatic cropping to isolate product subjects.
  name: Product Crop
- description: Apply realistic depth-of-field blur effects using AI depth estimation.
  name: Depth Blur
image: /assets/icons/adobe-photoshop.png
integrations:
- description: Native integration with other Creative Cloud apps via shared libraries and cloud storage.
  name: Adobe Creative Cloud
- description: Roundtrip editing between Lightroom and Photoshop for photography workflows.
  name: Adobe Lightroom
- description: Generative AI features powered by Adobe Firefly for content creation.
  name: Adobe Firefly
- description: API supports input/output from AWS S3, Azure Blob, Google Cloud Storage, and Dropbox.
  name: Cloud Storage Providers
jsonld:
- class_count: 16
  name: Adobe Photoshop Context
  property_count: 28
  slug: adobe-photoshop-context
layout: provider
modified: '2026-04-17'
name: Adobe Photoshop
rules:
- name: Adobe Photoshop API Rules
  rule_count: 19
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 3
  slug: adobe-photoshop-spectral-rules
skills: []
slug: adobe-photoshop
solutions:
- description: Cloud-based REST API for programmatic image processing at scale.
  name: Photoshop API (Firefly Services)
- description: Modern plugin platform for extending Photoshop with JavaScript and HTML.
  name: Photoshop Desktop (UXP)
- description: Native plugin SDK for filters, file formats, and performance-critical extensions.
  name: Photoshop Desktop (C++ SDK)
- description: Automation via UXP scripts (.psjs) or legacy ExtendScript (.jsx).
  name: Photoshop Scripting
tags:
- AI/ML
- Creative Cloud
- Image Editing
- Photoshop
- Plugins
- REST API
- Scripting
url: https://raw.githubusercontent.com/api-evangelist/adobe-photoshop/refs/heads/main/apis.yml
use_cases:
- description: Automate background removal, product crop, and image enhancement for e-commerce catalogs.
  name: Product Photography Automation
- description: Replace Smart Objects in PSD templates to generate personalized marketing materials at scale.
  name: Template-Based Design Generation
- description: Process thousands of images with consistent edits using the cloud API or Actions.
  name: Batch Image Processing
- description: Build UXP plugins that add custom panels, automate tasks, and integrate with external services.
  name: Creative Workflow Plugins
- description: Convert between PSD, JPEG, PNG, TIFF, and other formats programmatically.
  name: Image Format Conversion
- description: Use generative fill and AI features to extend, modify, or enhance image content.
  name: Content-Aware Editing
- description: Automate print-ready output generation with proper color spaces and bleed settings.
  name: Print Production Automation
- description: Connect digital asset management systems with Photoshop for automated processing pipelines.
  name: DAM Integration
---
