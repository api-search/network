---
description: A configured instance of an integration in Cortex XSOAR.
layout: schema
name: IntegrationInstance
properties_list:
- description: ''
  name: id
  type: string
- description: Unique name of this instance.
  name: name
  type: string
- description: Integration brand name.
  name: brand
  type: string
- description: ''
  name: enabled
  type: string
- description: ''
  name: isIntegrationScript
  type: boolean
- description: ''
  name: incomingMapperId
  type: string
- description: ''
  name: mappingId
  type: string
- description: Integration configuration parameters.
  name: configuration
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsoar-api-integration-instance-schema.json
slug: cortex-xsoar-api-integration-instance
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: IntegrationInstance
---
