---
description: A Fraud Detector rule that maps model scores and event variables to outcomes.
layout: schema
name: Rule
properties_list:
- description: Unique rule identifier.
  name: ruleId
  type: string
- description: Detector this rule belongs to.
  name: detectorId
  type: string
- description: Version of the rule.
  name: ruleVersion
  type: string
- description: ''
  name: description
  type: string
- description: Rule expression language.
  name: language
  type: string
- description: Rule expression evaluated against event variables and model scores.
  name: expression
  type: string
- description: Outcomes triggered when the rule matches.
  name: outcomes
  type: array
- description: ''
  name: arn
  type: string
provider_name: Amazon Fraud Detector
provider_slug: amazon-fraud-detector
schema_file: json-schema/amazon-fraud-detector-rule-schema.json
slug: amazon-fraud-detector-rule
tags:
- AWS
- Financial Services
- Fraud Detection
- Machine Learning
- Security
title: Rule
---
