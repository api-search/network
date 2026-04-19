---
description: Request body for creating a new action plan
layout: schema
name: CreateActionPlanRequest
properties_list:
- description: Title of the action plan
  name: title
  type: string
- description: Description of planned actions
  name: description
  type: string
- description: Employee ID of the action plan owner
  name: owner_employee_id
  type: string
- description: Target completion date
  name: due_date
  type: string
provider_name: Allianz Engagement Survey
provider_slug: allianz-engagement-survey
schema_file: json-schema/engagement-survey-create-action-plan-request-schema.json
slug: engagement-survey-create-action-plan-request
tags:
- Analytics
- Enterprise
- Human Resources
- Insurance
- Surveys
- Employee Experience
title: CreateActionPlanRequest
---
