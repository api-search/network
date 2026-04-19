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
- social media
- careers
- message archiving and regulatory communications governance.
- integrates linkedin authentication and sharing into applications.
- analytics
- posts jobs and manages candidates through ats integrations.
- uses sales navigator for lead generation and crm sync.
- get learning activity reports
- authentication, sharing, and verification for consumer apps.
- employee development tracking and content access.
- archives communications for regulatory compliance.
- sales intelligence, lead management, and crm integration.
- retrieve learning activity reports.
- learning
- get ad analytics
- data portability and advertiser transparency for dma.
- retrieve ad analytics by various pivots and dimensions.
- manages b2b ad campaigns and audience targeting on linkedin.
- retrieve ad analytics by various pivots.
- business
- professional networking
- recruiting
- reporting
- marketing
- tracks employee learning activity and completions.
- linkedin
- b2b advertising, audience targeting, and campaign analytics.
- retrieve learning activity reports aggregated by account, group, individual, or content.
- job posting, recruiting, and applicant tracking.
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
