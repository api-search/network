---
description: Status information for a Host resource
layout: schema
name: HostStatus
properties_list:
- description: Current state of the Host
  name: state
  type: string
- description: Last completed phase of the Host lifecycle
  name: phaseCompleted
  type: string
- description: Description of any error state
  name: errorReason
  type: string
- description: Source of the TLS certificate
  name: tlsCertificateSource
  type: string
provider_name: Ambassador
provider_slug: ambassador
schema_file: json-schema/ambassador-host-status-schema.json
slug: ambassador-host-status
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
title: HostStatus
---
