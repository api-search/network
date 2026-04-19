---
api_count: 1
apis:
- description: The Agrio Agriculture API provides AI-powered plant disease and pest diagnosis from images, plus crop advisory data, credit balance management, and access to a catalog of supported crop types. The Ima
  name: Agrio Agriculture API
  slug: agrio
capabilities:
- description: Unified crop protection capability combining Agrio's AI-powered plant disease diagnosis, pest detection, and crop advisory services. Used by agronomists, crop advisors, and precision agriculture platf
  name: Agrio Crop Protection
  slug: crop-protection
common:
- title: ''
  type: Website
  url: https://agrio.app
- title: ''
  type: Portal
  url: https://pro.agrio.app/image-diagnosis-api
- title: ''
  type: Support
  url: mailto:info@saillog.co
- title: ''
  type: SpectralRules
  url: rules/agrio-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/crop-protection.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/agrio-vocabulary.yaml
created: ''
description: Agrio is a precision plant protection solution that helps growers and crop advisors forecast, identify, and treat plant diseases, pests, and nutrient deficiencies. With Agrio APIs, developers can access AI-powered plant disease diagnosis from images, crop advisory data, weather pattern analysis, pest and disease predictions, and satellite vegetation monitoring to build accurate crop advisory tools.
features:
- description: Computer vision algorithms identify plant diseases, pests, and nutrient deficiencies from uploaded photos with confidence scores.
  name: AI Image Diagnosis
- description: Predictive algorithms forecast disease pressure before or between scouting events to enable proactive intervention.
  name: AgrioShield Pest Prediction
- description: Remote sensing AI detects vegetation issues from satellite data, enabling early detection before visible symptoms appear.
  name: Satellite Imagery Alerts
- description: Returns multiple ranked diagnoses with confidence scores, common names, and scientific names for disambiguation.
  name: Ranked Diagnoses
- description: API usage is metered using a credit system; one credit is consumed per diagnosis request.
  name: Credit-Based Usage
- description: Discoverable catalog of supported crop types for building targeted diagnosis workflows.
  name: Supported Crop Catalog
image: ''
integrations:
- description: Agrio APIs integrate weather pattern data to enhance pest and disease prediction models.
  name: Weather Data Systems
- description: Remote sensing data from satellite providers is used for vegetation monitoring and anomaly detection.
  name: Satellite Imagery Providers
jsonld:
- class_count: 7
  name: Agrio Context
  property_count: 16
  slug: agrio-context
layout: provider
modified: '2026-04-19'
name: agrio
rules:
- name: agrio API Rules
  rule_count: 21
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 11
  slug: agrio-spectral-rules
skills: []
slug: agrio
solutions: []
tags:
- Agriculture
- Plant Disease
- Pest Detection
- AI
- Crop Advisory
url: https://raw.githubusercontent.com/api-evangelist/agrio/refs/heads/main/apis.yml
use_cases:
- description: Embed AI plant disease diagnosis into existing crop advisory and farm management applications.
  name: Crop Advisory Tool Integration
- description: Enable agronomists and farmers to photograph plant symptoms and receive immediate AI-powered diagnosis.
  name: In-Field Disease Identification
- description: Use AgrioShield alerts to notify growers when disease or pest conditions become favorable before visible symptoms appear.
  name: Early Warning Systems
- description: Integrate Agrio diagnosis into precision agriculture platforms for targeted treatment recommendations.
  name: Precision Agriculture Platforms
- description: Access Agrio plant disease data for agricultural research and development of new advisory models.
  name: Research and Development
---
