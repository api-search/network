---
description: A collection of OData report data rows
layout: schema
name: ODataRowCollection
properties_list:
- description: Total count of rows (when $inlinecount=allpages is used)
  name: __count
  type: string
- description: URI for the next page of results
  name: __next
  type: string
- description: Array of data rows
  name: value
  type: array
provider_name: Crystal Reports
provider_slug: crystal-reports
schema_file: json-schema/crystal-reports-o-data-row-collection-schema.json
slug: crystal-reports-o-data-row-collection
tags:
- Business Intelligence
- Crystal Reports
- Data Analytics
- Enterprise Software
- Reporting
- SAP
title: ODataRowCollection
---
