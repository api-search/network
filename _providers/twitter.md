---
api_count: 3
apis:
- description: The core X API providing programmatic access to posts, users, spaces, lists, direct messages, bookmarks, likes, reposts, follows, blocks, mutes, trends, communities, and compliance data. Supports post
  name: X API
  slug: x-api
- description: 'The X Ads API enables programmatic management of advertising campaigns on the X platform including campaign creation and scheduling, custom audience building, creative management (draft posts, cards, '
  name: X Ads API
  slug: x-ads-api
- description: The X Activity API provides real-time activity event subscriptions with sub-second delivery via streaming or webhooks. Subscribe to profile updates, follows, likes, reposts, and other user activity ev
  name: X Activity API
  slug: x-activity-api
capabilities:
- description: Unified workflow for managing compliance jobs, data streams, and real-time compliance monitoring on X. Used by compliance officers, data engineers, and platform operations.
  name: X Compliance and Data Management
  slug: compliance-and-data
- description: Unified workflow for creating, managing, and analyzing posts, media, bookmarks, and lists on X. Used by social media managers, content creators, and marketing teams.
  name: X Content Publishing and Management
  slug: content-publishing
- description: Unified workflow for managing user relationships, direct messages, spaces, and community interactions on X. Used by community managers, customer support teams, and engagement specialists.
  name: X Engagement and Community Management
  slug: engagement
- description: Unified workflow for monitoring conversations, searching posts, analyzing trends, and extracting insights from X data. Used by data analysts, brand managers, and researchers.
  name: X Social Listening and Analytics
  slug: social-listening
common:
- title: ''
  type: Portal
  url: https://developer.x.com/en/portal/dashboard
- title: ''
  type: GettingStarted
  url: https://docs.x.com/x-api/getting-started/make-your-first-request
- title: ''
  type: Console
  url: https://developer.x.com/en/portal/dashboard
- title: ''
  type: SignUp
  url: https://developer.x.com/en/portal/petition/essential/basic-info
- title: ''
  type: Authentication
  url: https://docs.x.com/resources/fundamentals/authentication
- title: Python XDK
  type: SDK
  url: https://docs.x.com/sdks-and-tools/python-xdk
- title: TypeScript XDK
  type: SDK
  url: https://docs.x.com/sdks-and-tools/typescript-xdk
- title: xurl
  type: CLI
  url: https://docs.x.com/sdks-and-tools/xurl
- title: ''
  type: Pricing
  url: https://developer.x.com/en/portal/petition/essential/basic-info
- title: ''
  type: TermsOfService
  url: https://developer.x.com/en/developer-terms/agreement-and-policy
- title: ''
  type: PrivacyPolicy
  url: https://x.com/en/privacy
- title: ''
  type: StatusPage
  url: https://api.twitterstat.us/
- title: ''
  type: Support
  url: https://devcommunity.x.com/
- title: ''
  type: Blog
  url: https://blog.x.com/developer
- title: ''
  type: ReleaseNotes
  url: https://docs.x.com/changelog
- title: ''
  type: GitHubOrganization
  url: https://github.com/xdevplatform
- title: ''
  type: GitHubRepository
  url: https://github.com/xdevplatform/xdk-python
- title: ''
  type: GitHubRepository
  url: https://github.com/xdevplatform/xdk-typescript
- title: ''
  type: GitHubRepository
  url: https://github.com/xdevplatform/xurl
- title: ''
  type: GitHubRepository
  url: https://github.com/xdevplatform/xdk
- title: ''
  type: GitHubRepository
  url: https://github.com/xdevplatform/twitter-api-java-sdk
- title: ''
  type: GitHubRepository
  url: https://github.com/xdevplatform/twitter-ruby-ads-sdk
- title: ''
  type: Tools
  url: https://github.com/xdevplatform/xmcp
- title: ''
  type: Sandbox
  url: https://github.com/xdevplatform/playground
- title: ''
  type: CodeExamples
  url: https://github.com/xdevplatform/samples
