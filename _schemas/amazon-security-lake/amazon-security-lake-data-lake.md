---
description: Represents an Amazon Security Lake data lake configuration.
layout: schema
name: DataLake
properties_list:
- description: The ARN of the data lake.
  name: dataLakeArn
  type: string
- description: The AWS region where the data lake is configured.
  name: region
  type: string
- description: The current status of the data lake.
  name: status
  type: string
- description: The encryption configuration for the data lake.
  name: encryptionConfiguration
  type: object
- description: The lifecycle configuration for the data lake.
  name: lifecycleConfiguration
  type: object
- description: The ARN of the S3 bucket where security data is stored.
  name: s3BucketArn
  type: string
provider_name: Amazon Security Lake
provider_slug: amazon-security-lake
schema_file: json-schema/amazon-security-lake-data-lake-schema.json
slug: amazon-security-lake-data-lake
tags:
- AWS
- Data Lake
- Security
- SIEM
- Threat Detection
title: DataLake
---
