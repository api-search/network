---
aid: car-api:car-api-makemodelsindexget
name: Get Models
tags:
- Models
humanURL: 
properties: []
description: >-
  Search models by year, make, model, trim or make_id.  To include the models make in the description request with the query parameter as `verbose=yes`.  For complex queries you may use the json field to send an array of URL encoded JSON conditions, example:  `[{"field": "make", "op": "in", "val": ["Ford", "Acura"]}, {"field": "year", "op": ">=", "val": 2010}]`  JSON operators: `=`, `!=`, `>`, `<`, `>=`, `<=`, `in`, `not in`, `like`, `not like`, `not null`, and `is null`.  JSON search fields:  ...

---
