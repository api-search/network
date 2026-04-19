---
description: Score summary for a single survey question
layout: schema
name: QuestionScore
properties_list:
- description: Question identifier
  name: question_id
  type: string
- description: The survey question text
  name: question
  type: string
- description: Average score on a 1-5 scale
  name: score
  type: number
- description: Percentage of favorable responses (4-5 on Likert scale)
  name: favorable
  type: number
provider_name: Allianz Engagement Survey
provider_slug: allianz-engagement-survey
schema_file: json-schema/engagement-survey-question-score-schema.json
slug: engagement-survey-question-score
tags:
- Analytics
- Enterprise
- Human Resources
- Insurance
- Surveys
- Employee Experience
title: QuestionScore
---
