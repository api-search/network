---
description: DataRisk schema from Palo Alto Networks Prisma Cloud DSPM API
layout: schema
name: DataRisk
properties_list:
- description: Unique risk identifier.
  name: id
  type: string
- description: Short description of the risk.
  name: title
  type: string
- description: Detailed explanation of the risk and its potential impact.
  name: description
  type: string
- description: Severity of the risk.
  name: riskLevel
  type: string
- description: Category of the data security risk.
  name: riskCategory
  type: string
- description: Current status of the risk.
  name: status
  type: string
- description: Data store where the risk was identified.
  name: dataStoreId
  type: string
- description: Name of the affected data store.
  name: dataStoreName
  type: string
- description: Cloud provider of the affected data store.
  name: cloudProvider
  type: string
- description: Cloud account ID of the affected data store.
  name: cloudAccountId
  type: string
- description: Cloud region of the affected data store.
  name: region
  type: string
- description: Classification labels of sensitive data at risk.
  name: affectedClassifications
  type: array
- description: Number of data assets affected by this risk.
  name: affectedDataAssetCount
  type: integer
- description: Recommended remediation steps.
  name: remediation
  type: object
- description: Timestamp when the risk was first detected.
  name: detectedAt
  type: string
- description: Timestamp of the most recent risk evaluation.
  name: lastEvaluatedAt
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-dspm-api-data-risk-schema.json
slug: prisma-cloud-dspm-api-data-risk
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: DataRisk
---
