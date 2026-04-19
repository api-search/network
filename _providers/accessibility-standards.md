---
api_count: 6
apis:
- description: The current stable web accessibility standard published by the W3C Accessibility Guidelines Working Group (AG WG). WCAG 2.2 comprises 13 guidelines organized under four principles (perceivable, operab
  name: Web Content Accessibility Guidelines (WCAG) 2.2
  slug: ''
- description: Accessible Rich Internet Applications (WAI-ARIA) 1.2 is a W3C Recommendation (June 2023) that defines semantic attributes enabling assistive technologies to interpret dynamic web content and complex i
  name: WAI-ARIA 1.2
  slug: ''
- description: 'ATAG 2.0 is a W3C Recommendation that defines standards for making authoring tools (CMSes, code editors, web-based tools) accessible to authors with disabilities, and for helping those tools generate '
  name: Authoring Tool Accessibility Guidelines (ATAG) 2.0
  slug: ''
- description: UAAG 2.0 is a W3C standard for browsers, browser extensions, media players, and other user agents that render web content. It defines how user agents should make web content accessible to users with d
  name: User Agent Accessibility Guidelines (UAAG) 2.0
  slug: ''
- description: Section 508 of the Rehabilitation Act requires U.S. federal agencies to ensure their information and communication technology (ICT) is accessible to people with disabilities. The Revised 508 Standards
  name: Section 508
  slug: ''
- description: ACT Rules Format 1.1 (W3C Recommendation, February 2026) establishes a standardized format for documenting accessibility conformance testing rules. The framework supports automated, semi-automated, an
  name: Accessibility Conformance Testing (ACT) Rules Format 1.1
  slug: ''
common:
- title: ''
  type: Website
  url: https://www.w3.org/WAI/standards-guidelines/
- title: W3C GitHub Organization
  type: GitHubOrganization
  url: https://github.com/w3c
- title: W3C Accessibility Evaluation Tools List
  type: Tools
  url: https://www.w3.org/WAI/test-evaluate/tools/list/
- title: axe-core Accessibility Testing Engine
  type: Tools
  url: https://github.com/dequelabs/axe-core
- title: Pa11y Automated Accessibility Testing
  type: Tools
  url: https://github.com/pa11y/pa11y
- title: Accessibility Standards JSON-LD Context
  type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/json-ld/accessibility-standards-context.jsonld
- title: Accessibility Standards Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/vocabulary/accessibility-standards-vocabulary.yaml
created: '2025-01-01'
description: Guidelines and technical specifications that ensure digital content, applications, and technologies are usable by people with disabilities, including standards like WCAG, Section 508, and ARIA. These standards help organizations meet regulatory requirements and demonstrate accountability to stakeholders.
features:
- description: Standards requiring that information and user interface components be presentable to users in ways they can perceive, including text alternatives for non-text content.
  name: Perceivable Content
- description: Standards ensuring that user interface components and navigation are operable, including keyboard accessibility and sufficient time limits.
  name: Operable Interface
- description: Standards ensuring that information and the operation of the user interface is understandable, including readable text and predictable navigation.
  name: Understandable Information
- description: Standards requiring that content be robust enough to be reliably interpreted by a wide variety of user agents, including assistive technologies.
  name: Robust Technology
- description: Three-tiered conformance model (Level A, AA, AAA) providing graduated accessibility requirements for organizations to target.
  name: Conformance Levels
- description: ACT Rules Framework providing standardized, machine-readable rules for automated accessibility conformance testing.
  name: Automated Testing Rules
image: /assets/icons/accessibility-standards.png
integrations:
- description: Open-source accessibility testing engine by Deque Systems implementing WCAG 2.0/2.1/2.2 rules, integrates with browsers, testing frameworks, and CI tools.
  name: axe-core
- description: Open-source Node.js tool for automated accessibility testing against WCAG standards, integrates with GitHub Actions and CI/CD pipelines.
  name: Pa11y
- description: GSA's Government-wide IT Accessibility Program providing guidance, training, and resources for federal Section 508 compliance.
  name: Section508.gov
- description: European standard referencing WCAG 2.1 AA, applicable to public and private sector digital services in EU member states.
  name: EU Accessibility Act / EN 301 549
- description: International Standards Organization adoption of WCAG 2.2, enabling global regulatory alignment with the W3C standard.
  name: ISO/IEC 40500:2025
jsonld:
- class_count: 7
  name: Accessibility Standards Context
  property_count: 24
  slug: accessibility-standards-context
layout: provider
modified: '2026-04-19'
name: Accessibility Standards
skills: []
slug: accessibility-standards
solutions: []
tags:
- Accessibility
- Compliance
- UX
- Web Standards
- WCAG
- ARIA
- Section 508
- Disability
url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/apis.yml
use_cases:
- description: Using WCAG 2.2 success criteria and ACT rules to audit web applications for accessibility compliance.
  name: Web Application Accessibility Auditing
- description: Applying Section 508 standards when procuring or developing information and communication technology for U.S. federal agencies.
  name: Federal Government ICT Procurement
- description: Using WAI-ARIA attributes to make dynamic JavaScript-driven interfaces accessible to screen readers and assistive technologies.
  name: Accessible Rich Internet Application Development
- description: Integrating axe-core or Pa11y into continuous integration pipelines to catch accessibility regressions automatically.
  name: Automated CI/CD Accessibility Testing
- description: Producing Voluntary Product Accessibility Templates (VPATs) and Accessibility Conformance Reports aligned with Section 508 and WCAG.
  name: Regulatory Compliance Documentation
---
