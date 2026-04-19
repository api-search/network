---
description: Request body for updating an existing SAP HANA Cloud service instance. Only include the parameters that need to be changed.
layout: schema
name: UpdateServiceInstanceRequest
properties_list:
- description: The updated name for the service instance.
  name: name
  type: string
- description: Updated labels for the service instance.
  name: labels
  type: object
- description: The new service plan identifier if changing the instance plan.
  name: service_plan_id
  type: string
provider_name: SAP HANA
provider_slug: sap-hana
schema_file: json-schema/sap-hana-cloud-rest-update-service-instance-request-schema.json
slug: sap-hana-cloud-rest-update-service-instance-request
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
title: UpdateServiceInstanceRequest
---
