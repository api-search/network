---
api_count: 30
apis:
- description: GraphQL query for accessing course catalog information including titles, descriptions, authors, duration, release dates, and retirement status. Updated daily.
  name: Pluralsight Course Catalog API
  slug: course-catalog-api
- description: GraphQL query for accessing the general content catalog including videos, guides, interactive courses, and other content types beyond traditional courses.
  name: Pluralsight Content Catalog API
  slug: content-catalog-api
- description: GraphQL query for accessing learning path catalog data including structured sequences of courses and content organized around specific skills and roles.
  name: Pluralsight Learning Paths API
  slug: learning-paths-api
- description: GraphQL queries for accessing lab catalog and lab activity data for hands-on learning experiences and practical exercises.
  name: Pluralsight Labs API
  slug: labs-api
- description: GraphQL query for accessing the program catalog including structured learning programs and curriculum offerings.
  name: Pluralsight Programs API
  slug: programs-api
- description: GraphQL query for accessing content tags and taxonomy data used to categorize and organize learning content.
  name: Pluralsight Tags API
  slug: tags-api
- description: GraphQL query for resolving content slugs to internal identifiers, enabling lookup of content by human-readable URL slugs.
  name: Pluralsight Content Slug API
  slug: content-slug-api
- description: GraphQL queries and mutations for managing content channels including creating channels, managing members and groups, organizing content sections, and tracking channel progress.
  name: Pluralsight Channels API
  slug: channels-api
- description: GraphQL query for tracking user course progress including completion status and viewing history for video courses. Updated daily.
  name: Pluralsight Course Progress API
  slug: course-progress-api
- description: GraphQL query for tracking user progress across all content types including videos, guides, paths, interactive courses, and projects. Currently in beta.
  name: Pluralsight Content Progress API
  slug: content-progress-api
- description: GraphQL query for retrieving daily course engagement metrics and usage statistics.
  name: Pluralsight Course Daily Usage API
  slug: course-daily-usage-api
- description: GraphQL query for retrieving practice exam attempt data including scores and results.
  name: Pluralsight Practice Exams API
  slug: practice-exams-api
- description: GraphQL queries for accessing skill assessments, Skill IQ scores, assessment catalogs, and competency measurements.
  name: Pluralsight Skills Assessment API
  slug: skills-assessment-api
- description: GraphQL queries and mutations for Role IQ assessments, role catalogs, skill assignments, and user/team role associations.
  name: Pluralsight Role IQ API
  slug: role-iq-api
- description: GraphQL queries and mutations for managing users including listing users, inviting members, editing user details, removing users, and canceling invitations.
  name: Pluralsight User Management API
  slug: user-management-api
- description: GraphQL queries and mutations for managing teams including creating teams, managing membership, assigning managers, and configuring team permissions.
  name: Pluralsight Teams API
  slug: teams-api
- description: GraphQL query for retrieving account and plan details including subscription tier and configuration.
  name: Pluralsight Plan Info API
  slug: plan-info-api
- description: REST API for accessing DORA engineering metrics including deployment frequency, lead time for changes, change failure rate, and time to restore service.
  name: Pluralsight Flow DORA Metrics API
  slug: flow-dora-metrics-api
- description: REST API for accessing code-level engineering metrics and developer productivity data with date range filtering.
  name: Pluralsight Flow Coding Metrics API
  slug: flow-coding-metrics-api
- description: REST API for accessing pull request and collaboration metrics for engineering teams with date range filtering.
  name: Pluralsight Flow Collaboration Metrics API
  slug: flow-collaboration-metrics-api
- description: REST API for accessing commit data and aggregated commit metrics across repositories.
  name: Pluralsight Flow Commits API
  slug: flow-commits-api
- description: REST API for accessing pull request data, comments, and events across repositories.
  name: Pluralsight Flow Pull Requests API
  slug: flow-pull-requests-api
- description: REST API for accessing repository data and metadata across connected source control systems.
  name: Pluralsight Flow Repos API
  slug: flow-repos-api
- description: REST API for managing Flow users including listing, updating, merging, hiding, and bulk operations on user accounts.
  name: Pluralsight Flow Users API
  slug: flow-users-api
- description: REST API for managing Flow engineering teams and team membership data.
  name: Pluralsight Flow Teams API
  slug: flow-teams-api
- description: REST API for managing Flow integrations and checking connection status with external tools and services.
  name: Pluralsight Flow Integrations API
  slug: flow-integrations-api
- description: REST API for accessing ticket data including comments, events, and project associations from connected project management tools.
  name: Pluralsight Flow Tickets API
  slug: flow-tickets-api
- description: Legacy REST API for downloading user, course completion, and course usage reports as CSV files. Deprecated as of February 2025, removal scheduled for November 2025.
  name: Pluralsight Reports REST API
  slug: reports-rest-api
- description: Legacy REST API for managing user invitations, users, and teams within a plan. Deprecated as of February 2025, removal scheduled for November 2025.
  name: Pluralsight Licensing REST API
  slug: licensing-rest-api
- description: Legacy public REST API for accessing the full course catalog without authentication. Returns course IDs, titles, durations, release dates, and retirement status.
  name: Pluralsight Public Course Catalog REST API
  slug: public-course-catalog-rest-api
capabilities:
- description: Unified workflow for engineering managers to track developer productivity, code quality, collaboration, and delivery performance through Flow metrics. Combines coding metrics, collaboration metrics, D
  name: Pluralsight Engineering Metrics
  slug: engineering-metrics
