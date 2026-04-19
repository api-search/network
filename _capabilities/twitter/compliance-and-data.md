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
- get a compliance job by its id
- list compliance jobs
- likes compliance stream
- engagement specialist
- data compliance, deletion tracking, and regulatory event monitoring.
- labels compliance stream
- getComplianceJobs
- stream post compliance events in real-time
- stream likes compliance events in real-time
- post compliance stream
- create and list compliance jobs
- stream post compliance events
- streamLabelsCompliance
- monitors brand mentions, sentiment, and competitive landscape.
- builds and maintains communities through engagement and moderation.
- content
- stream labels compliance events
- monitor conversations, search posts, analyze trends, and extract insights.
- data analyst
- ensures data handling meets regulatory and platform compliance requirements.
- community manager
- extracts insights from social data through search, streaming, and analytics.
- stream labels compliance events in real-time
- user compliance stream
- get a specific compliance job
- stream user compliance events
- social monitoring, search, trending topics, and sentiment analysis.
- brand manager
- researcher
- manages brand presence, campaigns, and content strategy.
- stream user compliance events in real-time
- post creation, editing, media management, and content analytics.
- user relationships, direct messaging, spaces, and community interaction.
- customer support
- real-time data
- streamPostsCompliance
- advertising
- streaming
- getComplianceJobsById
- create a new compliance job
- data engineer
- creates, schedules, and analyzes social media content across platforms.
- compliance
- createComplianceJobs
- data management
- streamUsersCompliance
- platform operations
- produces original posts, threads, and media content on x.
- stream likes compliance events
- manage compliance jobs, data streams, and real-time compliance monitoring.
- conducts academic or market research using x data archives.
- content creator
- social media manager
- social media
- manages user relationships, follows, and interaction strategies.
- handles customer inquiries and issues via direct messages and replies.
- marketing team
- get a compliance job by id
- microblogging
- x api
- manages data pipelines, streaming ingestion, and compliance data flows.
- streamLikesCompliance
- compliance officer
- create, manage, and analyze posts, media, bookmarks, and lists.
- manage user relationships, direct messages, spaces, and community interactions.
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
