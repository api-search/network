---
description: Represents information about a provisioned resource.
layout: schema
name: ResourceDescription
properties_list:
- description: The primary identifier for the resource.
  name: Identifier
  type: string
- description: A JSON string representing the current resource property values. The properties returned depend on the resource type schema.
  name: Properties
  type: string
provider_name: AWS CloudFormation
provider_slug: cloudformation
schema_file: json-schema/cloud-control-resource-description-schema.json
slug: cloud-control-resource-description
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
title: ResourceDescription
---
