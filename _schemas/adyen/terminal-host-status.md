---
description: Indicate the reachability of the host by the POI Terminal. State of a Host.
layout: schema
name: HostStatus
properties_list:
- description: Identification of the Acquirer.
  name: AcquirerID
  type: integer
- description: Indicate if a Host is reachable.
  name: IsReachableFlag
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-host-status-schema.json
slug: terminal-host-status
tags:
- Payments
- Financial Services
- Fintech
title: HostStatus
---
