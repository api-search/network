---
description: A Spot user represents an individual or programmatic identity with permissions to access and manage resources within a Spot organization.
layout: schema
name: Spot User
properties_list:
- description: The unique identifier of the user.
  name: userId
  type: string
- description: The username of the user.
  name: username
  type: string
- description: The email address of the user.
  name: email
  type: string
- description: The first name of the user.
  name: firstName
  type: string
- description: The last name of the user.
  name: lastName
  type: string
- description: The type of user, either a human user or programmatic API user.
  name: type
  type: string
- description: The role assigned to the user within an account.
  name: role
  type: string
- description: The identifier of the organization the user belongs to.
  name: organizationId
  type: string
provider_name: Spot
provider_slug: spot
schema_file: json-schema/user.json
slug: user
tags:
- Autoscaling
- Cloud Infrastructure
- Containers
- Cost Optimization
- FinOps
- Kubernetes
- Spot Instances
title: Spot User
---
