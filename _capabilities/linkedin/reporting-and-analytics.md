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
- careers
- manages b2b ad campaigns and audience targeting on linkedin.
- employee development tracking and content access.
- learning
- business
- job posting, recruiting, and applicant tracking.
- integrates linkedin authentication and sharing into applications.
- reporting
- social media
- retrieve ad analytics by various pivots and dimensions.
- posts jobs and manages candidates through ats integrations.
- linkedin
- get ad analytics
- marketing
- data portability and advertiser transparency for dma.
- b2b advertising, audience targeting, and campaign analytics.
- analytics
- get learning activity reports
- uses sales navigator for lead generation and crm sync.
- retrieve learning activity reports.
- authentication, sharing, and verification for consumer apps.
- sales intelligence, lead management, and crm integration.
- tracks employee learning activity and completions.
- message archiving and regulatory communications governance.
- retrieve learning activity reports aggregated by account, group, individual, or content.
- archives communications for regulatory compliance.
- professional networking
- recruiting
- retrieve ad analytics by various pivots.
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
