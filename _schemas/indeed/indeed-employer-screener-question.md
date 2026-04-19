---
description: A screener question configured on a job posting.
layout: schema
name: ScreenerQuestion
properties_list:
- description: Unique identifier for the screener question.
  name: id
  type: string
- description: The text of the question.
  name: question
  type: string
- description: The type of expected response.
  name: type
  type: string
- description: Whether the candidate must answer this question.
  name: required
  type: boolean
- description: Available options for select-type questions.
  name: options
  type: array
provider_name: Indeed
provider_slug: indeed
schema_file: json-schema/indeed-employer-screener-question-schema.json
slug: indeed-employer-screener-question
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
title: ScreenerQuestion
---
