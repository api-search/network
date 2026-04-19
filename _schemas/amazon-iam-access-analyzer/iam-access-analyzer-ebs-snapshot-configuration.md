---
description: The proposed access control configuration for an Amazon EBS volume snapshot. You can propose a configuration for a new Amazon EBS volume snapshot or an Amazon EBS volume snapshot that you own by specifying the user IDs, groups, and optional KMS encryption key. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySnapshotAttribute.html">ModifySnapshotAttribute</a>.
layout: schema
name: EbsSnapshotConfiguration
properties_list:
- description: ''
  name: userIds
  type: object
- description: ''
  name: groups
  type: object
- description: ''
  name: kmsKeyId
  type: object
provider_name: Amazon IAM Access Analyzer
provider_slug: amazon-iam-access-analyzer
schema_file: json-schema/iam-access-analyzer-ebs-snapshot-configuration-schema.json
slug: iam-access-analyzer-ebs-snapshot-configuration
tags:
- Access Control
- AWS
- Compliance
- IAM
- Policy Management
- Security
title: EbsSnapshotConfiguration
---
