---
description: Process model settings for the application pool worker processes.
layout: schema
name: ProcessModel
properties_list:
- description: The idle timeout in minutes before a worker process is shut down.
  name: idle_timeout
  type: integer
- description: The maximum number of worker processes for the application pool (web garden).
  name: max_processes
  type: integer
- description: Whether health monitoring pings are enabled.
  name: pinging_enabled
  type: boolean
- description: The interval in seconds between health monitoring pings.
  name: ping_interval
  type: integer
- description: The maximum time in seconds allowed for a worker process to respond to a health ping.
  name: ping_response_time
  type: integer
- description: The time in seconds allowed for a worker process to gracefully shut down.
  name: shutdown_time_limit
  type: integer
- description: The time in seconds allowed for a worker process to start up.
  name: startup_time_limit
  type: integer
- description: The action to take when the idle timeout is reached.
  name: idle_timeout_action
  type: string
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/iis-administration-process-model-schema.json
slug: iis-administration-process-model
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: ProcessModel
---
