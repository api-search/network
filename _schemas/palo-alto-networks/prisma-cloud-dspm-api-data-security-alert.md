---
description: DataSecurityAlert schema from Palo Alto Networks Prisma Cloud DSPM API
layout: schema
name: DataSecurityAlert
properties_list:
- description: Unique alert identifier.
  name: id
  type: string
- description: Short description of the alert condition.
  name: title
  type: string
- description: Detailed alert description.
  name: description
  type: string
- description: Alert severity level.
  name: severity
  type: string
- description: Current alert status.
  name: status
  type: string
- description: Category of data security alert.
  name: alertType
  type: string
- description: Affected data store identifier.
  name: dataStoreId
  type: string
- description: Name of the affected data store.
  name: dataStoreName
  type: string
- description: Cloud provider of the affected data store.
  name: cloudProvider
  type: string
- description: Cloud account identifier.
  name: cloudAccountId
  type: string
- description: Cloud region of the affected data store.
  name: region
  type: string
- description: Data classification labels involved in the alert.
  name: affectedClassifications
  type: array
- description: Timestamp when the alert was generated.
  name: detectedAt
  type: string
- description: Timestamp when the alert was resolved. Null if still open.
  name: resolvedAt
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-dspm-api-data-security-alert-schema.json
slug: prisma-cloud-dspm-api-data-security-alert
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: DataSecurityAlert
---
