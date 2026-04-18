---
description: An Advisor rule that defines detection logic for a specific system issue, along with resolution steps and remediation guidance.
layout: schema
name: Rule
properties_list:
- description: The unique identifier of the rule.
  name: rule_id
  type: string
- description: A description of what the rule detects.
  name: description
  type: string
- description: Whether the rule is currently active.
  name: active
  type: boolean
- description: The category the rule belongs to.
  name: category
  type: object
- description: The impact level of the rule.
  name: impact
  type: object
- description: The likelihood value (1-4).
  name: likelihood
  type: integer
- description: The calculated total risk score.
  name: total_risk
  type: integer
- description: The risk associated with applying the remediation.
  name: risk_of_change
  type: integer
- description: Whether an Ansible remediation playbook is available.
  name: has_playbook
  type: boolean
- description: When the rule was published.
  name: publish_date
  type: string
- description: The number of systems currently affected by this rule.
  name: systems_affected
  type: integer
- description: Available resolution options for the rule.
  name: resolution_set
  type: array
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-insights-rule-schema.json
slug: red-hat-insights-rule
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: Rule
---
