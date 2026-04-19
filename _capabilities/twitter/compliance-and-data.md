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
- stream likes compliance events in real-time
- data engineer
- data compliance, deletion tracking, and regulatory event monitoring.
- post creation, editing, media management, and content analytics.
- getComplianceJobsById
- microblogging
- user compliance stream
- platform operations
- social monitoring, search, trending topics, and sentiment analysis.
- compliance officer
- manages user relationships, follows, and interaction strategies.
- data analyst
- list compliance jobs
- get a compliance job by its id
- manage compliance jobs, data streams, and real-time compliance monitoring.
- marketing team
- social media manager
- manages brand presence, campaigns, and content strategy.
- builds and maintains communities through engagement and moderation.
- stream post compliance events
- data management
- user relationships, direct messaging, spaces, and community interaction.
- brand manager
- get a specific compliance job
- social media
- post compliance stream
- stream labels compliance events
- streamLikesCompliance
- manages data pipelines, streaming ingestion, and compliance data flows.
- engagement specialist
- researcher
- stream post compliance events in real-time
- create and list compliance jobs
- monitor conversations, search posts, analyze trends, and extract insights.
- compliance
- stream likes compliance events
- create a new compliance job
- extracts insights from social data through search, streaming, and analytics.
- likes compliance stream
- stream labels compliance events in real-time
- content creator
- streaming
- monitors brand mentions, sentiment, and competitive landscape.
- streamLabelsCompliance
- ensures data handling meets regulatory and platform compliance requirements.
- getComplianceJobs
- streamPostsCompliance
- content
- manage user relationships, direct messages, spaces, and community interactions.
- x api
- labels compliance stream
- streamUsersCompliance
- creates, schedules, and analyzes social media content across platforms.
- real-time data
- advertising
- stream user compliance events
- createComplianceJobs
- stream user compliance events in real-time
- produces original posts, threads, and media content on x.
- handles customer inquiries and issues via direct messages and replies.
- community manager
- get a compliance job by id
- conducts academic or market research using x data archives.
- customer support
- create, manage, and analyze posts, media, bookmarks, and lists.
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
