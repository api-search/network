---
description: A named collection of AWS resources to include in a Firewall Manager policy.
layout: schema
name: ResourceSet
properties_list:
- description: Unique resource set identifier.
  name: Id
  type: string
- description: Name of the resource set.
  name: Name
  type: string
- description: Optional description.
  name: Description
  type: string
- description: List of AWS resource types in the set.
  name: ResourceTypeList
  type: array
- description: Time the resource set was last updated.
  name: LastUpdateTime
  type: string
- description: Status of the resource set.
  name: ResourceSetStatus
  type: string
provider_name: Amazon Firewall Manager
provider_slug: amazon-firewall-manager
schema_file: json-schema/amazon-firewall-manager-resource-set-schema.json
slug: amazon-firewall-manager-resource-set
tags:
- AWS
- Compliance
- Firewall
- Network Security
- Security
title: ResourceSet
---
