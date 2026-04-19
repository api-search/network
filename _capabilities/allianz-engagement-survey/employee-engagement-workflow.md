---
consumed_apis:
- allianz-engagement-survey
description: Workflow capability for HR teams running employee engagement surveys at Allianz, covering survey planning, participant management, results analysis, and action plan tracking.
layout: capability
name: Allianz Employee Engagement Workflow
operations:
- description: List all engagement surveys
  method: GET
  name: list-surveys
  path: /v1/surveys
- description: Create a new engagement survey
  method: POST
  name: create-survey
  path: /v1/surveys
- description: List participants and response status
  method: GET
  name: list-participants
  path: /v1/surveys/{survey_id}/participants
- description: Add employees as survey participants
  method: POST
  name: add-participants
  path: /v1/surveys/{survey_id}/participants
- description: Get engagement analytics for a survey
  method: GET
  name: get-analytics
  path: /v1/surveys/{survey_id}/analytics
- description: List action plans for a survey
  method: GET
  name: list-action-plans
  path: /v1/surveys/{survey_id}/action-plans
- description: Create an action plan from survey insights
  method: POST
  name: create-action-plan
  path: /v1/surveys/{survey_id}/action-plans
personas: []
provider_name: Allianz Engagement Survey
provider_slug: allianz-engagement-survey
search_terms:
- list all engagement surveys
- hr professional responsible for running engagement surveys and following up with business units
- end-to-end workflow for hr teams running engagement surveys
- HR Business Partner
- list action plans
- get analytics
- create action plan
- create engagement survey
- employee experience
- add employees as survey participants
- Team Manager
- insurance
- create an action plan to address employee engagement survey findings
- survey analytics and reporting
- people manager who reviews team-level results and creates action plans
- analyst who interprets engagement data and generates insights and recommendations
- list participants and response status
- get survey analytics
- human resources
- survey management for hr teams
- create survey
- list improvement action plans created from survey findings
- list surveys
- participant management for a survey
- list engagement surveys
- surveys
- analytics
- create an action plan from survey insights
- list action plans for a survey
- get details and configuration of a specific engagement survey
- analyzing survey results and generating engagement insights
- get aggregated engagement scores, participation rates, and insights for a survey
- list all allianz employee engagement surveys with status and type filtering
- list participants and track who has responded to a survey
- create a new annual, pulse, onboarding, or exit engagement survey
- creating and tracking improvement initiatives from survey findings
- get engagement analytics for a survey
- add participants
- list participants
- add survey participants
- enterprise
- create a new engagement survey
- list survey participants
- action plan management
- creating and managing employee engagement surveys
- add employees to a survey and send invitation emails
- get engagement survey
- People Analytics Analyst
slug: employee-engagement-workflow
tags:
- Human Resources
- Employee Experience
- Surveys
- Analytics
tools:
- description: List all Allianz employee engagement surveys with status and type filtering
  hints:
    openWorld: false
    readOnly: true
  name: list-engagement-surveys
- description: Create a new annual, pulse, onboarding, or exit engagement survey
  hints:
    openWorld: false
    readOnly: false
  name: create-engagement-survey
- description: Get details and configuration of a specific engagement survey
  hints:
    openWorld: false
    readOnly: true
  name: get-engagement-survey
- description: List participants and track who has responded to a survey
  hints:
    openWorld: false
    readOnly: true
  name: list-survey-participants
- description: Add employees to a survey and send invitation emails
  hints:
    openWorld: false
    readOnly: false
  name: add-survey-participants
- description: Get aggregated engagement scores, participation rates, and insights for a survey
  hints:
    openWorld: false
    readOnly: true
  name: get-survey-analytics
- description: List improvement action plans created from survey findings
  hints:
    openWorld: false
    readOnly: true
  name: list-action-plans
- description: Create an action plan to address employee engagement survey findings
  hints:
    openWorld: false
    readOnly: false
  name: create-action-plan
---
