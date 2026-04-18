---
description: Classification schema from Palo Alto Networks Prisma Cloud DSPM API
layout: schema
name: Classification
properties_list:
- description: Unique classification identifier.
  name: id
  type: string
- description: Classification label name.
  name: name
  type: string
- description: Detailed description of what the classification detects.
  name: description
  type: string
- description: Broad category of the classification.
  name: category
  type: string
- description: Default sensitivity level for data matching this classification.
  name: sensitivityLevel
  type: string
- description: Whether this is a built-in or custom classification.
  name: isBuiltIn
  type: boolean
- description: Regulatory frameworks referencing this data classification.
  name: regulatoryFrameworks
  type: array
- description: Number of data stores where matching data has been found.
  name: dataStoreCount
  type: integer
- description: Number of data assets matching this classification.
  name: dataAssetCount
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-dspm-api-classification-schema.json
slug: prisma-cloud-dspm-api-classification
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Classification
---
