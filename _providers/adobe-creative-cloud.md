---
api_count: 17
apis:
- description: The Adobe Firefly API provides programmatic access to generative AI capabilities for image creation and manipulation. Key endpoints include text-to-image generation, generative fill for inpainting mas
  name: Adobe Firefly API
  slug: firefly-api
- description: A JavaScript SDK for embedding Adobe Express creative editing tools directly into web applications. The SDK provides a full editor component for design creation, quick actions for common image and vid
  name: Adobe Express Embed SDK
  slug: express-embed-sdk
- description: A REST API for accessing and managing Creative Cloud Libraries, enabling synchronization of colors, character styles, paragraph styles, graphics, and other creative assets across Adobe applications an
  name: Creative Cloud Libraries API
  slug: cc-libraries-api
- description: A REST API for managing files, folders, and projects in Adobe Creative Cloud cloud storage. The API supports creating and organizing projects with hierarchical folder structures, uploading and downloa
  name: Adobe Cloud Storage and Collaboration API
  slug: cloud-storage-api
- description: A REST API for searching, licensing, and integrating Adobe Stock assets including photos, vectors, illustrations, videos, templates, and 3D content into applications and workflows. The Search API enab
  name: Adobe Stock API
  slug: stock-api
- description: The Adobe Fonts API (formerly Typekit API) provides programmatic access to Adobe's font library for web and application integration. The API supports querying font family information and variations, c
  name: Adobe Fonts API
  slug: fonts-api
- description: A cloud-based REST API for creating, converting, and manipulating PDF documents programmatically. Part of Adobe Acrobat Services, the API supports PDF creation from HTML, images, and Office formats, c
  name: Adobe PDF Services API
  slug: pdf-services-api
- description: A REST API for generating PDF and Word documents by merging JSON data into Microsoft Word templates. Part of Adobe Acrobat Services, the API supports conditional content insertion, dynamic table gener
  name: Adobe Document Generation API
  slug: document-generation-api
- description: A REST API for creating and managing electronic signature workflows programmatically. The API supports document upload, agreement creation with configurable signing flows, real-time status tracking vi
  name: Acrobat Sign API
  slug: acrobat-sign-api
- description: Adobe I/O Events provides an event-driven webhook infrastructure for subscribing to changes across Adobe services. Developers register webhook endpoints to receive real-time HTTP POST notifications wh
  name: Adobe I/O Events
  slug: io-events
- description: A serverless computing platform built on Apache OpenWhisk that enables developers to deploy and execute custom code on Adobe's cloud infrastructure. I/O Runtime supports event-driven and HTTP-triggere
  name: Adobe I/O Runtime
  slug: io-runtime
- description: A complete application development framework for building custom enterprise applications on Adobe infrastructure. App Builder combines Adobe I/O Runtime for serverless backend functions, Adobe I/O Eve
  name: Adobe App Builder
  slug: app-builder
- description: The Unified Extensibility Platform (UXP) is Adobe's modern cross-app plugin development framework replacing the legacy CEP platform. UXP uses a JavaScript engine with support for ES6+ and provides a c
  name: Adobe UXP (Unified Extensibility Platform)
  slug: uxp
- description: 'The Common Extensibility Platform (CEP) is Adobe''s legacy framework for building integrated HTML5 panels across multiple Creative Cloud desktop applications. CEP panels use HTML5, CSS, and JavaScript '
  name: Adobe CEP (Common Extensibility Platform)
  slug: cep
- description: A cloud-based REST API that provides programmatic access to Photoshop's image editing capabilities without requiring a local installation. Part of Adobe Firefly Services, the API supports PSD document
  name: Adobe Photoshop API
  slug: photoshop-api
- description: A REST API for managing photos, albums, and applying presets in Adobe Lightroom, enabling automated photo organization and editing workflows. The API provides programmatic access to Lightroom's cloud-
  name: Adobe Lightroom API
  slug: lightroom-api
- description: 'The Adobe Developer Distribution portal for publishing and managing plugins and extensions in the Creative Cloud Marketplace and Adobe Exchange. Supports UXP plugins, CEP extensions (ZXP format), and '
  name: Adobe Developer Distribution
  slug: developer-distribution
asyncapis:
- description: 'Adobe I/O Events enables developers to receive near-real-time notifications when events occur across Adobe products and services. Events are delivered via webhooks or journaling (pull-based polling). '
  name: Adobe I/O Events
  slug: adobe-io-events-asyncapi-original
common:
- title: ''
  type: Portal
  url: https://developer.adobe.com/
- title: ''
  type: Portal
  url: https://developer.adobe.com/creative-cloud/
- title: ''
  type: Documentation
  url: https://developer.adobe.com/apis
- title: ''
  type: Portal
  url: https://developer.adobe.com/developer-console/
- title: ''
  type: Authentication
  url: https://developer.adobe.com/developer-console/docs/guides/authentication/
- title: ''
  type: Authentication
  url: https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/
- title: ''
  type: Website
  url: https://www.adobe.com/creativecloud.html
- title: ''
  type: Blog
  url: https://blog.developer.adobe.com/
- title: ''
  type: Blog
  url: https://medium.com/adobetech
- title: ''
  type: Forum
  url: https://forums.creativeclouddeveloper.com
