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
- Ad Operations
- Customer Support
- Marketing Manager
- advertising
- create a new threads post.
- manages day-to-day ad campaign optimization.
- get posts from a facebook user's feed.
- get threads performance insights.
- content management
- publish instagram media
- direct messaging and customer communication.
- publish instagram media.
- Conversational Commerce
- customer messaging across messenger and whatsapp.
- messaging
- performance tracking and insights.
- list posts
- get facebook feed
- facebook post management.
- plans and executes advertising campaigns.
- list instagram media.
- get threads insights
- create a threads post.
- get instagram performance insights.
- manages content and engagement across meta platforms.
- creates and publishes visual and text content.
- content publishing
- create a new facebook post.
- campaign management and audience targeting.
- manage advertising campaigns and performance.
- instagram content management.
- create post
- get instagram insights
- get posts from a user's feed.
- social networking
- Content Creator
- list instagram media for an account.
- create and publish instagram content.
- publishing
- facebook
- threads content management.
- create instagram media
- publishing and managing content across platforms.
- list instagram media
- social media
- create facebook post
- Social Media Manager
- manage content across facebook, instagram, and threads.
- handles customer inquiries via messaging channels.
- create threads post
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
