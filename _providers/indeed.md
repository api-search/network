---
api_count: 14
apis:
- description: Search for jobs by keyword, location, and other criteria. Returns job listings with details including title, company, location, and description. This API is deprecated and not available for new integr
  name: Indeed Job Search API
  slug: job-search
- description: Monetize your website by displaying Indeed job listings. Earn revenue through cost-per-click advertising.
  name: Indeed Publisher API
  slug: publisher
- description: Allow job seekers to apply to your jobs directly through Indeed with a streamlined application process. Supports screener questions, EEO compliance for US employers, and disposition data integration.
  name: Indeed Apply API
  slug: apply
- description: A GraphQL API that enables ATS partners to create, upsert, expire, and get status for job postings on Indeed. Supports qualifications, working hours, salary, benefits, and employer information.
  name: Indeed Job Sync API
  slug: job-sync
- description: A GraphQL API that enables ATS partners to send disposition data for Indeed Apply and non-Indeed Apply jobs to Indeed, tracking application status changes through various stages of the hiring process.
  name: Indeed Disposition Sync API
  slug: disposition-sync
- description: A GraphQL API used to get information about and manage an employer's sponsored job campaigns on Indeed, including campaign creation, budget management, and performance insights.
  name: Indeed Sponsored Jobs API
  slug: sponsored-jobs
- description: Allows partners to list and update job postings on Indeed, including adding metadata to ATS-sourced jobs for improved quality and sponsorship grouping, and subscribing to jobs lifecycle events via web
  name: Indeed Job Update API
  slug: job-update
- description: Stream real-time server-sent events (SSE) to enable front-end applications to update instantly, supporting event filtering, deduplication, and latency tracking.
  name: Indeed Real-time API
  slug: real-time
- description: A GraphQL API for scheduling, updating, retrieving information about, and canceling virtual interview events with job candidates. This API is deprecated.
  name: Indeed Interview API
  slug: interview
- description: A RESTful abstraction of Indeed's employer-facing partner APIs, providing unified access to employer management, candidate retrieval, and job posting operations.
  name: Indeed Employer API
  slug: employer
- description: A GraphQL API for creating and updating employer entities on Indeed and the Indeed PLUS platform.
  name: Indeed Employer Data API
  slug: employer-data
- description: Tracks candidate events such as job application page visits and completed applications from Indeed to your site. Provides data for reporting, analytics dashboards, and apply-based bidding algorithms.
  name: Indeed Conversion Tracking API
  slug: conversion-tracking
- description: Part of the Candidate Sync APIs, this API allows ATS partners to register employers for Candidate Sync integration.
  name: Indeed Employer Registration API
  slug: employer-registration
- description: Part of the Candidate Sync APIs, this API enables ATS partners to get candidate and application information from Indeed on behalf of employers.
  name: Indeed Retrieve Candidates API
  slug: retrieve-candidates
capabilities:
- description: Unified workflow for managing the hiring pipeline including employer setup, job posting, candidate retrieval, and disposition tracking. Used by ATS partners and hiring platform developers.
  name: Indeed Talent Acquisition
  slug: talent-acquisition
common:
- title: ''
  type: DeveloperPortal
  url: https://opensource.indeedeng.io/
- title: ''
  type: TermsOfService
  url: https://www.indeed.com/legal/terms-of-service
- title: ''
  type: PrivacyPolicy
  url: https://www.indeed.com/legal/privacy
- title: ''
  type: StatusPage
  url: https://status.indeed.com
- title: ''
  type: Support
  url: https://support.indeed.com/hc/en-us
- title: ''
  type: Blog
  url: https://engineering.indeedblog.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/indeedeng
- title: ''
  type: X
  url: https://twitter.com/indeedeng
- title: ''
  type: RateLimits
  url: https://opensource.indeedeng.io/api-documentation/docs/rate-limits
- title: ''
  type: Authentication
  url: https://docs.indeed.com/authorization/
- title: ''
  type: GettingStarted
  url: https://docs.indeed.com/getstarted/
- title: ''
  type: ReleaseNotes
  url: https://docs.indeed.com/release-notes/
- title: ''
  type: Sandbox
  url: https://docs.indeed.com/getstarted/simulated-graphql-environment
- title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/indeed-com/
- title: Employer API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/employer-api.yaml
- title: Talent Acquisition Workflow
  type: NaftikoCapability
  url: capabilities/talent-acquisition.yaml
created: '2025-01-01'
description: Indeed is the world's largest job site, connecting millions of job seekers with employers across industries and locations worldwide. Indeed offers a suite of APIs for applicant tracking systems, job boards, and hiring platforms to integrate with its employment ecosystem.
features:
- description: Search millions of job listings by keyword, location, salary, and other criteria across industries worldwide.
  name: Job Search and Discovery
- description: Post and syndicate job listings from ATS platforms to Indeed's marketplace with automated synchronization.
  name: Job Posting and Syndication
- description: Retrieve and manage candidate applications, track disposition status, and sync hiring data with ATS systems.
  name: Candidate Management
- description: Create and manage pay-per-click sponsored job campaigns with budget controls and performance analytics.
  name: Sponsored Job Campaigns
- description: Enable one-click job applications directly through Indeed with screener questions and EEO compliance.
  name: Indeed Apply Integration
- description: Track candidate events from Indeed to employer sites for analytics, reporting, and bidding optimization.
  name: Conversion Tracking
- description: Stream server-sent events for instant application updates and job lifecycle notifications.
  name: Real-Time Event Streaming
image: https://www.indeed.com/images/indeed-logo.png
integrations:
- description: Native ATS integration for job posting synchronization and candidate data exchange with Greenhouse.
  name: Greenhouse
- description: Pre-built integration for posting jobs and retrieving candidate applications through Lever ATS.
  name: Lever
- description: Enterprise integration for syncing job postings and candidate data with Workday Recruiting.
  name: Workday
- description: Integration for job distribution and candidate management through iCIMS talent acquisition platform.
  name: iCIMS
- description: Connector for job posting and candidate synchronization with SAP SuccessFactors Recruiting.
  name: SAP SuccessFactors
- description: Integration for distributing jobs and managing candidates through Oracle Taleo ATS.
  name: Oracle Taleo
jsonld:
- class_count: 0
  name: Indeed Context
  property_count: 14
  slug: indeed-context
- class_count: 0
  name: Indeed Employer Context
  property_count: 0
  slug: indeed-employer-context
layout: provider
modified: '2026-04-18'
name: Indeed
rules:
- name: Indeed API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: indeed-spectral-rules
skills: []
slug: indeed
solutions: []
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
url: https://raw.githubusercontent.com/api-evangelist/indeed/refs/heads/main/apis.yml
use_cases:
- description: Automatically distribute job postings from applicant tracking systems to Indeed's marketplace with real-time synchronization.
  name: ATS Job Distribution
- description: Retrieve and manage candidates through the hiring pipeline with disposition tracking and status updates.
  name: Candidate Pipeline Management
- description: Track campaign performance, application conversions, and ROI across sponsored and organic job listings.
  name: Recruitment Marketing Analytics
- description: Create and manage employer profiles on Indeed to attract candidates with company information and branding.
  name: Employer Branding
- description: Scale recruitment operations with automated job posting, candidate retrieval, and application processing.
  name: High-Volume Hiring
---
