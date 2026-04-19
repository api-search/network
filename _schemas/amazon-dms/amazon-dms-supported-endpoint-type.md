---
description: Provides information about types of supported endpoints in response to a request by the <code>DescribeEndpointTypes</code> operation. This information includes the type of endpoint, the database engine name, and whether change data capture (CDC) is supported.
layout: schema
name: SupportedEndpointType
properties_list:
- description: ''
  name: EngineName
  type: object
- description: ''
  name: SupportsCDC
  type: object
- description: ''
  name: EndpointType
  type: object
- description: ''
  name: ReplicationInstanceEngineMinimumVersion
  type: object
- description: ''
  name: EngineDisplayName
  type: object
provider_name: Amazon DMS
provider_slug: amazon-dms
schema_file: json-schema/amazon-dms-supported-endpoint-type-schema.json
slug: amazon-dms-supported-endpoint-type
tags:
- AWS
- Data Replication
- Database
- Database Migration
- Migration
title: SupportedEndpointType
---
