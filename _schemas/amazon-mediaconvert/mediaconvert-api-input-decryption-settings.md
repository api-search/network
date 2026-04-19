---
description: Settings for decrypting any input files that you encrypt before you upload them to Amazon S3. MediaConvert can decrypt files only when you use AWS Key Management Service (KMS) to encrypt the data key that you use to encrypt your content.
layout: schema
name: InputDecryptionSettings
properties_list:
- description: ''
  name: DecryptionMode
  type: object
- description: ''
  name: EncryptedDecryptionKey
  type: object
- description: ''
  name: InitializationVector
  type: object
- description: ''
  name: KmsKeyRegion
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-input-decryption-settings-schema.json
slug: mediaconvert-api-input-decryption-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: InputDecryptionSettings
---
