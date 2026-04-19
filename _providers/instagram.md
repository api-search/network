---
api_count: 4
apis:
- description: The Instagram API with Instagram Login enables access to Instagram Business and Creator accounts using Instagram native login flow. Supports media management, content publishing, comment handling, men
  name: Instagram API with Instagram Login
  slug: instagram-api-with-instagram-login
- description: The Instagram API with Facebook Login accesses Instagram Business and Creator accounts linked to Facebook Pages. Enables media retrieval and publishing, comment management, mention identification, has
  name: Instagram API with Facebook Login
  slug: instagram-api-with-facebook-login
- description: 'The Messenger API support for Instagram consolidates Instagram and Facebook Page messaging into a unified platform. Enables businesses and creators to manage conversations, send and receive messages, '
  name: Instagram Messaging API
  slug: instagram-messaging-api
- description: The Instagram oEmbed endpoint returns HTML and metadata for embedding Instagram photos, videos, reels, and carousels on third-party websites using the standard oEmbed protocol.
  name: Instagram oEmbed API
  slug: instagram-oembed-api
capabilities:
- description: Unified workflow for Instagram analytics and insights including account-level metrics, media-level performance data, user profile analysis, and competitor research via business discovery. Used by mark
  name: Instagram Analytics And Insights
  slug: analytics-and-insights
- description: Unified workflow for managing Instagram community interactions including comment moderation, replies, hashtag discovery, and mention tracking. Used by community managers and social media teams to enga
  name: Instagram Community Engagement
  slug: community-engagement
- description: Unified workflow for managing Instagram content including media browsing, publishing (container creation and publish), stories, carousel albums, and media updates. Used by social media managers and co
  name: Instagram Content Management
  slug: content-management
common:
- title: ''
  type: Portal
  url: https://developers.facebook.com/docs/instagram-platform
- title: ''
  type: GettingStarted
  url: https://developers.facebook.com/docs/instagram-api/getting-started
- title: ''
  type: Authentication
  url: https://developers.facebook.com/docs/instagram-api/overview#authentication
- title: ''
  type: TermsOfService
  url: https://developers.facebook.com/terms
- title: ''
  type: PrivacyPolicy
  url: https://www.facebook.com/privacy/explanation
- title: ''
  type: StatusPage
  url: https://developers.facebook.com/status/
- title: ''
  type: ChangeLog
  url: https://developers.facebook.com/docs/instagram-api/changelog
- title: ''
  type: Support
  url: https://developers.facebook.com/support
- title: ''
  type: Blog
  url: https://developers.facebook.com/blog/
- title: ''
  type: GitHubOrganization
  url: https://github.com/fbsamples
created: '2024-01-01'
description: Instagram is a photo and video sharing social networking platform owned by Meta. The Instagram APIs allow developers to build integrations with Instagram Business and Creator accounts for content publishing, media management, comment moderation, hashtag discovery, insights and analytics, messaging, and embedding. Available through the Meta Developer Platform with Facebook Login or Instagram Login authentication.
features:
- description: Publish photos, videos, reels, carousels, and stories to Instagram Business and Creator accounts programmatically.
  name: Content Publishing
- description: Retrieve, manage, and organize published media including photos, videos, stories, and albums.
  name: Media Management
- description: Read, reply to, hide, and delete comments on Instagram media for brand safety and engagement.
  name: Comment Moderation
- description: Search for hashtags and discover top and recent media associated with specific hashtags.
  name: Hashtag Discovery
- description: Identify and retrieve media where your account has been mentioned by other Instagram users.
  name: Mention Tracking
- description: Access account-level and media-level metrics for reach, impressions, engagement, and audience demographics.
  name: Insights and Analytics
- description: Send and receive messages through Instagram Direct for customer service and business communication.
  name: Instagram Direct Messaging
- description: Publish ephemeral story content including photos and videos that disappear after 24 hours.
  name: Stories Publishing
- description: Create and publish short-form video content as Instagram Reels.
  name: Reels Publishing
- description: Embed Instagram posts, reels, and videos on third-party websites using the standard oEmbed protocol.
  name: oEmbed
- description: Receive real-time notifications for comments, mentions, messages, and story insights via webhooks.
  name: Webhooks
- description: Send private direct messages in response to public comments on your Instagram media.
  name: Private Replies
image: /assets/icons/instagram.png
integrations:
- description: Unified management of Instagram and Facebook content, messaging, and advertising through the Meta platform.
  name: Facebook
- description: Centralized dashboard for managing Instagram and Facebook business accounts, content, and insights.
  name: Meta Business Suite
- description: Cross-platform messaging through Meta unified messaging infrastructure.
  name: WhatsApp
- description: Real-time event notifications for comments, mentions, messages, and story insights.
  name: Webhooks
jsonld:
- class_count: 11
  name: Instagram Graph Api Context
  property_count: 37
  slug: instagram-graph-api-context
layout: provider
modified: '2026-04-17'
name: Instagram
rules:
- name: Instagram API Rules
  rule_count: 20
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 4
  slug: instagram-spectral-rules
skills: []
slug: instagram
solutions:
- description: Native Instagram authentication for Business and Creator accounts with full API access.
  name: Instagram API with Instagram Login
- description: Facebook Page-linked authentication for Instagram Business accounts with hashtag discovery.
  name: Instagram API with Facebook Login
- description: Unified messaging across Instagram Direct and Facebook Messenger for business communication.
  name: Instagram Messaging
- description: oEmbed and embed tools for displaying Instagram content on third-party websites.
  name: Instagram Embedding
tags:
- Instagram
- Meta
- Photos
- Social Media
- Videos
- Content Publishing
url: https://raw.githubusercontent.com/api-evangelist/instagram/refs/heads/main/apis.yml
use_cases:
- description: Automate content publishing, scheduling, and media management across Instagram accounts.
  name: Social Media Management
- description: Track mentions, comments, and hashtags to monitor brand sentiment and engagement.
  name: Brand Monitoring
- description: Manage Instagram Direct conversations for customer support and business inquiries.
  name: Customer Service
- description: Retrieve insights and metrics for measuring content performance and audience growth.
  name: Analytics and Reporting
- description: Discover and curate content through hashtag search and mention tracking.
  name: Content Curation
- description: Connect product catalogs and shopping features with Instagram content for social commerce.
  name: E-commerce Integration
- description: Track creator account metrics, media performance, and audience insights for influencer campaigns.
  name: Influencer Marketing
- description: Embed Instagram posts, reels, and galleries on websites and blogs using oEmbed.
  name: Website Embedding
---
