---
description: SearchRequest schema from openapi
layout: schema
name: SearchRequest
properties_list:
- description: A string that includes keywords and filters to search for resources.
  name: QueryString
  type: string
- description: The maximum number of results to include in the response.
  name: MaxResults
  type: integer
- description: The token for the next page of results.
  name: NextToken
  type: string
- description: The ARN of the view to search.
  name: ViewArn
  type: string
provider_name: Amazon Resource Explorer
provider_slug: amazon-resource-explorer
schema_file: json-schema/amazon-resource-explorer-openapi-search-request-schema.json
slug: amazon-resource-explorer-openapi-search-request
tags:
- AWS
- Discovery
- Inventory
- Operations
- Resource Management
title: SearchRequest
---
