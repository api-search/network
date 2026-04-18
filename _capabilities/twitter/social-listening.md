---
consumed_apis:
- x-posts
- x-streaming
- x-users
description: Unified workflow for monitoring conversations, searching posts, analyzing trends, and extracting insights from X data. Used by data analysts, brand managers, and researchers.
layout: capability
name: X Social Listening and Analytics
operations:
- description: Search posts from last 7 days
  method: POST
  name: searchPostsRecent
  path: /v1/listening/search/recent
- description: Search full archive of posts
  method: POST
  name: searchPostsAll
  path: /v1/listening/search/all
- description: Get counts from last 7 days
  method: GET
  name: getPostsCountsRecent
  path: /v1/listening/counts/recent
- description: Get counts from full archive
  method: GET
  name: getPostsCountsAll
  path: /v1/listening/counts/all
- description: Get post insights for last 28 hours
  method: GET
  name: getInsights28Hr
  path: /v1/listening/insights/28hr
- description: Get historical post insights
  method: GET
  name: getInsightsHistorical
  path: /v1/listening/insights/historical
- description: Stream posts matching filter rules
  method: GET
  name: streamPostsSearch
  path: /v1/listening/streams/search
- description: Add or delete stream rules
  method: POST
  name: addSearchStreamRules
  path: /v1/listening/streams/search/rules
- description: Get current stream rules
  method: GET
  name: getSearchStreamRules
  path: /v1/listening/streams/search/rules
- description: Stream all public posts
  method: GET
  name: streamPostsFirehose
  path: /v1/listening/streams/firehose
- description: Stream 10% sample of posts
  method: GET
  name: streamPostsSample10
  path: /v1/listening/streams/sample10
- description: Retrieve users by IDs
  method: GET
  name: getUsersByIds
  path: /v1/listening/users
- description: Retrieve users by usernames
  method: GET
  name: getUsersByUsernames
  path: /v1/listening/users/by
- description: Get user followers
  method: GET
  name: getFollowers
  path: /v1/listening/users/{id}/followers
- description: Get users being followed
  method: GET
  name: getFollowing
  path: /v1/listening/users/{id}/following
personas:
- description: Extracts insights from social data through search, streaming, and analytics.
  id: data-analyst
  name: Data Analyst
- description: Monitors brand mentions, sentiment, and competitive landscape.
  id: brand-manager
  name: Brand Manager
- description: Conducts academic or market research using X data archives.
  id: researcher
  name: Researcher
