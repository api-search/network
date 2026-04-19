---
description: Information about a landing zone operation.
layout: schema
name: LandingZoneOperationDetail
properties_list:
- description: The time the operation completed.
  name: endTime
  type: string
- description: The unique identifier of the operation.
  name: operationIdentifier
  type: string
- description: The type of landing zone operation.
  name: operationType
  type: string
- description: The time the operation was initiated.
  name: startTime
  type: string
- description: The status of the operation.
  name: status
  type: string
- description: If the operation result is FAILED, this string contains a message explaining why.
  name: statusMessage
  type: string
provider_name: Amazon Control Tower
provider_slug: amazon-control-tower
schema_file: json-schema/landing-zone-operation-detail-schema.json
slug: landing-zone-operation-detail
tags:
- AWS
- Compliance
- Governance
- Landing Zone
- Multi-Account
- Security
- Controls
title: LandingZoneOperationDetail
---
