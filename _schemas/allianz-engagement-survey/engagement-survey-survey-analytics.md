---
description: Aggregated analytics and insights for an engagement survey
layout: schema
name: SurveyAnalytics
properties_list:
- description: Survey being analyzed
  name: survey_id
  type: string
- description: Percentage of invited employees who responded
  name: participation_rate
  type: number
- description: Overall engagement score out of 100
  name: engagement_score
  type: number
- description: Percentage of favorable responses across all questions
  name: favorable_percentage
  type: number
- description: Per-question score breakdown
  name: question_scores
  type: array
provider_name: Allianz Engagement Survey
provider_slug: allianz-engagement-survey
schema_file: json-schema/engagement-survey-survey-analytics-schema.json
slug: engagement-survey-survey-analytics
tags:
- Analytics
- Enterprise
- Human Resources
- Insurance
- Surveys
- Employee Experience
title: SurveyAnalytics
---
