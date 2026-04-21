---
consumed_apis:
- instagram-graph
description: Unified workflow for managing Instagram community interactions including comment moderation, replies, hashtag discovery, and mention tracking. Used by community managers and social media teams to engage with followers, moderate comments, discover trending content via hashtags, and monitor brand mentions.
layout: capability
name: Instagram Community Engagement
operations:
- description: Get comments on an Instagram media object.
  method: GET
  name: get-media-comments
  path: /v1/media/{media_id}/comments
- description: Create a comment on an Instagram media object.
  method: POST
  name: create-comment
  path: /v1/media/{media_id}/comments
- description: Get fields on an Instagram comment.
  method: GET
  name: get-comment
  path: /v1/comments/{comment_id}
- description: Hide or unhide a comment on your media.
  method: POST
  name: hide-comment
  path: /v1/comments/{comment_id}
- description: Delete a comment on your media.
  method: DELETE
  name: delete-comment
  path: /v1/comments/{comment_id}
- description: Get replies to a comment.
  method: GET
  name: get-comment-replies
  path: /v1/comments/{comment_id}/replies
- description: Reply to a comment.
  method: POST
  name: create-comment-reply
  path: /v1/comments/{comment_id}/replies
- description: Search for a hashtag by name and get its ID.
  method: GET
  name: search-hashtag
  path: /v1/hashtags/search
- description: Get the most popular media tagged with a specific hashtag.
  method: GET
  name: get-hashtag-top-media
  path: /v1/hashtags/{hashtag_id}/top-media
- description: Get the most recently published media tagged with a specific hashtag.
  method: GET
  name: get-hashtag-recent-media
  path: /v1/hashtags/{hashtag_id}/recent-media
- description: Get IG Media objects where the user has been tagged by other users.
  method: GET
  name: get-user-tags
  path: /v1/users/{user_id}/tags
personas: []
provider_name: Instagram
provider_slug: instagram
search_terms:
- get ig media objects where the user has been tagged by other users.
- community engagement
- search for hashtags.
- comments on a media object.
- create comment reply
- hide comment
- website embedding of instagram content.
- get fields on an instagram comment.
- search hashtag
- instagram
- replies to a comment.
- individual comment operations.
- recent media for a hashtag.
- get user tags
- publishes and manages content across instagram accounts.
- creates and publishes photos, videos, reels, and stories.
- hide or unhide a comment on your media.
- delete a comment on your media.
- meta
- embeds instagram content on websites and applications.
- manages instagram direct conversations for business inquiries.
- get comment replies
- content publishing
- photos
- get media comments
- get the most recently published media tagged with a specific hashtag.
- hashtags
- monitors mentions, comments, and brand sentiment on instagram.
- content publishing and media management.
- get hashtag top media
- media where user was tagged.
- delete comment
- reply to a comment.
- get comment
- mentions
- insights and performance metrics.
- social media
- get comments on an instagram media object.
- videos
- comments
- get the most popular media tagged with a specific hashtag.
- create a comment on an instagram media object.
- get hashtag recent media
- create comment
- tracks content performance and audience insights.
- get replies to a comment.
- search for a hashtag by name and get its id.
- comments, mentions, and community interaction.
- instagram direct messaging.
- top media for a hashtag.
slug: community-engagement
tags:
- Instagram
- Community Engagement
- Social Media
- Comments
- Hashtags
- Mentions
tools:
- description: Get comments on an Instagram media object.
  hints:
    idempotent: true
    readOnly: true
  name: get-media-comments
- description: Create a comment on an Instagram media object.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-comment
- description: Get fields on an Instagram comment.
  hints:
    idempotent: true
    readOnly: true
  name: get-comment
- description: Hide or unhide a comment on your media.
  hints:
    idempotent: true
    readOnly: false
  name: hide-comment
- description: Delete a comment on your media.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-comment
- description: Get replies to a comment.
  hints:
    idempotent: true
    readOnly: true
  name: get-comment-replies
- description: Reply to a comment.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-comment-reply
- description: Search for a hashtag by name and get its ID.
  hints:
    idempotent: true
    readOnly: true
  name: search-hashtag
- description: Get the most popular media tagged with a specific hashtag.
  hints:
    idempotent: true
    readOnly: true
  name: get-hashtag-top-media
- description: Get the most recently published media tagged with a specific hashtag.
  hints:
    idempotent: true
    readOnly: true
  name: get-hashtag-recent-media
- description: Get IG Media objects where the user has been tagged by other users.
  hints:
    idempotent: true
    readOnly: true
  name: get-user-tags
---
