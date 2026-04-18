---
consumed_apis:
- marketing-reporting-roi
- learning-activity-reports
description: Unified workflow for marketing analysts to access ad analytics, B2B metrics, learning activity reports, and performance data -- combining reporting/ROI and learning activity APIs.
layout: capability
name: LinkedIn Reporting And Analytics
operations:
- description: Retrieve ad analytics by various pivots.
  method: GET
  name: get-ad-analytics
  path: /v1/ad-analytics
- description: Retrieve learning activity reports.
  method: GET
  name: get-learning-activity-reports
  path: /v1/learning-activity-reports
personas: []
provider_name: LinkedIn
provider_slug: linkedin
search_terms:
- retrieve learning activity reports aggregated by account, group, individual, or content.
- business
- learning
- retrieve ad analytics by various pivots.
- manages b2b ad campaigns and audience targeting on linkedin.
- tracks employee learning activity and completions.
- posts jobs and manages candidates through ats integrations.
- get ad analytics
- b2b advertising, audience targeting, and campaign analytics.
- integrates linkedin authentication and sharing into applications.
- social media
- reporting
- professional networking
- marketing
- message archiving and regulatory communications governance.
- archives communications for regulatory compliance.
- get learning activity reports
- analytics
- recruiting
- job posting, recruiting, and applicant tracking.
- data portability and advertiser transparency for dma.
- employee development tracking and content access.
- retrieve learning activity reports.
- retrieve ad analytics by various pivots and dimensions.
- sales intelligence, lead management, and crm integration.
- uses sales navigator for lead generation and crm sync.
- linkedin
- careers
- authentication, sharing, and verification for consumer apps.
slug: reporting-and-analytics
tags:
- LinkedIn
- Reporting
- Analytics
- Learning
tools:
- description: Retrieve ad analytics by various pivots and dimensions.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-ad-analytics
- description: Retrieve learning activity reports aggregated by account, group, individual, or content.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-learning-activity-reports
---