provider_name: X (Twitter)
provider_slug: twitter
search_terms:
- getSearchStreamRules
- get counts of posts matching a query from full archive
- handles customer inquiries and issues via direct messages and replies.
- searchPostsRecent
- get posts mentioning a specific user
- real-time data
- data engineer
- monitor conversations, search posts, analyze trends, and extract insights.
- builds and maintains communities through engagement and moderation.
- stream a 10% sample of all public posts in real-time
- retrieve multiple users by their usernames
- look up users by ids
- stream posts matching filtered stream rules in real-time
- social listening
- add or delete rules for the filtered search stream
- retrieve users by ids
- brand manager
- getPostsCountsAll
- social monitoring, search, trending topics, and sentiment analysis.
- getInsightsHistorical
- 10% sample stream
- search full archive of posts
- get followers of a user
- content creator
- compliance officer
- data analyst
- community manager
- streamPostsSample10
- trends
- get posts authored by a specific user
- look up users by usernames
- get current stream rules
- customer support
- streaming
- get counts from last 7 days
- manage user relationships, direct messages, spaces, and community interactions.
- manage compliance jobs, data streams, and real-time compliance monitoring.
- retrieve the authenticated user's profile
- researcher
- search all posts
- stream 10% sample of posts
- get users being followed
- produces original posts, threads, and media content on x.
- search posts from last 7 days
- marketing team
- social media manager
- get counts from full archive
- get followers
- full firehose stream
- searchPostsAll
- content
- getFollowers
- get user followers
- getUserTimeline
- microblogging
- creates, schedules, and analyzes social media content across platforms.
- conducts academic or market research using x data archives.
- advertising
- getUsersMe
- monitors brand mentions, sentiment, and competitive landscape.
- retrieve multiple users by their ids
- social media
- stream all public posts in real-time via the firehose
- search
- get following
- manages brand presence, campaigns, and content strategy.
- get historical post insights
- filtered search stream
- engagement specialist
- streamPostsFirehose
- getFollowing
- create, manage, and analyze posts, media, bookmarks, and lists.
- getPostsCountsRecent
- streamPostsSearch
- manages user relationships, follows, and interaction strategies.
- get users that a user is following
- getInsights28Hr
- get recent post counts
- x api
- ensures data handling meets regulatory and platform compliance requirements.
- get counts of posts matching a query from last 7 days
- add or delete stream rules
- getUsersByIds
- get 28-hour post insights
- get current rules for the filtered search stream
- get post insights for last 28 hours
- retrieve users by usernames
- get post insights for the last 28 hours
- user relationships, direct messaging, spaces, and community interaction.
- getUserMentions
- getUsersByUsernames
- analytics
- extracts insights from social data through search, streaming, and analytics.
- stream all public posts
- post creation, editing, media management, and content analytics.
- addSearchStreamRules
- manage stream filter rules
- search for posts from the last 7 days
- search the full archive of posts
- platform operations
- get all post counts
- stream posts matching filter rules
- search recent posts
- manages data pipelines, streaming ingestion, and compliance data flows.
- data compliance, deletion tracking, and regulatory event monitoring.
slug: social-listening
tags:
- X API
- Social Listening
- Analytics
- Search
- Trends
tools:
- description: Search for posts from the last 7 days
  hints:
    idempotent: true
    readOnly: true
  name: searchPostsRecent
- description: Search the full archive of posts
  hints:
    idempotent: true
    readOnly: true
  name: searchPostsAll
- description: Get counts of posts matching a query from last 7 days
  hints:
    idempotent: true
    readOnly: true
  name: getPostsCountsRecent
- description: Get counts of posts matching a query from full archive
  hints:
    idempotent: true
    readOnly: true
  name: getPostsCountsAll
- description: Get post insights for the last 28 hours
  hints:
    idempotent: true
    readOnly: true
  name: getInsights28Hr
- description: Get historical post insights
  hints:
    idempotent: true
    readOnly: true
  name: getInsightsHistorical
- description: Stream posts matching filtered stream rules in real-time
  hints:
    idempotent: true
    readOnly: true
  name: streamPostsSearch
- description: Add or delete rules for the filtered search stream
  hints:
    idempotent: false
    readOnly: false
  name: addSearchStreamRules
- description: Get current rules for the filtered search stream
  hints:
    idempotent: true
    readOnly: true
  name: getSearchStreamRules
- description: Stream all public posts in real-time via the firehose
  hints:
    idempotent: true
    readOnly: true
  name: streamPostsFirehose
- description: Stream a 10% sample of all public posts in real-time
  hints:
    idempotent: true
    readOnly: true
  name: streamPostsSample10
- description: Retrieve multiple users by their IDs
  hints:
    idempotent: true
    readOnly: true
  name: getUsersByIds
- description: Retrieve multiple users by their usernames
  hints:
    idempotent: true
    readOnly: true
  name: getUsersByUsernames
- description: Retrieve the authenticated user's profile
  hints:
    idempotent: true
    readOnly: true
  name: getUsersMe
- description: Get followers of a user
  hints:
    idempotent: true
    readOnly: true
  name: getFollowers
- description: Get users that a user is following
  hints:
    idempotent: true
    readOnly: true
  name: getFollowing
- description: Get posts authored by a specific user
  hints:
    idempotent: true
    readOnly: true
  name: getUserTimeline
- description: Get posts mentioning a specific user
  hints:
    idempotent: true
    readOnly: true
  name: getUserMentions
---
