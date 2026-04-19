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
- messaging
- social media
- Conversational Commerce
- facebook post management.
- Ad Operations
- create a threads post.
- create facebook post
- advertising
- get threads performance insights.
- publishing
- manage content across facebook, instagram, and threads.
- social networking
- manages day-to-day ad campaign optimization.
- get instagram insights
- handles customer inquiries via messaging channels.
- create threads post
- Marketing Manager
- threads content management.
- create and publish instagram content.
- get threads insights
- get facebook feed
- create a new facebook post.
- direct messaging and customer communication.
- get instagram performance insights.
- Content Creator
- manage advertising campaigns and performance.
- publish instagram media.
- creates and publishes visual and text content.
- campaign management and audience targeting.
- publishing and managing content across platforms.
- get posts from a user's feed.
- list instagram media.
- plans and executes advertising campaigns.
- performance tracking and insights.
- content publishing
- list instagram media
- create a new threads post.
- facebook
- manages content and engagement across meta platforms.
- Social Media Manager
- create instagram media
- list posts
- instagram content management.
- content management
- Customer Support
- list instagram media for an account.
- get posts from a facebook user's feed.
- publish instagram media
- create post
- customer messaging across messenger and whatsapp.
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
