---
consumed_apis:
- x-streaming
- x-posts
description: Unified workflow for managing compliance jobs, data streams, and real-time compliance monitoring on X. Used by compliance officers, data engineers, and platform operations.
layout: capability
name: X Compliance and Data Management
operations:
- description: Create a new compliance job
  method: POST
  name: createComplianceJobs
  path: /v1/compliance/jobs
- description: List compliance jobs
  method: GET
  name: getComplianceJobs
  path: /v1/compliance/jobs
- description: Get a compliance job by ID
  method: GET
  name: getComplianceJobsById
  path: /v1/compliance/jobs/{id}
- description: Stream user compliance events
  method: GET
  name: streamUsersCompliance
  path: /v1/compliance/streams/users
- description: Stream post compliance events
  method: GET
  name: streamPostsCompliance
  path: /v1/compliance/streams/posts
- description: Stream likes compliance events
  method: GET
  name: streamLikesCompliance
  path: /v1/compliance/streams/likes
- description: Stream labels compliance events
  method: GET
  name: streamLabelsCompliance
  path: /v1/compliance/streams/labels
personas:
- description: Ensures data handling meets regulatory and platform compliance requirements.
  id: compliance-officer
  name: Compliance Officer
- description: Manages data pipelines, streaming ingestion, and compliance data flows.
  id: data-engineer
  name: Data Engineer
provider_name: X (Twitter)
provider_slug: twitter
search_terms:
- stream labels compliance events in real-time
- researcher
- data compliance, deletion tracking, and regulatory event monitoring.
- streamUsersCompliance
- manage user relationships, direct messages, spaces, and community interactions.
- streamLikesCompliance
- get a specific compliance job
- extracts insights from social data through search, streaming, and analytics.
- compliance
- streamPostsCompliance
- marketing team
- stream user compliance events
- customer support
- compliance officer
- post creation, editing, media management, and content analytics.
- creates, schedules, and analyzes social media content across platforms.
- brand manager
- social media
- create a new compliance job
- post compliance stream
- ensures data handling meets regulatory and platform compliance requirements.
- labels compliance stream
- stream likes compliance events
- data analyst
- platform operations
- create, manage, and analyze posts, media, bookmarks, and lists.
- createComplianceJobs
- data engineer
- stream post compliance events
- manage compliance jobs, data streams, and real-time compliance monitoring.
- streamLabelsCompliance
- handles customer inquiries and issues via direct messages and replies.
- content
- get a compliance job by its id
- manages user relationships, follows, and interaction strategies.
- stream likes compliance events in real-time
- streaming
- x api
- getComplianceJobsById
- stream labels compliance events
- community manager
- social media manager
- manages brand presence, campaigns, and content strategy.
- microblogging
- content creator
- builds and maintains communities through engagement and moderation.
- engagement specialist
- likes compliance stream
- get a compliance job by id
- monitor conversations, search posts, analyze trends, and extract insights.
- list compliance jobs
- produces original posts, threads, and media content on x.
- monitors brand mentions, sentiment, and competitive landscape.
- conducts academic or market research using x data archives.
- manages data pipelines, streaming ingestion, and compliance data flows.
- real-time data
- advertising
- create and list compliance jobs
- stream post compliance events in real-time
- user compliance stream
- user relationships, direct messaging, spaces, and community interaction.
- data management
- social monitoring, search, trending topics, and sentiment analysis.
- getComplianceJobs
- stream user compliance events in real-time
slug: compliance-and-data
tags:
- X API
- Compliance
- Data Management
- Streaming
tools:
- description: Create a new compliance job
  hints:
    idempotent: false
    readOnly: false
  name: createComplianceJobs
- description: List compliance jobs
  hints:
    idempotent: true
    readOnly: true
  name: getComplianceJobs
- description: Get a compliance job by its ID
  hints:
    idempotent: true
    readOnly: true
  name: getComplianceJobsById
- description: Stream user compliance events in real-time
  hints:
    idempotent: true
    readOnly: true
  name: streamUsersCompliance
- description: Stream post compliance events in real-time
  hints:
    idempotent: true
    readOnly: true
  name: streamPostsCompliance
- description: Stream likes compliance events in real-time
  hints:
    idempotent: true
    readOnly: true
  name: streamLikesCompliance
- description: Stream labels compliance events in real-time
  hints:
    idempotent: true
    readOnly: true
  name: streamLabelsCompliance
---
