---
description: Request to list investigations
layout: schema
name: ListInvestigationsRequest
properties_list:
- description: The ARN of the behavior graph.
  name: GraphArn
  type: string
- description: Lists the investigations for a behavior graph based on the maximum number of investigations in a page.
  name: NextToken
  type: string
- description: Lists the investigations for a behavior graph based on the total number of investigations.
  name: MaxResults
  type: integer
- description: Filters the investigation results based on a criteria.
  name: FilterCriteria
  type: object
- description: Sorts the investigation results based on a criteria.
  name: SortCriteria
  type: object
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-list-investigations-request-schema.json
slug: amazon-detective-list-investigations-request
tags:
- AWS
- Forensics
- Investigation
- Security
title: ListInvestigationsRequest
---
