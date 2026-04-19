---
description: The request object for sending user feedback on Cortex Analyst responses
layout: schema
name: SendFeedbackRequest
properties_list:
- description: Request id associated with the feedback
  name: request_id
  type: string
- description: Whether the response was good (true) or bad (false)
  name: positive
  type: boolean
- description: The text for the detailed feedback message
  name: feedback_message
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-analyst-send-feedback-request-schema.json
slug: cortex-analyst-send-feedback-request
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: SendFeedbackRequest
---
