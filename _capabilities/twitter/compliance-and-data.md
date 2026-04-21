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
- engagement specialist
- streamPostsCompliance
- compliance
- stream post compliance events
- data management
- community manager
- creates, schedules, and analyzes social media content across platforms.
- user relationships, direct messaging, spaces, and community interaction.
- microblogging
- produces original posts, threads, and media content on x.
- advertising
- streamLabelsCompliance
- create, manage, and analyze posts, media, bookmarks, and lists.
- manages data pipelines, streaming ingestion, and compliance data flows.
- monitors brand mentions, sentiment, and competitive landscape.
- manage user relationships, direct messages, spaces, and community interactions.
- getComplianceJobs
- streamLikesCompliance
- stream user compliance events
- labels compliance stream
- manage compliance jobs, data streams, and real-time compliance monitoring.
- post compliance stream
- stream user compliance events in real-time
- real-time data
- handles customer inquiries and issues via direct messages and replies.
- content creator
- list compliance jobs
- manages user relationships, follows, and interaction strategies.
- content
- builds and maintains communities through engagement and moderation.
- user compliance stream
- streaming
- data engineer
- stream post compliance events in real-time
- social media manager
- likes compliance stream
- stream likes compliance events in real-time
- customer support
- get a specific compliance job
- stream labels compliance events
- extracts insights from social data through search, streaming, and analytics.
- x api
- createComplianceJobs
- get a compliance job by its id
- researcher
- monitor conversations, search posts, analyze trends, and extract insights.
- stream likes compliance events
- marketing team
- brand manager
- platform operations
- ensures data handling meets regulatory and platform compliance requirements.
- social media
- create and list compliance jobs
- conducts academic or market research using x data archives.
- social monitoring, search, trending topics, and sentiment analysis.
- get a compliance job by id
- manages brand presence, campaigns, and content strategy.
- getComplianceJobsById
- data compliance, deletion tracking, and regulatory event monitoring.
- stream labels compliance events in real-time
- create a new compliance job
- post creation, editing, media management, and content analytics.
- streamUsersCompliance
- data analyst
- compliance officer
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
