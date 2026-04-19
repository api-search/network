---
description: RotationRules schema from Amazon Secrets Manager API
layout: schema
name: RotationRules
properties_list:
- description: The number of days between automatic scheduled rotations.
  name: AutomaticallyAfterDays
  type: integer
- description: The length of the rotation window in hours.
  name: Duration
  type: string
- description: A cron or rate expression that defines the schedule for rotation.
  name: ScheduleExpression
  type: string
provider_name: Amazon Secrets Manager
provider_slug: amazon-secrets-manager
schema_file: json-schema/amazon-secrets-manager-rotation-rules-schema.json
slug: amazon-secrets-manager-rotation-rules
tags:
- AWS
- Configuration
- Credentials
- Rotation
- Secrets
- Security
title: RotationRules
---
