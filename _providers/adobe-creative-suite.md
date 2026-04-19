---
api_count: 16
apis:
- description: The Adobe Photoshop API provides programmatic access to Photoshop image manipulation capabilities including automated editing, masking, and compositing. It enables developers to integrate Photoshop pr
  name: Adobe Photoshop API
  slug: photoshop-api
- description: The Adobe Lightroom API provides access to photo management features including albums, collections, and editing presets stored in the Lightroom cloud catalog. Developers can use it to build integratio
  name: Adobe Lightroom API
  slug: lightroom-api
- description: 'The Adobe Illustrator API enables programmatic creation and manipulation of vector graphics through scripting and plugin interfaces. It exposes the Illustrator object model so developers can automate '
  name: Adobe Illustrator API
  slug: illustrator-api
- description: The Adobe InDesign API allows developers to automate document layout and publishing workflows through scripting and UXP plugins. It exposes InDesign's document model for tasks such as batch exporting,
  name: Adobe InDesign API
  slug: indesign-api
- description: The Adobe Premiere Pro API gives developers access to video editing automation through scripting and panel extensions. It allows integration with external media asset management systems, automated seq
  name: Adobe Premiere Pro API
  slug: premiere-pro-api
- description: 'The Adobe After Effects API enables scripting and plugin development for motion graphics and visual effects workflows. Developers can automate rendering, manipulate compositions programmatically, and '
  name: Adobe After Effects API
  slug: after-effects-api
- description: 'The Adobe Creative Cloud Libraries API provides access to shared design assets stored in Creative Cloud Libraries, including colors, character styles, graphics, and components. It allows applications '
  name: Adobe Creative Cloud Libraries API
  slug: creative-cloud-libraries-api
- description: 'The Adobe Stock API enables search, licensing, and retrieval of stock photos, illustrations, vectors, videos, and templates from the Adobe Stock marketplace. It supports both editorial and commercial '
  name: Adobe Stock API
  slug: stock-api
- description: 'The Adobe Firefly API provides access to Adobe''s generative AI capabilities for creating and editing images, vectors, and text effects from natural language prompts. It is built on the Firefly family '
  name: Adobe Firefly API
  slug: firefly-api
- description: The Adobe PDF Services API provides cloud-based tools for creating, converting, combining, compressing, and extracting content from PDF documents. It is part of the Adobe Acrobat Services platform and
  name: Adobe PDF Services API
  slug: pdf-services-api
- description: The Adobe Analytics API provides programmatic access to Adobe Analytics report suites for retrieving, segmenting, and analyzing web and app behavioral data. It supports both the Reporting API for quer
  name: Adobe Analytics API
  slug: analytics-api
- description: The Adobe Experience Manager Assets API provides access to the AEM digital asset management system for uploading, retrieving, and managing assets stored in AEM as a Cloud Service. It enables integrati
  name: Adobe Experience Manager Assets API
  slug: experience-manager-assets-api
- description: The Adobe Acrobat Sign API enables sending, tracking, and managing electronic signature agreements programmatically. It supports creating agreements from documents or templates, managing signers and r
  name: Adobe Acrobat Sign API
  slug: acrobat-sign-api
- description: The Adobe Fonts API provides access to the Adobe Fonts library for discovering and embedding web fonts in applications and websites. It allows querying font families, retrieving font metadata, and gen
  name: Adobe Fonts API
  slug: fonts-api
- description: The Adobe Express Embed SDK allows developers to embed Adobe Express editing capabilities directly into their own web applications. It provides a customizable in-app editing experience for images, vid
  name: Adobe Express Embed SDK
  slug: express-embed-sdk
- description: Adobe UXP (Unified Extensibility Platform) is the modern plugin and scripting platform used across Adobe creative applications including Photoshop, InDesign, Illustrator, and XD. It provides a JavaScr
  name: Adobe UXP
  slug: uxp
capabilities:
- description: 'AI-powered content generation workflow using Adobe Firefly for creating images, videos, and visual variations from text prompts. Used by content creators, marketers, and designers who need to rapidly '
  name: Adobe AI Content Generation
  slug: ai-content-generation
- description: End-to-end creative asset production workflow combining AI content generation (Firefly), image editing and manipulation (Photoshop), and stock asset sourcing and licensing (Stock). Used by creative di
  name: Adobe Creative Production
  slug: creative-production
- description: PDF document lifecycle management workflow using Adobe PDF Services for creating, converting, combining, compressing, OCR processing, accessibility tagging, and template-based document generation. Use
  name: Adobe Document Management
  slug: document-management
- description: Automated image editing and processing workflow using the Adobe Photoshop API for background removal, masking, layer management, rendition creation, document operations, and smart object editing. Used
  name: Adobe Image Editing
  slug: image-editing
