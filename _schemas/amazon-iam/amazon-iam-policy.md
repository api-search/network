---
description: Policy schema from AWS IAM API
layout: schema
name: Policy
properties_list:
- description: The friendly name identifying the policy.
  name: PolicyName
  type: string
- description: The stable and unique string identifying the policy.
  name: PolicyId
  type: string
- description: The Amazon Resource Name (ARN) of the policy.
  name: Arn
  type: string
- description: The path to the policy.
  name: Path
  type: string
- description: The identifier for the version of the policy that is the default.
  name: DefaultVersionId
  type: string
- description: The number of entities the policy is attached to.
  name: AttachmentCount
  type: integer
- description: Specifies whether the policy can be attached.
  name: IsAttachable
  type: boolean
- description: A description of the policy.
  name: Description
  type: string
- description: The date and time when the policy was created.
  name: CreateDate
  type: string
- description: The date and time when the policy was last updated.
  name: UpdateDate
  type: string
provider_name: Amazon IAM
provider_slug: amazon-iam
schema_file: json-schema/amazon-iam-policy-schema.json
slug: amazon-iam-policy
tags:
- Access Management
- Authentication
- Authorization
- AWS
- Identity
- Security
title: Policy
---
