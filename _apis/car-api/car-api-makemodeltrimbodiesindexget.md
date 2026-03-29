---
aid: car-api:car-api-makemodeltrimbodiesindexget
name: Search vehicle bodies
tags:
- Bodies
humanURL: 
properties: []
description: >-
  To include additional information about the returned body (such as year, make, model and trim) request with the query parameter as `verbose=yes`.  For complex queries you may use the json field to send an array of URL encoded JSON conditions, example:  `[{"field": "doors", "op": ">=", "val": 4}, {"field": "type", "op": "in", "val": ["SUV","Van"]}]`  See `/api/vehicle-attributes` for a complete list of vehicle attributes.  JSON operators: `=`, `!=`, `>`, `<`, `>=`, `<=`, `in`, `not in`, `like`...

---