- description: Unified workflow for L&D managers and content administrators to browse, organize, and manage learning content across courses, channels, learning paths, programs, labs, and tags. Combines content catal
  name: Pluralsight Learning Content Management
  slug: learning-content-management
- description: Unified workflow for L&D managers to track learning progress, course completions, daily usage patterns, and generate reports. Combines content progress, course progress, course daily usage, and report
  name: Pluralsight Reporting And Analytics
  slug: reporting-and-analytics
- description: Unified workflow for L&D managers and developers to assess skills through Skill IQ, Role IQ, and practice exams. Combines skills assessment, role IQ, and practice exams APIs for comprehensive competen
  name: Pluralsight Skills Assessment
  slug: skills-assessment
- description: Unified workflow for platform administrators to manage users, teams, licensing, plan configuration, and Flow workspace settings. Combines user management, teams, licensing, plan info, Flow users, Flow
  name: Pluralsight User And Team Administration
  slug: user-and-team-administration
common:
- title: ''
  type: Portal
  url: https://developer.pluralsight.com
- title: ''
  type: GettingStarted
  url: https://developer.pluralsight.com/docs/getting-started
- title: ''
  type: Authentication
  url: https://developer.pluralsight.com/docs/getting-started
- title: ''
  type: FAQ
  url: https://developer.pluralsight.com/docs/getting-started/faqs
- title: ''
  type: CodeExamples
  url: https://developer.pluralsight.com/docs/getting-started/examples
- title: ''
  type: GraphQL
  url: https://developer.pluralsight.com/docs/getting-started/using-graphql
- title: ''
  type: Documentation
  url: https://developer.pluralsight.com/docs/deprecations/2025-deprecation-guide
- title: ''
  type: Documentation
  url: https://help.pluralsight.com/hc/en-us/articles/24420566008084-Migrating-from-REST-to-GraphQL-APIs
- title: ''
  type: RateLimits
  url: https://developer.pluralsight.com/docs/rate-limits
- title: ''
  type: TermsOfService
  url: https://www.pluralsight.com/terms
- title: ''
  type: PrivacyPolicy
  url: https://www.pluralsight.com/privacy
- title: ''
  type: Support
  url: https://help.pluralsight.com
- title: ''
  type: StatusPage
  url: https://status.pluralsight.com
- title: ''
  type: Blog
  url: https://www.pluralsight.com/blog
created: '2024'
description: APIs for the Pluralsight technology skills and engineering intelligence platform, providing access to courses, learning paths, assessments, user progress, channels, teams, and engineering metrics via GraphQL and REST APIs.
features:
- description: Access the full Pluralsight course catalog with titles, authors, duration, and release dates via GraphQL.
  name: Course Catalog API
- description: Measure technology skills with Skill IQ assessments and track competency levels.
  name: Skills Assessment
- description: Assess role readiness and track skill gaps for technology roles.
  name: Role IQ
- description: Track course completion, content progress, and daily usage across users and teams.
  name: Learning Progress Tracking
- description: Create and manage curated content channels with sections and member management.
  name: Channels
- description: Manage users, invitations, teams, and permissions via GraphQL mutations.
  name: User and Team Management
- description: Access DevOps Research and Assessment metrics for engineering team performance.
  name: DORA Metrics
- description: Track code-level productivity metrics and developer activity.
  name: Coding Metrics
- description: Monitor pull request and code review collaboration patterns.
  name: Collaboration Metrics
- description: Access hands-on lab catalog and track lab activity for practical learning.
  name: Labs
- description: Retrieve practice exam attempts and scores for certification preparation.
  name: Practice Exams
- description: Access commit, PR, ticket, and repository data for engineering analytics.
  name: Flow Engineering Intelligence
image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
integrations: []
jsonld:
- class_count: 3
  name: Pluralsight Context
  property_count: 8
  slug: pluralsight-context
layout: provider
modified: '2026-04-17'
name: Pluralsight
rules:
- name: Pluralsight API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: pluralsight-spectral-rules
skills: []
slug: pluralsight
solutions:
- description: Technology skills platform with courses, assessments, and learning paths for upskilling teams.
  name: Pluralsight Skills
- description: Engineering intelligence platform with DORA metrics, coding analytics, and collaboration insights.
  name: Pluralsight Flow
tags:
- Courses
- Education
- Engineering Metrics
- Learning
- Skills Assessment
- Technology
- Video Training
url: https://raw.githubusercontent.com/api-evangelist/pluralsight/refs/heads/main/apis.yml
use_cases:
- description: Sync Pluralsight course catalog and completion data with enterprise learning management systems.
  name: LMS Integration
- description: Assess team skill levels and identify training needs using Skill IQ and Role IQ data.
  name: Skills Gap Analysis
- description: Track DORA metrics, coding activity, and collaboration patterns for engineering teams.
  name: Engineering Performance
- description: Generate training completion reports for regulatory and compliance requirements.
  name: Compliance Reporting
- description: Automate new hire provisioning, team assignment, and learning path enrollment.
  name: Onboarding Automation
- description: Build custom learning channels with curated content for specific teams and roles.
  name: Content Curation
- description: Analyze commit, PR, and ticket data to measure and improve developer productivity.
  name: Developer Productivity
- description: Track practice exam scores and assessment results for certification readiness.
  name: Certification Tracking
---
