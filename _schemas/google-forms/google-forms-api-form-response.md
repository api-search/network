---
description: A response to a Google Form.
layout: schema
name: FormResponse
properties_list:
- description: Output only. The form ID.
  name: formId
  type: string
- description: Output only. The response ID.
  name: responseId
  type: string
- description: Timestamp for the first time the response was submitted.
  name: createTime
  type: string
- description: Timestamp for the most recent submission.
  name: lastSubmittedTime
  type: string
- description: The email address of the respondent.
  name: respondentEmail
  type: string
- description: The actual answers keyed by question ID.
  name: answers
  type: object
- description: Total points awarded for quiz forms.
  name: totalScore
  type: number
provider_name: Google Forms
provider_slug: google-forms
schema_file: json-schema/google-forms-api-form-response-schema.json
slug: google-forms-api-form-response
tags:
- Data Collection
- Forms
- Google
- Google Workspace
- Questionnaires
- Responses
- Surveys
title: FormResponse
---
