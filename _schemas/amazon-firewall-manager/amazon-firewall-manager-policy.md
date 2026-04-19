---
description: An AWS Firewall Manager policy defining security rules and resource scope.
layout: schema
name: Policy
properties_list:
- description: Unique policy identifier.
  name: PolicyId
  type: string
- description: Friendly name of the policy.
  name: PolicyName
  type: string
- description: Token for optimistic locking.
  name: PolicyUpdateToken
  type: string
- description: Details about the security service type and configuration.
  name: SecurityServicePolicyData
  type: object
- description: AWS resource type in scope.
  name: ResourceType
  type: string
- description: If True, resources with specified tags are excluded.
  name: ExcludeResourceTags
  type: boolean
- description: If True, Firewall Manager auto-remediates non-compliant resources.
  name: RemediationEnabled
  type: boolean
- description: ARN of the policy.
  name: PolicyArn
  type: string
provider_name: Amazon Firewall Manager
provider_slug: amazon-firewall-manager
schema_file: json-schema/amazon-firewall-manager-policy-schema.json
slug: amazon-firewall-manager-policy
tags:
- AWS
- Compliance
- Firewall
- Network Security
- Security
title: Policy
---
