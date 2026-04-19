---
description: Paginated list of engagement surveys
layout: schema
name: SurveyList
properties_list:
- description: Total number of surveys matching the filter
  name: total
  type: integer
- description: Current pagination offset
  name: offset
  type: integer
- description: Maximum number returned per page
  name: limit
  type: integer
- description: List of survey objects
  name: items
  type: array
provider_name: Allianz Engagement Survey
provider_slug: allianz-engagement-survey
schema_file: json-schema/engagement-survey-survey-list-schema.json
slug: engagement-survey-survey-list
tags:
- Analytics
- Enterprise
- Human Resources
- Insurance
- Surveys
- Employee Experience
title: SurveyList
---
