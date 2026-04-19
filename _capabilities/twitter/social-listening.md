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
- social listening
- manages user relationships, follows, and interaction strategies.
- get users that a user is following
- brand manager
- get counts from full archive
- addSearchStreamRules
- get recent post counts
- content creator
- streamPostsSample10
- getPostsCountsRecent
- get post insights for last 28 hours
- get counts of posts matching a query from full archive
- get current stream rules
- get posts mentioning a specific user
- real-time data
- social monitoring, search, trending topics, and sentiment analysis.
- filtered search stream
- search the full archive of posts
- data engineer
- user relationships, direct messaging, spaces, and community interaction.
- getFollowing
- builds and maintains communities through engagement and moderation.
- get posts authored by a specific user
- get following
- streamPostsFirehose
- streaming
- search all posts
- manage user relationships, direct messages, spaces, and community interactions.
- look up users by ids
- monitor conversations, search posts, analyze trends, and extract insights.
- stream all public posts
- content
- search recent posts
- getUserMentions
- creates, schedules, and analyzes social media content across platforms.
- getInsights28Hr
- get historical post insights
- streamPostsSearch
- getSearchStreamRules
- produces original posts, threads, and media content on x.
- compliance officer
- get post insights for the last 28 hours
- search for posts from the last 7 days
- getUsersByUsernames
- get counts of posts matching a query from last 7 days
- data compliance, deletion tracking, and regulatory event monitoring.
- manage compliance jobs, data streams, and real-time compliance monitoring.
- stream 10% sample of posts
- searchPostsAll
- social media manager
- get followers of a user
- searchPostsRecent
- get all post counts
- retrieve multiple users by their ids
- stream posts matching filter rules
- getUserTimeline
- getPostsCountsAll
- getUsersMe
- retrieve users by ids
- add or delete stream rules
- get user followers
- manages data pipelines, streaming ingestion, and compliance data flows.
- search posts from last 7 days
- engagement specialist
- trends
- get 28-hour post insights
- full firehose stream
- stream posts matching filtered stream rules in real-time
- handles customer inquiries and issues via direct messages and replies.
- extracts insights from social data through search, streaming, and analytics.
- marketing team
- monitors brand mentions, sentiment, and competitive landscape.
- 10% sample stream
- retrieve multiple users by their usernames
- ensures data handling meets regulatory and platform compliance requirements.
- social media
- retrieve the authenticated user's profile
- getUsersByIds
- conducts academic or market research using x data archives.
- advertising
- create, manage, and analyze posts, media, bookmarks, and lists.
- analytics
- stream a 10% sample of all public posts in real-time
- getInsightsHistorical
- data analyst
- customer support
- get current rules for the filtered search stream
- researcher
- stream all public posts in real-time via the firehose
- retrieve users by usernames
- get followers
- platform operations
- post creation, editing, media management, and content analytics.
- community manager
- get users being followed
- manage stream filter rules
- x api
- add or delete rules for the filtered search stream
- microblogging
- look up users by usernames
- search full archive of posts
- search
- get counts from last 7 days
- manages brand presence, campaigns, and content strategy.
- getFollowers
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
