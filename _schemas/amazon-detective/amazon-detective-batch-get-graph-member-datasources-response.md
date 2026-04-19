---
description: Response from getting datasource details for behavior graph members
layout: schema
name: BatchGetGraphMemberDatasourcesResponse
properties_list:
- description: Details on the data source packages active in the behavior graph.
  name: MemberDatasources
  type: array
- description: Accounts that data source package information could not be retrieved for.
  name: UnprocessedAccounts
  type: array
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-batch-get-graph-member-datasources-response-schema.json
slug: amazon-detective-batch-get-graph-member-datasources-response
tags:
- AWS
- Forensics
- Investigation
- Security
title: BatchGetGraphMemberDatasourcesResponse
---
