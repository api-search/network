---
description: Information about a SASE service affected by a notification.
layout: schema
name: ServiceInfo
properties_list:
- description: Name of the SASE service.
  name: serviceName
  type: string
- description: Current operational status of the service.
  name: serviceStatus
  type: string
- description: Region where the service is deployed.
  name: region
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-notifications-service-info-schema.json
slug: sase-notifications-service-info
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ServiceInfo
---
