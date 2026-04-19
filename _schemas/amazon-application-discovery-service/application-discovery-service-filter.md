---
description: Filter schema from Amazon Application Discovery Service API
layout: schema
name: Filter
properties_list:
- description: The name of the filter.
  name: name
  type: string
- description: A string value on which to filter.
  name: values
  type: array
- description: A conditional operator. The following operators are valid — EQUALS, NOT_EQUALS, CONTAINS, NOT_CONTAINS.
  name: condition
  type: string
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-filter-schema.json
slug: application-discovery-service-filter
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: Filter
---
