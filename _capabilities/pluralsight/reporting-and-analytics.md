---
consumed_apis:
- pluralsight-content-progress
- pluralsight-course-progress
- pluralsight-course-daily-usage
- pluralsight-reports-rest
description: Unified workflow for L&D managers to track learning progress, course completions, daily usage patterns, and generate reports. Combines content progress, course progress, course daily usage, and reports REST APIs.
layout: capability
name: Pluralsight Reporting And Analytics
operations:
- description: Track user progress across all content types
  method: POST
  name: query-content-progress
  path: /v1/content-progress
- description: Track user course progress and completion status
  method: POST
  name: query-course-progress
  path: /v1/course-progress
- description: Retrieve daily course engagement metrics
  method: POST
  name: query-course-daily-usage
  path: /v1/course-daily-usage
- description: Download a user report as CSV
  method: GET
  name: download-user-report
  path: /v1/user-reports
- description: Download a course completion report as CSV
  method: GET
  name: download-course-completion-report
  path: /v1/course-completion-reports
- description: Download a course usage report as CSV
  method: GET
  name: download-course-usage-report
  path: /v1/course-usage-reports
personas: []
provider_name: Pluralsight
provider_slug: pluralsight
search_terms:
- skills assessment
- technology
- download a user report as csv. deprecated - migrate to graphql.
- analytics
- courses
- engineering metrics
- learning progress
- track user course progress and completion status
- download a course completion report as csv
- reporting
- download a user report as csv
- user course progress including completion status and viewing history
- course completion
- track user progress across all content types including videos, guides, paths, interactive courses, and projects.
- course completion reports as csv downloads (legacy rest, deprecated)
- course usage reports as csv downloads (legacy rest, deprecated)
- download a course usage report as csv. deprecated - migrate to graphql.
- download course usage report
- download course completion report
- query course progress
- retrieve daily course engagement metrics and usage statistics.
- video training
- pluralsight
- learning
- track user course progress including completion status and viewing history for video courses.
- query content progress
- education
- download a course usage report as csv
- query course daily usage
- track user progress across all content types
- retrieve daily course engagement metrics
- download a course completion report as csv. deprecated - migrate to graphql.
- user progress across all content types including videos, guides, paths, and projects
- user reports as csv downloads (legacy rest, deprecated)
- daily course engagement metrics and usage statistics
- download user report
slug: reporting-and-analytics
tags:
- Pluralsight
- Reporting
- Analytics
- Learning Progress
- Course Completion
tools:
- description: Track user progress across all content types including videos, guides, paths, interactive courses, and projects.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-content-progress
- description: Track user course progress including completion status and viewing history for video courses.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-course-progress
- description: Retrieve daily course engagement metrics and usage statistics.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-course-daily-usage
- description: Download a user report as CSV. Deprecated - migrate to GraphQL.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: download-user-report
- description: Download a course completion report as CSV. Deprecated - migrate to GraphQL.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: download-course-completion-report
- description: Download a course usage report as CSV. Deprecated - migrate to GraphQL.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: download-course-usage-report
---
