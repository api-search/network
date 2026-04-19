---
description: An SAP HANA Cloud database instance representing an in-memory, column-oriented, relational database deployed on SAP Business Technology Platform. Each instance provides a fully managed SAP HANA database with configurable memory, vCPU, and storage resources, along with optional services such as the script server for predictive analysis, the JSON document store for semi-structured data, and the data provisioning server for smart data integration. Instances are provisioned within SAP BTP subaccounts and managed through the SAP HANA Cloud REST API or SAP HANA Cloud Central cockpit.
layout: schema
name: SAP HANA Cloud Database Instance
properties_list:
- description: The unique identifier assigned to the SAP HANA Cloud service instance during provisioning. This UUID is used in all API operations to reference the specific database instance and remains constant thro
  name: id
  type: string
- description: The user-defined name of the SAP HANA Cloud database instance. Must be unique within the SAP BTP subaccount and is used for identification in the SAP HANA Cloud Central cockpit, API responses, and ser
  name: name
  type: string
- description: The identifier of the SAP BTP service plan used to provision this instance. The service plan determines the instance type (e.g., hana for SAP HANA database, hana-td for SAP HANA database with data tie
  name: service_plan_id
  type: string
- description: The human-readable name of the service plan used for this instance, indicating the database type and tier.
  name: service_plan_name
  type: string
- description: The platform identifier indicating the SAP BTP runtime environment where the instance is deployed. Typically cloud-foundry for Cloud Foundry-based environments or kubernetes for Kyma-based environment
  name: platform_id
  type: string
- description: ''
  name: context
  type: object
- description: ''
  name: parameters
  type: object
- description: 'Key-value labels assigned to the instance for organization, filtering, and governance purposes within the SAP BTP subaccount. Labels can be used to categorize instances by environment, team, project, '
  name: labels
  type: object
- description: ISO 8601 timestamp when the SAP HANA Cloud service instance was initially provisioned. Set automatically during instance creation and remains constant throughout the instance lifecycle.
  name: created_at
  type: string
- description: ISO 8601 timestamp when the SAP HANA Cloud service instance was last modified. Updated automatically whenever instance configuration, state, or metadata is changed through the API or cockpit.
  name: updated_at
  type: string
- description: Indicates whether the SAP HANA Cloud instance has completed provisioning and is ready to accept database connections. An instance is not ready during initial provisioning, scaling operations, or error
  name: ready
  type: boolean
- description: Indicates whether the SAP HANA Cloud instance is currently operational and accepting database connections. An instance may be provisioned (ready) but not usable if it has been intentionally stopped to
  name: usable
  type: boolean
- description: ''
  name: last_operation
  type: object
- description: The current provisioning lifecycle state of the instance, reflecting whether the underlying infrastructure has been fully set up, is being modified, or is being removed.
  name: provisioningState
  type: string
- description: The current running state of the database instance. A Started instance is running and accepting connections, while a Stopped instance retains all data but does not consume compute resources.
  name: operationalState
  type: string
- description: ''
  name: connectionEndpoints
  type: object
- description: The list of currently active alerts for this database instance, monitoring conditions such as memory pressure, disk usage, long-running statements, and connection limits.
  name: alerts
  type: array
- description: ''
  name: metrics
  type: object
provider_name: SAP HANA
provider_slug: sap-hana
schema_file: json-schema/sap-hana-database-schema.json
slug: sap-hana-database
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
title: SAP HANA Cloud Database Instance
---
