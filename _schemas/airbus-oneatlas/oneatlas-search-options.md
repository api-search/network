---
description: ''
layout: schema
name: SearchOptions
properties_list:
- description: The acquisition date or the acquisition date range.
  name: acquisitionDate
  type: object
- description: The geographic search area expressed as a bbox string (decimal degrees values separated by a comma). Values are min lon,min lat, max lon, max lat.
  name: bbox
  type: string
- description: The cloud cover percentage or the cloud cover percentage range.
  name: cloudCover
  type: object
- description: The commercial reference.
  name: commercialReference
  type: string
- description: The constellation or constellation list (comma separated list). Possible values will be described in a future endpoint (*/api/v1/opensearch/domains/constellation*).
  name: constellation
  type: string
- description: ''
  name: correlationId
  type: object
- description: ''
  name: expirationDate
  type: object
- description: The geographic search area.
  name: geometry
  type: object
- description: ''
  name: id
  type: object
- description: The incident angle or the incident angle range in degree.
  name: incidenceAngle
  type: object
- description: The maximum number of items that the response can contain.
  name: itemsPerPage
  type: integer
- description: The requested page
  name: page
  type: integer
- description: The parent identifier (identified as sourceId in other catalogs)
  name: parentIdentifier
  type: string
- description: The platform or platform list (comma separated list). Possible values will be described in a future endpoint (*/api/v1/opensearch/domains/platform*).
  name: platform
  type: string
- description: The product type or product type list (comma separated list). Possible values will be described in a future endpoint (*/api/v1/opensearch/domains/productType*).
  name: productType
  type: string
- description: The production status or production status list (comma separated list).
  name: productionStatus
  type: string
- description: The publication date or the publication date range.
  name: publicationDate
  type: object
- description: A generic query parameter, will search in productType and title. Search is in "contains" mode.
  name: q
  type: string
- description: The resolution or the resolution range in meters.
  name: resolution
  type: object
- description: The snow cover percentage or the snow cover percentage range.
  name: snowCover
  type: object
- description: The order strategy for the items. Accepted values are all opensearch attributes separated by a comma. Minus sign can be used to sort descending on the attribute. Otherwise the sort is ascending.
  name: sortBy
  type: string
- description: The product identifier inside original referential
  name: sourceIdentifier
  type: string
- description: The workspace id/name or workspace id/name list (comma separated list)
  name: workspace
  type: string
provider_name: Airbus OneAtlas
provider_slug: airbus-oneatlas
schema_file: json-schema/oneatlas-search-options-schema.json
slug: oneatlas-search-options
tags:
- Imagery
- Satellites
title: SearchOptions
---
