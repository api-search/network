---
description: BrowserDeployment schema from Palo Alto Networks Prisma Access Browser Management API
layout: schema
name: BrowserDeployment
properties_list:
- description: Unique identifier of the deployment.
  name: deployment_id
  type: string
- description: Display name of the deployment.
  name: name
  type: string
- description: Description of the deployment configuration.
  name: description
  type: string
- description: Target operating system platform.
  name: platform
  type: string
- description: Default browser policy assigned to users in this deployment.
  name: policy_id
  type: string
- description: Browser update channel for this deployment.
  name: update_channel
  type: string
- description: Number of devices in this deployment.
  name: device_count
  type: integer
- description: ''
  name: created_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-browser-api-browser-deployment-schema.json
slug: prisma-access-browser-api-browser-deployment
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: BrowserDeployment
---
