---
description: An SAP HANA Cloud instance as represented in the inventory service, providing a consolidated view of instance status and configuration.
layout: schema
name: InventoryInstance
properties_list:
- description: The unique identifier of the service instance.
  name: serviceInstanceId
  type: string
- description: The name of the service plan (e.g., hana, hana-td, relational-data-lake).
  name: servicePlanName
  type: string
- description: The display name of the instance.
  name: instanceName
  type: string
- description: The current provisioning state of the instance.
  name: provisioningState
  type: string
- description: The current operational state of the instance.
  name: operationalState
  type: string
- description: Allocated memory in gigabytes.
  name: memory
  type: integer
- description: Number of allocated virtual CPUs.
  name: vcpu
  type: integer
- description: Allocated persistent storage in gigabytes.
  name: storage
  type: integer
- description: ISO 8601 timestamp when the instance was created.
  name: createdAt
  type: string
- description: ISO 8601 timestamp when the instance was last modified.
  name: modifiedAt
  type: string
provider_name: SAP HANA
provider_slug: sap-hana
schema_file: json-schema/sap-hana-cloud-rest-inventory-instance-schema.json
slug: sap-hana-cloud-rest-inventory-instance
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
title: InventoryInstance
---
