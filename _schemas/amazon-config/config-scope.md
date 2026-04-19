---
description: Defines which resources trigger an evaluation for an Config rule. The scope can include one or more resource types, a combination of a tag key and value, or a combination of one resource type and one resource ID. Specify a scope to constrain which resources trigger an evaluation for a rule. Otherwise, evaluations for the rule are triggered when any resource in your recording group changes in configuration.
layout: schema
name: Scope
properties_list:
- description: ''
  name: ComplianceResourceTypes
  type: object
- description: ''
  name: TagKey
  type: object
- description: ''
  name: TagValue
  type: object
- description: ''
  name: ComplianceResourceId
  type: object
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/config-scope-schema.json
slug: config-scope
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: Scope
---
