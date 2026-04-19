---
description: The encryption settings, if any, that are used for decrypting your input files or encrypting your output files. If your input file is encrypted, you must specify the mode that Elastic Transcoder uses to decrypt your file, otherwise you must specify the mode you want Elastic Transcoder to use to encrypt your output files.
layout: schema
name: Encryption
properties_list:
- description: ''
  name: Mode
  type: object
- description: ''
  name: Key
  type: object
- description: ''
  name: KeyMd5
  type: object
- description: ''
  name: InitializationVector
  type: object
provider_name: Amazon Elastic Transcoder
provider_slug: amazon-elastic-transcoder
schema_file: json-schema/amazon-elastic-transcoder-encryption-schema.json
slug: amazon-elastic-transcoder-encryption
tags:
- Amazon Web Services
- AWS
- Media
- Transcoding
- Video
title: Encryption
---
