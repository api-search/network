---
aid: amazon-neptune:amazon-neptune-executegremlintraversal
name: Execute a Gremlin traversal via HTTP POST
tags:
- Query
humanURL: 
properties: []
description: >-
  Submits a Gremlin traversal query to the Neptune HTTP REST endpoint. The query is provided as a JSON body with a gremlin property containing the traversal string. All results are returned in a single JSON response by default. For large result sets, chunked responses can be enabled to avoid OutOfMemoryError.

---
