---
description: A Spot account represents a logical unit within an organization, typically mapped to a cloud provider account or subscription for managing infrastructure resources.
layout: schema
name: Spot Account
properties_list:
- description: The unique identifier of the account.
  name: id
  type: string
- description: The name of the account.
  name: name
  type: string
- description: The identifier of the parent organization.
  name: organizationId
  type: string
- description: The linked cloud provider account identifier.
  name: cloudAccountId
  type: string
- description: The external ID used for cloud provider trust relationships.
  name: providerExternalId
  type: string
provider_name: Spot
provider_slug: spot
schema_file: json-schema/account.json
slug: account
tags:
- Autoscaling
- Cloud Infrastructure
- Containers
- Cost Optimization
- FinOps
- Kubernetes
- Spot Instances
title: Spot Account
---
