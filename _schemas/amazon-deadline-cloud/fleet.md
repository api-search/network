---
description: A compute fleet in a render farm providing worker capacity for jobs.
layout: schema
name: Fleet
properties_list:
- description: The unique identifier of the fleet
  name: fleetId
  type: string
- description: ''
  name: farmId
  type: string
- description: ''
  name: displayName
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: workerCount
  type: integer
- description: The ARN of the IAM role for the fleet
  name: roleArn
  type: string
- description: ''
  name: createdAt
  type: string
provider_name: Amazon Deadline Cloud
provider_slug: amazon-deadline-cloud
schema_file: json-schema/fleet-schema.json
slug: fleet
tags:
- AWS
- Compute
- Media
- Rendering
- Visual Effects
title: Fleet
---
