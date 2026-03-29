---
aid: car-api:car-api-makemodeltrimmileagesindexget
name: Search vehicle mileages
tags:
- Mileages
humanURL: 
properties: []
description: >-
  To include additional information about the returned body (such as year, make, model and trim) request with the query parameter as `verbose=yes`.  For complex queries you may use the json field to send an array of URL encoded JSON conditions, example:  `[{"field": "combined_mpg", "op": ">=", "val": 20}, {"field": "combined_mpg", "op": "<=", "val": 30}]`  JSON operators: `=`, `!=`, `>`, `<`, `>=`, `<=`, `in`, `not in`, `like`, `not like`, `not null`, and `is null`.  JSON search fields:  `year`...

---
