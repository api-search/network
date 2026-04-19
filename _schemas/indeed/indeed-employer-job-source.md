---
description: Information about the source system for the job posting, used to identify the originating ATS or job board.
layout: schema
name: JobSource
properties_list:
- description: The name of the source system. Must remain consistent across all job postings from the same source.
  name: sourceName
  type: string
- description: The URL of the original job posting on the source system.
  name: sourceUrl
  type: string
provider_name: Indeed
provider_slug: indeed
schema_file: json-schema/indeed-employer-job-source-schema.json
slug: indeed-employer-job-source
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
title: JobSource
---
