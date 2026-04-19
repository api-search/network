---
description: A resource registered with AWS Lake Formation.
layout: schema
name: DataLakeResource
properties_list:
- description: The ARN of the resource registered with Lake Formation.
  name: ResourceArn
  type: string
- description: The IAM role that registered the resource.
  name: RoleArn
  type: string
- description: The date and time the resource was last modified.
  name: LastModified
  type: string
provider_name: Amazon Lake Formation
provider_slug: amazon-lake-formation
schema_file: json-schema/amazon-lake-formation-resource-schema.json
slug: amazon-lake-formation-resource
tags:
- Access Control
- Analytics
- AWS
- Data Governance
- Data Lake
- S3
title: DataLakeResource
---
