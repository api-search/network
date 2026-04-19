---
description: Request to get datasource details for behavior graph members
layout: schema
name: BatchGetGraphMemberDatasourcesRequest
properties_list:
- description: The ARN of the behavior graph.
  name: GraphArn
  type: string
- description: The list of AWS accounts to get data source package information for.
  name: AccountIds
  type: array
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-batch-get-graph-member-datasources-request-schema.json
slug: amazon-detective-batch-get-graph-member-datasources-request
tags:
- AWS
- Forensics
- Investigation
- Security
title: BatchGetGraphMemberDatasourcesRequest
---
