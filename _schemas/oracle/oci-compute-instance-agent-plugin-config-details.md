---
description: Configuration details for an Oracle Cloud Agent plugin
layout: schema
name: InstanceAgentPluginConfigDetails
properties_list:
- description: The plugin name (e.g., Vulnerability Scanning, Bastion)
  name: name
  type: string
- description: Whether the plugin should be enabled or disabled
  name: desiredState
  type: string
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-instance-agent-plugin-config-details-schema.json
slug: oci-compute-instance-agent-plugin-config-details
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: InstanceAgentPluginConfigDetails
---
