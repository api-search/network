---
description: Response containing a list of objects.
layout: schema
name: ListObjects
properties_list:
- description: List of object summaries.
  name: objects
  type: array
- description: Prefixes for pseudo-directory grouping.
  name: prefixes
  type: array
- description: Object name to resume listing.
  name: nextStartWith
  type: string
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/object-storage-list-objects-schema.json
slug: object-storage-list-objects
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: ListObjects
---