- title: ''
  type: CodeExamples
  url: https://github.com/xdevplatform/xchat-bot-python
- title: ''
  type: PostmanWorkspace
  url: https://docs.x.com/sdks-and-tools/postman
- title: ''
  type: PostmanCollection
  url: postman/x-api-v2-postman-collection.json
- title: ''
  type: X
  url: https://x.com/XDevelopers
created: '2025-07-29'
description: X (formerly Twitter) is a social media platform providing APIs for accessing and integrating with posts, users, spaces, direct messages, lists, media, trends, and real-time streaming data. The X API enables developers to build applications that read and write X data, manage advertising campaigns, and subscribe to real-time activity events. Available through pay-per-use credit-based pricing with enterprise options for high-volume access.
features:
- description: Create, delete, edit, repost, quote, like, and bookmark posts programmatically.
  name: Post Management
- description: Access filtered streams, sampled streams, firehose, and language-specific streams for real-time post data.
  name: Real-Time Streaming
- description: Search the complete archive of public posts with advanced query operators and date filtering.
  name: Full-Archive Search
- description: Look up users by ID or username, manage follows, blocks, mutes, and retrieve user metrics.
  name: User Lookup and Management
- description: Discover and look up live audio Spaces with host, speaker, and listener data.
  name: Spaces
- description: Send and receive direct messages, create conversations, and manage participants.
  name: Direct Messages
- description: Create, manage, and query lists including membership, followers, and pinned lists.
  name: Lists
- description: Access personalized and geographic trending topics.
  name: Trends
- description: Upload images, videos, and large files using chunked upload with metadata and subtitle support.
  name: Media Upload
- description: Access compliance streams and batch jobs for data deletion and user protection events.
  name: Compliance
- description: Access community data and community notes for collaborative fact-checking.
  name: Communities and Community Notes
- description: Programmatically create, schedule, and manage advertising campaigns with targeting and budget controls.
  name: Ad Campaign Management
image: https://abs.twimg.com/favicons/twitter.ico
integrations:
- description: Official Postman collections for exploring and testing X API endpoints interactively.
  name: Postman
- description: Integration with AI tools and agents through Model Context Protocol servers.
  name: MCP Servers
- description: Real-time event delivery via webhooks for the Activity API.
  name: Webhook Delivery
jsonld:
- class_count: 23
  name: X Api Context
  property_count: 118
  slug: x-api-context
layout: provider
modified: '2026-04-17'
name: X (Twitter)
rules:
- name: X (Twitter) API Rules
  rule_count: 53
  severity_counts:
    error: 17
    hint: 0
    info: 18
    warn: 18
  slug: twitter-spectral-rules
skills: []
slug: twitter
solutions:
- description: Credit-based pricing with no commitments. Pay only for what you use with access to core X API endpoints.
  name: X API Pay-Per-Use
- description: High-volume access with custom rate limits, dedicated account management, full firehose, and premium support.
  name: X API Enterprise
- description: Advertising platform API for campaign management, audience targeting, creative management, and analytics.
  name: X Ads API
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
url: https://raw.githubusercontent.com/api-evangelist/twitter/refs/heads/main/apis.yml
use_cases:
- description: Monitor brand mentions, sentiment, and conversations in real-time using filtered streams and search endpoints.
  name: Social Listening
- description: Automate post creation, scheduling, and thread publishing for social media management platforms.
  name: Content Publishing
- description: Retrieve post metrics, user engagement data, and campaign performance for business intelligence.
  name: Analytics and Reporting
- description: Build automated accounts that respond to mentions, post updates, or provide customer service.
  name: Bot Development
- description: Access full-archive search and streaming data for social media research and trend analysis.
  name: Research and Academic Analysis
- description: Programmatically manage ad campaigns, audiences, creatives, and bidding strategies at scale.
  name: Advertising Automation
- description: Track live events, breaking news, and trending topics with streaming APIs and trend endpoints.
  name: Real-Time Event Monitoring
- description: Manage followers, lists, and direct messages for community engagement and moderation.
  name: Community Management
---