- title: ''
  type: Forum
  url: https://community.adobe.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/adobe
- title: ''
  type: GitHubOrganization
  url: https://github.com/AdobeDocs
- title: ''
  type: GitHubOrganization
  url: https://github.com/Adobe-CEP
- title: ''
  type: Support
  url: https://developer.adobe.com/support/
- title: ''
  type: Pricing
  url: https://developer.adobe.com/document-services/pricing/main/
- title: ''
  type: Status
  url: https://status.adobe.com/
- title: ''
  type: Documentation
  url: https://developer.adobe.com/adobe-status/
- title: ''
  type: Security
  url: https://helpx.adobe.com/security.html
- title: ''
  type: X
  url: https://x.com/AdobeDevs
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
created: '2025-02-26'
description: Adobe Creative Cloud is a suite of software and cloud services for graphic design, video editing, web development, photography, and 3D content creation. Its developer platform provides APIs for generative AI via Firefly Services, cloud storage and asset management, PDF document processing, electronic signatures, stock asset licensing, font delivery, and embeddable creative tools via the Express Embed SDK.
features:
- description: Generate images from text prompts, fill masked regions, and expand images using Adobe Firefly AI models.
  name: Generative AI Image Creation
- description: Create, convert, extract, compress, OCR, and protect PDF documents programmatically.
  name: PDF Document Processing
- description: Create and manage electronic signature workflows with Acrobat Sign for agreement lifecycle management.
  name: Electronic Signatures
- description: Search, preview, and license photos, vectors, videos, and templates from Adobe Stock.
  name: Stock Asset Licensing
- description: Sync colors, styles, graphics, and design assets across Adobe applications and custom integrations.
  name: Creative Cloud Libraries
- description: Manage files, folders, and projects in Creative Cloud cloud storage with collaboration.
  name: Cloud Storage
- description: Access and deliver Adobe Fonts (formerly Typekit) for web and application typography.
  name: Font Delivery
- description: Embed Adobe Express editor and quick actions in web applications via the Embed SDK.
  name: Embeddable Creative Tools
- description: Build extensions for Photoshop, InDesign, Illustrator, and other CC apps using UXP or CEP.
  name: Plugin Development
- description: Subscribe to real-time notifications for changes across Adobe services via I/O Events.
  name: Event-Driven Webhooks
- description: Automate Photoshop and Lightroom operations in the cloud without local installations.
  name: Cloud Image Processing
- description: Generate PDFs and Word documents by merging JSON data into templates.
  name: Document Generation
image: /assets/icons/adobe-creative-cloud.png
integrations:
- description: PDF Services integration with Word, Excel, and PowerPoint for document conversion.
  name: Microsoft Office
- description: Acrobat Sign integration with Salesforce for electronic signature workflows in CRM.
  name: Salesforce
- description: Acrobat Sign integration with Workday for HR document signing workflows.
  name: Workday
- description: Integration with AEM, Analytics, and Target for enterprise content management.
  name: Adobe Experience Cloud
- description: Acrobat Sign notifications and signing workflows within Slack channels.
  name: Slack
- description: Open-source SDKs and documentation repositories for developer integration.
  name: GitHub
jsonld:
- class_count: 18
  name: Adobe Creative Cloud Context
  property_count: 43
  slug: adobe-creative-cloud-context
layout: provider
modified: '2026-04-17'
name: Adobe Creative Cloud
rules:
- name: Adobe Creative Cloud API Rules
  rule_count: 20
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 4
  slug: adobe-creative-cloud-spectral-rules
skills: []
slug: adobe-creative-cloud
solutions:
- description: Complete suite of 20+ creative applications with API access for desktop and cloud workflows.
  name: Creative Cloud All Apps
- description: Generative AI APIs combining Firefly, Photoshop, and Lightroom for cloud image processing.
  name: Adobe Firefly Services
- description: PDF Services, Document Generation, and Acrobat Sign APIs for document workflow automation.
  name: Adobe Acrobat Services
- description: Full-stack application framework for building custom enterprise extensions on Adobe infrastructure.
  name: Adobe App Builder
tags:
- AI/ML
- Cloud
- Creative
- Design
- Documents
- Photography
- SaaS
- Video
url: https://raw.githubusercontent.com/api-evangelist/adobe-creative-cloud/refs/heads/main/apis.yml
use_cases:
- description: Automate image generation, editing, and processing workflows using Firefly and Photoshop APIs.
  name: Creative Asset Automation
- description: Generate, convert, sign, and archive documents using PDF Services and Acrobat Sign.
  name: Document Workflow Automation
- description: Use Firefly generative fill and Photoshop background removal for product photography automation.
  name: E-commerce Product Images
- description: Sync brand colors, fonts, and assets across teams using Creative Cloud Libraries API.
  name: Brand Asset Management
- description: Generate personalized visual content at scale using Firefly text-to-image for marketing campaigns.
  name: Content Personalization
- description: Automate PDF creation, compression, and accessibility tagging for digital publication workflows.
  name: Digital Publishing
- description: Create, send, sign, and track electronic agreements with Acrobat Sign API integration.
  name: Contract Management
- description: Embed Adobe Stock search and licensing into content management and publishing platforms.
  name: Stock Asset Integration
---
