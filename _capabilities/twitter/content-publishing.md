---
consumed_apis:
- x-posts
- x-media
- x-bookmarks
- x-lists
description: Unified workflow for creating, managing, and analyzing posts, media, bookmarks, and lists on X. Used by social media managers, content creators, and marketing teams.
layout: capability
name: X Content Publishing and Management
operations:
- description: Create a new post
  method: POST
  name: createPosts
  path: /v1/content/posts
- description: Retrieve posts by IDs
  method: GET
  name: getPostsByIds
  path: /v1/content/posts
- description: Delete a post
  method: DELETE
  name: deletePostById
  path: /v1/content/posts/{id}
- description: Get analytics for a post
  method: GET
  name: getPostsAnalytics
  path: /v1/content/posts/{id}/analytics
- description: Upload media for posts
  method: POST
  name: mediaUpload
  path: /v1/content/media/upload
- description: Initialize a chunked media upload
  method: POST
  name: initializeMediaUpload
  path: /v1/content/media/upload/initialize
- description: Finalize a chunked media upload
  method: POST
  name: finalizeMediaUpload
  path: /v1/content/media/upload/finalize
- description: Bookmark a post
  method: POST
  name: createUsersBookmark
  path: /v1/content/users/{id}/bookmarks
- description: Get bookmarked posts
  method: GET
  name: getUsersBookmarks
  path: /v1/content/users/{id}/bookmarks
- description: Create a new list
  method: POST
  name: createLists
  path: /v1/content/lists
- description: Add a member to a list
  method: POST
  name: addListsMember
  path: /v1/content/lists/{id}/members
- description: Get posts from a list timeline
  method: GET
  name: getListsPosts
  path: /v1/content/lists/{id}/posts
personas:
- description: Creates, schedules, and analyzes social media content across platforms.
  id: social-media-manager
  name: Social Media Manager
- description: Produces original posts, threads, and media content on X.
  id: content-creator
  name: Content Creator
- description: Manages brand presence, campaigns, and content strategy.
  id: marketing-team
  name: Marketing Team
provider_name: X (Twitter)
provider_slug: twitter
search_terms:
- social monitoring, search, trending topics, and sentiment analysis.
- real-time data
- getListsMembers
- handles customer inquiries and issues via direct messages and replies.
- createMediaMetadata
- get list posts
- get bookmarked posts
- manage compliance jobs, data streams, and real-time compliance monitoring.
- get bookmarked posts for the authenticated user
- advertising
- media
- manage a specific post
- initializeMediaUpload
- manages user relationships, follows, and interaction strategies.
- x api
- content
- get the members of a list
- social media
- createPosts
- remove a bookmark
- produces original posts, threads, and media content on x.
- delete a post
- delete a post by its id
- post creation, editing, media management, and content analytics.
- manage user relationships, direct messages, spaces, and community interactions.
- get posts from a list's timeline
- getUsersBookmarks
- engagement specialist
- posts
- initialize chunked upload
- monitors brand mentions, sentiment, and competitive landscape.
- create or update metadata (alt text) for uploaded media
- data compliance, deletion tracking, and regulatory event monitoring.
- get a list by its id
- platform operations
- finalizeMediaUpload
- appendMediaUpload
- manage list members
- createUsersBookmark
- compliance officer
- upload media for posts
- get analytics data for a specific post
- create, manage, and analyze posts, media, bookmarks, and lists.
- get the processing status of an uploaded media
- monitor conversations, search posts, analyze trends, and extract insights.
- user relationships, direct messaging, spaces, and community interaction.
- initialize a chunked media upload
- microblogging
- data engineer
- addListsMember
- create a new list on x
- ensures data handling meets regulatory and platform compliance requirements.
- getListsPosts
- deletePostById
- finalize a chunked media upload
- researcher
- retrieve posts by ids
- create a new post (tweet) on x
- getMediaUploadStatus
- get post analytics
- streaming
- upload media for posts (simple upload for small files)
- deleteLists
- getPostsByIds
- create a new list
- data analyst
- get analytics for a post
- create and retrieve posts
- manages brand presence, campaigns, and content strategy.
- content creator
- manages data pipelines, streaming ingestion, and compliance data flows.
- upload media
- add a member to a list
- deleteUsersBookmark
- getListsById
- social media manager
- create a new post
- retrieve multiple posts by their ids
- append a chunk to an in-progress media upload
- marketing team
- marketing
- brand manager
- extracts insights from social data through search, streaming, and analytics.
- mediaUpload
- getPostsAnalytics
- publishing
- bookmark a post
- get posts from a list timeline
- update a list's name or description
- customer support
- creates, schedules, and analyzes social media content across platforms.
- delete a list
- updateLists
- community manager
- builds and maintains communities through engagement and moderation.
- finalize chunked upload
- conducts academic or market research using x data archives.
- create lists
- manage user bookmarks
- createLists
slug: content-publishing
tags:
- X API
- Content
- Publishing
- Posts
- Media
- Marketing
tools:
- description: Create a new post (tweet) on X
  hints:
    idempotent: false
    readOnly: false
  name: createPosts
- description: Retrieve multiple posts by their IDs
  hints:
    idempotent: true
    readOnly: true
  name: getPostsByIds
- description: Delete a post by its ID
  hints:
    destructive: true
    readOnly: false
  name: deletePostById
- description: Get analytics data for a specific post
  hints:
    idempotent: true
    readOnly: true
  name: getPostsAnalytics
- description: Upload media for posts (simple upload for small files)
  hints:
    idempotent: false
    readOnly: false
  name: mediaUpload
- description: Initialize a chunked media upload
  hints:
    idempotent: false
    readOnly: false
  name: initializeMediaUpload
- description: Append a chunk to an in-progress media upload
  hints:
    idempotent: true
    readOnly: false
  name: appendMediaUpload
- description: Finalize a chunked media upload
  hints:
    idempotent: false
    readOnly: false
  name: finalizeMediaUpload
- description: Get the processing status of an uploaded media
  hints:
    idempotent: true
    readOnly: true
  name: getMediaUploadStatus
- description: Create or update metadata (alt text) for uploaded media
  hints:
    idempotent: true
    readOnly: false
  name: createMediaMetadata
- description: Bookmark a post
  hints:
    idempotent: false
    readOnly: false
  name: createUsersBookmark
- description: Get bookmarked posts for the authenticated user
  hints:
    idempotent: true
    readOnly: true
  name: getUsersBookmarks
- description: Remove a bookmark
  hints:
    destructive: true
    readOnly: false
  name: deleteUsersBookmark
- description: Create a new list on X
  hints:
    idempotent: false
    readOnly: false
  name: createLists
- description: Get a list by its ID
  hints:
    idempotent: true
    readOnly: true
  name: getListsById
- description: Update a list's name or description
  hints:
    idempotent: true
    readOnly: false
  name: updateLists
- description: Add a member to a list
  hints:
    idempotent: false
    readOnly: false
  name: addListsMember
- description: Get the members of a list
  hints:
    idempotent: true
    readOnly: true
  name: getListsMembers
- description: Get posts from a list's timeline
  hints:
    idempotent: true
    readOnly: true
  name: getListsPosts
- description: Delete a list
  hints:
    destructive: true
    readOnly: false
  name: deleteLists
---
