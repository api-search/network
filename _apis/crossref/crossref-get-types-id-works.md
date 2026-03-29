---
aid: crossref:crossref-get-types-id-works
name: GET /types/{id}/works
tags:
- Types
- Works
humanURL: 
properties: []
description: >-
  returns list of works of type {id}. ## Queries  Free form search queries can be made, for example, works that include `renear` or `ontologies` (or both):  ##  ``` /works?query=renear+ontologies ```   ## Field Queries Field queries allow for queries that match only particular fields of metadata. For example, this query matches records that contain the tokens `richard` or `feynman` (or both) in any author field:  ##  ``` /works?query.author=richard+feynman ```  ##  Field queries can be combined...

---
