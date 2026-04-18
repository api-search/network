---
description: A system registered in QueryGrid.
layout: schema
name: System
properties_list:
- description: Unique system identifier.
  name: id
  type: string
- description: System name.
  name: name
  type: string
- description: System type.
  name: type
  type: string
- description: Parent data center identifier.
  name: dataCenterId
  type: string
- description: System status.
  name: status
  type: string
- description: System hostname.
  name: hostname
  type: string
provider_name: Teradata
provider_slug: teradata
schema_file: json-schema/querygrid-manager-api-system-schema.json
slug: querygrid-manager-api-system
tags:
- Analytics
- Cloud
- Data Management
- Data Warehousing
- Database
- Enterprise
- Machine Learning
- SQL
title: System
---
