---
description: The result of a SOQL query, containing the matching records and pagination metadata.
layout: schema
name: QueryResult
properties_list:
- description: The total number of records matching the query. May be larger than the number of records in the current page if the result is paginated.
  name: totalSize
  type: integer
- description: Whether all query results have been returned. If false, use nextRecordsUrl to retrieve the next page.
  name: done
  type: boolean
- description: URL to retrieve the next page of results. Only present when done is false.
  name: nextRecordsUrl
  type: string
- description: Array of SObject records matching the query. May be a partial result if the total exceeds the page size.
  name: records
  type: array
provider_name: Salesforce
provider_slug: salesforce
schema_file: json-schema/salesforce-rest-query-result-schema.json
slug: salesforce-rest-query-result
tags:
- AI
- Analytics
- Cloud
- Commerce
- CRM
- Customer Service
- Enterprise
- Marketing
- Platform
- Sales
title: QueryResult
---
