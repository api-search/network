---
description: Configuration for Indeed Apply integration on the job posting.
layout: schema
name: IndeedApplyConfig
properties_list:
- description: Whether Indeed Apply is enabled for this job posting.
  name: enabled
  type: boolean
- description: The URL where Indeed sends application data when a candidate applies through Indeed Apply.
  name: postUrl
  type: string
- description: Screener questions to present to candidates during application.
  name: screenerQuestions
  type: array
- description: Whether EEO compliance questions are enabled. Available for US employers only.
  name: eeoEnabled
  type: boolean
provider_name: Indeed
provider_slug: indeed
schema_file: json-schema/indeed-employer-indeed-apply-config-schema.json
slug: indeed-employer-indeed-apply-config
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
title: IndeedApplyConfig
---
