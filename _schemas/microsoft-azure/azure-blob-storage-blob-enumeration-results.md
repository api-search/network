---
description: An enumeration of blobs.
layout: schema
name: BlobEnumerationResults
properties_list:
- description: The service endpoint URL.
  name: ServiceEndpoint
  type: string
- description: The name of the container.
  name: ContainerName
  type: string
- description: The prefix used to filter results.
  name: Prefix
  type: string
- description: The marker used for pagination.
  name: Marker
  type: string
- description: The maximum number of results.
  name: MaxResults
  type: integer
- description: ''
  name: Blobs
  type: object
- description: The next marker for pagination.
  name: NextMarker
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-blob-storage-blob-enumeration-results-schema.json
slug: azure-blob-storage-blob-enumeration-results
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: BlobEnumerationResults
---
