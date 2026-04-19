---
description: <p>Status information for your Config Managed rules and Config Custom Policy rules. The status includes information such as the last time the rule ran, the last time it failed, and the related error for the last failure.</p> <p>This action does not return status information about Config Custom Lambda rules.</p>
layout: schema
name: ConfigRuleEvaluationStatus
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
  name: LastSuccessfulInvocationTime
  type: object
- description: ''
  name: LastFailedInvocationTime
  type: object
- description: ''
  name: LastSuccessfulEvaluationTime
  type: object
- description: ''
  name: LastFailedEvaluationTime
  type: object
- description: ''
  name: FirstActivatedTime
  type: object
- description: ''
  name: LastDeactivatedTime
  type: object
- description: ''
  name: LastErrorCode
  type: object
- description: ''
  name: LastErrorMessage
  type: object
- description: ''
  name: FirstEvaluationStarted
  type: object
- description: ''
  name: LastDebugLogDeliveryStatus
  type: object
- description: ''
  name: LastDebugLogDeliveryStatusReason
  type: object
- description: ''
  name: LastDebugLogDeliveryTime
  type: object
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/config-config-rule-evaluation-status-schema.json
slug: config-config-rule-evaluation-status
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: ConfigRuleEvaluationStatus
---
