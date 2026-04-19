---
api_count: 19
apis:
- description: Access Apple Music catalog, user library, and playback controls.
  name: Apple Music API
  slug: ''
- description: Access weather forecasts, current conditions, and historical weather data.
  name: WeatherKit REST API
  slug: ''
- description: Automate tasks for App Store Connect and access app metadata.
  name: App Store Connect API
  slug: ''
- description: Embed interactive Apple Maps on websites.
  name: MapKit JS
  slug: ''
- description: Integrate Sign in with Apple authentication.
  name: Sign in with Apple REST API
  slug: ''
- description: Send push notifications to iOS, macOS, watchOS, and tvOS devices.
  name: Apple Push Notification Service (APNs)
  slug: ''
- description: Manage customer App Store transactions from your server, including in-app purchases and subscriptions.
  name: App Store Server API
  slug: ''
- description: Receive real-time notifications about in-app purchase events and subscription lifecycle changes.
  name: App Store Server Notifications V2
  slug: ''
- description: Server-side geocoding, reverse geocoding, search, and estimated time of arrival using Apple Maps.
  name: Apple Maps Server API
  slug: ''
- description: Publish, manage, update, and delete Apple News Format articles.
  name: Apple News API
  slug: ''
- description: Reduce fraudulent use of your services by managing device state and asserting app integrity.
  name: DeviceCheck API
  slug: ''
- description: Create, manage, and report on Apple Search Ads campaigns programmatically.
  name: Apple Ads Campaign Management API
  slug: ''
- description: Create, distribute, and update passes for the Apple Wallet app via a web service.
  name: Wallet Passes Web Service
  slug: ''
- description: Automate management of users, roles, provisioning profiles, and bundle identifiers for enterprise apps.
  name: Enterprise Program API
  slug: ''
- description: Automate device management actions and access data about devices enrolled via Automated Device Enrollment.
  name: Apple School and Business Manager API
  slug: ''
- description: Accept Apple Pay payments on your website using JavaScript-based APIs.
  name: Apple Pay on the Web
  slug: ''
- description: Create, distribute, and update orders in Apple Wallet for order tracking.
  name: Wallet Orders
  slug: ''
- description: Declare educational activities supported by your app for use with Apple Schoolwork.
  name: ClassKit Catalog API
  slug: ''
- description: Access the Apple Music catalog metadata in bulk for albums, songs, and artists.
  name: Apple Music Feed API
  slug: ''
capabilities:
- description: Unified workflow for managing the Apple app lifecycle including app metadata, builds, TestFlight beta testing, and beta group management. Used by app developers and release managers.
  name: Apple App Lifecycle
  slug: app-lifecycle
common:
- title: ''
  type: DeveloperPortal
  url: https://developer.apple.com
- title: ''
  type: TermsOfService
  url: https://developer.apple.com/terms/
- title: ''
  type: PrivacyPolicy
  url: https://www.apple.com/legal/privacy/
- title: ''
  type: Support
  url: https://developer.apple.com/support/
- title: ''
  type: Blog
  url: https://developer.apple.com/news/
- title: ''
  type: StatusPage
  url: https://developer.apple.com/system-status/
- title: ''
  type: SignUp
  url: https://developer.apple.com/programs/enroll/
- title: ''
  type: Pricing
  url: https://developer.apple.com/support/compare-memberships/
- title: ''
  type: GitHubOrganization
  url: https://github.com/apple
- title: ''
  type: YouTube
  url: https://developer.apple.com/videos/
- title: ''
  type: ChangeLog
  url: https://developer.apple.com/documentation/updates
- title: ''
  type: Authentication
  url: https://developer.apple.com/documentation/appstoreconnectapi/generating-tokens-for-api-requests
- title: ''
  type: Tutorials
  url: https://developer.apple.com/tutorials/
- title: ''
  type: CodeExamples
  url: https://developer.apple.com/sample-code/
- title: ''
  type: SDK
  url: https://developer.apple.com/download/
- title: ''
  type: Contact
  url: https://developer.apple.com/contact/
- title: ''
  type: JSONLD
  url: json-ld/apple-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/apple-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/app-lifecycle.yaml
created: '2024-01-15'
description: Collection of Apple's public APIs and developer resources.
features:
- description: Automate app management, TestFlight, submissions, and analytics through a comprehensive REST API.
  name: App Store Connect
- description: Accept payments seamlessly on web and in apps with secure tokenized transactions.
  name: Apple Pay
- description: Send real-time notifications to billions of Apple devices across iOS, macOS, watchOS, and tvOS.
  name: Push Notifications
- description: Privacy-focused authentication that lets users sign in without sharing personal information.
  name: Sign in with Apple
- description: Embed interactive maps and perform server-side geocoding with Apple Maps infrastructure.
  name: MapKit and Maps Server
- description: Access hyper-local weather forecasts, conditions, and historical data worldwide.
  name: WeatherKit
- description: Integrate Apple Music catalog, user library, and playback into apps and websites.
  name: MusicKit
image: https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png
integrations:
- description: Full IDE integration for building, testing, and deploying apps across all Apple platforms.
  name: Xcode
- description: Beta testing platform for distributing pre-release builds to internal and external testers.
  name: TestFlight
- description: View app performance metrics, downloads, and user engagement data.
  name: App Analytics
- description: Store and sync app data across devices using Apple's cloud infrastructure.
  name: CloudKit
jsonld:
- class_count: 0
  name: App Store Connect Context
  property_count: 0
  slug: app-store-connect-context
- class_count: 2
  name: Apple Context
  property_count: 9
  slug: apple-context
layout: provider
modified: '2026-04-18'
name: Apple
rules:
- name: Apple API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: apple-spectral-rules
skills: []
slug: apple
solutions: []
tags:
- Developer
- iOS
- macOS
- Mobile
- Technology
url: https://developer.apple.com
use_cases:
- description: Automate app submissions, manage TestFlight beta testing, and handle app metadata at scale.
  name: App Distribution
- description: Manage subscriptions, consumables, and transaction history with server-side verification.
  name: In-App Purchases
- description: Automate device enrollment and management for schools and businesses at scale.
  name: Enterprise Device Management
- description: Publish and manage articles in Apple News with rich media and analytics.
  name: Content Publishing
- description: Build location-aware applications with geocoding, routing, and interactive maps.
  name: Location Services
---
