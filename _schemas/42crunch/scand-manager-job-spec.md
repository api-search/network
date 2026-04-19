---
description: Specification for creating a new conformance scan job
layout: schema
name: JobSpec
properties_list:
- description: On-premises scan token issued by the 42Crunch Platform
  name: token
  type: string
- description: ''
  name: name
  type: object
- description: Expiration time for the job in seconds (max 7 days)
  name: expirationTime
  type: integer
- description: Hostname and port for connecting to the 42Crunch Platform
  name: platformService
  type: string
- description: Docker image for the scand-agent container
  name: scandImage
  type: string
- description: Environment variables for scand-agent. Must start with SECURITY_, SCAN42C_, HTTP_PROXY, HTTPS_PROXY, HTTP_PROXY_API, HTTPS_PROXY_API, NO_PROXY, or NO_PROXY_API.
  name: env
  type: object
provider_name: 42Crunch
provider_slug: 42crunch
schema_file: json-schema/scand-manager-job-spec-schema.json
slug: scand-manager-job-spec
tags:
- API Security
- Platform
- Scanning
- Security
- OpenAPI
- DevSecOps
title: JobSpec
---
