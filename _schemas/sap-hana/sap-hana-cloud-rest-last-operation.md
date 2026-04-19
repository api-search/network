---
description: Details about the last operation performed on the service instance.
layout: schema
name: LastOperation
properties_list:
- description: The type of operation that was performed.
  name: type
  type: string
- description: The current state of the operation.
  name: state
  type: string
- description: A human-readable description of the operation status.
  name: description
  type: string
- description: ISO 8601 timestamp when the operation was initiated.
  name: created_at
  type: string
- description: ISO 8601 timestamp when the operation status was last updated.
  name: updated_at
  type: string
provider_name: SAP HANA
provider_slug: sap-hana
schema_file: json-schema/sap-hana-cloud-rest-last-operation-schema.json
slug: sap-hana-cloud-rest-last-operation
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
title: LastOperation
---
