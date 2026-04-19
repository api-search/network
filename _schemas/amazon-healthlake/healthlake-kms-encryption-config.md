---
description: The customer-managed-key(CMK) used when creating a data store. If a customer owned key is not specified, an AWS owned key will be used for encryption.
layout: schema
name: KmsEncryptionConfig
properties_list:
- description: ''
  name: CmkType
  type: object
- description: ''
  name: KmsKeyId
  type: object
provider_name: Amazon HealthLake
provider_slug: amazon-healthlake
schema_file: json-schema/healthlake-kms-encryption-config-schema.json
slug: healthlake-kms-encryption-config
tags:
- AWS
- FHIR
- Health Data
- Healthcare
- HIPAA
- Cloud Computing
title: KmsEncryptionConfig
---
