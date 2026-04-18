---
consumed_apis:
- marketing-content
- marketing-community
description: Unified workflow for content marketers to create rich ad content, manage organization pages, track engagement, and monitor social actions -- combining content APIs and community management.
layout: capability
name: LinkedIn Content And Community
operations:
- description: Create a post.
  method: POST
  name: create-post
  path: /v1/posts
- description: Fetch multiple posts.
  method: GET
  name: get-posts
  path: /v1/posts
- description: Create a share with company mention.
  method: POST
  name: create-share
  path: /v1/shares
- description: Create an ad creative.
  method: POST
  name: create-creative
  path: /v1/creatives
- description: Search for creatives.
  method: GET
  name: search-creatives
  path: /v1/creatives
- description: Create InMail content.
  method: POST
  name: create-inmail-content
  path: /v1/inmail-contents
- description: Create a sponsored conversation.
  method: POST
  name: create-sponsored-conversation
  path: /v1/conversation-ads
- description: Get sponsored conversations.
  method: GET
  name: get-sponsored-conversations
  path: /v1/conversation-ads
- description: Initialize image upload.
  method: POST
  name: initialize-image-upload
  path: /v1/images
- description: Initialize video upload.
  method: POST
  name: initialize-video-upload
  path: /v1/videos
- description: Look up organization by ID.
  method: GET
  name: get-organization-by-id
  path: /v1/organizations/{organization_id}
- description: Retrieve follower statistics.
  method: GET
  name: get-follower-statistics
  path: /v1/follower-statistics
- description: Retrieve page statistics.
  method: GET
  name: get-page-statistics
  path: /v1/page-statistics
personas: []
provider_name: LinkedIn
provider_slug: linkedin
search_terms:
- retrieve inmail content by id.
- business
- retrieve follower statistics.
- get share statistics
- get sponsored conversations.
- manages b2b ad campaigns and audience targeting on linkedin.
- look up organization by id.
- search for creatives.
- get sponsored conversations
- tracks employee learning activity and completions.
- create post
- posts jobs and manages candidates through ats integrations.
- b2b advertising, audience targeting, and campaign analytics.
- get follower count
- create creative
- create a sponsored conversation.
- integrates linkedin authentication and sharing into applications.
- social media
- get notifications
- professional networking
- marketing
- retrieve organization follower count.
- message archiving and regulatory communications governance.
- archives communications for regulatory compliance.
- fetch multiple posts.
- create sponsored conversation
- get follower statistics
- initialize document upload
- get posts
- create a share with company mention.
- recruiting
- create an ad creative.
- initialize image upload.
- retrieve page statistics.
- initialize document upload.
- job posting, recruiting, and applicant tracking.
- initialize video upload.
- get page statistics
- data portability and advertiser transparency for dma.
- employee development tracking and content access.
- get inmail content
- search creatives
- create inmail content
- community management
- initialize image upload
- retrieve share statistics.
- retrieve social action notifications.
- create share
- sales intelligence, lead management, and crm integration.
- create inmail content.
- uses sales navigator for lead generation and crm sync.
- linkedin
- content marketing
- create a post.
- careers
- get organization by id
- initialize video upload
- authentication, sharing, and verification for consumer apps.
slug: content-and-community
tags:
- LinkedIn
- Content Marketing
- Community Management
- Social Media
tools:
- description: Create a post.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-post
- description: Fetch multiple posts.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-posts
- description: Create a share with company mention.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-share
- description: Create an ad creative.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-creative
- description: Search for creatives.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: search-creatives
- description: Create InMail content.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-inmail-content
- description: Retrieve InMail content by ID.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-inmail-content
- description: Create a sponsored conversation.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-sponsored-conversation
- description: Initialize image upload.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: initialize-image-upload
- description: Initialize video upload.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: initialize-video-upload
- description: Initialize document upload.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: initialize-document-upload
- description: Look up organization by ID.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-organization-by-id
- description: Retrieve follower statistics.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-follower-statistics
- description: Retrieve page statistics.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-page-statistics
- description: Retrieve share statistics.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-share-statistics
- description: Retrieve organization follower count.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-follower-count
- description: Retrieve social action notifications.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-notifications
---
