---
description: An error returned by the Indeed API.
layout: schema
name: ApiError
properties_list:
- description: A machine-readable error code.
  name: code
  type: string
- description: A human-readable description of the error.
  name: message
  type: string
- description: The field that caused the error, if applicable.
  name: field
  type: string
provider_name: Indeed
provider_slug: indeed
schema_file: json-schema/indeed-employer-api-error-schema.json
slug: indeed-employer-api-error
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
title: ApiError
---
