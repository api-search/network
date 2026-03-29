---
aid: car-api:car-api-makemodeltrimsindexget
name: Search trims
tags:
- Trims
humanURL: 
properties: []
description: >-
  To include additional information about the returned body (such as year, make, model and trim) request with the query parameter as `verbose=yes`.  For complex queries you may use the json field to send an array of URL encoded JSON conditions, example:  `[{"field": "year", "op": ">=", "val": 2010}, {"field": "year", "op": "<=", "val": 2020}]`  JSON operators: `=`, `!=`, `>`, `<`, `>=`, `<=`, `in`, `not in`, `like`, `not like`, `not null`, and `is null`.  JSON search fields:  `year`, `make`, `m...

---
