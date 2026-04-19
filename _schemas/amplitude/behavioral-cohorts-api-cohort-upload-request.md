---
description: CohortUploadRequest schema from Amplitude Behavioral Cohorts API
layout: schema
name: CohortUploadRequest
properties_list:
- description: The name of the cohort to create or update.
  name: name
  type: string
- description: Array of user_id or amplitude_id values to include in the cohort.
  name: ids
  type: array
- description: The email address of the cohort owner.
  name: owner
  type: string
- description: If provided, updates the existing cohort with this ID instead of creating a new one.
  name: existing_cohort_id
  type: string
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/behavioral-cohorts-api-cohort-upload-request-schema.json
slug: behavioral-cohorts-api-cohort-upload-request
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: CohortUploadRequest
---
