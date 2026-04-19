---
description: Response from listing indicators
layout: schema
name: ListIndicatorsResponse
properties_list:
- description: The ARN of the behavior graph.
  name: GraphArn
  type: string
- description: The investigation ID of the investigation report.
  name: InvestigationId
  type: string
- description: List if there are more results available.
  name: NextToken
  type: string
- description: Lists the indicators of compromise.
  name: Indicators
  type: array
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-list-indicators-response-schema.json
slug: amazon-detective-list-indicators-response
tags:
- AWS
- Forensics
- Investigation
- Security
title: ListIndicatorsResponse
---
