---
description: PutStorageConfigurationResponse schema
layout: schema
name: PutStorageConfigurationResponse
properties_list:
- description: ''
  name: storageType
  type: object
- description: ''
  name: multiLayerStorage
  type: object
- description: ''
  name: disassociatedDataStorage
  type: object
- description: How many days your data is kept in the hot tier. By default, your data is kept indefinitely in the hot tier.
  name: retentionPeriod
  type: object
- description: Contains current status information for the configuration.
  name: configurationStatus
  type: object
provider_name: Amazon IoT SiteWise
provider_slug: amazon-iot-sitewise
schema_file: json-schema/iot-sitewise-put-storage-configuration-response-schema.json
slug: iot-sitewise-put-storage-configuration-response
tags:
- AWS
- Asset Management
- Industrial IoT
- IoT
- Time Series Data
title: PutStorageConfigurationResponse
---
