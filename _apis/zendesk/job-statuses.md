---
aid: zendesk:job-statuses
baseURL: https://{subdomain}.zendesk.com
description: Zendesk Job Statuses is the mechanism and API resource that tracks long-running, asynchronous tasks kicked off in Zendesksuch as bulk ticket updates, user or organization imports, and other create/update many operations. Instead of waiting for a synchronous response, these endpoints return a job ID that you can poll to see whether the work is queued, in progress, or completed, along with progress counts, result details, and any errors.
humanURL: https://developer.zendesk.com/api-reference/ticketing/ticket-management/job_statuses/
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Zendesk Job Statuses
properties:
- type: Documentation
  url: https://developer.zendesk.com/api-reference/ticketing/ticket-management/job_statuses/
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/openapi/job-statuses-openapi-original.yml
provider_name: Zendesk
provider_slug: zendesk
slug: job-statuses
tags:
- Jobs
- Statuses
---
