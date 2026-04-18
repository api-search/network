---
description: The base resource model for Azure Resource Manager resources. All Azure resources inherit from this schema, which defines the standard properties shared by all Azure resource types including ID, name, type, location, tags, and system metadata.
layout: schema
name: Azure Resource
properties_list:
- description: Fully qualified resource ID for the resource. The format is /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
  name: id
  type: string
- description: The name of the resource.
  name: name
  type: string
- description: The type of the resource, in the format {resourceProviderNamespace}/{resourceType}.
  name: type
  type: string
- description: The geo-location where the resource lives. Must be one of the supported Azure regions.
  name: location
  type: string
- description: Resource tags. Key-value pairs used to organize and categorize Azure resources for billing, management, and automation purposes.
  name: tags
  type: object
- description: The fully qualified resource ID of the resource that manages this resource. Used when a resource is managed by another Azure resource.
  name: managedBy
  type: string
- description: The kind of the resource. Metadata used by the portal/tooling/etc. to render different UX experiences for resources of the same type.
  name: kind
  type: string
- description: Resource Etag for optimistic concurrency control.
  name: etag
  type: string
- description: ''
  name: identity
  type: object
- description: ''
  name: sku
  type: object
- description: ''
  name: plan
  type: object
- description: The availability zones for the resource.
  name: zones
  type: array
- description: ''
  name: systemData
  type: object
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/microsoft-azure-resource-schema.json
slug: microsoft-azure-resource
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: Azure Resource
---
