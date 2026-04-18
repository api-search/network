---
description: An IAM user in Oracle Cloud Infrastructure.
layout: schema
name: User
properties_list:
- description: The OCID of the user.
  name: id
  type: string
- description: The OCID of the tenancy.
  name: compartmentId
  type: string
- description: The name of the user.
  name: name
  type: string
- description: The description of the user.
  name: description
  type: string
- description: The email address.
  name: email
  type: string
- description: ''
  name: lifecycleState
  type: string
- description: Whether MFA is activated.
  name: isMfaActivated
  type: boolean
- description: ''
  name: timeCreated
  type: string
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/iam-user-schema.json
slug: iam-user
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: User
---
