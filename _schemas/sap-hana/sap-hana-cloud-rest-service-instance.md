---
description: An SAP HANA Cloud service instance representing a provisioned database with its configuration, status, and connection details.
layout: schema
name: ServiceInstance
properties_list:
- description: The unique identifier assigned to the service instance during provisioning.
  name: id
  type: string
- description: The user-defined name of the SAP HANA Cloud service instance, used for identification in the cockpit and API responses.
  name: name
  type: string
- description: The identifier of the service plan used to provision this instance, determining the available features and resource tiers.
  name: service_plan_id
  type: string
- description: The platform identifier indicating the runtime environment (e.g., cloud-foundry or kubernetes).
  name: platform_id
  type: string
- description: Platform-specific context information including subaccount, organization, and space details.
  name: context
  type: object
- description: Key-value labels assigned to the instance for organization and filtering purposes.
  name: labels
  type: object
- description: ISO 8601 timestamp when the service instance was created.
  name: created_at
  type: string
- description: ISO 8601 timestamp when the service instance was last updated.
  name: updated_at
  type: string
- description: Indicates whether the service instance is fully provisioned and ready for use.
  name: ready
  type: boolean
- description: Indicates whether the service instance is currently usable, accounting for both provisioning state and operational status.
  name: usable
  type: boolean
provider_name: SAP HANA
provider_slug: sap-hana
schema_file: json-schema/sap-hana-cloud-rest-service-instance-schema.json
slug: sap-hana-cloud-rest-service-instance
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
title: ServiceInstance
---
