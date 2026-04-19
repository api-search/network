---
description: Schema for an AWS Config rule resource, representing a compliance rule that evaluates whether AWS resources conform to desired configurations.
layout: schema
name: AWS Config Rule
properties_list:
- description: The name that you assign to the AWS Config rule.
  name: ConfigRuleName
  type: string
- description: The ARN of the AWS Config rule.
  name: ConfigRuleArn
  type: string
- description: The ID of the AWS Config rule.
  name: ConfigRuleId
  type: string
- description: The description that you provide for the AWS Config rule.
  name: Description
  type: string
- description: Defines which resources trigger an evaluation for the rule.
  name: Scope
  type: object
- description: Provides the rule owner, rule identifier, and notifications that cause the function to evaluate your AWS resources.
  name: Source
  type: object
- description: A string, in JSON format, that is passed to the AWS Config rule Lambda function.
  name: InputParameters
  type: string
- description: The maximum frequency with which AWS Config runs evaluations for a rule.
  name: MaximumExecutionFrequency
  type: string
- description: Indicates whether the AWS Config rule is active or is currently being deleted.
  name: ConfigRuleState
  type: string
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/amazon-config-rule-schema.json
slug: amazon-config-rule
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: AWS Config Rule
---
