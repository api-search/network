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
- get ad analytics
- retrieve learning activity reports aggregated by account, group, individual, or content.
- integrates linkedin authentication and sharing into applications.
- posts jobs and manages candidates through ats integrations.
- analytics
- business
- learning
- employee development tracking and content access.
- social media
- get learning activity reports
- marketing
- job posting, recruiting, and applicant tracking.
- manages b2b ad campaigns and audience targeting on linkedin.
- tracks employee learning activity and completions.
- retrieve ad analytics by various pivots and dimensions.
- linkedin
- retrieve learning activity reports.
- careers
- authentication, sharing, and verification for consumer apps.
- archives communications for regulatory compliance.
- message archiving and regulatory communications governance.
- sales intelligence, lead management, and crm integration.
- recruiting
- retrieve ad analytics by various pivots.
- uses sales navigator for lead generation and crm sync.
- professional networking
- reporting
- b2b advertising, audience targeting, and campaign analytics.
- data portability and advertiser transparency for dma.
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
