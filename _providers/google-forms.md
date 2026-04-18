---
api_count: 1
apis:
- description: Create and modify Google Forms, read form responses and structure, set up watches for change notifications, and integrate forms with external applications via Cloud Pub/Sub.
  name: Google Forms API v1
  slug: ''
capabilities:
- description: Workflow capability for managing Google Forms - creating forms, collecting responses, and monitoring changes via watches. Used by form administrators and data analysts.
  name: Google Forms Form Management
  slug: form-management
common:
- title: ''
  type: Console
  url: https://console.cloud.google.com/apis/library/forms.googleapis.com
- title: ''
  type: GettingStarted
  url: https://developers.google.com/forms/api/guides
- title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- title: ''
  type: RateLimits
  url: https://developers.google.com/forms/api/guides/quota
- title: ''
  type: Support
  url: https://developers.google.com/forms/api/support
- title: ''
  type: JSON-LD
  url: json-ld/google-forms-api-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/google-forms-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/form-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/google-forms-vocabulary.yaml
created: '2024-01-15'
description: The Google Forms API is a RESTful interface that lets you create and modify Google Forms programmatically, read form responses, set up watches for notifications on form changes and new responses, and integrate forms with external applications.
features:
- description: Programmatically create Google Forms with custom titles and descriptions.
  name: Form Creation
- description: Apply multiple changes to a form in a single API call.
  name: Batch Updates
- description: Read and analyze form responses programmatically.
  name: Response Collection
- description: Receive real-time notifications via Cloud Pub/Sub when forms change or responses are submitted.
  name: Watch Notifications
- description: Create and grade quiz forms with correct answers and scoring.
  name: Quiz Support
- description: Control whether forms are published and accepting responses.
  name: Publish Settings
- description: Support for file upload question types.
  name: File Upload Questions
- description: Support for rating-style questions with customizable icons.
  name: Rating Questions
image: https://www.gstatic.com/images/branding/product/2x/forms_2020q4_48dp.png
integrations:
- description: Automatically link form responses to Google Sheets for analysis.
  name: Google Sheets
- description: Receive real-time notifications about form events via Pub/Sub topics.
  name: Google Cloud Pub/Sub
- description: Store file upload responses in Google Drive.
  name: Google Drive
- description: Integrate with other Google Workspace apps for collaboration.
  name: Google Workspace
jsonld:
- class_count: 5
  name: Google Forms Api Context
  property_count: 17
  slug: google-forms-api-context
layout: provider
modified: '2026-04-18'
name: Google Forms
rules:
- name: Google Forms API Rules
  rule_count: 27
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 10
  slug: google-forms-spectral-rules
skills: []
slug: google-forms
solutions: []
tags:
- Data Collection
- Forms
- Google
- Google Workspace
- Questionnaires
- Responses
- Surveys
url: https://developers.google.com/forms/api
use_cases:
- description: Create and distribute surveys programmatically as part of CRM or marketing workflows.
  name: Automated Survey Distribution
- description: Automatically collect and analyze form responses for reporting dashboards.
  name: Response Analytics
- description: Trigger downstream workflows when new responses are submitted using watches.
  name: Event-Driven Processing
- description: Build automated grading systems for educational quizzes.
  name: Quiz and Assessment Automation
- description: Integrate forms into data collection pipelines for research or operations.
  name: Data Collection Pipelines
---
