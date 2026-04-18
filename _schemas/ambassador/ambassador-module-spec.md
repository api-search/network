---
description: Specification for a Module resource
layout: schema
name: ModuleSpec
properties_list:
- description: Module configuration. The shape depends on the module name (e.g., ambassador, authentication, tracing).
  name: config
  type: object
- description: Ambassador IDs that should apply this Module
  name: ambassador_id
  type: array
provider_name: Ambassador
provider_slug: ambassador
schema_file: json-schema/ambassador-module-spec-schema.json
slug: ambassador-module-spec
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
title: ModuleSpec
---
