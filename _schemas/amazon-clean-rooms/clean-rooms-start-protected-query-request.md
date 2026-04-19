---
description: Request body for starting a protected query.
layout: schema
name: StartProtectedQueryRequest
properties_list:
- description: The type of the protected query.
  name: type
  type: string
- description: The parameters for the SQL type protected query.
  name: sqlParameters
  type: object
- description: Contains configuration details for protected query results.
  name: resultConfiguration
  type: object
provider_name: Amazon Clean Rooms
provider_slug: amazon-clean-rooms
schema_file: json-schema/clean-rooms-start-protected-query-request-schema.json
slug: clean-rooms-start-protected-query-request
tags:
- AWS
- Clean Rooms
- Data Collaboration
- Privacy
- Analytics
- Marketing
title: StartProtectedQueryRequest
---
