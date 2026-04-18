---
description: A Meraki network.
layout: schema
name: Network
properties_list:
- description: Network ID.
  name: id
  type: string
- description: Organization ID.
  name: organizationId
  type: string
- description: Network name.
  name: name
  type: string
- description: Product types in the network.
  name: productTypes
  type: array
- description: Timezone of the network.
  name: timeZone
  type: string
- description: Tags applied to the network.
  name: tags
  type: array
provider_name: Cisco
provider_slug: cisco
schema_file: json-schema/cisco-meraki-api-network-schema.json
slug: cisco-meraki-api-network
tags:
- Collaboration
- Enterprise
- Networking
- Security
- SD-WAN
title: Network
---
