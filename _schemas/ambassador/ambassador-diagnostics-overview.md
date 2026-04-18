---
description: Diagnostic overview of an Ambassador instance
layout: schema
name: DiagnosticsOverview
properties_list:
- description: System-level information
  name: system
  type: object
- description: Active Ambassador configuration summary
  name: ambassador_config
  type: object
- description: Status of the underlying Envoy proxy
  name: envoy_status
  type: object
- description: Summary of active routes
  name: route_info
  type: array
- description: List of configuration errors
  name: errors
  type: array
provider_name: Ambassador
provider_slug: ambassador
schema_file: json-schema/ambassador-diagnostics-overview-schema.json
slug: ambassador-diagnostics-overview
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
title: DiagnosticsOverview
---
