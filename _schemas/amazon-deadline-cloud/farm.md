---
description: A render farm in Amazon Deadline Cloud that contains queues, fleets, and jobs.
layout: schema
name: Farm
properties_list:
- description: The unique identifier of the render farm
  name: farmId
  type: string
- description: ''
  name: displayName
  type: string
- description: ''
  name: description
  type: string
- description: The ARN of the KMS key. This ARN uniquely identifies the key.
  name: kmsKeyArn
  type: string
- description: ''
  name: createdAt
  type: string
provider_name: Amazon Deadline Cloud
provider_slug: amazon-deadline-cloud
schema_file: json-schema/farm-schema.json
slug: farm
tags:
- AWS
- Compute
- Media
- Rendering
- Visual Effects
title: Farm
---
