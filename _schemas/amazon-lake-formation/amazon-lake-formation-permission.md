---
description: A Lake Formation permission grant.
layout: schema
name: Permission
properties_list:
- description: The principal (IAM user, role, or group) being granted permissions.
  name: Principal
  type: object
- description: The resource on which permissions are being granted.
  name: Resource
  type: object
- description: The permissions being granted.
  name: Permissions
  type: array
provider_name: Amazon Lake Formation
provider_slug: amazon-lake-formation
schema_file: json-schema/amazon-lake-formation-permission-schema.json
slug: amazon-lake-formation-permission
tags:
- Access Control
- Analytics
- AWS
- Data Governance
- Data Lake
- S3
title: Permission
---
