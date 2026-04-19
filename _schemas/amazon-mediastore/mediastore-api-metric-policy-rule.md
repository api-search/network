---
description: A setting that enables metrics at the object level. Each rule contains an object group and an object group name. If the policy includes the MetricPolicyRules parameter, you must include at least one rule. Each metric policy can include up to five rules by default. You can also <a href="https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/mediastore/quotas">request a quota increase</a> to allow up to 300 rules per policy.
layout: schema
name: MetricPolicyRule
properties_list:
- description: ''
  name: ObjectGroup
  type: object
- description: ''
  name: ObjectGroupName
  type: object
provider_name: Amazon MediaStore
provider_slug: amazon-mediastore
schema_file: json-schema/mediastore-api-metric-policy-rule-schema.json
slug: mediastore-api-metric-policy-rule
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: MetricPolicyRule
---
