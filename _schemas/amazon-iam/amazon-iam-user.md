---
description: Schema representing an AWS Identity and Access Management (IAM) user resource.
layout: schema
name: AWS IAM User
properties_list:
- description: The path to the user. For more information about paths, see IAM identifiers in the IAM User Guide.
  name: Path
  type: string
- description: The friendly name identifying the user.
  name: UserName
  type: string
- description: The stable and unique string identifying the user. For more information about IDs, see IAM identifiers in the IAM User Guide.
  name: UserId
  type: string
- description: The Amazon Resource Name (ARN) that identifies the user.
  name: Arn
  type: string
- description: The date and time, in ISO 8601 date-time format, when the user was created.
  name: CreateDate
  type: string
- description: The date and time, in ISO 8601 date-time format, when the user's password was last used to sign in to an AWS website.
  name: PasswordLastUsed
  type:
  - string
  - 'null'
- description: The ARN of the policy used to set the permissions boundary for the user.
  name: PermissionsBoundary
  type: object
- description: A list of tags attached to the user.
  name: Tags
  type: array
provider_name: Amazon IAM
provider_slug: amazon-iam
schema_file: json-schema/amazon-iam-user-schema.json
slug: amazon-iam-user
tags:
- Access Management
- Authentication
- Authorization
- AWS
- Identity
- Security
title: AWS IAM User
---
