---
description: Request body for registering an instance.
layout: schema
name: RegisterInstanceRequest
properties_list:
- description: An identifier that you want to associate with the instance.
  name: InstanceId
  type: string
- description: A unique string that identifies the request and allows failed RegisterInstance requests to be retried.
  name: CreatorRequestId
  type: string
- description: A string map that contains the following information, including custom attributes.
  name: Attributes
  type: object
provider_name: Amazon Cloud Map
provider_slug: amazon-cloud-map
schema_file: json-schema/cloud-map-register-instance-request-schema.json
slug: cloud-map-register-instance-request
tags:
- AWS
- Cloud Map
- Service Discovery
- Microservices
- DNS
title: RegisterInstanceRequest
---
