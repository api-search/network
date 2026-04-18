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
- get instagram insights
- get facebook feed
- create and publish instagram content.
- manages day-to-day ad campaign optimization.
- Customer Support
- customer messaging across messenger and whatsapp.
- create threads post
- list instagram media.
- publish instagram media.
- create post
- Ad Operations
- get instagram performance insights.
- get threads insights
- get posts from a facebook user's feed.
- creates and publishes visual and text content.
- social media
- create instagram media
- instagram content management.
- facebook post management.
- manages content and engagement across meta platforms.
- plans and executes advertising campaigns.
- manage advertising campaigns and performance.
- Conversational Commerce
- handles customer inquiries via messaging channels.
- get threads performance insights.
- get posts from a user's feed.
- social networking
- Marketing Manager
- list posts
- content management
- publish instagram media
- content publishing
- threads content management.
- create facebook post
- Content Creator
- messaging
- campaign management and audience targeting.
- direct messaging and customer communication.
- Social Media Manager
- create a threads post.
- performance tracking and insights.
- manage content across facebook, instagram, and threads.
- facebook
- advertising
- publishing
- publishing and managing content across platforms.
- create a new facebook post.
- list instagram media
- list instagram media for an account.
- create a new threads post.
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
