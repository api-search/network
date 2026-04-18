---
description: Error response returned by the OCI API
layout: schema
name: Error
properties_list:
- description: A short error code that defines the error, meant for programmatic parsing
  name: code
  type: string
- description: A human-readable error string
  name: message
  type: string
- description: The HTTP status code
  name: status
  type: integer
- description: Unique Oracle-assigned identifier for the request
  name: opcRequestId
  type: string
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-error-schema.json
slug: oci-compute-error
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: Error
---
