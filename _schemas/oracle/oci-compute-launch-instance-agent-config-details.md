---
description: Configuration options for the Oracle Cloud Agent on launch
layout: schema
name: LaunchInstanceAgentConfigDetails
properties_list:
- description: Whether to disable the Monitoring plugin
  name: isMonitoringDisabled
  type: boolean
- description: Whether to disable the Management plugin
  name: isManagementDisabled
  type: boolean
- description: Whether to disable all plugins
  name: areAllPluginsDisabled
  type: boolean
- description: Plugin configuration details
  name: pluginsConfig
  type: array
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-launch-instance-agent-config-details-schema.json
slug: oci-compute-launch-instance-agent-config-details
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: LaunchInstanceAgentConfigDetails
---
