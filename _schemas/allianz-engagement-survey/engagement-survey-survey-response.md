---
description: An anonymized survey response submission
layout: schema
name: SurveyResponse
properties_list:
- description: Unique identifier for the response
  name: response_id
  type: string
- description: Survey this response belongs to
  name: survey_id
  type: string
- description: Timestamp when the response was submitted
  name: submitted_at
  type: string
- description: List of question answers
  name: answers
  type: array
provider_name: Allianz Engagement Survey
provider_slug: allianz-engagement-survey
schema_file: json-schema/engagement-survey-survey-response-schema.json
slug: engagement-survey-survey-response
tags:
- Analytics
- Enterprise
- Human Resources
- Insurance
- Surveys
- Employee Experience
title: SurveyResponse
---
