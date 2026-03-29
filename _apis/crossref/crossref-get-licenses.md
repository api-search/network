---
aid: crossref:crossref-get-licenses
name: GET /licenses
tags:
- Licenses
humanURL: 
properties: []
description: >-
  Returns a list of licenses. ## Querying  This endpoint accepts `query` parameter, which allows for free text querying. The result contains aggregated licenses from the works that match given query.  ##  For example, this request:  ##  ``` /licenses?query=richard+feynman ```  ##  will first select works matching `richard+feynman`, and aggregate their licenses.  ## Pagination with offsets  Offsets are an easy way to iterate over results sets up to 10,000 items. This limit applies to the sum of ...

---
