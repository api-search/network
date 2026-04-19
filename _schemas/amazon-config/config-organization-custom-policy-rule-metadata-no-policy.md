---
description: metadata for your organization Config Custom Policy rule including the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata such as resource type, resource ID of Amazon Web Services resource, and organization trigger types that trigger Config to evaluate Amazon Web Services resources against a rule.
layout: schema
name: OrganizationCustomPolicyRuleMetadataNoPolicy
properties_list:
- description: ''
  name: Description
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
- description: ''
  name: PolicyRuntime
  type: object
- description: ''
  name: DebugLogDeliveryAccounts
  type: object
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/config-organization-custom-policy-rule-metadata-no-policy-schema.json
slug: config-organization-custom-policy-rule-metadata-no-policy
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: OrganizationCustomPolicyRuleMetadataNoPolicy
---
