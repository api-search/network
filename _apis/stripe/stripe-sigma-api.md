---
aid: stripe:stripe-sigma-api
name: Stripe Sigma API
tags:
  - Queries
  - Runs
  - Scheduled
properties:
  - url: https://stripe.com/docs/api/sigma/scheduled_queries
    type: Documentation
  - url: openapi/sigma-openapi-original.yml
    type: OpenAPI
description: >-
  If you have scheduled a Sigma query, you'll receive a
  sigma.scheduled_query_run.created webhook each time the query runs. The
  webhook contains a ScheduledQueryRun object, which you can use to retrieve the
  query results.

---