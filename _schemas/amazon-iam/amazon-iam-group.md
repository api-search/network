---
description: Group schema from AWS IAM API
layout: schema
name: Group
properties_list:
- description: The path to the group.
  name: Path
  type: string
- description: The friendly name that identifies the group.
  name: GroupName
  type: string
- description: The stable and unique string identifying the group.
  name: GroupId
  type: string
- description: The Amazon Resource Name (ARN) specifying the group.
  name: Arn
  type: string
- description: The date and time when the group was created.
  name: CreateDate
  type: string
provider_name: Amazon IAM
provider_slug: amazon-iam
schema_file: json-schema/amazon-iam-group-schema.json
slug: amazon-iam-group
tags:
- Access Management
- Authentication
- Authorization
- AWS
- Identity
- Security
title: Group
---
