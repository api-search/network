---
consumed_apis:
- x-users
- x-direct-messages
- x-spaces
description: Unified workflow for managing user relationships, direct messages, spaces, and community interactions on X. Used by community managers, customer support teams, and engagement specialists.
layout: capability
name: X Engagement and Community Management
operations:
- description: Follow a user
  method: POST
  name: followUser
  path: /v1/engagement/users/{id}/following
- description: Unfollow a user
  method: DELETE
  name: unfollowUser
  path: /v1/engagement/users/{source_user_id}/following/{target_user_id}
- description: Block a user
  method: POST
  name: blockUsers
  path: /v1/engagement/users/{id}/blocking
- description: Unblock a user
  method: DELETE
  name: unblockUsers
  path: /v1/engagement/users/{source_user_id}/blocking/{target_user_id}
- description: Mute a user
  method: POST
  name: muteUser
  path: /v1/engagement/users/{id}/muting
- description: Unmute a user
  method: DELETE
  name: unmuteUser
  path: /v1/engagement/users/{source_user_id}/muting/{target_user_id}
- description: Create a new group DM conversation
  method: POST
  name: createDirectMessagesConversation
  path: /v1/engagement/dm/conversations
- description: Send a DM to an existing conversation
  method: POST
  name: createDirectMessagesByConversationId
  path: /v1/engagement/dm/conversations/{dm_conversation_id}/messages
- description: Get recent DM events
  method: GET
  name: getDirectMessagesEvents
  path: /v1/engagement/dm/events
- description: Search for Spaces by keyword
  method: GET
  name: searchSpaces
  path: /v1/engagement/spaces/search
- description: Get multiple Spaces by IDs
  method: GET
  name: getSpacesByIds
  path: /v1/engagement/spaces
personas:
- description: Builds and maintains communities through engagement and moderation.
  id: community-manager
  name: Community Manager
- description: Handles customer inquiries and issues via direct messages and replies.
  id: customer-support
  name: Customer Support
- description: Manages user relationships, follows, and interaction strategies.
  id: engagement-specialist
  name: Engagement Specialist
provider_name: X (Twitter)
provider_slug: twitter
search_terms:
- engagement specialist
- block a user
- microblogging
- get users muted by the authenticated user
- produces original posts, threads, and media content on x.
- manages data pipelines, streaming ingestion, and compliance data flows.
- manage user relationships, direct messages, spaces, and community interactions.
- manage following
- manages user relationships, follows, and interaction strategies.
- get dm events for a specific conversation
- followUser
- search for spaces by keyword
- monitor conversations, search posts, analyze trends, and extract insights.
- getDirectMessagesEvents
- social monitoring, search, trending topics, and sentiment analysis.
- retrieve spaces by ids
- user relationships, direct messaging, spaces, and community interaction.
- create, manage, and analyze posts, media, bookmarks, and lists.
- getMutedUsers
- content
- builds and maintains communities through engagement and moderation.
- get recent dm events for the authenticated user
- streaming
- unblockUsers
- brand manager
- create a new group dm conversation
- platform operations
- social media
- unmuteUser
- create dm conversations
- get dm events
- createDirectMessagesByParticipantId
- post creation, editing, media management, and content analytics.
- createDirectMessagesByConversationId
- compliance officer
- engagement
- muteUser
- getDirectMessagesEventsByConversationId
- send a direct message to an existing conversation
- creates, schedules, and analyzes social media content across platforms.
- community manager
- advertising
- handles customer inquiries and issues via direct messages and replies.
- send a direct message to a user by participant id
- unmute a user
- data engineer
- social media manager
- customer support
- getSpacesByIds
- extracts insights from social data through search, streaming, and analytics.
- get posts shared in a space
- marketing team
- unfollow a user
- retrieve multiple spaces by their ids
- getSpacesPosts
- conducts academic or market research using x data archives.
- unblock a user
- get multiple spaces by ids
- manage mutes
- data analyst
- get users blocked by the authenticated user
- follow a user
- mute a user
- unfollowUser
- searchSpaces
- getBlockedUsers
- monitors brand mentions, sentiment, and competitive landscape.
- manage compliance jobs, data streams, and real-time compliance monitoring.
- real-time data
- manage blocks
- blockUsers
- get recent dm events
- send a dm to an existing conversation
- search spaces
- content creator
- createDirectMessagesConversation
- community
- x api
- researcher
- ensures data handling meets regulatory and platform compliance requirements.
- direct messages
- send dm to a conversation
- manages brand presence, campaigns, and content strategy.
- data compliance, deletion tracking, and regulatory event monitoring.
- spaces
slug: engagement
tags:
- X API
- Engagement
- Community
- Direct Messages
- Spaces
tools:
- description: Follow a user
  hints:
    idempotent: false
    readOnly: false
  name: followUser
- description: Unfollow a user
  hints:
    destructive: true
    readOnly: false
  name: unfollowUser
- description: Block a user
  hints:
    idempotent: false
    readOnly: false
  name: blockUsers
- description: Unblock a user
  hints:
    destructive: true
    readOnly: false
  name: unblockUsers
- description: Get users blocked by the authenticated user
  hints:
    idempotent: true
    readOnly: true
  name: getBlockedUsers
- description: Mute a user
  hints:
    idempotent: false
    readOnly: false
  name: muteUser
- description: Unmute a user
  hints:
    destructive: true
    readOnly: false
  name: unmuteUser
- description: Get users muted by the authenticated user
  hints:
    idempotent: true
    readOnly: true
  name: getMutedUsers
- description: Create a new group DM conversation
  hints:
    idempotent: false
    readOnly: false
  name: createDirectMessagesConversation
- description: Send a direct message to a user by participant ID
  hints:
    idempotent: false
    readOnly: false
  name: createDirectMessagesByParticipantId
- description: Send a direct message to an existing conversation
  hints:
    idempotent: false
    readOnly: false
  name: createDirectMessagesByConversationId
- description: Get recent DM events for the authenticated user
  hints:
    idempotent: true
    readOnly: true
  name: getDirectMessagesEvents
- description: Get DM events for a specific conversation
  hints:
    idempotent: true
    readOnly: true
  name: getDirectMessagesEventsByConversationId
- description: Search for Spaces by keyword
  hints:
    idempotent: true
    readOnly: true
  name: searchSpaces
- description: Retrieve multiple Spaces by their IDs
  hints:
    idempotent: true
    readOnly: true
  name: getSpacesByIds
- description: Get posts shared in a Space
  hints:
    idempotent: true
    readOnly: true
  name: getSpacesPosts
---
