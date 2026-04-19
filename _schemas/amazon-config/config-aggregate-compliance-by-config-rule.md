---
description: <p>Indicates whether an Config rule is compliant based on account ID, region, compliance, and rule name.</p> <p>A rule is compliant if all of the resources that the rule evaluated comply with it. It is noncompliant if any of these resources do not comply.</p>
layout: schema
name: AggregateComplianceByConfigRule
properties_list:
- description: ''
  name: ConfigRuleName
  type: object
- description: ''
  name: Compliance
  type: object
- description: ''
  name: AccountId
  type: object
- description: ''
  name: AwsRegion
  type: object
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/config-aggregate-compliance-by-config-rule-schema.json
slug: config-aggregate-compliance-by-config-rule
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: AggregateComplianceByConfigRule
---
