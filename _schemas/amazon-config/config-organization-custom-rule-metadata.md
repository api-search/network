---
description: organization custom rule metadata such as resource type, resource ID of Amazon Web Services resource, Lambda function ARN, and organization trigger types that trigger Config to evaluate your Amazon Web Services resources against a rule. It also provides the frequency with which you want Config to run evaluations for the rule if the trigger type is periodic.
layout: schema
name: OrganizationCustomRuleMetadata
properties_list:
- description: ''
  name: Description
  type: object
- description: ''
  name: LambdaFunctionArn
  type: object
- description: ''
  name: OrganizationConfigRuleTriggerTypes
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
schema_file: json-schema/config-organization-custom-rule-metadata-schema.json
slug: config-organization-custom-rule-metadata
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: OrganizationCustomRuleMetadata
---
