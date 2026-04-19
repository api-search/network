---
description: Response from getting membership datasource history
layout: schema
name: BatchGetMembershipDatasourcesResponse
properties_list:
- description: Details on the data source packages active in the behavior graph.
  name: MembershipDatasources
  type: array
- description: Graphs that data source package information could not be retrieved for.
  name: UnprocessedGraphs
  type: array
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-batch-get-membership-datasources-response-schema.json
slug: amazon-detective-batch-get-membership-datasources-response
tags:
- AWS
- Forensics
- Investigation
- Security
title: BatchGetMembershipDatasourcesResponse
---
