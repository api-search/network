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
- Conversational Commerce
- get threads performance insights.
- plans and executes advertising campaigns.
- handles customer inquiries via messaging channels.
- manages content and engagement across meta platforms.
- social networking
- list instagram media.
- campaign management and audience targeting.
- create post
- manage advertising campaigns and performance.
- get posts from a user's feed.
- advertising
- create a new facebook post.
- create instagram media
- Marketing Manager
- facebook post management.
- get threads insights
- Customer Support
- Ad Operations
- social media
- create and publish instagram content.
- content management
- manages day-to-day ad campaign optimization.
- get facebook feed
- get posts from a facebook user's feed.
- messaging
- direct messaging and customer communication.
- list posts
- facebook
- get instagram insights
- publish instagram media
- get instagram performance insights.
- performance tracking and insights.
- create a new threads post.
- list instagram media for an account.
- create threads post
- list instagram media
- manage content across facebook, instagram, and threads.
- Content Creator
- instagram content management.
- creates and publishes visual and text content.
- Social Media Manager
- customer messaging across messenger and whatsapp.
- create facebook post
- threads content management.
- publishing and managing content across platforms.
- content publishing
- publishing
- create a threads post.
- publish instagram media.
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
