---
aid: crossref:crossref-get-journals-issn-works
name: GET /journals/{issn}/works
tags:
- Journals
- Works
humanURL: 
properties: []
description: >-
  Returns a list of works in the journal identified by {issn}. ## Queries  Free form search queries can be made, for example, works that include `renear` or `ontologies` (or both):  ##  ``` /works?query=renear+ontologies ```   ## Field Queries Field queries allow for queries that match only particular fields of metadata. For example, this query matches records that contain the tokens `richard` or `feynman` (or both) in any author field:  ##  ``` /works?query.author=richard+feynman ```  ##  Fiel...

---
