---
consumed_apis:
- graph-api
- instagram-api
- threads-api
description: Workflow capability for managing content across Facebook, Instagram, and Threads. Combines Graph API for Facebook posts, Instagram API for visual content, and Threads API for text-based publishing. Used by social media managers and content creators.
layout: capability
name: Facebook Social Media Management
operations:
- description: Get posts from a user's feed.
  method: GET
  name: list-posts
  path: /v1/posts
- description: Create a new Facebook post.
  method: POST
  name: create-post
  path: /v1/posts
- description: List Instagram media.
  method: GET
  name: list-instagram-media
  path: /v1/instagram-media
- description: Publish Instagram media.
  method: POST
  name: publish-instagram-media
  path: /v1/instagram-media
- description: Create a Threads post.
  method: POST
  name: create-threads-post
  path: /v1/threads
personas: []
provider_name: Facebook
provider_slug: facebook
search_terms:
- content management
- manage advertising campaigns and performance.
- performance tracking and insights.
- get facebook feed
- get instagram performance insights.
- Marketing Manager
- instagram content management.
- create facebook post
- Content Creator
- customer messaging across messenger and whatsapp.
- list instagram media for an account.
- Social Media Manager
- create post
- create a threads post.
- list posts
- create a new threads post.
- get threads performance insights.
- Customer Support
- get instagram insights
- handles customer inquiries via messaging channels.
- create threads post
- manage content across facebook, instagram, and threads.
- direct messaging and customer communication.
- advertising
- manages content and engagement across meta platforms.
- facebook post management.
- messaging
- publish instagram media
- social networking
- Ad Operations
- facebook
- create and publish instagram content.
- publish instagram media.
- publishing
- create instagram media
- creates and publishes visual and text content.
- threads content management.
- content publishing
- create a new facebook post.
- social media
- publishing and managing content across platforms.
- Conversational Commerce
- get threads insights
- list instagram media.
- list instagram media
- get posts from a facebook user's feed.
- plans and executes advertising campaigns.
- campaign management and audience targeting.
- get posts from a user's feed.
- manages day-to-day ad campaign optimization.
slug: social-media-management
tags:
- Facebook
- Social Media
- Content Management
- Publishing
tools:
- description: Get posts from a Facebook user's feed.
  hints:
    readOnly: true
  name: get-facebook-feed
- description: Create a new Facebook post.
  hints:
    readOnly: false
  name: create-facebook-post
- description: List Instagram media for an account.
  hints:
    readOnly: true
  name: list-instagram-media
- description: Create and publish Instagram content.
  hints:
    readOnly: false
  name: create-instagram-media
- description: Get Instagram performance insights.
  hints:
    readOnly: true
  name: get-instagram-insights
- description: Create a new Threads post.
  hints:
    readOnly: false
  name: create-threads-post
- description: Get Threads performance insights.
  hints:
    readOnly: true
  name: get-threads-insights
---
