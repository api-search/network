---
description: DataStore schema from Palo Alto Networks Prisma Cloud DSPM API
layout: schema
name: DataStore
properties_list:
- description: Unique data store identifier in Prisma Cloud.
  name: id
  type: string
- description: Name of the data store as it appears in the cloud provider.
  name: name
  type: string
- description: Cloud provider where the data store is hosted.
  name: cloudProvider
  type: string
- description: Cloud account ID that owns the data store.
  name: cloudAccountId
  type: string
- description: Cloud region where the data store is located.
  name: region
  type: string
- description: Category of the data store service.
  name: serviceType
  type: string
- description: Specific cloud service name (e.g., Amazon S3, Amazon RDS).
  name: serviceName
  type: string
- description: Whether encryption at rest is enabled.
  name: encryptionEnabled
  type: boolean
- description: Whether the data store is accessible from the public internet.
  name: isPubliclyAccessible
  type: boolean
- description: Overall risk level computed from data sensitivity and security posture.
  name: riskLevel
  type: string
- description: Number of sensitive data assets found in this data store.
  name: sensitiveDataCount
  type: integer
- description: Distinct classification labels found in the data store.
  name: classificationLabels
  type: array
- description: Total number of data assets discovered in this data store.
  name: dataAssetCount
  type: integer
- description: Timestamp when the data store was first discovered by DSPM.
  name: discoveredAt
  type: string
- description: Timestamp of the most recent data classification scan.
  name: lastScannedAt
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-dspm-api-data-store-schema.json
slug: prisma-cloud-dspm-api-data-store
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: DataStore
---
