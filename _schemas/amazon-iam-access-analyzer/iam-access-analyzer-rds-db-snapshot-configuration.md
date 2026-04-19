---
description: The proposed access control configuration for an Amazon RDS DB snapshot. You can propose a configuration for a new Amazon RDS DB snapshot or an Amazon RDS DB snapshot that you own by specifying the <code>RdsDbSnapshotAttributeValue</code> and optional KMS encryption key. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBSnapshotAttribute.html">ModifyDBSnapshotAttribute</a>.
layout: schema
name: RdsDbSnapshotConfiguration
properties_list:
- description: ''
  name: attributes
  type: object
- description: ''
  name: kmsKeyId
  type: object
provider_name: Amazon IAM Access Analyzer
provider_slug: amazon-iam-access-analyzer
schema_file: json-schema/iam-access-analyzer-rds-db-snapshot-configuration-schema.json
slug: iam-access-analyzer-rds-db-snapshot-configuration
tags:
- Access Control
- AWS
- Compliance
- IAM
- Policy Management
- Security
title: RdsDbSnapshotConfiguration
---
