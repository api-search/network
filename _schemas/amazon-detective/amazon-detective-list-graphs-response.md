---
description: Response from listing behavior graphs
layout: schema
name: ListGraphsResponse
properties_list:
- description: A list of behavior graphs that the account is an administrator account of.
  name: GraphList
  type: array
- description: If there are more behavior graphs remaining in the results, then this is the pagination token to use.
  name: NextToken
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-list-graphs-response-schema.json
slug: amazon-detective-list-graphs-response
tags:
- AWS
- Forensics
- Investigation
- Security
title: ListGraphsResponse
---
