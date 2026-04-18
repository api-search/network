---
description: Configuration options for the Oracle Cloud Agent software
layout: schema
name: InstanceAgentConfig
properties_list:
- description: Whether the Monitoring plugin is disabled
  name: isMonitoringDisabled
  type: boolean
- description: Whether the Management plugin is disabled
  name: isManagementDisabled
  type: boolean
- description: Whether all plugins are disabled
  name: areAllPluginsDisabled
  type: boolean
- description: The configuration of plugins associated with this instance
  name: pluginsConfig
  type: array
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-instance-agent-config-schema.json
slug: oci-compute-instance-agent-config
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: InstanceAgentConfig
---
