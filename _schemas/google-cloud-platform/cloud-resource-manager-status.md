---
description: The Status type defines a logical error model that is suitable for REST APIs. It is used to communicate error details from the API.
layout: schema
name: Status
properties_list:
- description: The status code, which should be an enum value of google.rpc.Code.
  name: code
  type: integer
- description: A developer-facing error message in English.
  name: message
  type: string
- description: A list of messages that carry the error details.
  name: details
  type: array
provider_name: Google Cloud Platform
provider_slug: google-cloud-platform
schema_file: json-schema/cloud-resource-manager-status-schema.json
slug: cloud-resource-manager-status
tags:
- API Management
- Cloud Computing
- Infrastructure
- Platform as a Service
title: Status
---
