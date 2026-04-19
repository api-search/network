---
description: Request to list datasource packages
layout: schema
name: ListDatasourcePackagesRequest
properties_list:
- description: The ARN of the behavior graph.
  name: GraphArn
  type: string
- description: For requests to get the next page of results.
  name: NextToken
  type: string
- description: The total number of items to return.
  name: MaxResults
  type: integer
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-list-datasource-packages-request-schema.json
slug: amazon-detective-list-datasource-packages-request
tags:
- AWS
- Forensics
- Investigation
- Security
title: ListDatasourcePackagesRequest
---
