---
description: Amazon Kendra query result containing ranked document passages and answers.
layout: schema
name: QueryResult
properties_list:
- description: The unique identifier for the query.
  name: QueryId
  type: string
- description: The results of the search query.
  name: ResultItems
  type: array
- description: The total number of items found.
  name: TotalNumberOfResults
  type: integer
- description: Contains the facet results.
  name: FacetResults
  type: array
provider_name: Amazon Kendra
provider_slug: amazon-kendra
schema_file: json-schema/amazon-kendra-query-result-schema.json
slug: amazon-kendra-query-result
tags:
- AI
- AWS
- Enterprise Search
- Knowledge Management
- Machine Learning
- Natural Language
title: QueryResult
---
