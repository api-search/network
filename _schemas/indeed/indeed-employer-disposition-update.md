---
description: An update to the disposition (application status) of a candidate for a specific job posting. Used to sync hiring pipeline status changes back to Indeed.
layout: schema
name: DispositionUpdate
properties_list:
- description: The unique identifier for the application.
  name: applicationId
  type: string
- description: The new disposition status for the application. Must be one of Indeed's predefined categories.
  name: status
  type: string
- description: The timestamp when the status change occurred.
  name: statusUpdatedAt
  type: string
- description: The reason for rejection, if the status is REJECTED.
  name: rejectionReason
  type: string
provider_name: Indeed
provider_slug: indeed
schema_file: json-schema/indeed-employer-disposition-update-schema.json
slug: indeed-employer-disposition-update
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
title: DispositionUpdate
---
