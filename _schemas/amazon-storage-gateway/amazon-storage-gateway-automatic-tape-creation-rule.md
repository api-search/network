---
description: An automatic tape creation policy consists of automatic tape creation rules where each rule defines when and how to create new tapes. For more information about automatic tape creation, see <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/GettingStartedCreateTapes.html#CreateTapesAutomatically">Creating Tapes Automatically</a>.
layout: schema
name: AutomaticTapeCreationRule
properties_list:
- description: ''
  name: TapeBarcodePrefix
  type: object
- description: ''
  name: PoolId
  type: object
- description: ''
  name: TapeSizeInBytes
  type: object
- description: ''
  name: MinimumNumTapes
  type: object
- description: ''
  name: Worm
  type: object
provider_name: Amazon Storage Gateway
provider_slug: amazon-storage-gateway
schema_file: json-schema/amazon-storage-gateway-automatic-tape-creation-rule-schema.json
slug: amazon-storage-gateway-automatic-tape-creation-rule
tags:
- AWS
- Backup
- File Storage
- Gateway
- Hybrid Cloud
- Storage
title: AutomaticTapeCreationRule
---
