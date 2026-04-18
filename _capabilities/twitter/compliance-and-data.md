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
- monitor conversations, search posts, analyze trends, and extract insights.
- content
- getComplianceJobsById
- platform operations
- post compliance stream
- social media manager
- manage user relationships, direct messages, spaces, and community interactions.
- social media
- compliance
- stream post compliance events in real-time
- streamLikesCompliance
- ensures data handling meets regulatory and platform compliance requirements.
- engagement specialist
- data management
- user compliance stream
- streamLabelsCompliance
- monitors brand mentions, sentiment, and competitive landscape.
- stream likes compliance events
- researcher
- community manager
- microblogging
- user relationships, direct messaging, spaces, and community interaction.
- manages brand presence, campaigns, and content strategy.
- createComplianceJobs
- manage compliance jobs, data streams, and real-time compliance monitoring.
- handles customer inquiries and issues via direct messages and replies.
- marketing team
- post creation, editing, media management, and content analytics.
- get a compliance job by id
- streamPostsCompliance
- stream post compliance events
- stream labels compliance events
- brand manager
- conducts academic or market research using x data archives.
- manages user relationships, follows, and interaction strategies.
- advertising
- customer support
- social monitoring, search, trending topics, and sentiment analysis.
- data compliance, deletion tracking, and regulatory event monitoring.
- x api
- stream user compliance events in real-time
- create, manage, and analyze posts, media, bookmarks, and lists.
- list compliance jobs
- streamUsersCompliance
- getComplianceJobs
- create and list compliance jobs
- produces original posts, threads, and media content on x.
- streaming
- manages data pipelines, streaming ingestion, and compliance data flows.
- data analyst
- data engineer
- builds and maintains communities through engagement and moderation.
- stream labels compliance events in real-time
- labels compliance stream
- extracts insights from social data through search, streaming, and analytics.
- creates, schedules, and analyzes social media content across platforms.
- get a specific compliance job
- stream likes compliance events in real-time
- stream user compliance events
- real-time data
- compliance officer
- create a new compliance job
- likes compliance stream
- get a compliance job by its id
- content creator
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
