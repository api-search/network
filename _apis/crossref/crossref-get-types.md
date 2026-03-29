---
aid: crossref:crossref-get-types
name: GET /types
tags:
- Types
humanURL: 
properties: []
description: >-
  Returns a list of valid work types. ## Pagination with offsets  Offsets can be used to iterate over the results. For this route, the maximum number of available results is 80,000, which in this case allows to retrieve all the indexed items. This limit applies to the sum of values of parameters `offset` + `rows`.  ##  The number of items returned in a single response is controlled by `rows` parameter (default is 20, and maximum is 1,000). To limit results to 5, for example, you could do the fo...

---
