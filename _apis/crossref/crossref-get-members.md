---
aid: crossref:crossref-get-members
name: GET /members
tags:
- Members
humanURL: 
properties: []
description: >-
  Returns a list of all Crossref members (mostly publishers). ## Queries  Free form search queries can be made, for example, funders that include `association` and `library`:  ##  ``` /members?query=association+library ```   ## Filters  Filters allow you to select items based on specific criteria. All filter results are lists.  ##  Example:  ## ``` /members?filter=current-doi-count:0 ``` ##  ### Multiple filters  Multiple filters can be specified in a single query. In such a case, different fil...

---
