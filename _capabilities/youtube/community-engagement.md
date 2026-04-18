---
consumed_apis:
- youtube-data
description: Workflow for managing community interactions including comments, comment threads, subscriptions, and channel management. Designed for community managers, social media teams, and content moderators.
layout: capability
name: YouTube Community Engagement
operations:
- description: List comments
  method: GET
  name: list-comments
  path: /v1/comments
- description: Post a new comment
  method: POST
  name: create-comment
  path: /v1/comments
- description: Update a comment
  method: PUT
  name: update-comment
  path: /v1/comments
- description: Delete a comment
  method: DELETE
  name: delete-comment
  path: /v1/comments
- description: List comment threads
  method: GET
  name: list-comment-threads
  path: /v1/comment-threads
- description: Create a new comment thread
  method: POST
  name: create-comment-thread
  path: /v1/comment-threads
- description: Update a comment thread
  method: PUT
  name: update-comment-thread
  path: /v1/comment-threads
- description: List subscriptions
  method: GET
  name: list-subscriptions
  path: /v1/subscriptions
- description: Subscribe to a channel
  method: POST
  name: subscribe
  path: /v1/subscriptions
- description: Unsubscribe from a channel
  method: DELETE
  name: unsubscribe
  path: /v1/subscriptions
- description: List channels
  method: GET
  name: list-channels
  path: /v1/channels
- description: Update channel settings
  method: PUT
  name: update-channel
  path: /v1/channels
personas: []
provider_name: Youtube
provider_slug: youtube
search_terms:
- post a new comment
- manage comment threads
- list comments on a video or channel
- delete comment
- comments
- update comment
- update an existing comment
- list subscriptions
- set moderation status
- delete a comment
- unsubscribe from channel
- update channel
- update a comment thread
- manage individual comments
- create comment thread
- streaming
- list youtube channels
- set moderation status on comments
- media
- youtube
- update a comment
- list comment threads
- manage channel subscriptions
- moderation
- subscribe
- video
- create comment
- unsubscribe
- list comments
- update comment thread
- unsubscribe from a channel
- videos
- community
- google
- unsubscribe from a youtube channel
- create a new comment thread
- subscribe to channel
- subscribe to a channel
- update channel settings
- social
- subscribe to a youtube channel
- subscriptions
- manage channel information
- list channels
- list channel subscriptions
slug: community-engagement
tags:
- YouTube
- Community
- Comments
- Subscriptions
- Moderation
tools:
- description: List comments on a video or channel
  hints:
    idempotent: true
    readOnly: true
  name: list-comments
- description: Post a new comment
  hints:
    idempotent: false
    readOnly: false
  name: create-comment
- description: Update an existing comment
  hints:
    idempotent: true
    readOnly: false
  name: update-comment
- description: Delete a comment
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-comment
- description: Set moderation status on comments
  hints:
    idempotent: true
    readOnly: false
  name: set-moderation-status
- description: List comment threads
  hints:
    idempotent: true
    readOnly: true
  name: list-comment-threads
- description: Create a new comment thread
  hints:
    idempotent: false
    readOnly: false
  name: create-comment-thread
- description: List channel subscriptions
  hints:
    idempotent: true
    readOnly: true
  name: list-subscriptions
- description: Subscribe to a YouTube channel
  hints:
    idempotent: false
    readOnly: false
  name: subscribe-to-channel
- description: Unsubscribe from a YouTube channel
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: unsubscribe-from-channel
- description: List YouTube channels
  hints:
    idempotent: true
    readOnly: true
  name: list-channels
- description: Update channel settings
  hints:
    idempotent: true
    readOnly: false
  name: update-channel
---
