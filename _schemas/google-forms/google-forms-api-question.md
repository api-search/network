---
description: A question in a Google Form.
layout: schema
name: Question
properties_list:
- description: Output only. The ID of the question.
  name: questionId
  type: string
- description: Whether the question must be answered.
  name: required
  type: boolean
- description: ''
  name: grading
  type: object
- description: ''
  name: choiceQuestion
  type: object
- description: ''
  name: textQuestion
  type: object
- description: ''
  name: scaleQuestion
  type: object
- description: ''
  name: dateQuestion
  type: object
- description: ''
  name: timeQuestion
  type: object
provider_name: Google Forms
provider_slug: google-forms
schema_file: json-schema/google-forms-api-question-schema.json
slug: google-forms-api-question
tags:
- Data Collection
- Forms
- Google
- Google Workspace
- Questionnaires
- Responses
- Surveys
title: Question
---
