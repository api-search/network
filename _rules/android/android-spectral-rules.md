---
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Android.
layout: rules
name: Android API Rules
provider_name: Android
provider_slug: android
rule_count: 7
rules:
- description: Info title must be present
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/android-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/android/refs/heads/main/rules/android-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: android-spectral-rules
tags:
- AI
- Android
- Automotive
- Google
- Machine Learning
- Mobile Development
- SDK
- TV
- Wearables
- Spectral
- Linting
- API Governance
---
