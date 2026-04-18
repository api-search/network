---
description: LearningActivity from LinkedIn API
layout: schema
name: LearningActivity
properties_list:
- description: Type of engagement activity
  name: engagementType
  type: string
- description: Numeric value of the engagement
  name: engagementValue
  type: integer
- description: Whether the metric is unique or total count
  name: engagementMetricQualifier
  type: string
- description: Type of learning asset
  name: assetType
  type: string
- description: Timestamp of first engagement
  name: firstEngagedAt
  type: integer
- description: Timestamp of last engagement
  name: lastEngagedAt
  type: integer
provider_name: LinkedIn
provider_slug: linkedin
schema_file: json-schema/linkedin-learning-activity-reports-learning-activity-schema.json
slug: linkedin-learning-activity-reports-learning-activity
tags:
- Business
- Careers
- Marketing
- Professional Networking
- Recruiting
- Social Media
title: LearningActivity
---
