---
description: SearchResponse schema from openapi
layout: schema
name: SearchResponse
properties_list:
- description: The count of matching resources.
  name: Count
  type: object
- description: The token for the next page of results.
  name: NextToken
  type: string
- description: ''
  name: Resources
  type: array
- description: The ARN of the view used for the search.
  name: ViewArn
  type: string
provider_name: Amazon Resource Explorer
provider_slug: amazon-resource-explorer
schema_file: json-schema/amazon-resource-explorer-openapi-search-response-schema.json
slug: amazon-resource-explorer-openapi-search-response
tags:
- AWS
- Discovery
- Inventory
- Operations
- Resource Management
title: SearchResponse
---
