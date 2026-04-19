---
description: organization managed rule metadata such as resource type and ID of Amazon Web Services resource along with the rule identifier. It also provides the frequency with which you want Config to run evaluations for the rule if the trigger type is periodic.
layout: schema
name: OrganizationManagedRuleMetadata
properties_list:
- description: ''
  name: Description
  type: object
- description: ''
  name: RuleIdentifier
  type: object
- description: ''
  name: InputParameters
  type: object
- description: ''
  name: MaximumExecutionFrequency
  type: object
- description: ''
  name: ResourceTypesScope
  type: object
- description: ''
  name: ResourceIdScope
  type: object
- description: ''
  name: TagKeyScope
  type: object
- description: ''
  name: TagValueScope
  type: object
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/config-organization-managed-rule-metadata-schema.json
slug: config-organization-managed-rule-metadata
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: OrganizationManagedRuleMetadata
---
