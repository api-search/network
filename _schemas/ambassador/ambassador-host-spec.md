---
description: Specification for an Ambassador Host
layout: schema
name: HostSpec
properties_list:
- description: Hostname that this Host resource applies to. Supports wildcard patterns like *.example.com.
  name: hostname
  type: string
- description: Ambassador IDs that should apply this Host
  name: ambassador_id
  type: array
- description: ACME certificate provider configuration for automatic TLS certificates
  name: acmeProvider
  type: object
- description: Reference to a TLSContext resource for TLS configuration
  name: tlsContext
  type: object
- description: Reference to a Kubernetes TLS Secret containing certificates
  name: tlsSecret
  type: object
- description: Policy for handling insecure requests
  name: requestPolicy
  type: object
- description: Label selector for Mappings this Host should be associated with
  name: selector
  type: object
provider_name: Ambassador
provider_slug: ambassador
schema_file: json-schema/ambassador-host-spec-schema.json
slug: ambassador-host-spec
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
title: HostSpec
---
