---
description: Provides the source and the message types that trigger Config to evaluate your Amazon Web Services resources against a rule. It also provides the frequency with which you want Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for <code>SourceDetail</code> only for custom rules.
layout: schema
name: SourceDetail
properties_list:
- description: ''
  name: EventSource
  type: object
- description: ''
  name: MessageType
  type: object
- description: ''
  name: MaximumExecutionFrequency
  type: object
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/config-source-detail-schema.json
slug: config-source-detail
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: SourceDetail
---
