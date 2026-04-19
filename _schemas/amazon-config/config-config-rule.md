---
description: '<p>Config rules evaluate the configuration settings of your Amazon Web Services resources. A rule can run when Config detects a configuration change to an Amazon Web Services resource or at a periodic frequency that you choose (for example, every 24 hours). There are two types of rules: <i>Config Managed Rules</i> and <i>Config Custom Rules</i>.</p> <p>Config Managed Rules are predefined, customizable rules created by Config. For a list of managed rules, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html">List of Config Managed Rules</a>.</p> <p>Config Custom Rules are rules that you create from scratch. There are two ways to create Config custom rules: with Lambda functions (<a href="https://docs.aws.amazon.com/config/latest/developerguide/gettingstarted-concepts.html#gettingstarted-concepts-function"> Lambda Developer Guide</a>) and with Guard (<a href="https://github.com/aws-cloudformation/cloudformation-guard">Guard GitHub
  Repository</a>), a policy-as-code language. Config custom rules created with Lambda are called <i>Config Custom Lambda Rules</i> and Config custom rules created with Guard are called <i>Config Custom Policy Rules</i>.</p> <p>For more information about developing and using Config rules, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html">Evaluating Resource with Config Rules</a> in the <i>Config Developer Guide</i>.</p> <note> <p>You can use the Amazon Web Services CLI and Amazon Web Services SDKs if you want to create a rule that triggers evaluations for your resources when Config delivers the configuration snapshot. For more information, see <a>ConfigSnapshotDeliveryProperties</a>.</p> </note>'
layout: schema
name: ConfigRule
properties_list:
- description: ''
  name: ConfigRuleName
  type: object
- description: ''
  name: ConfigRuleArn
  type: object
- description: ''
  name: ConfigRuleId
  type: object
- description: ''
  name: Description
  type: object
- description: ''
  name: Scope
  type: object
- description: ''
  name: Source
  type: object
- description: ''
  name: InputParameters
  type: object
- description: ''
  name: MaximumExecutionFrequency
  type: object
- description: ''
  name: ConfigRuleState
  type: object
- description: ''
  name: CreatedBy
  type: object
- description: ''
  name: EvaluationModes
  type: object
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/config-config-rule-schema.json
slug: config-config-rule
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: ConfigRule
---
