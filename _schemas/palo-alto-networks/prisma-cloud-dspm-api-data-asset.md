---
description: DataAsset schema from Palo Alto Networks Prisma Cloud DSPM API
layout: schema
name: DataAsset
properties_list:
- description: Unique data asset identifier.
  name: id
  type: string
- description: Parent data store identifier.
  name: dataStoreId
  type: string
- description: Name of the parent data store.
  name: dataStoreName
  type: string
- description: Name of the data asset (e.g., table name, column name, object prefix, directory name).
  name: name
  type: string
- description: Type of data asset.
  name: assetType
  type: string
- description: Full path to the data asset within the data store.
  name: path
  type: string
- description: Classification labels applied to this data asset.
  name: classificationLabels
  type: array
- description: Sensitivity level based on the most sensitive classification.
  name: sensitivityLevel
  type: string
- description: Sample data patterns found during classification.
  name: sampleFindings
  type: array
- description: Approximate number of records in this data asset.
  name: recordCount
  type: integer
- description: Timestamp when the data asset was first discovered.
  name: discoveredAt
  type: string
- description: Timestamp of the most recent classification scan.
  name: lastScannedAt
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-dspm-api-data-asset-schema.json
slug: prisma-cloud-dspm-api-data-asset
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: DataAsset
---
