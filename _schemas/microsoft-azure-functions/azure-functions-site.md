---
description: A web app, a mobile app backend, or an API app.
layout: schema
name: Site
properties_list:
- description: Site resource specific properties
  name: properties
  type: object
- description: Managed service identity.
  name: identity
  type: object
- description: Extended Location.
  name: extendedLocation
  type: object
- description: Kind of resource. If the resource is an app, you can refer to https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference fo
  name: kind
  type: string
provider_name: Microsoft Azure Functions
provider_slug: microsoft-azure-functions
schema_file: json-schema/azure-functions-site-schema.json
slug: azure-functions-site
tags:
- Azure
- Cloud
- Compute
- Event-Driven
- Microsoft
- Serverless
title: Site
---
