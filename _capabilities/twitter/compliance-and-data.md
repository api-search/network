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
- x api
- manages brand presence, campaigns, and content strategy.
- microblogging
- real-time data
- post compliance stream
- content
- create, manage, and analyze posts, media, bookmarks, and lists.
- builds and maintains communities through engagement and moderation.
- stream post compliance events
- streamPostsCompliance
- content creator
- get a compliance job by id
- monitors brand mentions, sentiment, and competitive landscape.
- compliance
- conducts academic or market research using x data archives.
- likes compliance stream
- customer support
- post creation, editing, media management, and content analytics.
- manage compliance jobs, data streams, and real-time compliance monitoring.
- community manager
- getComplianceJobsById
- researcher
- getComplianceJobs
- stream user compliance events
- create and list compliance jobs
- labels compliance stream
- createComplianceJobs
- manage user relationships, direct messages, spaces, and community interactions.
- user relationships, direct messaging, spaces, and community interaction.
- streamLikesCompliance
- platform operations
- data engineer
- stream post compliance events in real-time
- manages data pipelines, streaming ingestion, and compliance data flows.
- ensures data handling meets regulatory and platform compliance requirements.
- advertising
- produces original posts, threads, and media content on x.
- data analyst
- marketing team
- creates, schedules, and analyzes social media content across platforms.
- stream user compliance events in real-time
- stream likes compliance events in real-time
- stream labels compliance events in real-time
- extracts insights from social data through search, streaming, and analytics.
- manages user relationships, follows, and interaction strategies.
- data compliance, deletion tracking, and regulatory event monitoring.
- social monitoring, search, trending topics, and sentiment analysis.
- social media
- get a compliance job by its id
- compliance officer
- streaming
- brand manager
- data management
- streamLabelsCompliance
- engagement specialist
- handles customer inquiries and issues via direct messages and replies.
- get a specific compliance job
- stream likes compliance events
- monitor conversations, search posts, analyze trends, and extract insights.
- user compliance stream
- streamUsersCompliance
- stream labels compliance events
- create a new compliance job
- list compliance jobs
- social media manager
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
