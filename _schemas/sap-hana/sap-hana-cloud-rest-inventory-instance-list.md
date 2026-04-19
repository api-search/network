---
description: A paginated list of SAP HANA Cloud instances from the inventory service.
layout: schema
name: InventoryInstanceList
properties_list:
- description: Total number of instances matching the query criteria.
  name: totalCount
  type: integer
- description: The list of inventory instances for the current page.
  name: items
  type: array
provider_name: SAP HANA
provider_slug: sap-hana
schema_file: json-schema/sap-hana-cloud-rest-inventory-instance-list-schema.json
slug: sap-hana-cloud-rest-inventory-instance-list
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
title: InventoryInstanceList
---
