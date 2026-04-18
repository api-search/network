---
description: A Spot access policy defines a set of permissions that control what actions users and groups can perform on Spot platform services and resources.
layout: schema
name: Spot Access Policy
properties_list:
- description: The unique identifier of the access policy.
  name: id
  type: string
- description: The name of the access policy.
  name: name
  type: string
- description: A description of the access policy.
  name: description
  type: string
- description: The list of permissions granted by this policy.
  name: permissions
  type: array
provider_name: Spot
provider_slug: spot
schema_file: json-schema/access-policy.json
slug: access-policy
tags:
- Autoscaling
- Cloud Infrastructure
- Containers
- Cost Optimization
- FinOps
- Kubernetes
- Spot Instances
title: Spot Access Policy
---
