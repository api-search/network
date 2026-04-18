---
description: AccessPolicyRequest schema from Palo Alto Networks SASE IAM Service API
layout: schema
name: AccessPolicyRequest
properties_list:
- description: ID of the service account or user to grant access to.
  name: principal_id
  type: string
- description: Type of principal.
  name: principal_type
  type: string
- description: ID of the role to assign.
  name: role_id
  type: string
- description: TSG scope for this policy.
  name: tsg_id
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-iam-api-access-policy-request-schema.json
slug: sase-iam-api-access-policy-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AccessPolicyRequest
---
