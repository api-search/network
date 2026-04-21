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
- business
- b2b advertising, audience targeting, and campaign analytics.
- retrieve learning activity reports aggregated by account, group, individual, or content.
- sales intelligence, lead management, and crm integration.
- retrieve learning activity reports.
- analytics
- retrieve ad analytics by various pivots.
- job posting, recruiting, and applicant tracking.
- reporting
- uses sales navigator for lead generation and crm sync.
- archives communications for regulatory compliance.
- message archiving and regulatory communications governance.
- careers
- manages b2b ad campaigns and audience targeting on linkedin.
- linkedin
- recruiting
- retrieve ad analytics by various pivots and dimensions.
- authentication, sharing, and verification for consumer apps.
- professional networking
- get ad analytics
- learning
- get learning activity reports
- posts jobs and manages candidates through ats integrations.
- marketing
- social media
- data portability and advertiser transparency for dma.
- tracks employee learning activity and completions.
- integrates linkedin authentication and sharing into applications.
- employee development tracking and content access.
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
