---
aid: vtex:vtex-scrolldocuments
name: VTex Scroll documents
tags:
- Scroll
humanURL: 
properties: []
description: >-
  If you need to query the entire VTEX Master Data database, or your collection is over 10.000 documents, use this endpoint.  In the first request, the `X-VTEX-MD-TOKEN` token will be returned in the header. This token must be passed to the next request in the query string `_token` parameter. The token has a timeout of 10 minutes, which refreshes after each request.  After the token is obtained, it is no longer necessary to send the filter or document size per page parameters. You only need...

---
