---
description: ''
layout: schema
name: Encryption
properties_list:
- description: Specifies the encryption type used.
  name: type
  type: string
- description: Specifies the ID for the Cloud KMS-managed key used to encrypt files written to the bucket.
  name: kms_key_id
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/external-volume-encryption-schema.json
slug: external-volume-encryption
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Encryption
---
