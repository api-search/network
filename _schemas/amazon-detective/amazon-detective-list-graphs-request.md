---
description: Request to list behavior graphs
layout: schema
name: ListGraphsRequest
properties_list:
- description: For requests to get the next page of results. The pagination token from the previous request.
  name: NextToken
  type: string
- description: The maximum number of graphs to return at a time.
  name: MaxResults
  type: integer
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-list-graphs-request-schema.json
slug: amazon-detective-list-graphs-request
tags:
- AWS
- Forensics
- Investigation
- Security
title: ListGraphsRequest
---
