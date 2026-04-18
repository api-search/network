---
description: Container for grant information.
layout: schema
name: Grant
properties_list:
- description: The person being granted permissions.
  name: Grantee
  type: object
- description: Specifies the permission given to the grantee.
  name: Permission
  type: string
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-rest-grant-schema.json
slug: amazon-s3-rest-grant
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: Grant
---
