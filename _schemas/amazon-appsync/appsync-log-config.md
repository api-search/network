---
description: Logging configuration for a GraphQL API
layout: schema
name: LogConfig
properties_list:
- description: CloudWatch Logs role ARN
  name: cloudWatchLogsRoleArn
  type: string
- description: Field log level
  name: fieldLogLevel
  type: string
- description: Whether to exclude verbose content
  name: excludeVerboseContent
  type: boolean
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-log-config-schema.json
slug: appsync-log-config
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: LogConfig
---
