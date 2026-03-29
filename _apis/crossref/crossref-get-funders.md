---
aid: crossref:crossref-get-funders
name: GET /funders
tags:
- Funders
humanURL: 
properties: []
description: >-
  Returns a list of all funders in the [Funder Registry](https://gitlab.com/crossref/open_funder_registry). ## Queries  Free form search queries can be made, for example, funders that include `research` and `foundation`:  ##  ``` /funders?query=research+foundation ```   ## Filters  Filters allow you to select items based on specific criteria. All filter results are lists.  ##  Example:  ## ``` /funders?filter=location:Spain ``` ##  This endpoint supports the following filters:  ##  + `location`...

---
