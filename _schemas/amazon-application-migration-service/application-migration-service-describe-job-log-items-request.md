---
description: Request to describe job log items
layout: schema
name: DescribeJobLogItemsRequest
properties_list:
- description: Job ID to get log items for
  name: jobID
  type: string
- description: Maximum results to return
  name: maxResults
  type: integer
- description: Pagination token
  name: nextToken
  type: string
- description: Account ID for cross-account access
  name: accountID
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-describe-job-log-items-request-schema.json
slug: application-migration-service-describe-job-log-items-request
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: DescribeJobLogItemsRequest
---
