---
description: ''
layout: schema
name: LoggingConfig
properties_list:
- description: Log output directory
  name: logDirectory
  type: string
- description: ''
  name: consoleLogLevel
  type: string
- description: Name of the messages log file
  name: messageFileName
  type: string
- description: Name of the trace log file
  name: traceFileName
  type: string
- description: Trace specification string
  name: traceSpecification
  type: string
- description: Maximum log file size in MB
  name: maxFileSize
  type: integer
- description: Maximum number of log files
  name: maxFiles
  type: integer
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-liberty-admin-rest-logging-config-schema.json
slug: websphere-liberty-admin-rest-logging-config
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: LoggingConfig
---
