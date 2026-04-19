---
description: A survey participant record
layout: schema
name: Participant
properties_list:
- description: Unique identifier for the participant record
  name: participant_id
  type: string
- description: Allianz employee identifier
  name: employee_id
  type: string
- description: Current response status of the participant
  name: status
  type: string
- description: Timestamp when the invitation was sent
  name: invited_at
  type: string
- description: Timestamp when the participant submitted their response
  name: responded_at
  type: string
provider_name: Allianz Engagement Survey
provider_slug: allianz-engagement-survey
schema_file: json-schema/engagement-survey-participant-schema.json
slug: engagement-survey-participant
tags:
- Analytics
- Enterprise
- Human Resources
- Insurance
- Surveys
- Employee Experience
title: Participant
---
