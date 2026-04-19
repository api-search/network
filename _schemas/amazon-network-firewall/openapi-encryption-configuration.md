---
description: A complex type that contains optional Amazon Web Services Key Management Service (KMS) encryption settings for your Network Firewall resources. Your data is encrypted by default with an Amazon Web Services owned key that Amazon Web Services owns and manages for you. You can use either the Amazon Web Services owned key, or provide your own customer managed key. To learn more about KMS encryption of your Network Firewall resources, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/kms-encryption-at-rest.html">Encryption at rest with Amazon Web Services Key Managment Service</a> in the <i>Network Firewall Developer Guide</i>.
layout: schema
name: EncryptionConfiguration
properties_list:
- description: ''
  name: KeyId
  type: object
- description: ''
  name: Type
  type: object
provider_name: Amazon Network Firewall
provider_slug: amazon-network-firewall
schema_file: json-schema/openapi-encryption-configuration-schema.json
slug: openapi-encryption-configuration
tags:
- AWS
- Firewall
- Intrusion Detection
- Network Security
- VPC
title: EncryptionConfiguration
---
