---
description: Use this structure to propose allowing <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations">cryptographic operations</a> in the grant only when the operation request includes the specified <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context">encryption context</a>. You can specify only one type of encryption context. An empty map is treated as not specified. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantConstraints.html">GrantConstraints</a>.
layout: schema
name: KmsGrantConstraints
properties_list:
- description: ''
  name: encryptionContextEquals
  type: object
- description: ''
  name: encryptionContextSubset
  type: object
provider_name: Amazon IAM Access Analyzer
provider_slug: amazon-iam-access-analyzer
schema_file: json-schema/iam-access-analyzer-kms-grant-constraints-schema.json
slug: iam-access-analyzer-kms-grant-constraints
tags:
- Access Control
- AWS
- Compliance
- IAM
- Policy Management
- Security
title: KmsGrantConstraints
---
