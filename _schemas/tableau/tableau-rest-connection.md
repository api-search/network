---
description: ''
layout: schema
name: Connection
properties_list:
- description: The unique identifier for the connection.
  name: id
  type: string
- description: The type of connection (e.g., sqlserver, postgres).
  name: type
  type: string
- description: The address of the server for the connection.
  name: serverAddress
  type: string
- description: The port used for the connection.
  name: serverPort
  type: string
- description: The user name for the connection.
  name: userName
  type: string
- description: ''
  name: datasource
  type: object
provider_name: Tableau
provider_slug: tableau
schema_file: json-schema/tableau-rest-connection-schema.json
slug: tableau-rest-connection
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
title: Connection
---
