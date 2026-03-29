---
aid: crossref:crossref-get-journals
name: GET /journals
tags:
- Journals
humanURL: 
properties: []
description: >-
  Return a list of journals in the Crossref database. ## Queries  Free form search queries can be made, for example, journals that include `pharmacy` and `health`:  ##  ``` /journals?query=pharmacy+health ```   ## Pagination with offsets  Offsets can be used to iterate over the results. For this route, the maximum number of available results is 80,000, which in this case allows to retrieve all the indexed items. This limit applies to the sum of values of parameters `offset` + `rows`.  ##  The n...

---
