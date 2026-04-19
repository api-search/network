---
description: An instance mapping that associates an SAP HANA Cloud service instance with a target in another subaccount or environment.
layout: schema
name: InstanceMapping
properties_list:
- description: The unique identifier of the instance mapping.
  name: mappingId
  type: string
- description: The source service instance identifier.
  name: serviceInstanceId
  type: string
- description: The target subaccount identifier.
  name: targetSubaccountId
  type: string
- description: The target environment instance identifier.
  name: targetEnvironmentInstanceId
  type: string
- description: ISO 8601 timestamp when the mapping was created.
  name: createdAt
  type: string
provider_name: SAP HANA
provider_slug: sap-hana
schema_file: json-schema/sap-hana-cloud-rest-instance-mapping-schema.json
slug: sap-hana-cloud-rest-instance-mapping
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
title: InstanceMapping
---
