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
- retrieve users by usernames
- social media manager
- get counts from last 7 days
- retrieve the authenticated user's profile
- community manager
- filtered search stream
- full firehose stream
- getFollowers
- manages brand presence, campaigns, and content strategy.
- handles customer inquiries and issues via direct messages and replies.
- stream posts matching filtered stream rules in real-time
- get following
- conducts academic or market research using x data archives.
- get posts mentioning a specific user
- customer support
- streaming
- 10% sample stream
- data engineer
- builds and maintains communities through engagement and moderation.
- search for posts from the last 7 days
- search the full archive of posts
- manages data pipelines, streaming ingestion, and compliance data flows.
- getUserTimeline
- content
- searchPostsAll
- social media
- manage user relationships, direct messages, spaces, and community interactions.
- search full archive of posts
- get current stream rules
- ensures data handling meets regulatory and platform compliance requirements.
- engagement specialist
- search
- get users that a user is following
- user relationships, direct messaging, spaces, and community interaction.
- manage compliance jobs, data streams, and real-time compliance monitoring.
- add or delete stream rules
- post creation, editing, media management, and content analytics.
- searchPostsRecent
- brand manager
- get users being followed
- advertising
- retrieve multiple users by their usernames
- stream all public posts
- social monitoring, search, trending topics, and sentiment analysis.
- x api
- streamPostsSample10
- getInsights28Hr
- add or delete rules for the filtered search stream
- social listening
- get historical post insights
- getUsersByUsernames
- retrieve multiple users by their ids
- monitor conversations, search posts, analyze trends, and extract insights.
- platform operations
- monitors brand mentions, sentiment, and competitive landscape.
- search posts from last 7 days
- manage stream filter rules
- get user followers
- stream 10% sample of posts
- getUsersByIds
- search all posts
- marketing team
- retrieve users by ids
- getInsightsHistorical
- get current rules for the filtered search stream
- getUserMentions
- manages user relationships, follows, and interaction strategies.
- get followers of a user
- get 28-hour post insights
- get counts from full archive
- stream all public posts in real-time via the firehose
- produces original posts, threads, and media content on x.
- get posts authored by a specific user
- get post insights for last 28 hours
- addSearchStreamRules
- create, manage, and analyze posts, media, bookmarks, and lists.
- compliance officer
- streamPostsSearch
- getUsersMe
- streamPostsFirehose
- search recent posts
- look up users by usernames
- get post insights for the last 28 hours
- trends
- getFollowing
- analytics
- stream posts matching filter rules
- get recent post counts
- researcher
- microblogging
- get counts of posts matching a query from full archive
- getSearchStreamRules
- data compliance, deletion tracking, and regulatory event monitoring.
- get followers
- getPostsCountsAll
- data analyst
- get all post counts
- getPostsCountsRecent
- look up users by ids
- get counts of posts matching a query from last 7 days
- extracts insights from social data through search, streaming, and analytics.
- creates, schedules, and analyzes social media content across platforms.
- stream a 10% sample of all public posts in real-time
- real-time data
- content creator
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
