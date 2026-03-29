---
aid: factset:factset-getcargoendpoint
name: Gets an object given an ID. In this case ID retrieved from mapping Location header, object data in response body.
tags:
- Analytics
- Cargo
- Groups
- Objects
humanURL: 
properties: []
description: >-
  Raw object data can be found in the response body. This can be either the mapped PDF/PPT or STACH json, depending on the mapping. https://pages.github.factset.com/analytics-reporting/stachschema/#/   Optional request header "accept-encoding", with allowed values of "br" and "gzip". If accept-encoding is passed, the response is compressed.

---
