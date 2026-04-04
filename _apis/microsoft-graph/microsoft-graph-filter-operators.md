---
aid: microsoft-graph:microsoft-graph-filter-operators
name: Microsoft Graph Filter Operators
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/filteroperators-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph filter operators are the OData $filter expressions you add to
  Graph API requests to narrow results on the server before theyre returned.
  They let you select only the resources that match certain criteriasuch as
  equality and comparison checks (eq, ne, gt, ge, lt, le), logical combinations
  (and, or, not), string matching (startswith, endswith, contains), membership
  tests (in), and collection predicates (any, all). Using filters reduces
  payload size and improves performance by avoiding clientside postprocessing.
  Support for specific operators varies by resource and property (not all fields
  are filterable), and some advanced scenarioslike filtering on certain
  directory properties or using $count with filtersrequire the ConsistencyLevel:
  eventual header.

---