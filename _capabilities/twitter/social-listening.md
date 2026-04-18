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
- manages brand presence, campaigns, and content strategy.
- content
- retrieve the authenticated user's profile
- get counts from last 7 days
- getInsightsHistorical
- monitors brand mentions, sentiment, and competitive landscape.
- conducts academic or market research using x data archives.
- retrieve users by usernames
- getInsights28Hr
- researcher
- get user followers
- analytics
- get all post counts
- stream 10% sample of posts
- trends
- ensures data handling meets regulatory and platform compliance requirements.
- extracts insights from social data through search, streaming, and analytics.
- creates, schedules, and analyzes social media content across platforms.
- streamPostsSearch
- brand manager
- engagement specialist
- retrieve multiple users by their ids
- get followers of a user
- add or delete stream rules
- social media manager
- x api
- real-time data
- get posts authored by a specific user
- search full archive of posts
- builds and maintains communities through engagement and moderation.
- getFollowing
- getPostsCountsAll
- get recent post counts
- get following
- post creation, editing, media management, and content analytics.
- stream all public posts in real-time via the firehose
- manage compliance jobs, data streams, and real-time compliance monitoring.
- search for posts from the last 7 days
- searchPostsRecent
- 10% sample stream
- search recent posts
- get historical post insights
- search
- stream posts matching filter rules
- manages data pipelines, streaming ingestion, and compliance data flows.
- get posts mentioning a specific user
- marketing team
- social monitoring, search, trending topics, and sentiment analysis.
- get followers
- getUserMentions
- look up users by ids
- get current rules for the filtered search stream
- streamPostsSample10
- microblogging
- create, manage, and analyze posts, media, bookmarks, and lists.
- content creator
- search posts from last 7 days
- search all posts
- add or delete rules for the filtered search stream
- retrieve multiple users by their usernames
- getUsersMe
- get 28-hour post insights
- searchPostsAll
- look up users by usernames
- stream a 10% sample of all public posts in real-time
- manage user relationships, direct messages, spaces, and community interactions.
- manage stream filter rules
- user relationships, direct messaging, spaces, and community interaction.
- getSearchStreamRules
- advertising
- data analyst
- data compliance, deletion tracking, and regulatory event monitoring.
- streaming
- handles customer inquiries and issues via direct messages and replies.
- streamPostsFirehose
- get users being followed
- getFollowers
- monitor conversations, search posts, analyze trends, and extract insights.
- getPostsCountsRecent
- get users that a user is following
- filtered search stream
- get counts of posts matching a query from full archive
- full firehose stream
- get post insights for the last 28 hours
- search the full archive of posts
- customer support
- community manager
- addSearchStreamRules
- platform operations
- getUserTimeline
- data engineer
- get current stream rules
- get counts of posts matching a query from last 7 days
- produces original posts, threads, and media content on x.
- manages user relationships, follows, and interaction strategies.
- social media
- getUsersByIds
- get post insights for last 28 hours
- stream posts matching filtered stream rules in real-time
- social listening
- get counts from full archive
- stream all public posts
- getUsersByUsernames
- retrieve users by ids
- compliance officer
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
