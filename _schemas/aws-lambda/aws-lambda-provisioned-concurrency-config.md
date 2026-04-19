---
description: Provisioned concurrency configuration for a function
layout: schema
name: ProvisionedConcurrencyConfig
properties_list:
- description: The amount of provisioned concurrency requested
  name: RequestedProvisionedConcurrentExecutions
  type: integer
- description: The amount of provisioned concurrency available
  name: AvailableProvisionedConcurrentExecutions
  type: integer
- description: The amount of provisioned concurrency allocated
  name: AllocatedProvisionedConcurrentExecutions
  type: integer
- description: The status of the allocation
  name: Status
  type: string
- description: For failed allocations, the reason the status is FAILED
  name: StatusReason
  type: string
- description: The date and time the configuration was last modified
  name: LastModified
  type: string
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-provisioned-concurrency-config-schema.json
slug: aws-lambda-provisioned-concurrency-config
tags: []
title: ProvisionedConcurrencyConfig
---
