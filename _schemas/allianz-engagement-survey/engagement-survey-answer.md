---
description: An individual question answer within a survey response
layout: schema
name: Answer
properties_list:
- description: Identifier of the question being answered
  name: question_id
  type: string
- description: Numeric score on a 1-5 Likert scale
  name: score
  type: integer
- description: Open text response for free-text questions
  name: text_response
  type: string
provider_name: Allianz Engagement Survey
provider_slug: allianz-engagement-survey
schema_file: json-schema/engagement-survey-answer-schema.json
slug: engagement-survey-answer
tags:
- Analytics
- Enterprise
- Human Resources
- Insurance
- Surveys
- Employee Experience
title: Answer
---
