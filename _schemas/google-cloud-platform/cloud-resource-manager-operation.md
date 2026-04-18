---
description: Represents a long-running operation that is the result of a network API call. Many Resource Manager operations are asynchronous and return an Operation that can be polled for status.
layout: schema
name: Operation
properties_list:
- description: The server-assigned name, which is only unique within the same service. Used to poll for the operation status.
  name: name
  type: string
- description: Service-specific metadata associated with the operation.
  name: metadata
  type: object
- description: If true, the operation is complete and either error or response is available.
  name: done
  type: boolean
- description: The normal response of the operation. Contains the result on success.
  name: response
  type: object
provider_name: Google Cloud Platform
provider_slug: google-cloud-platform
schema_file: json-schema/cloud-resource-manager-operation-schema.json
slug: cloud-resource-manager-operation
tags:
- API Management
- Cloud Computing
- Infrastructure
- Platform as a Service
title: Operation
---
