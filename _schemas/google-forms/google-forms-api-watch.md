---
description: A watch for receiving notifications about form changes or responses.
layout: schema
name: Watch
properties_list:
- description: Output only. The ID of this watch.
  name: id
  type: string
- description: The target for watch notifications.
  name: target
  type: object
- description: Which event type to watch for.
  name: eventType
  type: string
- description: Timestamp of when this was created.
  name: createTime
  type: string
- description: Timestamp for when this will expire.
  name: expireTime
  type: string
- description: ''
  name: errorType
  type: string
- description: ''
  name: state
  type: string
provider_name: Google Forms
provider_slug: google-forms
schema_file: json-schema/google-forms-api-watch-schema.json
slug: google-forms-api-watch
tags:
- Data Collection
- Forms
- Google
- Google Workspace
- Questionnaires
- Responses
- Surveys
title: Watch
---
