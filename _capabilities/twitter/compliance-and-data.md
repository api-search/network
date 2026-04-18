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
- streamLikesCompliance
- social monitoring, search, trending topics, and sentiment analysis.
- post compliance stream
- monitor conversations, search posts, analyze trends, and extract insights.
- engagement specialist
- manages brand presence, campaigns, and content strategy.
- user relationships, direct messaging, spaces, and community interaction.
- data management
- getComplianceJobs
- stream labels compliance events
- content creator
- stream post compliance events in real-time
- manages data pipelines, streaming ingestion, and compliance data flows.
- handles customer inquiries and issues via direct messages and replies.
- data engineer
- microblogging
- social media manager
- stream user compliance events in real-time
- compliance
- ensures data handling meets regulatory and platform compliance requirements.
- manage compliance jobs, data streams, and real-time compliance monitoring.
- monitors brand mentions, sentiment, and competitive landscape.
- getComplianceJobsById
- stream labels compliance events in real-time
- marketing team
- data compliance, deletion tracking, and regulatory event monitoring.
- advertising
- brand manager
- extracts insights from social data through search, streaming, and analytics.
- stream user compliance events
- platform operations
- streamLabelsCompliance
- stream post compliance events
- labels compliance stream
- createComplianceJobs
- create and list compliance jobs
- researcher
- manages user relationships, follows, and interaction strategies.
- get a compliance job by its id
- x api
- real-time data
- content
- streamPostsCompliance
- compliance officer
- social media
- get a specific compliance job
- customer support
- likes compliance stream
- streamUsersCompliance
- create a new compliance job
- creates, schedules, and analyzes social media content across platforms.
- get a compliance job by id
- produces original posts, threads, and media content on x.
- streaming
- list compliance jobs
- user compliance stream
- builds and maintains communities through engagement and moderation.
- community manager
- post creation, editing, media management, and content analytics.
- create, manage, and analyze posts, media, bookmarks, and lists.
- manage user relationships, direct messages, spaces, and community interactions.
- conducts academic or market research using x data archives.
- data analyst
- stream likes compliance events in real-time
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
