---
description: ListConfigurationsRequest schema from Amazon Application Discovery Service API
layout: schema
name: ListConfigurationsRequest
properties_list:
- description: A valid configuration identified by Application Discovery Service.
  name: configurationType
  type: string
- description: You can filter the list using a key-value format.
  name: filters
  type: array
- description: The total number of items to return. The maximum value is 100.
  name: maxResults
  type: integer
- description: Token to retrieve the next set of results.
  name: nextToken
  type: string
- description: Certain filter criteria return output that can be sorted in ascending or descending order. For a list of output characteristics for each filter, see Using the ListConfigurations Action in the AWS Appl
  name: orderBy
  type: array
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-list-configurations-request-schema.json
slug: application-discovery-service-list-configurations-request
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: ListConfigurationsRequest
---
