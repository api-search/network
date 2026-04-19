---
description: A behavior graph that could not be processed
layout: schema
name: UnprocessedGraph
properties_list:
- description: The ARN of the organization behavior graph.
  name: GraphArn
  type: string
- description: The reason data source package information could not be retrieved for the behavior graph.
  name: Reason
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-unprocessed-graph-schema.json
slug: amazon-detective-unprocessed-graph
tags:
- AWS
- Forensics
- Investigation
- Security
title: UnprocessedGraph
---
