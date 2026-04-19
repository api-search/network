---
description: FailedConfiguration schema from Amazon Application Discovery Service API
layout: schema
name: FailedConfiguration
properties_list:
- description: The configuration ID of the configuration that failed to delete.
  name: configurationId
  type: string
- description: The error status code.
  name: errorStatusCode
  type: integer
- description: A descriptive message indicating why the associated configuration failed to delete.
  name: errorMessage
  type: string
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-failed-configuration-schema.json
slug: application-discovery-service-failed-configuration
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: FailedConfiguration
---
