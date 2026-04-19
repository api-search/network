---
description: An employee engagement survey definition
layout: schema
name: Survey
properties_list:
- description: Unique identifier for the survey
  name: survey_id
  type: string
- description: Title of the survey
  name: title
  type: string
- description: Type of engagement survey
  name: survey_type
  type: string
- description: Current lifecycle status of the survey
  name: status
  type: string
- description: Description of the survey purpose and scope
  name: description
  type: string
- description: Date when the survey becomes available to participants
  name: start_date
  type: string
- description: Date when the survey closes
  name: end_date
  type: string
- description: Timestamp when the survey was created
  name: created_at
  type: string
- description: Timestamp when the survey was last modified
  name: modified_at
  type: string
provider_name: Allianz Engagement Survey
provider_slug: allianz-engagement-survey
schema_file: json-schema/engagement-survey-survey-schema.json
slug: engagement-survey-survey
tags:
- Analytics
- Enterprise
- Human Resources
- Insurance
- Surveys
- Employee Experience
title: Survey
---
