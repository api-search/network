---
api_count: 5
apis:
- description: Learning Management System API for managing courses, learners, and learning content.
  name: Adobe Captivate Prime API
  slug: ''
- description: API for SCORM-compliant content delivery and tracking.
  name: Adobe Captivate SCORM API
  slug: ''
- description: Experience API for tracking learning experiences.
  name: Adobe Captivate xAPI (Tin Can API)
  slug: ''
- description: API for collaborative review and commenting on eLearning projects.
  name: Adobe Captivate Review API
  slug: ''
- description: Webhooks API for Adobe Learning Manager that enables real-time event notifications for learner activities, course completions, enrollments, and other learning management events.
  name: Adobe Learning Manager Webhooks API
  slug: ''
asyncapis:
- description: The Adobe Learning Manager Webhooks API enables real-time event notifications for learning management activities. When configured, Adobe Learning Manager sends HTTP POST requests to registered webhook
  name: Adobe Learning Manager Webhooks API
  slug: adobe-captivate-learning-manager-webhooks-asyncapi
capabilities:
- description: Unified workflow capability for managing learning objects, enrollments, completions, and compliance tracking using Adobe Learning Manager APIs. Designed for L&D administrators and HR integration devel
  name: Adobe Captivate Learning Management
  slug: learning-management
common:
- title: ''
  type: Support
  url: https://helpx.adobe.com/support/captivate.html
- title: ''
  type: Community
  url: https://community.adobe.com/t5/adobe-captivate/ct-p/ct-captivate
- title: ''
  type: Blog
  url: https://elearning.adobe.com/
- title: ''
  type: StatusPage
  url: https://status.adobe.com/
- title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy.html
- title: ''
  type: Contact
  url: https://www.adobe.com/products/captivate/contact.html
- title: ''
  type: Portal
  url: https://experienceleague.adobe.com/docs/learning-manager/using/introduction.html
- title: ''
  type: GettingStarted
  url: https://experienceleague.adobe.com/docs/learning-manager/using/getting-started/getting-started.html
- title: ''
  type: Documentation
  url: https://experienceleague.adobe.com/docs/learning-manager/using/home.html
- title: ''
  type: Console
  url: https://developer.adobe.com/console/
- title: ''
  type: ChangeLog
  url: https://experienceleague.adobe.com/docs/learning-manager/using/whats-new.html
- title: ''
  type: Website
  url: https://business.adobe.com/products/learning-manager/adobe-learning-manager.html
- title: ''
  type: Login
  url: https://learningmanager.adobe.com/
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AdobeELearning
- title: ''
  type: GitHubOrganization
  url: https://github.com/adobe
- title: ''
  type: JSONSchema
  url: json-schema/adobe-captivate-learning-object-schema.json
- title: ''
  type: JSON-LD
  url: json-ld/adobe-captivate-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/adobe-captivate-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/learning-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/adobe-captivate-vocabulary.yaml
- title: ''
  type: JSON-LD
  url: json-ld/adobe-captivate-learning-manager-webhooks-context.jsonld
- title: ''
  type: JSON-LD
  url: json-ld/adobe-captivate-prime-api-context.jsonld
created: '2024-01-20'
description: Adobe Captivate is an eLearning authoring tool used to create responsive eLearning content, software demonstrations, and interactive training modules.
features:
- description: Create and manage courses, learning programs, certifications, and job aids with full CRUD operations via REST API.
  name: Learning Object Management
- description: Programmatically enroll learners, track progress, and retrieve completion status across all learning objects.
  name: Learner Enrollment and Tracking
- description: Receive real-time HTTP POST notifications for enrollment, completion, badge, and certification events.
  name: Webhook Event Notifications
- description: Manage gamification points, leaderboards, and badge awards to motivate learners.
  name: Gamification and Badges
- description: Organize and expose learning content through catalogs with filtering and tagging capabilities.
  name: Catalog Management
- description: Associate skills with learning content and track learner skill attainment through the API.
  name: Skill Tracking
- description: Secure API access using OAuth 2.0 with role-based scopes for admin, learner, manager, and author roles.
  name: OAuth 2.0 Authentication
- description: Deliver and track SCORM-compliant and xAPI (Tin Can) learning content for LMS interoperability.
  name: SCORM and xAPI Support
- description: Use the Jobs API to import and export users, enrollments, and completion data in bulk.
  name: Bulk Data Import/Export
- description: Manage announcements and notifications sent to learners, managers, and administrators.
  name: Notification Management
image: /assets/icons/adobe-captivate.png
integrations:
- description: Sync learner data and completion status between Adobe Learning Manager and Salesforce CRM.
  name: Salesforce
- description: Surface learning content and notifications directly within Microsoft Teams via connector.
  name: Microsoft Teams
- description: Import organizational user data from Workday HCM to manage learner accounts automatically.
  name: Workday
- description: Bi-directional sync with SAP SuccessFactors for user provisioning and learning record exchange.
  name: SAP SuccessFactors
- description: Embed learning content and catalogs within Adobe Experience Manager sites.
  name: Adobe Experience Manager
- description: Schedule and launch virtual classroom sessions directly from Adobe Learning Manager.
  name: Zoom
- description: Import LinkedIn Learning content into Adobe Learning Manager catalogs for blended learning.
  name: LinkedIn Learning
- description: Host and launch SCORM content packages through SCORM Cloud integration.
  name: SCORM Cloud
jsonld:
- class_count: 0
  name: Adobe Captivate Context
  property_count: 16
  slug: adobe-captivate-context
- class_count: 5
  name: Adobe Captivate Learning Manager Webhooks Context
  property_count: 9
  slug: adobe-captivate-learning-manager-webhooks-context
- class_count: 45
  name: Adobe Captivate Prime Api Context
  property_count: 80
  slug: adobe-captivate-prime-api-context
layout: provider
modified: '2026-04-19'
name: Adobe Captivate
rules:
- name: Adobe Captivate API Rules
  rule_count: 34
  severity_counts:
    error: 16
    hint: 0
    info: 4
    warn: 14
  slug: adobe-captivate-spectral-rules
skills: []
slug: adobe-captivate
solutions: []
tags:
- Authoring
- Education
- eLearning
- LMS
- SCORM
- Training
- xAPI
url: https://raw.githubusercontent.com/api-evangelist/adobe-captivate/refs/heads/main/apis.yml
use_cases:
- description: Automatically provision users from HRIS systems like Workday or SAP SuccessFactors into Adobe Learning Manager.
  name: HR System Integration
- description: Build branded training portals that surface Adobe Learning Manager content through the REST API.
  name: Custom Learning Portal
- description: Auto-enroll new hires in mandatory compliance courses and track completion for regulatory reporting.
  name: Compliance Training Automation
- description: Extract learner progress and completion data to build custom analytics and reporting dashboards.
  name: Learning Analytics Dashboard
- description: Integrate course purchases with e-commerce platforms and auto-enroll paying customers.
  name: E-Commerce Integration
- description: Use webhooks to monitor learner activity in real time and trigger downstream workflows on completion.
  name: Real-Time Progress Monitoring
- description: Automate certification enrollment, renewal reminders, and expiry tracking using the REST API.
  name: Certification Management
---
