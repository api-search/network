---
description: AccessPolicy schema from Palo Alto Networks SASE IAM Service API
layout: schema
name: AccessPolicy
properties_list:
- description: Unique identifier of the access policy.
  name: id
  type: string
- description: ID of the service account or user this policy applies to.
  name: principal_id
  type: string
- description: Type of principal.
  name: principal_type
  type: string
- description: ID of the role assigned by this policy.
  name: role_id
  type: string
- description: Name of the role assigned.
  name: role_name
  type: string
- description: TSG scope this policy applies to.
  name: tsg_id
  type: string
- description: ''
  name: created_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-iam-api-access-policy-schema.json
slug: sase-iam-api-access-policy
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AccessPolicy
---
