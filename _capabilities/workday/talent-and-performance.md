---
consumed_apis:
- workday-recruiting
- workday-talent
- workday-performance
description: Unified talent and performance management combining Recruiting, Talent, and Performance Management APIs for HR and talent leads to manage hiring pipelines, career development, and performance evaluations.
layout: capability
name: Workday Talent and Performance
operations:
- description: List job requisitions
  method: GET
  name: list-requisitions
  path: /v1/job-requisitions
- description: List candidates
  method: GET
  name: list-candidates
  path: /v1/candidates
- description: List performance reviews
  method: GET
  name: list-reviews
  path: /v1/performance-reviews
- description: List succession plans
  method: GET
  name: list-succession-plans
  path: /v1/succession-plans
personas: []
provider_name: Workday
provider_slug: workday
search_terms:
- recruiting list requisitions
- list all prospects
- enterprise software
- request feedback for a worker
- talent get certifications
- talent list succession plans
- list all job requisitions
- performance reviews
- recruiting list prospects
- get certifications for a worker
- list reviews
- list all job postings
- recruiting list candidates
- list job requisitions
- recruiting list postings
- performance get goals
- job requisitions
- get talent profile for a worker
- get goals for a worker
- list feedback badges
- get skills for a worker
- performance request feedback
- performance list badges
- hcm
- list all job applications
- recruiting list applications
- get a job requisition by id
- cloud computing
- talent management
- list performance reviews
- list mentorships
- recruiting
- get a candidate by id
- list requisitions
- talent get profile
- get a job application by id
- give a feedback badge to a worker
- saas
- performance give badge
- list all candidates
- performance
- recruiting get requisition
- candidates
- recruiting get application
- list candidates
- talent get skills
- workday
- performance list reviews
- talent list mentorships
- recruiting get candidate
- financial management
- list succession plans
- succession plans
slug: talent-and-performance
tags:
- Workday
- Talent Management
- Performance
- Recruiting
tools:
- description: List all job requisitions
  hints:
    readOnly: true
  name: recruiting-list-requisitions
- description: Get a job requisition by ID
  hints:
    readOnly: true
  name: recruiting-get-requisition
- description: List all job postings
  hints:
    readOnly: true
  name: recruiting-list-postings
- description: List all candidates
  hints:
    readOnly: true
  name: recruiting-list-candidates
- description: Get a candidate by ID
  hints:
    readOnly: true
  name: recruiting-get-candidate
- description: List all job applications
  hints:
    readOnly: true
  name: recruiting-list-applications
- description: Get a job application by ID
  hints:
    readOnly: true
  name: recruiting-get-application
- description: List all prospects
  hints:
    readOnly: true
  name: recruiting-list-prospects
- description: Get talent profile for a worker
  hints:
    readOnly: true
  name: talent-get-profile
- description: List mentorships
  hints:
    readOnly: true
  name: talent-list-mentorships
- description: Get skills for a worker
  hints:
    readOnly: true
  name: talent-get-skills
- description: Get certifications for a worker
  hints:
    readOnly: true
  name: talent-get-certifications
- description: List succession plans
  hints:
    readOnly: true
  name: talent-list-succession-plans
- description: Get goals for a worker
  hints:
    readOnly: true
  name: performance-get-goals
- description: List performance reviews
  hints:
    readOnly: true
  name: performance-list-reviews
- description: List feedback badges
  hints:
    readOnly: true
  name: performance-list-badges
- description: Give a feedback badge to a worker
  hints:
    readOnly: false
  name: performance-give-badge
- description: Request feedback for a worker
  hints:
    readOnly: false
  name: performance-request-feedback
---
