---
description: Indicates whether an Amazon Web Services resource that is evaluated according to one or more Config rules is compliant. A resource is compliant if it complies with all of the rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.
layout: schema
name: ComplianceByResource
properties_list:
- description: ''
  name: ResourceType
  type: object
- description: ''
  name: ResourceId
  type: object
- description: ''
  name: Compliance
  type: object
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/config-compliance-by-resource-schema.json
slug: config-compliance-by-resource
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: ComplianceByResource
---
