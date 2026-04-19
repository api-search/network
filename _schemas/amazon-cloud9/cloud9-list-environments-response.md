---
description: Response for listing environments.
layout: schema
name: ListEnvironmentsResponse
properties_list:
- description: If there are more than 25 items in the list, only the first 25 are returned.
  name: nextToken
  type: string
- description: The list of environment identifiers.
  name: environmentIds
  type: array
provider_name: Amazon Cloud9
provider_slug: amazon-cloud9
schema_file: json-schema/cloud9-list-environments-response-schema.json
slug: cloud9-list-environments-response
tags:
- AWS
- Cloud9
- IDE
- Development
- Browser-Based
title: ListEnvironmentsResponse
---
