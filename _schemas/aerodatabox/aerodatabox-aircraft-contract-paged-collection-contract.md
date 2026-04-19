---
description: AircraftContractPagedCollectionContract schema from AeroDataBox API
layout: schema
name: AircraftContractPagedCollectionContract
properties_list:
- description: The total number of items across all pages
  name: totalCount
  type: integer
- description: The offset of the current page of the collection (number of items skipped before this page)
  name: pageOffset
  type: integer
- description: Maximum number of items on the current page of the collection (`Count` cannot be more than this value)
  name: pageSize
  type: integer
- description: This value is true when collection has more pages
  name: hasNextPage
  type: boolean
- description: The number of items in the collection
  name: count
  type: integer
- description: The collection of items
  name: items
  type: array
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-aircraft-contract-paged-collection-contract-schema.json
slug: aerodatabox-aircraft-contract-paged-collection-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: AircraftContractPagedCollectionContract
---
