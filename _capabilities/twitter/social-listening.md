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
- engagement specialist
- get post insights for last 28 hours
- stream 10% sample of posts
- microblogging
- getFollowers
- produces original posts, threads, and media content on x.
- manages data pipelines, streaming ingestion, and compliance data flows.
- manage user relationships, direct messages, spaces, and community interactions.
- look up users by usernames
- get user followers
- get recent post counts
- retrieve the authenticated user's profile
- get counts from full archive
- getUsersByUsernames
- search for posts from the last 7 days
- manages user relationships, follows, and interaction strategies.
- get followers
- getPostsCountsRecent
- filtered search stream
- monitor conversations, search posts, analyze trends, and extract insights.
- get current rules for the filtered search stream
- getSearchStreamRules
- social monitoring, search, trending topics, and sentiment analysis.
- stream a 10% sample of all public posts in real-time
- search the full archive of posts
- searchPostsAll
- user relationships, direct messaging, spaces, and community interaction.
- create, manage, and analyze posts, media, bookmarks, and lists.
- social listening
- search all posts
- full firehose stream
- getFollowing
- retrieve multiple users by their ids
- content
- get followers of a user
- builds and maintains communities through engagement and moderation.
- streaming
- retrieve users by ids
- getUserMentions
- streamPostsSearch
- brand manager
- platform operations
- get current stream rules
- social media
- stream posts matching filtered stream rules in real-time
- retrieve users by usernames
- post creation, editing, media management, and content analytics.
- getPostsCountsAll
- get following
- compliance officer
- advertising
- creates, schedules, and analyzes social media content across platforms.
- community manager
- search recent posts
- get historical post insights
- get users being followed
- handles customer inquiries and issues via direct messages and replies.
- get posts authored by a specific user
- addSearchStreamRules
- searchPostsRecent
- data engineer
- social media manager
- customer support
- extracts insights from social data through search, streaming, and analytics.
- streamPostsFirehose
- add or delete stream rules
- marketing team
- look up users by ids
- conducts academic or market research using x data archives.
- stream posts matching filter rules
- getInsights28Hr
- 10% sample stream
- search posts from last 7 days
- data analyst
- get counts of posts matching a query from last 7 days
- getInsightsHistorical
- search full archive of posts
- get posts mentioning a specific user
- analytics
- monitors brand mentions, sentiment, and competitive landscape.
- search
- get 28-hour post insights
- manage compliance jobs, data streams, and real-time compliance monitoring.
- add or delete rules for the filtered search stream
- get counts from last 7 days
- real-time data
- getUsersMe
- get all post counts
- stream all public posts in real-time via the firehose
- stream all public posts
- get counts of posts matching a query from full archive
- content creator
- getUserTimeline
- trends
- streamPostsSample10
- getUsersByIds
- x api
- get users that a user is following
- researcher
- ensures data handling meets regulatory and platform compliance requirements.
- get post insights for the last 28 hours
- retrieve multiple users by their usernames
- manages brand presence, campaigns, and content strategy.
- data compliance, deletion tracking, and regulatory event monitoring.
- manage stream filter rules
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
