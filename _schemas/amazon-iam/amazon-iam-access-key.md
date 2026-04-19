---
description: AccessKey schema from AWS IAM API
layout: schema
name: AccessKey
properties_list:
- description: The name of the IAM user the access key is associated with.
  name: UserName
  type: string
- description: The ID for this access key.
  name: AccessKeyId
  type: string
- description: The status of the access key.
  name: Status
  type: string
- description: The secret key used to sign requests. Only returned on creation.
  name: SecretAccessKey
  type: string
- description: The date when the access key was created.
  name: CreateDate
  type: string
provider_name: Amazon IAM
provider_slug: amazon-iam
schema_file: json-schema/amazon-iam-access-key-schema.json
slug: amazon-iam-access-key
tags:
- Access Management
- Authentication
- Authorization
- AWS
- Identity
- Security
title: AccessKey
---
