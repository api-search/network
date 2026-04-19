---
api_count: 1
apis:
- description: RESTful API for Amazon Location Service operations including maps, places, routes, geofences, trackers, and device position management for location-aware applications.
  name: Amazon Location Service REST API
  slug: ''
capabilities:
- description: Unified workflow capability for Amazon Location Service combining resource management and operations.
  name: Amazon Location Service Workflow
  slug: amazon-location-service-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Portal
  url: https://aws.amazon.com/location/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/location/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/mobile/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/location/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
- title: ''
  type: Status
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Knowledge Center
  url: https://repost.aws/knowledge-center
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: Stack Overflow
  url: https://stackoverflow.com/questions/tagged/amazon-location-service
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-location-service-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-location-service-workflow.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-location-service-vocabulary.yaml
created: '2024-01-15'
description: Amazon Location Service provides location-based services including maps, places, routes, trackers, and geofences, enabling developers to add location functionality to applications securely and cost-effectively.
features:
- description: Render interactive maps with customizable styles using vector tiles and raster tiles.
  name: Maps
- description: Search for addresses, points of interest, and geographic coordinates.
  name: Places Search
- description: Calculate optimal routes with turn-by-turn directions and estimated travel time.
  name: Route Calculation
- description: Create virtual boundaries and detect when tracked devices enter or exit those areas.
  name: Geofencing
- description: Track the real-time position of assets, vehicles, and people.
  name: Asset Tracking
- description: Data does not leave AWS infrastructure, keeping location data private and secure.
  name: Data Privacy
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Authenticate map and location requests using Cognito identity pools.
  name: Amazon Cognito
- description: Ingest device location data from IoT Core into Location Service tracking.
  name: AWS IoT Core
- description: Trigger events when geofences are entered or exited via EventBridge.
  name: Amazon EventBridge
- description: Use HERE maps and location data as a data provider within Location Service.
  name: HERE Technologies
- description: Access Esri basemaps and location data through Amazon Location Service.
  name: Esri
jsonld:
- class_count: 2
  name: Amazon Location Service Context
  property_count: 7
  slug: amazon-location-service-context
layout: provider
modified: '2026-04-19'
name: Amazon Location Service
rules:
- name: Amazon Location Service API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 7
  slug: amazon-location-service-spectral-rules
skills: []
slug: amazon-location-service
solutions: []
tags:
- AWS
- Geocoding
- Geofencing
- Location
- Maps
- Routing
url: https://aws.amazon.com/location/
use_cases:
- description: Track vehicle fleets in real time and optimize routes for delivery efficiency.
  name: Fleet Management
- description: Build store locators and proximity-based search for retail applications.
  name: Store Locator
- description: Send notifications when assets enter or exit defined geographic boundaries.
  name: Geofence Alerts
- description: Embed interactive maps in web and mobile applications.
  name: Map Visualization
---
