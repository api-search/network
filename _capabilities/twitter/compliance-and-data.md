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
- getComplianceJobsById
- social media manager
- manages user relationships, follows, and interaction strategies.
- ensures data handling meets regulatory and platform compliance requirements.
- social media
- user relationships, direct messaging, spaces, and community interaction.
- stream post compliance events
- conducts academic or market research using x data archives.
- streamPostsCompliance
- streaming
- stream likes compliance events in real-time
- brand manager
- advertising
- streamUsersCompliance
- stream labels compliance events
- create, manage, and analyze posts, media, bookmarks, and lists.
- manage user relationships, direct messages, spaces, and community interactions.
- content creator
- get a compliance job by its id
- streamLikesCompliance
- streamLabelsCompliance
- compliance
- data analyst
- monitor conversations, search posts, analyze trends, and extract insights.
- data management
- manages brand presence, campaigns, and content strategy.
- researcher
- content
- manages data pipelines, streaming ingestion, and compliance data flows.
- creates, schedules, and analyzes social media content across platforms.
- likes compliance stream
- stream user compliance events
- real-time data
- social monitoring, search, trending topics, and sentiment analysis.
- engagement specialist
- data engineer
- post compliance stream
- labels compliance stream
- community manager
- platform operations
- handles customer inquiries and issues via direct messages and replies.
- x api
- produces original posts, threads, and media content on x.
- extracts insights from social data through search, streaming, and analytics.
- marketing team
- compliance officer
- post creation, editing, media management, and content analytics.
- stream user compliance events in real-time
- microblogging
- list compliance jobs
- get a specific compliance job
- get a compliance job by id
- monitors brand mentions, sentiment, and competitive landscape.
- builds and maintains communities through engagement and moderation.
- getComplianceJobs
- create a new compliance job
- stream post compliance events in real-time
- data compliance, deletion tracking, and regulatory event monitoring.
- create and list compliance jobs
- stream labels compliance events in real-time
- manage compliance jobs, data streams, and real-time compliance monitoring.
- createComplianceJobs
- customer support
- user compliance stream
- stream likes compliance events
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
