---
description: Provides the CustomPolicyDetails, the rule owner (<code>Amazon Web Services</code> for managed rules, <code>CUSTOM_POLICY</code> for Custom Policy rules, and <code>CUSTOM_LAMBDA</code> for Custom Lambda rules), the rule identifier, and the events that cause the evaluation of your Amazon Web Services resources.
layout: schema
name: Source
properties_list:
- description: ''
  name: Owner
  type: object
- description: ''
  name: SourceIdentifier
  type: object
- description: ''
  name: SourceDetails
  type: object
- description: ''
  name: CustomPolicyDetails
  type: object
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/config-source-schema.json
slug: config-source
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: Source
---