- description: Stock asset discovery, licensing, and management workflow using the Adobe Stock API. Used by content curators, marketing teams, and creative directors to search for stock photos, illustrations, vector
  name: Adobe Stock Asset Sourcing
  slug: stock-asset-sourcing
common:
- title: ''
  type: JSON-LD
  url: json-ld/adobe-creative-suite-context.jsonld
- title: ''
  type: JSONSchema
  url: json-schema/adobe-creative-suite-image-job-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/adobe-creative-suite-firefly-generation-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/adobe-creative-suite-stock-file-schema.json
- title: ''
  type: Portal
  url: https://developer.adobe.com/
- title: ''
  type: SignUp
  url: https://developer.adobe.com/console/home
- title: ''
  type: GettingStarted
  url: https://developer.adobe.com/developer-console/docs/guides/getting-started/
- title: ''
  type: Documentation
  url: https://developer.adobe.com/developer-console/docs/
- title: ''
  type: Blog
  url: https://blog.developer.adobe.com/
- title: ''
  type: GitHub Organization
  url: https://github.com/adobe
- title: ''
  type: Community
  url: https://community.adobe.com/t5/developers/ct-p/developers
- title: ''
  type: Stack Overflow
  url: https://stackoverflow.com/questions/tagged/adobe
- title: ''
  type: Console
  url: https://developer.adobe.com/console/
- title: ''
  type: Authentication
  url: https://developer.adobe.com/developer-console/docs/guides/authentication/
- title: ''
  type: ChangeLog
  url: https://developer.adobe.com/developer-console/docs/release-notes/
- title: ''
  type: Support
  url: https://developer.adobe.com/support/
- title: ''
  type: StatusPage
  url: https://status.adobe.com/
- title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy.html
created: '2024-01-01'
description: Adobe Creative Suite is a collection of professional software applications for graphic design, video editing, web development, and photography.
features:
- description: Photoshop and Lightroom APIs for cloud-based image editing, background removal, and rendition generation.
  name: Cloud Image Processing
- description: Adobe Firefly API for text-to-image generation, generative fill, and style transfer.
  name: Generative AI
- description: Create, convert, extract, compress, and protect PDF documents programmatically.
  name: PDF Document Services
- description: Acrobat Sign API for creating and managing electronic signature workflows.
  name: Electronic Signatures
- description: Search, preview, and license photos, vectors, and videos from Adobe Stock.
  name: Stock Asset Licensing
- description: Sync colors, styles, and design assets across Adobe applications.
  name: Creative Cloud Libraries
- description: Adobe Fonts API for web font delivery and typography management.
  name: Font Delivery
- description: Premiere Pro and After Effects scripting for video production automation.
  name: Video Editing Automation
- description: Illustrator scripting for vector artwork creation and batch processing.
  name: Vector Graphics Automation
- description: InDesign Server and scripting for document layout automation.
  name: Desktop Publishing
- description: Adobe Express Embed SDK for integrating creative editing into web apps.
  name: Embeddable Creative Tools
- description: UXP framework for building modern plugins across Creative Cloud apps.
  name: Plugin Development
image: /assets/icons/adobe-creative-suite.png
integrations: []
jsonld:
- class_count: 56
  name: Adobe Creative Suite Context
  property_count: 99
  slug: adobe-creative-suite-context
layout: provider
modified: '2026-04-17'
name: Adobe Creative Suite
rules:
- name: Adobe Creative Suite API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: adobe-creative-suite-spectral-rules
skills: []
slug: adobe-creative-suite
solutions:
- description: Complete suite of 20+ creative applications with API access.
  name: Adobe Creative Cloud
- description: Generative AI APIs combining Firefly, Photoshop, and Lightroom.
  name: Adobe Firefly Services
- description: PDF Services, Document Generation, and Acrobat Sign APIs.
  name: Adobe Acrobat Services
- description: Embeddable creative tools with quick actions and templates.
  name: Adobe Express
tags:
- Creative
- Design
- Graphics
- Photography
- Video
url: https://raw.githubusercontent.com/api-evangelist/adobe-creative-suite/refs/heads/main/apis.yml
use_cases:
- description: Automate background removal, cropping, and enhancement for e-commerce.
  name: Product Photography Automation
- description: Generate personalized visual content using Firefly and template automation.
  name: Content Personalization at Scale
- description: PDF creation, conversion, signing, and archiving workflows.
  name: Document Workflow Automation
- description: Centralize brand assets in Creative Cloud Libraries for consistent usage.
  name: Brand Asset Management
- description: Automate video editing, rendering, and export with Premiere Pro APIs.
  name: Video Production Pipeline
- description: Automate layout, typesetting, and print-ready output with InDesign.
  name: Print Production
- description: Generate icon sets, components, and design tokens from data.
  name: Design System Generation
- description: Export optimized SVGs, images, and fonts for web applications.
  name: Web Asset Pipeline
---
