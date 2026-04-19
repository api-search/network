---
description: The proposed access control configuration for an Amazon RDS DB cluster snapshot. You can propose a configuration for a new Amazon RDS DB cluster snapshot or an Amazon RDS DB cluster snapshot that you own by specifying the <code>RdsDbClusterSnapshotAttributeValue</code> and optional KMS encryption key. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBClusterSnapshotAttribute.html">ModifyDBClusterSnapshotAttribute</a>.
layout: schema
name: RdsDbClusterSnapshotConfiguration
properties_list:
- description: ''
  name: attributes
  type: object
- description: ''
  name: kmsKeyId
  type: object
provider_name: Amazon IAM Access Analyzer
provider_slug: amazon-iam-access-analyzer
schema_file: json-schema/iam-access-analyzer-rds-db-cluster-snapshot-configuration-schema.json
slug: iam-access-analyzer-rds-db-cluster-snapshot-configuration
tags:
- Access Control
- AWS
- Compliance
- IAM
- Policy Management
- Security
title: RdsDbClusterSnapshotConfiguration
---
