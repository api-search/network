---
description: A paginated list of SAP HANA Cloud service instances in the subaccount.
layout: schema
name: ServiceInstanceList
properties_list:
- description: Total number of service instances matching the query criteria.
  name: num_items
  type: integer
- description: The list of service instances for the current page.
  name: items
  type: array
- description: Pagination token to retrieve the next page of results.
  name: token
  type: string
provider_name: SAP HANA
provider_slug: sap-hana
schema_file: json-schema/sap-hana-cloud-rest-service-instance-list-schema.json
slug: sap-hana-cloud-rest-service-instance-list
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
title: ServiceInstanceList
---
