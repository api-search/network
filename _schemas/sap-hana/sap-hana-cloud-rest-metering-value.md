---
description: A metering data record representing resource consumption for billing purposes.
layout: schema
name: MeteringValue
properties_list:
- description: ISO 8601 timestamp for the metering period.
  name: timestamp
  type: string
- description: The number of compute unit hours consumed during the metering period. Compute units are based on memory and vCPU allocation.
  name: computeUnitHours
  type: number
- description: The storage consumption in gigabytes during the metering period.
  name: storageGB
  type: number
- description: The data lake storage consumption in gigabytes during the metering period, if a data lake instance is attached.
  name: dataLakeCapacityGB
  type: number
- description: The backup storage consumption in gigabytes during the metering period.
  name: backupStorageGB
  type: number
provider_name: SAP HANA
provider_slug: sap-hana
schema_file: json-schema/sap-hana-cloud-rest-metering-value-schema.json
slug: sap-hana-cloud-rest-metering-value
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
title: MeteringValue
---
