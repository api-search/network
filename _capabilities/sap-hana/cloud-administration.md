---
consumed_apis:
- hana-cloud-rest
description: Unified workflow for SAP HANA Cloud database administration including instance lifecycle management, monitoring alerts, performance metrics, and metering. Used by database administrators and cloud platform engineers.
layout: capability
name: SAP HANA Cloud Administration
operations:
- description: List all SAP HANA Cloud instances.
  method: GET
  name: list-instances
  path: /v1/instances
- description: Provision a new instance.
  method: POST
  name: create-instance
  path: /v1/instances
- description: Get instance details.
  method: GET
  name: get-instance
  path: /v1/instances/{instanceId}
- description: Update an instance.
  method: PATCH
  name: update-instance
  path: /v1/instances/{instanceId}
- description: Delete an instance.
  method: DELETE
  name: delete-instance
  path: /v1/instances/{instanceId}
- description: List alert events.
  method: GET
  name: list-alerts
  path: /v1/alerts
- description: Get database metrics.
  method: GET
  name: get-metrics
  path: /v1/metrics
personas: []
provider_name: SAP HANA
provider_slug: sap-hana
search_terms:
- list all sap hana cloud instances.
- get instance details.
- delete a service instance permanently.
- provision a new instance.
- delete mapping
- update instance configuration.
- analytics
- get database metrics.
- list instances
- get metering
- list mappings
- list alert rules for an instance.
- retrieve database performance metrics.
- list instance mappings.
- administration
- list alert rules
- enterprise
- delete an instance.
- get instance
- get details of a specific instance.
- retrieve consumption metering data.
- alert monitoring.
- cloud
- list triggered alert events for an instance.
- performance metrics.
- in-memory
- update an instance.
- provision a new sap hana cloud instance.
- update alert rules for an instance.
- sap hana
- individual instance operations.
- list alert events.
- delete instance
- delete an instance mapping.
- list all instances in the inventory.
- create mapping
- get metrics
- create a new instance mapping.
- list alerts
- instance lifecycle management.
- list inventory
- list all sap hana cloud service instances.
- update instance
- update alert rules
- create instance
- database
- monitoring
slug: cloud-administration
tags:
- SAP HANA
- Cloud
- Administration
- Monitoring
tools:
- description: List all SAP HANA Cloud service instances.
  hints:
    openWorld: true
    readOnly: true
  name: list-instances
- description: Provision a new SAP HANA Cloud instance.
  hints:
    readOnly: false
  name: create-instance
- description: Get details of a specific instance.
  hints:
    readOnly: true
  name: get-instance
- description: Update instance configuration.
  hints:
    idempotent: true
    readOnly: false
  name: update-instance
- description: Delete a service instance permanently.
  hints:
    destructive: true
    idempotent: true
  name: delete-instance
- description: List all instances in the inventory.
  hints:
    readOnly: true
  name: list-inventory
- description: List triggered alert events for an instance.
  hints:
    readOnly: true
  name: list-alerts
- description: List alert rules for an instance.
  hints:
    readOnly: true
  name: list-alert-rules
- description: Update alert rules for an instance.
  hints:
    idempotent: true
    readOnly: false
  name: update-alert-rules
- description: Retrieve database performance metrics.
  hints:
    readOnly: true
  name: get-metrics
- description: Retrieve consumption metering data.
  hints:
    readOnly: true
  name: get-metering
- description: List instance mappings.
  hints:
    readOnly: true
  name: list-mappings
- description: Create a new instance mapping.
  hints:
    readOnly: false
  name: create-mapping
- description: Delete an instance mapping.
  hints:
    destructive: true
    idempotent: true
  name: delete-mapping
---
