---
description: An action plan created to address survey findings
layout: schema
name: ActionPlan
properties_list:
- description: Unique identifier for the action plan
  name: plan_id
  type: string
- description: Survey this action plan relates to
  name: survey_id
  type: string
- description: Title of the action plan
  name: title
  type: string
- description: Detailed description of the planned actions
  name: description
  type: string
- description: Current status of the action plan
  name: status
  type: string
- description: Name of the action plan owner
  name: owner
  type: string
- description: Target completion date for the action plan
  name: due_date
  type: string
- description: Timestamp when the action plan was created
  name: created_at
  type: string
provider_name: Allianz Engagement Survey
provider_slug: allianz-engagement-survey
schema_file: json-schema/engagement-survey-action-plan-schema.json
slug: engagement-survey-action-plan
tags:
- Analytics
- Enterprise
- Human Resources
- Insurance
- Surveys
- Employee Experience
title: ActionPlan
---
