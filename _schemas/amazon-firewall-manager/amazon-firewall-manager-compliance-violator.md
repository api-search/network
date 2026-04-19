---
description: A resource not in compliance with a Firewall Manager policy.
layout: schema
name: ComplianceViolator
properties_list:
- description: ID of the non-compliant resource.
  name: ResourceId
  type: string
- description: Reason the resource is not compliant.
  name: ViolationReason
  type: string
- description: AWS resource type.
  name: ResourceType
  type: string
provider_name: Amazon Firewall Manager
provider_slug: amazon-firewall-manager
schema_file: json-schema/amazon-firewall-manager-compliance-violator-schema.json
slug: amazon-firewall-manager-compliance-violator
tags:
- AWS
- Compliance
- Firewall
- Network Security
- Security
title: ComplianceViolator
---
