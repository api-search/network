---
aid: elsevier:elsevier-scival-api
name: Elsevier SciVal API
tags: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://dev.elsevier.com/scival_apis.html
overlays:
  - url: overlays/https://dev.elsevier.com/elsdoc/scival-openapi-search.yml
    type: APIs.io Search
properties:
  - url: https://dev.elsevier.com/scival.html
    type: Documentation
  - url: https://dev.elsevier.com/elsdoc/scival
    type: OpenAPI
description: |+

  The SciVal API gives access to a comprehensive basket of metrics for
  researchers (Scopus Author profiles) and all 8,500+ institutions available
  in SciVal, Elsevier's platform for research performance benchmarking. It
  returns metrics from SciVal for a given a Scopus Author or Institution
  identifier (or multiples of each).




---