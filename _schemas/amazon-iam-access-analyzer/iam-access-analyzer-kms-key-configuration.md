---
description: <p>Proposed access control configuration for a KMS key. You can propose a configuration for a new KMS key or an existing KMS key that you own by specifying the key policy and KMS grant configuration. If the configuration is for an existing key and you do not specify the key policy, the access preview uses the existing policy for the key. If the access preview is for a new resource and you do not specify the key policy, then the access preview uses the default key policy. The proposed key policy cannot be an empty string. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default">Default key policy</a>. For more information about key policy limits, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/resource-limits.html">Resource quotas</a>.</p> <p/>
layout: schema
name: KmsKeyConfiguration
properties_list:
- description: ''
  name: keyPolicies
  type: object
- description: ''
  name: grants
  type: object
provider_name: Amazon IAM Access Analyzer
provider_slug: amazon-iam-access-analyzer
schema_file: json-schema/iam-access-analyzer-kms-key-configuration-schema.json
slug: iam-access-analyzer-kms-key-configuration
tags:
- Access Control
- AWS
- Compliance
- IAM
- Policy Management
- Security
title: KmsKeyConfiguration
---
