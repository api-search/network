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
- stream labels compliance events
- stream user compliance events
- manages user relationships, follows, and interaction strategies.
- stream labels compliance events in real-time
- compliance
- get a compliance job by id
- data analyst
- community manager
- handles customer inquiries and issues via direct messages and replies.
- advertising
- microblogging
- x api
- stream user compliance events in real-time
- data engineer
- ensures data handling meets regulatory and platform compliance requirements.
- real-time data
- monitor conversations, search posts, analyze trends, and extract insights.
- streamUsersCompliance
- monitors brand mentions, sentiment, and competitive landscape.
- social media
- builds and maintains communities through engagement and moderation.
- streamPostsCompliance
- getComplianceJobs
- createComplianceJobs
- post compliance stream
- streaming
- customer support
- user relationships, direct messaging, spaces, and community interaction.
- manages data pipelines, streaming ingestion, and compliance data flows.
- manage user relationships, direct messages, spaces, and community interactions.
- get a compliance job by its id
- manage compliance jobs, data streams, and real-time compliance monitoring.
- brand manager
- streamLabelsCompliance
- researcher
- user compliance stream
- manages brand presence, campaigns, and content strategy.
- extracts insights from social data through search, streaming, and analytics.
- produces original posts, threads, and media content on x.
- post creation, editing, media management, and content analytics.
- likes compliance stream
- stream post compliance events in real-time
- create a new compliance job
- social monitoring, search, trending topics, and sentiment analysis.
- engagement specialist
- marketing team
- list compliance jobs
- social media manager
- streamLikesCompliance
- create, manage, and analyze posts, media, bookmarks, and lists.
- labels compliance stream
- content
- platform operations
- content creator
- data management
- create and list compliance jobs
- getComplianceJobsById
- stream post compliance events
- stream likes compliance events in real-time
- creates, schedules, and analyzes social media content across platforms.
- get a specific compliance job
- stream likes compliance events
- compliance officer
- conducts academic or market research using x data archives.
- data compliance, deletion tracking, and regulatory event monitoring.
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
