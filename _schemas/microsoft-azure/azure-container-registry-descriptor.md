---
description: Docker V2 image layer descriptor.
layout: schema
name: Descriptor
properties_list:
- description: Layer media type.
  name: mediaType
  type: string
- description: Layer size.
  name: size
  type: integer
- description: Layer digest.
  name: digest
  type: string
- description: Specifies a list of URLs from which this object may be downloaded.
  name: urls
  type: array
- description: Additional information about the descriptor.
  name: annotations
  type: object
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-container-registry-descriptor-schema.json
slug: azure-container-registry-descriptor
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: Descriptor
---
