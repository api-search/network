---
description: Response from the RunInstances action
layout: schema
name: RunInstancesResponse
properties_list:
- description: The ID of the reservation
  name: reservationId
  type: string
- description: The ID of the AWS account that owns the reservation
  name: ownerId
  type: string
- description: The instances launched
  name: instances
  type: array
provider_name: Amazon EC2
provider_slug: amazon-ec2
schema_file: json-schema/ec2-openapi-run-instances-response-schema.json
slug: ec2-openapi-run-instances-response
tags:
- AWS
- Cloud Computing
- Compute
- IaaS
- Infrastructure
- Virtual Machines
title: RunInstancesResponse
---
