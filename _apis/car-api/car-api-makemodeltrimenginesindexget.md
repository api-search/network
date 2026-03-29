---
aid: car-api:car-api-makemodeltrimenginesindexget
name: Search vehicle engines
tags:
- Engines
humanURL: 
properties: []
description: >-
  To include additional information about the returned body (such as year, make, model and trim) request with the query parameter as `verbose=yes`.  For complex queries you may use the json field to send an array of URL encoded JSON conditions, example:  `[{"field": "horsepower_hp", "op": ">=", "val": 100}, {"field": "horsepower_hp", "op": "<=", "val": 300}]`  See `/api/vehicle-attributes` for a complete list of vehicle attributes.  JSON operators: `=`, `!=`, `>`, `<`, `>=`, `<=`, `in`, `not in...

---
