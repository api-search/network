---
description: The result of a Salesforce SOQL (Salesforce Object Query Language) query executed via the REST API /query or /queryAll endpoints. Contains the total number of matching records, a pagination flag, an optional URL for the next page of results, and an array of SObject records matching the query.
layout: schema
name: Salesforce SOQL Query Result
properties_list:
- description: 'The total number of records matching the SOQL query across all pages. This is the count of all matching records, not just the records in the current page. May be larger than the length of the records '
  name: totalSize
  type: integer
- description: Whether all query results have been retrieved and included in the current response. If true, the records array contains all matching records. If false, additional pages of results are available via th
  name: done
  type: boolean
- description: The relative URL to retrieve the next page of query results. Only present when done is false, indicating there are more records beyond the current page. Pass this URL to the GET /query/{queryId} endpo
  name: nextRecordsUrl
  type: string
- description: An array of Salesforce SObject records matching the SOQL query. Each record is an object with an attributes property (containing type and url) plus field name/value pairs for all fields included in th
  name: records
  type: array
provider_name: Salesforce
provider_slug: salesforce
schema_file: json-schema/salesforce-query-result-schema.json
slug: salesforce-query-result
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
title: Salesforce SOQL Query Result
---
