---
description: Role schema from AWS IAM API
layout: schema
name: Role
properties_list:
- description: The path to the role.
  name: Path
  type: string
- description: The friendly name that identifies the role.
  name: RoleName
  type: string
- description: The stable and unique string identifying the role.
  name: RoleId
  type: string
- description: The Amazon Resource Name (ARN) specifying the role.
  name: Arn
  type: string
- description: The date and time when the role was created.
  name: CreateDate
  type: string
- description: The policy that grants an entity permission to assume the role.
  name: AssumeRolePolicyDocument
  type: string
- description: A description of the role.
  name: Description
  type: string
- description: The maximum session duration (in seconds) for the specified role.
  name: MaxSessionDuration
  type: integer
- description: ''
  name: Tags
  type: array
provider_name: Amazon IAM
provider_slug: amazon-iam
schema_file: json-schema/amazon-iam-role-schema.json
slug: amazon-iam-role
tags:
- Access Management
- Authentication
- Authorization
- AWS
- Identity
- Security
title: Role
---
