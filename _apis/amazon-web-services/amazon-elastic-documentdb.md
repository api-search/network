---
aid: amazon-web-services:amazon-elastic-documentdb
name: Amazon Elastic DocumentDB
tags:
  - ARN
  - Cluster
  - Clusters
  - Resources
  - Restore
  - Snapshots
  - Tags
  - Untag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: >-

  https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-using-elastic-clusters.html
overlays:
  - url: overlays/docdb-elastic-openapi-search.yml
    type: APIs.io Search
  - url: overlays/docdb-elastic-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: >-

      https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-using-elastic-clusters.html
    type: Documentation
  - url: openapi/docdb-elastic-openapi-original.yml
    type: OpenAPI
description: |-

  The Amazon DocumentDB API offers elastic clusters that can handle high
  volumes of reads/writes per second and store petabytes of data. These
  clusters make it easier for developers to work with Amazon DocumentDB by
  removing the need to select, oversee, or update instances.

---