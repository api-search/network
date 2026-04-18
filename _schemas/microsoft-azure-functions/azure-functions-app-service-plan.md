---
description: App Service plan.
layout: schema
name: AppServicePlan
properties_list:
- description: AppServicePlan resource specific properties
  name: properties
  type: object
- description: Description of a SKU for a scalable resource.
  name: sku
  type: object
- description: Extended Location.
  name: extendedLocation
  type: object
- description: Kind of resource. If the resource is an app, you can refer to https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference fo
  name: kind
  type: string
- description: Managed service identity.
  name: identity
  type: object
provider_name: Microsoft Azure Functions
provider_slug: microsoft-azure-functions
schema_file: json-schema/azure-functions-app-service-plan-schema.json
slug: azure-functions-app-service-plan
tags:
- Azure
- Cloud
- Compute
- Event-Driven
- Microsoft
- Serverless
title: AppServicePlan
---
