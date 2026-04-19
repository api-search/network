---
description: ''
layout: schema
name: SearchResponse
properties_list:
- description: ''
  name: error
  type: boolean
- description: ''
  name: features
  type: array
- description: Number of requested items per page
  name: itemsPerPage
  type: integer
- description: The index of the first item present in the response
  name: startIndex
  type: integer
- description: The total number of items present in the catalog
  name: totalResults
  type: integer
- description: ''
  name: type
  type: string
provider_name: Airbus OneAtlas
provider_slug: airbus-oneatlas
schema_file: json-schema/oneatlas-search-response-schema.json
slug: oneatlas-search-response
tags:
- Imagery
- Satellites
title: SearchResponse
---
